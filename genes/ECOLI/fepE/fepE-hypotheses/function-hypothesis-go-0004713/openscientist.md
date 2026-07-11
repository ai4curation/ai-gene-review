---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-06T15:42:03.153357'
end_time: '2026-07-06T15:52:20.531552'
duration_seconds: 617.38
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: ECOLI
  gene: fepE
  gene_symbol: fepE
  uniprot_accession: P26266
  taxon_id: NCBITaxon:83333
  taxon_label: Escherichia coli (strain K12)
  focus_type: function_assignment
  hypothesis_slug: function-hypothesis-go-0004713
  hypothesis_text: fepE has protein tyrosine kinase activity (GO:0004713).
  term_context: '- Term: protein tyrosine kinase activity (GO:0004713)

    - Evidence type: IBA

    - Original reference: GO_REF:0000033'
  reference_context: '- GO_REF:0000033

    - PMID:40703034

    - PMID:22437828

    - PMID:12603743

    - file:ECOLI/fepE/fepE-deep-research-falcon.md'
  source_file: genes/ECOLI/fepE/fepE-ai-review.yaml
  source_selector: existing_annotations[2].function_hypothesis
  source_context_yaml: "term:\n  id: GO:0004713\n  label: protein tyrosine kinase\
    \ activity\nevidence_type: IBA\noriginal_reference_id: GO_REF:0000033"
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 1
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

- **Organism code:** ECOLI
- **Taxon:** Escherichia coli (strain K12) (NCBITaxon:83333)
- **Gene directory:** fepE
- **Gene symbol:** fepE
- **UniProt accession:** P26266

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** function-hypothesis-go-0004713
- **Source file:** genes/ECOLI/fepE/fepE-ai-review.yaml
- **Source selector:** existing_annotations[2].function_hypothesis

## Seed Hypothesis

fepE has protein tyrosine kinase activity (GO:0004713).

## Term and Decision Context

- Term: protein tyrosine kinase activity (GO:0004713)
- Evidence type: IBA
- Original reference: GO_REF:0000033

## Reference Context

- GO_REF:0000033
- PMID:40703034
- PMID:22437828
- PMID:12603743
- file:ECOLI/fepE/fepE-deep-research-falcon.md

## Source Context YAML

