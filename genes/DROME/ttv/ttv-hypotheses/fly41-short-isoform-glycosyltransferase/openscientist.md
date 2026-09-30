---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-08T21:52:11.930084'
end_time: '2026-09-08T22:25:08.741024'
duration_seconds: 1976.81
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: DROME
  gene: ttv
  gene_symbol: ttv
  uniprot_accession: D5SHU8
  taxon_id: NCBITaxon:7227
  taxon_label: Drosophila melanogaster
  focus_type: function_assignment
  hypothesis_slug: fly41-short-isoform-glycosyltransferase
  hypothesis_text: The Drosophila melanogaster protein D5SHU8 has glycosyltransferase
    activity.
  term_context: '- Term: glycosyltransferase activity (GO:0016757)

    - # Focused fly function hypothesis


    Hypothesis: The Drosophila melanogaster protein D5SHU8 has glycosyltransferase
    activity.


    Target: Drosophila melanogaster (NCBITaxon:7227), UniProt D5SHU8. Gene label:
    ttv. Verify identity and isoform independently; the gene label is not evidence
    for the hypothesis.


    ## Original prediction


    F:glycosyltransferase activity


    ## Decisive question


    Assess glycosyltransferase activity of the supplied exact sequence. Resolve its
    annotated transcript/isoform and compare it with structurally and biochemically
    characterized EXT-family proteins and relevant Drosophila partners. Determine
    which catalytic domain and substrate-binding architecture are present, whether
    the protein can fold into a functional catalytic unit, and whether partner interactions
    or targeting are required for intrinsic catalysis versus an in-vivo glycan-biosynthesis
    role. Neither short length nor a conserved catalytic residue alone settles the
    question. Distinguish experimentally demonstrated isolated-domain activity from
    structural plausibility.


    ## Identity and sequence


    - Target record: https://www.uniprot.org/uniprotkb/D5SHU8/entry

    - FlyBase identifier(s) from the cohort identity mapping: FBgn0265974.

    - Frozen current UniProt sequence: 299 residues; SHA-256 `76d919802eaf321c50ecd217e0e45d5f74f2ec9e6fb7a3806aa74f3433760493`.

    - The sequence was frozen for the fly cohort on 2026-09-08. It is not established
    as the original prediction-time input. Analyze this sequence explicitly and document
    any alternate accession, version or isoform you analyze.


    ```fasta

    >D5SHU8 Drosophila melanogaster ttv

    MPFLLNSMGAEPRHNYTAVIYVQIGAALGPNAALYKLVRTITKSQFVERILVLWAADRPL

    PLKKRWPPTSHIPLHVISLGGSTRSQGAGPTSQTTEGRPSISQRFLPYDEIQTDAVLSLD

    EDAILNTDELDFAYTVWRDFPERIVGYPARAHFWDDSKNAWGYTSKWTNYYSIVLTGAAF

    YHRYYNYLYTNWLSLLLLKTVQQSSNCEDILMNLLVSHVTRKPPIKVTQRKGYKDRETGR

    SPWNDPDHFIQRQSCLNTFAAVFGYMPLIRSNLRMDPMLYRDPVSNLRKKYRQIELVGS

    ```


    Primary literature lead to inspect (not a preassigned conclusion): https://pubmed.ncbi.nlm.nih.gov/36593275/


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
  source_file: genes/DROME/ttv/ttv-ai-review.yaml
  source_selector: free-text
  source_context_yaml: "hypothesis: The Drosophila melanogaster protein D5SHU8 has\
    \ glycosyltransferase activity.\nfocus_type: function_assignment\nterm_id: GO:0016757\n\
    term_label: glycosyltransferase activity\ncontext:\n- |\n  # Focused fly function\
    \ hypothesis\n\n  Hypothesis: The Drosophila melanogaster protein D5SHU8 has glycosyltransferase\
    \ activity.\n\n  Target: Drosophila melanogaster (NCBITaxon:7227), UniProt D5SHU8.\
    \ Gene label: ttv. Verify identity and isoform independently; the gene label is\
    \ not evidence for the hypothesis.\n\n  ## Original prediction\n\n  F:glycosyltransferase\
    \ activity\n\n  ## Decisive question\n\n  Assess glycosyltransferase activity\
    \ of the supplied exact sequence. Resolve its annotated transcript/isoform and\
    \ compare it with structurally and biochemically characterized EXT-family proteins\
    \ and relevant Drosophila partners. Determine which catalytic domain and substrate-binding\
    \ architecture are present, whether the protein can fold into a functional catalytic\
    \ unit, and whether partner interactions or targeting are required for intrinsic\
    \ catalysis versus an in-vivo glycan-biosynthesis role. Neither short length nor\
    \ a conserved catalytic residue alone settles the question. Distinguish experimentally\
    \ demonstrated isolated-domain activity from structural plausibility.\n\n  ##\
    \ Identity and sequence\n\n  - Target record: https://www.uniprot.org/uniprotkb/D5SHU8/entry\n\
    \  - FlyBase identifier(s) from the cohort identity mapping: FBgn0265974.\n  -\
    \ Frozen current UniProt sequence: 299 residues; SHA-256 `76d919802eaf321c50ecd217e0e45d5f74f2ec9e6fb7a3806aa74f3433760493`.\n\
    \  - The sequence was frozen for the fly cohort on 2026-09-08. It is not established\
    \ as the original prediction-time input. Analyze this sequence explicitly and\
    \ document any alternate accession, version or isoform you analyze.\n\n  ```fasta\n\
    \  >D5SHU8 Drosophila melanogaster ttv\n  MPFLLNSMGAEPRHNYTAVIYVQIGAALGPNAALYKLVRTITKSQFVERILVLWAADRPL\n\
    \  PLKKRWPPTSHIPLHVISLGGSTRSQGAGPTSQTTEGRPSISQRFLPYDEIQTDAVLSLD\n  EDAILNTDELDFAYTVWRDFPERIVGYPARAHFWDDSKNAWGYTSKWTNYYSIVLTGAAF\n\
    \  YHRYYNYLYTNWLSLLLLKTVQQSSNCEDILMNLLVSHVTRKPPIKVTQRKGYKDRETGR\n  SPWNDPDHFIQRQSCLNTFAAVFGYMPLIRSNLRMDPMLYRDPVSNLRKKYRQIELVGS\n\
    \  ```\n\n  Primary literature lead to inspect (not a preassigned conclusion):\
    \ https://pubmed.ncbi.nlm.nih.gov/36593275/\n\n  ## Evidence and deliverable\n\
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
citation_count: 5
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
- **Gene directory:** ttv
- **Gene symbol:** ttv
- **UniProt accession:** D5SHU8

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** fly41-short-isoform-glycosyltransferase
- **Source file:** genes/DROME/ttv/ttv-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

