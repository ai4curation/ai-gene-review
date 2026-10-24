---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-08T21:52:11.930139'
end_time: '2026-09-08T22:09:28.885597'
duration_seconds: 1036.96
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: DROME
  gene: TyrRS
  gene_symbol: TyrRS
  uniprot_accession: Q9VV60
  taxon_id: NCBITaxon:7227
  taxon_label: Drosophila melanogaster
  focus_type: function_assignment
  hypothesis_slug: fly41-resveratrol-recognition
  hypothesis_text: The Drosophila melanogaster protein Q9VV60 binds resveratrol.
  term_context: '- Term: resveratrol binding (GO:1905594)

    - # Focused fly function hypothesis


    Hypothesis: The Drosophila melanogaster protein Q9VV60 binds resveratrol.


    Target: Drosophila melanogaster (NCBITaxon:7227), UniProt Q9VV60. Gene label:
    TyrRS. Verify identity and isoform independently; the gene label is not evidence
    for the hypothesis.


    ## Original prediction


    F:resveratrol binding


    ## Decisive question


    Evaluate biochemical resveratrol recognition by the supplied fly TyrRS sequence
    using verified ligand-bound structures, experimentally tested contact residues
    and conformational requirements in characterized TyrRS proteins. Establish the
    transferability of the binding pocket rather than relying on whole-protein similarity.
    Assess assay conditions, controls and compound isomer where reported. If docking
    is used, include meaningful controls and treat scores as hypotheses, not measured
    binding or evidence of physiological function. Separate binding from downstream
    stress signaling and from whether this interaction merits a GO molecular-function
    annotation; check the current status and scope of the emitted term independently.


    ## Identity and sequence


    - Target record: https://www.uniprot.org/uniprotkb/Q9VV60/entry

    - FlyBase identifier(s) from the cohort identity mapping: FBgn0027080.

    - Frozen current UniProt sequence: 525 residues; SHA-256 `94682a9b94b943a5eca242d7bb960b2787dc2557781933a8d5849bd5e371a01f`.

    - The sequence was frozen for the fly cohort on 2026-09-08. It is not established
    as the original prediction-time input. Analyze this sequence explicitly and document
    any alternate accession, version or isoform you analyze.


    ```fasta

    >Q9VV60 Drosophila melanogaster TyrRS

    MVGITPAEKKALITRNLQETLGDDKLTKILAERDLKIYWGTATTGKPHVAYFVPMSKIAD

    FLKAGCEVTILFADLHAYLDNMKAPWSLLELRTKYYEQVIKAMLSSIGVPLEKLKFVKGS

    DYQLSKEYTLDVYKLSSVVTQHDAKKAGAEVVKQVEYPLLSGLLYPGLQALDEEYLKVDA

    QFGGVDQRKIFTFSEKYLPQLGYEKRIHFMNPMVPGLAGGKMSSSEEDSKIDLLDSPANV

    KKKLKKAFCEPGNIADNGLLSFVKHVLFSLFKEGEGFEVNREAEHGGDVTFLKYEDLEKY

    YAEDKLHPGDLKATVEKYINRLLDPIRKAFENPELQKLSAAAYPPPAKVKAGAAPAAGAD

    EDAPHRLDIRVGKVVEVARHPDADTLYVLKIDLAEAQPRTIISGLVKFVTEEELNQRLVA

    VLCNLKPSKMRGILSEGMVLCTSNADHTVVEPIVLPATATAGSRLSFEGFSGTPDEQLNP

    KKKVWEKLSADFKTNSDGLAVWKDNFLLTPEGEKLSSKLANCSIK

    ```


    Primary literature lead to inspect (not a preassigned conclusion): https://pubmed.ncbi.nlm.nih.gov/25533949/


    ## Evidence and deliverable


    Use primary literature and public sequence, structural and genomic resources.
    This is a focused mechanistic investigation, not a general gene overview. Seek
    supporting, contrary and competing explanations; an unresolved result is acceptable.
    Distinguish direct fly experiments, justified transfers and results on a different
    isoform. Do not equate missing target experiments with evidence of absence.


    Do not consult the ai-gene-review repository''s current reviews, generated research
    summaries or local bioinformatics analyses; these are held out for comparison.
    Agreement with ARBA or repeated prediction text does not validate the biology.
    Save executed methods/code, actual analysis outputs, sequence identifiers and
    primary-source URLs/DOIs/PMIDs. Report decisive evidence and limitations, not
    just a verdict. Do not fabricate computations or use docking/structural resemblance
    alone as experimental validation.'
  reference_context: No specific reference context supplied.
  source_file: genes/DROME/TyrRS/TyrRS-ai-review.yaml
  source_selector: free-text
  source_context_yaml: "hypothesis: The Drosophila melanogaster protein Q9VV60 binds\
    \ resveratrol.\nfocus_type: function_assignment\nterm_id: GO:1905594\nterm_label:\
    \ resveratrol binding\ncontext:\n- |\n  # Focused fly function hypothesis\n\n\
    \  Hypothesis: The Drosophila melanogaster protein Q9VV60 binds resveratrol.\n\
    \n  Target: Drosophila melanogaster (NCBITaxon:7227), UniProt Q9VV60. Gene label:\
    \ TyrRS. Verify identity and isoform independently; the gene label is not evidence\
    \ for the hypothesis.\n\n  ## Original prediction\n\n  F:resveratrol binding\n\
    \n  ## Decisive question\n\n  Evaluate biochemical resveratrol recognition by\
    \ the supplied fly TyrRS sequence using verified ligand-bound structures, experimentally\
    \ tested contact residues and conformational requirements in characterized TyrRS\
    \ proteins. Establish the transferability of the binding pocket rather than relying\
    \ on whole-protein similarity. Assess assay conditions, controls and compound\
    \ isomer where reported. If docking is used, include meaningful controls and treat\
    \ scores as hypotheses, not measured binding or evidence of physiological function.\
    \ Separate binding from downstream stress signaling and from whether this interaction\
    \ merits a GO molecular-function annotation; check the current status and scope\
    \ of the emitted term independently.\n\n  ## Identity and sequence\n\n  - Target\
    \ record: https://www.uniprot.org/uniprotkb/Q9VV60/entry\n  - FlyBase identifier(s)\
    \ from the cohort identity mapping: FBgn0027080.\n  - Frozen current UniProt sequence:\
    \ 525 residues; SHA-256 `94682a9b94b943a5eca242d7bb960b2787dc2557781933a8d5849bd5e371a01f`.\n\
    \  - The sequence was frozen for the fly cohort on 2026-09-08. It is not established\
    \ as the original prediction-time input. Analyze this sequence explicitly and\
    \ document any alternate accession, version or isoform you analyze.\n\n  ```fasta\n\
    \  >Q9VV60 Drosophila melanogaster TyrRS\n  MVGITPAEKKALITRNLQETLGDDKLTKILAERDLKIYWGTATTGKPHVAYFVPMSKIAD\n\
    \  FLKAGCEVTILFADLHAYLDNMKAPWSLLELRTKYYEQVIKAMLSSIGVPLEKLKFVKGS\n  DYQLSKEYTLDVYKLSSVVTQHDAKKAGAEVVKQVEYPLLSGLLYPGLQALDEEYLKVDA\n\
    \  QFGGVDQRKIFTFSEKYLPQLGYEKRIHFMNPMVPGLAGGKMSSSEEDSKIDLLDSPANV\n  KKKLKKAFCEPGNIADNGLLSFVKHVLFSLFKEGEGFEVNREAEHGGDVTFLKYEDLEKY\n\
    \  YAEDKLHPGDLKATVEKYINRLLDPIRKAFENPELQKLSAAAYPPPAKVKAGAAPAAGAD\n  EDAPHRLDIRVGKVVEVARHPDADTLYVLKIDLAEAQPRTIISGLVKFVTEEELNQRLVA\n\
    \  VLCNLKPSKMRGILSEGMVLCTSNADHTVVEPIVLPATATAGSRLSFEGFSGTPDEQLNP\n  KKKVWEKLSADFKTNSDGLAVWKDNFLLTPEGEKLSSKLANCSIK\n\
    \  ```\n\n  Primary literature lead to inspect (not a preassigned conclusion):\
    \ https://pubmed.ncbi.nlm.nih.gov/25533949/\n\n  ## Evidence and deliverable\n\
    \n  Use primary literature and public sequence, structural and genomic resources.\
    \ This is a focused mechanistic investigation, not a general gene overview. Seek\
    \ supporting, contrary and competing explanations; an unresolved result is acceptable.\
    \ Distinguish direct fly experiments, justified transfers and results on a different\
    \ isoform. Do not equate missing target experiments with evidence of absence.\n\
    \n  Do not consult the ai-gene-review repository's current reviews, generated\
    \ research summaries or local bioinformatics analyses; these are held out for\
    \ comparison. Agreement with ARBA or repeated prediction text does not validate\
    \ the biology. Save executed methods/code, actual analysis outputs, sequence identifiers\
    \ and primary-source URLs/DOIs/PMIDs. Report decisive evidence and limitations,\
    \ not just a verdict. Do not fabricate computations or use docking/structural\
    \ resemblance alone as experimental validation.\nreference_id: []"
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

