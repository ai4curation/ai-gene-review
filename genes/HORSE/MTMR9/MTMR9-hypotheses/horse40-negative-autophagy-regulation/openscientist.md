---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-08T15:57:03.815496'
end_time: '2026-09-08T16:50:49.187365'
duration_seconds: 3225.37
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: HORSE
  gene: MTMR9
  gene_symbol: A0A9L0T3C1
  uniprot_accession: A0A9L0T3C1
  taxon_id: NCBITaxon:9796
  taxon_label: Equus caballus
  focus_type: function_assignment
  hypothesis_slug: horse40-negative-autophagy-regulation
  hypothesis_text: The horse protein A0A9L0T3C1 negatively regulates autophagy.
  term_context: "- Term: negative regulation of autophagy (GO:0010507)\n- # Focused\
    \ function hypothesis\n\nHypothesis: The horse protein A0A9L0T3C1 negatively regulates\
    \ autophagy.\n\nTarget: Equus caballus (NCBITaxon:9796), UniProt A0A9L0T3C1. Gene\
    \ label: MTMR9; verify identity independently rather than treating the label as\
    \ proof.\n\nTarget GO claim: GO:0010507 \u2014 negative regulation of autophagy.\
    \ Verify its definition and scope.\n\n## Decisive question\n\nEvaluate the partner-dependent\
    \ mechanism for this process and whether the exact protein supports it. Identify\
    \ experimentally grounded partners and substrate pathways. Distinguish complex\
    \ formation, enzyme regulation and the direction of an autophagy phenotype.\n\n\
    ## Identity and sequence inputs\n\n- Target record: https://www.uniprot.org/uniprotkb/A0A9L0T3C1/entry\n\
    - Human comparison lead: https://www.uniprot.org/uniprotkb/Q96QG7/entry (MTMR9).\
    \ Establish the relevant orthology/isoform relationship rather than assuming it.\n\
    - Frozen current UniProt sequence: 507 residues; SHA-256 `0a21ea798953b735f23b338b4365a2eaa154a29b4f4db7db9c773e81a7022f3d`.\n\
    - These are current sequences downloaded for the cohort on 2026-09-08. Identity\
    \ with the original prediction-time input has not been established. Evaluate the\
    \ supplied sequence explicitly; document any different sequence used.\n\n```fasta\n\
    >A0A9L0T3C1 Equus caballus MTMR9\nMEFAELIRTPRVDNVVLHRPFYPAVEGTLCLTGHHLILSSRQDNTEELWLLHSNIDAIDK\n\
    RFVGPLGTIIIKCKDFRIIQLDIPGMEECLNIASSIETSEWRLSYVNKEFAVCPSYPPIV\nIVPKSIDDEALRKVATFRHGGRFPVLSYYHKKNGMVIMRSGQPLTGTNGRRCKEDEKLIN\n\
    ATLRAGKRGYIIDTRSLTVAQQARAKGGGFEQEAHYPQWRRIHKSIERYHILQESLIKLV\nEACNDQTHNMDRWLSKLEASNWLTHIKEILTTACLAAQCIDREGASILIHGTEGTDSTLQ\n\
    VTSLAQIILEPRSRTIRGFEALIEREWLQAGHPFQQRCAQSAYCNSKQKWESPVFLLFLD\nCVWQILRQFPCSFEFNENFLIMLFEHAYASQFGTFLGNNESERCKLKLQQKTMSLWSWVN\n\
    RPSELRKFTSPLFEANNLVIWPSVAPQSLHLWEGIFLRWNRSSKYLDEAYEEMVNIIEYN\nKELQAKVNILRRQLAELETEDGMQESP\n\
    ```\n\n## Evidence and deliverable\n\nUse primary literature and public sequence,\
    \ structural and genomic resources. Select analyses that answer the decisive question;\
    \ this is not a general gene review. Assess support and contrary evidence, and\
    \ allow an unresolved outcome. Distinguish directly observed horse evidence, justified\
    \ mammalian transfer, and results for a different protein model.\n\nDo not consult\
    \ the ai-gene-review repository's existing judgments, research syntheses or local\
    \ bioinformatics analyses. Those are held out for comparison. Do not use agreement\
    \ with ARBA or another prediction as biological validation. Preserve reproducible\
    \ methods, accessions/versions, actual computation outputs and primary-source\
    \ URLs/DOIs/PMIDs. Report the decisive findings and limitations, not just a verdict."
  reference_context: No specific reference context supplied.
  source_file: genes/HORSE/MTMR9/MTMR9-ai-review.yaml
  source_selector: free-text
  source_context_yaml: "hypothesis: The horse protein A0A9L0T3C1 negatively regulates\
    \ autophagy.\nfocus_type: function_assignment\nterm_id: GO:0010507\nterm_label:\
    \ negative regulation of autophagy\ncontext:\n- |\n  # Focused function hypothesis\n\
    \n  Hypothesis: The horse protein A0A9L0T3C1 negatively regulates autophagy.\n\
    \n  Target: Equus caballus (NCBITaxon:9796), UniProt A0A9L0T3C1. Gene label: MTMR9;\
    \ verify identity independently rather than treating the label as proof.\n\n \
    \ Target GO claim: GO:0010507 \u2014 negative regulation of autophagy. Verify\
    \ its definition and scope.\n\n  ## Decisive question\n\n  Evaluate the partner-dependent\
    \ mechanism for this process and whether the exact protein supports it. Identify\
    \ experimentally grounded partners and substrate pathways. Distinguish complex\
    \ formation, enzyme regulation and the direction of an autophagy phenotype.\n\n\
    \  ## Identity and sequence inputs\n\n  - Target record: https://www.uniprot.org/uniprotkb/A0A9L0T3C1/entry\n\
    \  - Human comparison lead: https://www.uniprot.org/uniprotkb/Q96QG7/entry (MTMR9).\
    \ Establish the relevant orthology/isoform relationship rather than assuming it.\n\
    \  - Frozen current UniProt sequence: 507 residues; SHA-256 `0a21ea798953b735f23b338b4365a2eaa154a29b4f4db7db9c773e81a7022f3d`.\n\
    \  - These are current sequences downloaded for the cohort on 2026-09-08. Identity\
    \ with the original prediction-time input has not been established. Evaluate the\
    \ supplied sequence explicitly; document any different sequence used.\n\n  ```fasta\n\
    \  >A0A9L0T3C1 Equus caballus MTMR9\n  MEFAELIRTPRVDNVVLHRPFYPAVEGTLCLTGHHLILSSRQDNTEELWLLHSNIDAIDK\n\
    \  RFVGPLGTIIIKCKDFRIIQLDIPGMEECLNIASSIETSEWRLSYVNKEFAVCPSYPPIV\n  IVPKSIDDEALRKVATFRHGGRFPVLSYYHKKNGMVIMRSGQPLTGTNGRRCKEDEKLIN\n\
    \  ATLRAGKRGYIIDTRSLTVAQQARAKGGGFEQEAHYPQWRRIHKSIERYHILQESLIKLV\n  EACNDQTHNMDRWLSKLEASNWLTHIKEILTTACLAAQCIDREGASILIHGTEGTDSTLQ\n\
    \  VTSLAQIILEPRSRTIRGFEALIEREWLQAGHPFQQRCAQSAYCNSKQKWESPVFLLFLD\n  CVWQILRQFPCSFEFNENFLIMLFEHAYASQFGTFLGNNESERCKLKLQQKTMSLWSWVN\n\
    \  RPSELRKFTSPLFEANNLVIWPSVAPQSLHLWEGIFLRWNRSSKYLDEAYEEMVNIIEYN\n  KELQAKVNILRRQLAELETEDGMQESP\n\
    \  ```\n\n  ## Evidence and deliverable\n\n  Use primary literature and public\
    \ sequence, structural and genomic resources. Select analyses that answer the\
    \ decisive question; this is not a general gene review. Assess support and contrary\
    \ evidence, and allow an unresolved outcome. Distinguish directly observed horse\
    \ evidence, justified mammalian transfer, and results for a different protein\
    \ model.\n\n  Do not consult the ai-gene-review repository's existing judgments,\
    \ research syntheses or local bioinformatics analyses. Those are held out for\
    \ comparison. Do not use agreement with ARBA or another prediction as biological\
    \ validation. Preserve reproducible methods, accessions/versions, actual computation\
    \ outputs and primary-source URLs/DOIs/PMIDs. Report the decisive findings and\
    \ limitations, not just a verdict.\nreference_id: []"
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
citation_count: 3
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

