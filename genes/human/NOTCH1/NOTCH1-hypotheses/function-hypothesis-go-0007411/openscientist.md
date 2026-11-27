---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-20T18:11:33.712800'
end_time: '2026-09-20T18:23:13.609619'
duration_seconds: 699.9
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: human
  gene: NOTCH1
  gene_symbol: NOTCH1
  uniprot_accession: P46531
  taxon_id: NCBITaxon:9606
  taxon_label: Homo sapiens
  focus_type: function_assignment
  hypothesis_slug: function-hypothesis-go-0007411
  hypothesis_text: Human NOTCH1 participates in axon guidance (GO:0007411). Evaluate
    direct axon pathfinding/patterning evidence independently of changes in neuronal
    fate, neurite length and survival. Assess conservation of noncanonical Notch/Abl
    signaling demonstrated in Drosophila, distinguishing it from SLIT/ROBO signaling
    and from canonical nuclear Notch signaling. Establish whether the gene product
    performs a guidance-relevant mechanistic step. A questionable cross-family annotation
    source does not itself disprove the target's biology, and absence of a human assay
    is not sufficient to refute an appropriately supported conserved function.
  term_context: No specific term context supplied.
  reference_context: No specific reference context supplied.
  source_file: genes/human/NOTCH1/NOTCH1-ai-review.yaml
  source_selector: free-text
  source_context_yaml: "hypothesis: Human NOTCH1 participates in axon guidance (GO:0007411).\
    \ Evaluate direct axon pathfinding/patterning\n  evidence independently of changes\
    \ in neuronal fate, neurite length and survival. Assess conservation\n  of noncanonical\
    \ Notch/Abl signaling demonstrated in Drosophila, distinguishing it from SLIT/ROBO\
    \ signaling\n  and from canonical nuclear Notch signaling. Establish whether the\
    \ gene product performs a guidance-relevant\n  mechanistic step. A questionable\
    \ cross-family annotation source does not itself disprove the target's\n  biology,\
    \ and absence of a human assay is not sufficient to refute an appropriately supported\
    \ conserved\n  function.\nfocus_type: function_assignment\ncontext: []\nreference_id:\
    \ []"
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
- filename: NOTCH1_GO0007411_evidence_matrix.csv
  path: openscientist_artifacts/NOTCH1_GO0007411_evidence_matrix.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist NOTCH1 GO0007411 evidence matrix
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
- **Gene directory:** NOTCH1
- **Gene symbol:** NOTCH1
- **UniProt accession:** P46531

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** function-hypothesis-go-0007411
- **Source file:** genes/human/NOTCH1/NOTCH1-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

Human NOTCH1 participates in axon guidance (GO:0007411). Evaluate direct axon pathfinding/patterning evidence independently of changes in neuronal fate, neurite length and survival. Assess conservation of noncanonical Notch/Abl signaling demonstrated in Drosophila, distinguishing it from SLIT/ROBO signaling and from canonical nuclear Notch signaling. Establish whether the gene product performs a guidance-relevant mechanistic step. A questionable cross-family annotation source does not itself disprove the target's biology, and absence of a human assay is not sufficient to refute an appropriately supported conserved function.

## Term and Decision Context

No specific term context supplied.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: Human NOTCH1 participates in axon guidance (GO:0007411). Evaluate direct axon pathfinding/patterning
  evidence independently of changes in neuronal fate, neurite length and survival. Assess conservation
  of noncanonical Notch/Abl signaling demonstrated in Drosophila, distinguishing it from SLIT/ROBO signaling
  and from canonical nuclear Notch signaling. Establish whether the gene product performs a guidance-relevant
  mechanistic step. A questionable cross-family annotation source does not itself disprove the target's
  biology, and absence of a human assay is not sufficient to refute an appropriately supported conserved
  function.
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

# NOTCH1 (human, P46531) — Axon Guidance (GO:0007411) Function-Assignment Review

**Focus:** function_assignment · `function-hypothesis-go-0007411`
**Source:** genes/human/NOTCH1/NOTCH1-ai-review.yaml
**Iteration:** 3 of 3 (final)