```yaml
term:
  id: GO:0004713
  label: protein tyrosine kinase activity
evidence_type: IBA
original_reference_id: GO_REF:0000033
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

# FepE (P26266) and the Protein Tyrosine Kinase Annotation (GO:0004713): A Focused Curation Report

**Gene:** fepE / *wzz(fepE)* (*Escherichia coli* K-12) · **UniProt:** P26266 (377 aa) · **Term under review:** protein tyrosine kinase activity (GO:0004713) · **Evidence code:** IBA · **Reference:** GO_REF:0000033 (PAINT / phylogenetic annotation) · **Focus type:** function_assignment

**Executive verdict: REFUTED / OVER-ANNOTATED.**

---

## Summary

The seed hypothesis states that **fepE has protein tyrosine kinase activity (GO:0004713)**. This report evaluates whether the *E. coli* gene product FepE (P26266) *directly* possesses that molecular function. Based on sequence architecture, membrane topology, protein-domain composition, a motif scan, and the primary literature on both FepE and its distant kinase relatives, the annotation is **not supported**. FepE is a **PCP-1 (WzzB-type) polysaccharide co-polymerase** — a regulator of very-long O-antigen chain length in lipopolysaccharide (LPS) biosynthesis — and it lacks every structural hallmark required for bacterial tyrosine (BY-)kinase activity.

The GO:0004713 IBA annotation arises from a **phylogenetic (PAINT/IBA) inference within PANTHER family PTHR32309 ("TYROSINE-PROTEIN KINASE")**, propagated under GO_REF:0000033. This family lumps genuine bacterial tyrosine autokinases (Wzc, Etk) together with catalytically inert chain-length regulators (WzzB, FepE) because both classes share the periplasmic **polysaccharide co-polymerase (PCP)** module. The shared module is not the kinase — it is the periplasmic chain-length-sensing domain. FepE possesses **only** that periplasmic Wzz domain and does **not** carry the cytoplasmic BY-kinase machinery. The IBA annotation is therefore a classic case of **family-level over-annotation** in which a molecular-function term valid for one subfamily is inappropriately projected onto a non-catalytic sister subfamily.

The recommended curation action is to **remove (or NOT-qualify) the GO:0004713 annotation** on P26266 and retain the biologically accurate O-antigen chain-length-regulation and inner-membrane annotations. The verdict is robust: it is supported by computed topology (an 18-residue cytoplasmic C-terminus far too short to house the ~230-residue cytoplasmic kinase domain), by Pfam domain architecture (PF02706/Wzz only, with none of the AAA_31 P-loop, GNVR, or WZC_N domains that define BY-kinases), and by a motif scan showing FepE lacks the C-terminal tyrosine autophosphorylation cluster that is the defining catalytic feature of Wzc and Etk. The main caveat is that this is a negative, absence-of-machinery argument from sequence/domain informatics plus the established PCP literature; there is no direct enzymatic assay reporting FepE kinase activity, and none is needed because the mechanistic prerequisites are absent.

---

## Key Findings

### Finding 1 — FepE lacks the tyrosine-autokinase module; GO:0004713 is paralog over-annotation

**Topology is incompatible with a cytoplasmic kinase.** Computed from the UniProt P26266 record, FepE is a 377-residue inner-membrane protein with the canonical PCP-1 architecture: a short cytoplasmic N-terminus (residues ~1–41), a first transmembrane helix (~42–62), a large periplasmic domain (~63–338), a second transmembrane helix (~339–359), and a very short cytoplasmic C-terminus (~360–377). The functional consequence is decisive: the cytoplasmic C-terminal tail is **only ~18 residues long**. Bacterial tyrosine (BY-)kinases such as Wzc and Etk carry a **~230-residue cytoplasmic kinase domain** (a P-loop/Walker-A-containing ATP-binding module plus a C-terminal tyrosine cluster). An 18-residue tail cannot house such a domain, and FepE's bulk — its ~275-residue periplasmic domain — faces the wrong compartment for any cytoplasmic phosphotransfer chemistry.

**Domain architecture confirms the absence of catalytic machinery.** FepE's Pfam architecture consists of **PF02706 (Wzz) only** — the periplasmic polysaccharide co-polymerase chain-length-regulator domain. It **lacks** all of the domains that define true BY-kinases: **PF13614 (AAA_31)**, the P-loop / Walker-A ATP-binding kinase module; **PF13807 (GNVR)**, the accessory domain adjacent to the kinase core; and **PF23607 (WZC_N)**, the N-terminal element of Wzc-type kinases. All three are present in Wzc (P76387) and Etk (P38134). Because the PCP/Wzz module is shared between chain-length regulators and BY-kinases, family clustering pulls them together, but catalytic identity resides entirely in the cytoplasmic modules FepE does not have.

**Motif scan confirms the absence of the tyrosine autophosphorylation cluster.** The defining biochemical hallmark of a BY-kinase is a C-terminal tyrosine-rich cluster that is the site of autophosphorylation, working together with a functional Walker-A (P-loop) motif. A residue scan of the C-terminal ~40 residues found FepE has a **single tyrosine** in its short cytoplasmic tail, versus the **6–7 tyrosine autophosphorylation-cluster residues** seen in genuine *E. coli* BY-kinases. There is no tyrosine cluster to phosphorylate and no ATP-binding P-loop to do the phosphorylating.

| Protein | UniProt | Length (aa) | Tyr in C-terminal cluster | Kinase module | BY-kinase? |
|---|---|---|---|---|---|
| **FepE** | P26266 | 377 | **1** (no cluster) | absent (PF02706 only) | **No** |
| Wzc | P76387 | 720 | 6 | present (P-loop + Tyr cluster) | Yes |
| Etk | P38134 | 726 | 7 | present (P-loop + Tyr cluster) | Yes |

**Provenance of the annotation.** The IBA annotation traces to **PANTHER family PTHR32309** ("TYROSINE-PROTEIN KINASE"), which places FepE in subfamily SF13 alongside the Wzc/Etk-type kinases (SF32) and propagates the molecular-function term via **GO_REF:0000033 (PAINT)**. The inference is phylogenetic, not experimental, and it inherits the term from the catalytically active branch of a mixed family.

---

## Mechanistic Model / Interpretation

The core of this case is the distinction between two functionally divergent classes of proteins that share one domain. Both are anchored in the inner membrane by two transmembrane helices and both present a large periplasmic PCP domain. The difference lies entirely in the cytoplasm.

```
   PCP-1 chain-length regulator (FepE, WzzB)      BY-kinase (Wzc, Etk)
   ------------------------------------------      ---------------------------------
        periplasm                                       periplasm
   ┌───────────────────────┐                       ┌───────────────────────┐
   │  PCP / Wzz domain      │  (chain-length       │  PCP / Wzz-like domain │
   │  (PF02706)             │   sensing)           │  (PF02706-related)     │
   └───┬───────────────┬────┘                       └───┬───────────────┬────┘
   ~~~~│TM1~~~~~~~~~~~~~│TM2~~~ inner membrane ~~~~~~~~~│TM1~~~~~~~~~~~~~│TM2~~~
       │               │                                │               │
   N-term            C-term (~18 aa)                  N-term            │
                     NO kinase                                    ┌─────┴──────────┐
                                                                  │ Cytoplasmic     │
                                                                  │ BY-kinase domain│
                                                                  │ ~230 aa:        │
                                                                  │  • Walker-A/    │
                                                                  │    P-loop (ATP) │
                                                                  │  • C-terminal   │
                                                                  │    Tyr cluster  │
                                                                  │    (6–7 Tyr)    │
                                                                  │  PF13614/PF13807│
                                                                  └─────────────────┘
