---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-08T15:57:03.797429'
end_time: '2026-09-08T17:02:57.632113'
duration_seconds: 3953.83
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: HORSE
  gene: CTDSP2
  gene_symbol: CTDSP2
  uniprot_accession: F7A4N8
  taxon_id: NCBITaxon:9796
  taxon_label: Equus caballus
  focus_type: function_assignment
  hypothesis_slug: horse40-kinase-activity
  hypothesis_text: The horse protein F7A4N8 enables kinase activity.
  term_context: "- Term: kinase activity (GO:0016301)\n- # Focused function hypothesis\n\
    \nHypothesis: The horse protein F7A4N8 enables kinase activity.\n\nTarget: Equus\
    \ caballus (NCBITaxon:9796), UniProt F7A4N8. Gene label: CTDSP2; verify identity\
    \ independently rather than treating the label as proof.\n\nTarget GO claim: GO:0016301\
    \ \u2014 kinase activity. Verify its definition and scope.\n\n## Decisive question\n\
    \nDetermine whether this exact sequence supports a kinase fold and phosphotransfer\
    \ mechanism. Establish its family independently; if a kinase mechanism is unsupported,\
    \ identify the strongest alternative explanation without assuming the gene label\
    \ is correct.\n\n## Identity and sequence inputs\n\n- Target record: https://www.uniprot.org/uniprotkb/F7A4N8/entry\n\
    - Human comparison lead: https://www.uniprot.org/uniprotkb/O14595/entry (CTDSP2).\
    \ Establish the relevant orthology/isoform relationship rather than assuming it.\n\
    - Frozen current UniProt sequence: 174 residues; SHA-256 `94788163d6db3dbca3e1432762d7b2a1e8b57e1be2048c233c505a07a0b5042c`.\n\
    - These are current sequences downloaded for the cohort on 2026-09-08. Identity\
    \ with the original prediction-time input has not been established. Evaluate the\
    \ supplied sequence explicitly; document any different sequence used.\n\n```fasta\n\
    >F7A4N8 Equus caballus CTDSP2\nMEHGSIITQARREDALVLTKQGLVSKSSPKKPRGRNIFKALFCCFRAQHVGQSSPSTELS\n\
    TYKEEANTIAKSDLLQCLQYQFYQGIRFWGTARVHPTAALASISMSRALHRPQGRRGRGA\nSTVSSFSTSWPSSGASLGCSLSSRLLDKPRSSQSSAGGLLGLSWWQISAACLWF\n\
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
  source_file: genes/HORSE/CTDSP2/CTDSP2-ai-review.yaml
  source_selector: free-text
  source_context_yaml: "hypothesis: The horse protein F7A4N8 enables kinase activity.\n\
    focus_type: function_assignment\nterm_id: GO:0016301\nterm_label: kinase activity\n\
    context:\n- |\n  # Focused function hypothesis\n\n  Hypothesis: The horse protein\
    \ F7A4N8 enables kinase activity.\n\n  Target: Equus caballus (NCBITaxon:9796),\
    \ UniProt F7A4N8. Gene label: CTDSP2; verify identity independently rather than\
    \ treating the label as proof.\n\n  Target GO claim: GO:0016301 \u2014 kinase\
    \ activity. Verify its definition and scope.\n\n  ## Decisive question\n\n  Determine\
    \ whether this exact sequence supports a kinase fold and phosphotransfer mechanism.\
    \ Establish its family independently; if a kinase mechanism is unsupported, identify\
    \ the strongest alternative explanation without assuming the gene label is correct.\n\
    \n  ## Identity and sequence inputs\n\n  - Target record: https://www.uniprot.org/uniprotkb/F7A4N8/entry\n\
    \  - Human comparison lead: https://www.uniprot.org/uniprotkb/O14595/entry (CTDSP2).\
    \ Establish the relevant orthology/isoform relationship rather than assuming it.\n\
    \  - Frozen current UniProt sequence: 174 residues; SHA-256 `94788163d6db3dbca3e1432762d7b2a1e8b57e1be2048c233c505a07a0b5042c`.\n\
    \  - These are current sequences downloaded for the cohort on 2026-09-08. Identity\
    \ with the original prediction-time input has not been established. Evaluate the\
    \ supplied sequence explicitly; document any different sequence used.\n\n  ```fasta\n\
    \  >F7A4N8 Equus caballus CTDSP2\n  MEHGSIITQARREDALVLTKQGLVSKSSPKKPRGRNIFKALFCCFRAQHVGQSSPSTELS\n\
    \  TYKEEANTIAKSDLLQCLQYQFYQGIRFWGTARVHPTAALASISMSRALHRPQGRRGRGA\n  STVSSFSTSWPSSGASLGCSLSSRLLDKPRSSQSSAGGLLGLSWWQISAACLWF\n\
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
- **Gene directory:** CTDSP2
- **Gene symbol:** CTDSP2
- **UniProt accession:** F7A4N8

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** horse40-kinase-activity
- **Source file:** genes/HORSE/CTDSP2/CTDSP2-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

