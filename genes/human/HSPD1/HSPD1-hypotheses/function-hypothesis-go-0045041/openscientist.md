---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-20T21:54:38.491795'
end_time: '2026-09-20T22:15:54.328280'
duration_seconds: 1275.84
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: human
  gene: HSPD1
  gene_symbol: HSPD1
  uniprot_accession: P10809
  taxon_id: NCBITaxon:9606
  taxon_label: Homo sapiens
  focus_type: function_assignment
  hypothesis_slug: function-hypothesis-go-0045041
  hypothesis_text: Human HSPD1/Hsp60 participates in protein import into the mitochondrial
    intermembrane space (GO:0045041). Trace IBA source PTN000143510 and yeast Hsp60
    SGD:S000004249. Compare primary PMID:1347713 antifolding/export results with PMID:7911803
    stop-transfer import experiments. Which protein substrates/routes require Hsp60,
    and does any demonstrated difference exclude conservation in human HSPD1? Distinguish
    chaperone contributions to translocation from folding after import. A matrix location
    does not itself preclude an intermembrane-space import role, and one experimentally
    grounded donor is not intrinsically weak.
  term_context: No specific term context supplied.
  reference_context: No specific reference context supplied.
  source_file: genes/human/HSPD1/HSPD1-ai-review.yaml
  source_selector: free-text
  source_context_yaml: "hypothesis: Human HSPD1/Hsp60 participates in protein import\
    \ into the mitochondrial intermembrane space\n  (GO:0045041). Trace IBA source\
    \ PTN000143510 and yeast Hsp60 SGD:S000004249. Compare primary PMID:1347713\n\
    \  antifolding/export results with PMID:7911803 stop-transfer import experiments.\
    \ Which protein substrates/routes\n  require Hsp60, and does any demonstrated\
    \ difference exclude conservation in human HSPD1? Distinguish\n  chaperone contributions\
    \ to translocation from folding after import. A matrix location does not itself\n\
    \  preclude an intermembrane-space import role, and one experimentally grounded\
    \ donor is not intrinsically\n  weak.\nfocus_type: function_assignment\ncontext:\
    \ []\nreference_id: []"
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
- filename: HSPD1_GO0045041_decision_table.csv
  path: openscientist_artifacts/HSPD1_GO0045041_decision_table.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist HSPD1 GO0045041 decision table
- filename: HSPD1_GO0045041_evidence_matrix.csv
  path: openscientist_artifacts/HSPD1_GO0045041_evidence_matrix.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist HSPD1 GO0045041 evidence matrix
- filename: HSPD1_GO0045041_provenance.json
  path: openscientist_artifacts/HSPD1_GO0045041_provenance.json
  media_type: application/json
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist HSPD1 GO0045041 provenance
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
- **Gene directory:** HSPD1
- **Gene symbol:** HSPD1
- **UniProt accession:** P10809

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** function-hypothesis-go-0045041
- **Source file:** genes/human/HSPD1/HSPD1-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

Human HSPD1/Hsp60 participates in protein import into the mitochondrial intermembrane space (GO:0045041). Trace IBA source PTN000143510 and yeast Hsp60 SGD:S000004249. Compare primary PMID:1347713 antifolding/export results with PMID:7911803 stop-transfer import experiments. Which protein substrates/routes require Hsp60, and does any demonstrated difference exclude conservation in human HSPD1? Distinguish chaperone contributions to translocation from folding after import. A matrix location does not itself preclude an intermembrane-space import role, and one experimentally grounded donor is not intrinsically weak.

## Term and Decision Context

No specific term context supplied.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: Human HSPD1/Hsp60 participates in protein import into the mitochondrial intermembrane space
  (GO:0045041). Trace IBA source PTN000143510 and yeast Hsp60 SGD:S000004249. Compare primary PMID:1347713
  antifolding/export results with PMID:7911803 stop-transfer import experiments. Which protein substrates/routes
  require Hsp60, and does any demonstrated difference exclude conservation in human HSPD1? Distinguish
  chaperone contributions to translocation from folding after import. A matrix location does not itself
  preclude an intermembrane-space import role, and one experimentally grounded donor is not intrinsically
  weak.
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

# AIGR Deep Research Report: HSPD1/Hsp60 and GO:0045041 (Protein Import into Mitochondrial Intermembrane Space)

