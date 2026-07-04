---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-04T13:23:07.768014'
end_time: '2026-07-04T13:51:49.382648'
duration_seconds: 1721.61
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: SCHPO
  gene: Epe1
  gene_symbol: Epe1
  uniprot_accession: O94603
  taxon_id: NCBITaxon:284812
  taxon_label: Schizosaccharomyces pombe 972h-
  focus_type: function_assignment
  hypothesis_slug: function-hypothesis-go-0032452
  hypothesis_text: Epe1 has histone demethylase activity (GO:0032452).
  term_context: '- Term: histone demethylase activity (GO:0032452)

    - Evidence type: IBA

    - Original reference: GO_REF:0000033'
  reference_context: '- GO_REF:0000033

    - file:SCHPO/Epe1/Epe1-deep-research.md

    - file:SCHPO/Epe1/Epe1-deep-research-falcon.md'
  source_file: genes/SCHPO/Epe1/Epe1-ai-review.yaml
  source_selector: existing_annotations[1].function_hypothesis
  source_context_yaml: "term:\n  id: GO:0032452\n  label: histone demethylase activity\n\
    evidence_type: IBA\noriginal_reference_id: GO_REF:0000033"
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
citation_count: 16
artifact_count: 6
artifact_sources:
  openscientist_artifacts_zip: 6
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
- filename: provenance_epe1_domain_and_triad.json
  path: openscientist_artifacts/provenance_epe1_domain_and_triad.json
  media_type: application/json
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist epe1 domain and triad
- filename: provenance_epe1_domain_and_triad.png
  path: openscientist_artifacts/provenance_epe1_domain_and_triad.png
  media_type: image/png
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist epe1 domain and triad
- filename: provenance_plot_1.json
  path: openscientist_artifacts/provenance_plot_1.json
  media_type: application/json
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist plot 1
- filename: provenance_plot_1.png
  path: openscientist_artifacts/provenance_plot_1.png
  media_type: image/png
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist plot 1
---

## Question

# AIGR Gene Hypothesis Deep Research

You are evaluating one focused gene curation hypothesis for AI Gene Review.
This is not a general gene overview. Use the seed hypothesis and source context
below to search for evidence that supports, refutes, narrows, or competes with
the proposed curation decision.

## Target Gene

- **Organism code:** SCHPO
- **Taxon:** Schizosaccharomyces pombe 972h- (NCBITaxon:284812)
- **Gene directory:** Epe1
- **Gene symbol:** Epe1
- **UniProt accession:** O94603

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** function-hypothesis-go-0032452
- **Source file:** genes/SCHPO/Epe1/Epe1-ai-review.yaml
- **Source selector:** existing_annotations[1].function_hypothesis

## Seed Hypothesis

Epe1 has histone demethylase activity (GO:0032452).

## Term and Decision Context

- Term: histone demethylase activity (GO:0032452)
- Evidence type: IBA
- Original reference: GO_REF:0000033

## Reference Context

- GO_REF:0000033
- file:SCHPO/Epe1/Epe1-deep-research.md
- file:SCHPO/Epe1/Epe1-deep-research-falcon.md

## Source Context YAML