- **Organism code:** DROME
- **Taxon:** Drosophila melanogaster (NCBITaxon:7227)
- **Gene directory:** TyrRS
- **Gene symbol:** TyrRS
- **UniProt accession:** Q9VV60

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** fly41-resveratrol-recognition
- **Source file:** genes/DROME/TyrRS/TyrRS-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

The Drosophila melanogaster protein Q9VV60 binds resveratrol.

## Term and Decision Context

- Term: resveratrol binding (GO:1905594)
- # Focused fly function hypothesis

Hypothesis: The Drosophila melanogaster protein Q9VV60 binds resveratrol.

Target: Drosophila melanogaster (NCBITaxon:7227), UniProt Q9VV60. Gene label: TyrRS. Verify identity and isoform independently; the gene label is not evidence for the hypothesis.

## Original prediction

F:resveratrol binding

## Decisive question

Evaluate biochemical resveratrol recognition by the supplied fly TyrRS sequence using verified ligand-bound structures, experimentally tested contact residues and conformational requirements in characterized TyrRS proteins. Establish the transferability of the binding pocket rather than relying on whole-protein similarity. Assess assay conditions, controls and compound isomer where reported. If docking is used, include meaningful controls and treat scores as hypotheses, not measured binding or evidence of physiological function. Separate binding from downstream stress signaling and from whether this interaction merits a GO molecular-function annotation; check the current status and scope of the emitted term independently.