---

## Executive Judgment

**Verdict: Partially supported / weakly supported — retain only as a non-core, phylogenetically-inferred BP annotation with an explicit caveat; do NOT treat as a direct, experimentally-established human function.**

The seed hypothesis is correct on two points and unproven on the decisive one:

1. **A genuine, guidance-specific Notch mechanism exists** — but it has been demonstrated only in *Drosophila*. Notch controls axon growth and guidance through a **noncanonical, Su(H)-independent pathway** using the Abl tyrosine kinase, the adaptor Disabled, the GEF Trio, and Rac GTPase (PMID:18062953, 21246649, 29343637). This is mechanistically distinct from SLIT/ROBO and from canonical nuclear Notch, exactly as the hypothesis states, and it is separable from neuronal fate.
2. **The "questionable cross-family annotation source" is real and confirmed.** The human NOTCH1 → GO:0007411 record is an **IBA/PAINT phylogenetic inference** (ECO:0000318, GO_REF:0000033, GO_Central), not a human experiment. Its `withFrom` support set mixes legitimate Notch orthologs (fly Notch FBgn0264089; mouse Notch MGI:1315202/3/5) **with human SLIT1/SLIT2/SLIT3** (O75093/O75094/O94813) — a distinct SLIT/ROBO ligand family. So SLIT cross-family contamination materially contributed to the propagation.
3. **The decisive gap:** there is **no direct human/vertebrate axon-*pathfinding* evidence.** The only documented mammalian NOTCH1 neuronal phenotype is **inhibition of neurite outgrowth / neurite morphology** via canonical CBF1 signaling (PMID:10465425) — a length/morphology effect the hypothesis explicitly asks to *exclude* from guidance evidence. Mammalian noncanonical Notch does exist in neurons but has been mapped to a different output (synaptic-vesicle protein expression, PMID:27040987). A computed STRING v12 check found **no curated interaction** between human NOTCH1 and the Abl/Trio/Rac module (the NOTCH1–ABL1 edge is text-mining-driven: tscore 0.596, escore 0.113, dscore 0).

**Bottom line for the curator:** The hypothesis's principled stance — that a bad annotation source and the absence of a human assay do not by themselves refute a conserved function — is fair. But "not refuted" is not "supported." The affirmative evidence is entirely *Drosophila*, the human annotation is inference contaminated by a paralogous family, and the accessible human data point *away* from directional guidance and toward neurite morphology/fate. The term should be retained at most as a **non-core, inferred** annotation with a caveat, or generalized; it should **not** be presented as a demonstrated core human function.

---

## Evidence Matrix

| Citation | Evidence type | Direction | Claim tested | Key finding | Context | Confidence & limitations |
|---|---|---|---|---|---|---|
| QuickGO / GO_Central (GO_REF:0000033) | Computational / database (IBA) | Qualifies | Is the human annotation experiment-based? | IBA phylogenetic annotation; `withFrom` mixes fly/mouse Notch with human **SLIT1/2/3** | Human P46531, PAINT | High (direct DB pull); confirms propagation + cross-family contamination |
| PMID:18062953 | Direct assay + mutant phenotype | Supports (fly) | Does Notch perform guidance via a guidance-specific step? | Notch directs axon growth/guidance via **Su(H)-independent Abl/Disabled/Trio** pathway; separable from cell fate | *Drosophila* CNS/motor axons | High; organism = fly, not human |
| PMID:21246649 | Mutant phenotype / genetic | Supports (fly) | What is the guidance effector step? | **Rac** (via Trio GEF1) is the crucial Rho GTPase in noncanonical Notch/Abl guidance | *Drosophila* motor neurons | High; fly-specific |
| PMID:29343637 | Direct assay | Supports (fly) | Receptor-proximal requirements? | **Tyrosine phosphorylation + proteolytic cleavage** of Notch required for noncanonical Notch/Abl axon patterning | *Drosophila* | High; fly-specific |
| PMID:10465425 | Direct assay (overexpression) | Competing / qualifies | What does mammalian Notch1 do in neurons? | Notch1 **inhibits neurite outgrowth / morphology** via **CBF1 (canonical)**; blocked by Numb | Mouse primary cortical/hippocampal neurons | High; measures neurite length/morphology, **not** directional guidance |
| PMID:27040987 | Direct assay / genetic | Qualifies | Does mammalian noncanonical Notch exist, and its output? | γ-secretase/CBF1-independent Notch controls **synaptic-vesicle protein expression** | Mouse postmitotic neurons | High; mammalian noncanonical Notch is real but output ≠ axon guidance |
| STRING v12 (computed this run) | Computational / interaction | Qualifies / refutes-coupling | Does human NOTCH1 couple to Abl/Trio/Rac? | **No** ABL1/TRIO/DAB1/RAC1 in top-80 partners; NOTCH1–ABL1 edge text-mining-driven (t=0.596, e=0.113, d=0) | Human 9606 | Medium; DB absence ≠ proof of no interaction |

