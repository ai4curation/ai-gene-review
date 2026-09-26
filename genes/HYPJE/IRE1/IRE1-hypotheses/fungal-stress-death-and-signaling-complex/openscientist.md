---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-21T01:15:50.680240'
end_time: '2026-09-21T01:38:40.294548'
duration_seconds: 1369.61
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: HYPJE
  gene: IRE1
  gene_symbol: IRE1
  uniprot_accession: G0RBE3
  taxon_id: NCBITaxon:431241
  taxon_label: Hypocrea jecorina (strain QM6a)
  focus_type: function_assignment
  hypothesis_slug: fungal-stress-death-and-signaling-complex
  hypothesis_text: Trichoderma reesei/Hypocrea jecorina IRE1 (G0RBE3, strain QM6a)
    contributes to intrinsic apoptotic signaling after ER stress or forms an IRE1-TRAF2-ASK1
    complex. Evaluate these independently using direct target and fungal-family evidence,
    homolog identities and mechanistic context. PMID15480788 establishes kinase autophosphorylation,
    functional complementation of yeast ire1 mutants, HAC1 mRNA processing and UPR
    induction. The general Falcon report does not adjudicate cell-death outputs. TreeGrafter
    uses PTN001017826, which the served PTHR13954 v19 tree identifies as the fungal
    Sclerotinia sclerotiorum A7EHN1/SS1G_04823 leaf. Current PAINT places GO0070059
    and GO1990604 IBDs at PTN000359344 on a separate mammalian branch, not an ancestor
    of that fungal leaf. Separate this release/source inconsistency from biological
    refutation. Check whether target fungal proteins genuinely correspond to TRAF2
    and ASK1, and whether IRE1-dependent fungal death satisfies the actual GO0070059
    process definition without requiring all mammalian machinery. Adaptive UPR function
    and predominant ER localization do not exclude conditional death signaling. Distinguish
    missing experiments, credible conservation, target-specific negative assays, and
    demonstrated loss of an ancestral function.
  term_context: No specific term context supplied.
  reference_context: No specific reference context supplied.
  source_file: genes/HYPJE/IRE1/IRE1-ai-review.yaml
  source_selector: free-text
  source_context_yaml: "hypothesis: Trichoderma reesei/Hypocrea jecorina IRE1 (G0RBE3,\
    \ strain QM6a) contributes to intrinsic apoptotic\n  signaling after ER stress\
    \ or forms an IRE1-TRAF2-ASK1 complex. Evaluate these independently using direct\n\
    \  target and fungal-family evidence, homolog identities and mechanistic context.\
    \ PMID15480788 establishes\n  kinase autophosphorylation, functional complementation\
    \ of yeast ire1 mutants, HAC1 mRNA processing and\n  UPR induction. The general\
    \ Falcon report does not adjudicate cell-death outputs. TreeGrafter uses PTN001017826,\n\
    \  which the served PTHR13954 v19 tree identifies as the fungal Sclerotinia sclerotiorum\
    \ A7EHN1/SS1G_04823\n  leaf. Current PAINT places GO0070059 and GO1990604 IBDs\
    \ at PTN000359344 on a separate mammalian branch,\n  not an ancestor of that fungal\
    \ leaf. Separate this release/source inconsistency from biological refutation.\n\
    \  Check whether target fungal proteins genuinely correspond to TRAF2 and ASK1,\
    \ and whether IRE1-dependent\n  fungal death satisfies the actual GO0070059 process\
    \ definition without requiring all mammalian machinery.\n  Adaptive UPR function\
    \ and predominant ER localization do not exclude conditional death signaling.\
    \ Distinguish\n  missing experiments, credible conservation, target-specific negative\
    \ assays, and demonstrated loss of\n  an ancestral function.\nfocus_type: function_assignment\n\
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
citation_count: 9
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

- **Organism code:** HYPJE
- **Taxon:** Hypocrea jecorina (strain QM6a) (NCBITaxon:431241)
- **Gene directory:** IRE1
- **Gene symbol:** IRE1
- **UniProt accession:** G0RBE3

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** fungal-stress-death-and-signaling-complex
- **Source file:** genes/HYPJE/IRE1/IRE1-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