- **Organism code:** HORSE
- **Taxon:** Equus caballus (NCBITaxon:9796)
- **Gene directory:** MTMR9
- **Gene symbol:** A0A9L0T3C1
- **UniProt accession:** A0A9L0T3C1

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** horse40-negative-autophagy-regulation
- **Source file:** genes/HORSE/MTMR9/MTMR9-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

The horse protein A0A9L0T3C1 negatively regulates autophagy.

## Term and Decision Context

- Term: negative regulation of autophagy (GO:0010507)
- # Focused function hypothesis

Hypothesis: The horse protein A0A9L0T3C1 negatively regulates autophagy.

Target: Equus caballus (NCBITaxon:9796), UniProt A0A9L0T3C1. Gene label: MTMR9; verify identity independently rather than treating the label as proof.

Target GO claim: GO:0010507 — negative regulation of autophagy. Verify its definition and scope.

## Decisive question

Evaluate the partner-dependent mechanism for this process and whether the exact protein supports it. Identify experimentally grounded partners and substrate pathways. Distinguish complex formation, enzyme regulation and the direction of an autophagy phenotype.

## Identity and sequence inputs

- Target record: https://www.uniprot.org/uniprotkb/A0A9L0T3C1/entry
- Human comparison lead: https://www.uniprot.org/uniprotkb/Q96QG7/entry (MTMR9). Establish the relevant orthology/isoform relationship rather than assuming it.
- Frozen current UniProt sequence: 507 residues; SHA-256 `0a21ea798953b735f23b338b4365a2eaa154a29b4f4db7db9c773e81a7022f3d`.
- These are current sequences downloaded for the cohort on 2026-09-08. Identity with the original prediction-time input has not been established. Evaluate the supplied sequence explicitly; document any different sequence used.