The Drosophila melanogaster protein D5SHU8 has glycosyltransferase activity.

## Term and Decision Context

- Term: glycosyltransferase activity (GO:0016757)
- # Focused fly function hypothesis

Hypothesis: The Drosophila melanogaster protein D5SHU8 has glycosyltransferase activity.

Target: Drosophila melanogaster (NCBITaxon:7227), UniProt D5SHU8. Gene label: ttv. Verify identity and isoform independently; the gene label is not evidence for the hypothesis.

## Original prediction

F:glycosyltransferase activity

## Decisive question

Assess glycosyltransferase activity of the supplied exact sequence. Resolve its annotated transcript/isoform and compare it with structurally and biochemically characterized EXT-family proteins and relevant Drosophila partners. Determine which catalytic domain and substrate-binding architecture are present, whether the protein can fold into a functional catalytic unit, and whether partner interactions or targeting are required for intrinsic catalysis versus an in-vivo glycan-biosynthesis role. Neither short length nor a conserved catalytic residue alone settles the question. Distinguish experimentally demonstrated isolated-domain activity from structural plausibility.

## Identity and sequence

- Target record: https://www.uniprot.org/uniprotkb/D5SHU8/entry
- FlyBase identifier(s) from the cohort identity mapping: FBgn0265974.
- Frozen current UniProt sequence: 299 residues; SHA-256 `76d919802eaf321c50ecd217e0e45d5f74f2ec9e6fb7a3806aa74f3433760493`.
- The sequence was frozen for the fly cohort on 2026-09-08. It is not established as the original prediction-time input. Analyze this sequence explicitly and document any alternate accession, version or isoform you analyze.

```fasta
>D5SHU8 Drosophila melanogaster ttv
MPFLLNSMGAEPRHNYTAVIYVQIGAALGPNAALYKLVRTITKSQFVERILVLWAADRPL
PLKKRWPPTSHIPLHVISLGGSTRSQGAGPTSQTTEGRPSISQRFLPYDEIQTDAVLSLD
EDAILNTDELDFAYTVWRDFPERIVGYPARAHFWDDSKNAWGYTSKWTNYYSIVLTGAAF
YHRYYNYLYTNWLSLLLLKTVQQSSNCEDILMNLLVSHVTRKPPIKVTQRKGYKDRETGR
SPWNDPDHFIQRQSCLNTFAAVFGYMPLIRSNLRMDPMLYRDPVSNLRKKYRQIELVGS
```

Primary literature lead to inspect (not a preassigned conclusion): https://pubmed.ncbi.nlm.nih.gov/36593275/

## Evidence and deliverable

Use primary literature and public sequence, structural and genomic resources. This is a focused mechanistic investigation, not a general gene overview. Seek supporting, contrary and competing explanations; an unresolved result is acceptable. Distinguish direct fly experiments, justified transfers and results on a different isoform. Do not equate missing target experiments with evidence of absence.