## Identity and sequence

- Target record: https://www.uniprot.org/uniprotkb/Q9VV60/entry
- FlyBase identifier(s) from the cohort identity mapping: FBgn0027080.
- Frozen current UniProt sequence: 525 residues; SHA-256 `94682a9b94b943a5eca242d7bb960b2787dc2557781933a8d5849bd5e371a01f`.
- The sequence was frozen for the fly cohort on 2026-09-08. It is not established as the original prediction-time input. Analyze this sequence explicitly and document any alternate accession, version or isoform you analyze.

```fasta
>Q9VV60 Drosophila melanogaster TyrRS
MVGITPAEKKALITRNLQETLGDDKLTKILAERDLKIYWGTATTGKPHVAYFVPMSKIAD
FLKAGCEVTILFADLHAYLDNMKAPWSLLELRTKYYEQVIKAMLSSIGVPLEKLKFVKGS
DYQLSKEYTLDVYKLSSVVTQHDAKKAGAEVVKQVEYPLLSGLLYPGLQALDEEYLKVDA
QFGGVDQRKIFTFSEKYLPQLGYEKRIHFMNPMVPGLAGGKMSSSEEDSKIDLLDSPANV
KKKLKKAFCEPGNIADNGLLSFVKHVLFSLFKEGEGFEVNREAEHGGDVTFLKYEDLEKY
YAEDKLHPGDLKATVEKYINRLLDPIRKAFENPELQKLSAAAYPPPAKVKAGAAPAAGAD
EDAPHRLDIRVGKVVEVARHPDADTLYVLKIDLAEAQPRTIISGLVKFVTEEELNQRLVA
VLCNLKPSKMRGILSEGMVLCTSNADHTVVEPIVLPATATAGSRLSFEGFSGTPDEQLNP
KKKVWEKLSADFKTNSDGLAVWKDNFLLTPEGEKLSSKLANCSIK
```

Primary literature lead to inspect (not a preassigned conclusion): https://pubmed.ncbi.nlm.nih.gov/25533949/

## Evidence and deliverable

Use primary literature and public sequence, structural and genomic resources. This is a focused mechanistic investigation, not a general gene overview. Seek supporting, contrary and competing explanations; an unresolved result is acceptable. Distinguish direct fly experiments, justified transfers and results on a different isoform. Do not equate missing target experiments with evidence of absence.

