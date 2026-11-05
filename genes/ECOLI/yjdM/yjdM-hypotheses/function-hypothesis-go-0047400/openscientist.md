---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-24T04:40:32.594059'
end_time: '2026-10-24T05:48:11.628811'
duration_seconds: 4059.03
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: ECOLI
  gene: yjdM
  gene_symbol: yjdM
  uniprot_accession: P0AFJ1
  taxon_id: NCBITaxon:83333
  taxon_label: Escherichia coli K-12
  focus_type: function_assignment
  hypothesis_slug: function-hypothesis-go-0047400
  hypothesis_text: yjdM has phosphonoacetate hydrolase activity (GO:0047400).
  term_context: '- Term: phosphonoacetate hydrolase activity (GO:0047400)

    - Evidence type: IDA

    - Original reference: PMID:37963869'
  reference_context: '- PMID:37963869

    - PMID:40703034

    - file:ECOLI/yjdM/yjdM-deep-research-falcon.md'
  source_file: genes/ECOLI/yjdM/yjdM-ai-review.yaml
  source_selector: existing_annotations[3].function_hypothesis
  source_context_yaml: "term:\n  id: GO:0047400\n  label: phosphonoacetate hydrolase\
    \ activity\nevidence_type: IDA\noriginal_reference_id: PMID:37963869"
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
citation_count: 7
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
- **Taxon:** Escherichia coli K-12 (NCBITaxon:83333)
- **Gene directory:** yjdM
- **Gene symbol:** yjdM
- **UniProt accession:** P0AFJ1

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** function-hypothesis-go-0047400
- **Source file:** genes/ECOLI/yjdM/yjdM-ai-review.yaml
- **Source selector:** existing_annotations[3].function_hypothesis

## Seed Hypothesis

yjdM has phosphonoacetate hydrolase activity (GO:0047400).

## Term and Decision Context

- Term: phosphonoacetate hydrolase activity (GO:0047400)
- Evidence type: IDA
- Original reference: PMID:37963869

## Reference Context

- PMID:37963869
- PMID:40703034
- file:ECOLI/yjdM/yjdM-deep-research-falcon.md

## Source Context YAML

