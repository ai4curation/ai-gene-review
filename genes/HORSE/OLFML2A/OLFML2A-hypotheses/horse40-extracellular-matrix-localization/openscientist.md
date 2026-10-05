---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-08T15:57:03.797878'
end_time: '2026-09-08T16:12:22.029227'
duration_seconds: 918.23
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: HORSE
  gene: OLFML2A
  gene_symbol: OLFML2A
  uniprot_accession: A0A9L0SKW1
  taxon_id: NCBITaxon:9796
  taxon_label: Equus caballus
  focus_type: function_assignment
  hypothesis_slug: horse40-extracellular-matrix-localization
  hypothesis_text: The horse protein A0A9L0SKW1 localizes to the extracellular matrix.
  term_context: "- Term: extracellular matrix (GO:0031012)\n- # Focused function hypothesis\n\
    \nHypothesis: The horse protein A0A9L0SKW1 localizes to the extracellular matrix.\n\
    \nTarget: Equus caballus (NCBITaxon:9796), UniProt A0A9L0SKW1. Gene label: OLFML2A;\
    \ verify identity independently rather than treating the label as proof.\n\nTarget\
    \ GO claim: GO:0031012 \u2014 extracellular matrix. Verify its definition and\
    \ scope.\n\n## Decisive question\n\nDetermine whether the exact sequence and credible\
    \ transcript model support entry into the secretory pathway and extracellular-matrix\
    \ residence. Distinguish secretion from matrix association, and distinguish the\
    \ supplied protein from alternative products of the locus.\n\n## Identity and\
    \ sequence inputs\n\n- Target record: https://www.uniprot.org/uniprotkb/A0A9L0SKW1/entry\n\
    - Human comparison lead: https://www.uniprot.org/uniprotkb/Q68BL7/entry (OLFML2A).\
    \ Establish the relevant orthology/isoform relationship rather than assuming it.\n\
    - Frozen current UniProt sequence: 599 residues; SHA-256 `069f390f83475c7f4749a7dff36c9d553c6334ea6dc0d2004ab814d07ef297ab`.\n\
    - These are current sequences downloaded for the cohort on 2026-09-08. Identity\
    \ with the original prediction-time input has not been established. Evaluate the\
    \ supplied sequence explicitly; document any different sequence used.\n\n```fasta\n\
    >A0A9L0SKW1 Equus caballus OLFML2A\nMDSQVFGDMDQVRMTSEGSDCRCKCIMRPLSKDACSRVRSGRARVEDFYTVETVSSGTDC\n\
    RCSCTAPPSSLNPCENEWKMEKLKKQAPELLKLQSMVASQMNTLEESIKANLSRENEVVR\nESMRHFSEQLKHYENHSAIMMSIKKELSSLGLQLLQKDAATAPAAGPATGPGSKAQDTAG\n\
    GKGKDTNKYGSMQKSFVDRGLPKAPKEKLLKVEKLRKEGSKSRFPQPTGKPRALAQQQAV\nVRGITYYKAGRKEATEAVADNALKGTSWLEQLPPRVEGRPSEPNSAEHDEARPRTSEGVD\n\
    LAPGTPASDPTPTPTPTTTTSPMSTEPPSRPEVPSQGREASCEGTLRAVDPPVRHHSYGR\nHEGAWMKDPAARDDRIYVTNYYYGNSLVEFRNLENFKQGRWSNMYKLPYNWIGTGHVVYQ\n\
    GAFYYNRAFTKNIIKYDLRQRFVASWALLPDVVYEDTTPWKWRGHSDIDFAVDESGLWVI\nYPAVDDRDEAQPEVIVLSRLDPGDLSVHRETTWKTRLRRNSYGNCFLVCGILYAVDTYNQ\n\
    REGQVAYAFDTHTGTDARPQLPFLNEHAYTTQIDYNPKERVLYAWDNGHQLTYTLHFVV\n```\n\n## Evidence\
    \ and deliverable\n\nUse primary literature and public sequence, structural and\
    \ genomic resources. Select analyses that answer the decisive question; this is\
    \ not a general gene review. Assess support and contrary evidence, and allow an\
    \ unresolved outcome. Distinguish directly observed horse evidence, justified\
    \ mammalian transfer, and results for a different protein model.\n\nDo not consult\
    \ the ai-gene-review repository's existing judgments, research syntheses or local\
    \ bioinformatics analyses. Those are held out for comparison. Do not use agreement\
    \ with ARBA or another prediction as biological validation. Preserve reproducible\
    \ methods, accessions/versions, actual computation outputs and primary-source\
    \ URLs/DOIs/PMIDs. Report the decisive findings and limitations, not just a verdict."
  reference_context: No specific reference context supplied.
  source_file: genes/HORSE/OLFML2A/OLFML2A-ai-review.yaml
  source_selector: free-text
  source_context_yaml: "hypothesis: The horse protein A0A9L0SKW1 localizes to the\
    \ extracellular matrix.\nfocus_type: function_assignment\nterm_id: GO:0031012\n\
    term_label: extracellular matrix\ncontext:\n- |\n  # Focused function hypothesis\n\
    \n  Hypothesis: The horse protein A0A9L0SKW1 localizes to the extracellular matrix.\n\
    \n  Target: Equus caballus (NCBITaxon:9796), UniProt A0A9L0SKW1. Gene label: OLFML2A;\
    \ verify identity independently rather than treating the label as proof.\n\n \
    \ Target GO claim: GO:0031012 \u2014 extracellular matrix. Verify its definition\
    \ and scope.\n\n  ## Decisive question\n\n  Determine whether the exact sequence\
    \ and credible transcript model support entry into the secretory pathway and extracellular-matrix\
    \ residence. Distinguish secretion from matrix association, and distinguish the\
    \ supplied protein from alternative products of the locus.\n\n  ## Identity and\
    \ sequence inputs\n\n  - Target record: https://www.uniprot.org/uniprotkb/A0A9L0SKW1/entry\n\
    \  - Human comparison lead: https://www.uniprot.org/uniprotkb/Q68BL7/entry (OLFML2A).\
    \ Establish the relevant orthology/isoform relationship rather than assuming it.\n\
    \  - Frozen current UniProt sequence: 599 residues; SHA-256 `069f390f83475c7f4749a7dff36c9d553c6334ea6dc0d2004ab814d07ef297ab`.\n\
    \  - These are current sequences downloaded for the cohort on 2026-09-08. Identity\
    \ with the original prediction-time input has not been established. Evaluate the\
    \ supplied sequence explicitly; document any different sequence used.\n\n  ```fasta\n\
    \  >A0A9L0SKW1 Equus caballus OLFML2A\n  MDSQVFGDMDQVRMTSEGSDCRCKCIMRPLSKDACSRVRSGRARVEDFYTVETVSSGTDC\n\
    \  RCSCTAPPSSLNPCENEWKMEKLKKQAPELLKLQSMVASQMNTLEESIKANLSRENEVVR\n  ESMRHFSEQLKHYENHSAIMMSIKKELSSLGLQLLQKDAATAPAAGPATGPGSKAQDTAG\n\
    \  GKGKDTNKYGSMQKSFVDRGLPKAPKEKLLKVEKLRKEGSKSRFPQPTGKPRALAQQQAV\n  VRGITYYKAGRKEATEAVADNALKGTSWLEQLPPRVEGRPSEPNSAEHDEARPRTSEGVD\n\
    \  LAPGTPASDPTPTPTPTTTTSPMSTEPPSRPEVPSQGREASCEGTLRAVDPPVRHHSYGR\n  HEGAWMKDPAARDDRIYVTNYYYGNSLVEFRNLENFKQGRWSNMYKLPYNWIGTGHVVYQ\n\
    \  GAFYYNRAFTKNIIKYDLRQRFVASWALLPDVVYEDTTPWKWRGHSDIDFAVDESGLWVI\n  YPAVDDRDEAQPEVIVLSRLDPGDLSVHRETTWKTRLRRNSYGNCFLVCGILYAVDTYNQ\n\
    \  REGQVAYAFDTHTGTDARPQLPFLNEHAYTTQIDYNPKERVLYAWDNGHQLTYTLHFVV\n  ```\n\n  ##\
    \ Evidence and deliverable\n\n  Use primary literature and public sequence, structural\
    \ and genomic resources. Select analyses that answer the decisive question; this\
    \ is not a general gene review. Assess support and contrary evidence, and allow\
    \ an unresolved outcome. Distinguish directly observed horse evidence, justified\
    \ mammalian transfer, and results for a different protein model.\n\n  Do not consult\
    \ the ai-gene-review repository's existing judgments, research syntheses or local\
    \ bioinformatics analyses. Those are held out for comparison. Do not use agreement\
    \ with ARBA or another prediction as biological validation. Preserve reproducible\
    \ methods, accessions/versions, actual computation outputs and primary-source\
    \ URLs/DOIs/PMIDs. Report the decisive findings and limitations, not just a verdict.\n\
    reference_id: []"
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
- **Gene directory:** OLFML2A
- **Gene symbol:** OLFML2A
- **UniProt accession:** A0A9L0SKW1

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** horse40-extracellular-matrix-localization
- **Source file:** genes/HORSE/OLFML2A/OLFML2A-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

