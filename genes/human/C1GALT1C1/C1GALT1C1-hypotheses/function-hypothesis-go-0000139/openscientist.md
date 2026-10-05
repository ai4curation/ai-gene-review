---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-17T05:31:55.028298'
end_time: '2026-09-17T05:42:39.569222'
duration_seconds: 644.54
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: human
  gene: C1GALT1C1
  gene_symbol: C1GALT1C1
  uniprot_accession: Q96EU7
  taxon_id: NCBITaxon:9606
  taxon_label: Homo sapiens
  focus_type: function_assignment
  hypothesis_slug: function-hypothesis-go-0000139
  hypothesis_text: C1GALT1C1 has Golgi membrane (GO:0000139).
  term_context: '- Term: Golgi membrane (GO:0000139)

    - Evidence type: TAS

    - Original reference: Reactome:R-HSA-1964505'
  reference_context: '- Reactome:R-HSA-1964505

    - PMID:37216524'
  source_file: genes/human/C1GALT1C1/C1GALT1C1-ai-review.yaml
  source_selector: existing_annotations[1].function_hypothesis
  source_context_yaml: "term:\n  id: GO:0000139\n  label: Golgi membrane\nevidence_type:\
    \ TAS\noriginal_reference_id: Reactome:R-HSA-1964505"
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
artifact_count: 3
artifact_sources:
  openscientist_artifacts_zip: 3
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
- filename: go_decision_table.csv
  path: openscientist_artifacts/go_decision_table.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist go decision table
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
- **Gene directory:** C1GALT1C1
- **Gene symbol:** C1GALT1C1
- **UniProt accession:** Q96EU7

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** function-hypothesis-go-0000139
- **Source file:** genes/human/C1GALT1C1/C1GALT1C1-ai-review.yaml
- **Source selector:** existing_annotations[1].function_hypothesis

## Seed Hypothesis

C1GALT1C1 has Golgi membrane (GO:0000139).

## Term and Decision Context

- Term: Golgi membrane (GO:0000139)
- Evidence type: TAS
- Original reference: Reactome:R-HSA-1964505

## Reference Context

- Reactome:R-HSA-1964505
- PMID:37216524

## Source Context YAML

