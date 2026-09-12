---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-08T15:57:03.806550'
end_time: '2026-09-08T16:32:06.381897'
duration_seconds: 2102.58
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: HORSE
  gene: PTPRN2
  gene_symbol: A0A9L0T4W6
  uniprot_accession: A0A9L0T4W6
  taxon_id: NCBITaxon:9796
  taxon_label: Equus caballus
  focus_type: function_assignment
  hypothesis_slug: horse40-protein-dephosphorylation
  hypothesis_text: The horse protein A0A9L0T4W6 participates in protein dephosphorylation.
  term_context: "- Term: protein dephosphorylation (GO:0006470)\n- # Focused function\
    \ hypothesis\n\nHypothesis: The horse protein A0A9L0T4W6 participates in protein\
    \ dephosphorylation.\n\nTarget: Equus caballus (NCBITaxon:9796), UniProt A0A9L0T4W6.\
    \ Gene label: PTPRN2; verify identity independently rather than treating the label\
    \ as proof.\n\nTarget GO claim: GO:0006470 \u2014 protein dephosphorylation. Verify\
    \ its definition and scope.\n\n## Decisive question\n\nIdentify a direct or regulatory\
    \ mechanism for participation in protein dephosphorylation. Separate phosphoprotein\
    \ substrates from phosphoinositide substrates, and establish whether characterized\
    \ mammalian mechanisms transfer to this protein. Lack of intrinsic catalysis alone\
    \ does not exclude participation.\n\n## Identity and sequence inputs\n\n- Target\
    \ record: https://www.uniprot.org/uniprotkb/A0A9L0T4W6/entry\n- Human comparison\
    \ lead: https://www.uniprot.org/uniprotkb/Q92932/entry (PTPRN2). Establish the\
    \ relevant orthology/isoform relationship rather than assuming it.\n- Frozen current\
    \ UniProt sequence: 976 residues; SHA-256 `6e469207454cac638b007421577b3c8140a28f2f24ed1e0ee900486ad5d7c821`.\n\
    - These are current sequences downloaded for the cohort on 2026-09-08. Identity\
    \ with the original prediction-time input has not been established. Evaluate the\
    \ supplied sequence explicitly; document any different sequence used.\n\n```fasta\n\
    >A0A9L0T4W6 Equus caballus PTPRN2\nMGPPLALLLLLLLLPRGPPAAPATRARPLPGLLGCLFEDGLCRPSETCVDGFTWQDDYTQ\n\
    HVMAQELSNLPKTYPQHPESSNPARTSMQSVDNEKRYSQEGDIALAKALQRYLPYLEALS\nQATTSNLLPRMKHGRPPSEGEDALAESVLTYVAQTSALTYAPMPREDYPAGHPLRTLSRL\n\
    QPDELSPKVVGSVDRQNLVAALGAYAAQKHPPPPREGDPGLHNLLHAPWREPRVLSAPAT\nPQKWPLSPGDPKHPLGRGDEALIQSLLKDLRRHQVDMASLSPLDPEEMARVIANAMQGVG\n\
    TEGEREEAGMGVGGEPGEQVDSPEAGLHEARKVGDVRDNRVQDDDDRVYEEVNRLSLTLG\nDLLQDPGSQFLPGAPPLVESFKTEIKKSEDPGASLSSEEESAGVENVRSQTYVKELLERP\n\
    QVDGFGEFQRQIPGAWKEDRRLEAGAQERSGEGLELEVQPSEESGYIVTETDPLSLEKGK\nELLAGVARLLEVPMSVFVDIDVVGPAVTFKVSANVLNVTTAEAVEAAVENKDNLEKTSGL\n\
    KILQTGVGSKSKLKLRPHQAEQEDSTKFIVLTLISVAAILGVLLASGVIYCLRHSSHYRL\nKEKLSGPGGHAGLDATAYQELCRQRMAVRTSDRPEAPHTSRISSVSSQFSDGPMPSPSAR\n\
    SSTSSWSEEPAQPNMDISTGHMVLAYMEDHLKNKNRLEKEWEALCAYQAEPSSSLVAQRE\nENVPKNRCPAVLTYDHSRILLKSENSHSNSDYINASPIMDHDPRNPAYIATQGPLPATVA\n\
    DFWQMVWESGCVVIVMLTPLSENGVRQCYHYWPDEGSNLYHIYEVNLVSEHIWCEDFLVR\nSFYLKNLQTNETRTVTQFHFLSWYDQGVPSSTRSLLDFRRKVNKCYRGRSCPIIVHCSDG\n\
    AGRSGTYVLIDMVLNKMAKGSTVITSHRGARTCTWGGTQLGFFESMLPVRGRHCRRSHTG\nWKTIRVLCTSRSLLGS\n\
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
  source_file: genes/HORSE/PTPRN2/PTPRN2-ai-review.yaml
  source_selector: free-text
  source_context_yaml: "hypothesis: The horse protein A0A9L0T4W6 participates in protein\
    \ dephosphorylation.\nfocus_type: function_assignment\nterm_id: GO:0006470\nterm_label:\
    \ protein dephosphorylation\ncontext:\n- |\n  # Focused function hypothesis\n\n\
    \  Hypothesis: The horse protein A0A9L0T4W6 participates in protein dephosphorylation.\n\
    \n  Target: Equus caballus (NCBITaxon:9796), UniProt A0A9L0T4W6. Gene label: PTPRN2;\
    \ verify identity independently rather than treating the label as proof.\n\n \
    \ Target GO claim: GO:0006470 \u2014 protein dephosphorylation. Verify its definition\
    \ and scope.\n\n  ## Decisive question\n\n  Identify a direct or regulatory mechanism\
    \ for participation in protein dephosphorylation. Separate phosphoprotein substrates\
    \ from phosphoinositide substrates, and establish whether characterized mammalian\
    \ mechanisms transfer to this protein. Lack of intrinsic catalysis alone does\
    \ not exclude participation.\n\n  ## Identity and sequence inputs\n\n  - Target\
    \ record: https://www.uniprot.org/uniprotkb/A0A9L0T4W6/entry\n  - Human comparison\
    \ lead: https://www.uniprot.org/uniprotkb/Q92932/entry (PTPRN2). Establish the\
    \ relevant orthology/isoform relationship rather than assuming it.\n  - Frozen\
    \ current UniProt sequence: 976 residues; SHA-256 `6e469207454cac638b007421577b3c8140a28f2f24ed1e0ee900486ad5d7c821`.\n\
    \  - These are current sequences downloaded for the cohort on 2026-09-08. Identity\
    \ with the original prediction-time input has not been established. Evaluate the\
    \ supplied sequence explicitly; document any different sequence used.\n\n  ```fasta\n\
    \  >A0A9L0T4W6 Equus caballus PTPRN2\n  MGPPLALLLLLLLLPRGPPAAPATRARPLPGLLGCLFEDGLCRPSETCVDGFTWQDDYTQ\n\
    \  HVMAQELSNLPKTYPQHPESSNPARTSMQSVDNEKRYSQEGDIALAKALQRYLPYLEALS\n  QATTSNLLPRMKHGRPPSEGEDALAESVLTYVAQTSALTYAPMPREDYPAGHPLRTLSRL\n\
    \  QPDELSPKVVGSVDRQNLVAALGAYAAQKHPPPPREGDPGLHNLLHAPWREPRVLSAPAT\n  PQKWPLSPGDPKHPLGRGDEALIQSLLKDLRRHQVDMASLSPLDPEEMARVIANAMQGVG\n\
    \  TEGEREEAGMGVGGEPGEQVDSPEAGLHEARKVGDVRDNRVQDDDDRVYEEVNRLSLTLG\n  DLLQDPGSQFLPGAPPLVESFKTEIKKSEDPGASLSSEEESAGVENVRSQTYVKELLERP\n\
    \  QVDGFGEFQRQIPGAWKEDRRLEAGAQERSGEGLELEVQPSEESGYIVTETDPLSLEKGK\n  ELLAGVARLLEVPMSVFVDIDVVGPAVTFKVSANVLNVTTAEAVEAAVENKDNLEKTSGL\n\
    \  KILQTGVGSKSKLKLRPHQAEQEDSTKFIVLTLISVAAILGVLLASGVIYCLRHSSHYRL\n  KEKLSGPGGHAGLDATAYQELCRQRMAVRTSDRPEAPHTSRISSVSSQFSDGPMPSPSAR\n\
    \  SSTSSWSEEPAQPNMDISTGHMVLAYMEDHLKNKNRLEKEWEALCAYQAEPSSSLVAQRE\n  ENVPKNRCPAVLTYDHSRILLKSENSHSNSDYINASPIMDHDPRNPAYIATQGPLPATVA\n\
    \  DFWQMVWESGCVVIVMLTPLSENGVRQCYHYWPDEGSNLYHIYEVNLVSEHIWCEDFLVR\n  SFYLKNLQTNETRTVTQFHFLSWYDQGVPSSTRSLLDFRRKVNKCYRGRSCPIIVHCSDG\n\
    \  AGRSGTYVLIDMVLNKMAKGSTVITSHRGARTCTWGGTQLGFFESMLPVRGRHCRRSHTG\n  WKTIRVLCTSRSLLGS\n\
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
- **Gene directory:** PTPRN2
- **Gene symbol:** A0A9L0T4W6
- **UniProt accession:** A0A9L0T4W6

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** horse40-protein-dephosphorylation
- **Source file:** genes/HORSE/PTPRN2/PTPRN2-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