The horse protein F7A4N8 enables kinase activity.

## Term and Decision Context

- Term: kinase activity (GO:0016301)
- # Focused function hypothesis

Hypothesis: The horse protein F7A4N8 enables kinase activity.

Target: Equus caballus (NCBITaxon:9796), UniProt F7A4N8. Gene label: CTDSP2; verify identity independently rather than treating the label as proof.

Target GO claim: GO:0016301 — kinase activity. Verify its definition and scope.

## Decisive question

Determine whether this exact sequence supports a kinase fold and phosphotransfer mechanism. Establish its family independently; if a kinase mechanism is unsupported, identify the strongest alternative explanation without assuming the gene label is correct.

## Identity and sequence inputs

- Target record: https://www.uniprot.org/uniprotkb/F7A4N8/entry
- Human comparison lead: https://www.uniprot.org/uniprotkb/O14595/entry (CTDSP2). Establish the relevant orthology/isoform relationship rather than assuming it.
- Frozen current UniProt sequence: 174 residues; SHA-256 `94788163d6db3dbca3e1432762d7b2a1e8b57e1be2048c233c505a07a0b5042c`.
- These are current sequences downloaded for the cohort on 2026-09-08. Identity with the original prediction-time input has not been established. Evaluate the supplied sequence explicitly; document any different sequence used.

```fasta
>F7A4N8 Equus caballus CTDSP2
MEHGSIITQARREDALVLTKQGLVSKSSPKKPRGRNIFKALFCCFRAQHVGQSSPSTELS
TYKEEANTIAKSDLLQCLQYQFYQGIRFWGTARVHPTAALASISMSRALHRPQGRRGRGA
STVSSFSTSWPSSGASLGCSLSSRLLDKPRSSQSSAGGLLGLSWWQISAACLWF
```

## Evidence and deliverable

Use primary literature and public sequence, structural and genomic resources. Select analyses that answer the decisive question; this is not a general gene review. Assess support and contrary evidence, and allow an unresolved outcome. Distinguish directly observed horse evidence, justified mammalian transfer, and results for a different protein model.