```yaml
term:
  id: GO:0000139
  label: Golgi membrane
evidence_type: TAS
original_reference_id: Reactome:R-HSA-1964505
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

# C1GALT1C1 (Cosmc) — Golgi membrane (GO:0000139) function-assignment review

**Gene:** C1GALT1C1 (Cosmc), Homo sapiens, UniProt Q96EU7
**Seed hypothesis:** C1GALT1C1 has Golgi membrane (GO:0000139)
**Evidence type / reference under review:** TAS, Reactome:R-HSA-1964505 (co-ref PMID:37216524)
**Focus:** function-assignment — does the gene product directly have this CC term?

---

## Executive Judgment

**Verdict: Refuted / over-annotated (for the direct-localization claim).**

C1GALT1C1 encodes **Cosmc**, the C1GALT1-specific molecular chaperone. Multiple
independent primary studies establish that **Cosmc is an endoplasmic-reticulum
(ER)-resident single-pass type II membrane protein**, and one study maps a
specific **ER-retention determinant to its transmembrane domain**. It is the
*client* enzyme it chaperones — **T-synthase / C1GALT1 — that resides in the
Golgi**, not Cosmc itself.

The GO:0000139 (Golgi membrane) annotation is **TAS from Reactome:R-HSA-1964505**,
a pathway model of Golgi-lumenal O-glycosylation. It is best explained as a
**compartment carry-over**: Reactome assigns the Golgi compartment to the
glycosylation reaction and its participants, and Cosmc — a regulator/client-folding
factor mentioned in that pathway context — inherited the Golgi-membrane location.
UniProt's own subcellular-location statement is deliberately conservative ("Membrane;
Single-pass type II membrane protein") and does **not** assert Golgi.

**Most important caveat:** No paper directly demonstrates Golgi residence of Cosmc,
so the annotation is not experimentally grounded; conversely, direct ER localization
is well supported. The safest curation action is to **replace GO:0000139 with the
ER membrane term (GO:0005789)**. A minor caveat is that UniProt itself has not (yet)
attached an ER-membrane GO CC term to Q96EU7, so a curator should add it from the
primary literature.

---

## Evidence Matrix

| Citation | Evidence type | Supports/Refutes/Qualifies | Claim tested | Key finding | Context | Confidence & limitations |
|---|---|---|---|---|---|---|
| PMID:18695044 (Ju et al., J Cell Biol 2008) | Localization + interaction (direct assay) | **Refutes** Golgi; supports ER | Where does Cosmc reside? | "Cosmc is an endoplasmic reticulum (ER)-localized … chaperone that binds directly to human T-synthase"; T-synthase "resides in the Golgi apparatus" | Human cells; T-synthase folding | High. Foundational paper; clearly separates Cosmc (ER) from client (Golgi). |
| PMID:21262965 (Sun et al., J Biol Chem 2011) | Structural/mutagenesis localization | **Refutes** Golgi; supports ER | Determinant of Cosmc localization | 18-aa TMD "is essential for ER localization and confers ER retention"; TMD Cys required for dimer/ER retention | Chimera & mutant studies | High. Mechanistic ER-retention motif; steady-state ER residence. |
| PMID:19923218 (Aryal et al., J Biol Chem 2010) | Direct in-vitro chaperone assay | **Refutes** Golgi; supports ER | Cosmc identity/location | "an endoplasmic reticulum-localized molecular chaperone termed Cosmc" | In vitro folding of T-synthase | High. Independent reaffirmation of ER localization. |
| PMID:12122208 (Ju & Cummings, PNAS 2002) | Discovery/functional | Qualifies (function, not location) | Cosmc function | Cosmc is the unique chaperone required for T-synthase activity | Human/mammalian | High for function; establishes chaperone role. |
| PMID:37216524 (Erger et al., 2023) | Mutant phenotype (human disease) | Qualifies (chaperonopathy) | Cosmc as chaperone in disease | Germline C1GALT1C1 defect = congenital disorder of glycosylation via reduced T-synthase activity | Human patients | High for chaperone role; not a localization study. Co-reference of the annotation. |
| UniProt Q96EU7 (database) | Database/topology | Qualifies | Topology & existing CC terms | SL comment is an **inference (ECO:0000305)**: only "Membrane; Single-pass type II membrane protein" (cyto 1–6, TM 7–26, lumenal 27–318). CC keywords list only "Membrane" — **no ER and no Golgi keyword**; function hedged as "Probable chaperone". GO CC = GO:0000139 (TAS:Reactome), GO:0070062 exosome (HDA) | Curated record | Medium. UniProt is agnostic and does **not** assert Golgi; Golgi term is the Reactome TAS in question. |
| Human Protein Atlas (C1GALT1C1) | Localization (antibody IF, database) | **Refutes/Qualifies** Golgi | Independent IF localization | Subcellular main location = **"Vesicles"** — not Golgi | Human cell lines, antibody-based | Medium. Antibody IF; vesicular pattern, does not support Golgi; cannot alone resolve ER vs vesicles. |
| Reactome:R-HSA-1964505 | Pathway/database | **Competing / source of annotation** | Basis of GO:0000139 | Reaction = "C1GALT1 transfers Galactose to the Tn antigen forming Core 1 glycoproteins"; compartment = **Golgi membrane, Golgi lumen**. This is a **C1GALT1 (T-synthase) catalytic reaction**; Cosmc inherits the Golgi compartment by pathway association | Reactome ContentService (fetched this run) | Low as direct Cosmc-localization evidence; **confirmed compartment carry-over**. |
| Reactome fetch (this run) | Computational/database | **Refutes direct claim** | Origin of GO:0000139 | The Golgi term originates from the Golgi-resident client's reaction, not from Cosmc localization data | Programmatic API | High confidence in provenance; closes the carry-over loop. |

---

## GO Decision Table (leads — require curator verification)

| GO_ID | Label | Aspect | Evidence basis | Assessment | Curation lead |
|---|---|---|---|---|---|
| GO:0000139 | Golgi membrane | CC | Reactome TAS (R-HSA-1964505 = **C1GALT1 Golgi reaction**) | Pathway-compartment carry-over; no direct Cosmc evidence | **REMOVE or mark non-core** |
| GO:0005789 | endoplasmic reticulum membrane | CC | Primary lit PMID:18695044, 19923218, **21262965** (TMD ER-retention motif) | Best-supported direct localization | **ADD (IDA)** |
| GO:0070062 | extracellular exosome | CC | UniProt HDA proteomics | Secondary/high-throughput | Retain as non-core |
| GO:0051082 | unfolded protein binding | MF | Chaperone for T-synthase folding (PMID:19923218) | Direct chaperone activity | Consider ADD |
| GO:0006457 | protein folding | BP | Chaperone-assisted folding of C1GALT1 | Core process | Consider ADD |

*(Also saved as `go_decision_table.csv`.)*

## GO Curation Implications

- **Term class:** Cellular Component.
- **Lead (requires curator verification):** **Do not retain GO:0000139 (Golgi
  membrane) as a direct localization for Cosmc.** Replace with
  **GO:0005789 (endoplasmic reticulum membrane)** — consistent with type II
  single-pass topology and the mapped TMD ER-retention motif.
- **Rationale:** The Golgi term is TAS carried from a Reactome pathway whose
  compartment reflects the glycosylation reaction (Golgi lumen) and the client
  enzyme C1GALT1/T-synthase, **not** Cosmc's own residence. Multiple primary
  papers place Cosmc in the ER.
- **If retention is preferred by policy** (because Reactome TAS terms are not
  auto-removed): at minimum **add GO:0005789 with experimental support
  (e.g., IDA from PMID:21262965 / PMID:18695044)** and flag GO:0000139 as
  non-core / pathway-context. GO:0070062 (extracellular exosome, HDA) is likely
  a proteomics secondary observation and non-core.
- Avoid defaulting to "protein binding"; the informative, better-supported term
  is ER membrane (CC) plus the established MF/BP of chaperone activity for
  T-synthase folding (e.g., GO:0051082 unfolded protein binding / GO:0006486
  context via its client).

---

## Mechanistic Scope

- **Direct molecular function:** Cosmc is an ER-lumenal-facing type II membrane
  chaperone that binds nascent/partly denatured **T-synthase (C1GALT1)** and
  promotes its folding, preventing aggregation and ubiquitin-mediated
  degradation (PMID:18695044, PMID:19923218).
- **Direct location:** ER membrane, retained via its TMD (PMID:21262965).
- **Downstream / pathway consequence (NOT Cosmc's own location):** Properly
  folded T-synthase traffics to and functions in the **Golgi**, synthesizing the
  core 1 O-glycan (T-antigen). Golgi is where the *product* enzyme acts — this is
  the effect that Reactome's Golgi compartment captures, and the likely origin of
  the Golgi mis-assignment to Cosmc.
- **Disease manifestation (downstream):** Loss/mutation of Cosmc → Tn syndrome /
  congenital disorder of glycosylation (PMID:37216524) — a phenotype of impaired
  chaperone function, not evidence of Golgi residence.

---

## Conflicts and Alternatives

- **Compartment carry-over (most likely):** Reactome models the O-glycosylation
  reaction in the Golgi; Cosmc inherits "Golgi membrane" by pathway association.
- **Client/chaperone conflation:** T-synthase (Golgi) vs Cosmc (ER) are routinely
  discussed together; the Golgi location of the client can be mis-attributed to
  the chaperone.
- **Exosome annotation (GO:0070062):** high-throughput proteomics; not a
  functional localization and does not support Golgi.
- **Paralog note:** A paralog **C1GALT1C1L (Q6BAM2)** exists but is a distinct gene;
  the seed accession Q96EU7 is canonical Cosmc, so the Golgi term is not a paralog
  mixup — it is a same-gene pathway-compartment carry-over.
- **Reactome confirmation (this run):** R-HSA-1964505 is explicitly the *C1GALT1*
  Golgi galactosyltransferase reaction (compartment: Golgi membrane/lumen),
  confirming the Golgi CC term reflects the client enzyme's reaction, not Cosmc.
- **No isoform/organism conflict found:** ER localization is reported for human
  Cosmc; the mechanism (TMD ER-retention) is intrinsic to the protein sequence.
- **No primary paper places Cosmc in the Golgi** — the competing hypothesis (Golgi
  residence) lacks direct experimental support.

---

## Knowledge Gaps

1. **Absence of an ER-membrane GO CC term in UniProt for Q96EU7.** Checked UniProt
   JSON: only Golgi (TAS) and exosome (HDA) CC terms are present. Matters because a
   curator replacing the Golgi term needs a positive ER term with proper evidence
   codes. Resolution: attach GO:0005789 with IDA citing PMID:21262965 / PMID:18695044.
2. **Whether any Cosmc pool cycles to the ERGIC/cis-Golgi.** No evidence found for
   this; the TMD retention data argue against significant Golgi steady-state pools.
   Resolution: colocalization microscopy (Cosmc vs ER markers/calnexin vs Golgi
   markers/GM130) — already effectively addressed by prior ER-retention work.
3. **Policy question:** whether GO/Reactome TAS compartment terms should be
   auto-propagated to regulatory participants. Matters broadly for chaperones of
   Golgi enzymes. Resolution: curator/consortium policy decision.

---

## Discriminating Tests

- **Confocal colocalization / IF:** endogenous or tagged Cosmc vs ER (calnexin,
  PDI) and Golgi (GM130, TGN46) markers — expect ER, not Golgi (confirmatory).
- **Glycosidase sensitivity:** Endo H sensitivity of Cosmc N-glycans (if any) →
  ER-type high-mannose vs Golgi-processed complex glycans distinguishes compartment.
- **TMD swap experiments (already reported, PMID:21262965):** replacing Cosmc TMD
  with a non-ER TMD relocalizes it — direct causal test of ER retention.
- **Proximity labeling (BioID/APEX) from an ER-anchored vs Golgi-anchored bait**
  to define Cosmc's steady-state neighborhood.

---

## Curation Leads (require curator verification)

- **Action change:** Replace **GO:0000139 (Golgi membrane, TAS:Reactome)** →
  **GO:0005789 (endoplasmic reticulum membrane)** as the direct CC; or, if
  retaining, downgrade GO:0000139 to non-core/pathway-context and add GO:0005789.
- **Candidate references + exact snippets to verify:**
  - PMID:18695044 — "Cosmc is an endoplasmic reticulum (ER)-localized adenosine
    triphosphate binding chaperone that binds directly to human T-synthase";
    "Formation of active T-synthase, which resides in the Golgi apparatus,
    requires a unique molecular chaperone, Cosmc".
  - PMID:21262965 — "the 18 amino acid transmembrane domain (TMD) of Cosmc is
    essential for ER localization and confers ER retention to select chimeras".
  - PMID:19923218 — "an endoplasmic reticulum-localized molecular chaperone termed
    Cosmc".
- **Candidate replacement/added GO terms:** CC GO:0005789 (ER membrane);
  supporting MF GO:0051082 (unfolded protein binding); BP GO:0006457 (protein
  folding) / regulation of O-glycan biosynthesis via client.
- **Suggested curator questions:** (1) Is Reactome TAS compartment appropriate as
  a direct CC for a regulator whose client lives in that compartment? (2) Should
  GO:0070062 (exosome, HDA) be treated as non-core?
- **Suggested experiments:** ER/Golgi colocalization; Endo H assay; TMD-swap
  relocalization (confirmatory of published result).

---

## Provenance

- UniProt Q96EU7 programmatic fetch (execute_code, requests) returned:
  SL comment "Membrane; Single-pass type II membrane protein" (evidence
  ECO:0000305, i.e., curator inference); CC keyword only "Membrane" (no ER, no
  Golgi); function "Probable chaperone"; topology cyto 1–6 / TM 7–26 / lumenal
  27–318; GO CC = GO:0000139 (TAS:Reactome), GO:0070062 (HDA).
- Human Protein Atlas API (search_download) for C1GALT1C1 returned subcellular
  main location "Vesicles" (antibody-based IF) — not Golgi.
- QuickGO/EBI endpoint was unreachable during this run (connection timeout); the
  full GO annotation set could not be independently enumerated beyond UniProt's.
- Reactome ContentService fetch of R-HSA-1964505 (this run) returned displayName
  "C1GALT1 transfers Galactose to the Tn antigen forming Core 1 glycoproteins (T
  antigens)", schemaClass "Reaction", compartment ['Golgi membrane','Golgi lumen'].
- GO decision table saved as `go_decision_table.csv`.
- PubMed retrievals: PMID:18695044, 21262965, 19923218, 37216524.

*Independent-resource cross-check (Iteration 2): neither UniProt (agnostic
"Membrane", inferred) nor HPA (vesicular) supports Golgi residence; only Reactome
TAS does. This reinforces the over-annotation conclusion.*

*All localization conclusions are drawn from primary literature and the UniProt
record; the Golgi-inheritance interpretation is inference from the Reactome
compartment model and is labeled as such.*


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)
- [OpenScientist go decision table](openscientist_artifacts/go_decision_table.csv)