Do not consult the ai-gene-review repository's current reviews, generated research summaries or local bioinformatics analyses; these are held out for comparison. Agreement with ARBA or repeated prediction text does not validate the biology. Save executed methods/code, actual analysis outputs, sequence identifiers and primary-source URLs/DOIs/PMIDs. Report decisive evidence and limitations, not just a verdict. Do not fabricate computations or use docking/structural resemblance alone as experimental validation.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: The Drosophila melanogaster protein D5SHU8 has glycosyltransferase activity.
focus_type: function_assignment
term_id: GO:0016757
term_label: glycosyltransferase activity
context:
- |
  # Focused fly function hypothesis

  Hypothesis: The Drosophila melanogaster protein D5SHU8 has glycosyltransferase activity.

  Target: Drosophila melanogaster (NCBITaxon:7227), UniProt D5SHU8. Gene label: ttv. Verify identity and isoform independently; the gene label is not evidence for the hypothesis.

  ## Original prediction

  F:glycosyltransferase activity

  ## Decisive question

  Assess glycosyltransferase activity of the supplied exact sequence. Resolve its annotated transcript/isoform and compare it with structurally and biochemically characterized EXT-family proteins and relevant Drosophila partners. Determine which catalytic domain and substrate-binding architecture are present, whether the protein can fold into a functional catalytic unit, and whether partner interactions or targeting are required for intrinsic catalysis versus an in-vivo glycan-biosynthesis role. Neither short length nor a conserved catalytic residue alone settles the question. Distinguish experimentally demonstrated isolated-domain activity from structural plausibility.

  ## Identity and sequence

  - Target record: https://www.uniprot.org/uniprotkb/D5SHU8/entry
  - FlyBase identifier(s) from the cohort identity mapping: FBgn0265974.
  - Frozen current UniProt sequence: 299 residues; SHA-256 `76d919802eaf321c50ecd217e0e45d5f74f2ec9e6fb7a3806aa74f3433760493`.
  - The sequence was frozen for the fly cohort on 2026-09-08. It is not established as the original prediction-time input. Analyze this sequence explicitly and document any alternate accession, version or isoform you analyze.

  ```fasta
  >D5SHU8 Drosophila melanogaster ttv
  MPFLLNSMGAEPRHNYTAVIYVQIGAALGPNAALYKLVRTITKSQFVERILVLWAADRPL
  PLKKRWPPTSHIPLHVISLGGSTRSQGAGPTSQTTEGRPSISQRFLPYDEIQTDAVLSLD
  EDAILNTDELDFAYTVWRDFPERIVGYPARAHFWDDSKNAWGYTSKWTNYYSIVLTGAAF
  YHRYYNYLYTNWLSLLLLKTVQQSSNCEDILMNLLVSHVTRKPPIKVTQRKGYKDRETGR
  SPWNDPDHFIQRQSCLNTFAAVFGYMPLIRSNLRMDPMLYRDPVSNLRKKYRQIELVGS
  ```

  Primary literature lead to inspect (not a preassigned conclusion): https://pubmed.ncbi.nlm.nih.gov/36593275/

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

## Target: *Drosophila melanogaster* **ttv** (UniProt **D5SHU8**) — glycosyltransferase activity (GO:0016757)

**Target gene:** *Drosophila melanogaster* ttv (FlyBase FBgn0265974 / CG10117), UniProt **D5SHU8** (299 aa, TrEMBL/unreviewed).
**Term under test:** glycosyltransferase activity — **GO:0016757** (Molecular Function).
**Seed hypothesis:** "The *Drosophila melanogaster* protein D5SHU8 has glycosyltransferase activity."
**Investigation:** 3 iterations completed; 3 confirmed findings; 5 primary/structural literature sources reviewed.

---

## Summary

The seed hypothesis is **partially supported**. Three independent lines of sequence and homology evidence establish beyond reasonable doubt that D5SHU8 is a genuine, deeply conserved fragment of the *Drosophila* EXT1 ortholog **tout-velu (ttv)**. The 299-aa sequence aligns co-linearly and at **100% identity to residues 462–760 of the canonical, reviewed ttv protein Q9V730 (760 aa)**, and is **55.7% identical (Smith-Waterman, 166/298 aa) to the C-terminal catalytic region of human EXT1 (Q16394[466–744])**. This region corresponds precisely to the **isolated C-terminal GT64 (α1,4-GlcNAc-transferase) catalytic domain** (Pfam PF09258; InterPro IPR015338/IPR004263), and it retains the active-site aspartate (canonical Asp670 → D5SHU8 Asp209), the DED binding motif, and 8 of 9 known catalytic/substrate-binding residues. On these grounds, a **broad glycosyltransferase-activity term (GO:0016757) is a defensible, homology-based annotation** for this sequence — it is not a spurious match, a divergent paralog, or a mis-mapped fragment.