The horse protein A0A9L0T4W6 participates in protein dephosphorylation.

## Term and Decision Context

- Term: protein dephosphorylation (GO:0006470)
- # Focused function hypothesis

Hypothesis: The horse protein A0A9L0T4W6 participates in protein dephosphorylation.

Target: Equus caballus (NCBITaxon:9796), UniProt A0A9L0T4W6. Gene label: PTPRN2; verify identity independently rather than treating the label as proof.

Target GO claim: GO:0006470 — protein dephosphorylation. Verify its definition and scope.

## Decisive question

Identify a direct or regulatory mechanism for participation in protein dephosphorylation. Separate phosphoprotein substrates from phosphoinositide substrates, and establish whether characterized mammalian mechanisms transfer to this protein. Lack of intrinsic catalysis alone does not exclude participation.

## Identity and sequence inputs

- Target record: https://www.uniprot.org/uniprotkb/A0A9L0T4W6/entry
- Human comparison lead: https://www.uniprot.org/uniprotkb/Q92932/entry (PTPRN2). Establish the relevant orthology/isoform relationship rather than assuming it.
- Frozen current UniProt sequence: 976 residues; SHA-256 `6e469207454cac638b007421577b3c8140a28f2f24ed1e0ee900486ad5d7c821`.
- These are current sequences downloaded for the cohort on 2026-09-08. Identity with the original prediction-time input has not been established. Evaluate the supplied sequence explicitly; document any different sequence used.