*Provenance artifacts:* `NOTCH1_GO0007411_evidence_matrix.csv` (this run); QuickGO and STRING API calls executed live in iterations 1–2.

---

## GO Curation Implications (leads — require curator verification)

| GO ID | Term | Aspect | Current evidence | Recommended action (lead) | Rationale |
|---|---|---|---|---|---|
| GO:0007411 | axon guidance | BP | IBA (ECO:0000318) | **Retain as non-core inferred, add caveat — OR generalize** | No direct human/vertebrate pathfinding evidence; support set SLIT-contaminated; conserved fly mechanism unverified in human |

- The evidence supports a **BP** term at most, not an MF. Do **not** downgrade to "protein binding."
- **Do not present as a core function.** If the review pipeline distinguishes core vs. non-core, mark axon guidance **non-core** for human NOTCH1.
- If a curator wants to preserve the conserved biology without over-claiming the human protein, an acceptable lead is to keep GO:0007411 **only** with the IBA evidence code and a note that the phylogenetic support is partly cross-family (SLIT), OR generalize to a less specific neuronal-development term that the mammalian data actually support (e.g., regulation of neuron differentiation / regulation of neuron projection development — curator to verify exact ID).
- **Flag the PAINT annotation to GO_Central**: the `withFrom` inclusion of SLIT1/2/3 in a Notch-family propagation is a likely tree/family-grouping artifact worth reporting.

---

## Mechanistic Scope

- **Immediate molecular step being tested (fly):** transmembrane Notch receptor, after tyrosine phosphorylation and cleavage, physically associates with Disabled and Trio and activates Rac to remodel the growth-cone cytoskeleton — a *bona fide* guidance-relevant step, independent of Su(H)/CBF1 transcription (PMID:18062953, 21246649, 29343637).
- **Downstream / excluded phenotypes:** neuronal fate specification (canonical Notch), neurite outgrowth length and branching (mammalian PMID:10465425), survival, and disease phenotypes. These are explicitly outside the guidance claim and, for human, are the *only* things actually observed.
- **Directionality distinction:** "axon guidance" (GO:0007411) means directional pathfinding/patterning. Mammalian NOTCH1 data show a scalar effect on neurite length/morphology, not steering — an important curation distinction.

---

## Conflicts and Alternatives

1. **Cross-family (paralog/family) confusion:** SLIT1/2/3 in the IBA `withFrom` set means part of the "axon guidance" signal came from the true SLIT/ROBO guidance ligands, not from Notch biology — classic annotation carry-over.
2. **Organism-specific difference:** The guidance mechanism is demonstrated in *Drosophila*; the mammalian ortholog's documented neuronal action (neurite inhibition via CBF1) is a *different* pathway output.
3. **Canonical vs. noncanonical:** The human annotation does not specify the noncanonical mechanism; a naive reader could conflate it with canonical Notch, which is not what the fly guidance work shows.
4. **Interaction-data gap:** No curated human NOTCH1–ABL1/TRIO/DAB1/RAC1 interaction; the apparent link is literature co-mention, not experiment.

---

## Knowledge Gaps