However, the hypothesis as literally stated — that *this exact truncated sequence* is a catalytically competent glycosyltransferase — is **not directly demonstrated**, and several structural facts argue for caution. D5SHU8 is a **truncated short isoform** beginning at internal Met462; it **lacks the N-terminal type-II transmembrane signal-anchor** (canonical residues ~7–25) that targets ttv to the Golgi, and it **lacks the entire N-terminal GT47/exostosin glucuronyltransferase (GlcA-transferase) domain**. The only direct enzymatic evidence for the ttv/EXT1 protein comes from assays on the **full-length** protein, which further showed that robust dual glycosyltransferase activity is **partner-dependent** — markedly augmented by co-expression with SOTV/EXT2. No published study reports catalytic activity for an isolated EXT1/ttv GT64 domain, nor for this specific 299-aa isoform.

**Bottom line for the curator:** GO:0016757 should be **retained for D5SHU8 only as an inferred, generic, isoform-caveated annotation** with an evidence code appropriate to sequence/structural homology (e.g., ISS or IEA), **not** upgraded to a directly-assayed, more specific molecular-function term (such as a specific GlcNAc-transferase EC-level term) and **not** paired with a confident Golgi-membrane cellular-component assertion for this exact sequence. The most important caveats are the missing GT47 domain, the missing membrane anchor, the partner-dependence of the demonstrated activity, and the complete absence of any isolated-domain enzymatic assay.

---

## Identity and Sequence Provenance

| Item | Value |
|---|---|
| Accession analyzed | D5SHU8 (TrEMBL, UniProtKB unreviewed) |
| Length | 299 aa (matches frozen cohort length; SHA-256 `76d919802eaf321c50…`) |
| Submission name / clone | "MIP20656p", EMBL **BT124899 / ADG57806.1** |
| RefSeq | NP_001260972.1 / NM_001274043.1 |
| Gene | ttv, CG10117, FlyBase **FBgn0265974** |
| Domains (InterPro/Pfam) | GT64_dom (IPR015338), Exostosin (IPR004263); **Pfam PF09258** (res ~16–280) |
| Canonical reference | **Q9V730** (reviewed, 760 aa, "Exostosin-1", type-II membrane protein) |
| Relationship to canonical | **D5SHU8 == Q9V730[462–760], 100% identity, co-linear (offset 461)** |

The 299-aa length and exact residue string match the frozen FASTA, and the 100% co-linear mapping to Q9V730 fixes the identity unambiguously. The record is an **N-terminally truncated cDNA product** (internal Met462 start) representing the isolated C-terminal GT64 domain.

---

## Key Findings

### Finding 1 — D5SHU8 is the isolated C-terminal GT64 domain of ttv/EXT1 (a truncated short isoform)

The 299-residue D5SHU8 sequence aligns **co-linearly and with 100% identity (299/299) to residues 462–760 of the canonical reviewed ttv protein Q9V730 (760 aa)**, beginning at canonical offset 461. It thus corresponds precisely to the C-terminal 299 residues of the full-length protein with no substitutions. This C-terminal region carries a **GT64 glycosyltransferase domain** (Pfam PF09258; InterPro IPR015338 "GT64_dom"; associated with IPR004263 Exostosin), spanning approximately D5SHU8 residues 16–280.

Crucially, the truncation removes two functionally essential N-terminal features of full-length ttv/EXT1: (1) the **type-II transmembrane signal-anchor** (canonical residues ~7–25), the sole membrane-targeting determinant that localizes ttv to the Golgi apparatus where heparan sulfate is polymerized; and (2) the **entire N-terminal GT47/exostosin domain**, which encodes the **glucuronyltransferase (GlcA-transferase, GlcAT-II)** half of the bifunctional EXT1 co-polymerase.

Of the nine canonical catalytic/substrate-binding residues, **8 are retained** in D5SHU8, including the active-site **Asp670 → Asp209** and the **DED binding motif (canonical 581–583 → D5SHU8 120–122)**. The single missing binding residue, **Arg437**, lies in the deleted N-terminal GT47 region. Thus D5SHU8 preserves the GlcNAc-transferase (GlcNAcT-II) active-site machinery but discards the glucuronyltransferase machinery — it is a single-domain, half-enzyme fragment relative to the bifunctional full-length protein.

### Finding 2 — Direct enzyme evidence exists for full-length TTV, not for the isolated GT64 isoform