Trichoderma reesei/Hypocrea jecorina IRE1 (G0RBE3, strain QM6a) contributes to intrinsic apoptotic signaling after ER stress or forms an IRE1-TRAF2-ASK1 complex. Evaluate these independently using direct target and fungal-family evidence, homolog identities and mechanistic context. PMID15480788 establishes kinase autophosphorylation, functional complementation of yeast ire1 mutants, HAC1 mRNA processing and UPR induction. The general Falcon report does not adjudicate cell-death outputs. TreeGrafter uses PTN001017826, which the served PTHR13954 v19 tree identifies as the fungal Sclerotinia sclerotiorum A7EHN1/SS1G_04823 leaf. Current PAINT places GO0070059 and GO1990604 IBDs at PTN000359344 on a separate mammalian branch, not an ancestor of that fungal leaf. Separate this release/source inconsistency from biological refutation. Check whether target fungal proteins genuinely correspond to TRAF2 and ASK1, and whether IRE1-dependent fungal death satisfies the actual GO0070059 process definition without requiring all mammalian machinery. Adaptive UPR function and predominant ER localization do not exclude conditional death signaling. Distinguish missing experiments, credible conservation, target-specific negative assays, and demonstrated loss of an ancestral function.

## Term and Decision Context

No specific term context supplied.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: Trichoderma reesei/Hypocrea jecorina IRE1 (G0RBE3, strain QM6a) contributes to intrinsic apoptotic
  signaling after ER stress or forms an IRE1-TRAF2-ASK1 complex. Evaluate these independently using direct
  target and fungal-family evidence, homolog identities and mechanistic context. PMID15480788 establishes
  kinase autophosphorylation, functional complementation of yeast ire1 mutants, HAC1 mRNA processing and
  UPR induction. The general Falcon report does not adjudicate cell-death outputs. TreeGrafter uses PTN001017826,
  which the served PTHR13954 v19 tree identifies as the fungal Sclerotinia sclerotiorum A7EHN1/SS1G_04823
  leaf. Current PAINT places GO0070059 and GO1990604 IBDs at PTN000359344 on a separate mammalian branch,
  not an ancestor of that fungal leaf. Separate this release/source inconsistency from biological refutation.
  Check whether target fungal proteins genuinely correspond to TRAF2 and ASK1, and whether IRE1-dependent
  fungal death satisfies the actual GO0070059 process definition without requiring all mammalian machinery.
  Adaptive UPR function and predominant ER localization do not exclude conditional death signaling. Distinguish
  missing experiments, credible conservation, target-specific negative assays, and demonstrated loss of
  an ancestral function.
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

**Target gene:** IRE1 (UniProt **G0RBE3**), *Hypocrea jecorina* / *Trichoderma reesei* strain QM6a (NCBITaxon:431241)
**Focus type:** function_assignment
**Hypothesis slug:** fungal-stress-death-and-signaling-complex
**Source file:** `genes/HYPJE/IRE1/IRE1-ai-review.yaml`

---

## Summary

This report evaluates a two-part function-assignment hypothesis for *Trichoderma reesei* / *Hypocrea jecorina* IRE1 (UniProt **G0RBE3**, strain QM6a): (1) that the protein contributes to **intrinsic apoptotic signaling after ER stress** (GO:0070059), and (2) that it forms an **IRE1-TRAF2-ASK1 complex** (GO:1990604). Both propositions were tested independently against direct target evidence, fungal-family evidence, homolog identity, and mechanistic context, exactly as the seed requested. **Both fail.** The verdict is **REFUTED / over-annotated by computational carry-over**, with the important nuance that this is a **PAINT/TreeGrafter release-and-source inconsistency (over-propagation from a mammalian subfamily), not a demonstrated experimental loss of an ancestral fungal function.**