```fasta
>A0A9L0T4W6 Equus caballus PTPRN2
MGPPLALLLLLLLLPRGPPAAPATRARPLPGLLGCLFEDGLCRPSETCVDGFTWQDDYTQ
HVMAQELSNLPKTYPQHPESSNPARTSMQSVDNEKRYSQEGDIALAKALQRYLPYLEALS
QATTSNLLPRMKHGRPPSEGEDALAESVLTYVAQTSALTYAPMPREDYPAGHPLRTLSRL
QPDELSPKVVGSVDRQNLVAALGAYAAQKHPPPPREGDPGLHNLLHAPWREPRVLSAPAT
PQKWPLSPGDPKHPLGRGDEALIQSLLKDLRRHQVDMASLSPLDPEEMARVIANAMQGVG
TEGEREEAGMGVGGEPGEQVDSPEAGLHEARKVGDVRDNRVQDDDDRVYEEVNRLSLTLG
DLLQDPGSQFLPGAPPLVESFKTEIKKSEDPGASLSSEEESAGVENVRSQTYVKELLERP
QVDGFGEFQRQIPGAWKEDRRLEAGAQERSGEGLELEVQPSEESGYIVTETDPLSLEKGK
ELLAGVARLLEVPMSVFVDIDVVGPAVTFKVSANVLNVTTAEAVEAAVENKDNLEKTSGL
KILQTGVGSKSKLKLRPHQAEQEDSTKFIVLTLISVAAILGVLLASGVIYCLRHSSHYRL
KEKLSGPGGHAGLDATAYQELCRQRMAVRTSDRPEAPHTSRISSVSSQFSDGPMPSPSAR
SSTSSWSEEPAQPNMDISTGHMVLAYMEDHLKNKNRLEKEWEALCAYQAEPSSSLVAQRE
ENVPKNRCPAVLTYDHSRILLKSENSHSNSDYINASPIMDHDPRNPAYIATQGPLPATVA
DFWQMVWESGCVVIVMLTPLSENGVRQCYHYWPDEGSNLYHIYEVNLVSEHIWCEDFLVR
SFYLKNLQTNETRTVTQFHFLSWYDQGVPSSTRSLLDFRRKVNKCYRGRSCPIIVHCSDG
AGRSGTYVLIDMVLNKMAKGSTVITSHRGARTCTWGGTQLGFFESMLPVRGRHCRRSHTG
WKTIRVLCTSRSLLGS
```

