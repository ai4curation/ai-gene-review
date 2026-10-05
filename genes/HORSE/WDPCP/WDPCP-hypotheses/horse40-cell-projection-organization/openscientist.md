---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-08T15:57:03.798452'
end_time: '2026-09-08T16:39:11.108041'
duration_seconds: 2527.31
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: HORSE
  gene: WDPCP
  gene_symbol: WDPCP
  uniprot_accession: A0A3Q2KRK8
  taxon_id: NCBITaxon:9796
  taxon_label: Equus caballus
  focus_type: function_assignment
  hypothesis_slug: horse40-cell-projection-organization
  hypothesis_text: The horse protein A0A3Q2KRK8 participates in cell projection organization.
  term_context: "- Term: cell projection organization (GO:0030030)\n- # Focused function\
    \ hypothesis\n\nHypothesis: The horse protein A0A3Q2KRK8 participates in cell\
    \ projection organization.\n\nTarget: Equus caballus (NCBITaxon:9796), UniProt\
    \ A0A3Q2KRK8. Gene label: WDPCP; verify identity independently rather than treating\
    \ the label as proof.\n\nTarget GO claim: GO:0030030 \u2014 cell projection organization.\
    \ Verify its definition and scope.\n\n## Decisive question\n\nEvaluate the molecular\
    \ scaffold and experimental basis for the broad cell-projection-organization process.\
    \ Compare relevant mammalian structures and isoforms, and distinguish alterations\
    \ affecting a specific biochemical property from those that undermine the whole\
    \ process.\n\n## Identity and sequence inputs\n\n- Target record: https://www.uniprot.org/uniprotkb/A0A3Q2KRK8/entry\n\
    - Human comparison lead: https://www.uniprot.org/uniprotkb/O95876/entry (WDPCP).\
    \ Establish the relevant orthology/isoform relationship rather than assuming it.\n\
    - Frozen current UniProt sequence: 705 residues; SHA-256 `a132072d392ff9ec8d0962a571a5ae3534476ecfc0679bdeb9051777f3aa5a0a`.\n\
    - These are current sequences downloaded for the cohort on 2026-09-08. Identity\
    \ with the original prediction-time input has not been established. Evaluate the\
    \ supplied sequence explicitly; document any different sequence used.\n\n```fasta\n\
    >A0A3Q2KRK8 Equus caballus WDPCP\nMSFCLTELHLWSLKNTLHIGDRDIGVYQYYDKKDPPVTDHGNLEEKQKLAESRDYPWTLK\n\
    NRRPEKLRDSLKELEELMQNSQCVLSKWNNKYVCQLLFGSGVLVSLSLSGPQLEKVVIDR\nSLVGKLISDTISDALLTDSFIILSFFAQNKLCFIQFTKKMGSPDVNKRLEKLSALDYKIS\n\
    YYEIPGPVNRTTERRLAINCVQDIVVCWWPLVSDDAWPWAPISSEKNRANLLLLGYAQGR\nLEVLSSVRTEWDPLDVRFGTKQPYQVLTVERSISVDKEPMADSCIYEYVRNKIHCVSVTR\n\
    IPLRSKAISCCRNVTEDKLILGCEDSSLILYETHRRVTLLAQAELLPSLICCHPTGSILL\nVGSNQGELQIFDMALSPINIQLLAEDRSPRETLQFNKFFDVSSGLVQMQWIAPQVVSQKP\n\
    DSGDIYDLLFLRFDRGPLGVLLFKLGIFTRGQLGLVDIIFQYIHCDEICEAINILSSMNW\nDTLGHQCFISMSAIVNHLLRQKLTPEREAQLEASLGTFYAPTRPLLDSTVLEYRDQISKY\n\
    ARRFFHHLLRYQRFEKAFLLAVDIGARDLFMDIHYLALDKGELALAEVARKKASDIDAES\nITSGVELLGPLHRGDTLNEAFVGLSLAPQREDTFPDNLPHFCSVHRHIIQQRTLNVSSNG\n\
    QVFNRRNKLEKDTCAGSLMPKTCNEEDQSFDVASYWKHQQWTMYA\n```\n\n## Evidence and deliverable\n\
    \nUse primary literature and public sequence, structural and genomic resources.\
    \ Select analyses that answer the decisive question; this is not a general gene\
    \ review. Assess support and contrary evidence, and allow an unresolved outcome.\
    \ Distinguish directly observed horse evidence, justified mammalian transfer,\
    \ and results for a different protein model.\n\nDo not consult the ai-gene-review\
    \ repository's existing judgments, research syntheses or local bioinformatics\
    \ analyses. Those are held out for comparison. Do not use agreement with ARBA\
    \ or another prediction as biological validation. Preserve reproducible methods,\
    \ accessions/versions, actual computation outputs and primary-source URLs/DOIs/PMIDs.\
    \ Report the decisive findings and limitations, not just a verdict."
  reference_context: No specific reference context supplied.
  source_file: genes/HORSE/WDPCP/WDPCP-ai-review.yaml
  source_selector: free-text
  source_context_yaml: "hypothesis: The horse protein A0A3Q2KRK8 participates in cell\
    \ projection organization.\nfocus_type: function_assignment\nterm_id: GO:0030030\n\
    term_label: cell projection organization\ncontext:\n- |\n  # Focused function\
    \ hypothesis\n\n  Hypothesis: The horse protein A0A3Q2KRK8 participates in cell\
    \ projection organization.\n\n  Target: Equus caballus (NCBITaxon:9796), UniProt\
    \ A0A3Q2KRK8. Gene label: WDPCP; verify identity independently rather than treating\
    \ the label as proof.\n\n  Target GO claim: GO:0030030 \u2014 cell projection\
    \ organization. Verify its definition and scope.\n\n  ## Decisive question\n\n\
    \  Evaluate the molecular scaffold and experimental basis for the broad cell-projection-organization\
    \ process. Compare relevant mammalian structures and isoforms, and distinguish\
    \ alterations affecting a specific biochemical property from those that undermine\
    \ the whole process.\n\n  ## Identity and sequence inputs\n\n  - Target record:\
    \ https://www.uniprot.org/uniprotkb/A0A3Q2KRK8/entry\n  - Human comparison lead:\
    \ https://www.uniprot.org/uniprotkb/O95876/entry (WDPCP). Establish the relevant\
    \ orthology/isoform relationship rather than assuming it.\n  - Frozen current\
    \ UniProt sequence: 705 residues; SHA-256 `a132072d392ff9ec8d0962a571a5ae3534476ecfc0679bdeb9051777f3aa5a0a`.\n\
    \  - These are current sequences downloaded for the cohort on 2026-09-08. Identity\
    \ with the original prediction-time input has not been established. Evaluate the\
    \ supplied sequence explicitly; document any different sequence used.\n\n  ```fasta\n\
    \  >A0A3Q2KRK8 Equus caballus WDPCP\n  MSFCLTELHLWSLKNTLHIGDRDIGVYQYYDKKDPPVTDHGNLEEKQKLAESRDYPWTLK\n\
    \  NRRPEKLRDSLKELEELMQNSQCVLSKWNNKYVCQLLFGSGVLVSLSLSGPQLEKVVIDR\n  SLVGKLISDTISDALLTDSFIILSFFAQNKLCFIQFTKKMGSPDVNKRLEKLSALDYKIS\n\
    \  YYEIPGPVNRTTERRLAINCVQDIVVCWWPLVSDDAWPWAPISSEKNRANLLLLGYAQGR\n  LEVLSSVRTEWDPLDVRFGTKQPYQVLTVERSISVDKEPMADSCIYEYVRNKIHCVSVTR\n\
    \  IPLRSKAISCCRNVTEDKLILGCEDSSLILYETHRRVTLLAQAELLPSLICCHPTGSILL\n  VGSNQGELQIFDMALSPINIQLLAEDRSPRETLQFNKFFDVSSGLVQMQWIAPQVVSQKP\n\
    \  DSGDIYDLLFLRFDRGPLGVLLFKLGIFTRGQLGLVDIIFQYIHCDEICEAINILSSMNW\n  DTLGHQCFISMSAIVNHLLRQKLTPEREAQLEASLGTFYAPTRPLLDSTVLEYRDQISKY\n\
    \  ARRFFHHLLRYQRFEKAFLLAVDIGARDLFMDIHYLALDKGELALAEVARKKASDIDAES\n  ITSGVELLGPLHRGDTLNEAFVGLSLAPQREDTFPDNLPHFCSVHRHIIQQRTLNVSSNG\n\
    \  QVFNRRNKLEKDTCAGSLMPKTCNEEDQSFDVASYWKHQQWTMYA\n  ```\n\n  ## Evidence and deliverable\n\
    \n  Use primary literature and public sequence, structural and genomic resources.\
    \ Select analyses that answer the decisive question; this is not a general gene\
    \ review. Assess support and contrary evidence, and allow an unresolved outcome.\
    \ Distinguish directly observed horse evidence, justified mammalian transfer,\
    \ and results for a different protein model.\n\n  Do not consult the ai-gene-review\
    \ repository's existing judgments, research syntheses or local bioinformatics\
    \ analyses. Those are held out for comparison. Do not use agreement with ARBA\
    \ or another prediction as biological validation. Preserve reproducible methods,\
    \ accessions/versions, actual computation outputs and primary-source URLs/DOIs/PMIDs.\
    \ Report the decisive findings and limitations, not just a verdict.\nreference_id:\
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
citation_count: 8
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
- **Gene directory:** WDPCP
- **Gene symbol:** WDPCP
- **UniProt accession:** A0A3Q2KRK8

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** horse40-cell-projection-organization
- **Source file:** genes/HORSE/WDPCP/WDPCP-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