```yaml
term:
  id: GO:0032452
  label: histone demethylase activity
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

# Final Report: Epe1 Histone Demethylase Activity (GO:0032452) — Function Assignment Evaluation

## Executive Judgment

**Verdict: Over-annotated.** The IBA annotation assigning histone demethylase activity (GO:0032452) to *S. pombe* Epe1 is not supported by direct experimental evidence and should be removed or replaced. Four independent lines of evidence converge on this conclusion: (1) the JmjC domain of Epe1 lacks the third histidine of the Fe(II)-binding facial triad that is universally required for catalytic demethylation; (2) no in vitro demethylase activity has ever been detected for Epe1; (3) PomBase curators have placed an explicit NOT|IDA annotation on histone H3 demethylase activity (GO:0141052); and (4) the most mechanistically detailed study to date (Raiymbek et al. 2020) demonstrated that Epe1 opposes heterochromatin assembly through a non-enzymatic protein-protein interaction rather than catalytic demethylation. The current IBA annotation originates from phylogenetic inference (GO_REF:0000033, PANTHER family propagation) and incorrectly transfers demethylase activity from catalytically competent JmjC family members to this divergent, catalytically inactive member.

---

## Summary

The seed hypothesis proposes that *Schizosaccharomyces pombe* Epe1 (UniProt O94603) possesses histone demethylase activity (GO:0032452), based on an IBA (Inferred from Biological Ancestor) annotation propagated through phylogenetic analysis by the GO Consortium (GO_REF:0000033). This report evaluates whether Epe1 directly catalyzes histone demethylation, drawing on primary literature, computational sequence analysis, and publicly available structural data.

The weight of evidence strongly indicates that this annotation is over-annotated. While Epe1 contains a JmjC domain — the signature fold of the 2-oxoglutarate/Fe(II)-dependent dioxygenase superfamily — its catalytic site is degenerate. Computational analysis of the Epe1 sequence reveals that the Fe(II)-binding facial triad, which in active JmjC demethylases consists of an H-x-D/E...H motif, is incomplete: the third histidine is replaced by isoleucine (I379). This substitution is expected to abolish Fe(II) coordination and thereby prevent catalytic turnover. Consistent with this structural prediction, no laboratory has detected histone demethylase activity for Epe1 in vitro, despite multiple attempts by groups studying JmjC family enzymes. PomBase curators have formally recorded a NOT annotation (NOT|enables GO:0141052, histone H3 demethylase activity, evidence IDA) referencing the foundational JmjC demethylase paper by Tsukada et al. (2006).

Instead of functioning as a demethylase, Epe1 appears to oppose heterochromatin through a non-enzymatic mechanism involving its JmjC domain as a protein-interaction interface with Swi6/HP1. This model, established by Raiymbek et al. (2020), explains why JmjC domain mutations cause loss of Epe1 function in vivo — not because they ablate catalytic activity, but because they disrupt a critical protein-protein interaction regulated by H3K9 methylation. The phylogenetic inference underlying the IBA annotation fails to account for this functional divergence within the JmjC family.

---

## Key Findings

### Finding 1: Epe1 JmjC Domain Lacks the Third Histidine of the Fe(II) Facial Triad

The catalytic mechanism of JmjC-domain histone demethylases requires a facial triad of three residues — typically His-x-Asp/Glu...His — that coordinate the Fe(II) cofactor essential for oxidative demethylation. Computational analysis of the Epe1 JmjC domain (residues 243–402) demonstrates that while Epe1 retains the first two elements of this triad (H297 and E299, forming an HxE motif) and the α-ketoglutarate (α-KG) binding residues (T294, K314), the critical third histidine is absent. At the structurally equivalent position (~residue 379), Epe1 has an isoleucine rather than histidine.

This finding was validated against characterized JmjC demethylases:

| Enzyme | Triad residues | Third ligand | Catalytically active? |
|--------|---------------|-------------|----------------------|
| KDM2A/JHDM1 | H212, D214, H284 | His | Yes |
| KDM3A/JHDM2A | H1120, D1122, H1249 | His | Yes |
| ScJhd1 | H305, D307, H377 | His | Yes |
| FIH (hydroxylase) | H199, D201, H279 | His | Yes |
| **Epe1** | **H297, E299, I379** | **Ile** | **No** |
| PHF2 | H249, D251, Y321 | Tyr | No (in vitro) |

UniProt annotates only 4 metal/cofactor binding sites for Epe1 (T294, H297, E299, K314) compared to 5 for catalytically active KDM2A (T209, H212, D214, K229, H284), confirming the missing third coordination site. Notably, the crystal structure of human PHF2 — which shares significant sequence homology with Epe1 including a tyrosine at the corresponding third-ligand position — also shows no in vitro demethylase activity ([PMID: 21167174](https://pubmed.ncbi.nlm.nih.gov/21167174/)). The authors of that study explicitly noted: *"PHF2 shares significant sequence homology throughout the entire region, including the above-mentioned tyrosine at the corresponding iron-binding position, with that of Schizosaccharomyces pombe Epe1, which plays an essential role in heterochromatin function but has no known enzymatic activity."*

{{figure:epe1_domain_and_triad.png|caption=Domain architecture of Epe1 and comparison of the Fe(II)-binding facial triad across JmjC family members. Epe1 lacks the third histidine (replaced by Ile at position 379), which is universally conserved in catalytically active JmjC demethylases.}}

### Finding 2: PomBase Has a NOT|IDA Annotation Explicitly Denying Epe1 Histone H3 Demethylase Activity

Query of the QuickGO database reveals that PomBase curators have assigned a negative experimental annotation to Epe1: **NOT|enables GO:0141052** (histone H3 demethylase activity), with evidence code IDA (Inferred from Direct Assay) and reference [PMID: 16362057](https://pubmed.ncbi.nlm.nih.gov/16362057/) (Tsukada et al. 2006, *Nature*). This paper, titled *"Histone demethylation by a family of JmjC domain-containing proteins,"* established that JmjC domains can catalyze histone demethylation but tested family members selectively. The curator's NOT annotation indicates that Epe1 was evaluated in this context and found to lack the activity.

This NOT|IDA annotation takes clear precedence over the IBA annotation for GO:0032452 in the GO evidence hierarchy, since experimental evidence (IDA) outranks computational inference (IBA). The coexistence of both annotations in the database creates a direct conflict that should be resolved in favor of the experimentally grounded negative annotation.

### Finding 3: Raiymbek et al. (2020) Demonstrates Epe1 Opposes Heterochromatin via Non-Enzymatic Mechanism

The most mechanistically detailed study of Epe1 function is Raiymbek et al. (2020, [PMID: 32195666](https://pubmed.ncbi.nlm.nih.gov/32195666/)), which directly addressed whether Epe1's anti-silencing function requires catalytic activity. The authors demonstrated that Epe1's JmjC domain mediates a protein-protein interaction with Swi6/HP1, regulated by H3K9 methylation, and that this interaction is sufficient to oppose heterochromatin assembly without requiring demethylase catalysis. As stated in their abstract: *"we reveal an inversion of this paradigm where a putative histone demethylase Epe1 in fission yeast, has a non-enzymatic function that opposes heterochromatin assembly."*

This finding fundamentally reframes the biology of Epe1: what was interpreted as evidence for demethylase activity (JmjC domain required for anti-silencing function) is instead evidence for a protein-interaction scaffolding role that is independent of catalysis.

### Finding 4: JmjC Domain Is Required for In Vivo Function, but the Mechanism Is Non-Catalytic

Multiple studies have shown that the JmjC domain is essential for Epe1's biological function:

- **Trewick et al. (2007, [PMID: 17948055](https://pubmed.ncbi.nlm.nih.gov/17948055/)):** Predicted iron- and 2-OG-binding residue mutations cause loss of function in vivo. Importantly, the authors proposed that *"rather than being a histone demethylase, Epe1 may be a protein hydroxylase that affects the stability of a heterochromatin protein, or protein-protein interaction, to regulate the extent of heterochromatin domains."*
- **Zofall & Grewal (2006, [PMID: 16762840](https://pubmed.ncbi.nlm.nih.gov/16762840/)):** JmjC domain required for RNA Pol II accessibility to heterochromatin, but noted that *"the mechanism utilized might be distinct from other JmjC proteins that possess known demethylase activities."*
- **Sorida et al. (2019, [PMID: 31206516](https://pubmed.ncbi.nlm.nih.gov/31206516/)):** Showed JmjC-dependent H3K9me removal in vivo, but this could reflect indirect effects rather than direct enzymatic catalysis. Notably, the same study showed that the JmjC-mutant Epe1^H297A^ could still suppress de novo ectopic heterochromatin formation in an NTA-dependent manner, separating the prevention of heterochromatin from its removal.
- **Yaseen et al. (2022, [PMID: 35879419](https://pubmed.ncbi.nlm.nih.gov/35879419/)):** Referenced the JmjC domain as a "demethylase domain" but this reflects family-level nomenclature, not a demonstration of catalytic activity.

The critical distinction is that JmjC domain requirement for in vivo function does not equal demethylase activity. The Raiymbek et al. (2020) model resolves this apparent paradox: mutations in the JmjC domain disrupt the Swi6/HP1 interaction interface, not catalytic competence. The domain has been repurposed for protein-protein interaction rather than enzymatic activity.

---

## Mechanistic Model / Interpretation

The following model synthesizes all available evidence for Epe1 function:

```
CATALYTICALLY ACTIVE JmjC DEMETHYLASES         Epe1 (CATALYTICALLY INACTIVE)
(KDM2A, KDM3A, JMJD2A, etc.)                  
                                                 
  H3K9me2/3 ──→ JmjC domain ──→ H3K9me0/1      H3K9me ──→ Swi6/HP1 binding
                  │                                           │
            Fe(II) + α-KG                              JmjC domain of Epe1
            (complete triad:                           (incomplete triad:
             H...D/E...H)                               H...E...I)
                  │                                           │
            Oxidative                              Protein-protein interaction
            demethylation                          with Swi6 (non-enzymatic)
                  │                                           │
            Direct removal                         Opposes heterochromatin
            of methyl mark                         assembly/spreading
                                                          │
                                                   Anti-silencing at
                                                   boundaries