Do not consult the ai-gene-review repository's current reviews, generated research summaries or local bioinformatics analyses; these are held out for comparison. Agreement with ARBA or repeated prediction text does not validate the biology. Save executed methods/code, actual analysis outputs, sequence identifiers and primary-source URLs/DOIs/PMIDs. Report decisive evidence and limitations, not just a verdict. Do not fabricate computations or use docking/structural resemblance alone as experimental validation.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: The Drosophila melanogaster protein Q9VV60 binds resveratrol.
focus_type: function_assignment
term_id: GO:1905594
term_label: resveratrol binding
context:
- |
  # Focused fly function hypothesis

  Hypothesis: The Drosophila melanogaster protein Q9VV60 binds resveratrol.

  Target: Drosophila melanogaster (NCBITaxon:7227), UniProt Q9VV60. Gene label: TyrRS. Verify identity and isoform independently; the gene label is not evidence for the hypothesis.

  ## Original prediction

  F:resveratrol binding

  ## Decisive question

  Evaluate biochemical resveratrol recognition by the supplied fly TyrRS sequence using verified ligand-bound structures, experimentally tested contact residues and conformational requirements in characterized TyrRS proteins. Establish the transferability of the binding pocket rather than relying on whole-protein similarity. Assess assay conditions, controls and compound isomer where reported. If docking is used, include meaningful controls and treat scores as hypotheses, not measured binding or evidence of physiological function. Separate binding from downstream stress signaling and from whether this interaction merits a GO molecular-function annotation; check the current status and scope of the emitted term independently.

  ## Identity and sequence

  - Target record: https://www.uniprot.org/uniprotkb/Q9VV60/entry
  - FlyBase identifier(s) from the cohort identity mapping: FBgn0027080.
  - Frozen current UniProt sequence: 525 residues; SHA-256 `94682a9b94b943a5eca242d7bb960b2787dc2557781933a8d5849bd5e371a01f`.
  - The sequence was frozen for the fly cohort on 2026-09-08. It is not established as the original prediction-time input. Analyze this sequence explicitly and document any alternate accession, version or isoform you analyze.

  ```fasta
  >Q9VV60 Drosophila melanogaster TyrRS
  MVGITPAEKKALITRNLQETLGDDKLTKILAERDLKIYWGTATTGKPHVAYFVPMSKIAD
  FLKAGCEVTILFADLHAYLDNMKAPWSLLELRTKYYEQVIKAMLSSIGVPLEKLKFVKGS
  DYQLSKEYTLDVYKLSSVVTQHDAKKAGAEVVKQVEYPLLSGLLYPGLQALDEEYLKVDA
  QFGGVDQRKIFTFSEKYLPQLGYEKRIHFMNPMVPGLAGGKMSSSEEDSKIDLLDSPANV
  KKKLKKAFCEPGNIADNGLLSFVKHVLFSLFKEGEGFEVNREAEHGGDVTFLKYEDLEKY
  YAEDKLHPGDLKATVEKYINRLLDPIRKAFENPELQKLSAAAYPPPAKVKAGAAPAAGAD
  EDAPHRLDIRVGKVVEVARHPDADTLYVLKIDLAEAQPRTIISGLVKFVTEEELNQRLVA
  VLCNLKPSKMRGILSEGMVLCTSNADHTVVEPIVLPATATAGSRLSFEGFSGTPDEQLNP
  KKKVWEKLSADFKTNSDGLAVWKDNFLLTPEGEKLSSKLANCSIK
  ```

  Primary literature lead to inspect (not a preassigned conclusion): https://pubmed.ncbi.nlm.nih.gov/25533949/

  ## Evidence and deliverable

  Use primary literature and public sequence, structural and genomic resources. This is a focused mechanistic investigation, not a general gene overview. Seek supporting, contrary and competing explanations; an unresolved result is acceptable. Distinguish direct fly experiments, justified transfers and results on a different isoform. Do not equate missing target experiments with evidence of absence.

  Do not consult the ai-gene-review repository's current reviews, generated research summaries or local bioinformatics analyses; these are held out for comparison. Agreement with ARBA or repeated prediction text does not validate the biology. Save executed methods/code, actual analysis outputs, sequence identifiers and primary-source URLs/DOIs/PMIDs. Report decisive evidence and limitations, not just a verdict. Do not fabricate computations or use docking/structural resemblance alone as experimental validation.
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

## Target: *Drosophila melanogaster* TyrRS (UniProt Q9VV60, FBgn0027080)
## Hypothesis: "Q9VV60 binds resveratrol" (GO:1905594 — resveratrol binding)
## Focus type: function_assignment

---

## Summary

The proposed function assignment **"F:resveratrol binding" (GO:1905594)** for *Drosophila* TyrRS should **not** be applied to the gene review, and if present it should be **removed**. Three independent lines of evidence converge on this conclusion. First, the GO term itself is **obsolete** — GO:1905594 "resveratrol binding" was obsoleted on 2026-07-19 with the explicit rationale that *"binding to resveratrol is not an evolved molecular function"*, has no replacement or "consider" term, and carries **zero annotations across all organisms**. Second, **no organism carries this annotation**, including the human ortholog YARS1, which is the only protein where a TyrRS–resveratrol interaction has actually been measured; GO curators translated that human experiment into the general term GO:0036094 "small molecule binding," not a resveratrol-specific term. Third, resveratrol is a **plant stilbene phytoalexin** that is not endogenous to *Drosophila*, so any binding is a xenobiotic/pharmacological event rather than a physiological molecular function.

The most important caveat is that binding is genuinely **plausible on structural grounds**. The fly tyrosine-binding pocket is fully conserved with the human pocket where resveratrol was co-crystallized: fly Q9VV60 shares 68.4% identity with human YARS1, and all nine reported human resveratrol-contact residues are identical in the fly protein. But plausibility-by-homology is not measured binding — it has never been tested in *Drosophila* — and homology does not rescue an obsolete, unannotatable GO term.

The gene's real, experimentally supported molecular function is **tyrosine–tRNA ligation** (GO:0004831), backed by a fly IDA experiment ([PMID: 19561293](https://pubmed.ncbi.nlm.nih.gov/19561293/)). **Verdict: REFUTED** as a GO annotation; only weakly/partially supported as an in-vitro biochemical possibility that has no bearing on annotation.