Do not consult the ai-gene-review repository's existing judgments, research syntheses or local bioinformatics analyses. Those are held out for comparison. Do not use agreement with ARBA or another prediction as biological validation. Preserve reproducible methods, accessions/versions, actual computation outputs and primary-source URLs/DOIs/PMIDs. Report the decisive findings and limitations, not just a verdict.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: The horse protein F7A4N8 enables kinase activity.
focus_type: function_assignment
term_id: GO:0016301
term_label: kinase activity
context:
- |
  # Focused function hypothesis

  Hypothesis: The horse protein F7A4N8 enables kinase activity.

  Target: Equus caballus (NCBITaxon:9796), UniProt F7A4N8. Gene label: CTDSP2; verify identity independently rather than treating the label as proof.

  Target GO claim: GO:0016301 — kinase activity. Verify its definition and scope.

  ## Decisive question

  Determine whether this exact sequence supports a kinase fold and phosphotransfer mechanism. Establish its family independently; if a kinase mechanism is unsupported, identify the strongest alternative explanation without assuming the gene label is correct.

  ## Identity and sequence inputs

  - Target record: https://www.uniprot.org/uniprotkb/F7A4N8/entry
  - Human comparison lead: https://www.uniprot.org/uniprotkb/O14595/entry (CTDSP2). Establish the relevant orthology/isoform relationship rather than assuming it.
  - Frozen current UniProt sequence: 174 residues; SHA-256 `94788163d6db3dbca3e1432762d7b2a1e8b57e1be2048c233c505a07a0b5042c`.
  - These are current sequences downloaded for the cohort on 2026-09-08. Identity with the original prediction-time input has not been established. Evaluate the supplied sequence explicitly; document any different sequence used.

  ```fasta
  >F7A4N8 Equus caballus CTDSP2
  MEHGSIITQARREDALVLTKQGLVSKSSPKKPRGRNIFKALFCCFRAQHVGQSSPSTELS
  TYKEEANTIAKSDLLQCLQYQFYQGIRFWGTARVHPTAALASISMSRALHRPQGRRGRGA
  STVSSFSTSWPSSGASLGCSLSSRLLDKPRSSQSSAGGLLGLSWWQISAACLWF
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

# Focused Hypothesis Report — F7A4N8 (Equus caballus CTDSP2): "enables kinase activity" (GO:0016301)

## Executive Judgment

**Verdict: REFUTED (kinase activity not supported), with the strongest alternative being a HAD-like protein phosphatase family.**

The seed hypothesis is that horse protein **F7A4N8 enables kinase activity (GO:0016301)**. Independent
sequence and orthology analysis refutes this:

1. **No kinase machinery.** The exact 174-aa sequence (SHA-256 verified) contains **none** of the
   defining eukaryotic protein-kinase catalytic motifs (Gly-rich loop GxGxxG, VAIK β3 lysine, HRD
   catalytic loop, DFG Mg-binding, APE). It has only 3 aspartates in 174 residues — incompatible with
   an ATP-phosphotransfer active site.
2. **The gene family is a phosphatase, not a kinase.** CTDSP2 belongs to the FCP/SCP small
   C-terminal-domain phosphatase family (HAD-like hydrolase superfamily). Its human ortholog O14595 is a
   reviewed **protein phosphatase** (active-site Asp107 forms a 4-aspartylphosphate intermediate). A
   phosphatase catalyzes **de**phosphorylation — mechanistically the opposite of a kinase.
3. **This particular horse model is truncated/aberrant.** F7A4N8 matches human CTDSP2 at ~96% identity
   over only the N-terminal ~84 residues, then diverges into a Ser/Arg-rich low-complexity C-terminus.
   It **lacks the entire FCP1-homology catalytic phosphatase domain** (human residues 97–255, DLDET
   active site). So this sequence supports neither kinase nor (on its own) phosphatase catalysis.

**Most important caveat:** F7A4N8 is a TrEMBL/Ensembl automatic prediction whose C-terminus appears to be
an incomplete or mis-predicted gene model. Identity with the original prediction-time input was not
independently establishable, but the supplied sequence was verified byte-for-byte (hash match).

---

## Reproducible Methods & Provenance

- **Sequences (retrieved 2026-09-08 from UniProt REST `rest.uniprot.org/uniprotkb/{acc}.json`):**
  - Target: **F7A4N8** (TrEMBL, *Equus caballus*), 174 aa, mass 19,012 Da; submitted name "CTD small
    phosphatase 2"; gene CTDSP2 (VGNC). SHA-256 = `94788163d6db3dbca3e1432762d7b2a1e8b57e1be2048c233c505a07a0b5042c` **(match confirmed)**.
  - Human lead: **O14595** (Swiss-Prot), "Carboxy-terminal domain RNA polymerase II polypeptide A small
    phosphatase 2", 271 aa; FCP1-homology domain 97–255; active sites Asp107 (4-aspartylphosphate
    intermediate) and Asp109 (proton donor); Mg binding 218; keywords Hydrolase, Protein phosphatase,
    Magnesium, Nucleus; has PDB structure.
- **Motif scan** (regex against the verified sequence) — kinase hallmarks and FCP/SCP DxDxT/V motif.
- **Pairwise comparison** F7A4N8 vs O14595 (identity of shared prefix; divergence point; catalytic-domain
  presence).
- Computed outputs are reproduced in the Evidence Matrix and Mechanistic Scope below.

**Independent cross-database checks (added Iteration 2):**
- **UniProt F7A4N8** has **no GO cross-references** and the word "kinase" appears **0 times** — the kinase
  claim is not database-derived.
- **UniProt O14595** GO annotations: **GO:0008420** "RNA polymerase II CTD heptapeptide repeat phosphatase
  activity" with **IDA (direct assay)** evidence; **GO:0006470** protein dephosphorylation (IDA);
  GO:0005654 nucleoplasm (TAS). "kinase" appears 0 times; "phosphatase" 13 times.
- **InterPro F7A4N8** → **HTTP 204 (no domain matches at all)** — the horse model carries neither a kinase
  domain nor the phosphatase domain.
- **InterPro O14595** → FCP1 homology domain (IPR004274), Dullard phosphatase domain (IPR011948), HAD-like
  superfamily (IPR036412), Pfam **PF03031 "NLI interacting factor-like phosphatase"**, SMART SM00577
  "catalytic domain of ctd-like phosphatases", SFLD "RNA Pol CTD Phosphatase Like" — all phosphatase/HAD
  signatures, **zero kinase signatures**.

**Structural check (added Iteration 3):** AlphaFold DB model **AF-F7A4N8-F1 (v6, 2025-03-31)** — mean
pLDDT **46.2 (very low)**; 66% of residues pLDDT <50, 98% <70; shared N-terminus (res 1–84) mean 51.4,
divergent C-terminus (res 85–174) mean 41.4. **No high-confidence globular/catalytic fold**, consistent
with the InterPro no-domain result.

Key computed values:
- Kinase motifs GxGxxG / VAIK / HRD / DFG / APE: **all NONE**.
- FCP/SCP catalytic motif DxDx[TV] / DLDET in F7A4N8: **NONE** ("DLDET" absent).
- F7A4N8 vs O14595 identity over first 84 aa: **81/84 = 96.4%**; sequences track together until human
  ~res 84 (…CLQYQFYQ), then diverge. Human DLDET catalytic motif at residues 107–111 has **no counterpart**
  in the horse model.
- F7A4N8 composition: Ser 16.7%, Arg 8.0%, Asp 1.7% (Asp at positions 14, 73, 147 only).

---

## Evidence Matrix

| # | Citation | Evidence type | Supports/Refutes | Claim tested | Key finding | Context | Confidence / limitations |
|---|----------|---------------|------------------|--------------|-------------|---------|--------------------------|
| 1 | This analysis (UniProt F7A4N8, 2026-09-08) | Computational (motif scan) | **Refutes** | F7A4N8 has kinase catalytic machinery | No GxGxxG/VAIK/HRD/DFG/APE; only 3 Asp | Horse protein sequence | High; sequence-based, no experiment |
| 2 | UniProt O14595 (Swiss-Prot) | Database (curated, structure-backed) | **Competing/qualifies** | True MF of CTDSP2 | Protein phosphatase; Asp107 4-aspartylphosphate intermediate; FCP1 domain; PDB structure | Human ortholog | High (reviewed + 3D) |
| 3 | This analysis (pairwise align) | Structural/evolutionary | **Refutes/qualifies** | Horse model encodes the catalytic domain | F7A4N8 = 96% id over N-term ~84 aa, then diverges; **lacks FCP1 catalytic domain / DLDET** | Horse vs human | High; alignment is unambiguous at divergence |
| 4 | Burkholder et al. 2018, **PMID 30217818** | Direct assay (kinetics + X-ray) | **Competing** | SCP family reaction direction | SCP1 **dephosphorylates** REST degron pSer-861 (phosphatase) | Human, in vitro + HEK293 | High; paralog SCP1, transfer to family |
| 5 | Visvanathan et al. 2007, **PMID 17403776** | Mutant/overexpression phenotype | **Competing** | SCP family is a phosphatase | "phosphatase SCP1 (small C-terminal domain phosphatase 1)" controls neurogenesis | Mouse/chick CNS development | High; paralog-level |
| 6 | Panina et al. 2024, **PMID 38609948** | Review/functional (drug targeting) | **Competing** | SCP1 enzymatic class | Inhibitors target "small C-terminal domain phosphatase 1 (SCP1)" | Human glioblastoma | Moderate; confirms phosphatase class |
| 7 | UniProt O14595 GO (2026-09-08) | Database (IDA-backed) | **Competing** | True MF of ortholog | **GO:0008420 CTD phosphatase activity, IDA (direct assay)**; GO:0006470 dephosphorylation | Human | High; direct-assay evidence code |
| 8 | UniProt F7A4N8 GO (2026-09-08) | Database | **Refutes (absence)** | Any kinase annotation exists | **No GO terms; "kinase" appears 0×** in the record | Horse | High; shows claim is not DB-derived |
| 9 | InterPro F7A4N8 vs O14595 (2026-09-08) | Structural/evolutionary | **Refutes/qualifies** | Domain content of horse model | F7A4N8 = **no InterPro domains (HTTP 204)**; O14595 = FCP1/HAD phosphatase domains, no kinase | Horse vs human | High; independent domain DB |
| 10 | AlphaFold AF-F7A4N8-F1 v6 (2025-03-31) | Structural (predicted) | **Refutes/qualifies** | Horse model has a folded catalytic domain | Mean pLDDT 46.2 (very low); 66% residues <50, 98% <70; no globular domain | Horse | Moderate-high; prediction, but clearly no fold |

---

## GO Curation Implications

- **GO:0016301 kinase activity — REMOVE / do not annotate.** No sequence, structural, or family evidence
  supports kinase activity for F7A4N8 or the CTDSP2 family. This is a misannotation (a phosphatase gene
  annotated with the mechanistically opposite activity). *(Lead — requires curator verification.)*
- **Better-supported MF (by orthology/family, requires the catalytic domain):**
  `GO:0004721 phosphoprotein phosphatase activity` (or more specific
  `GO:0008420 RNA polymerase II CTD heptapeptide repeat phosphatase activity` /
  `GO:0004725`-adjacent serine/threonine phosphatase), plus `GO:0046872 metal ion (Mg) binding`.
  **Caveat:** these should be transferred to the horse gene with an ISS/orthology qualifier and a note that
  the current F7A4N8 protein model lacks the catalytic domain — the annotation belongs to the *gene*, not
  necessarily to this truncated protein isoform.
- **BP/CC (family-level, orthology):** BP `GO:0006470 protein dephosphorylation` /
  transcription regulation; CC `GO:0005634 nucleus`.
- Avoid "protein binding" as a terminal recommendation — the phosphatase MF is more informative and
  well-supported for the gene.

---

## Mechanistic Scope

- **Immediate molecular function tested:** ATP-dependent phosphotransfer (kinase). **Not supported** — no
  ATP-binding/kinase fold in the sequence.
- **Established family function (direct gene-product activity):** Mg²⁺-dependent HAD-family
  aspartate-nucleophile **phosphatase** that removes phosphate from phospho-Ser substrates (RNA Pol II CTD
  Ser5; REST degron phosphosites). This is a hydrolase reaction, not phosphotransfer.
- **Downstream/phenotypic (not the MF):** transcriptional regulation, REST stabilization, neuronal gene
  silencing, neurogenesis timing — consequences of phosphatase activity, not the activity itself.

---

## Conflicts and Alternatives

- **Reaction-direction confusion (kinase vs phosphatase):** The most likely source of the erroneous
  "kinase activity" term. Both terms concern phosphate, but the gene is a phosphatase. No paralog of CTDSP2
  is a kinase.
- **Truncated/aberrant gene model:** F7A4N8's C-terminus (res 85–174) is Ser/Arg-rich low-complexity and
  diverges from all mammalian CTDSP2 orthologs, which continue into a conserved catalytic domain. This
  looks like an incomplete or frameshifted Ensembl prediction rather than a genuine catalytic-domain-less
  isoform; it warrants caution before transferring *any* enzymatic MF to this specific protein record.
- **Isoform/orthology:** Identity is confirmed as horse CTDSP2 by gene name and VGNC/Ensembl xrefs and by
  the 96% N-terminal match to human CTDSP2 — but the protein model is not full-length.

---

## Knowledge Gaps

| Gap | What was checked | Why it matters | What would resolve it |
|-----|------------------|----------------|-----------------------|
| Is F7A4N8 a real truncated isoform or a mis-prediction? | UniProt features + alignment show divergence at res ~84 and missing catalytic domain | Determines whether *this protein* has any enzymatic MF | Inspect Ensembl gene model / RNA-seq / a corrected full-length horse CTDSP2 transcript |
| Direct horse enzymatic assay | None found | No directly observed horse phosphatase/kinase data exists | In vitro pNPP/CTD-peptide phosphatase assay on full-length horse CTDSP2 |
| Provenance of the kinase GO term | Not in supplied context | Whether it is IEA/ARBA carry-over vs. a specific claim | Trace annotation source & evidence code in the review |

## Discriminating Tests

1. **Retrieve full-length horse CTDSP2** (Ensembl/RefSeq) and re-scan for the DLDET motif and FCP1 domain
   — expected present in the true gene, absent in F7A4N8's current model.
2. **HMM/domain search (Pfam PF03031 "NIF"/FCP1-like) and structure (AlphaFold F7A4N8)** to confirm the
   catalytic core is absent from this model.
3. **Phosphatase activity assay** (para-nitrophenyl phosphate or phospho-CTD peptide) on recombinant
   full-length horse CTDSP2 — positive would confirm phosphatase; a kinase assay (ATP transfer) would be
   negative.

## Curation Leads (require curator verification)

- **Action:** Remove/reject GO:0016301 "kinase activity" for CTDSP2 (F7A4N8) as a misannotation.
- **Replacement MF leads:** `GO:0004721 phosphoprotein phosphatase activity` /
  `GO:0008420 RNA Pol II CTD phosphatase activity`; add `GO:0046872 magnesium ion binding`; BP
  `GO:0006470 protein dephosphorylation`; CC `GO:0005634 nucleus` — all as **orthology (ISS)** with a note
  that the current F7A4N8 model lacks the catalytic domain.
- **Candidate references to verify:** PMID 30217818 (SCP1 phosphatase kinetics + structure), PMID 17403776
  (SCP1 phosphatase in CNS development), PMID 38609948 (SCP1 as a phosphatase drug target); database:
  UniProt O14595 (human CTDSP2, reviewed phosphatase).
- **Suggested question for curator:** Should enzymatic MF terms be attached to the F7A4N8 protein record at
  all, given it is a truncated model missing the catalytic domain — or annotated at the gene level only?

## Limitations

- No directly observed *Equus caballus* biochemical data were found; family/ortholog transfer relies on
  human/mouse SCP paralogs. Motif and alignment analyses are computational. PubMed queries for "SCP2/CTDSP2"
  specifically returned no results; cited evidence is for the closely related paralog SCP1 and the family.


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)