The horse protein A0A3Q2KRK8 participates in cell projection organization.

## Term and Decision Context

- Term: cell projection organization (GO:0030030)
- # Focused function hypothesis

Hypothesis: The horse protein A0A3Q2KRK8 participates in cell projection organization.

Target: Equus caballus (NCBITaxon:9796), UniProt A0A3Q2KRK8. Gene label: WDPCP; verify identity independently rather than treating the label as proof.

Target GO claim: GO:0030030 — cell projection organization. Verify its definition and scope.

## Decisive question

Evaluate the molecular scaffold and experimental basis for the broad cell-projection-organization process. Compare relevant mammalian structures and isoforms, and distinguish alterations affecting a specific biochemical property from those that undermine the whole process.

## Identity and sequence inputs

- Target record: https://www.uniprot.org/uniprotkb/A0A3Q2KRK8/entry
- Human comparison lead: https://www.uniprot.org/uniprotkb/O95876/entry (WDPCP). Establish the relevant orthology/isoform relationship rather than assuming it.
- Frozen current UniProt sequence: 705 residues; SHA-256 `a132072d392ff9ec8d0962a571a5ae3534476ecfc0679bdeb9051777f3aa5a0a`.
- These are current sequences downloaded for the cohort on 2026-09-08. Identity with the original prediction-time input has not been established. Evaluate the supplied sequence explicitly; document any different sequence used.