The decisive biochemical evidence in the literature concerns the **full-length** protein. Izumikawa et al. 2006 ([PMID: 16303756](https://pubmed.ncbi.nlm.nih.gov/16303756/)) demonstrated in vitro that **TTV/DEXT1 and SOTV/DEXT2 have GlcNAcT-II and GlcAT-II activities** required for biosynthesis of the repeating disaccharide units of the heparan sulfate (HS) backbone, and — critically — that **co-expression of TTV with SOTV markedly augmented both glycosyltransferase activities** compared with TTV or SOTV expressed alone. The TTV–SOTV complex lacked GlcNAcT-I (chain initiation), which requires BOTV/EXTL3. This establishes two facts that qualify the seed hypothesis: (a) the demonstrated activity is a property of the **full-length** protein, and (b) full activity is **partner-dependent**, not a robust autonomous property.

Complementary in vivo evidence from Dasgupta et al. 2007 ([PMID: 17610078](https://pubmed.ncbi.nlm.nih.gov/17610078/)) showed that the human EXT1 gene functionally complements the *ttv* mutation in *Drosophila* — rescuing a *ttv*-null mutant to adulthood and restoring glycosaminoglycan (GAG) biosynthesis — firmly establishing ttv as the functional *Drosophila* EXT1 ortholog with a bona fide glycosyltransferase role in vivo. The structural work on the EXT1–EXT2 co-polymerase ([PMID: 36593275](https://pubmed.ncbi.nlm.nih.gov/36593275/)) confirms that the HS backbone is synthesized by an obligate **EXT1–EXT2 co-polymerase complex**. None of these studies reports catalytic activity for an **isolated EXT1/ttv GT64 domain** or for this specific **299-aa isoform**. The activity is therefore transferred to D5SHU8 by homology, not measured on it.

> Verified snippet (PMID 16303756): *"we demonstrated that TTV/DEXT1 and SOTV/DEXT2 had GlcNAcT-II and GlcAT-II activities required for the biosynthesis of repeating disaccharide units of the HS backbone, and the coexpression of TTV with SOTV markedly augmented both glycosyltransferase activities when compared with the expression of TTV or SOTV alone."*

> Verified snippet (PMID 17610078): *"the human EXT1 (hEXT1) gene is conserved through species and can functionally complement the ttv mutation in Drosophila. The hEXT1 gene was able to rescue a ttv null mutant to adulthood and restore GAG biosynthesis."*

### Finding 3 — D5SHU8 GT64 domain is 55.7% identical to human EXT1 C-terminal catalytic region

An independent Smith-Waterman local alignment (BLOSUM62 substitution matrix) of the full 299-aa D5SHU8 against human EXT1 (Q16394, 746 aa) yields a **single high-scoring block: D5SHU8[2–295] vs EXT1[466–744], 166/298 = 55.7% identity, alignment score 838**. This block is precisely the C-terminal GT64 (GlcNAc-transferase) region of EXT1. Combined with the 100% co-linear identity to canonical *Drosophila* ttv Q9V730[462–760], this cross-species conservation confirms that D5SHU8 is a **bona fide, deeply conserved EXT1/ttv GT64 catalytic domain** — not a spurious annotation, a divergent paralog, or a mis-mapped fragment. High sequence identity retained across ~500 million years of fly–human divergence is consistent with a functionally constrained catalytic module. (An earlier naïve same-offset comparison had given ~35%; the rigorous local alignment corrects this to 55.7% and decisively confirms the conserved fold.)

---

## Mechanistic Model / Interpretation

The full-length ttv/EXT1 protein is a **bifunctional, Golgi-resident type-II membrane glycosyltransferase** that, together with its partner SOTV/EXT2, forms the HS co-polymerase that builds the `(-GlcAβ1,4-GlcNAcα1,4-)n` heparan sulfate backbone. Its two catalytic activities are spatially segregated into two domains:

```
Full-length ttv/EXT1 (canonical Q9V730, 760 aa)
┌───────┬───────────────────────────┬───────────────────────────────┐
│ TM    │  GT47 / exostosin domain  │   GT64 domain (PF09258)        │
│ anchor│  GlcA-transferase (GlcAT) │   GlcNAc-transferase (GlcNAcT) │
│ ~7-25 │  binding residue Arg437   │   active-site Asp670; DED motif│
└───────┴───────────────────────────┴───────────────────────────────┘
   Golgi         [ REMOVED in D5SHU8 ]        [ = D5SHU8, res 462-760 ]
 targeting

D5SHU8 (299 aa) = C-terminal GT64 domain ONLY
                  ├─ retains active-site Asp209 + DED motif (120-122)
                  ├─ retains 8/9 catalytic/binding residues
                  ├─ LACKS TM signal-anchor  → no Golgi targeting
                  └─ LACKS GT47/GlcA-transferase → half-enzyme
```

**Interpretation.** D5SHU8 is a structurally plausible catalytic module — it preserves the GlcNAc-transferase active site and the substrate-binding DED motif of a well-characterized enzyme family. This is why automated pipelines (ARBA/UniRule/InterPro2GO) legitimately propagate GO:0016757 to it: the GT64 domain signature maps to the glycosyltransferase parent term. However, three mechanistic gaps separate "structural plausibility" from "demonstrated function of this sequence":

1. **Domain amputation.** The demonstrated in vitro TTV activity is bifunctional (both GlcNAcT-II and GlcAT-II). D5SHU8 has only the GT64 half; the GlcAT-II activity depends on the deleted GT47 domain. At best D5SHU8 could carry only the GlcNAcT-II half-activity, and even that has never been tested in isolation.
2. **Partner dependence.** Izumikawa et al. showed activity is markedly augmented by SOTV/EXT2 co-expression, and the structural study shows an obligate co-polymerase complex. Whether the isolated GT64 domain can fold and catalyze without the rest of the protein and without its partner is unknown.
3. **Loss of targeting.** Without the transmembrane anchor, D5SHU8 would not be retained in the Golgi in vivo, so even if intrinsically active it could not participate in the physiological glycan-biosynthesis pathway in its native compartment.

The seed's "decisive question" — intrinsic isolated-domain catalysis vs. an in-vivo glycan-biosynthesis role — resolves as: **neither has been experimentally demonstrated for this exact sequence.** The glycosyltransferase assignment rests on homology to a domain that is part of a demonstrated enzyme, which is a reasonable but not decisive basis.

---

## Evidence Base / Evidence Matrix

| Citation (PMID) | Evidence type | Direction | Claim tested | Key finding | Context | Confidence & limitations |
|---|---|---|---|---|---|---|
| This analysis (Q9V730 vs D5SHU8) | Structural/sequence (computational) | Qualifies | Which region/domain is D5SHU8? | 100% co-linear identity to canonical res 462–760 = isolated C-terminal **GT64** domain; lacks TM anchor + GT47 domain | UniProtKB/InterPro | High for mapping; domain boundaries approximate |
| This analysis (catalytic residue map) | Structural/evolutionary (computational) | Supports (partial) | Is catalytic constellation intact? | 8/9 canonical residues retained incl. active-site Asp670→Asp209; only GT47 residue Arg437 missing | UniProt feature transfer | High; inference, not assayed |
| This analysis (Smith-Waterman) | Structural/evolutionary (computational) | Supports | Is D5SHU8 a genuine conserved GT64 domain? | D5SHU8[2–295] vs human EXT1[466–744] = **166/298 = 55.7% identity** (score 838) | Fly vs human sequence | High for homology; not an activity assay |
| [16303756](https://pubmed.ncbi.nlm.nih.gov/16303756/) (Izumikawa 2006) | Direct in vitro assay | Supports (full-length) / Qualifies (isoform) | Does the ttv gene product have GT activity? | Full-length TTV has GlcNAcT-II + GlcAT-II; co-expression with SOTV markedly augments both | *Drosophila*, recombinant | High for full-length; **not tested on isolated GT64/299-aa isoform**; partner-dependent |
| [17610078](https://pubmed.ncbi.nlm.nih.gov/17610078/) (Dasgupta 2007) | Mutant complementation (in vivo) | Supports | Is ttv the functional EXT1 ortholog? | hEXT1 rescues ttv-null to adulthood, restores GAG biosynthesis | *Drosophila*/human | High for ortholog identity; whole-gene, not isoform |
| [14998928](https://pubmed.ncbi.nlm.nih.gov/14998928/) (Han 2004) | Mutant phenotype / interaction | Supports / qualifies | Role & partnering of ttv | Ttv and Sotv form a complex, co-localize; both needed for HSPG/morphogen distribution | *Drosophila* wing disc | High; pathway-level, supports partner dependence |
| [14645127](https://pubmed.ncbi.nlm.nih.gov/14645127/) (Takei 2003) | Mutant phenotype / genetics | Supports | ttv required for HSPG biosynthesis | ttv (with sotv/botv) required for HS proteoglycan synthesis; note hedged "have or are closely related to glycosyltransferase activities" | *Drosophila* | Medium-high; in vivo pathway role |
| [36593275](https://pubmed.ncbi.nlm.nih.gov/36593275/) (2023) | Structural (cryo-EM) | Qualifies | Is HS synthesis intrinsic to one domain? | HS backbone made by obligate **EXT1–EXT2 co-polymerase** complex | Human EXT1-2 | High; emphasizes complex requirement; not fly, not isolated domain |

---

## GO Curation Implications

**Lead requiring curator verification.**

### GO Decision Table

| GO ID | Label | Aspect | Applies to D5SHU8? | Recommended action | Basis |
|---|---|---|---|---|---|
| GO:0016757 | glycosyltransferase activity | MF | Yes (by homology) | **Retain** as inferred/generic, isoform-caveated (ISS/IEA) | Conserved GT64 catalytic domain (100% to ttv Q9V730[462–760]; 55.7% to human EXT1[466–744]); active-site Asp209 + 8/9 catalytic residues; no direct assay on this isolated isoform |
| GO:0008375 | acetylglucosaminyltransferase activity | MF | Full-length only | Attach to canonical gene product, not isoform-specifically | Direct in vitro GlcNAcT-II shown for full-length TTV (PMID 16303756); isolated-domain activity unproven |
| GO:0015020 | glucuronosyltransferase activity | MF | No | Do **not** assign to D5SHU8 | GlcAT-II maps to N-terminal GT47 domain, **absent** in D5SHU8 |
| GO:0015012 | heparan sulfate proteoglycan biosynthetic process | BP | Full-length only | Attach to canonical; non-core for truncated isoform | In vivo HS/GAG synthesis needs membrane targeting + SOTV/EXT2 (PMIDs 16303756, 14998928, 17610078); both absent in isoform |
| GO:0000139 / GO:0016020 | Golgi membrane / membrane | CC | No | Do **not** assign to D5SHU8 | Lacks type-II TM signal-anchor (canonical res 7–25); cannot be Golgi-anchored |

**Net:** the current prediction "F:glycosyltransferase activity" is **correct in direction but should not be strengthened**; treat it as a **non-core, homology-inferred, isoform-caveated** annotation. Avoid "protein binding" as a summary; the informative call here is the GT64 catalytic-domain MF.

---

## Mechanistic Scope

The immediate molecular function under test is **catalysis of glycosyl transfer** — specifically, in the ttv/EXT1 context, transfer of N-acetylglucosamine (GlcNAcT-II) during heparan sulfate chain elongation. This is distinct from, and must be separated from:

- **Downstream pathway consequences** — HS/HSPG biosynthesis (a BP), the aggregate output of the EXT1–EXT2 co-polymerase, not a direct readout of the isolated GT64 domain.
- **Developmental/phenotypic outcomes** — morphogen (Hh, Dpp, Wg) gradient formation and wing patterning, which are *pleiotropic loss-of-function phenotypes* of *ttv* mutation ([PMID: 14645127](https://pubmed.ncbi.nlm.nih.gov/14645127/), [PMID: 14998928](https://pubmed.ncbi.nlm.nih.gov/14998928/)), several steps removed from the enzymatic act. They support the gene's role in glycan biosynthesis but do not demonstrate that the D5SHU8 fragment catalyzes anything.
- **Disease manifestation** — human EXT1 loss causes hereditary multiple exostoses; relevant to the family's importance but not evidence about this isoform's activity.

The seed hypothesis is a **function-assignment** claim about direct gene-product activity. The evidence supports the direct activity of the *full-length* gene product and the *homologous plausibility* of the D5SHU8 domain, but not a measured direct activity of D5SHU8 itself.

---

## Conflicts and Alternatives

1. **Isoform truncation (primary conflict).** The record is an N-terminally truncated cDNA product (internal Met462 start) — the C-terminal GT64 half only. Automated annotation transfers "glycosyltransferase activity" from the domain, but the deleted GT47 domain and TM anchor mean the isoform is not a faithful stand-in for the full enzyme.
2. **Partner-dependence.** Izumikawa et al. show activity is markedly augmented by SOTV/EXT2 and the structural work shows an obligate complex. An isolated, anchor-less single domain may not be autonomously catalytic.
3. **"Closely related to glycosyltransferase activities" hedging.** The EXT-family literature ([PMID: 14645127](https://pubmed.ncbi.nlm.nih.gov/14645127/)) itself uses cautious phrasing, reflecting that domain presence ≠ proven catalysis for every member.
4. **Database carry-over risk.** The GO:0016757 assignment likely originates from InterPro2GO/ARBA mapping of PF09258 and from the full ortholog; auto-annotated CC terms ("ER/Golgi membrane") partly contradict the truncated sequence (no TM anchor) — a source of over-annotation if applied uncritically.
5. **No paralog confusion detected.** The 100% identity to ttv Q9V730 and 55.7% to human EXT1 (not EXTL1/2/3) rules out mis-assignment to a different EXT paralog. Identity is secure; only isoform completeness and measured activity are in question.

---

## Limitations and Knowledge Gaps

| Gap | What was checked | Why it matters | What would resolve it |
|---|---|---|---|
| No assay on the exact 299-aa isoform | 5 papers; all activity data on full-length TTV or the EXT1-2 complex | GO:0016757 for D5SHU8 rests entirely on homology | In vitro GlcNAcT-II assay on recombinant D5SHU8 (± SOTV/EXT2) |
| Can the isolated GT64 domain fold/catalyze alone? | Structural literature shows obligate EXT1-2 complex; no isolated-domain data | Determines whether "intrinsic catalysis" is even possible for this fragment | Recombinant expression + activity/thermostability of GT64 domain alone |
| Provenance/status of the D5SHU8 record | Mapped to clone MIP20656p/ADG57806.1, RefSeq NP_001260972.1, FBgn0265974; begins at internal Met, lacks anchor | Whether a real isoform vs. partial-cDNA artifact affects whether CC/BP annotations apply | FlyBase transcript evidence; RNA-seq/Ribo-seq isoform support |
| In vivo expression & localization of the short isoform | Not directly determined; TM anchor absent by sequence | If not Golgi-targeted, cannot participate in native HS pathway | Tagged-isoform localization; targeted proteomics |
| Substrate specificity of D5SHU8 | 8/9 catalytic residues present, Arg437 (GT47) absent | Distinguishes GlcNAcT-II-only vs. no activity | Defined-substrate transferase assays |
| Full detail of PMID 36593275 | Only opening sentence programmatically retrievable in-run | Used at review level only | Full-text access to structural methods/results |

Additional caveats: domain-boundary coordinates for GT47/GT64 are approximate; catalytic-residue calls are UniProt feature transfers (inference, not assay).

---

## Discriminating Tests

1. **In vitro glycosyltransferase assay on recombinant D5SHU8** (residues 462–760), measuring GlcNAcT-II activity with UDP-GlcNAc donor and a heparosan/oligosaccharide acceptor, **with and without co-expressed SOTV/EXT2** — the single most decisive experiment for intrinsic vs. partner-dependent catalysis.
2. **Folding/stability check** (CD, thermal shift, or limited proteolysis) on the isolated GT64 domain to determine whether it forms a stable fold without the GT47 domain.
3. **Domain-swap/complementation:** does D5SHU8 rescue any ttv-null phenotype? (Prediction: no, due to missing anchor + GT47.)
4. **Expression/topology check:** GFP-tag localization — predict soluble/cytosolic, not Golgi-anchored, unlike full-length.
5. **FlyBase/RNA-seq isoform verification** to confirm whether the 299-aa form is a genuinely expressed transcript or a partial-cDNA artifact.
6. **Structural comparison / modeling** of D5SHU8 against the EXT1–EXT2 cryo-EM structure ([PMID: 36593275](https://pubmed.ncbi.nlm.nih.gov/36593275/)) — used as a hypothesis-generator only, **not** as validation.

---

## Proposed Follow-up Experiments / Curation Leads

*All labeled as leads requiring curator verification.*

- **Curation action (immediate):** Keep GO:0016757 on D5SHU8 with a homology/electronic evidence code and add an **isoform caveat** noting (a) truncation to the GT64 domain, (b) absence of the GT47/GlcAT-II domain and TM anchor, and (c) that direct activity is demonstrated only for full-length TTV and is partner-dependent. Do **not** add specific child MF terms or a confident Golgi CC term for this record.
- **Reference to attach (verify snippet):** [PMID: 16303756](https://pubmed.ncbi.nlm.nih.gov/16303756/) — *"TTV/DEXT1 and SOTV/DEXT2 had GlcNAcT-II and GlcAT-II activities … coexpression of TTV with SOTV markedly augmented both glycosyltransferase activities…"* — label as support for the **full-length gene product**, qualifying for the isoform.
- **Reference to attach (verify snippet):** [PMID: 17610078](https://pubmed.ncbi.nlm.nih.gov/17610078/) — *"the human EXT1 (hEXT1) gene … can functionally complement the ttv mutation … restore GAG biosynthesis."* — supports ortholog identity/in-vivo function at the gene level.
- **Experiment to prioritize:** the in vitro isolated-domain GlcNAcT-II assay (Discriminating Test 1), which would move the annotation from homology-inferred to directly-tested for this sequence — resolving the core of the "decisive question."
- **Suggested curator question:** Is the 299-aa D5SHU8 a curated biological isoform or a partial cDNA? The answer determines whether any localization/process annotations should be propagated to this record at all.

---

## Provenance Notes

- **Sequence identity established computationally:** D5SHU8 (299 aa) vs canonical ttv Q9V730 (760 aa): co-linear, offset 461, 299/299 = 100% identity → residues 462–760. D5SHU8[2–295] vs human EXT1 Q16394[466–744]: Smith-Waterman (BLOSUM62), 166/298 = 55.7% identity, score 838.
- **Domain assignment:** GT64 (Pfam PF09258; InterPro IPR015338; Exostosin IPR004263), D5SHU8 residues ~16–280. Catalytic Asp670→Asp209; DED motif 581–583→120–122; 8/9 catalytic/binding residues retained; Arg437 (GT47 region) absent.
- **Identity cross-references:** gene *ttv*/CG10117/FBgn0265974; cDNA clone MIP20656p / GenBank ADG57806.1; RefSeq NP_001260972.1.
- **Frozen input:** 299 residues, SHA-256 `76d919802eaf321c50ecd217e0e45d5f74f2ec9e6fb7a3806aa74f3433760493` (frozen 2026-09-08). SHA-256 recomputation was blocked in the sandbox; length and exact residue string match the frozen FASTA.
- **Artifacts saved during the run:** `/tmp/catalytic_residue_mapping.csv`, `/tmp/ttv_domain_map.png`, `/tmp/GO_decision_table.csv`.

---

*Report compiled from 3 completed investigation iterations, 3 confirmed sequence/homology findings, and 5 primary/structural literature sources. No direct enzymatic assay on the D5SHU8 isoform exists in the accessed literature; the glycosyltransferase assignment is homology-based and should be curated accordingly.*


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)