| Gap | What was checked | Why it matters | What would resolve it |
|---|---|---|---|
| No human/vertebrate axon-pathfinding assay for NOTCH1 | PubMed (multiple queries) — none found | Decides whether the term is a demonstrated human function | In vivo/vitro growth-cone turning or commissural/RGC pathfinding assay with NOTCH1 perturbation |
| Human NOTCH1↔Abl/Trio/Rac coupling | STRING v12 (computed) — no curated edge | Tests whether the conserved mechanism operates in human | Co-IP/proximity labeling of NOTCH1 with ABL1/TRIO/DAB1 in human neurons |
| Conservation of the fly Notch phospho-tyrosine/cleavage guidance determinants in human NOTCH1 | Not directly aligned this run (time-limited) | Sequence conservation would strengthen "could perform the step" | Alignment of the Drosophila Notch ICD tyrosine sites/Dab-binding region to P46531 |
| PANTHER family PTN002911625 composition | Inferred from `withFrom` (contains SLIT + Notch) | Confirms the cross-family grouping causing over-propagation | Direct inspection of the PANTHER tree/family membership |

---

## Discriminating Tests

1. **Growth-cone turning / directional pathfinding assay** with human NOTCH1 gain/loss (and a Su(H)/RBPJ-uncoupled allele) to separate guidance from neurite length and fate.
2. **Interaction mapping** (co-IP, BioID/APEX) of human NOTCH1 with ABL1, TRIO, DAB1, RAC1 in neurons to test whether the noncanonical module is engaged.
3. **Structure-function**: express a human NOTCH1 carrying the Drosophila Dab-binding/tyrosine determinants vs. wild type; test rescue of a guidance phenotype.
4. **Vertebrate in vivo**: zebrafish/mouse notch1 conditional knockdown in a defined tract (e.g., commissural or motor axons) scored for pathfinding errors distinct from proliferation/fate.
5. **Sequence/orthology**: align P46531 ICD to Drosophila Notch guidance determinants; report conservation conservatively.

---

## Curation Leads (require curator verification)

- **Action lead:** Change GO:0007411 from an unqualified functional claim to an **IBA, non-core, caveated** annotation — or generalize to a neuronal-development term the mammalian data support. Do **not** record axon guidance as a demonstrated core human function.
- **Reference leads with exact snippets to verify:**
  - PMID:18062953 — "*Notch directs axon growth and guidance in Drosophila via a "non-canonical", i.e. non-Su(H)-mediated, signaling pathway, characterized by association with the adaptor protein, Disabled, and Trio, an accessory factor of the Abl tyrosine kinase*" (establishes fly guidance mechanism).
  - PMID:21246649 — "*it is the crucial Rho GTPase in "noncanonical" Notch/Abl signaling*" (Rac effector step).
  - PMID:10465425 — "*Transfection at two days in vitro with full length Notch1 inhibited neurite outgrowth*" (mammalian effect is neurite length, not guidance).
  - PMID:27040987 — "*a novel Notch signaling is involved in expression of synaptic proteins in postmitotic neurons*" (mammalian noncanonical Notch output ≠ guidance).
- **Database lead:** Report to GO_Central that the NOTCH1 GO:0007411 PAINT `withFrom` set includes human SLIT1/2/3, indicating cross-family over-propagation.
- **Suggested curator questions:** (a) Is there any vertebrate in vivo axon-pathfinding phenotype for notch1 not attributable to fate/proliferation? (b) Does the review pipeline want to keep conserved-but-untested functions as IBA-only with caveats?
- **Suggested experiments:** items 1–3 under Discriminating Tests.

---

## Limitations

- Three-iteration budget; PubMed queries intermittently rate-limited and some returned no hits (may under-sample vertebrate literature).
- Sequence-level conservation of the specific fly guidance determinants was not aligned in this run (flagged as a gap).
- STRING absence of an edge is suggestive, not proof, of no interaction.
- Local repository `*-bioinformatics` analyses were intentionally withheld and not consulted.


## Artifacts

- [OpenScientist NOTCH1 GO0007411 evidence matrix](openscientist_artifacts/NOTCH1_GO0007411_evidence_matrix.csv)
- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)