**Gene:** HSPD1 (human), UniProt P10809
**Focus type:** function_assignment
**Hypothesis slug:** function-hypothesis-go-0045041
**Term under evaluation:** GO:0045041 — *protein import into mitochondrial intermembrane space*

---

## Summary

The seed hypothesis proposes that human HSPD1/Hsp60 directly participates in protein import into the mitochondrial intermembrane space (IMS), tracing the annotation through IBA source PANTHER node PTN000143510 and yeast Hsp60 (SGD:S000004249), and asks whether the difference between the antifolding/export result (PMID:1347713) and the stop-transfer import result (PMID:7911803) excludes conservation in human HSPD1. After tracing the annotation provenance and reconciling the primary literature, the evidence does **not** support treating GO:0045041 as a directly demonstrated, core function of human HSPD1. It is best treated as a **weakly supported, non-core, inference-only (IBA) term**.

Three facts drive this conclusion. First, the human annotation to GO:0045041 is **IBA-only** (phylogenetically inferred from a yeast ancestor via GO_Central); there is no human experimental (IDA/IMP/EXP) support, and every experimentally supported human HSPD1 term describes **matrix chaperonin folding**, with a primary location of mitochondrial matrix. Second, the single donor experiment (yeast, PMID:1347713) demonstrates only an **indirect, substrate-selective matrix "antifolding" role** in conservative sorting of cytochrome b2 — not a translocase or IMS-import activity — and is **directly contradicted on that same substrate** by PMID:7911803, which shows the b2-presequence passenger reaches the IMS **independently of hsp60** via inner-membrane stop-transfer. Third, the **dedicated IMS import machinery is the MIA40/CHCHD4–Erv1 disulfide relay**, not Hsp60.

The most important caveat is that human HSPD1 and yeast Hsp60 are unambiguous orthologs (~58–61% identity), so an antifolding-type contribution to conservative sorting is *plausibly conserved* and the term need not be hard-refuted. But plausibility of an indirect, selective matrix chaperone contribution is a fundamentally different claim from "HSPD1 directly performs protein import into the IMS." The recommended curation posture is to **down-weight or remove GO:0045041 as a direct function, or retain it only with an explicit low-confidence / indirect-role qualifier**, while foregrounding the directly supported matrix protein-folding terms.

---

## Key Findings

### Finding 1 — The human GO:0045041 annotation rests solely on phylogenetic inference (IBA); all direct human evidence is matrix folding, not IMS import

A direct interrogation of the UniProt P10809 GO annotation set shows a clean split between what is *inferred* and what is *experimentally demonstrated* for human HSPD1. The term **GO:0045041 ("protein import into mitochondrial intermembrane space") is annotated ONLY as IBA:GO_Central** (Inferred from Biological Ancestor — a phylogenetic propagation), with **no IDA, IMP, or other experimental support**.

By contrast, every experimentally supported process/function annotation for human HSPD1 describes **matrix chaperonin activity**: protein refolding (GO:0042026, IDA), protein stabilization (GO:0050821, IMP), response to unfolded protein (GO:0006986, IDA), ATP-dependent protein folding chaperone (GO:0140662), and unfolded protein binding (implied by chaperonin function). Furthermore, UniProt's primary subcellular location for HSPD1 is **mitochondrion matrix**; no IMS localization is annotated (the only membrane-associated annotation is an ISS "mitochondrial inner membrane"). This matters because a *directly demonstrated* IMS-import function would normally be accompanied by experimental evidence of the protein acting in the relevant pathway; here there is none for human. The annotation is entirely a downstream product of tree-based inference, not human experimentation.

### Finding 2 — The yeast donor evidence is indirect (antifolding) and is directly contested on the same substrate (cytochrome b2)