```fasta
>A0A3Q2KRK8 Equus caballus WDPCP
MSFCLTELHLWSLKNTLHIGDRDIGVYQYYDKKDPPVTDHGNLEEKQKLAESRDYPWTLK
NRRPEKLRDSLKELEELMQNSQCVLSKWNNKYVCQLLFGSGVLVSLSLSGPQLEKVVIDR
SLVGKLISDTISDALLTDSFIILSFFAQNKLCFIQFTKKMGSPDVNKRLEKLSALDYKIS
YYEIPGPVNRTTERRLAINCVQDIVVCWWPLVSDDAWPWAPISSEKNRANLLLLGYAQGR
LEVLSSVRTEWDPLDVRFGTKQPYQVLTVERSISVDKEPMADSCIYEYVRNKIHCVSVTR
IPLRSKAISCCRNVTEDKLILGCEDSSLILYETHRRVTLLAQAELLPSLICCHPTGSILL
VGSNQGELQIFDMALSPINIQLLAEDRSPRETLQFNKFFDVSSGLVQMQWIAPQVVSQKP
DSGDIYDLLFLRFDRGPLGVLLFKLGIFTRGQLGLVDIIFQYIHCDEICEAINILSSMNW
DTLGHQCFISMSAIVNHLLRQKLTPEREAQLEASLGTFYAPTRPLLDSTVLEYRDQISKY
ARRFFHHLLRYQRFEKAFLLAVDIGARDLFMDIHYLALDKGELALAEVARKKASDIDAES
ITSGVELLGPLHRGDTLNEAFVGLSLAPQREDTFPDNLPHFCSVHRHIIQQRTLNVSSNG
QVFNRRNKLEKDTCAGSLMPKTCNEEDQSFDVASYWKHQQWTMYA
```

## Evidence and deliverable

Use primary literature and public sequence, structural and genomic resources. Select analyses that answer the decisive question; this is not a general gene review. Assess support and contrary evidence, and allow an unresolved outcome. Distinguish directly observed horse evidence, justified mammalian transfer, and results for a different protein model.