```fasta
>A0A9L0T3C1 Equus caballus MTMR9
MEFAELIRTPRVDNVVLHRPFYPAVEGTLCLTGHHLILSSRQDNTEELWLLHSNIDAIDK
RFVGPLGTIIIKCKDFRIIQLDIPGMEECLNIASSIETSEWRLSYVNKEFAVCPSYPPIV
IVPKSIDDEALRKVATFRHGGRFPVLSYYHKKNGMVIMRSGQPLTGTNGRRCKEDEKLIN
ATLRAGKRGYIIDTRSLTVAQQARAKGGGFEQEAHYPQWRRIHKSIERYHILQESLIKLV
EACNDQTHNMDRWLSKLEASNWLTHIKEILTTACLAAQCIDREGASILIHGTEGTDSTLQ
VTSLAQIILEPRSRTIRGFEALIEREWLQAGHPFQQRCAQSAYCNSKQKWESPVFLLFLD
CVWQILRQFPCSFEFNENFLIMLFEHAYASQFGTFLGNNESERCKLKLQQKTMSLWSWVN
RPSELRKFTSPLFEANNLVIWPSVAPQSLHLWEGIFLRWNRSSKYLDEAYEEMVNIIEYN
KELQAKVNILRRQLAELETEDGMQESP
```

## Evidence and deliverable

Use primary literature and public sequence, structural and genomic resources. Select analyses that answer the decisive question; this is not a general gene review. Assess support and contrary evidence, and allow an unresolved outcome. Distinguish directly observed horse evidence, justified mammalian transfer, and results for a different protein model.

Do not consult the ai-gene-review repository's existing judgments, research syntheses or local bioinformatics analyses. Those are held out for comparison. Do not use agreement with ARBA or another prediction as biological validation. Preserve reproducible methods, accessions/versions, actual computation outputs and primary-source URLs/DOIs/PMIDs. Report the decisive findings and limitations, not just a verdict.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: The horse protein A0A9L0T3C1 negatively regulates autophagy.
focus_type: function_assignment
term_id: GO:0010507
term_label: negative regulation of autophagy
context:
- |
  # Focused function hypothesis

  Hypothesis: The horse protein A0A9L0T3C1 negatively regulates autophagy.

  Target: Equus caballus (NCBITaxon:9796), UniProt A0A9L0T3C1. Gene label: MTMR9; verify identity independently rather than treating the label as proof.

  Target GO claim: GO:0010507 — negative regulation of autophagy. Verify its definition and scope.

  ## Decisive question

  Evaluate the partner-dependent mechanism for this process and whether the exact protein supports it. Identify experimentally grounded partners and substrate pathways. Distinguish complex formation, enzyme regulation and the direction of an autophagy phenotype.

  ## Identity and sequence inputs

  - Target record: https://www.uniprot.org/uniprotkb/A0A9L0T3C1/entry
  - Human comparison lead: https://www.uniprot.org/uniprotkb/Q96QG7/entry (MTMR9). Establish the relevant orthology/isoform relationship rather than assuming it.
  - Frozen current UniProt sequence: 507 residues; SHA-256 `0a21ea798953b735f23b338b4365a2eaa154a29b4f4db7db9c773e81a7022f3d`.
  - These are current sequences downloaded for the cohort on 2026-09-08. Identity with the original prediction-time input has not been established. Evaluate the supplied sequence explicitly; document any different sequence used.

  ```fasta
  >A0A9L0T3C1 Equus caballus MTMR9
  MEFAELIRTPRVDNVVLHRPFYPAVEGTLCLTGHHLILSSRQDNTEELWLLHSNIDAIDK
  RFVGPLGTIIIKCKDFRIIQLDIPGMEECLNIASSIETSEWRLSYVNKEFAVCPSYPPIV
  IVPKSIDDEALRKVATFRHGGRFPVLSYYHKKNGMVIMRSGQPLTGTNGRRCKEDEKLIN
  ATLRAGKRGYIIDTRSLTVAQQARAKGGGFEQEAHYPQWRRIHKSIERYHILQESLIKLV
  EACNDQTHNMDRWLSKLEASNWLTHIKEILTTACLAAQCIDREGASILIHGTEGTDSTLQ
  VTSLAQIILEPRSRTIRGFEALIEREWLQAGHPFQQRCAQSAYCNSKQKWESPVFLLFLD
  CVWQILRQFPCSFEFNENFLIMLFEHAYASQFGTFLGNNESERCKLKLQQKTMSLWSWVN
  RPSELRKFTSPLFEANNLVIWPSVAPQSLHLWEGIFLRWNRSSKYLDEAYEEMVNIIEYN
  KELQAKVNILRRQLAELETEDGMQESP
  ```

  ## Evidence and deliverable

  Use primary literature and public sequence, structural and genomic resources. Select analyses that answer the decisive question; this is not a general gene review. Assess support and contrary evidence, and allow an unresolved outcome. Distinguish directly observed horse evidence, justified mammalian transfer, and results for a different protein model.

  Do not consult the ai-gene-review repository's existing judgments, research syntheses or local bioinformatics analyses. Those are held out for comparison. Do not use agreement with ARBA or another prediction as biological validation. Preserve reproducible methods, accessions/versions, actual computation outputs and primary-source URLs/DOIs/PMIDs. Report the decisive findings and limitations, not just a verdict.
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