The experimental basis for the whole inference chain is the yeast work in **[PMID:1347713](https://pubmed.ncbi.nlm.nih.gov/1347713/)** (Koll et al., 1992, *Cell*). In yeast, cytochrome b2 reaches the IMS by a two-step "conservative sorting" route: it is first imported into the matrix, then re-exported across the inner membrane. Koll et al. showed that Hsp60 **arrests folding of the protein in the matrix ("antifolding")**, keeping the export-competent domain translocation-competent and thereby coupling import to export. This is an **indirect matrix chaperone role** — Hsp60 keeps a substrate unfolded so it can be handed to the export machinery — and is emphatically *not* an IMS translocase activity.

Critically, the same substrate is the subject of a directly contradictory result. **[PMID:7911803](https://pubmed.ncbi.nlm.nih.gov/7911803/)** (Rospert, Müller, Schatz, Glick, 1994) analyzed a fusion protein targeted to the IMS by the **same bipartite cytochrome b2 presequence** and found it was sorted to the IMS **"independently of hsp60."** The mechanistic explanation is decisive: the b2 presequence arrests import at the inner membrane (a **stop-transfer** mechanism), so the passenger "is never exposed to hsp60." In other words, on the very substrate that motivated the Hsp60-sorting idea, the IMS route does **not** require Hsp60.

Two further papers show that even Hsp60's matrix folding role is **substrate-selective**, not general. **[PMID:8631298](https://pubmed.ncbi.nlm.nih.gov/8631298/)** (Rospert, 1996) found that of four monomeric imported proteins, only rhodanese required hsp60 for folding; DHFR, barnase, and Cpr3p folded efficiently without it and showed no detectable binding — "the mitochondrial chaperonin system is not essential for the folding of all matrix proteins." **[PMID:9774331](https://pubmed.ncbi.nlm.nih.gov/9774331/)** (Dubaquié et al., 1998) found in vivo hsp60/hsp10 substrates to be "overlapping but non-identical," i.e., differential and selective. Taken together, the donor evidence is (a) indirect, (b) selective, and (c) self-contradicted on its flagship substrate — a weak foundation for a directly-worded import annotation.

### Finding 3 — The dedicated IMS protein-import machinery is the MIA40/CHCHD4–Erv1 disulfide relay, not Hsp60

The IMS has its **own** dedicated import pathway, mechanistically distinct from anything Hsp60 does. **[PMID:33921425](https://pubmed.ncbi.nlm.nih.gov/33921425/)** (Dickson-Murray et al., 2021) states plainly: "The main protein import pathway for the intermembrane space (IMS) recognises proteins that are cysteine-rich, and it is the only import pathway that chemically modifies the imported precursors... The key component of this pathway is **Mia40 (called CHCHD4 in human cells)**." Precursors are trapped in the IMS by disulfide-bond formation (oxidative folding).

Supporting structural and reconstitution work reinforces this. **[PMID:20136511](https://pubmed.ncbi.nlm.nih.gov/20136511/)** (Endo et al., 2010) describes a "dedicated disulfide relay system" consisting of Tim40/Mia40 and Erv1 that traps small soluble proteins. **[PMID:19477928](https://pubmed.ncbi.nlm.nih.gov/19477928/)** (Tienson et al., 2009) demonstrated by in vitro reconstitution that "Mia40, Erv1, and oxygen are the minimal machinery" to import and oxidize small Tim proteins. Meanwhile, bipartite-presequence IMS proteins such as cytochrome b2 reach the IMS via the **TIM23 translocase and a stop-transfer step** (PMID:7911803). Neither of the two genuine IMS-import routes has Hsp60 as a core component; Hsp60's documented role is downstream, in the matrix, folding proteins *after* import.

### Finding 4 — Human HSPD1 and yeast Hsp60 are clear orthologs (~58–61% identity); orthology does not exclude conservation of the antifolding role

To test whether the IBA inference could be justified on conservation grounds, a global Needleman–Wunsch alignment was performed between UniProt **P10809** (human HSPD1, 573 aa) and **P19882** (yeast Hsp60, SGD:S000004249, 572 aa). The alignment yielded **348 identical positions over 602 aligned columns (57.8% identity; 60.8% relative to the shorter sequence)**. Group I chaperonins are among the most deeply conserved protein families known, structurally and functionally.

The interpretation cuts both ways and must be stated carefully. Strong orthology means an *antifolding contribution to conservative sorting* is **plausibly conserved** in human — so the term should not be hard-refuted. But orthology to a protein with an indirect, substrate-selective matrix role does **not** license a direct "protein import into the IMS" molecular function assignment. Conservation supports *plausibility of the same indirect role*, not the stronger claim encoded by the GO term.

### Finding 5 — The human IBA traces to a single yeast IMP leaf (PMID:1347713); the contradicting paper is not captured as a NOT annotation

A QuickGO provenance query pinned down the exact annotation topology. **Human HSPD1 (P10809)** has exactly **one** annotation to GO:0045041 — IBA (ECO:0000318), GO_REF:0000033, assignedBy GO_Central, qualifier `involved_in`, with/from **PANTHER:PTN000143510 + SGD:S000004249**. **Yeast Hsp60 (P19882 / SGD:S000004249)** has **two** annotations to GO:0045041 — the same IBA, **plus one experimental IMP** (ECO:0000315) referenced to **PMID:1347713**, assignedBy SGD, qualifier `involved_in`.

Crucially, **no annotation cites PMID:7911803**, and there is **no NOT-qualified annotation** recording the contradictory stop-transfer result. The entire human annotation therefore rests on a single experimental leaf whose central claim is contested in the primary literature, and the curation record does not currently reflect that contest. This is a textbook case where phylogenetic propagation can amplify a fragile, indirect, and disputed single-organism result into a confident-looking human annotation.

---

## Mechanistic Model / Interpretation

The core confusion the seed hypothesis rightly flags is between **chaperone contributions to translocation** and **folding after import**. Resolving that distinction is what settles the curation question.

```
   CYTOSOL
      |  precursor with bipartite b2-type presequence
      v
  ============ OUTER MEMBRANE (TOM) ============
      |
      v
  ~~~~~~~~ INNER MEMBRANE (TIM23) ~~~~~~~~
      |
      |-- STOP-TRANSFER at inner membrane (b2 presequence)
      |        --> lateral release / IMP cleavage --> IMS
      |        *** Hsp60 NOT required (PMID:7911803) ***
      |
      v (full matrix import, then conservative re-export)
   MATRIX
      |
   [Hsp60/Hsp10 chaperonin]
      |-- FOLDS a SUBSET of matrix proteins (rhodanese; not DHFR/barnase/Cpr3p)
      |        (PMID:8631298, PMID:9774331)
      |-- ANTIFOLDING: keeps b2 unfolded to permit re-export
      |        --> INDIRECT coupling of import to export (PMID:1347713)
      v
   IMS proteins via re-export (conservative sorting)


  SEPARATE, DEDICATED IMS IMPORT PATHWAY (no Hsp60):
   cysteine-rich precursors --> MIA40/CHCHD4 + Erv1 disulfide relay
   --> oxidative folding traps protein in IMS (PMID:33921425, 20136511, 19477928)
```

Under this model, Hsp60's only documented contact with IMS biogenesis is an **indirect, matrix-side, substrate-selective antifolding role** in the conservative-sorting route (Koll 1992). That is a legitimate biological phenomenon, but it is: not translocase activity (Hsp60 does not move proteins across a membrane); not the dedicated IMS pathway (that is MIA40/CHCHD4–Erv1); contradicted on its own model substrate (b2 reaches the IMS without Hsp60 exposure); and selective (most matrix proteins fold independently of Hsp60). The GO term GO:0045041, applied with an `involved_in` qualifier to human HSPD1, reads as a direct, general involvement in IMS import — a mismatch in both specificity and confidence with what the evidence supports.

### Molecular-function vs. process framing

| Aspect | What the GO term implies | What the evidence actually supports |
|---|---|---|
| Location of action | IMS / import machinery | Mitochondrial matrix |
| Molecular activity | Participation in IMS translocation | ATP-dependent protein folding (chaperonin) |
| Substrate scope | General IMS-import substrates | Selective subset of matrix proteins |
| Directness | Direct involvement | Indirect antifolding coupling |
| Human evidence | (implied) | None — IBA only |

---

## Evidence Base / Evidence Matrix

| Citation | Evidence type | Supports/Refutes/Qualifies | Claim tested | Key finding | Context | Confidence & limitations |
|---|---|---|---|---|---|---|
| UniProt P10809 / QuickGO | Review/database | Qualifies (weakens) | Is GO:0045041 experimentally supported in human? | Human GO:0045041 is IBA-only; all EXP terms are matrix folding; primary location = matrix | Human HSPD1 | High confidence on annotation status; database-level, not experimental |
| [PMID:1347713](https://pubmed.ncbi.nlm.nih.gov/1347713/) (Koll 1992) | Mutant phenotype / direct assay | Qualifies (indirect support) | Does Hsp60 participate in IMS sorting of cyt b2? | Hsp60 "antifolds" b2 in matrix, coupling import to re-export | Yeast, isolated mitochondria | Sole donor leaf; indirect role; substrate-specific |
| [PMID:7911803](https://pubmed.ncbi.nlm.nih.gov/7911803/) (Rospert/Glick 1994) | Direct assay (co-IP, translocation intermediates) | Refutes (competing) | Is Hsp60 required to sort b2-presequence proteins to IMS? | b2-presequence fusion sorted to IMS independently of hsp60; passenger never exposed to hsp60 (stop-transfer) | Yeast, isolated mitochondria | Directly contradicts donor on same substrate; not captured as NOT annotation |
| [PMID:8631298](https://pubmed.ncbi.nlm.nih.gov/8631298/) (Rospert 1996) | Direct assay | Qualifies | Do all matrix proteins need Hsp60 to fold? | Only rhodanese required hsp60; DHFR/barnase/Cpr3p folded without it | Yeast mitochondria | Establishes substrate selectivity |
| [PMID:9774331](https://pubmed.ncbi.nlm.nih.gov/9774331/) (Dubaquié 1998) | Mutant phenotype (in vivo screen) | Qualifies | In vivo substrate spectrum of hsp60/hsp10 | Overlapping but non-identical, selective substrate requirements | Yeast, in vivo | Reinforces selectivity |
| [PMID:33921425](https://pubmed.ncbi.nlm.nih.gov/33921425/) (Dickson-Murray 2021) | Review | Refutes (competing pathway) | What is the dedicated IMS import pathway? | Mia40/CHCHD4 disulfide relay is THE main IMS import pathway | Human/yeast, review | Review-level but describes established consensus |
| [PMID:20136511](https://pubmed.ncbi.nlm.nih.gov/20136511/) (Endo 2010) | Structural/review | Refutes (competing pathway) | Machinery for small soluble IMS proteins | Dedicated Tim40/Mia40–Erv1 disulfide relay | Yeast, structural | Review of structural data |
| [PMID:19477928](https://pubmed.ncbi.nlm.nih.gov/19477928/) (Tienson 2009) | Direct assay (in vitro reconstitution) | Refutes (competing pathway) | Minimal machinery to import small Tims | Mia40 + Erv1 + O2 are sufficient; Hsp60 not involved | In vitro | Strong mechanistic evidence for alternative pathway |
| Sequence alignment P10809 vs P19882 (this study) | Computational (structural/evolutionary) | Qualifies (permits conservation) | Are human HSPD1 and yeast Hsp60 orthologs? | 57.8% identity over 602 columns; clear orthologs | Human vs yeast | Own computation; supports plausibility only, not directness |
| QuickGO provenance query (this study) | Review/database | Qualifies (weakens) | What is the IBA provenance? | Single yeast IMP leaf (PMID:1347713); PMID:7911803 not recorded; no NOT | Human + yeast | Own query; database-level |

---

## GO Curation Implications

**Lead (requires curator verification):** GO:0045041 for human HSPD1 should be **down-weighted, removed as a direct function, or retained only with an explicit low-confidence / indirect-role qualifier.** It should not be presented as a core molecular activity of HSPD1.

Reasoning by GO aspect:

- **GO:0045041 is a Biological Process (BP) term.** For human HSPD1 it is supported only by IBA, and the donor evidence describes an *indirect* matrix chaperone contribution, not direct IMS translocation. The most defensible action is to treat it as **non-core**: either remove it, or keep it flagged as inference-only with a note that the underlying donor claim is contested (PMID:7911803) and substrate-selective (PMID:8631298).
- **The terms that should be foregrounded** are the directly supported ones: **GO:0140662 (ATP-dependent protein folding chaperone, MF)**, **GO:0042026 (protein refolding, BP, IDA)**, **GO:0050821 (protein stabilization, BP, IMP)**, and **GO:0006986 (response to unfolded protein, BP, IDA)**, with **CC = mitochondrial matrix**. These represent HSPD1's primary function.
- **If GO:0045041 is retained at all**, curators should consider linking the contradicting reference (PMID:7911803) — currently absent — so the IBA propagation is not silently overstated.
- Avoid defaulting to "protein binding"; the informative primary term is the chaperonin folding activity (GO:0140662), which is well supported.

---

## Mechanistic Scope

The immediate molecular activity of HSPD1/Hsp60 that is directly evidenced is **ATP-dependent chaperonin-mediated protein folding in the mitochondrial matrix**, acting as a tetradecameric (double-heptamer) folding chamber with its co-chaperonin Hsp10 (HSPE1). Recent human structural work (e.g., [PMID:38951622](https://pubmed.ncbi.nlm.nih.gov/38951622/)) confirms a conserved group I chaperonin folding cycle with client encapsulation in the folding chamber.

The IMS-import claim under evaluation is **not** this immediate activity. It is a **downstream, pathway-level consequence** observed for a specific yeast substrate (cytochrome b2) via conservative sorting, where Hsp60's contribution is to keep the substrate unfolded (antifolding) so the separate export machinery can re-translocate it. That is: direct gene-product activity = ATP-dependent protein (re)folding / holding-unfolded in the matrix; downstream/pathway consequence (not direct) = enabling IMS delivery of certain conservatively sorted substrates; not demonstrated at all for human = any IMS-import role is inferred, not measured.

Loss-of-function human phenotypes (hypomyelinating leukodystrophy, e.g., [PMID:39500555](https://pubmed.ncbi.nlm.nih.gov/39500555/), [PMID:32532876](https://pubmed.ncbi.nlm.nih.gov/32532876/); MitCHAP-60 disease) are attributable to impaired chaperonin assembly/folding, not to a specific IMS-import defect, and thus do not support GO:0045041 as a core function.

---

## Conflicts and Alternatives

1. **Same-substrate contradiction (strongest conflict).** PMID:1347713 (Hsp60 couples b2 import to export) vs PMID:7911803 (b2-presequence fusion sorted to IMS independently of hsp60 via stop-transfer). The passenger "is never exposed to hsp60." This is a direct experimental conflict on the flagship substrate.
2. **Competing dedicated pathway.** The genuine, dedicated IMS import machinery is MIA40/CHCHD4–Erv1 (PMID:33921425, 20136511, 19477928). Hsp60 is not a component. This reframes any Hsp60 "IMS-import" role as, at most, an indirect and marginal contribution to one conservative-sorting route.
3. **Substrate selectivity.** PMID:8631298 and PMID:9774331 show Hsp60's matrix role itself is not general. Generalizing a selective, indirect effect into a broad "protein import into IMS" annotation is an over-generalization.
4. **Annotation carry-over / frequency bias.** The human term is a pure IBA propagation from one yeast IMP leaf via PANTHER PTN000143510. There is no independent human confirmation, and the contradicting paper is not recorded — a classic phylogenetic over-annotation risk.
5. **Consistent alternative interpretation:** Hsp60's real biology is matrix folding; its apparent "IMS-sorting" role is a special case of its matrix antifolding/holding activity applied to a subset of conservatively sorted precursors — a downstream effect, not a distinct import function.

No paralog-confusion issue was identified (HSPD1 is the sole human mitochondrial group I chaperonin), and human/yeast orthology is solid, so the conflict is about *directness and specificity of the term*, not about identity.

---

## Limitations and Knowledge Gaps

1. **No direct human assay either way.** What was checked: UniProt/QuickGO annotations and human structural/disease literature. Why it matters: neither a positive human IMS-import assay nor a human NOT experiment exists, so the human position is inference-bound. Resolution: a human-mitochondria import assay testing whether HSPD1 depletion affects delivery of conservatively sorted IMS substrates.
2. **Conservative sorting in humans is under-characterized.** What was checked: yeast conservative-sorting literature (cyt b2, Oxa1, COXII). Why it matters: it is unclear how prominent the conservative-sorting route is in human mitochondria versus stop-transfer and MIA pathways. Resolution: substrate-mapping of human IMS proteins by import route.
3. **The donor annotation's contest is not curated.** What was checked: QuickGO provenance. Why it matters: PMID:7911803 is not linked and there is no NOT annotation, so the IBA looks stronger than the evidence warrants. Resolution: curator review of the yeast leaf annotation and its counter-evidence.
4. **"Antifolding" is not cleanly captured by any single GO term.** Why it matters: the real, defensible contribution (holding a substrate unfolded to permit export) is a legitimate chaperone activity but is being represented by an import-process term. Resolution: consider whether an "unfolded protein binding"/"protein stabilization"-type framing better represents the indirect contribution than an IMS-import BP term.

---

## Discriminating Tests

The following would most efficiently distinguish "HSPD1 directly imports IMS proteins" from "HSPD1 is a matrix folding chaperone with, at most, an indirect antifolding contribution to conservative sorting":

1. **Human HSPD1 knockdown + IMS-substrate import assay.** Deplete/inactivate HSPD1 in human cells or isolated human mitochondria and measure import/maturation of (a) MIA40/CHCHD4 substrates (small Tims, SOD1/CCS, TRIAP1) and (b) any conservatively sorted human IMS proteins. Prediction under the refutation: MIA substrates unaffected; only matrix-folding-dependent maturation affected.
2. **Co-immunoprecipitation of import intermediates** (as in PMID:7911803) in human mitochondria to test whether IMS-destined precursors ever physically associate with HSPD1. Prediction: bipartite/stop-transfer and MIA substrates show no stable HSPD1 binding.
3. **Route assignment of the human IMS proteome** (stop-transfer vs MIA vs conservative sorting) to quantify how many human IMS proteins could even in principle depend on a matrix Hsp60 step.
4. **Curated re-alignment of PANTHER node PTN000143510** to check whether the IBA to GO:0045041 is warranted given the contested single leaf, and whether a NOT annotation on the yeast leaf is justified.

---

## Proposed Follow-up Actions / Curation Leads (require curator verification)

**Candidate action change:**
- **Remove or down-weight GO:0045041 (`involved_in`) on human HSPD1**, or retain only with a low-confidence, indirect-role qualifier. Rationale: IBA-only; donor evidence indirect, selective, and contested.

**Candidate references to attach / verify (exact snippets):**
- [PMID:7911803](https://pubmed.ncbi.nlm.nih.gov/7911803/): *"there was no detectable binding to hsp60 with a fusion protein that was targeted to the intermembrane space by the bipartite cytochrome b2 presequence... the cytochrome b2 presequence arrests import through the inner membrane, with the result that the attached passenger protein is never exposed to hsp60."* — counter-evidence to the donor claim; currently not linked.
- [PMID:1347713](https://pubmed.ncbi.nlm.nih.gov/1347713/): the sole experimental donor leaf (antifolding/conservative sorting) — verify it supports only an indirect matrix role.
- [PMID:33921425](https://pubmed.ncbi.nlm.nih.gov/33921425/): *"The key component of this pathway is Mia40 (called CHCHD4 in human cells)"* — establishes the true dedicated IMS-import machinery.
- [PMID:8631298](https://pubmed.ncbi.nlm.nih.gov/8631298/): substrate-selectivity of hsp60.

**Candidate terms to foreground instead (directly supported):**
- GO:0140662 — ATP-dependent protein folding chaperone (MF)
- GO:0042026 — protein refolding (BP, IDA)
- GO:0050821 — protein stabilization (BP, IMP)
- GO:0006986 — response to unfolded protein (BP, IDA)
- CC: mitochondrial matrix

**Suggested curator questions:**
- Should the yeast leaf annotation (PMID:1347713) carry a note/counter-reference to PMID:7911803, and should the IBA to human be re-evaluated on that basis?
- Is an "antifolding/holding-unfolded" contribution better represented by a stabilization/binding term than by an IMS-import process term?

**Suggested experiments:** the discriminating tests above (human HSPD1-depletion IMS import assays; co-IP of import intermediates).

---

## Bottom Line

The seed hypothesis is technically not *impossible* — human/yeast orthology is strong and an indirect antifolding contribution to conservative sorting could be conserved. But the GO term GO:0045041, as applied to human HSPD1, over-states the evidence: it is IBA-only, traces to a single contested yeast leaf, describes an indirect and substrate-selective matrix role rather than a translocase activity, and is contradicted on its own model substrate while the genuine dedicated IMS-import machinery (MIA40/CHCHD4–Erv1) is a different system. Curation should treat it as **weakly supported / non-core / inference-only** and prioritize the directly supported matrix protein-folding terms.


## Artifacts

- [OpenScientist HSPD1 GO0045041 decision table](openscientist_artifacts/HSPD1_GO0045041_decision_table.csv)
- [OpenScientist HSPD1 GO0045041 evidence matrix](openscientist_artifacts/HSPD1_GO0045041_evidence_matrix.csv)
- [OpenScientist HSPD1 GO0045041 provenance](openscientist_artifacts/HSPD1_GO0045041_provenance.json)
- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)