Do not consult the ai-gene-review repository's existing judgments, research syntheses or local bioinformatics analyses. Those are held out for comparison. Do not use agreement with ARBA or another prediction as biological validation. Preserve reproducible methods, accessions/versions, actual computation outputs and primary-source URLs/DOIs/PMIDs. Report the decisive findings and limitations, not just a verdict.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: The horse protein A0A3Q2KRK8 participates in cell projection organization.
focus_type: function_assignment
term_id: GO:0030030
term_label: cell projection organization
context:
- |
  # Focused function hypothesis

  Hypothesis: The horse protein A0A3Q2KRK8 participates in cell projection organization.

  Target: Equus caballus (NCBITaxon:9796), UniProt A0A3Q2KRK8. Gene label: WDPCP; verify identity independently rather than treating the label as proof.

  Target GO claim: GO:0030030 — cell projection organization. Verify its definition and scope.

  ## Decisive question

  Evaluate the molecular scaffold and experimental basis for the broad cell-projection-organization process. Compare relevant mammalian structures and isoforms, and distinguish alterations affecting a specific biochemical property from those that undermine the whole process.

  ## Identity and sequence inputs

  - Target record: https://www.uniprot.org/uniprotkb/A0A3Q2KRK8/entry
  - Human comparison lead: https://www.uniprot.org/uniprotkb/O95876/entry (WDPCP). Establish the relevant orthology/isoform relationship rather than assuming it.
  - Frozen current UniProt sequence: 705 residues; SHA-256 `a132072d392ff9ec8d0962a571a5ae3534476ecfc0679bdeb9051777f3aa5a0a`.
  - These are current sequences downloaded for the cohort on 2026-09-08. Identity with the original prediction-time input has not been established. Evaluate the supplied sequence explicitly; document any different sequence used.

  ```fasta
  >A0A3Q2KRK8 Equus caballus WDPCP
  MSFCLTELHLWSLKNTLHIGDRDIGVYQYYDKKDPPVTDHGNLEEKQKLAESRDYPWTLK
  NRRPEKLRDSLKELEELMQNSQCVLSKWNNKYVCQLLFGSGVLVSLSLSGPQLEKVVIDR
  SLVGKLISDTISDALLTDSFIILSFFAQNKLCFIQFTKKMGSPDVNKRLEKLSALDYKIS
  YYEIPGPVNRTTERRLAINCVQDIVVCWWPLVSDDAWPWAPISSEKNRANLLLLGYAQGR
  LEVLSSVRTEWDPLDVRFGTKQPYQVLTVERSISVDKEPMADSCIYEYVRNKIHCVSVTR
  IPLRSKAISCCRNVTEDKLILGCEDSSLILYETHRRVTLLAQAELLPSLICCHPTGSILL
  VGSNQGELQIFDMALSPINIQLLAEDRSPRETLQFNKFFDVSSGLVQMQWIAPQVVSQKP
  DSGDIYDLLFLRFDRGPLGVLLFKLGIFTRGQLGLVDIIFQYIHCDEICEAINILSSMNW
  DTLGHQCFISMSAIVNHLLRQKLTPEREAQLEASLGTFYAPTRPLLDSTVLEYRDQISKY
  ARRFFHHLLRYQRFEKAFLLAVDIGARDLFMDIHYLALDKGELALAEVARKKASDIDAES
  ITSGVELLGPLHRGDTLNEAFVGLSLAPQREDTFPDNLPHFCSVHRHIIQQRTLNVSSNG
  QVFNRRNKLEKDTCAGSLMPKTCNEEDQSFDVASYWKHQQWTMYA
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

**Target:** *Equus caballus* WDPCP, UniProt **A0A3Q2KRK8** (705 aa)
**Hypothesis (function assignment):** The horse protein A0A3Q2KRK8 participates in **cell projection organization (GO:0030030)**
**Focus type:** function_assignment
**Date:** 2026-09-08
**Sources:** Primary literature (PMIDs) + public sequence/domain/structure resources (UniProt, InterPro, QuickGO). No ai-gene-review repository judgments, syntheses, or local bioinformatics analyses were consulted.

---

## Summary

The hypothesis that horse A0A3Q2KRK8 participates in cell projection organization (GO:0030030) is **SUPPORTED**, with two curation caveats: the term is generic (more specific child terms are better supported), and all functional evidence is transferred by orthology rather than observed directly in horse. Three independent lines of evidence converge on this conclusion. First, identity is secure: the supplied 705-aa sequence is byte-identical to the current UniProt A0A3Q2KRK8 record (matching the provided SHA-256), and global alignment to human WDPCP (O95876) yields 83.3% identity with the diagnostic Frtz + WD40-repeat domain architecture — this is a genuine one-to-one WDPCP (Fritz) ortholog, not a mislabeled paralog. Second, the molecular biology of WDPCP is exceptionally well characterized in mammals: it is a core scaffolding and lipid-binding subunit of the CPLANE complex required for primary cilium assembly and actin-based planar cell polarity, both of which are, by GO definition, forms of cell projection organization. Third, the horse truncation relative to human is terminal-only and preserves the functional scaffold and the process-critical apical-docking residues N512/W513.

Mechanistically, WDPCP is a WD40/Frtz β-propeller scaffold within the crescent-shaped CPLANE complex (INTU–FUZ–WDPCP–JBTS17–RSG1) that binds phosphatidylinositol-3-phosphate and recruits partners including Septin 2. Its direct activity — scaffolding, lipid binding, and partner recruitment — drives two cellular readouts: assembly of the primary cilium (via basal-body apical docking and transition-zone function, feeding Hedgehog signaling) and organization of actin-based projections (planar cell polarity, directional migration). Loss- and point-mutation studies in mouse collapse both branches and produce Bardet–Biedl / Meckel–Gruber-like ciliopathy phenotypes. Because the horse ortholog shares the full domain architecture and the exact process-critical residues, the same mechanistic model is expected to hold.

For curation, GO:0030030 is correct but coarse. The evidence more precisely supports specific children (cilium assembly GO:0060271; establishment of planar polarity) plus candidate cellular-component (ciliary transition zone/basal body, actin cytoskeleton) and molecular-function (PI3P binding / structural scaffold) leads. Because there is no direct equine assay and the horse record is unreviewed TrEMBL, an **ISS/ISO** (orthology-transfer) evidence code is appropriate — not an experimental code, which belongs to the mouse and human records.

---

## Key Findings

### Finding 1 — A0A3Q2KRK8 is a genuine WDPCP (Fritz) ortholog, not a mislabeled paralog

The first gate for any function-assignment hypothesis is identity, and treating the "WDPCP" gene label as proof would be circular. Identity was therefore verified independently at the sequence and domain level. The supplied 705-aa FASTA was confirmed byte-identical to the current UniProt A0A3Q2KRK8 sequence (equality verified in code) and matches the provided SHA-256 `a132072d392ff9ec8d0962a571a5ae3534476ecfc0679bdeb9051777f3aa5a0a`, establishing that the analyzed sequence is exactly the frozen cohort sequence.

A global Needleman–Wunsch alignment of the horse protein against human WDPCP (O95876, 746 aa) gives **624 identical positions over a 749-position alignment = 83.3% identity** (88.5% over the horse length). Full-length identity at this level is diagnostic of a true one-to-one ortholog rather than a distant paralog. Consistent with this, UniProt annotates gene = **WDPCP**, InterPro **IPR024511 (Frtz domain)** plus **IPR036322 (WD40 repeat domain superfamily)**, Pfam **PF11768 (Frtz)**, and PANTHER **PTHR13667:SF5** ("WD repeat-containing and planar cell polarity effector protein Fritz homolog"). Keyword annotations include *Cell projection*, *Cilium*, *Cilium biogenesis/degradation*, and *Cytoskeleton* — the same functional vocabulary carried by the mammalian orthologs.

This finding removes the most common failure mode for function-assignment hypotheses — paralog overannotation — and licenses careful transfer of mammalian WDPCP biology to the horse protein. The one methodological caveat is that the alignment used simple identity-based (±1) Needleman–Wunsch scoring as an estimate, not a Smith–Waterman/BLAST E-value; the 83% figure is a robust identity estimate rather than a formal statistic.

### Finding 2 — WDPCP participates in cell projection organization via CPLANE-dependent ciliogenesis and actin-based polarity

WDPCP's function is unusually well characterized in mammals, and the evidence maps directly onto GO:0030030.

**Loss-of-function, actin and cilia (mouse).** [PMID: 24302887](https://pubmed.ncbi.nlm.nih.gov/24302887/) (Cui et al., 2013) showed that Wdpcp-deficient mice develop a Bardet–Biedl / Meckel–Gruber-like ciliopathy. Wdpcp localizes to the ciliary transition zone and to actin filaments/focal adhesions, interacts with Septin 2 (Sept2), and its loss both disorganizes actin filaments and abolishes cilia. The verified snippets — *"Wdpcp, a PCP effector, was recently shown to regulate both ciliogenesis and collective cell movement"* and *"organization of the actin filaments and focal contacts were markedly changed in Wdpcp-deficient cells"* — directly connect WDPCP to the organization of two distinct cell-projection systems.

**Structural scaffold, cryo-EM (human/mouse).** [PMID: 35427153](https://pubmed.ncbi.nlm.nih.gov/35427153/) resolved the near-atomic structure of the human and mouse WDPCP–Inturned–Fuzzy (CPLANE) complex. WDPCP is a structural scaffold within a crescent-shaped complex that binds phospholipids, and a ciliopathy mutation perturbs lipid binding. The verified snippet — *"the crescent-shaped CPLANE complex binds phospholipids such as phosphatidylinositol 3-phosphate via multiple modules"* — defines WDPCP's direct molecular role as a scaffolding/lipid-binding subunit.

**Point mutation, whole-process resolution (mouse).** [PMID: 41268724](https://pubmed.ncbi.nlm.nih.gov/41268724/) (2025) generated a Wdpcp point mutant (deletion of D481/W482, equivalent to human N512/W513). The protein is still made but fails apical basal-body docking, and *"Cilia formation and Hh signaling were severely impaired"* with neural-tube/craniofacial/polydactyly defects. This is the key discriminator required by the decisive question: it ties a specific structural element to failure of the whole ciliogenesis process, rather than a mere biochemical tweak.

**Pathway context.** [PMID: 38546045](https://pubmed.ncbi.nlm.nih.gov/38546045/) shows the CPLANE partner Fuzzy recruits ARHGAP35 (p190A RhoGAP) to the basal body to restrain actin polymerization for ciliogenesis; [PMID: 35740972](https://pubmed.ncbi.nlm.nih.gov/35740972/) (review) and [PMID: 31562761](https://pubmed.ncbi.nlm.nih.gov/31562761/) place WDPCP as a core CPLANE effector with a Longin-domain/Rab-GEF-adjacent architecture. Human genetics ([PMID: 32055034](https://pubmed.ncbi.nlm.nih.gov/32055034/); [PMID: 37239474](https://pubmed.ncbi.nlm.nih.gov/37239474/)) supports WDPCP as a Bardet–Biedl/ciliopathy gene.

Because both cilia and lamellipodia/actin-based projections are GO cell projections, this ensemble of assay, mutant-phenotype, localization, interaction, and structural evidence satisfies GO:0030030 at the process level. WDPCP's direct molecular role is a CPLANE scaffold/lipid-binding subunit; its cellular consequence is organization of cilia and actin-based projections.

### Finding 3 — The horse truncation is terminal-only; the process-critical apical-docking residues are conserved

Because the horse protein (705 aa) is 41 residues shorter than human WDPCP (746 aa), the deletion location determines whether orthology transfer is valid. Global alignment with traceback (match +2 / mismatch −1 / gap −2) gives **623/748 identical (83.3%)**. The 43 human residues absent from the horse alignment map almost entirely to the **extreme N-terminus (human residues ~1–33)** plus a handful of scattered residues at the **far C-terminus (~718–731)**. The internal body — where the Frtz and WD40 scaffold modules reside — is contiguous and highly conserved.

Decisively, the residues human **N512/W513** are perfectly conserved in horse: the aligned window "NILSSMNWDTLGH" is identical in both species. The two-codon deletion of the mouse equivalents (D481/W482) abolishes ciliary apical docking, ciliogenesis, and Hedgehog signaling ([PMID: 41268724](https://pubmed.ncbi.nlm.nih.gov/41268724/)), and the human W513S substitution is a Bardet–Biedl allele. Thus the horse truncation does not remove the functional scaffold or the process-critical docking residues. The N-terminal shortening most plausibly reflects an incomplete/alternative gene model (start-boundary artifact) in the unreviewed TrEMBL prediction rather than genuine functional divergence — strengthening, not weakening, the orthology-transfer argument. This directly answers the decisive question: there is no evidence of a horse-specific alteration to a process-critical biochemical property.

### Finding 4 — GO:0030030 is a high-level BP ancestor of cilium assembly; WDPCP's demonstrated role sits within its subtree

The target term's scope was verified against the QuickGO (EBI) record. GO:0030030 has aspect = **biological_process** and definition: *"A process that is carried out at the cellular level which results in the assembly, arrangement of constituent parts, or disassembly of a prolongation or process extending from a cell, e.g. a flagellum or axon."* Its subtree descends via child GO:0120036 (plasma membrane bounded cell projection organization) → GO:0044782 (cilium organization) → GO:0060271 (cilium assembly). WDPCP's experimentally demonstrated processes (cilium assembly and establishment of planar polarity / actin-based projection organization) are therefore true descendants of GO:0030030. The term is correctly placed relative to WDPCP's biology, but it is a high-level ancestor — correct yet less informative than the specific children the evidence supports.

---

## Mechanistic Model / Interpretation

```
                 CPLANE complex (INTU–FUZ–WDPCP–JBTS17–RSG1)
                 crescent-shaped scaffold; binds PI3P (cryo-EM)
                              │
          ┌───────────────────┴───────────────────┐
          ▼                                        ▼
  Ciliogenesis branch                     Actin / PCP branch
  - WDPCP at transition zone              - WDPCP on actin filaments,
  - apical basal-body docking               focal adhesions
    (requires N512/W513)                  - interacts with Sept2
  - primary cilium assembly               - directional migration,
  - Hedgehog signaling output               planar cell polarity
          │                                        │
          └───────────────┬────────────────────────┘
                          ▼
        Cell projection organization (GO:0030030)  ← generic, correct
        ├─ cilium assembly (GO:0060271)            ← best-supported child
        └─ establishment of planar polarity         ← best-supported child
                          │
                          ▼  (loss of function)
        Ciliopathy: Bardet-Biedl / Meckel-Gruber, NTD, polydactyly
        (downstream disease outcomes — NOT the MF/BP call)