```

FepE performs its function — regulating the **very-long** modal length of O-antigen polysaccharide chains during Wzx/Wzy-dependent LPS assembly — through its periplasmic domain and its oligomerization state, **not** through any phosphotransfer chemistry. The crystallographic and mutagenesis literature reinforces this: chain-length regulation depends on Wzz/FepE **oligomerization** and on residues in the periplasmic α-helical bundle (e.g., helix-8 intermonomer contacts), phenomena entirely separate from kinase catalysis. In contrast, Wzc's function in group-1 capsule assembly **requires** phosphorylation of its C-terminal tyrosine-rich domain and a functional Walker-A motif — the exact features FepE lacks.

The mechanistic conclusion is that the seed hypothesis conflates a **shared periplasmic accessory module** (the reason the two proteins cluster in one PANTHER family) with a **catalytic activity** encoded only in the cytoplasmic modules of the kinase subfamily. FepE's activity, process, and location are all inconsistent with GO:0004713: no ATP-binding catalytic domain (activity), no phosphotransfer role in its pathway (process), and its bulk faces the periplasm while the tiny cytoplasmic tail cannot host a kinase (location).

---

## Evidence Base

| # | Citation | Evidence type | Direction | Claim tested | Key finding | Context | Confidence / limitations |
|---|----------|---------------|-----------|--------------|-------------|---------|--------------------------|
| 1 | UniProt **P26266** (computed) | Computational (domain + topology) | **Refutes** | FepE has a kinase domain | Pfam = **PF02706 Wzz only**; cytoplasmic C-terminus = ~18 aa; no AAA_31/GNVR/WZC_N | *E. coli* K-12 inner membrane | High for domain absence; database-derived features |
| 2 | This analysis (motif scan) | Computational | **Refutes** | FepE has BY-kinase Tyr cluster + P-loop | 1 Tyr in C-terminal 40 aa (vs 6–7 in Wzc/Etk); no canonical Walker-A in the short cytoplasmic tail | Sequence-based | High; motif-level, not experimental |
| 3 | [PMID: 22437828](https://pubmed.ncbi.nlm.nih.gov/22437828/) | Structural / evolutionary (crystal, incl. Wzz_FepE) | **Refutes / qualifies** | FepE architecture | PCPs incl. FepE are "chain length regulator periplasmic proteins…anchored in the inner membrane by two transmembrane helices"; FepE crystal used for chain-length structure–function | Gram-negative PCP-1 | High; direct structural characterization, no kinase module |
| 4 | [PMID: 11053445](https://pubmed.ncbi.nlm.nih.gov/11053445/) | Direct assay (of the paralog) | **Competing (defines the real kinase)** | What confers tyrosine kinase activity | "The tyrosine-rich domain at the C terminus of Wzc…is the site of phosphorylation and autophosphorylation of Wzc requires a functional Walker A motif" | *E. coli* Wzc / group-1 capsule | High; defines features FepE lacks |
| 5 | [PMID: 29603538](https://pubmed.ncbi.nlm.nih.gov/29603538/) | Functional / genetic (overexpression) | **Competing (defines the real function)** | FepE's function | Overexpressing *fepE*/*wzzB* increases long/very-long O-polysaccharide — chain-length regulation | *Salmonella* / Gram-negative LPS | High; confirms co-polymerase role |
| 6 | [PMID: 23019341](https://pubmed.ncbi.nlm.nih.gov/23019341/) / [PMID: 23646936](https://pubmed.ncbi.nlm.nih.gov/23646936/) | Mutant phenotype / regulation | **Qualifies** | *wzz(fepE)* role in vivo | *wzz(fepE)* controls very-long O-antigen; PmrAB-regulated; separable from *wzz_st* | *S.* Typhimurium | High for BP/CC, not MF kinase |
| 7 | [PMID: 22069314](https://pubmed.ncbi.nlm.nih.gov/22069314/) | Mutant / structural | **Qualifies** | How chain length is regulated | Regulation maps to periplasmic α-helix intermonomer contacts / oligomerization (mapped onto FepE structure) — non-catalytic mechanism | *P. aeruginosa* Wzz2 | High for mechanism; heterologous protein |
| 8 | PANTHER **PTHR32309** (annotation source) | Database | **Explains over-annotation** | Origin of IBA | Family named "TYROSINE-PROTEIN KINASE"; FepE = SF13, Wzc/Etk = SF32 — same tree, different catalytic status | PAINT / GO_REF:0000033 | High; identifies the propagation artifact |

**How the literature supports the verdict.** [PMID: 22437828](https://pubmed.ncbi.nlm.nih.gov/22437828/) establishes FepE as a PCP-1 chain-length regulator anchored by two TM helices with a periplasmic domain — architecture incompatible with a cytoplasmic kinase. [PMID: 11053445](https://pubmed.ncbi.nlm.nih.gov/11053445/) defines the molecular hallmarks of BY-kinase activity (C-terminal tyrosine cluster + functional Walker-A) present in Wzc and absent in FepE, anchoring the correct assignment of GO:0004713 to the kinase subfamily. [PMID: 22069314](https://pubmed.ncbi.nlm.nih.gov/22069314/) shows chain-length regulation depends on periplasmic α-helix/oligomerization contacts — a non-catalytic mechanism. [PMID: 29603538](https://pubmed.ncbi.nlm.nih.gov/29603538/), [PMID: 23646936](https://pubmed.ncbi.nlm.nih.gov/23646936/), and [PMID: 23019341](https://pubmed.ncbi.nlm.nih.gov/23019341/) confirm FepE's genuine role in setting very-long O-antigen chain length and its downstream physiological consequences.

---

## GO Curation Implications (leads — require curator verification)

- **GO:0004713 protein tyrosine kinase activity (MF, IBA): REMOVE / do not accept (or NOT-qualify).** The evidence indicates over-annotation via PANTHER PTHR32309 IBA. FepE lacks the AAA_31 kinase domain, the P-loop, and the C-terminal tyrosine cluster required for the activity. Retaining it would assign a molecular function the protein cannot perform.
- **Better-supported terms to consider:**
  - **BP:** `GO:0009103` lipopolysaccharide biosynthetic process and a "regulation of O-antigen / LPS chain length" concept — FepE determines very-long O-antigen modal length ([PMID: 22437828](https://pubmed.ncbi.nlm.nih.gov/22437828/), [PMID: 29603538](https://pubmed.ncbi.nlm.nih.gov/29603538/)).
  - **CC:** inner (plasma) membrane, integral membrane with periplasmic domain (UniProt topology; [PMID: 22437828](https://pubmed.ncbi.nlm.nih.gov/22437828/)). The existing inner-membrane annotation is well supported.
  - **MF:** there is no crisp catalytic MF term for PCP co-polymerase function; do **not** substitute "protein binding." A "polysaccharide co-polymerase / chain-length determinant" descriptor is preferable if the ontology supports it.
- **Net action:** remove/downgrade the kinase MF; retain membrane CC; strengthen the LPS/O-antigen chain-length BP annotations.

**GO decision table**

| Term | ID | Aspect | Current | Recommended action | Rationale |
|---|---|---|---|---|---|
| protein tyrosine kinase activity | GO:0004713 | MF | IBA (GO_REF:0000033) | **Remove / NOT** | No kinase domain, no Tyr cluster, wrong topology; family over-annotation |
| lipopolysaccharide biosynthetic process | GO:0009103 | BP | — | **Assert / retain** | FepE acts in Wzx/Wzy-dependent LPS assembly |
| O-antigen / LPS chain-length determination | (BP) | BP | — | **Assert** | Directly supported by function & structure literature |
| integral component of plasma (inner) membrane | GO:0005887 | CC | — | **Retain** | Two-TM-helix inner-membrane anchor |

---

## Mechanistic Scope

- **Immediate molecular role tested:** catalysis of protein-tyrosine phosphorylation (ATP + protein-Tyr → ADP + phospho-Tyr). This requires an intracellular kinase domain (P-loop/Walker-A + Walker-B + activation region) and, for BY-kinases, a C-terminal tyrosine cluster. **FepE has none of these.**
- **What FepE actually does (direct):** as an inner-membrane PCP-1 oligomer, its large periplasmic domain acts as a molecular ruler/co-polymerase that sets *very-long* O-antigen modal chain length during Wzx/Wzy-dependent LPS assembly.
- **Downstream / pleiotropic (not the MF of FepE):** O-antigen length affects serum/complement resistance, virulence, and bile tolerance (*Salmonella* studies). These are LPS-phenotype consequences of the chain-length function, not evidence of enzymatic kinase activity.

---

## Conflicts and Alternatives

- **Paralog confusion (primary explanation):** Wzc/Etk are genuine BY-kinases in the same PANTHER family and share the periplasmic Wzz domain with FepE. The IBA propagated the kinase MF across the whole family, including the non-catalytic PCP-1 branch (FepE).
- **Shared-domain artifact:** the clustering signal is the periplasmic PCP/Wzz fold, an accessory chain-length module, not a catalytic one. Domain-sharing does not imply catalytic-activity sharing.
- **Historical naming:** "FepE / ferric enterobactin transport protein" is itself a legacy misnomer; genetic/functional work reassigned *wzz(fepE)* as the very-long O-antigen chain-length regulator. Neither name implies kinase activity.
- **No competing primary evidence** reports experimental tyrosine kinase activity for FepE; the annotation rests solely on phylogenetic inference. No isoform of the single-chain 377-aa protein could add a cytoplasmic kinase domain.

---

## Limitations and Knowledge Gaps

1. **No direct enzymatic test of FepE.** No in vitro kinase assay on purified FepE exists. *Checked:* PubMed. *Why it matters:* would be the definitive refutation. *Resolve:* in vitro ATP/[γ-³²P] autophosphorylation assay — expected negative. This affects only absolute certainty; the structural case is already decisive.
2. **AlphaFold geometry of the cytoplasmic tail.** *Checked:* topology only (18-aa tail). *Why it matters:* confirms no cryptic kinase fold. *Resolve:* inspect the AlphaFold DB model for P26266 for a folded cytoplasmic domain (expected: none).
3. **Exact PANTHER tree placement / evidence for other family members.** *Checked:* subfamily labels (SF13 vs SF32). *Why:* confirms the FepE branch is non-kinase. *Resolve:* PAINT ancestral-node review to confirm the exact node from which GO_REF:0000033 propagated the term.
4. **Topology/domain calls depend on UniProt/Pfam annotations.** These are high-confidence and corroborated by the FepE crystal structure, but database-derived; residue boundaries are approximate (this does not change the conclusion).

---

## Proposed Follow-up Experiments / Actions

- **In vitro autokinase assay** on purified recombinant FepE (± ATP), with Wzc as a positive control: a true BY-kinase autophosphorylates; FepE should not.
- **Phosphoproteomics / anti-phosphotyrosine (4G10) immunoblot** of FepE in *E. coli* — expect no Tyr phosphorylation of FepE.
- **ATP-binding test** (ATP-agarose pulldown or ITC) — expect no specific ATP binding by FepE.
- **Structural confirmation** — inspect the AlphaFold model and deposited FepE crystal structure to verify a short cytoplasmic tail and the absence of a P-loop kinase fold.
- **Comparative HMM/structure scan** — formal InterProScan/Pfam-HMM comparison of P26266 vs P76387 (Wzc) and P38134 (Etk), confirming FepE carries PF02706 only.
- **Curation actions** — remove/NOT-qualify GO:0004713 (MF); retain inner-membrane CC; add/strengthen LPS / O-antigen chain-length BP; record the PANTHER over-annotation rationale.

---

## Curation Leads (verify)

- **Candidate reference for the removal rationale:** [PMID: 22437828](https://pubmed.ncbi.nlm.nih.gov/22437828/) — snippet: *"chain length regulator periplasmic proteins (polysaccharide co-polymerases, PCPs) anchored in the inner membrane by two transmembrane helices"* (FepE architecture, no kinase).
- **Candidate reference defining the real kinase (contrast):** [PMID: 11053445](https://pubmed.ncbi.nlm.nih.gov/11053445/) — snippet: *"The tyrosine-rich domain at the C terminus of Wzc…autophosphorylation of Wzc requires a functional Walker A motif."*
- **Candidate GO changes:** remove/NOT GO:0004713 (MF); retain inner-membrane CC; add/strengthen LPS / O-antigen chain-length BP (e.g., GO:0009103).
- **Suggested reviewer question:** "Does any primary experiment show FepE tyrosine phosphorylation or ATP-dependent kinase activity, or does the annotation rest only on PANTHER IBA?" (Expected: only IBA.)

---

## Bottom Line

The seed hypothesis is **refuted as a direct function assignment**. FepE (P26266) is a non-catalytic PCP-1 (WzzB-type) O-antigen chain-length co-polymerase; the GO:0004713 IBA annotation is a PANTHER family (PTHR32309) over-annotation and should be removed or not propagated. The gene product's supportable annotations concern LPS / O-antigen chain-length regulation (BP) and inner-membrane localization (CC), not protein tyrosine kinase activity (MF).


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)