```yaml
term:
  id: GO:0047400
  label: phosphonoacetate hydrolase activity
evidence_type: IDA
original_reference_id: PMID:37963869
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

## Target: *E. coli* K-12 yjdM (UniProt P0AFJ1)
## Hypothesis under review: yjdM has phosphonoacetate hydrolase activity (GO:0047400), IDA, PMID:37963869

---

## Executive Judgment

**Verdict: Over-annotated / weakly supported — the GO:0047400 annotation should be removed, or at minimum downgraded and qualified as in-vitro-only and non-core.**

The single IDA annotation asserting that yjdM/P0AFJ1 has **phosphonoacetate hydrolase activity (GO:0047400, EC 3.11.1.2)** rests entirely on one machine-learning-prediction-plus-in-vitro study (DeepECtransformer, [PMID:37963869](https://pubmed.ncbi.nlm.nih.gov/37963869/)). A subsequent peer-reviewed reassessment ([PMID:40703034](https://pubmed.ncbi.nlm.nih.gov/40703034/)) explicitly concluded that "the PhnA activity observed in vitro is not supported," assigned the prediction the lowest possible confidence score, and called for additional in vivo experiments. Three independent lines of evidence — structural/evolutionary, genetic/historical, and genomic-context — converge to refute the homology-based premise of the annotation and to identify the underlying cause as a **name collision** between two unrelated genes both historically called "phnA."

YjdM is a small (111-amino-acid) dual zinc-ribbon protein (Pfam PF03831 + PF08274; InterPro IPR004624) whose four N-terminal cysteines form a single tetrahedral Cys4 zinc-binding site. The canonical phosphonoacetate hydrolase enzyme, PhnA from *Pseudomonas fluorescens* 23F, is a ~400-residue alkaline-phosphatase-superfamily binuclear-metal hydrolase that "showed no significant homology with any data bank accessions." These two proteins share neither size, fold, catalytic architecture, nor sequence. The *E. coli* "phnA" synonym for yjdM is a 1990 positional/alphabetical label for the first open reading frame in a sequenced phosphonate-region cluster — a gene that was subsequently shown by mutational analysis to lie **outside** the functional phnC–phnP phosphonate-utilization operon.

The most important caveat is that yjdM's genuine biochemical function remains experimentally uncharacterized. Refuting the phosphonoacetate-hydrolase assignment does **not** tell us what yjdM does; it only tells us what it almost certainly does not do. The better-supported molecular-function lead is **zinc ion binding** (via the Cys4 ribbon), and the gene should otherwise be treated as a conserved zinc-ribbon protein of unknown primary function.

---

## Key Findings

### Finding 1 — The GO:0047400 annotation is over-annotated and traces to a single disputed source

The phosphonoacetate hydrolase (GO:0047400; EC 3.11.1.2) IDA annotation on yjdM/P0AFJ1 derives **solely** from the DeepECtransformer study ([PMID:37963869](https://pubmed.ncbi.nlm.nih.gov/37963869/)), which combined a deep-learning EC-number prediction with a limited in vitro validation. That paper states: *"We experimentally validated the enzymatic activities predicted for three proteins (YgfF, YciO, and YjdM),"* making clear that YjdM's phosphonoacetate-hydrolase assignment is a machine-learning prediction with in-vitro follow-up, not an independently established biochemical characterization.

Critically, a peer-reviewed reassessment of exactly these predictions ([PMID:40703034](https://pubmed.ncbi.nlm.nih.gov/40703034/)) reached the opposite conclusion. It states verbatim: *"In conclusion, the PhnA activity observed in vitro is not supported, and additional in vivo experiments are required to confirm the biological role of this enzyme."* This reassessment assigned the YjdM prediction the lowest confidence score in its scheme (CS = 1). When the sole source of an IDA annotation is directly contradicted by a later peer-reviewed paper, the IDA code — which signifies a direct, reproducible experimental demonstration of function — is no longer appropriate.

The same reassessment also undercut the genomic rationale for a phosphonate role: *"However, except for E. coli, yjdM genes are generally not close to phosphonate catabolism or transport genes."* In other words, the apparent association between yjdM and phosphonate metabolism is a coincidence of *E. coli* gene order and does not generalize across the ~12,000 members of the IPR004624 family.

### Finding 2 — Structural and evolutionary evidence refutes homology to the true PhnA enzyme

The canonical phosphonoacetate hydrolase, encoded by *phnA* of *Pseudomonas fluorescens* 23F, is a novel carbon–phosphorus bond-cleaving enzyme of the alkaline-phosphatase superfamily. On its original cloning, *"The nucleotide and deduced amino acid sequences of the phnA gene showed no significant homology with any data bank accessions"* ([PMID:9300819](https://pubmed.ncbi.nlm.nih.gov/9300819/)) — meaning it is not homologous to the small zinc-ribbon YjdM family. The true enzyme is ~400 residues and uses a binuclear metal center typical of its superfamily; its gene clusters with phosphonoacetate transport and LysR-type regulatory genes (phnR, phnB), not with zinc-ribbon genes ([PMID:11344133](https://pubmed.ncbi.nlm.nih.gov/11344133/)).

By contrast, YjdM is a 111-residue dual zinc-ribbon protein (Pfam PF03831 "YjdM" + PF08274 "Zn_Ribbon_YjdM"; InterPro IPR004624), with CxxC cysteine pairs at C6/C9 and C23/C26. The AlphaFold model AF-P0AFJ1-F1 (mean pLDDT 78.2 over 111 residues; radius of gyration 22.2 Å) places the four N-terminal cysteines C6, C9, C23 and C26 in a tight tetrahedral cluster — all pairwise SG–SG distances between 3.4 and 3.8 Å and a centroid radius of ~2.2 Å — the exact geometry of a single Cys4 structural zinc site. The fifth cysteine (C93) sits 46–49 Å away and is not part of the metal site. This is a **structural zinc-binding ribbon**, not the α/β binuclear-metal active site of an alkaline-phosphatase-superfamily hydrolase. No shared fold, no shared active-site chemistry, no sequence homology: the homology premise behind the GO:0047400 transfer fails on every structural axis.

### Finding 3 — The "phnA" name is a 1990 historical artifact; yjdM lies outside the functional phosphonate operon

The association between yjdM and phosphonate metabolism is rooted in nomenclature, not biology. In 1990, Chen et al. ([PMID:2155230](https://pubmed.ncbi.nlm.nih.gov/2155230/)) sequenced the *E. coli* B phosphonate region and identified *"Seventeen open reading frames (phnA to phnQ) … in one transcriptional direction,"* naming them alphabetically by position. "phnA" was simply the first ORF (b4108/yjdM) in that stretch — a positional label, not a demonstrated enzyme, and entirely unrelated to the independently named *Pseudomonas* phosphonoacetate hydrolase gene *phnA*.

Metcalf and Wanner ([PMID:8388873](https://pubmed.ncbi.nlm.nih.gov/8388873/)) then defined the functional operon by mutational analysis: *"All genes for phosphonate (Pn) utilization in Escherichia coli are in a large cluster of 14 genes named, in alphabetical order, phnC to phnP."* The functional phosphonate-utilization operon is **phnC–phnP** — it explicitly excludes phnA (yjdM) and phnB. Thus yjdM is genetically excluded from the C–P lyase pathway in its own organism.

Consistent with this, STRING (identifier 511145.b4108) returns the unknown-function neighbor **yjdN** as the top partner (score 0.917), followed by phn-operon genes (phnD 0.83, phnJ 0.82, phnH 0.82, phnG 0.79, phnK 0.76, phnI 0.72, phnC 0.71, phnM 0.71). These phn associations are driven by STRING's **genomic-neighborhood** channel and reflect the coincidental physical adjacency of yjdM to the phn operon in *E. coli* — precisely the confounder shown not to generalize across genomes ([PMID:40703034](https://pubmed.ncbi.nlm.nih.gov/40703034/)). They are circular, not independent functional evidence. The UniProt record P0AFJ1 carries only the keyword "Hydrolase" and, notably, no zinc-binding site feature despite the clear Cys4 ribbon — confirming that the record's current functional identity is entirely downstream of the single disputed study.

---

## Mechanistic Model / Interpretation

The chain of reasoning that produced the GO:0047400 annotation, and where it breaks, can be summarized as follows:

```
   Pseudomonas fluorescens 23F phnA           E. coli b4108 "phnA" (= yjdM)
   ~400 aa, alkaline-phosphatase              111 aa, dual zinc-ribbon
   superfamily, binuclear metal               (PF03831 + PF08274 / IPR004624)
   TRUE phosphonoacetate hydrolase            Cys4 structural zinc site
   (EC 3.11.1.2)                              (C6/C9/C23/C26, SG-SG 3.4-3.8 Å)
          |                                             |
          |         *** NAME COLLISION ***              |
          |   both historically called "phnA"          |
          +----------------------+----------------------+
                                 |
                                 v
             DeepECtransformer ML predicts EC 3.11.1.2 for YjdM
                          (PMID:37963869)
                                 |
                                 v
             Limited in vitro assay -> IDA GO:0047400 on P0AFJ1
                                 |
           +---------------------+---------------------+
           |                                           |
           v                                           v
   REFUTED by reassessment               REFUTED by genetics/structure:
   (PMID:40703034):                      - phnC-phnP operon excludes yjdM
   "PhnA activity ... not                  (PMID:8388873; PMID:2155230)
    supported" in vivo; CS=1             - no homology to true PhnA
   yjdM not near phosphonate               (PMID:9300819)
   genes outside E. coli                 - AlphaFold: Cys4 Zn ribbon, not
                                           a hydrolase active site