The horse protein A0A9L0SKW1 localizes to the extracellular matrix.

## Term and Decision Context

- Term: extracellular matrix (GO:0031012)
- # Focused function hypothesis

Hypothesis: The horse protein A0A9L0SKW1 localizes to the extracellular matrix.

Target: Equus caballus (NCBITaxon:9796), UniProt A0A9L0SKW1. Gene label: OLFML2A; verify identity independently rather than treating the label as proof.

Target GO claim: GO:0031012 — extracellular matrix. Verify its definition and scope.

## Decisive question

Determine whether the exact sequence and credible transcript model support entry into the secretory pathway and extracellular-matrix residence. Distinguish secretion from matrix association, and distinguish the supplied protein from alternative products of the locus.

## Identity and sequence inputs

- Target record: https://www.uniprot.org/uniprotkb/A0A9L0SKW1/entry
- Human comparison lead: https://www.uniprot.org/uniprotkb/Q68BL7/entry (OLFML2A). Establish the relevant orthology/isoform relationship rather than assuming it.
- Frozen current UniProt sequence: 599 residues; SHA-256 `069f390f83475c7f4749a7dff36c9d553c6334ea6dc0d2004ab814d07ef297ab`.
- These are current sequences downloaded for the cohort on 2026-09-08. Identity with the original prediction-time input has not been established. Evaluate the supplied sequence explicitly; document any different sequence used.