---

## Key Findings

### Finding 1 — The fly tyrosine-binding pocket is fully conserved with the human pocket where resveratrol binds

The supplied sequence was verified independently: **525 residues, SHA-256 `94682a9b…a01f`** — an exact match to the frozen cohort sequence. UniProt Q9VV60 is annotated as "Tyrosine–tRNA ligase, GN=TyrRS," and the protein carries the diagnostic **class I aminoacyl-tRNA synthetase Rossmann-fold signatures**: a HIGH-like motif region **YWGTATTGKPH** (around position 38) and a **KMSKS**-family motif **KMSSS** (around position 221).

A global Needleman–Wunsch alignment (BLOSUM62) of fly Q9VV60 against human YARS1 (P54577) gives **357/522 = 68.4% identity**, with a near-identical catalytic core. Most decisively, all **nine reported resveratrol-contact residues** from the human co-crystal structure (PDB 4Q93; Y39, L72, A74, H77, V152, Y166, Q170, D173, I191) are **identical in the fly protein** at the corresponding positions (fly Y38, L71, A73, H76, V151, Y165, Q169, D172, I190), with conserved local sequence context around each.

This is the strongest evidence *for* the seed hypothesis. In human TyrRS the resveratrol pocket is the tyrosine active site, and that pocket is transferable to the fly enzyme by strict residue conservation. The direct human study ([PMID: 25533949](https://pubmed.ncbi.nlm.nih.gov/25533949/)) states: *"Here we present a 2.1 Å co-crystal structure of resveratrol bound to the active site of TyrRS."* Because resveratrol is a tyrosine mimic occupying that pocket, and the pocket is conserved, fly TyrRS could plausibly bind resveratrol in vitro. **However**, this remains an *inference by homology* — not a measured binding constant, not an assay in fly protein, and not evidence of physiological relevance. Under the standards set by the decisive question, pocket transferability is a *hypothesis*, not experimental validation.

### Finding 2 — GO:1905594 "resveratrol binding" is OBSOLETE and unannotatable

The QuickGO/EBI ontology record for GO:1905594 shows `isObsolete=True`, `name="obsolete resveratrol binding"`, `aspect=molecular_function`, and the comment: *"The reason for obsoletion is that binding to resveratrol is not an evolved molecular function."* The term has `replacedBy=None` and `consider=None`. The ontology history records the obsoletion action on **2026-07-19** (the `is_a binding` parentage was deleted). A QuickGO annotation search returns **0 annotations to GO:1905594 across all organisms.**

This is decisive for the curation question: an obsolete GO term with no replacement or "consider" alternative cannot be validly assigned to any gene product. The obsoletion rationale itself encodes the ontology curators' biological judgment that binding a plant-derived xenobiotic is not an evolved function of any protein. Resveratrol is a plant stilbene phytoalexin ([PMID: 38903666](https://pubmed.ncbi.nlm.nih.gov/38903666/): *"These compounds function as phytoalexins, aiding plant defense against phytopathogens"*; corroborated by [PMID: 40644839](https://pubmed.ncbi.nlm.nih.gov/40644839/)), not a *Drosophila* metabolite.

### Finding 3 — Neither the fly protein nor the directly assayed human ortholog carries a resveratrol-binding annotation

Current QuickGO molecular-function annotations for **fly Q9VV60** comprise nine terms — GO:0000049 (tRNA binding), GO:0000166 (nucleotide binding), GO:0003723 (RNA binding), GO:0004812 (aminoacyl-tRNA ligase), GO:0004831 (tyrosine–tRNA ligase; including **IDA [PMID: 19561293](https://pubmed.ncbi.nlm.nih.gov/19561293/)** [Storkebaum PNAS 2009, fly CMT model] and TAS [PMID: 26761199](https://pubmed.ncbi.nlm.nih.gov/26761199/) [fly aaRS review]), and GO:0005524 (ATP binding) — and **no resveratrol / GO:1905594 annotation**.

Human YARS1 (P54577) carries 33 MF annotations and **also has no GO:1905594**. Importantly, the resveratrol study [PMID: 25533949](https://pubmed.ncbi.nlm.nih.gov/25533949/) supports GO:0004831 (IDA), GO:0005515 (IPI — the PARP1 interaction), and **GO:0036094 "small molecule binding" (IDA)** on the human protein. In other words, when GO curators encountered the single direct resveratrol experiment, they chose the **general small-molecule-binding term**, not a resveratrol-specific one. The study's own framing is pharmacological: *"Resveratrol nullifies the catalytic activity and redirects TyrRS to a nuclear function."*

### Finding 4 — Q9VV60 is a single-isoform canonical cytoplasmic tyrosyl-tRNA synthetase with no resveratrol reference

The UniProt Q9VV60 record shows sequence length 525 (matching the frozen SHA-256), **no alternative products / isoforms listed**, `proteinExistence="1: Evidence at protein level"`, catalytic activity `tRNA(Tyr) + L-tyrosine + ATP = L-tyrosyl-tRNA(Tyr) + AMP + diphosphate + H(+)` (Rhea), and subcellular location Cytoplasm (ARBA). There is **no mention of resveratrol** anywhere in the FUNCTION, CATALYTIC, or LOCATION comments. This rules out isoform confusion and confirms the analyzed sequence is the canonical, only protein product of the locus.

---

## Mechanistic Model / Interpretation

The layered logic distinguishing "can bind" from "should be annotated" is summarized below:

```
                    Q9VV60 (fly TyrRS, 525 aa, cytoplasmic, PE1)
                                     |
             Class I aaRS Rossmann fold; tyrosine pocket
             (HIGH-like YWGTATTGKPH @38, KMSSS @221)
                                     |
        68.4% identity to human YARS1; ALL 9 resveratrol-contact
        residues IDENTICAL (Y38/L71/A73/H76/V151/Y165/Q169/D172/I190)
                                     |
        +----------------------------+----------------------------+
        |                                                         |
  BIOCHEMICAL PLAUSIBILITY                          CURATION / ONTOLOGY REALITY
  (resveratrol = tyrosine mimic,                    (GO:1905594 OBSOLETE 2026-07-19,
   occupies conserved Tyr pocket)                    "not an evolved MF", 0 annotations)
        |                                                         |
  Plausible in vitro binding                        Term unannotatable; even human
  BUT never measured in fly;                        resveratrol data curated as
  xenobiotic, not endogenous ligand                 GO:0036094 small molecule binding
        +----------------------------+----------------------------+
                                     |
                   GENUINE FUNCTION = tyrosine-tRNA ligation
                   (GO:0004831, fly IDA PMID:19561293)
```

The key conceptual separation the decisive question demanded is between **(a)** whether the protein can physically recognize the compound (plausible), **(b)** whether that recognition is a physiological molecular function (no — resveratrol is a plant defense metabolite absent from flies), and **(c)** whether it merits the specific GO term (no — the term is obsolete and unannotatable). All three must hold for a valid function assignment, and only the weakest link (a) is satisfied.

The downstream biology described in the human/rodent literature — resveratrol acting as a *tyrosine-free-mimic* (cis-RSV) or *tyrosine-like-mimic* (trans-RSV) to modulate TyrRS levels, nuclear translocation, and PARP1-mediated histone ADP-ribosylation ([PMID: 35688816](https://pubmed.ncbi.nlm.nih.gov/35688816/), [PMID: 25533949](https://pubmed.ncbi.nlm.nih.gov/25533949/)) — is **stress signaling downstream of binding** and must be separated from the binding event itself. Even where documented, it is human/rat biology, not fly.

---

## Evidence Base / Evidence Matrix

| Citation | Evidence type | Direction | Claim tested | Key finding | Context | Confidence / limitations |
|---|---|---|---|---|---|---|
| [PMID: 25533949](https://pubmed.ncbi.nlm.nih.gov/25533949/) | Direct assay + structure | Qualifies (supports plausibility; refutes term choice) | TyrRS binds resveratrol | 2.1 Å co-crystal of resveratrol in the TyrRS active site; nullifies catalysis, redirects to nuclear PARP1-activating function | **Human YARS1**, in vitro + cell | High for human; **not fly**; curated to GO:0036094, not GO:1905594 |
| Sequence/structure analysis (this work) | Structural/evolutionary (computational) | Supports (plausibility only) | Fly pocket can bind resveratrol | 68.4% identity to YARS1; all 9 contact residues identical | Fly Q9VV60 vs human P54577 / PDB 4Q93 | Homology inference, NOT measured binding |
| QuickGO / EBI ontology (this work) | Database | Refutes | GO:1905594 is a valid assignable term | Term OBSOLETE 2026-07-19, "not an evolved MF", 0 annotations, no replacement | All organisms | Decisive; ontology-level |
| QuickGO annotations (this work) | Database | Refutes | Fly/human TyrRS carry resveratrol binding | Neither Q9VV60 nor P54577 has GO:1905594; human data → GO:0036094 | Fly + human | Decisive; database-level |
| UniProt Q9VV60 (this work) | Database | Qualifies | Identity/isoform | Single 525-aa isoform, cytoplasmic, tyrosyl-tRNA ligase; no resveratrol mention | Fly | Confirms identity; rules out isoform confusion |
| [PMID: 19561293](https://pubmed.ncbi.nlm.nih.gov/19561293/) | Mutant phenotype / IDA | Competing (true function) | Fly TyrRS function | Fly IDA support for GO:0004831 tyrosine–tRNA ligase (CMT model) | *Drosophila* | Establishes genuine core function |
| [PMID: 35688816](https://pubmed.ncbi.nlm.nih.gov/35688816/) | Direct assay / mechanism | Qualifies (downstream) | RSV isomer effects on TyrRS | cis-RSV mimics tyrosine-free, trans-RSV mimics tyrosine-like conformation; opposite neuro effects | Rat cortical neurons / human | Downstream signaling, not fly; isomer-dependent |
| [PMID: 38903666](https://pubmed.ncbi.nlm.nih.gov/38903666/) | Review | Supports (rationale) | Resveratrol is xenobiotic to animals | Stilbenes/resveratrol are plant phytoalexins | Plants | Supports GO obsoletion rationale |
| [PMID: 40644839](https://pubmed.ncbi.nlm.nih.gov/40644839/) | Review | Supports (rationale) | Resveratrol is a plant defense metabolite | Resveratrol among lignin-pathway phytoalexins restricting pathogens | Plants | Contextual |

---

## GO Curation Implications

**Recommended action (lead requiring curator verification): REMOVE / DO NOT ADD "F:resveratrol binding" (GO:1905594).**

- The term is **obsolete** (2026-07-19) with **no `replacedBy` and no `consider`** term. Assigning an obsolete term is invalid regardless of the underlying biology.
- The obsoletion comment — *"binding to resveratrol is not an evolved molecular function"* — is itself the ontology's curator-level judgment that this should never be an MF annotation for any gene.
- **No downgraded resveratrol-specific replacement should be created.** If a curator wished to capture the (human, in vitro) small-molecule interaction, the precedent set on the human ortholog is **GO:0036094 "small molecule binding" (IDA)** — but that is supported only by the human experiment, and there is **no direct fly evidence** to transfer it with an experimental code. For the fly protein, no small-molecule-binding annotation is warranted from resveratrol data.
- **Retain the core molecular function: GO:0004831 "tyrosine–tRNA ligase activity"** (fly IDA [PMID: 19561293](https://pubmed.ncbi.nlm.nih.gov/19561293/)), along with the standard supporting terms already present (GO:0004812, GO:0005524, GO:0000166, GO:0000049, GO:0003723).

**GO decision table:**

| GO term | Aspect | Proposed status | Basis |
|---|---|---|---|
| GO:1905594 resveratrol binding | MF | **Remove / reject** | Obsolete, unannotatable, xenobiotic, no fly data |
| GO:0036094 small molecule binding | MF | Not for fly | Only human IDA precedent; no fly experiment |
| GO:0004831 tyrosine–tRNA ligase | MF | **Retain (core)** | Fly IDA PMID:19561293 |
| GO:0005524 ATP binding | MF | Retain | Standard for class I aaRS |

---

## Mechanistic Scope

The immediate molecular event under test is **direct physical recognition of the small molecule resveratrol by the TyrRS protein**. The evidence establishes that in human TyrRS this occurs in the **tyrosine active-site pocket**, with resveratrol acting as a tyrosine mimic that competitively occupies the substrate site and blocks aminoacylation. This binding is the *proximal* event.

Everything else described in the literature is **downstream**: loss of catalytic (aminoacylation) activity, nuclear translocation of TyrRS, activation of PARP1, histone serine-ADP-ribosylation, DNA-repair modulation, and neuroprotection versus neurodegeneration (isomer-dependent). These are pathway consequences and phenotypic outcomes measured in **human cells and rat neurons**, not molecular functions of the fly protein and not the binding event itself. For curation of the fly gene, only the proximal binding claim is in scope — and it has never been measured in *Drosophila*.

---

## Conflicts and Alternatives

1. **Organism transfer gap (primary conflict).** The only direct experiment is on **human YARS1**, not fly Q9VV60. Assigning a fly annotation from a human in vitro experiment would require an ISS/ISO-style justified transfer — but the target term is obsolete, so no transfer is possible regardless.
2. **Xenobiotic vs. physiological function.** Resveratrol is a plant phytoalexin ([PMID: 38903666](https://pubmed.ncbi.nlm.nih.gov/38903666/), [PMID: 40644839](https://pubmed.ncbi.nlm.nih.gov/40644839/)); flies do not synthesize it and it is not a natural ligand. A druggable pocket that happens to accept a xenobiotic is not an evolved molecular function — exactly the GO obsoletion rationale.
3. **Isomer dependence.** [PMID: 35688816](https://pubmed.ncbi.nlm.nih.gov/35688816/) shows cis- and trans-resveratrol bind the same pocket but drive **opposite** conformational/functional outcomes. A bare "resveratrol binding" annotation would obscure this and misrepresent the biology.
4. **Database carry-over risk.** The original "F:resveratrol binding" prediction most likely arose from automated similarity transfer of the human structural result to the fly ortholog — precisely the frequency-bias / paralog-overannotation failure mode the objective warns against. Neither UniProt nor GO curators applied this term to any organism.

No evidence was found that *refutes* physical binding capability; the conflicts are all about **relevance and annotatability**, not about whether the pocket could accept the ligand.

---

## Limitations and Knowledge Gaps

- **No direct fly binding measurement.** No ITC, SPR, thermal shift, or co-crystal exists for fly TyrRS + resveratrol. What was checked: PubMed literature, UniProt, and GO annotations — none report a fly assay. This matters because "missing target experiment ≠ evidence of absence"; binding remains *plausible but unmeasured*. Resolution: a direct biophysical binding assay on recombinant Q9VV60.
- **Docking not performed as a substitute.** Per the decisive question, docking would only generate hypotheses, not validation; it was intentionally not used to claim binding. Structural inference here is limited to residue-level conservation mapping.
- **PDB 4Q93 contact residues taken from the human structural literature**, not re-derived from an independent structure determination in this work; the residue-numbering transfer to fly relies on the pairwise alignment.
- **GO obsoletion date (2026-07-19)** reflects the ontology state at analysis time; curators should confirm the current QuickGO/OLS status at review time, though obsoletion is not expected to reverse.
- **Functional consequence in flies unknown.** Whether resveratrol modulates TyrRS catalysis or any nuclear/stress role *in Drosophila* has not been tested; the human PARP1 axis may not be conserved.

---

## Discriminating Tests

1. **Direct biophysical binding assay on recombinant fly Q9VV60** (isothermal titration calorimetry or surface plasmon resonance) with **cis- and trans-resveratrol separately**, using **L-tyrosine as a positive competitor control** and a non-binding stilbene analog as negative control. This directly tests the seed hypothesis in the target organism.
2. **Thermal shift / DSF** of Q9VV60 ± resveratrol vs. ± tyrosine to confirm active-site engagement.
3. **Aminoacylation inhibition assay**: does resveratrol inhibit fly TyrRS tyrosylation activity (as it does human)? A competitive Ki would confirm active-site occupancy.
4. **Co-crystallography or cryo-EM** of fly TyrRS + resveratrol to verify the contact residues predicted identical to human.
5. **Ontology/annotation audit**: confirm GO:1905594 obsolete status and the absence of any organism annotation in the current release before finalizing the review.

---

## Proposed Follow-up Experiments / Actions (Curation Leads)

*All leads require curator verification.*

- **Action change:** Remove/reject "F:resveratrol binding" (GO:1905594) from the TyrRS review; do not substitute a resveratrol-specific term. *Reason:* term obsolete 2026-07-19, no replacement, zero annotations, xenobiotic interaction, no fly data.
- **Retain:** GO:0004831 "tyrosine–tRNA ligase activity" as the experimentally supported core molecular function — fly IDA, [PMID: 19561293](https://pubmed.ncbi.nlm.nih.gov/19561293/).
- **Candidate reference to verify (human precedent — do not transfer to fly):** [PMID: 25533949](https://pubmed.ncbi.nlm.nih.gov/25533949/), snippet: *"Here we present a 2.1 Å co-crystal structure of resveratrol bound to the active site of TyrRS."* Note this was curated on human YARS1 as **GO:0036094 small molecule binding**, not resveratrol binding.
- **Supporting rationale reference:** [PMID: 38903666](https://pubmed.ncbi.nlm.nih.gov/38903666/), snippet: *"These compounds function as phytoalexins, aiding plant defense against phytopathogens"* — supports the "not an evolved animal MF" judgment.
- **Isomer caveat reference:** [PMID: 35688816](https://pubmed.ncbi.nlm.nih.gov/35688816/) — cis- vs. trans-resveratrol produce opposite TyrRS conformational effects; a generic binding term would be misleading.
- **Suggested curator question:** Was the original "F:resveratrol binding" prediction an automated similarity transfer from the human structure? If so, flag as ortholog over-annotation.
- **Suggested experiment (for the record):** direct ITC/SPR binding assay on recombinant fly Q9VV60 with cis/trans-resveratrol and tyrosine competition controls.

---

## Conclusion

The seed hypothesis is **biochemically plausible but curationally refuted.** Fly TyrRS almost certainly *can* accommodate resveratrol in its conserved tyrosine pocket (68.4% identity to human, all nine contact residues identical), but this has never been measured in *Drosophila*, represents a xenobiotic pharmacological interaction rather than an evolved function, and the specific GO term (GO:1905594) is obsolete, replacement-less, and unannotated in every organism — including the human protein where resveratrol binding was actually demonstrated. The genuine, experimentally supported molecular function of Q9VV60 is tyrosine–tRNA ligation (GO:0004831). The "F:resveratrol binding" assignment should be removed and not replaced.


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)