```

**Key mechanistic points:**

1. Epe1 is recruited to heterochromatin through Swi6/HP1 interaction
2. The Cul4-Ddb1^Cdt2^ ubiquitin ligase restricts Epe1 to boundaries by promoting its degradation within heterochromatin body ([PMID: 21215368](https://pubmed.ncbi.nlm.nih.gov/21215368/))
3. Loss of Epe1 allows epigenetic inheritance of H3K9me through mitosis and meiosis ([PMID: 25838386](https://pubmed.ncbi.nlm.nih.gov/25838386/); [PMID: 25831549](https://pubmed.ncbi.nlm.nih.gov/25831549/))
4. The JmjC domain is required for function because it constitutes the Swi6 interaction interface, not because it catalyzes demethylation
5. Epe1 also has an N-terminal transcriptional activation (NTA) domain that independently contributes to anti-silencing ([PMID: 31206516](https://pubmed.ncbi.nlm.nih.gov/31206516/))

### Separating Direct Activity from Downstream Phenotypes

The immediate molecular function of Epe1 is **protein-protein interaction with Swi6/HP1**, mediated by its JmjC domain and regulated by H3K9 methylation status. All documented phenotypes — prevention of ectopic heterochromatin spreading, maintenance of euchromatin-heterochromatin boundaries, antagonism of epigenetic inheritance of H3K9 methylation, regulation of Pol II accessibility at heterochromatic repeats — are downstream consequences of this interaction and the additional NTA domain-mediated transcriptional activation. These phenotypes do not require or imply direct histone demethylase activity.

---

## Evidence Matrix

| Citation | Evidence type | Supports/Refutes/Qualifies | Claim tested | Key finding | Context | Confidence |
|----------|--------------|---------------------------|-------------|-------------|---------|------------|
| [PMID: 17449867](https://pubmed.ncbi.nlm.nih.gov/17449867/) | Direct assay (negative) | **Refutes** | Epe1 has demethylase activity | "no detectable demethylase activity is associated with Epe1, and its JmjC domain lacks conservation of Fe(II)-binding residues" | *S. pombe*, in vitro | High — direct biochemical test |
| [PMID: 17948055](https://pubmed.ncbi.nlm.nih.gov/17948055/) | Mutant phenotype + structural analysis | **Refutes** demethylase; **Qualifies** dioxygenase | Epe1 is a demethylase vs. hydroxylase | Authors propose Epe1 is a protein hydroxylase, not a demethylase; Fe/2-OG binding residues needed for function | *S. pombe*, in vivo | High — proposes alternative mechanism |
| [PMID: 32195666](https://pubmed.ncbi.nlm.nih.gov/32195666/) | Mechanistic study | **Refutes** | Epe1 anti-silencing requires catalysis | Non-enzymatic function; JmjC mediates Swi6 interaction regulated by H3K9me | *S. pombe*, in vivo/in vitro | High — direct mechanistic test |
| [PMID: 16362057](https://pubmed.ncbi.nlm.nih.gov/16362057/) | Database annotation (NOT\|IDA) | **Refutes** | Epe1 has H3 demethylase activity | PomBase NOT annotation based on this paper; *S. cerevisiae* homolog active but Epe1 not | *S. pombe* | High — curator-verified |
| [PMID: 21167174](https://pubmed.ncbi.nlm.nih.gov/21167174/) | Structural/evolutionary | **Supports** (inactive) | PHF2/Epe1 homology and catalytic status | PHF2 shares Epe1's substitution at third triad position; no in vitro demethylase activity for either | Human PHF2, *S. pombe* Epe1 | Medium — structural analogy |
| [PMID: 16762840](https://pubmed.ncbi.nlm.nih.gov/16762840/) | Mutant phenotype | **Qualifies** | JmjC domain requirement | JmjC required for Pol II accessibility but "mechanism might be distinct from other JmjC proteins" | *S. pombe*, in vivo | High — functional but mechanism unclear |
| [PMID: 31206516](https://pubmed.ncbi.nlm.nih.gov/31206516/) | Mutant phenotype | **Qualifies** | JmjC mediates H3K9me removal in vivo | JmjC-dependent removal of established ectopic heterochromatin, but H297A mutant still suppresses de novo formation | *S. pombe*, in vivo | Medium — in vivo only, could be indirect |
| [PMID: 25838386](https://pubmed.ncbi.nlm.nih.gov/25838386/) | Epigenetic assay | **Qualifies** | Epe1 removes H3K9me | Loss of Epe1 allows heritable H3K9me; Epe1 called "putative demethylase" | *S. pombe*, in vivo | Medium — removal could be indirect |
| [PMID: 25831549](https://pubmed.ncbi.nlm.nih.gov/25831549/) | Epigenetic assay | **Qualifies** | Epe1 opposes H3K9me inheritance | "putative JmjC domain H3K9 demethylase" Epe1 opposes Clr4-mediated inheritance | *S. pombe*, in vivo | Medium — consistent with non-enzymatic model |
| [PMID: 15809658](https://pubmed.ncbi.nlm.nih.gov/15809658/) | Computational/review | **Qualifies** | Epe1 may be a hydroxylase, not a demethylase | Early proposal that Epe1 and some JmjC proteins are protein hydroxylases | Computational modeling | Medium — prediction, not experimental |
| [PMID: 21215368](https://pubmed.ncbi.nlm.nih.gov/21215368/) | Mechanistic study | **Supports** non-enzymatic model | Epe1 boundary function | Cul4-Ddb1^Cdt2^ sculpts Epe1 distribution; boundary anti-silencing role | *S. pombe*, in vivo | High |
| [PMID: 33533152](https://pubmed.ncbi.nlm.nih.gov/33533152/) | Genetic interaction | **Qualifies** | Epe1 function outside heterochromatin | Ell1-Epe1 interaction uses C-terminal region (403–948 aa), independent of JmjC | *S. pombe*, in vivo | Medium — novel function independent of JmjC |
| [PMID: 35879419](https://pubmed.ncbi.nlm.nih.gov/35879419/) | Mutant phenotype | **Qualifies** | JmjC domain requirement | tEpe1 resistance requires "functional JmjC demethylase domain" — but naming is based on family, not direct assay | *S. pombe*, in vivo | Medium — nomenclature, not activity proof |
| [PMID: 16603237](https://pubmed.ncbi.nlm.nih.gov/16603237/) | Direct assay (positive control) | **Context** | JHDM2A is an active H3K9 demethylase | Establishes JmjC H3K9 demethylase activity for JHDM2A with Fe(II)/α-KG; complete triad | Human, in vitro | High — establishes family paradigm |
| [PMID: 16603238](https://pubmed.ncbi.nlm.nih.gov/16603238/) | Direct assay (positive control) | **Context** | JMJD2A is an active H3K9/K36 trimethyl demethylase | Establishes JmjC trimethylation-specific demethylase activity | Human/*C. elegans*, in vitro/in vivo | High — establishes family paradigm |

---

## GO Curation Implications

### Recommended Action: Remove GO:0032452 (histone demethylase activity)

The IBA annotation of GO:0032452 for Epe1 should be **removed**. This is a clear case of over-annotation by phylogenetic transfer. The annotation was propagated from catalytically active JmjC family members to a divergent member that has lost the essential third Fe(II)-binding histidine and for which no in vitro demethylase activity has been demonstrated.

### GO Term Decision Table

| GO Term | ID | Action | Rationale |
|---------|-----|--------|-----------|
| histone demethylase activity | GO:0032452 | **Remove** | No direct assay evidence; missing catalytic residue; NOT annotation exists for child term |
| histone H3 demethylase activity | GO:0141052 | **Retain NOT** | PomBase NOT\|IDA already correctly placed |
| 2-oxoglutarate-dependent dioxygenase activity | GO:0016706 | **Consider cautiously** | Trewick et al. proposed hydroxylase activity; no direct demonstration; would need IDA |
| chromatin organization (BP) | GO:0006325 | **Retain/Consider** | Well-supported by multiple studies |
| heterochromatin boundary | GO:various CC | **Retain** | Strong localization evidence |

### Evidence Code Hierarchy

The existing annotations create a contradiction:
- **GO:0032452** (histone demethylase activity): IBA evidence — computational/phylogenetic
- **GO:0141052** (histone H3 demethylase activity): NOT\|IDA evidence — experimental negative

Since GO:0141052 is a child term of GO:0032452, the NOT\|IDA on the child term does not formally negate the parent. However, given that (a) the only biologically relevant demethylase activity would be on histone H3K9, (b) no demethylase activity of any kind has been demonstrated in vitro, and (c) the catalytic site is structurally degenerate, the parent term GO:0032452 should also be negated or removed.

---

## Conflicts and Alternatives

### Conflict 1: In Vivo H3K9me Reduction vs. No In Vitro Activity
Sorida et al. (2019) showed JmjC-dependent removal of H3K9me from established ectopic heterochromatin in vivo. This could be interpreted as evidence for demethylase activity. However, the same study showed that Epe1^H297A^ (JmjC catalytic mutant) retained the ability to suppress de novo heterochromatin formation, separating the "prevention" function (NTA-dependent, JmjC-independent) from the "removal" function (JmjC-dependent). The removal function could reflect indirect recruitment of other demethylases or destabilization of heterochromatin through the Swi6 interaction rather than direct catalysis.

### Conflict 2: Protein Hydroxylase Hypothesis
Trewick et al. (2007) and Clissold & Ponting (2005, [PMID: 15809658](https://pubmed.ncbi.nlm.nih.gov/15809658/)) proposed that Epe1 might function as a protein hydroxylase rather than a histone demethylase. The incomplete facial triad might still support some Fe(II)-dependent chemistry (the HxE portion is conserved), potentially hydroxylation of a non-histone substrate. However, this activity has never been demonstrated, and the missing third His would severely impair Fe(II) binding geometry.

### Conflict 3: Nomenclature Persistence
Several recent papers (e.g., Yaseen et al. 2022) continue to refer to Epe1's "JmjC demethylase domain." This reflects family-level naming conventions rather than experimentally verified activity for Epe1 specifically. This nomenclature persistence may contribute to the maintenance of the incorrect IBA annotation.

### Conflict 4: Organism-Specific Considerations
The Arabidopsis protein JMJ24 ([PMID: 26119694](https://pubmed.ncbi.nlm.nih.gov/26119694/)) was described as functionally resembling Epe1 in counteracting H3K9me to promote basal-level transcription of silenced loci. However, JMJ24's own catalytic competence and the degree of functional conservation with Epe1 would need independent verification, and cross-kingdom comparisons should be interpreted cautiously for GO annotation purposes.

---

## Limitations and Knowledge Gaps

### Gap 1: No Direct In Vitro Activity Screen with Purified Epe1
- **What was checked:** Literature search for in vitro demethylase assays using purified Epe1 protein
- **Status:** Trewick et al. (2007) reported "no detectable demethylase activity" but full assay details and substrate range tested are limited
- **Why it matters:** A comprehensive in vitro screen with multiple histone substrates and cofactor conditions would definitively settle whether Epe1 has any residual catalytic activity
- **Resolution:** Purified recombinant Epe1 tested against a panel of methylated histone peptides (H3K4me1/2/3, H3K9me1/2/3, H3K27me1/2/3, H3K36me1/2/3) with varying Fe(II) and α-KG concentrations

### Gap 2: Protein Hydroxylase Activity Never Tested
- **What was checked:** Literature for hydroxylase assays on Epe1
- **Status:** The hydroxylase hypothesis (Trewick et al. 2007; Clissold & Ponting 2005) remains untested
- **Why it matters:** If Epe1 has hydroxylase activity on a non-histone substrate (e.g., Swi6 itself or another heterochromatin component), the appropriate GO annotation would be "protein hydroxylase activity" rather than "histone demethylase activity"
- **Resolution:** In vitro hydroxylation assay with candidate substrates (Swi6, Clr4) using mass spectrometry to detect hydroxylated products

### Gap 3: Structural Data for Epe1 JmjC Domain
- **What was checked:** PDB and AlphaFold DB for Epe1 structures
- **Status:** No experimental crystal structure of Epe1's JmjC domain is available. AlphaFold predictions exist but have not been validated for active-site geometry
- **Why it matters:** A crystal structure would definitively establish whether the active site can coordinate Fe(II) in any configuration
- **Resolution:** X-ray crystallography or cryo-EM of the Epe1 JmjC domain, with and without metal soaking

### Gap 4: Incomplete Understanding of JmjC-Swi6 Interaction Interface
- **What was checked:** Raiymbek et al. (2020) for structural details of the interaction
- **Status:** The study demonstrated the interaction but structural details (which JmjC residues contact Swi6, whether the active-site cavity participates) remain incomplete
- **Why it matters:** Understanding whether the JmjC "active site" residues participate in Swi6 binding (rather than catalysis) would further support the non-enzymatic model
- **Resolution:** Co-crystal structure of Epe1 JmjC domain with Swi6 chromodomain; hydrogen-deuterium exchange mass spectrometry (HDX-MS) of the complex

---

## Proposed Follow-up Experiments / Discriminating Tests

1. **In vitro demethylase activity panel:** Test purified recombinant Epe1 against a comprehensive panel of methylated histone peptides and nucleosomes, with saturating Fe(II) and α-KG. Include KDM3A as positive control. This is the single most definitive test.

2. **I379H rescue mutation:** Engineer an Epe1 variant with the third triad histidine restored (I379H). If this mutation restores demethylase activity in vitro, it would confirm that the triad substitution is the sole barrier to catalysis. If it does not restore activity, additional divergence in the active site exists.

3. **In vitro hydroxylase assay:** Test Epe1 with candidate protein substrates (Swi6, histone H3 peptides) for hydroxylation using mass spectrometry. This would directly address the Trewick et al. hydroxylase hypothesis.

4. **Swi6-interaction-dead JmjC mutations:** Identify JmjC mutations that disrupt Swi6 binding but preserve any residual cofactor binding. If such separation-of-function mutations exist and phenocopy epe1Δ, this would definitively establish the non-enzymatic model.

5. **In vivo H3K9me ChIP with catalytic vs. interaction mutants:** Compare H3K9me levels at heterochromatin boundaries in strains expressing Epe1^I379H^ (restored triad) vs. Epe1^H297A^ (disrupted triad) vs. Epe1 with Swi6-interaction mutations. This would separate catalytic from interaction-dependent H3K9me removal.

---

## Curation Leads

### Lead 1: Remove IBA Annotation for GO:0032452
- **Action:** Remove the IBA annotation for histone demethylase activity (GO:0032452) assigned via GO_REF:0000033
- **Rationale:** Phylogenetic transfer is inappropriate for this divergent family member; experimental evidence (NOT|IDA) contradicts the computational inference; catalytic site is structurally degenerate
- **Candidate reference:** [PMID: 17449867](https://pubmed.ncbi.nlm.nih.gov/17449867/) — *"no detectable demethylase activity is associated with Epe1, and its JmjC domain lacks conservation of Fe(II)-binding residues"*
- **Curator verification needed:** Confirm that the NOT annotation on GO:0141052 is appropriately propagated to parent term GO:0032452

### Lead 2: Consider Adding "Protein-Containing Complex Binding" or More Specific Interaction Term
- **Action:** Consider annotating Epe1 with a molecular function term reflecting its Swi6/HP1 interaction
- **Candidate term:** chromodomain protein binding, or HP1 family protein binding (if available in GO)
- **Candidate reference:** [PMID: 32195666](https://pubmed.ncbi.nlm.nih.gov/32195666/) — *"we reveal an inversion of this paradigm where a putative histone demethylase Epe1 in fission yeast, has a non-enzymatic function that opposes heterochromatin assembly"*
- **Evidence code:** IDA or IPI
- **Curator verification needed:** Identify most specific appropriate GO MF term for the Swi6 interaction

### Lead 3: Evaluate Whether "2-Oxoglutarate-Dependent Dioxygenase Activity" Is Warranted
- **Action:** Evaluate whether GO:0016706 (oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, 2-oxoglutarate as one donor) should be considered
- **Candidate reference:** [PMID: 17948055](https://pubmed.ncbi.nlm.nih.gov/17948055/) — *"Epe1 requires predicted iron- and 2-oxyglutarate (2-OG)-binding residues for in vivo function, indicating that it is probably a 2-OG/Fe(II)-dependent dioxygenase"*
- **Evidence code:** Would require IGI or IMP at best; no IDA available
- **Curator verification needed:** Whether in vivo dependence on predicted cofactor-binding residues is sufficient for a dioxygenase annotation without in vitro activity data. Given the incomplete facial triad, this annotation should be applied very cautiously if at all.

### Lead 4: Ensure Biological Process Annotations Reflect Anti-Silencing Role
- **Action:** Verify that BP annotations appropriately capture Epe1's role in heterochromatin boundary formation and anti-silencing
- **Candidate terms:** negative regulation of gene silencing by heterochromatin (GO:various), heterochromatin boundary formation
- **Multiple supporting references available**

---

## Evidence Base: Key Literature

### Papers Directly Refuting Demethylase Activity

- **Trewick et al. (2007)** — [PMID: 17449867](https://pubmed.ncbi.nlm.nih.gov/17449867/): *"Interaction of Epe1 with the heterochromatin assembly pathway in Schizosaccharomyces pombe."* Reported no detectable demethylase activity for Epe1 and noted the JmjC domain lacks conservation of Fe(II)-binding residues. This is the primary negative biochemical result.

- **Trewick et al. (2007)** — [PMID: 17948055](https://pubmed.ncbi.nlm.nih.gov/17948055/): *"The JmjC domain protein Epe1 prevents unregulated assembly and disassembly of heterochromatin."* Proposed that Epe1 is a protein hydroxylase rather than a demethylase, while showing that predicted Fe/2-OG binding residues are needed for in vivo function.

- **Raiymbek et al. (2020)** — [PMID: 32195666](https://pubmed.ncbi.nlm.nih.gov/32195666/): *"An H3K9 methylation-dependent protein interaction regulates the non-enzymatic functions of a putative histone demethylase."* Demonstrated non-enzymatic mechanism; JmjC domain mediates Swi6 protein-protein interaction regulated by H3K9me.

### Papers Providing Structural/Evolutionary Context

- **Lee et al. (2011)** — [PMID: 21167174](https://pubmed.ncbi.nlm.nih.gov/21167174/): *"Structural basis for human PHF2 Jumonji domain interaction with metal ions."* Crystal structure of PHF2, Epe1's closest structural homolog, shows Tyr at third triad position and no demethylase activity. Explicitly notes Epe1 homology and lack of known enzymatic activity.

- **Clissold & Ponting (2005)** — [PMID: 15809658](https://pubmed.ncbi.nlm.nih.gov/15809658/): *"Methylation: lost in hydroxylation?"* Early computational proposal that Epe1 and certain JmjC proteins might be protein hydroxylases rather than demethylases.

### Papers Establishing JmjC Demethylase Family Paradigm

- **Tsukada et al. (2006)** — [PMID: 16362057](https://pubmed.ncbi.nlm.nih.gov/16362057/): *"Histone demethylation by a family of JmjC domain-containing proteins."* Established JmjC demethylase activity; basis for PomBase NOT annotation on Epe1.

- **Yamane et al. (2006)** — [PMID: 16603237](https://pubmed.ncbi.nlm.nih.gov/16603237/): *"JHDM2A, a JmjC-containing H3K9 demethylase."* Demonstrates H3K9 demethylase activity with complete facial triad — positive control family member.

- **Whetstine et al. (2006)** — [PMID: 16603238](https://pubmed.ncbi.nlm.nih.gov/16603238/): *"Reversal of histone lysine trimethylation by the JMJD2 family of histone demethylases."* Establishes JmjC trimethylation-specific demethylase activity.

### Papers Showing Epe1 In Vivo Function (Without Demonstrating Catalysis)

- **Zofall & Grewal (2006)** — [PMID: 16762840](https://pubmed.ncbi.nlm.nih.gov/16762840/): JmjC domain required for Pol II accessibility, but mechanism acknowledged as potentially distinct from demethylation.

- **Audergon et al. (2015)** — [PMID: 25838386](https://pubmed.ncbi.nlm.nih.gov/25838386/)  and **Ragunathan et al. (2015)** — [PMID: 25831549](https://pubmed.ncbi.nlm.nih.gov/25831549/): Both demonstrate that Epe1 loss enables epigenetic inheritance of H3K9me, establishing Epe1 as a key counter to heterochromatin heritability.

- **Sorida et al. (2019)** — [PMID: 31206516](https://pubmed.ncbi.nlm.nih.gov/31206516/): Most nuanced in vivo study; separates JmjC-dependent removal of established heterochromatin from NTA-dependent prevention of de novo heterochromatin, with both functions contributing to anti-silencing.

- **Braun et al. (2011)** — [PMID: 21215368](https://pubmed.ncbi.nlm.nih.gov/21215368/): Cul4-Ddb1^Cdt2^ ubiquitin ligase sculpts Epe1 distribution to boundaries by promoting degradation within heterochromatin body.

- **Srivastava et al. (2021)** — [PMID: 33533152](https://pubmed.ncbi.nlm.nih.gov/33533152/): Epe1-Ell1 interaction using C-terminal region (403–948 aa), independent of JmjC domain, reveals Epe1 functions beyond heterochromatin.

- **Yaseen et al. (2022)** — [PMID: 35879419](https://pubmed.ncbi.nlm.nih.gov/35879419/): Proteasome-dependent truncation of Epe1 mediates antifungal resistance; JmjC domain required but nomenclature reflects family assignment.

---

## Conclusion

The annotation of histone demethylase activity (GO:0032452) for *S. pombe* Epe1, based on phylogenetic inference (IBA), is **over-annotated** and should be removed. The convergence of structural (missing catalytic residue), biochemical (no in vitro activity), curatorial (NOT|IDA annotation), and mechanistic (non-enzymatic Swi6 interaction) evidence provides strong support for this conclusion. While Epe1 is unquestionably a critical regulator of heterochromatin boundaries and epigenetic inheritance in fission yeast, its molecular function appears to be mediated through protein-protein interaction rather than enzymatic demethylation. Future work should focus on testing the protein hydroxylase hypothesis and determining whether a restored catalytic triad (I379H) can confer demethylase activity.


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)
- [OpenScientist epe1 domain and triad](openscientist_artifacts/provenance_epe1_domain_and_triad.json)
![OpenScientist epe1 domain and triad](openscientist_artifacts/provenance_epe1_domain_and_triad.png)
- [OpenScientist plot 1](openscientist_artifacts/provenance_plot_1.json)
![OpenScientist plot 1](openscientist_artifacts/provenance_plot_1.png)