```fasta
>A0A9L0SKW1 Equus caballus OLFML2A
MDSQVFGDMDQVRMTSEGSDCRCKCIMRPLSKDACSRVRSGRARVEDFYTVETVSSGTDC
RCSCTAPPSSLNPCENEWKMEKLKKQAPELLKLQSMVASQMNTLEESIKANLSRENEVVR
ESMRHFSEQLKHYENHSAIMMSIKKELSSLGLQLLQKDAATAPAAGPATGPGSKAQDTAG
GKGKDTNKYGSMQKSFVDRGLPKAPKEKLLKVEKLRKEGSKSRFPQPTGKPRALAQQQAV
VRGITYYKAGRKEATEAVADNALKGTSWLEQLPPRVEGRPSEPNSAEHDEARPRTSEGVD
LAPGTPASDPTPTPTPTTTTSPMSTEPPSRPEVPSQGREASCEGTLRAVDPPVRHHSYGR
HEGAWMKDPAARDDRIYVTNYYYGNSLVEFRNLENFKQGRWSNMYKLPYNWIGTGHVVYQ
GAFYYNRAFTKNIIKYDLRQRFVASWALLPDVVYEDTTPWKWRGHSDIDFAVDESGLWVI
YPAVDDRDEAQPEVIVLSRLDPGDLSVHRETTWKTRLRRNSYGNCFLVCGILYAVDTYNQ
REGQVAYAFDTHTGTDARPQLPFLNEHAYTTQIDYNPKERVLYAWDNGHQLTYTLHFVV
```