```

The evidence is best explained by a classic annotation-propagation failure: a **lexical name collision** between two phylogenetically and biochemically unrelated genes, amplified by (a) a machine-learning EC prediction, (b) a single in-vitro assay that a later study could not support in vivo, and (c) a genomic-neighborhood coincidence specific to *E. coli*. None of these constitute direct evidence that the YjdM gene product catalyzes C–P bond cleavage of phosphonoacetate.

The positive signal in the data points elsewhere. The conserved dual-zinc-ribbon architecture and the tetrahedral Cys4 geometry are the strongest, most reproducible structural features of YjdM. These support a **zinc ion binding** molecular function and suggest a nucleic-acid-associated or metal-structural role typical of zinc-ribbon proteins, though the specific biological process remains undetermined.

---

## Evidence Matrix

| Citation | Evidence type | Supports/Refutes/Qualifies | Claim tested | Key finding | Context | Confidence & limitations |
|---|---|---|---|---|---|---|
| [PMID:37963869](https://pubmed.ncbi.nlm.nih.gov/37963869/) | Computational (ML) + in-vitro assay | Source of hypothesis (weak) | YjdM has phosphonoacetate hydrolase activity | DeepECtransformer predicted EC 3.11.1.2; "experimentally validated … for three proteins (YgfF, YciO, and YjdM)" | *E. coli*, in vitro | Single study; ML-driven; in-vitro only; not reproduced in vivo |
| [PMID:40703034](https://pubmed.ncbi.nlm.nih.gov/40703034/) | Review/reassessment of primary predictions | **Refutes** | Whether YjdM PhnA activity is real | "the PhnA activity observed in vitro is not supported"; lowest confidence (CS=1); yjdM "generally not close to phosphonate catabolism or transport genes" outside *E. coli* | Cross-genome analysis | Peer-reviewed; directly addresses the exact prediction |
| [PMID:9300819](https://pubmed.ncbi.nlm.nih.gov/9300819/) | Structural/evolutionary (sequence) | **Refutes homology** | Is YjdM homologous to true PhnA? | True phosphonoacetate hydrolase "showed no significant homology with any data bank accessions"; ~400-aa novel C–P lyase | *Pseudomonas fluorescens* 23F | Establishes the true enzyme family is sequence-distinct from YjdM |
| [PMID:8388873](https://pubmed.ncbi.nlm.nih.gov/8388873/) | Mutant/genetic (TnphoA') | **Refutes** | Is yjdM part of the phosphonate operon? | Functional operon is "14 genes named … phnC to phnP" — excludes phnA(yjdM)/phnB | *E. coli* | Definitive genetic delimitation of the pathway |
| [PMID:2155230](https://pubmed.ncbi.nlm.nih.gov/2155230/) | Sequence/historical | **Refutes (name collision)** | Origin of the "phnA" name | "Seventeen open reading frames (phnA to phnQ) … in one transcriptional direction" — alphabetical/positional naming | *E. coli* B | Shows "phnA" is a positional label, not an enzymatic assignment |
| [PMID:11344133](https://pubmed.ncbi.nlm.nih.gov/11344133/) | Structural/functional (gene region) | Qualifies (true-enzyme context) | Genomic context of the real phnA | Real phnA clusters with phnR (LysR regulator) and phnB (transporter), not zinc-ribbon genes | *Pseudomonas fluorescens* 23F | Orientation for the authentic enzyme's pathway |
| AlphaFold AF-P0AFJ1-F1 | Structural (computational) | **Refutes active site; supports Zn binding** | Hydrolase active site or zinc site? | Cys C6/C9/C23/C26 form tetrahedral Cys4 cluster (SG–SG 3.4–3.8 Å); C93 is 46–49 Å away; mean pLDDT 78.2 | Model, 111 aa | Model-based; geometry unambiguous for a structural zinc ribbon |
| STRING 511145.b4108 | Interaction/association (database) | Competing artifact | Does yjdM functionally associate with phn genes? | Top partner yjdN (0.917); phn links (0.71–0.83) via neighborhood channel | *E. coli* | Neighborhood-channel-driven; circular with *E. coli* gene order |

---

## GO Curation Implications

**Lead requiring curator verification:** Remove, or downgrade and qualify, the **GO:0047400 (phosphonoacetate hydrolase activity)** IDA annotation on P0AFJ1.

- **Molecular Function (the disputed term):** The IDA evidence code is not justified. The sole supporting study ([PMID:37963869](https://pubmed.ncbi.nlm.nih.gov/37963869/)) is machine-learning-driven with in-vitro-only validation, and it is directly contradicted in vivo by a peer-reviewed reassessment ([PMID:40703034](https://pubmed.ncbi.nlm.nih.gov/40703034/)). Recommended actions, in order of preference: (1) **remove** GO:0047400; or (2) if retained provisionally, **change the evidence code away from IDA** to a weaker/qualified code and flag it as in-vitro-only and non-core, with a curator note citing PMID:40703034.
- **Better-supported MF lead:** Add **zinc ion binding (GO:0008270)** based on the conserved Cys4 ribbon (AlphaFold tetrahedral geometry; Pfam PF03831/PF08274; InterPro IPR004624). Label as structural/computational inference (ISS/structural) pending experimental confirmation, not IDA.
- **Cellular Component:** Retain **cytosol (GO:0005829)** if independently supported; not in conflict with the above.
- **Biological Process:** No specific BP is supported. Do **not** annotate phosphonate catabolic process. The gene is genetically excluded from the phnC–phnP operon ([PMID:8388873](https://pubmed.ncbi.nlm.nih.gov/8388873/)).

The net recommendation is that GO:0047400 should **not** be treated as yjdM's function, and yjdM should be curated as a conserved zinc-ribbon protein of **unknown primary function** with a zinc-binding structural feature.

---

## Mechanistic Scope

The immediate molecular function being tested is the direct catalysis of C–P bond cleavage of phosphonoacetate (EC 3.11.1.2) by the YjdM polypeptide. The evidence relevant to that **direct gene-product activity** is: (a) one ML prediction + in-vitro assay that was not reproduced in vivo; (b) the absence of any sequence or structural homology to the true enzyme family; and (c) a structural model showing a zinc-binding ribbon rather than a hydrolase active site. None of these support direct catalytic activity.

The signals that might superficially *suggest* a phosphonate role are all **downstream or contextual**, not direct: the "phnA" name (a lexical artifact), the *E. coli*-specific genomic neighborhood (a gene-order coincidence), and STRING associations (a neighborhood-channel inference derived from that same coincidence). No loss-of-function phenotype, no in vivo growth-on-phosphonate dependency, and no biochemical reconstitution establishes a phosphonate-catabolic role for yjdM.

---

## Conflicts and Alternatives

1. **Name collision (primary alternative explanation).** Two unrelated genes are both called "phnA": the *Pseudomonas fluorescens* 23F phosphonoacetate hydrolase ([PMID:9300819](https://pubmed.ncbi.nlm.nih.gov/9300819/); [PMID:11344133](https://pubmed.ncbi.nlm.nih.gov/11344133/)) and the *E. coli* b4108/yjdM ORF ([PMID:2155230](https://pubmed.ncbi.nlm.nih.gov/2155230/)). The GO transfer appears to have flowed across this lexical bridge rather than across genuine homology.

2. **Organism-specific genomic context.** The yjdM–phn adjacency is specific to *E. coli*; across the broader IPR004624 family it does not hold ([PMID:40703034](https://pubmed.ncbi.nlm.nih.gov/40703034/)). Any functional inference from *E. coli* gene order is therefore not generalizable.

3. **In-vitro-only artifact.** The reassessment ([PMID:40703034](https://pubmed.ncbi.nlm.nih.gov/40703034/)) frames the in-vitro activity as unsupported in vivo — consistent with a spurious or promiscuous low-level activity under non-physiological conditions, a well-known risk when validating ML enzyme predictions.

4. **Database carry-over.** The UniProt "Hydrolase" keyword and the GO IDA together now form a self-reinforcing record even though they derive from a single disputed study; the missing zinc-binding feature annotation shows the record under-represents the best structural evidence.

**Alternative interpretation favored by the data:** YjdM is a zinc-ribbon protein whose conserved function involves zinc binding and, plausibly, nucleic-acid association (a common role for zinc ribbons), but whose specific biological process is uncharacterized.

---

## Evidence Base

| PMID | Title (abbrev.) | Role in this assessment |
|---|---|---|
| [37963869](https://pubmed.ncbi.nlm.nih.gov/37963869/) | DeepECtransformer ML enzyme prediction + validation | Sole source of the GO:0047400 IDA (ML + in-vitro) |
| [40703034](https://pubmed.ncbi.nlm.nih.gov/40703034/) | Reassessment of the predictions | Refutes: in-vitro PhnA activity "not supported" in vivo; CS=1 |
| [9300819](https://pubmed.ncbi.nlm.nih.gov/9300819/) | Cloning of *Pseudomonas* phosphonoacetate hydrolase | True enzyme is non-homologous to YjdM |
| [11344133](https://pubmed.ncbi.nlm.nih.gov/11344133/) | phnA gene region analysis in *P. fluorescens* 23F | True enzyme's pathway/regulatory context (phnR, phnB) |
| [8388873](https://pubmed.ncbi.nlm.nih.gov/8388873/) | TnphoA' mutational analysis of the phn operon | Functional operon is phnC–phnP; excludes yjdM |
| [2155230](https://pubmed.ncbi.nlm.nih.gov/2155230/) | Sequence of the *E. coli* phosphonate region | "phnA" is a positional/alphabetical label (name collision) |
| [21261917](https://pubmed.ncbi.nlm.nih.gov/21261917/) | Phosphonoacetate biosensor via PhnR | Orientation on the true phosphonoacetate degradative system |

The literature cleanly separates into two groups. The *Pseudomonas* phosphonoacetate-hydrolase papers ([PMID:9300819](https://pubmed.ncbi.nlm.nih.gov/9300819/), [PMID:11344133](https://pubmed.ncbi.nlm.nih.gov/11344133/), [PMID:21261917](https://pubmed.ncbi.nlm.nih.gov/21261917/)) describe the authentic EC 3.11.1.2 enzyme — large, non-homologous to YjdM, and embedded in its own phnR/phnB regulatory and transport context. The *E. coli* genetics papers ([PMID:2155230](https://pubmed.ncbi.nlm.nih.gov/2155230/), [PMID:8388873](https://pubmed.ncbi.nlm.nih.gov/8388873/)) show that the *E. coli* "phnA" label is positional and that yjdM sits outside the functional phnC–phnP operon. The two modern papers ([PMID:37963869](https://pubmed.ncbi.nlm.nih.gov/37963869/) and [PMID:40703034](https://pubmed.ncbi.nlm.nih.gov/40703034/)) are, respectively, the origin and the refutation of the annotation under review.

---

## Limitations and Knowledge Gaps

- **True function unknown.** Refuting phosphonoacetate hydrolase activity does not identify what yjdM actually does. The zinc-ribbon architecture suggests zinc binding and possibly nucleic-acid interaction, but no primary literature establishing an alternative function was found. *Resolved by:* targeted biochemistry and genetics (below).
- **AlphaFold is a model.** The Cys4 geometry is derived from a predicted structure (mean pLDDT 78.2), not an experimental structure. The geometry is unambiguous and internally consistent, but experimental confirmation (zinc content, EXAFS, or crystallography) is lacking. *Resolved by:* metal-content analysis and structure determination.
- **In-vitro assay details not independently re-examined here.** We rely on the reassessment's conclusion ([PMID:40703034](https://pubmed.ncbi.nlm.nih.gov/40703034/)) rather than re-analyzing the raw DeepECtransformer assay data. *Resolved by:* curator inspection of PMID:37963869 supplementary data and PMID:40703034 scoring rationale.
- **Snippet verification status.** Several key quotes (PMID:40703034, PMID:37963869, PMID:2155230) are flagged "unchecked" in the knowledge state; the PMID:9300819 and PMID:8388873 snippets are verified. A curator should confirm the unchecked snippets against the source abstracts.

---

## Discriminating Tests

1. **In vivo phosphonoacetate growth assay.** Test whether a yjdM deletion abolishes, and complementation restores, growth on phosphonoacetate as sole phosphorus source in *E. coli*. The phnC–phnP genetics predict **no** yjdM dependence. Most decisive single experiment.
2. **Purified-enzyme kinetics with proper controls.** Re-measure phosphonoacetate hydrolase activity of purified YjdM against a true PhnA positive control and a catalytically-dead negative control, with metal-dependence profiling. Distinguishes genuine catalysis from a non-specific in-vitro signal.
3. **Metal-content determination.** ICP-MS / atomic absorption on purified YjdM to confirm stoichiometric zinc, plus mutagenesis of C6/C9/C23/C26 to test zinc dependence of folding/stability. Confirms the Cys4 zinc site.
4. **Cross-genome synteny and phylogenetics.** Formal analysis of IPR004624 members' gene neighborhoods to confirm the *E. coli* phn adjacency is not conserved — operationalizes the PMID:40703034 observation quantitatively.
5. **Structural biology.** Crystallography or cryo-EM of YjdM (or ortholog) to test the zinc-ribbon model and rule out any hydrolase active-site pocket.

---

## Proposed Follow-up Actions / Curation Leads (require curator verification)

**Candidate action change:**
- GO:0047400 (phosphonoacetate hydrolase activity): **remove** or **downgrade/qualify** — change evidence away from IDA; mark in-vitro-only, non-core; add curator note citing the refuting reassessment.

**Candidate new/replacement GO terms:**
- Add **GO:0008270 zinc ion binding** (MF) as a structural/computational lead (Cys4 ribbon; IPR004624; AlphaFold tetrahedral geometry) — label as ISS/structural, not IDA.
- Retain **GO:0005829 cytosol** (CC) if independently supported.
- Do **not** add any phosphonate catabolic process (BP).

**Candidate references and exact snippets to verify:**
- [PMID:40703034](https://pubmed.ncbi.nlm.nih.gov/40703034/): *"In conclusion, the PhnA activity observed in vitro is not supported, and additional in vivo experiments are required to confirm the biological role of this enzyme."* and *"However, except for E. coli, yjdM genes are generally not close to phosphonate catabolism or transport genes."*
- [PMID:37963869](https://pubmed.ncbi.nlm.nih.gov/37963869/): *"We experimentally validated the enzymatic activities predicted for three proteins (YgfF, YciO, and YjdM)."*
- [PMID:8388873](https://pubmed.ncbi.nlm.nih.gov/8388873/): *"All genes for phosphonate (Pn) utilization in Escherichia coli are in a large cluster of 14 genes named, in alphabetical order, phnC to phnP."*
- [PMID:2155230](https://pubmed.ncbi.nlm.nih.gov/2155230/): *"Seventeen open reading frames (phnA to phnQ) were identified in one transcriptional direction."*
- [PMID:9300819](https://pubmed.ncbi.nlm.nih.gov/9300819/): *"The nucleotide and deduced amino acid sequences of the phnA gene showed no significant homology with any data bank accessions."*

**Suggested curator questions:**
- Does the GO IDA annotation cite any evidence independent of PMID:37963869? (Finding: no.)
- Has the in-vitro activity ever been reproduced in vivo? (Finding: no — explicitly unsupported per PMID:40703034.)
- Should UniProt P0AFJ1 gain a zinc-binding site feature (C6/C9/C23/C26)? (Recommended: yes, pending confirmation.)

**Suggested experiments:** the five discriminating tests above, prioritizing the in vivo phosphonoacetate growth assay in a yjdM deletion background.

---

*Prepared for AI Gene Review hypothesis-level curation. All quantitative and structural claims above are drawn from the cited primary literature, the AlphaFold AF-P0AFJ1-F1 model, and public STRING/UniProt records. Computational results (AlphaFold geometry, STRING scores) are reported as model/database-derived inferences, distinct from direct experimental results.*


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)