## Evidence and deliverable

Use primary literature and public sequence, structural and genomic resources. Select analyses that answer the decisive question; this is not a general gene review. Assess support and contrary evidence, and allow an unresolved outcome. Distinguish directly observed horse evidence, justified mammalian transfer, and results for a different protein model.

Do not consult the ai-gene-review repository's existing judgments, research syntheses or local bioinformatics analyses. Those are held out for comparison. Do not use agreement with ARBA or another prediction as biological validation. Preserve reproducible methods, accessions/versions, actual computation outputs and primary-source URLs/DOIs/PMIDs. Report the decisive findings and limitations, not just a verdict.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: The horse protein A0A9L0T4W6 participates in protein dephosphorylation.
focus_type: function_assignment
term_id: GO:0006470
term_label: protein dephosphorylation
context:
- |
  # Focused function hypothesis

  Hypothesis: The horse protein A0A9L0T4W6 participates in protein dephosphorylation.

  Target: Equus caballus (NCBITaxon:9796), UniProt A0A9L0T4W6. Gene label: PTPRN2; verify identity independently rather than treating the label as proof.

  Target GO claim: GO:0006470 — protein dephosphorylation. Verify its definition and scope.

  ## Decisive question

  Identify a direct or regulatory mechanism for participation in protein dephosphorylation. Separate phosphoprotein substrates from phosphoinositide substrates, and establish whether characterized mammalian mechanisms transfer to this protein. Lack of intrinsic catalysis alone does not exclude participation.

  ## Identity and sequence inputs

  - Target record: https://www.uniprot.org/uniprotkb/A0A9L0T4W6/entry
  - Human comparison lead: https://www.uniprot.org/uniprotkb/Q92932/entry (PTPRN2). Establish the relevant orthology/isoform relationship rather than assuming it.
  - Frozen current UniProt sequence: 976 residues; SHA-256 `6e469207454cac638b007421577b3c8140a28f2f24ed1e0ee900486ad5d7c821`.
  - These are current sequences downloaded for the cohort on 2026-09-08. Identity with the original prediction-time input has not been established. Evaluate the supplied sequence explicitly; document any different sequence used.

  ```fasta
  >A0A9L0T4W6 Equus caballus PTPRN2
  MGPPLALLLLLLLLPRGPPAAPATRARPLPGLLGCLFEDGLCRPSETCVDGFTWQDDYTQ
  HVMAQELSNLPKTYPQHPESSNPARTSMQSVDNEKRYSQEGDIALAKALQRYLPYLEALS
  QATTSNLLPRMKHGRPPSEGEDALAESVLTYVAQTSALTYAPMPREDYPAGHPLRTLSRL
  QPDELSPKVVGSVDRQNLVAALGAYAAQKHPPPPREGDPGLHNLLHAPWREPRVLSAPAT
  PQKWPLSPGDPKHPLGRGDEALIQSLLKDLRRHQVDMASLSPLDPEEMARVIANAMQGVG
  TEGEREEAGMGVGGEPGEQVDSPEAGLHEARKVGDVRDNRVQDDDDRVYEEVNRLSLTLG
  DLLQDPGSQFLPGAPPLVESFKTEIKKSEDPGASLSSEEESAGVENVRSQTYVKELLERP
  QVDGFGEFQRQIPGAWKEDRRLEAGAQERSGEGLELEVQPSEESGYIVTETDPLSLEKGK
  ELLAGVARLLEVPMSVFVDIDVVGPAVTFKVSANVLNVTTAEAVEAAVENKDNLEKTSGL
  KILQTGVGSKSKLKLRPHQAEQEDSTKFIVLTLISVAAILGVLLASGVIYCLRHSSHYRL
  KEKLSGPGGHAGLDATAYQELCRQRMAVRTSDRPEAPHTSRISSVSSQFSDGPMPSPSAR
  SSTSSWSEEPAQPNMDISTGHMVLAYMEDHLKNKNRLEKEWEALCAYQAEPSSSLVAQRE
  ENVPKNRCPAVLTYDHSRILLKSENSHSNSDYINASPIMDHDPRNPAYIATQGPLPATVA
  DFWQMVWESGCVVIVMLTPLSENGVRQCYHYWPDEGSNLYHIYEVNLVSEHIWCEDFLVR
  SFYLKNLQTNETRTVTQFHFLSWYDQGVPSSTRSLLDFRRKVNKCYRGRSCPIIVHCSDG
  AGRSGTYVLIDMVLNKMAKGSTVITSHRGARTCTWGGTQLGFFESMLPVRGRHCRRSHTG
  WKTIRVLCTSRSLLGS
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

# Focused Hypothesis Report — Horse PTPRN2 (A0A9L0T4W6) and "protein dephosphorylation" (GO:0006470)

**Hypothesis evaluated:** The horse protein A0A9L0T4W6 participates in protein dephosphorylation (GO:0006470).
**Focus type:** function_assignment. **Target:** *Equus caballus* (NCBITaxon:9796), UniProt A0A9L0T4W6, gene label PTPRN2.
**Date:** 2026-09-08.

---

## Executive Judgment

**Verdict: REFUTED / over-annotated for a direct function assignment.**

> **Provenance verified (Iteration 2):** The supplied 976-aa sequence's SHA-256 was recomputed in-sandbox = `6e469207454cac638b007421577b3c8140a28f2f24ed1e0ee900486ad5d7c821` — **exact match** to the frozen spec. The live UniProt record A0A9L0T4W6 (unreviewed TrEMBL, name "Protein-tyrosine-phosphatase") carries **only one MF GO term, GO:0004725 (protein tyrosine phosphatase activity), with evidence code `IEA:InterPro`** — i.e., an automated domain-presence annotation, no experimental support, and GO:0006470 is a *downstream* BP inference from it. InterPro correctly types the protein as **IPR033522 "IA-2/IA-2_beta"** (pseudophosphatase family).

Horse A0A9L0T4W6 is the ortholog of human **PTPRN2 (IA-2β / phogrin)**, a member of the receptor-type protein-tyrosine-phosphatase (RPTP) family that is one of the best-characterized **pseudophosphatases**. Across multiple independent biochemical studies the wild-type IA-2 family PTP-like domain has **no activity against conventional (protein/phosphotyrosine) substrates**; catalytic competence can only be engineered by "back-mutating" three non-consensus active-site residues to the active PTP1B identities (Drake 2003, PMID 12697028). The **only demonstrated intrinsic catalytic activity** of phogrin/PTPRN2 is toward **phosphoinositide lipids** (PI3P, PI(4,5)P2 — Caromile 2010, PMID 20097759; Sengelaub 2016, PMID 26620550), which is **lipid dephosphorylation, a process distinct from GO:0006470**. The protein's documented protein-directed effects are **non-catalytic** — scaffolding of the insulin receptor/IRS2 (Torii 2018, PMID 29483197) and heterodimeric **down-regulation** of an active RPTP (Gross 2002, PMID 12364328), i.e., *negative regulation* of dephosphorylation, not participation in it.

**Most important caveats.** (1) All functional data are from human/rodent/*C. elegans* orthologs; there is **no horse-specific assay**. Transfer is justified because the horse sequence is unambiguously the PTPRN2 ortholog and conserves the catalytic-degeneracy signature (see Identity below). (2) "Lack of intrinsic catalysis does not exclude participation" was tested explicitly — the only regulatory link that is directional *opposes* dephosphorylation, so it does not rescue the seed hypothesis.

---

## Evidence Matrix

| # | Citation (PMID/DOI) | Evidence type | Supports/Refutes/Qualifies | Claim tested | Key finding | Context | Confidence & limitations |
|---|---|---|---|---|---|---|---|
| 1 | Drake 2003 (12697028) | Direct enzyme assay + mutagenesis | **Refutes** direct role | Does IA-2/IA-2β dephosphorylate proteins? | WT IA-2 & IA-2β "lack activity against conventional PTP substrates"; activity needs back-mutation of 3 residues (PTP1B Tyr46/Asp181/Ala217) | Recombinant human catalytic domains, in vitro | High. In vitro; conventional (pTyr peptide/pNPP) substrates |
| 2 | Caromile 2010 (20097759) | Direct enzyme assay (lipid) | **Qualifies / Refutes** (protein) | What is phogrin's substrate? | "no significant enzymatic activity for phogrin has ever been reported"; phogrin dephosphorylates PI3P and PI(4,5)P2, **not** PI(3,4,5)P3; Cys-dependent | Recombinant + overexpression, β-cell biology | High for lipid substrate; activity low/context-dependent |
| 3 | Sengelaub 2016 (26620550) | Functional/enzymatic (cells) | **Qualifies** (lipid, not protein) | Substrate of PTPRN2 in cells | PTPRN2 reduces plasma-membrane PI(4,5)P2, releasing cofilin → actin remodeling/metastasis | Metastatic human breast cancer cells | Medium-high; substrate is a phosphoinositide |
| 4 | Gross 2002 (12364328) | Interaction (Y2H/pulldown/co-IP) | **Refutes/competing** | Does the PTP-like domain catalyze? Regulatory link? | "single enzymatically inactive PTP-like domain"; heterodimerizes with RPTPα/ε and **down-regulates** RPTPα activity | COS-1, yeast | High for inactivity; regulatory effect *inhibits* a PTP |
| 5 | Torii 2018 (29483197) | Mutant phenotype / interaction | **Qualifies** (non-catalytic) | Mechanism in signaling | "pseudophosphatase"; phogrin-IR complex stabilizes IRS2; KO lowers IRS2 44% | Mouse islets, β-cell lines | Medium-high; scaffolding, not catalysis |
| 6 | Cai 2009 (19343207) | Genetic/phenotype | **Supports "inactive"** | Nature of IA-2 | IA-2 = "a catalytically inactive protein phosphatase" in dense-core-vesicle membranes | *C. elegans* IDA-1 ortholog | Medium; ortholog, DCV biology |
| 7 | This report — sequence analysis | Structural/evolutionary (computational) | **Supports transfer + refutes** | Is horse the PTPRN2 ortholog? Is the catalytic site degenerate? | PTP-domain identity 80.7% to PTPRN2 vs 67.1% to PTPRN; P-loop and catalytic motifs identical to human PTPRN2; Asp sits at the PTP1B-Ala217 position (one of Drake's 3 non-consensus residues) | In-sandbox, UniProt Q92932/Q16849 | Medium-high; ungapped anchored window (no gapped aligner in sandbox) |
| 8 | This report — UniProt record | Database provenance | **Refutes / context** | Origin of the phosphatase annotation | Only MF term GO:0004725 with evidence `IEA:InterPro`; no experimental GO; InterPro types it IPR033522 IA-2/IA-2_beta; SHA-256 of sequence matches frozen spec exactly | Live UniProt A0A9L0T4W6 (2026-09-08) | High; shows the annotation is computational/domain-inherited |
| 9 | This report — PTP1B alignment | Structural/evolutionary (computational) | **Refutes** | Is the catalytic machinery intact in the horse itself? | Anchored to active PTP1B (P18031): P-loop `HCSDGAGR` vs active `HCSAGIGR` (Asp at Ala217 position); general-acid loop `WYDQGVP` vs active `WPDFGVP` (Pro→Tyr, WPD→WYD); catalytic Cys897/invariant Arg retained. The isolated `WPD` at idx 811 is 82 aa from the P-loop (canonical spacing ~33) and is NOT the catalytic loop | In-sandbox, UniProt A0A9L0T4W6 vs P18031 | Medium-high; anchored (not full gapped) alignment |

---

## GO Term Scope Verification (QuickGO, retrieved Iteration 3)

Authoritative GO definitions confirm that the seed term is **protein-substrate-specific** and distinct from the lipid term that phogrin's activity actually fits:

- **GO:0006470** protein dephosphorylation (BP): *"The process of removing one or more phosphoric residues from a **protein**."*
- **GO:0004725** protein tyrosine phosphatase activity (MF): *"Catalysis of the reaction: **protein** tyrosine phosphate + H2O = protein tyrosine + phosphate."*
- **GO:0046856** phosphatidylinositol dephosphorylation (BP): *"...removing one or more phosphate groups from a **phosphatidylinositol**."*
- **GO:0052866** phosphatidylinositol phosphate phosphatase activity (MF).

Because the only demonstrated PTPRN2 catalytic activity is on **phosphatidylinositol lipids**, it satisfies GO:0046856/GO:0052866 — **not** GO:0006470/GO:0004725, whose definitions explicitly require a protein substrate. This closes the decisive question's phosphoprotein-vs-phosphoinositide substrate separation.

## GO Decision Table (leads — require curator verification)

| GO term | Aspect | Current basis | Evidence verdict | Recommended action |
|---|---|---|---|---|
| GO:0006470 protein dephosphorylation | BP | Downstream of the MF PTP-activity call | Refuted (pseudophosphatase; no protein-substrate activity) | **Do not assign / remove** |
| GO:0004725 protein tyrosine phosphatase activity | MF | `IEA:InterPro` (domain presence) | Refuted for horse ortholog (WT inactive; ≥3 back-mutations needed) | **Remove or down-qualify**; not experimentally supported |
| GO:0052866 / GO:0004438 phosphatidylinositol/PI-phosphatase activity | MF | Not in record | Supported in human/mouse ortholog (Caromile 2010; Sengelaub 2016) | **Candidate ISS/ISO add** with low-activity caveat |
| GO:0046856 phosphatidylinositol dephosphorylation | BP | Not in record | Supported in ortholog | **Candidate ISS/ISO add** (replaces protein-dephos claim) |
| GO:0030141 secretory granule / GO:0030658 transport vesicle membrane | CC | `IEA` | Consistent with DCV biology | Retain (secondary to this hypothesis) |

## GO Curation Implications

- **GO:0006470 (protein dephosphorylation, BP):** Evidence does **not** support annotating horse PTPRN2 to this term as a direct/positive function. Recommended curator action: **do not assert / remove or restrict** any GO:0006470 (and the parent MF GO:0004721 phosphoprotein phosphatase activity / GO:0004725 protein tyrosine phosphatase activity) annotation that is based only on family membership or automated pipelines (e.g., InterPro/ARBA "PTP domain → protein dephosphorylation"). This is classic **pseudophosphatase over-annotation by paralog/domain inheritance**.
- **More accurate MF terms (leads, if any activity is to be annotated):** phosphatidylinositol phosphatase / phosphoinositide phosphatase activity (e.g., **GO:0004438 / GO:0052866**) with **BP GO:0046856 phosphatidylinositol dephosphorylation** — supported by Caromile 2010 and Sengelaub 2016, but note the activity is weak/context-dependent and should carry an appropriate evidence code (IDA in human/mouse; ISS/ISO for horse) and possibly a "low activity" note.
- **CC:** insulin/dense-core secretory-granule membrane and plasma membrane localization are well supported (secondary to this hypothesis).
- **Non-core / regulatory:** any protein-phosphorylation link is best captured as **negative regulation of a PTP** or **scaffolding (protein binding)** — but avoid "protein binding" as a terminal recommendation; prefer the phosphoinositide MF/BP terms where activity is annotated.

**Bottom line for the curator:** the seed function assignment (protein dephosphorylation) should be treated as **incorrect/over-precise**; the defensible catalytic annotation, if any, is lipid (phosphoinositide) dephosphorylation.

---

## Mechanistic Scope

Immediate molecular function tested = enzymatic removal of phosphate from a **protein** amino-acid residue. Direct gene-product activity: **absent** for proteins (degenerate PTP active site). The gene product's genuine molecular activities/roles are: (i) **weak phosphoinositide phosphatase** (lipid head-group, not protein); (ii) **secretory-granule membrane scaffold** influencing insulin/IRS2 signaling; (iii) **autoantigen** in diabetes. Downstream phenotypes (insulin secretion, β-cell signaling, cancer-cell migration) are **consequences of lipid signaling and scaffolding**, not evidence of protein-dephosphorylation catalysis.

---

## Conflicts and Alternatives

- **Paralog confusion:** IA-2 (PTPRN, Q16849) vs IA-2β/phogrin (PTPRN2, Q92932). Sequence analysis assigns the horse protein to **PTPRN2** (80.7% vs 67.1% PTP-domain identity; identical P-loop/WPD-loop to PTPRN2). Both paralogs are nonetheless pseudophosphatases, so the conclusion is robust to residual paralog uncertainty.
- **"Domain present ⇒ function present" fallacy:** the horse GO:0004725 call is `IEA:InterPro`, driven purely by PTP-domain detection; the InterPro rule even asserts an active-site phosphocysteine at residue 897. Yet the catalytic Cys/invariant Arg are embedded in a **degenerate active site** (P-loop `HCSDGAGR`; general-acid loop `WYDQGVP` not `WPDFGVP`), and direct assays (Drake 2003; Caromile 2010) show the WT domain is catalytically dead on proteins. Retention of a Cys/Arg (and a coincidental non-catalytic `WPD` triplet 82 aa away) is not evidence of activity.
- **Substrate misassignment:** literature activity is on **phosphoinositides**, which can be mis-mapped to "dephosphorylation → protein dephosphorylation" if the lipid nature of the substrate is not tracked.
- **Directionality:** the one directional protein-phosphorylation link (Gross 2002) is **inhibitory** toward an active PTP — opposite to "performing protein dephosphorylation."

---

## Knowledge Gaps

1. **No horse-specific biochemical data.** Checked: PubMed. Matters because the annotation is for *E. caballus*. Resolve: express horse PTP-like domain and assay pNPP/phosphopeptide vs PI3P/PI(4,5)P2.
2. **Exact active-site mapping in horse.** *Partially resolved (Iteration 2):* anchored alignment to active PTP1B (P18031) confirms a degenerate P-loop (`HCSDGAGR`, Asp at the PTP1B-Ala217 position) and an altered general-acid loop (`WYDQGVP` vs `WPDFGVP`; Pro→Tyr, WPD→WYD), with the catalytic Cys897/invariant Arg retained. The isolated `WPD` triplet noted in Iteration 1 is 82 aa from the P-loop (outside the ~33-aa catalytic register) and is not the catalytic loop. Residual gap: a full gapped alignment/AlphaFold superposition would fix each Drake residue (Tyr46/Asp181/Ala217 equivalents) unambiguously.
3. **Physiological relevance and magnitude of lipid-phosphatase activity in vivo** remains debated (low specific activity in some assays). Resolve: catalytic-Cys mutant rescue experiments in horse-relevant tissue.

---

## Discriminating Tests

1. **In vitro dual-substrate assay** of recombinant horse PTP-like domain: phosphotyrosine peptide/pNPP (protein-like) vs PI3P/PI(4,5)P2 (lipid). Prediction: negligible protein activity, measurable lipid activity → refutes GO:0006470, supports lipid term.
2. **Active-site back-mutation** (horse equivalents of PTP1B Tyr46/Asp181/Ala217): if only the triple mutant gains protein-pTyr activity, WT is confirmed pseudophosphatase.
3. **Catalytic-Cys (C→S) mutant** in a cell PI(4,5)P2 reporter assay to confirm lipid- (not protein-) directed catalysis.
4. **AlphaFold/structure superposition** on PTP1B to verify WPD-loop general-acid geometry and the Ala217-position Asp.

---

## Curation Leads (require curator verification)

- **Action change:** Flag/remove GO:0006470 (and MF GO:0004725/GO:0004721) as a direct annotation for A0A9L0T4W6 if present via automated/ISS routes; treat as **pseudophosphatase over-annotation**.
- **Candidate replacement terms (leads):** MF phosphoinositide/PI phosphatase activity (GO:0052866 / GO:0004438); BP GO:0046856 (phosphatidylinositol dephosphorylation) — annotate by ISS/ISO from human/mouse with a low-activity caveat, if the curator wishes to record catalytic function at all.
- **Candidate references + verify snippets:**
  - Drake 2003, PMID 12697028 — "characterized by a lack of activity against conventional PTP substrates"; three-residue back-mutation restores activity.
  - Caromile 2010, PMID 20097759 — "no significant enzymatic activity for phogrin has ever been reported"; dephosphorylates PI3P and PI(4,5)P2.
  - Gross 2002, PMID 12364328 — "single enzymatically inactive PTP-like domain"; "down-regulate RPTPalpha enzymatic activity".
  - Sengelaub 2016, PMID 26620550 — PTPRN2 reduces plasma-membrane PI(4,5)P2.
  - Torii 2018, PMID 29483197 — "pseudophosphatase"; phogrin-IR/IRS2 scaffolding.
  - Cai 2009, PMID 19343207 — IA-2 "a catalytically inactive protein phosphatase".
- **Suggested curator questions:** Is the existing GO:0006470 annotation IEA/ISS-derived from PTP-domain presence? Does any experimental annotation for the horse entry exist? Should catalytic annotation be recorded as lipid rather than protein dephosphorylation?
- **Suggested experiments:** the dual-substrate and back-mutation assays above.

---

## Limitations

- No gapped global aligner or structure tool in the execution sandbox; identity computed from an anchored ungapped PTP-domain window and whole-protein k-mer Jaccard. Paralog assignment is nonetheless clear.
- All primary functional evidence is from non-horse orthologs; horse conclusions are **justified transfer**, explicitly labeled, not direct observation.
- SHA-256 of the supplied sequence was recomputed with a pure-Python implementation (hashlib/struct blocked) and **matches the frozen spec exactly** (`6e46920745...5d7c821`; length 976), so the analysis is on the intended sequence.


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)