## Evidence and deliverable

Use primary literature and public sequence, structural and genomic resources. Select analyses that answer the decisive question; this is not a general gene review. Assess support and contrary evidence, and allow an unresolved outcome. Distinguish directly observed horse evidence, justified mammalian transfer, and results for a different protein model.

Do not consult the ai-gene-review repository's existing judgments, research syntheses or local bioinformatics analyses. Those are held out for comparison. Do not use agreement with ARBA or another prediction as biological validation. Preserve reproducible methods, accessions/versions, actual computation outputs and primary-source URLs/DOIs/PMIDs. Report the decisive findings and limitations, not just a verdict.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: The horse protein A0A9L0SKW1 localizes to the extracellular matrix.
focus_type: function_assignment
term_id: GO:0031012
term_label: extracellular matrix
context:
- |
  # Focused function hypothesis

  Hypothesis: The horse protein A0A9L0SKW1 localizes to the extracellular matrix.

  Target: Equus caballus (NCBITaxon:9796), UniProt A0A9L0SKW1. Gene label: OLFML2A; verify identity independently rather than treating the label as proof.

  Target GO claim: GO:0031012 — extracellular matrix. Verify its definition and scope.

  ## Decisive question

  Determine whether the exact sequence and credible transcript model support entry into the secretory pathway and extracellular-matrix residence. Distinguish secretion from matrix association, and distinguish the supplied protein from alternative products of the locus.

  ## Identity and sequence inputs

  - Target record: https://www.uniprot.org/uniprotkb/A0A9L0SKW1/entry
  - Human comparison lead: https://www.uniprot.org/uniprotkb/Q68BL7/entry (OLFML2A). Establish the relevant orthology/isoform relationship rather than assuming it.
  - Frozen current UniProt sequence: 599 residues; SHA-256 `069f390f83475c7f4749a7dff36c9d553c6334ea6dc0d2004ab814d07ef297ab`.
  - These are current sequences downloaded for the cohort on 2026-09-08. Identity with the original prediction-time input has not been established. Evaluate the supplied sequence explicitly; document any different sequence used.

  ```fasta
  >A0A9L0SKW1 Equus caballus OLFML2A
  MDSQVFGDMDQVRMTSEGSDCRCKCIMRPLSKDACSRVRSGRARVEDFYTVETVSSGTDC
  RCSCTAPPSSLNPCENEWKMEKLKKQAPELLKLQSMVASQMNTLEESIKANLSRENEVVR
  ESMRHFSEQLKHYENHSAIMMSIKKELSSLGLQLLQKDAATAPAAGPATGPGSKAQDTAG
  GKGKDTNKYGSMQKSFVDRGLPKAPKEKLLKVEKLRKEGSKSRFPQPTGKPRALAQQQAV
  VRGITYYKAGRKEATEAVADNALKGTSWLEQLPPRVEGRPSEPNSAEHDEARPRTSEGVD
  LAPGTPASDPTPTPTPTTTTSPMSTEPPSRPEVPSQGREASCEGTLRAVDPPVRHHSYGR
  HEGAWMKDPAARDDRIYVTNYYYGNSLVEFRNLENFKQGRWSNMYKLPYNWIGTGHVVYQ
  GAFYYNRAFTKNIIKYDLRQRFVASWALLPDVVYEDTTPWKWRGHSDIDFAVDESGLWVI
  YPAVDDRDEAQPEVIVLSRLDPGDLSVHRETTWKTRLRRNSYGNCFLVCGILYAVDTYNQ
  REGQVAYAFDTHTGTDARPQLPFLNEHAYTTQIDYNPKERVLYAWDNGHQLTYTLHFVV
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

# Focused Hypothesis Report — Horse OLFML2A (A0A9L0SKW1) localizes to the extracellular matrix (GO:0031012)

**Focus type:** function_assignment (CC localization) · **Term:** GO:0031012 extracellular matrix
**Target:** *Equus caballus* (NCBITaxon:9796), UniProt **A0A9L0SKW1**, 599 aa, PE=4 (Predicted), Ensembl gene model ENSECAG00000023908 / protein ENSECAP00000076704.
**Human comparison lead:** Q68BL7 (OLFML2A / Photomedin-1), 652 aa, PE=1.

---

## Executive Judgment

**Partially supported (support via justified mammalian orthology transfer; one important sequence caveat).**

- **Identity confirmed.** The supplied 599-aa sequence is byte-identical to the current UniProt A0A9L0SKW1 record and is an unambiguous **OLFML2A/photomedin-1 ortholog**: 87.2% identical to human OLFML2A over the mature chain, retaining the diagnostic domain architecture (N-terminal tandem CXCXCX9C cysteine motifs, mid-molecule coiled-coil, C-terminal olfactomedin domain).
- **The ortholog is genuinely an ECM protein.** Direct experimental work on the mouse ortholog (photomedin-1) shows it is **secreted, disulfide-bonded, O-glycosylated, and binds the ECM glycosaminoglycans chondroitin sulfate-E and heparin** (PMID 15836428). Human OLFML2A is PE1 with UniProt CC "Secreted." This justifies ECM localization by mammalian transfer.
- **Decisive caveat on the exact sequence.** The supplied horse ORF **begins exactly at the mature-chain boundary and lacks the entire N-terminal signal peptide.** Horse residue 2 aligns to human residue 28 (the first mature residue, immediately after human SIGNAL 1..27), and the horse N-terminus has no hydrophobic h-region (max Kyte-Doolittle window-7 = 0.83 vs 3.09 in the human signal).
- **The locus DOES encode secretion-competent isoforms (isoform resolution).** Ensembl gene ENSECAG00000023908 has 6 protein-coding transcripts; the **canonical is 662 aa** (ENSECAP00000071146, N-term `MAPGTSGNLLLAVCPW…`, hydrophobic, KD max 2.61) and isoform ENSECAP00000056820 (618 aa) starts `MAAAALPPRP…`, matching the human OLFML2A signal peptide (KD max 3.03). NCBI RefSeq likewise lists full-length models (XP_023484611.2, 650 aa; XP_023484612.1, 621 aa). The supplied **A0A9L0SKW1 = ENSECAP00000076704 (599 aa) is a minor, non-canonical, N-terminally-truncated isoform** — so the missing signal peptide is an **isoform/gene-model choice, not loss of secretion by the gene.**
- **Functional ECM-binding domain is intact.** The C-terminal olfactomedin (OLF) domain in the supplied 599-aa model (residues 341–599) is **99.6% identical to the human OLF domain (258/259)** and ends at the natural C-terminus (`…HFVV`). The GAG/proteoglycan-binding module that mediates ECM association is therefore fully preserved; only the N-terminal signal peptide is missing.
- **Paralog confusion ruled out.** Smith-Waterman: horse vs human OLFML2A (Q68BL7) = 983 vs human OLFML2B/photomedin-2 (Q68BL8) = 294 — unambiguously OLFML2A.
- The horse UniProt "Secreted" tag is **ARBA rule-based (automated), not experimental**, and must not be treated as biological validation.

**Bottom line for the curator:** ECM/secreted localization for horse OLFML2A is well supported *by orthology to an experimentally characterized ECM protein*, but is **not directly observed in horse** and is **not encoded by the supplied truncated ORF**. GO:0031012 is defensible as an ISS/ISO annotation with the signal-peptide-truncation caveat noted; it should not be asserted as directly-observed horse evidence.

---

## Evidence Matrix

| # | Citation | Evidence type | Stance | Claim tested | Key finding | Context | Confidence / limitations |
|---|----------|---------------|--------|--------------|-------------|---------|--------------------------|
| 1 | This report (computed) | Structural/evolutionary (Smith-Waterman, own run) | Supports (identity) | Is A0A9L0SKW1 truly OLFML2A? | Horse 2–599 ↔ human 28–652, score 983, **87.2% identity**; retains OLF domain (UniProt 341–599) + N-terminal CxCxCx9C motifs + coiled-coil | Horse vs human protein sequence | High; identity/architecture unambiguous |
| 2 | This report (computed) | Computational (hydrophobicity + alignment) | **Qualifies / competing** | Does the exact sequence encode a signal peptide? | Horse res.2 = human res.28 (mature-chain start); **no signal peptide, no hydrophobic N-term** (KD max 0.83 vs human 3.09); UniProt lists no SIGNAL/TM | Exact 599-aa ORF | High for the ORF; interpreted as 5′-truncated gene model |
| 3 | PMID **15836428** (Furutani et al., 2005, *Biochem J*) | **Direct assay + localization** | Supports (ortholog) | Is OLFML2A/photomedin-1 an ECM protein? | Identified in an ECM-protein screen; **secreted disulfide-bonded dimer, O-glycosylated; binds chondroitin sulfate-E and heparin**; retinal photoreceptor outer segment | Mouse cDNA / recombinant protein; retina | High for ortholog; species = mouse, not horse |
| 4 | UniProt Q68BL7 (human) | Review/database | Supports (ortholog) | Human OLFML2A localization/features | PE1; SIGNAL 1..27, CHAIN 28..652, OLF 394..652, COILED 157..183; KW Signal/Glycoprotein/Disulfide/Secreted; CC "Secreted" | Human | High; "Secreted" is broader than ECM |
| 5 | UniProt A0A9L0SKW1 (horse) | Database (automated) | Qualifies | Does the record itself assert ECM? | CC "Secreted" is **ARBA automated**; no SIGNAL feature; no explicit GO:0031012; PE4 Predicted | Horse | Automated only — not evidence |
| 6 | Ensembl ENSECAG00000023908 + NCBI RefSeq (own queries) | Computational (isoform resolution) | **Qualifies (resolves caveat)** | Does the locus encode signal-peptide isoforms? | Canonical 662 aa (`MAPGTSGNLLLAVCPW`, KD 2.61) and isoform 618 aa (`MAAAALPPRP`= human signal peptide, KD 3.03) **have signal peptides**; supplied 599-aa model is a minor truncated isoform (KD 0.83) | Horse locus, chr25 | High; shows truncation is isoform-specific, not gene-level |
| 7 | UniProt Q68BL8 vs Q68BL7 (own SW) | Structural/evolutionary | Supports (identity) | Is it OLFML2A not the OLFML2B paralog? | SW horse↔OLFML2A=983 vs ↔OLFML2B=294 | Horse vs human | High; paralog confusion excluded |

*Provenance:* sequence identity check, Smith-Waterman alignment, N-terminal Kyte-Doolittle hydrophobicity scan, and glyc/cysteine mapping were executed in-session (code + numeric outputs retained in the iteration transcript). SHA-256 could not be recomputed in-sandbox (hashlib/struct blocked), but the provided sequence was verified byte-identical to the live UniProt A0A9L0SKW1 FASTA and length 599 matches the frozen spec.

---

## GO Curation Implications (leads — require curator verification)

- **GO:0031012 (extracellular matrix, CC):** Biologically **defensible for the ortholog** — photomedin-1 was identified as an ECM protein and binds ECM proteoglycan GAG chains (PMID 15836428). Recommend annotating by **ISO/ISS from mouse/human**, with evidence code reflecting orthology (not IDA), and a **NOT-fully-encoded-signal-peptide caveat** on the horse model.
- **Alternative/parent term consideration:** UniProt curators annotate the human protein only as "Secreted" (≈ GO:0005576 extracellular region). GO:0031012 is *more specific* than the minimal database claim; it is supported by the CS-E/heparin-binding assay but a conservative curator could prefer **GO:0005576 extracellular region** if requiring the more specific ECM residence to be demonstrated for a mammalian ortholog. Either is more informative than "protein binding."
- **Supportable companion terms (leads):** MF — glycosaminoglycan binding / heparin binding (GO:0005539 / GO:0008201) from PMID 15836428; CC — GO:0005576 extracellular region (parent, safest).
- **Do not** cite the horse record's ARBA "Secreted" as independent support; it is a prediction, not validation.

---

## Mechanistic Scope

Immediate molecular/cellular function being tested is **localization/residence**, not catalysis. The gene product is a **secreted olfactomedin-domain glycoprotein** whose extracellular-matrix association is a *direct binding property* (olfactomedin/coiled-coil scaffold binding chondroitin sulfate-E– and heparin-type GAGs on proteoglycans). ECM residence is thus a primary property of the mature protein, not a downstream phenotype. The N-terminal CXCXCX9C motifs mediate disulfide-linked dimerization; the signal peptide (present in orthologs) drives secretory-pathway entry.

## Conflicts and Alternatives

- **Isoform-specific truncation (principal conflict, now resolved):** the supplied ORF lacks the signal peptide, so a naïve SignalP/secretion check on the exact 599-aa sequence would be **negative**. Isoform resolution shows this is one **alternative product** of the locus: the canonical 662-aa protein and a 618-aa isoform (`MAAAALPPRP…` = human signal peptide) are secretion-competent, so the truncation is an isoform/gene-model choice, not loss of secretion by the gene.
- **Term-scope mismatch:** databases annotate the human protein as "Secreted" (extracellular region), which is broader than "extracellular matrix"; ECM specificity rests on the mouse binding assay.
- **Paralog note — resolved:** OLFML2B (photomedin-2) is a close paralog with the same architecture and ECM binding. SW scoring (horse↔OLFML2A 983 vs ↔OLFML2B 294) unambiguously assigns the horse locus to **OLFML2A**.
- **Species evidence gap:** no horse-specific localization data exist; all functional evidence is mouse/human.

## Knowledge Gaps

1. **Does the true horse transcript encode a signal peptide? — largely RESOLVED.** Checked Ensembl (6 transcripts) and NCBI RefSeq: canonical 662-aa and 618-aa (`MAAAALPPRP`) isoforms carry hydrophobic signal peptides; the supplied 599-aa model does not. Remaining gap: which isoform(s) predominate in horse tissue (RNA-seq/proteomics) and whether the 599-aa ORF is a real product or a mis-prediction/NMD substrate.
2. **Is ECM (vs generic extracellular) the right granularity for horse?** Checked: orthologs bind ECM GAGs (mouse). Resolve with horse tissue localization or GAG-binding assay.
3. **Locus disambiguation OLFML2A vs OLFML2B.** Resolve via synteny/phylogenetic tree of equine olfactomedin genes.

## Discriminating Tests

- **Signal-peptide resolution:** SignalP-6.0 / DeepTMHMM on (a) the supplied 599-aa ORF and (b) a reconstructed full-length horse ORF from genomic + 5′-UTR; compare.
- **Transcript completeness:** map equine RNA-seq (e.g., FAANG) to ENSECAG00000023908 to confirm the true start codon and signal-peptide exon.
- **Orthology tree:** ML phylogeny of OLFML2A/OLFML2B across mammals to lock identity.
- **Localization/binding (if wet-lab):** express horse OLFML2A, test secretion and CS-E/heparin binding as in PMID 15836428.

## Curation Leads (verify before applying)

- **Reference to add:** PMID **15836428** — snippets to verify: *"characterized by the presence of tandem CXCXCX9C motifs in the N-terminal region, a coiled-coil domain and an olfactomedin domain"*; *"secreted as disulphide-bonded dimers (photomedin-1) … with O-linked carbohydrate chains"*; *"photomedins preferentially bound to chondroitin sulphate-E and heparin."*
- **Candidate GO action:** retain **GO:0031012** as an **ISO/ISS (orthology) annotation** with a curator note that the horse Ensembl model is signal-peptide-truncated; optionally back off to **GO:0005576** if ECM specificity for a mammalian ortholog is deemed insufficiently transferable. Consider adding **GO:0008201/GO:0005539** (heparin/GAG binding, MF) as leads.
- **Suggested question:** Is the horse OLFML2A gene model 5′-complete? If not, flag the "Secreted"/ECM annotation as inference pending a corrected model.
- **Do NOT** rely on the horse record's ARBA "Secreted" or agreement with predictions as validation.

---

## Provenance Tables (computed this run)

**Signal-peptide analysis across horse OLFML2A isoforms** (Ensembl `ENSECAG00000023908`; Kyte-Doolittle window-7):

| Ensembl protein | length (aa) | status | N-terminus | KD max | KD windows >1.6 | interpretation |
|---|---|---|---|---|---|---|
| ENSECAP00000071146 | 662 | canonical | MAPGTSGNLLLAVCPW | 2.61 | 4 | signal-peptide-like (secretion-competent) |
| ENSECAP00000056820 | 618 | non-canonical | MAAAALPPRPRPRP | 3.03 | 9 | = human signal peptide (secretion-competent) |
| ENSECAP00000036732 | 621 | non-canonical | MDSQVFGDMDQVRM | 0.83 | 0 | NO signal peptide (truncated) |
| **ENSECAP00000076704** | **599** | **TARGET = A0A9L0SKW1** | **MDSQVFGDMDQVRM** | **0.83** | **0** | **NO signal peptide (truncated)** |

**Paralog disambiguation** (Smith-Waterman, match +2/mismatch −1/gap −2):

| Comparison | SW score | Call |
|---|---|---|
| horse A0A9L0SKW1 vs human OLFML2A (Q68BL7) | 983 | assigned |
| horse A0A9L0SKW1 vs human OLFML2B / photomedin-2 (Q68BL8) | 294 | excluded |

**OLF domain integrity:** horse 341–599 vs human 394–652 → **258/259 = 99.6% identity**; both start `SCEGTLRAVDPPVRHHSYGR` and end `…HFVV`.

**GO decision table (leads — verify):**

| GO id | label | aspect | recommended action | basis |
|---|---|---|---|---|
| GO:0031012 | extracellular matrix | CC | Retain as ISO/ISS orthology annotation + caveat | Ortholog is ECM protein (PMID 15836428); locus has signal-peptide isoforms; supplied 599-aa model lacks signal peptide but has intact OLF domain (99.6% id) |
| GO:0005576 | extracellular region | CC | Safer parent alternative | Matches UniProt "Secreted"; use if ECM specificity deemed insufficiently transferable |
| GO:0008201 / GO:0005539 | heparin / GAG binding | MF | Candidate lead | Photomedin-1 binds CS-E and heparin (PMID 15836428) |

*(Provenance note: CSV export to disk was blocked by the read-only execution sandbox; tables above are the verbatim computed outputs retained from the executed code.)*

---

*Limitations:* No horse-specific experimental data; functional evidence is mouse/human orthologs. Signal-peptide absence is inferred from the current Ensembl ORF and may be corrected by future gene models. SHA-256 not recomputed in-sandbox (equivalent byte-identity verified against live UniProt FASTA).


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)