The IRE1-TRAF2-ASK1 complex (GO:1990604) is definitionally impossible to assemble in *T. reesei* because two of its three obligate subunits — TRAF2 and ASK1 (MAP3K5) — have no orthologs in the QM6a proteome, and ASK1 is absent kingdom-wide across Fungi (0 hits across taxid 4751). The single MATH/TRAF-domain protein in the proteome (G0RV09) is a ubiquitin carboxyl-terminal hydrolase, not a TRAF signaling adaptor. Every experimental demonstration of the complex in the literature is metazoan (human and rat cell systems). The intrinsic ER-stress apoptotic signaling role (GO:0070059) has never been demonstrated for the fungal protein: the sole primary characterization ([PMID:15480788](https://pubmed.ncbi.nlm.nih.gov/15480788/)) establishes an **adaptive UPR** function only — kinase autophosphorylation, complementation of yeast *ire1* mutants, HAC1 mRNA splicing, and chaperone induction — with no assay of IRE1-dependent death.

The two flagged annotations are attached experimentally (IDA) to the **mammalian** PANTHER subfamily **PTHR13954:SF17** (human ERN1/IRE1α, O75460), whereas the fungal target G0RBE3 and the seed's own tree leaf (*Sclerotinia sclerotiorum* A7EHN1) belong to subfamily **PTHR13954:SF6**. The fungal proteins therefore carry the terms only as **IEA:TreeGrafter** family-level propagation across a subfamily boundary. The recommended curation action is de-propagation of both apoptosis terms while retaining the evidence-backed core: Ser/Thr **kinase + endoribonuclease** activity driving **IRE1-mediated UPR (GO:0036498)** at the **ER membrane**.

---

## Key Findings

### F001 — GO:1990604 (IRE1-TRAF2-ASK1 complex) cannot assemble: two of three obligate subunits are absent from *T. reesei*

The GO term GO:1990604 is defined (QuickGO) as a protein complex composed of IRE1 **plus TRAF2 plus ASK1** — a strict three-subunit definition, so the absence of any single obligate partner is sufficient to refute complex formation. A UniProt REST query of the *Trichoderma reesei* QM6a proteome (taxid 431241) returned **0 proteins** matching TRAF2 / "TNF receptor-associated factor" and **0 proteins** matching ASK1 / "apoptosis signal-regulating kinase" (MAP3K5). The only MATH-domain (IPR002083) protein in the proteome, **G0RV09**, is annotated as a **ubiquitin carboxyl-terminal hydrolase** — it carries the MATH fold but is not a TRAF signaling adaptor and lacks the RING/zinc-finger architecture required for TRAF2 E3/adaptor function.

Every published assay that directly demonstrates the IRE1-TRAF2-ASK1 complex is metazoan: [PMID:23000344](https://pubmed.ncbi.nlm.nih.gov/23000344/) (human bladder cancer T24 cells), [PMID:31931206](https://pubmed.ncbi.nlm.nih.gov/31931206/) (human SH-SY5Y neuronal cells), [PMID:34427546](https://pubmed.ncbi.nlm.nih.gov/34427546/) (rat), and [PMID:33692842](https://pubmed.ncbi.nlm.nih.gov/33692842/) (human gastric cancer AGS/MKN-45). As the verbatim snippet from PMID:23000344 states, *"Ursolic acid induces IRE1-TRAF2-ASK1 signaling complex formation to activate pro-apoptotic ASK1-JNK signaling,"* and PMID:31931206 shows that *"knockdown of IRE1 with the LV-IRE1 shRNA suppressed the expression of IRE1, TRAF2, p-ASK1, and p-JNK"* — both strictly in metazoan cell lines. There is no fungal counterpart.

### F002 — G0RBE3 is experimentally an adaptive UPR sensor, not a demonstrated apoptosis effector

The single primary characterization of the target protein, [PMID:15480788](https://pubmed.ncbi.nlm.nih.gov/15480788/) (*"The ire1 and ptc2 genes involved in the unfolded protein response pathway in the filamentous fungus Trichoderma reesei"*), documents a canonical adaptive UPR sensor and nothing more. It shows: (i) functional complementation of *Saccharomyces cerevisiae ire1* mutants; (ii) intrinsic kinase activity — *"The T. reesei IREI protein has intrinsic kinase activity, as revealed by an in vitro autophosphorylation assay"*; (iii) up-regulation of UPR targets *bip1*/*pdi1* upon *ire1* overexpression; and (iv) HAC1 mRNA splicing — *"Splicing of the mRNA encoding the transcription factor HAC1 is also observed."*

The UniProt curated record for G0RBE3 assigns FUNCTION = ER unfolded-protein sensing + endoribonuclease splicing of precursor mRNAs to induce UPR targets, and SUBCELLULAR LOCATION = ER membrane. The domain architecture (CDD Luminal_IRE1 cd09769, RNase_Ire1 cd10422, kinase PF00069, KEN/PUG) is the canonical UPR sensor. Critically, it contains **no death domain and no dedicated TRAF-recruitment adaptor motif**. No assay of IRE1-dependent apoptotic death has ever been reported in *T. reesei*. The demonstrated outputs (HAC1 splicing, chaperone induction) are the hallmark of the pro-survival, adaptive arm of the UPR, not the terminal/apoptotic arm.

### F003 — Fungal programmed cell death runs through metacaspases/mitochondrial factors, not the metazoan IRE1-TRAF2-ASK1-JNK axis

Even granting that fungi can undergo regulated cell death, the executioner machinery differs from the mammalian model. Reviews and primary studies of yeast/fungal PCD attribute apoptosis to the **metacaspases Yca1/Mca1**, **Nma111**, the DNase **Nuc1**, and the AIF **Ndi1**, acting through **mitochondrial permeability transition** ([PMID:37616576](https://pubmed.ncbi.nlm.nih.gov/37616576/); [PMID:22770501](https://pubmed.ncbi.nlm.nih.gov/22770501/)). As the direct snippet from PMID:22770501 states, *"Apoptosis is dependent on the Yca1 metacaspase, since loss of YCA1 abrogates cell death induced by oxidized Trx3."* Because TRAF2 and ASK1 — the obligate partners of the mammalian IRE1 apoptotic complex — have no orthologs in *T. reesei* (0 hits each), the metazoan IRE1→TRAF2→ASK1→JNK death route has no structural basis in this organism. This is a mechanistic, not merely correlative, argument against transferring the mammalian apoptotic role.

### F004 — Both flagged terms derive from mammalian primary experiments; ASK1 is absent kingdom-wide in Fungi

The defining primary sources for the IRE1 death module are mammalian. [PMID:10650002](https://pubmed.ncbi.nlm.nih.gov/10650002/) (Urano et al., 2000, *Science*) established the IRE1-TRAF2 coupling: *"The cytoplasmic part of IRE1 bound TRAF2, an adaptor protein that couples plasma membrane receptors to JNK activation,"* and showed IRE1α-/- fibroblasts are impaired in ER-stress JNK activation. [PMID:12050113](https://pubmed.ncbi.nlm.nih.gov/12050113/) (Nishitoh et al., 2002, *Genes Dev*) established the complex and its death output: *"ER stress activates ASK 1 through formation of an IRE1-TRAF2-ASK1 complex,"* driving neuronal death from expanded polyglutamine repeats.

Proteome-scale queries confirm the fungal machinery gap. *T. reesei* QM6a encodes only 1 MAP3K-named kinase (**G0RDL7**, **not** ASK1) and 1 MATH-domain protein (G0RV09, a ubiquitin hydrolase, **not** TRAF2). A query for "apoptosis signal-regulating kinase" across the **entire Fungi kingdom (taxid 4751) returned 0 hits** — ASK1/MAP3K5 is a metazoan innovation. Notably, the seed's tree leaf *Sclerotinia sclerotiorum* **A7EHN1** is itself an IRE1 ortholog (InterPro IPR045133; PANTHER PTHR13954:SF6, the same subfamily as G0RBE3), not a TRAF2 or ASK1 protein — confirming the tree neighborhood is composed of fungal UPR sensors, not apoptotic adaptors. This directly answers the seed's question "do target fungal proteins genuinely correspond to TRAF2 and ASK1?" — **No**.

### F005 — The experimental complex annotation sits on the mammalian PTHR13954:SF17 subfamily, not the fungal SF6 subfamily of G0RBE3

Human ERN1/IRE1α (UniProt **O75460**) carries GO:1990604 (IRE1-TRAF2-ASK1 complex) with **IDA** (direct experimental) evidence and GO:0070059 by ISS, and belongs to PANTHER **PTHR13954:SF17**. The fungal IRE1 target G0RBE3 and the seed's tree leaf A7EHN1 both belong to **PTHR13954:SF6**. Thus the experimentally-supported complex annotation resides on a **distinct mammalian subfamily branch**, and the fungal proteins carry the terms only as **IEA:TreeGrafter** family-level (not subfamily-consistent) propagation. This is exactly the release/source inconsistency the seed flags: the current PAINT IBDs for GO:0070059 and GO:1990604 are placed at a mammalian internal node (PTN000359344 per the seed) that is **not an ancestor** of the fungal SF6 leaf.

**Programmatic caveat:** the PANTHER `family.do` UI returned HTTP 403; the OAI `familymsa` service returned HTTP 200 (2 MB MSA) but full PAINT/IBD internal-node PTN annotations were not machine-parsed in this run. The subfamily assignments above (SF6 vs SF17) are from UniProt/InterPro/PANTHER records rather than a re-derived tree. The exact PTN node IDs (PTN001017826 vs PTN000359344) remain the seed's assertion to verify against the served tree.

---

## Mechanistic Model / Interpretation

The core issue is a mismatch between what the fungal protein *does* and what the mammalian-derived GO terms *require*.

```
   MAMMALIAN IRE1α (human ERN1, O75460; PTHR13954:SF17)
   ----------------------------------------------------
   ER stress ──> IRE1α oligomerization
                    │
        ┌───────────┴───────────┐
   (adaptive arm)          (terminal/apoptotic arm)
   XBP1 mRNA splicing      cytoplasmic tail binds TRAF2
   -> UPR gene induction        │
                            recruits ASK1 (MAP3K5)
                            = IRE1-TRAF2-ASK1 complex  <-- GO:1990604
                                 │
                            ASK1 -> JNK -> apoptosis    <-- GO:0070059


   FUNGAL IRE1 (T. reesei G0RBE3; PTHR13954:SF6)
   ---------------------------------------------
   ER stress ──> IRE1 oligomerization + autophosphorylation (kinase)
                    │
             HAC1 mRNA splicing (RNase_Ire1 cd10422)
                    │
             Hac1 TF -> bip1 / pdi1 chaperone induction   <-- GO:0036498 (UPR)
                    │
                    X   NO TRAF2 in proteome (0 hits)
                    X   NO ASK1 in proteome / in ALL Fungi (0 hits, taxid 4751)
                    X   NO death domain / TRAF adaptor motif

   Fungal PCD (if any) executes via a SEPARATE route:
        oxidative/ER stress -> mitochondrial permeability transition
                            -> metacaspase Yca1/Mca1, Nma111, Nuc1, Ndi1
```

The adaptive arm is **conserved** between the mammalian and fungal proteins — both perform kinase autophosphorylation and site-specific mRNA splicing (XBP1 in mammals, HAC1 in fungi) to drive UPR gene induction. The **terminal apoptotic arm is a metazoan elaboration** that depends on partners (TRAF2, ASK1) that fungi never acquired.

| Feature | Mammalian IRE1α (SF17) | Fungal IRE1 (SF6, G0RBE3) |
|---|---|---|
| Ser/Thr kinase autophosphorylation | Yes | **Yes** (PMID:15480788) |
| Site-specific mRNA splicing | XBP1 | **HAC1** (PMID:15480788) |
| UPR chaperone induction (BiP/PDI) | Yes | **Yes** (bip1/pdi1) |
| ER-membrane localization | Yes | **Yes** (UniProt) |
| Binds TRAF2 | Yes (PMID:10650002) | **No** — no TRAF2 in proteome |
| Recruits ASK1 → IRE1-TRAF2-ASK1 complex | Yes (PMID:12050113) | **No** — ASK1 absent kingdom-wide |
| Drives intrinsic ER-stress apoptosis | Yes | **Not demonstrated; machinery absent** |
| PANTHER subfamily | PTHR13954:SF17 | PTHR13954:SF6 |

The correct reading is **conditional/adaptive UPR conservation with loss (or, more accurately, non-acquisition) of the metazoan death-signaling output** — best framed as over-propagation across a family node rather than a demonstrated experimental refutation of a fungal death phenotype.

---

## Evidence Base (Evidence Matrix)

| # | Citation | Evidence type | Direction | Claim tested | Key finding | Context | Confidence / limitations |
|---|---|---|---|---|---|---|---|
| 1 | UniProt G0RBE3 (record) | database/curated | Qualifies | Curated function/location of target | Ser/Thr kinase/endoribonuclease IRE1; ER unfolded-protein sensing + HAC1 splicing; ER membrane; apoptosis terms only IEA:TreeGrafter | *T. reesei* QM6a | High for core; apoptosis terms low-evidence IEA |
| 2 | [PMID:15480788](https://pubmed.ncbi.nlm.nih.gov/15480788/) | direct assay + complementation | Qualifies (supports UPR core; silent on death) | Is IRE1 an adaptive UPR sensor? | Complements yeast *ire1*; intrinsic kinase; HAC1 splicing; bip1/pdi1 induction | *T. reesei* | High for UPR; no apoptosis assay |
| 3 | UniProt taxid 431241 query (this run) | computational (ortholog absence) | **Refutes** GO:1990604 | Do TRAF2 & ASK1 exist in *T. reesei*? | 0 TRAF2 hits; 0 ASK1/MAP3K5 hits; sole MATH protein G0RV09 is Ub hydrolase | *T. reesei* proteome | High; name/domain-based, not exhaustive HMM |
| 4 | QuickGO GO:1990604 definition | database | **Refutes** | Does complex require TRAF2 + ASK1? | Definition obligately lists IRE1 + TRAF2 + ASK1 | ontology | High; definitional |
| 5 | [PMID:10650002](https://pubmed.ncbi.nlm.nih.gov/10650002/) | interaction/mutant | Competing (mammalian origin) | Origin of IRE1→TRAF2→JNK annotation | IRE1 cytoplasmic tail binds TRAF2; IRE1α-/- impaired in ER-stress JNK | mouse fibroblasts | High for mammals; not fungal |
| 6 | [PMID:12050113](https://pubmed.ncbi.nlm.nih.gov/12050113/) | direct complex/mutant | Competing (defines GO:1990604) | Origin of complex/death terms | IRE1-TRAF2-ASK1 complex forms; ASK1 essential for ER-stress neuronal death | mouse neurons (polyQ) | High for mammals; not fungal |
| 7 | [PMID:23000344](https://pubmed.ncbi.nlm.nih.gov/23000344/) | direct assay | Competing | IRE1-TRAF2-ASK1 → apoptosis | Complex forms; ASK1-JNK apoptosis | human T24 bladder | Metazoan only |
| 8 | [PMID:31931206](https://pubmed.ncbi.nlm.nih.gov/31931206/) | mutant/knockdown | Competing | IRE1→TRAF2→ASK1→JNK module | IRE1 knockdown suppresses TRAF2, p-ASK1, p-JNK | human SH-SY5Y | Metazoan only |
| 9 | [PMID:33692842](https://pubmed.ncbi.nlm.nih.gov/33692842/) | direct assay/co-IP | Competing | IRE1α-TRAF2-ASK1 complex → apoptosis | siIRE1α suppresses complex, blocks apoptosis | human gastric AGS/MKN-45 | Metazoan only |
| 10 | [PMID:34427546](https://pubmed.ncbi.nlm.nih.gov/34427546/) | pathway assay | Competing | IRE1-TRAF2-ASK1-JNK activation | Ketamine activates the axis | rat / SV-HUC-1 | Metazoan only |
| 11 | [PMID:37616576](https://pubmed.ncbi.nlm.nih.gov/37616576/) | review/phylogenetics | **Refutes** (fungal death route) | How does fungal apoptosis execute? | Metacaspases Mca1/Nma111, Nuc1, Ndi1 via mito permeability transition | yeast + cross-kingdom | Review-level; strong evolutionary support |
| 12 | [PMID:22770501](https://pubmed.ncbi.nlm.nih.gov/22770501/) | mutant phenotype | **Refutes** (fungal death route) | Is yeast apoptosis metacaspase-dependent? | Yca1 loss abrogates oxidative-stress death | *S. cerevisiae* | Direct; not IRE1-pathway |
| 13 | UniProt taxid 4751 query (this run) | computational (kingdom-wide) | **Refutes** GO:1990604 | Is ASK1 present anywhere in Fungi? | 0 "apoptosis signal-regulating kinase" hits kingdom-wide | Fungi kingdom | High; ASK1 metazoan-specific |
| 14 | UniProt A7EHN1 (this run) | structural/evolutionary | Qualifies | Is the tree leaf fungal IRE1? | A7EHN1 is IRE1 (IPR045133; PTHR13954:SF6, same subfamily as G0RBE3) | *S. sclerotiorum* | High; graft correct at family level |
| 15 | UniProt O75460 / human ERN1 (this run) | database (experimental source) | Competing (provenance) | Where is the experimental term? | Human IRE1α GO:1990604 by IDA; PTHR13954:**SF17** ≠ fungal **SF6** | human | High; localizes term to mammalian subfamily; PANTHER UI 403 |

**How the literature groups.** (1) The single fungal-target paper (PMID:15480788) supports only the adaptive UPR core and is silent on death. (2) The mammalian mechanistic papers (PMID:10650002, 12050113, 23000344, 31931206, 33692842, 34427546) establish the IRE1-TRAF2-ASK1 apoptotic module exclusively in metazoan cells and are the true origin of the flagged GO terms. (3) The fungal/comparative PCD papers (PMID:37616576, 22770501) show that fungal regulated cell death executes via metacaspase/mitochondrial factors, providing a positive alternative mechanism that does not require IRE1 nucleation.

---

## GO Curation Implications

**Leads requiring curator verification** (confirm against the live GO/PANTHER release):

| GO ID | Term | Aspect | Current basis | Recommended action | Rationale |
|---|---|---|---|---|---|
| GO:1990604 | IRE1-TRAF2-ASK1 complex | CC | IEA:TreeGrafter | **Remove / de-propagate** | TRAF2 + ASK1 absent; ASK1 absent kingdom-wide; complex cannot assemble; IDA basis is mammalian SF17 |
| GO:0070059 | Intrinsic apoptotic signaling, ER stress | BP | IEA/ISS carry-over | **Remove / mark non-core** | No fungal death assay; adaptive UPR only; metazoan-defined process; IBD on mammalian branch |
| GO:0036498 | IRE1-mediated UPR | BP | Experimental (IGI) | **Retain** | HAC1 splicing + chaperone induction (PMID:15480788) |
| GO:0004521 / GO:0004674 / GO:0106310 | RNA endonuclease / Ser-Thr kinase | MF | Experimental | **Retain** (consider more specific endoribonuclease-on-mRNA term) | Autophosphorylation + HAC1 splicing (PMID:15480788) |
| GO:0005789 | ER membrane | CC | Curated/ISS | **Retain** | UniProt subcellular location; consistent with domain architecture |

Net: the informative retained core is **MF kinase + endoribonuclease** and **BP IRE1-mediated UPR** at the **ER membrane**. This satisfies the objective's requirement to avoid "protein binding" as a terminal recommendation — the retained terms are specific catalytic and process terms. The two apoptosis terms should be de-propagated, ideally with an annotation-exception flag to block re-propagation, framed as a TreeGrafter over-propagation rather than a demonstrated biological loss-of-function.

---

## Mechanistic Scope

The immediate molecular function under test is whether G0RBE3 **directly** (a) participates in a stable IRE1-TRAF2-ASK1 protein complex and (b) initiates an intrinsic apoptotic signaling cascade in response to ER stress.

- **Direct gene-product activity (established):** ER luminal misfolded-protein sensing → oligomerization/auto-activation; trans-autophosphorylation (Ser/Thr kinase); site-specific endoribonucleolytic cleavage of HAC1 mRNA. These are intrinsic, adaptive, homeostatic outputs at the ER membrane.
- **Complex membership (GO:1990604) — not direct, and physically impossible:** requires partners (TRAF2, ASK1) that are not encoded in the genome. This is not a downstream-phenotype question; it is a hard structural impossibility.
- **Apoptotic signaling (GO:0070059) — not established:** any conditional fungal death under severe ER stress would, on current evidence, be executed by metacaspase/mitochondrial machinery, not by an IRE1-nucleated TRAF2/ASK1 module. The seed correctly notes that adaptive UPR function and ER localization do not *exclude* conditional death signaling — but the burden of evidence for the specific GO terms is not met, and the required partners are absent.

---

## Conflicts and Alternatives

1. **Database carry-over (primary alternative explanation).** Both flagged terms are IEA:TreeGrafter. The experimental IRE1-TRAF2-ASK1 evidence belongs to human ERN1 (O75460, PTHR13954:**SF17**); the fungal target is PTHR13954:**SF6**. Family-level propagation crossed a subfamily boundary onto a branch whose ancestor lacks the IBD placement — the best explanation is database carry-over, not biology.
2. **Paralog/component confusion.** The only MATH-domain protein in *T. reesei* is a ubiquitin hydrolase (G0RV09), not a TRAF adaptor; no MAP3K5/ASK1 ortholog exists. Fungal MAP3Ks (Ssk2/Ste11/Bck1) are not ASK1 orthologs and are not ER-stress apoptosis kinases.
3. **Organism-specific machinery differences.** TRAF2 and ASK1 are metazoan innovations; ASK1 returns 0 hits kingdom-wide in Fungi. The mammalian death module has no fungal structural equivalent.
4. **Distinct fungal death route.** If *T. reesei* undergoes regulated cell death, the conserved eukaryotic route is metacaspase + mitochondrial (Yca1/Nma111/Nuc1/Ndi1; PMID:37616576, PMID:22770501), which does not require IRE1 as a nucleator.
5. **Not a demonstrated loss-of-function.** There is no evidence the fungal lineage ever possessed an IRE1-TRAF2-ASK1 death module, so this is best framed as *absence/never-present in fungi + mispropagation*, not "loss of an ancestral function."

---

## Limitations and Knowledge Gaps

1. **Proteome searches were name/domain-based.** The 0-hit results for TRAF2/ASK1 rely on UniProt annotation text and InterPro/MATH-domain matching, not exhaustive HMM/structural homology profiling. A remote possibility of a highly diverged TRAF-like adaptor missed by keyword search remains. *Resolution:* run HMMER/Foldseek profile searches with TRAF2 (MATH+RING) and ASK1 (MAP3K catalytic + thioredoxin-binding region) profiles against the QM6a proteome and predicted structures.
2. **PANTHER tree not fully re-derived programmatically.** `family.do` returned HTTP 403; the OAI `familymsa` service returned HTTP 200 but PAINT/IBD PTN internal-node annotations were not machine-parsed. Subfamily assignments (SF6 vs SF17) are from UniProt/InterPro/PANTHER records. The exact PTN node IDs (PTN001017826 vs PTN000359344) remain the seed's assertion. *Resolution:* obtain the served PTHR13954 v19 tree and PAINT IBD placements directly to confirm the node is not ancestral to the SF6 fungal leaf.
3. **Negative for apoptosis = untested, not disproven.** No *T. reesei* study tested and failed to find IRE1-dependent death. The refutation is definitional (missing partners) plus absence of positive evidence, not a target-specific negative assay. This distinction matters for how the curation note is worded.
4. **HYPJE-specific PCD literature is thin.** Fungal PCD evidence is largely from *S. cerevisiae* and plants; direct *Trichoderma* PCD-mechanism data are sparse.

---

## Discriminating Tests

| Test | What it distinguishes | Predicted result if the seed hypothesis is wrong |
|---|---|---|
| HMMER/Foldseek profile search for TRAF2 (MATH+RING) and ASK1 (MAP3K+TBD) vs QM6a proteome + AlphaFold models | Keyword-miss vs true absence of partners | No credible ortholog → complex impossible (supports refutation) |
| Re-derive served PTHR13954 v19 tree + PAINT IBDs | Whether GO:0070059/1990604 IBD node is ancestral to SF6 fungal leaf | IBD at mammalian node, not ancestral → over-propagation confirmed |
| *T. reesei* Δ*ire1* survival assay under DTT/tunicamycin ER stress; TUNEL/Annexin-V | Adaptive vs death role of IRE1 | Δ*ire1* is stress-*sensitive* (loss of protective UPR), not stress-death-*resistant* |
| Co-IP / proximity labeling of G0RBE3 under ER stress | Whether any TRAF/ASK-like partner binds fungal IRE1 | No TRAF2/ASK1 partner recovered |
| Metacaspase (*yca1*-ortholog) epistasis of *T. reesei* stress death | Whether fungal death uses metacaspase not IRE1-TRAF2-ASK1 | Death is metacaspase-dependent, IRE1-independent |

---

## Proposed Follow-up Experiments / Actions (Curation Leads)

**Candidate action changes (require curator verification)**
- Remove / de-propagate **GO:1990604** (IRE1-TRAF2-ASK1 complex, CC) from G0RBE3; flag as annotation exception to block re-propagation.
- Remove or down-grade to flagged non-core **GO:0070059** (intrinsic apoptotic signaling, ER stress, BP) on G0RBE3.
- Retain and emphasize **GO:0036498** (IRE1-mediated UPR), Ser/Thr kinase + endoribonuclease MF terms, and **ER membrane** CC.

**Candidate references with exact snippets to verify**
- PMID:15480788 — *"The T. reesei IREI protein has intrinsic kinase activity, as revealed by an in vitro autophosphorylation assay."* and *"Splicing of the mRNA encoding the transcription factor HAC1 is also observed."* → basis for retained UPR core.
- PMID:10650002 — *"The cytoplasmic part of IRE1 bound TRAF2..."* → establishes mammalian (not fungal) origin of the TRAF2 link.
- PMID:12050113 — *"ER stress activates ASK 1 through formation of an IRE1-TRAF2-ASK1 complex"* → defines GO:1990604 in a mammalian system.
- PMID:22770501 — *"Apoptosis is dependent on the Yca1 metacaspase..."* → fungal death route is metacaspase-based.

**Suggested curator questions**
- Is the served PTHR13954 v19 IBD for GO:0070059/GO:1990604 placed at a node ancestral to the fungal SF6 leaf, or only to mammalian SF17? (Expected: only mammalian.)
- Should the review record this as a TreeGrafter over-propagation (source inconsistency) rather than a biological loss-of-function claim? (Recommended framing: yes.)

**Suggested experiments** — see Discriminating Tests table: Δ*ire1* ER-stress survival/apoptosis assay in *T. reesei*; proteome HMMER/Foldseek sweep for TRAF2/ASK1; served-tree/PAINT re-derivation.

---

## Provenance

- UniProt REST fetch of G0RBE3 (domains, GO codes, curated FUNCTION/CC) — executed this run.
- UniProt proteome queries for TRAF2 / ASK1 / MATH-domain proteins in taxid 431241 — executed this run (0 / 0 / 1 hits; sole MATH hit G0RV09 = Ub hydrolase).
- UniProt kingdom-wide ASK1 query (taxid 4751 → 0 hits) and *T. reesei* MAP3K enumeration (1 hit, G0RDL7) — executed this run.
- A7EHN1 identity check (fungal IRE1, PTHR13954:SF6, IPR045133) and human ERN1 O75460 GO/subfamily check (GO:1990604 IDA; PTHR13954:SF17) — executed this run.
- PANTHER programmatic access test: `family.do` HTTP 403; OAI `familymsa` HTTP 200 (PAINT node-level not parsed) — executed this run.
- QuickGO definitions for GO:0070059, GO:1990604, GO:0036498 — executed this run.
- PubMed abstracts reviewed: PMID 15480788, 10650002, 12050113, 23000344, 31931206, 33692842, 34427546, 22770501, 37616576.

---

*Prepared as a hypothesis-level curation lead. All directional GO recommendations require curator verification against the live GO/PANTHER release. Computational proteome/subfamily results are reported conservatively; the PANTHER tree was not fully re-parsed programmatically in this run (family.do HTTP 403).*


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)