```

WDPCP acts as a **structural scaffold and PI3P-binding hub** within the CPLANE complex. Through this dual role it organizes two classes of cell projections: the primary cilium (via basal-body apical docking and transition-zone function required for ciliogenesis and downstream Hedgehog signaling) and actin-based projections (via association with actin filaments/focal adhesions and Septin 2, driving planar cell polarity and directional migration). Loss or targeted point mutation of WDPCP collapses both branches, producing ciliopathy phenotypes. The horse ortholog shares 83% identity, the full domain architecture, and the exact process-critical residues, so the same mechanistic model is expected to hold — the appropriate inference type being orthology transfer, not direct observation.

**Evidence-provenance comparison:**

| Evidence layer | Organism | Directness for horse | Strength |
|---|---|---|---|
| Sequence identity / domain architecture | Horse vs. human | **Direct (horse sequence)** | High |
| Conserved N512/W513 docking residues | Horse vs. mouse/human | **Direct (horse sequence)** | High |
| CPLANE scaffold / PI3P binding (cryo-EM) | Human/mouse | Transferred by orthology | High (for ortholog) |
| Ciliogenesis + actin loss-of-function | Mouse | Transferred by orthology | High (for ortholog) |
| Apical-docking point mutant | Mouse | Transferred by orthology | High (for ortholog) |
| Direct equine assay | Horse | **None available** | — |

---

## Evidence Base / Evidence Matrix

| # | Citation (PMID) | Evidence type | Stance | Claim tested | Key finding | Context | Confidence / limitations |
|---|---|---|---|---|---|---|---|
| 1 | This report (UniProt A0A3Q2KRK8; InterPro) | Sequence/evolutionary (computed) | Supports (identity) | Is A0A3Q2KRK8 really WDPCP? | 83.3% identity to human WDPCP O95876; Frtz + WD40 domains; PANTHER "Fritz homolog" | Horse vs. human | High for identity; simple ±1 NW scoring (estimate, not BLAST) |
| 1b | This report (computed alignment) | Sequence/evolutionary (computed) | Supports/qualifies | Does the 705-aa truncation drop process-critical residues? | 43-aa difference is N-terminal (human 1–33) + far C-terminal; N512/W513 and Frtz/WD40 core conserved | Horse vs. human | High; truncation = gene-model boundary, not functional loss |
| 2 | [24302887](https://pubmed.ncbi.nlm.nih.gov/24302887/) | Mutant phenotype + localization + interaction | Supports (core) | Does WDPCP organize cilia and actin projections? | Wdpcp-null mice: ciliopathy; WDPCP at transition zone + actin/focal adhesions; binds Sept2; loss disorganizes actin & abolishes cilia | Mouse | High; direct genetics + cell biology |
| 3 | [35427153](https://pubmed.ncbi.nlm.nih.gov/35427153/) | Structural (cryo-EM) | Supports/qualifies (MF) | WDPCP's direct molecular role | Structure of WDPCP–Inturned–Fuzzy CPLANE; crescent scaffold binding PI3P; ciliopathy mutant has aberrant lipid binding | Human/mouse | High; defines scaffolding/lipid-binding activity |
| 4 | [41268724](https://pubmed.ncbi.nlm.nih.gov/41268724/) | Mutant phenotype (point mutant) | Supports | Are specific residues essential for ciliogenesis? | D481/W482 (≈ human N512/W513) deletion: protein made but fails apical docking; cilia & Hh severely impaired | Mouse | High; residues conserved in horse |
| 5 | [38546045](https://pubmed.ncbi.nlm.nih.gov/38546045/) | Mutant phenotype + mechanism | Supports (complex context) | Do CPLANE proteins control cilia via actin? | Fuzzy recruits ARHGAP35 to basal body; restrains actin polymerization for ciliogenesis | Mouse | Medium-high; about partner FUZ |
| 6 | [31562761](https://pubmed.ncbi.nlm.nih.gov/31562761/) | Structural/evolutionary (bioinformatic) | Qualifies (MF) | Protein family / activity | CPLANE triplicated Longin domains; likely Rab-GEF module | Cross-species | Medium; predictive |
| 7 | [35740972](https://pubmed.ncbi.nlm.nih.gov/35740972/) | Review/database | Supports (orientation) | Is WDPCP a CPLANE/ciliogenesis gene? | WDPCP is a CPLANE subunit linked to ciliogenesis, PCP, Hh | Review | Orientation only |
| 8 | [32055034](https://pubmed.ncbi.nlm.nih.gov/32055034/) / [37239474](https://pubmed.ncbi.nlm.nih.gov/37239474/) | Human genetics | Supports | Is WDPCP a ciliopathy gene? | WDPCP variants in Bardet-Biedl/ciliopathy cohorts | Human patients | Medium; supports process relevance |
| 9 | [34518561](https://pubmed.ncbi.nlm.nih.gov/34518561/) | Genetic association | Qualifies | Broader neuronal role? | WDPCP missense (p=3.96e-10, tinnitus); axonal migration/structural reinforcement | Human | Lower relevance to core cilia claim |

---

## GO Curation Implications

**GO:0030030 scope confirmed** (QuickGO): aspect = biological_process; the term is a high-level ancestor of cilium assembly. WDPCP's demonstrated role sits squarely inside its subtree, so annotation to GO:0030030 is correct but coarse.

**Lead (curator to verify):** *cell projection organization (GO:0030030)* can be **retained as a correct-but-generic** BP annotation for horse WDPCP, but more informative and better-supported terms are candidates to add or prefer:

| GO term | Aspect | Recommended action | Basis | Evidence code |
|---|---|---|---|---|
| GO:0030030 cell projection organization | BP | Retain (or generalize-to-specific) | Correct but generic parent | ISS/ISO |
| GO:0060271 cilium assembly / GO:0044782 cilium organization | BP | **Add / prefer** | Ciliogenesis LOF + point mutant | ISS/ISO |
| GO:0001736 establishment of planar polarity | BP | Add (lead) | Actin/PCP + migration data | ISS/ISO |
| ciliary transition zone / basal body / actin cytoskeleton | CC | Add (lead) | Localization (PMID 24302887) | ISS/ISO |
| phosphatidylinositol-3-phosphate binding / CPLANE structural scaffold | MF | Add (lead) | Cryo-EM (PMID 35427153) | ISS/ISO |

The molecular-function call should reflect the demonstrated lipid-binding/structural-scaffold role rather than a bare "protein binding." Because there is no direct equine experiment, the horse annotation should carry an **ISS/ISO (orthology)** evidence code; experimental codes (IDA/IMP) belong to the mouse and human records.

---

## Mechanistic Scope

The immediate molecular function being tested is WDPCP's role as a **WD40/Frtz β-propeller scaffold and PI3P-binding subunit of the CPLANE complex** that recruits partners (Sept2; CPLANE subunits; and, via the complex, actin regulators). Its immediate activity is scaffolding, lipid binding, and protein recruitment. The immediate cellular readout is organization of cell projections — primary-cilium assembly and actin-based planar polarity.

Direct gene-product activity (should drive the MF/CC/BP call): CPLANE scaffolding; PI3P binding; localization to transition zone, basal body, and actin filaments/focal adhesions; interaction with Septin 2. Downstream consequences (should NOT be conflated with the molecular function): Hedgehog signaling output, neural-tube/craniofacial/polydactyly developmental defects, and Bardet–Biedl / Meckel–Gruber ciliopathy disease manifestations. These are loss-of-function outcomes that support, but are not equivalent to, the GO:0030030 process annotation. The seed hypothesis is pitched at the correct process level, and the evidence discriminates a whole-process requirement (the point mutant abolishes ciliogenesis) from a mere biochemical tweak.

---

## Conflicts and Alternatives

- **Paralog confusion:** Effectively ruled out. 83% full-length identity, the diagnostic Frtz+WD40 architecture, and the PANTHER Fritz-homolog subfamily assignment identify a true one-to-one WDPCP ortholog.
- **Specificity vs. breadth:** The main tension is granularity, not contradiction — GO:0030030 is arguably "too broad" relative to what is demonstrated (cilium assembly + PCP), but it is not wrong.
- **Isoform / truncation artifact — RESOLVED:** The 43-residue horse↔human difference maps to the extreme N-terminus (human ~1–33) and a few far-C-terminal residues; the internal body and the process-critical N512/W513 are conserved. Most parsimoniously a gene-model/start-boundary artifact of the unreviewed TrEMBL prediction, not functional loss.
- **Complex-level vs. WDPCP-specific mechanism:** Some actin/RhoGAP detail (PMID 38546045) is shown for the partner FUZ, not WDPCP directly; transfer within CPLANE is reasonable but is complex-level.
- **Broader roles:** The tinnitus GWAS association (PMID 34518561) invokes axonal migration and cytoskeletal reinforcement — consistent with, but broader than, the core ciliogenesis role; it does not conflict with GO:0030030.
- **Database carry-over risk:** The horse record is unreviewed TrEMBL; the support here rests on primary mammalian literature plus the horse's own sequence/domain evidence, not on agreement with any electronic prediction.

---

## Limitations and Knowledge Gaps

1. **No direct horse data.** Checked: PubMed for equine WDPCP functional studies — only orthology plus human/mouse assays exist. This means any horse annotation is inherently ISS/ISO. Resolve with equine cell/ciliogenesis assays or expression data.
2. **Horse isoform completeness — largely resolved.** Checked: 705 vs. 746 aa; alignment locates the difference at the N-terminus (human ~1–33) and far C-terminus, with N512/W513 and the Frtz/WD40 core conserved. Residual uncertainty is whether the missing N-terminal ~33 residues carry any regulatory role (not implicated in published ciliogenesis assays). Resolve by confirming the equine gene model / 5′ transcript.
3. **Alignment method.** The 83% identity used simple ±1 Needleman–Wunsch scoring, an identity estimate rather than a Smith–Waterman/BLAST E-value. The conclusion is robust but should be confirmed with a standard tool for the record.
4. **GO granularity policy.** Which specific child term(s) the curator prefers depends on project policy on generic vs. specific terms when support is orthology-transferred.

---

## Proposed Follow-up Experiments / Actions

1. **Reciprocal-best-hit orthology confirmation** across Equidae and additional mammals (Ensembl Compara / OrthoDB) to formally lock in one-to-one orthology beyond pairwise identity.
2. **Structural superposition** of an AlphaFold model of A0A3Q2KRK8 onto the cryo-EM CPLANE structure (PMID 35427153) to confirm the scaffold fold and PI3P-binding modules are preserved in horse (Phenix `phenix.superpose_pdbs` / `compare_structures`).
3. **Residue-level conservation mapping** of all reported human ciliopathy alleles (e.g., W513S) onto the horse sequence — extend the N512/W513 check to the complete variant set.
4. **Equine ciliated-cell assay** (tracheal epithelium or fibroblast): siRNA knockdown of WDPCP with cilia (acetylated-tubulin) and actin (phalloidin) readouts — the single most decisive test to convert ISS into IDA/IMP.
5. **Co-immunoprecipitation** of equine WDPCP with INTU/FUZ/Sept2 to confirm CPLANE complex membership in horse.
6. **Curator decision** on parent-vs-child GO annotation and on adding the MF (PI3P binding) and CC (transition zone / actin cytoskeleton) leads with ISS/ISO codes.

---

## Curation Leads (require curator verification)

- **Action:** Keep GO:0030030 as a valid (generic) BP annotation; consider promoting to the specific children (cilium assembly GO:0060271; establishment of planar polarity GO:0001736) and adding CC (ciliary transition zone/basal body, actin cytoskeleton) and MF (phosphatidylinositol-3-phosphate binding / structural scaffold) leads. Use an **ISS/ISO** evidence code.
- **Candidate references with snippets to verify:**
  - [PMID: 24302887](https://pubmed.ncbi.nlm.nih.gov/24302887/): *"Wdpcp… regulate both ciliogenesis and collective cell movement"*; *"organization of the actin filaments and focal contacts were markedly changed in Wdpcp-deficient cells."*
  - [PMID: 35427153](https://pubmed.ncbi.nlm.nih.gov/35427153/): *"the crescent-shaped CPLANE complex binds phospholipids such as phosphatidylinositol 3-phosphate via multiple modules."*
  - [PMID: 41268724](https://pubmed.ncbi.nlm.nih.gov/41268724/): *"Cilia formation and Hh signaling were severely impaired."*
- **Suggested question to curator:** Does project policy prefer the specific cilium/PCP terms over the generic GO:0030030 when experimental support is orthology-transferred, and should MF/CC annotations beyond the single BP hypothesis be added?
- **Suggested experiment:** Equine ciliated-cell WDPCP knockdown with cilia/actin readouts (converts ISS → direct evidence).

---

## Conclusion

The seed hypothesis is **SUPPORTED**. Horse A0A3Q2KRK8 is a genuine WDPCP ortholog (83% identity to human WDPCP O95876, full Frtz+WD40 architecture, conserved process-critical residues N512/W513), and WDPCP is an experimentally established CPLANE-complex scaffold required for ciliogenesis and actin-based planar polarity in mouse and human — both forms of cell projection organization. GO:0030030 is therefore biologically justified for the horse protein. The two curation caveats are that the term is generic (specific children such as cilium assembly and establishment of planar polarity are better supported) and that all functional evidence is transferred by orthology to an unreviewed TrEMBL record, so an **ISS/ISO** evidence code is appropriate rather than an experimental one.


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)