**Target:** Horse (*Equus caballus*, NCBITaxon:9796) protein **A0A9L0T3C1** (gene label **MTMR9**, 507 aa)
**Hypothesis (focus type: function_assignment):** The protein *negatively regulates autophagy* — GO:0010507 (negative regulation of autophagy, BP).
**Human comparison lead:** MTMR9 / Q96QG7.
**Date:** 2026-09-08

---

## Summary

**Verdict: Partially supported (via justified mammalian transfer, with a mandatory scoping caveat).**

The hypothesis that horse MTMR9 (A0A9L0T3C1) negatively regulates autophagy is mechanistically grounded in primary literature, **but MTMR9 does not perform this function as a direct enzyme.** MTMR9 is a **catalytically inactive pseudophosphatase**. Its autophagy-relevant activity is entirely **partner/complex-dependent**: MTMR9 is an obligate activating subunit that binds active myotubularins (MTMR6/MTMR7/MTMR8), boosts their lipid-phosphatase activity, and redirects their substrate preference. In the **MTMR8/MTMR9 complex**, MTMR9 stimulates MTMR8 turnover of **PtdIns(3)P** and lowers cellular PtdIns(3)P — the essential autophagosome-nucleation lipid — thereby suppressing autophagy ([PMID:22647598](https://pubmed.ncbi.nlm.nih.gov/22647598/)). This supports GO:0010507 for MTMR9 **as a regulatory subunit**, not as a standalone catalytic effector.

The identity basis for transferring human evidence to horse is strong. A Needleman–Wunsch global alignment of the supplied 507-residue horse sequence against human MTMR9 (Q96QG7, 549 aa) gave **90.3% global identity (496/549) and 97.8% identity across the horse protein's length**, with an **identical, catalytically dead phosphatase P-loop** (`LIHGTEGTDSTLQVT`) in both species. The horse protein is a bona fide 1:1 MTMR9 ortholog; the ~42-residue length difference maps to a single contiguous N-terminal segment (likely a missing exon in the predicted horse gene model), while all functional domains are intact.

Three caveats dominate the curation decision. **(i)** All direct evidence is human/mammalian cell-based — there is **no horse-specific experimental evidence**; this is orthology transfer. **(ii)** The effect is **context-dependent**: in neurons, MTMR9 knockdown (unlike MTMR5/MTMR2) did **not** enhance autophagic substrate clearance ([PMID:35580604](https://pubmed.ncbi.nlm.nih.gov/35580604/)). **(iii)** MTMR9's most directly documented cellular function is arguably **ER-to-Golgi trafficking/secretion** ([PMID:31704058](https://pubmed.ncbi.nlm.nih.gov/31704058/)), competing with autophagy for "primary function" status, with autophagy being a downstream consequence of PtdIns(3)P depletion.

---

## Key Findings

### Finding 1 — Horse A0A9L0T3C1 is a catalytically dead (pseudophosphatase) MTMR9 ortholog

The supplied 507-amino-acid horse sequence was verified in full (length = 507, matching the frozen record). Its myotubularin protein-tyrosine-phosphatase (PTP) P-loop region reads `...ILIHGTEGTDSTLQ...` at approximately residues 289–300. Critically, **the canonical active-site cysteine of the CX₅R catalytic motif is absent from the phosphatase P-loop.** The only CX₅R-pattern match anywhere in the protein (`CVWQILR` at ~360) lies *outside* the P-loop and is incidental — it is not positioned to act as a catalytic nucleophile. The domain architecture — an N-terminal PH-GRAM lipid-binding region, an inactive PTP-like domain, and a C-terminal coiled-coil (`...RRQLAELETE`) for dimerization — matches human MTMR9 (Q96QG7).

This is exactly what the myotubularin literature predicts. Human MTMR9 is one of the **seven catalytically inactive myotubularins** that lack the conserved active-site cysteine required for phosphatase activity: *"Seven members are inactive because they lack the conserved cysteine residue in the CX(5)R motif required for activity"* ([PMID:22647598](https://pubmed.ncbi.nlm.nih.gov/22647598/)). The consequence for curation is decisive: **MTMR9 cannot dephosphorylate PtdIns(3)P (or any phosphoinositide) on its own.** Any autophagy phenotype must therefore be mediated through a partner, not through intrinsic catalysis.

### Finding 2 — MTMR9 negatively regulates autophagy as an activating subunit of the MTMR8/MTMR9 PI3P-phosphatase complex

The mechanistic basis for the autophagy claim is Zou et al. 2012 ([PMID:22647598](https://pubmed.ncbi.nlm.nih.gov/22647598/)). MTMR9 dimerizes with the active myotubularins MTMR6/7/8; complex formation **increases the partner's catalytic activity and changes its substrate specificity.** The MTMR8/MTMR9 complex prefers **PtdIns(3)P** as substrate (MTMR9 raises MTMR8 activity toward PtdIns(3)P roughly fourfold) and, in cells, the complex **reduces cellular PtdIns(3)P levels.** The paper's title explicitly frames MTMR9 as the determinant of *"the enzymatic activity, substrate specificity, and role in autophagy of MTMR8."*

The link to autophagy is lipid-mediated and well established at the pathway level: **PtdIns(3)P is the essential autophagy-initiating lipid** (produced by class III PI3K/VPS34) that marks the phagophore/omegasome and recruits the autophagy machinery for autophagosome nucleation. Depleting PtdIns(3)P suppresses autophagosome formation. Verbatim support: *"the MTMR8/R9 complex prefers PtdIns(3)P"* and *"whereas the MTMR8/R9 complex reduces cellular PtdIns(3)P levels."* Together these establish a coherent negative-regulation mechanism: MTMR9 (adaptor) → activates MTMR8 (enzyme) → depletes PtdIns(3)P (pro-autophagic lipid) → suppresses autophagy.

However, the direction and magnitude of the autophagy phenotype are **not uniform across cell types.** Chua et al. 2022 report that *"knockdown of MTMR5 or MTMR2, but not the unrelated phosphatase MTMR9, significantly enhances neuronal degradation of TDP-43"* ([PMID:35580604](https://pubmed.ncbi.nlm.nih.gov/35580604/)). In neurons, removing MTMR9 did not enhance autophagic substrate clearance — the opposite of what a simple, universal autophagy-suppressor model would predict. This qualifies the hypothesis: the autophagy-suppressive role is **context- and partner-dependent**, contingent on which active myotubularin partner is expressed and active in a given tissue.

### Finding 3 — Horse MTMR9 is a 1:1 ortholog of human MTMR9 with an identical inactive P-loop

A Needleman–Wunsch global alignment (identity scoring, gap penalty = −1) was run between horse A0A9L0T3C1 (507 aa) and human MTMR9 Q96QG7 (549 aa, fetched from the UniProt REST API). Results: **496/549 identical residues = 90.3% global identity**, and **97.8% identity across the 507-residue horse length.** The ~42-residue difference reflects a shorter/truncated horse record rather than sequence divergence within the aligned region. The myotubularin PTP P-loop is **identical** in both species (both read `LIHGTEGTDSTLQVT`), and in both species it **lacks the catalytic CX₅R cysteine** required for phosphatase activity.

This conservation level — especially the identity of the functional signature motif and the shared loss of the catalytic cysteine — strongly supports treating the horse protein as a true functional ortholog. It is the empirical justification for transferring the human mechanistic evidence (Finding 2) to the horse annotation via ISS/ISO.

### Finding 4 — Horse-vs-human differences localize to one N-terminal segment; functional domains intact

The alignment traceback (executed programmatically) shows that the 42 residues present in human MTMR9 but absent from the horse record form a **single contiguous block** at human residues ~92–139 (containing sequence such as `IASS...ITLMYPFFYRPMFEV...EDGWHSFLPEQEF...LYSSA`), located near/after the N-terminal PH-GRAM region. The **PTP-like pseudophosphatase domain** (P-loop `LIHGTEGTDSTLQVT`) and the **C-terminal coiled-coil dimerization region** are fully conserved (they fall within the 97.8% identity over the horse length).

The interpretation is that the horse difference is best explained as a **single N-terminal gene-model/exon gap** rather than a biologically meaningful divergence. The partner-binding and pseudophosphatase machinery that underpins the autophagy mechanism is intact. The gene-model artifact does not undermine functional transfer, but it should be flagged so curators know the horse record may be incomplete at its N-terminus (a truncated PH-GRAM could in principle alter membrane targeting).

---

## Mechanistic Model / Interpretation

The evidence converges on a single coherent model in which MTMR9 is an **obligate, catalytically dead regulatory subunit**, not an autophagy enzyme:

```
   MTMR9 (A0A9L0T3C1, horse)  =  pseudophosphatase ADAPTOR
   ┌─────────────────────────────────────────────────────────┐
   │  PH-GRAM  │  inactive PTP-like domain  │  coiled-coil     │
   │ (lipid/   │  (NO catalytic CX5R Cys —  │ (dimerization    │
   │  membrane)│   cannot dephosphorylate)  │  with partners)  │
   └─────────────────────────────────────────────────────────┘
                              │
                              │  heterodimerizes via coiled-coil
                              ▼
        MTMR6 / MTMR7 / MTMR8  (CATALYTICALLY ACTIVE partner)
                              │
             MTMR9 raises partner activity (~4x for MTMR8)
             and steers substrate specificity → PtdIns(3)P
                              ▼
                 depletes cellular PtdIns(3)P
                              │
        PtdIns(3)P = essential autophagosome-nucleation lipid
                              ▼
             ↓ autophagosome formation  =  NEGATIVE
                regulation of autophagy (GO:0010507)
                     — but CONTEXT-DEPENDENT
```

**Two features dominate the curation decision.** First, the activity is **indirect**. GO:0010507 is a *regulation* Biological Process node, so an indirect/regulatory contribution is not disqualifying in principle — regulation terms are appropriate for adaptors and scaffolds. But the *direct* molecular function of MTMR9 is **enzyme regulator / phosphatase activator + protein heterodimerization**, and the autophagy effect is a downstream *pathway* consequence of PtdIns(3)P depletion by the *partner*. Curators should not let GO:0010507 imply that MTMR9 is itself a lipid phosphatase acting on the autophagy pathway.

Second, the phenotype's **direction is not universal.** The Zou model (autophagy suppression via PtdIns(3)P depletion) is established in one system; the Chua neuronal data show no autophagy enhancement upon MTMR9 knockdown. This is consistent with a model in which MTMR9's net effect on autophagy depends on which active partner (MTMR6/7/8) it is paired with, the relative abundance of PtdIns(3)P pools, and tissue context. Quantitatively, MTMR9's boost to MTMR8/PtdIns(3)P activity is modest (~4-fold) compared to its large effect on MTMR6/PtdIns(3,5)P₂ (~30-fold), so autophagy is not obviously the dominant output of the module.

A competing/parallel function complicates the "primary function" question: MTMR9 localizes to the ER–Golgi intermediate compartment and Golgi, recruits its active partners MTMR6/MTMR8 there, co-localizes with and regulates RAB1A/WHAMM, and modulates protein secretion (including WNT3A) ([PMID:31704058](https://pubmed.ncbi.nlm.nih.gov/31704058/)). This trafficking role may be at least as central to MTMR9's biology as autophagy regulation.

---

## Evidence Base

| Citation | Evidence type | Supports / Refutes / Qualifies / Competing | Claim tested | Key finding | Organism / context | Confidence & limitations |
|---|---|---|---|---|---|---|
| [PMID:22647598](https://pubmed.ncbi.nlm.nih.gov/22647598/) (Zou et al. 2012, JBC) | Direct biochemical assay + cell PI3P measurement | **Supports** | MTMR9 lowers PtdIns(3)P via MTMR8 → suppresses autophagy | MTMR9 dimerizes with MTMR6/7/8, increases activity, alters specificity; **MTMR8/R9 complex prefers PtdIns(3)P** and **reduces cellular PtdIns(3)P**; title: MTMR9 "determines the … role in autophagy of MTMR8" | Human cell lines; in vitro enzymology + cellular lipid levels | High for mechanism; autophagy readout is downstream of lipid change; horse not tested; MTMR9 indirect/non-catalytic |
| [PMID:22647598](https://pubmed.ncbi.nlm.nih.gov/22647598/) | Sequence/structural annotation | **Qualifies** | MTMR9 is catalytically dead | 7 myotubularins (incl. MTMR9) lack the CX₅R catalytic cysteine | Human/family-wide | High; confirms activity is indirect |
| [PMID:35580604](https://pubmed.ncbi.nlm.nih.gov/35580604/) (Chua et al. 2022) | Loss-of-function (knockdown) phenotype | **Qualifies / partial refute of universality** | Does MTMR9 loss enhance autophagy? | MTMR5/MTMR2 knockdown enhanced neuronal TDP-43 autophagic degradation; **MTMR9 knockdown did NOT** | iPSC-derived neurons | Moderate–high; shows cell-type/partner-context dependence |
| [PMID:31704058](https://pubmed.ncbi.nlm.nih.gov/31704058/) (Doubravská et al. 2020) | Localization + interaction + LOF phenotype | **Competing (alternative core function)** | Primary cellular role of MTMR9 | MTMR9 localizes to ERGIC/Golgi, recruits MTMR6/MTMR8, regulates RAB1A/WHAMM; loss disrupts Golgi and reduces WNT3A secretion | Human cells | High for trafficking role; autophagy not the assayed endpoint |
| This report (sequence analysis) | Structural/evolutionary (computational) | **Supports mechanism (pseudophosphatase)** | Is horse MTMR9 catalytically active? | 507-aa horse seq verified; P-loop `ILIHGTEGTDSTLQ` lacks catalytic CX₅R cysteine → inactive; PH-GRAM + inactive PTP + coiled-coil architecture matches MTMR9 | *Equus caballus* supplied sequence | High; horse protein must act through partners |
| This report (NW alignment vs Q96QG7) | Structural/evolutionary (computational) | **Supports orthology transfer** | Is A0A9L0T3C1 a true MTMR9 ortholog? | **496/549 = 90.3% global; 97.8% over horse length**; identical P-loop `LIHGTEGTDSTLQVT`, both catalytically dead | Horse vs human MTMR9 | High; 1:1 ortholog; horse record ~42 aa shorter (single N-terminal block) |

**Literature notes:**

- ***Myotubularin-related protein (MTMR) 9 determines the enzymatic activity, substrate specificity, and role in autophagy of MTMR8.*** [PMID:22647598](https://pubmed.ncbi.nlm.nih.gov/22647598/). The central mechanistic paper — establishes MTMR9's catalytic inactivity, its activating heterodimer role, PtdIns(3)P depletion by the MTMR8/MTMR9 complex, and its governance of MTMR8's autophagy role. **Primary support** for both the mechanism and the "indirect/adaptor" scoping.
- ***Myotubularin-related phosphatase 5 is a critical determinant of autophagy in neurons.*** [PMID:35580604](https://pubmed.ncbi.nlm.nih.gov/35580604/). MTMR9 knockdown did not enhance neuronal TDP-43 degradation (unlike MTMR2/MTMR5). **Qualifies** the hypothesis by showing cell-type/context dependence.
- ***Human myotubularin-related protein 9 regulates ER-to-Golgi trafficking and modulates WNT3A secretion.*** [PMID:31704058](https://pubmed.ncbi.nlm.nih.gov/31704058/). Documents MTMR9's ERGIC/Golgi localization, RAB1A/WHAMM regulation, and secretion control. **Competing alternative** for MTMR9's primary cellular function.

---

## GO Curation Implications

- **Lead (requires curator verification): GO:0010507 (negative regulation of autophagy, BP) is defensible for horse MTMR9 but should be annotated as a complex-mediated/regulatory role, not a direct catalytic activity.** Suggested framing: MTMR9 *contributes to* negative regulation of autophagy **as part of / via** the MTMR8(or MTMR6/7)–MTMR9 phosphoinositide-3-phosphatase complex.
- **Evidence code:** For horse this is orthology transfer → best supported as **ISS/ISO** with the human papers as source (with/from Q96QG7), **not IDA** (no horse assay). The upstream human evidence is IDA/IMP-grade ([PMID:22647598](https://pubmed.ncbi.nlm.nih.gov/22647598/)).
- **Do NOT assign MF "phosphatidylinositol-3-phosphate phosphatase activity" to MTMR9 itself** — it is catalytically inactive. Better-supported MF terms are **phosphatase activator / enzyme activator activity** and **protein heterodimerization activity** with active myotubularins — both more informative than bare "protein binding."
- **Consider co-annotating** the well-documented **ER-to-Golgi vesicle-mediated transport / regulation of protein secretion** functions ([PMID:31704058](https://pubmed.ncbi.nlm.nih.gov/31704058/)), which are at least as strongly supported and may be the primary cellular role.
- **CC:** MTMR8/MTMR9 (myotubularin) phosphatase complex; ERGIC/Golgi membrane localization.
- **Non-core flag:** Treat GO:0010507 as a **context-dependent, non-primary** annotation.

---

## Mechanistic Scope

**Immediate molecular function of MTMR9:** a pseudophosphatase adaptor/activator. It heterodimerizes with catalytically active myotubularins and (a) increases their catalytic rate and (b) shifts substrate preference. In the MTMR8/R9 complex, the net cellular effect is **depletion of PtdIns(3)P**. MTMR9 has **no intrinsic phosphatase activity** (dead P-loop).

**Link to autophagy (downstream):** PtdIns(3)P produced by VPS34 at the phagophore is required for autophagosome nucleation and maturation. Lowering PtdIns(3)P via MTMR8/R9 therefore **reduces autophagy** — the mechanistic basis for GO:0010507. The autophagy phenotype is a **downstream consequence of a lipid-level change**, not a direct activity of MTMR9.

**Direction of phenotype:** ↑ MTMR8/R9 complex activity → ↓ PtdIns(3)P → ↓ autophagy (negative regulation). Loss of the complex would be expected to ↑ autophagy — but this was **not observed for MTMR9 knockdown in neurons** ([PMID:35580604](https://pubmed.ncbi.nlm.nih.gov/35580604/)), underscoring context dependence.

**Effects inferred only from loss of function:** the neuronal TDP-43 clearance data are knockdown phenotypes; MTMR9 knockdown did not change autophagic clearance, so loss-of-function evidence does not support a universal autophagy-suppressor role.

---

## Conflicts and Alternatives

- **Alternative core function (competing):** [PMID:31704058](https://pubmed.ncbi.nlm.nih.gov/31704058/) makes a strong case that MTMR9's primary documented cellular role is in **ER-to-Golgi trafficking and secretion** (RAB1A/WHAMM, WNT3A). Autophagy regulation may be a secondary/PtdIns(3)P-mediated consequence rather than the primary function.
- **Context/cell-type conflict:** MTMR9 knockdown did not enhance autophagy in neurons ([PMID:35580604](https://pubmed.ncbi.nlm.nih.gov/35580604/)), whereas MTMR5/MTMR2 did. The autophagy-suppressive role may be limited to cells where MTMR6/7/8 are co-expressed and PtdIns(3)P is rate-limiting.
- **Subfamily/paralog attribution:** The best-characterized "autophagy" myotubularin modules are actually MTMR5(SBF1)/MTMR2 ([PMID:35580604](https://pubmed.ncbi.nlm.nih.gov/35580604/)) and MTMR14 (Jumpy). Care is needed not to over-transfer autophagy roles across the family; MTMR9's contribution is specifically via MTMR6/7/8, and its quantitative boost to MTMR8/PtdIns(3)P is modest (~4×) vs its ~30× effect on MTMR6/PtdIns(3,5)P₂.
- **Horse vs human isoform/length:** the horse record is 507 aa vs human 549 aa; likely a shorter isoform/assembly with a single N-terminal missing block, but the functional PH-GRAM, inactive-PTP and coiled-coil regions are present, so orthology and the partner-dependent mechanism are preserved. No horse assay exists.

---

## Limitations and Knowledge Gaps

| Gap | What was checked | Why it matters | What would resolve it |
|---|---|---|---|
| No horse-specific data | PubMed for MTMR9/autophagy — all hits human | Annotation rests entirely on transfer | Confirm MTMR6/7/8 orthologs & co-expression in horse tissues; a horse-cell autophagy assay |
| Directionality of the autophagy phenotype for MTMR9 specifically | Zou (suppress) vs Chua (no effect in neurons) | GO:0010507 asserts a *negative* direction; may not hold in all tissues | Tissue-panel autophagy-flux with defined MTMR partners |
| Primary vs downstream | Compared autophagy vs trafficking literature | Determines whether GO:0010507 is core or non-core | Comparative loss-of-function phenotyping (autophagy vs secretion) |
| Partner requirement | Human data implicate MTMR6/7/8; horse partners not examined | Mechanism requires a specific active heterodimer | Co-IP/interaction proteomics + RNA-seq of partner expression in horse |
| Horse record completeness | NW alignment traceback: one N-terminal ~42-aa gap (human ~92–139) | Sequence-based annotation may use an incomplete model; truncated PH-GRAM could alter targeting | Inspect horse genomic locus/RefSeq model & RNA-seq exon coverage |
| Quantitative MTMR9-only autophagy readout | Zou measured PtdIns(3)P & MTMR8 activity, not MTMR9-only flux | Strength of the *negative regulation* claim | LC3-II/p62 flux & autophagosome counts on MTMR9-specific perturbation |

---

## Discriminating Tests

- **Horse-cell autophagy assay:** LC3-II/p62 flux and autophagosome counts (± bafilomycin) after MTMR9 knockdown/overexpression in an equine cell line, with and without MTMR8 co-manipulation.
- **PtdIns(3)P quantification** (2×FYVE biosensor / mass assay) upon MTMR8/R9 modulation to link the lipid change to autophagy directionality.
- **Complex-disruption mutant:** MTMR9 point mutants that abolish MTMR8 binding but preserve the protein — do they lose the autophagy effect (proving partner dependence)?
- **Partner co-expression map** in horse tissues (MTMR6/7/8) to predict where the autophagy role is active.
- **Epistasis vs VPS34:** does MTMR8/R9 suppression of autophagy require ongoing VPS34 PtdIns(3)P synthesis?
- **Separation-of-function:** test whether the autophagy effect and the ERGIC/Golgi trafficking effect are mechanistically coupled or independent (RAB1A controls).
- **Sequence/gene-model confirmation:** RNA-seq/Iso-Seq to confirm or correct the horse N-terminal exon gap.

---

## Proposed Follow-up Actions (Curation Leads)

*All leads require curator verification.*

1. **Retain GO:0010507 as ISS/ISO, scoped as complex-mediated regulation.** With-from: human MTMR9 (Q96QG7). Note that MTMR9 is a catalytically dead adaptor and the effect is indirect and context-dependent.
2. **Add more informative MF terms** for the direct action: *phosphatase activator activity* / *phosphoinositide phosphatase regulator activity* and *protein heterodimerization activity*. Prefer these over "protein binding."
3. **Consider a CC annotation** for ER–Golgi intermediate compartment / Golgi membrane and the MTMR8/MTMR9 phosphatase complex ([PMID:31704058](https://pubmed.ncbi.nlm.nih.gov/31704058/)).
4. **Flag the horse gene-model gap** (single N-terminal ~42-aa block missing vs human) for sequence-curation review.
5. **Candidate reference snippets to verify:**
   - [PMID:22647598](https://pubmed.ncbi.nlm.nih.gov/22647598/): *"the MTMR8/R9 complex prefers PtdIns(3)P"*; *"whereas the MTMR8/R9 complex reduces cellular PtdIns(3)P levels"*; *"Seven members are inactive because they lack the conserved cysteine residue in the CX(5)R motif required for activity."*
   - [PMID:35580604](https://pubmed.ncbi.nlm.nih.gov/35580604/): *"knockdown of MTMR5 or MTMR2, but not the unrelated phosphatase MTMR9, significantly enhances neuronal degradation of TDP-43."*
6. **Suggested curator question:** Is negative regulation of autophagy a *core* function or a downstream consequence of PtdIns(3)P depletion, given the equally strong trafficking evidence?
7. **Suggested experiment:** equine-cell autophagy flux ± MTMR9/MTMR8 perturbation (above).

---

## Provenance

- **Sequence check (executed):** input length verified = **507 aa**; PTP P-loop region `ILIHGTEGTDSTLQ` (~res 289–300) **lacks the catalytic CX₅R cysteine** (only CX₅R match `CVWQILR`@360 lies outside the P-loop) → inactive pseudophosphatase, consistent with human MTMR9.
- **Orthology (executed):** Needleman–Wunsch global alignment vs UniProt **Q96QG7** (human MTMR9, 549 aa, fetched via REST): **496/549 identical = 90.3% global; 97.8% over the horse 507-aa length**; **identical P-loop** `LIHGTEGTDSTLQVT` in both species (both catalytically dead). Confirms A0A9L0T3C1 is a bona fide 1:1 MTMR9 ortholog and validates human→horse evidence transfer.
- **Gap localization (executed):** the 42 human-only residues traceback to a **single contiguous block at human residues ~92–139** (`IASS…LYSSA`), i.e., one missing N-terminal segment near the PH-GRAM region — consistent with a missing exon in the predicted horse model. The PTP-like domain, P-loop and C-terminal coiled-coil are intact.
- **Literature:** PMID:22647598, PMID:35580604, PMID:31704058 (abstracts retrieved via PubMed).

---

## Bottom Line

Horse A0A9L0T3C1 is a genuine MTMR9 ortholog, and human evidence shows MTMR9 **does** contribute to negative regulation of autophagy — but **indirectly**, as a catalytically dead activating subunit of a PtdIns(3)P-depleting myotubularin complex, and in a **context-dependent** manner. GO:0010507 is a defensible inferred (ISS/ISO) annotation for horse MTMR9 **if scoped as a complex-mediated, non-catalytic, partner-dependent regulatory role**, complemented by more informative molecular-function terms and with clear caveats about the absence of horse-specific data and a competing ER-to-Golgi trafficking function.


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)