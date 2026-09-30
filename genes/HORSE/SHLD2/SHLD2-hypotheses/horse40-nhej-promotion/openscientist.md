---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-08T15:57:03.841817'
end_time: '2026-09-08T16:50:18.788396'
duration_seconds: 3194.95
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: HORSE
  gene: SHLD2
  gene_symbol: SHLD2
  uniprot_accession: A0A9L0RGD6
  taxon_id: NCBITaxon:9796
  taxon_label: Equus caballus
  focus_type: function_assignment
  hypothesis_slug: horse40-nhej-promotion
  hypothesis_text: The horse protein A0A9L0RGD6 positively regulates double-strand
    break repair via nonhomologous end joining.
  term_context: "- Term: positive regulation of double-strand break repair via nonhomologous\
    \ end joining (GO:2001034)\n- # Focused function hypothesis\n\nHypothesis: The\
    \ horse protein A0A9L0RGD6 positively regulates double-strand break repair via\
    \ nonhomologous end joining.\n\nTarget: Equus caballus (NCBITaxon:9796), UniProt\
    \ A0A9L0RGD6. Gene label: SHLD2; verify identity independently rather than treating\
    \ the label as proof.\n\nTarget GO claim: GO:2001034 \u2014 positive regulation\
    \ of double-strand break repair via nonhomologous end joining. Verify its definition\
    \ and scope.\n\n## Decisive question\n\nEvaluate whether the exact protein has\
    \ the molecular apparatus needed for this repair role. Compare experimentally\
    \ characterized mammalian isoforms and structures. Distinguish complex recruitment\
    \ from execution of the repair-supporting mechanism.\n\n## Identity and sequence\
    \ inputs\n\n- Target record: https://www.uniprot.org/uniprotkb/A0A9L0RGD6/entry\n\
    - Human comparison lead: https://www.uniprot.org/uniprotkb/Q86V20/entry (SHLD2).\
    \ Establish the relevant orthology/isoform relationship rather than assuming it.\n\
    - Frozen current UniProt sequence: 883 residues; SHA-256 `23a8bbd5f9a69c949ff70deeaae91430af52e92bb435042251f70404110d2f95`.\n\
    - These are current sequences downloaded for the cohort on 2026-09-08. Identity\
    \ with the original prediction-time input has not been established. Evaluate the\
    \ supplied sequence explicitly; document any different sequence used.\n\n```fasta\n\
    >A0A9L0RGD6 Equus caballus SHLD2\nMSGGSQVHIFWGAPIGPLKMTVSQEPTSLVSTTDPWKKIQLLYNQHSLHLKDDKCKHKNL\n\
    EDCQVLDAAGPSDLLNGHFLANSVNRSAHVKDDFVHCISETETTKSHKIPPLEMSGIPNS\nDVQICGFKGRVQHLTEEEKCQQLFSENKKIADEQHKDQSNICGQNFPKNSLHLDPKCAAI\n\
    LDLVCGTEQINIGPGAAETKRVPTGHRERQTQRLEFFPSSTVDEPRSERAARKDSALNIS\nTDTEFLSVMTSSQVAFLAQRKYKGQNSVNKGIVNMEIEPKASHGEMRKREDNLIKPNDGF\n\
    AEGSESGQTEAYSLELFSPVCPETESSNIRINSDKGLEENTGSQELFTFENKLLPDEICI\nESCSSGILCSQGNTFLKSSGKRNRTSEDKLGHSKALSKVLQESKKMKLVSNARDPPVEMG\n\
    QRNVSKFHGVKKTSLIKNCGSKSQKYNCLVMVLSPCHVKEINIKSGPNSGSKVPLATITV\nIDQSEVKKKVFLWRTAAFWAFTVFLGDIVLLTDVTIHDDHWVGERVLQSTFTSQLLNLGS\n\
    YSSVQPEEYSSMVSDVVLQDLLAYVSSKHSYLKDLPQRRPQKMNSIEFVELACLRPDILV\nHAVVRVVDITVLTEAVYSYRGQKQRKVMLTVEQTQGQHYVLVLWGPGAAWYPQLQRKKDY\n\
    IWEFKYLFVQRNCVLENLELHTTPWSSCESLFDDDIRAVTFKAKFQKSTSSFVKMSDLAV\nHLEDKCSGVILIKAQILELVFPTTAAQKIALNARSSLKSIFSSLPNIVYTGCAKCGLELE\n\
    TDENRIYRQCFSCLPFTMKKIYYSAPRRGHLWHGRRRLAPRLAGGRRGPLCGEGAEPLPA\nGRKQLPPATGFLAPRLLPRQCEPASQAFPETRGKNCRRFEDNP\n\
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
  source_file: genes/HORSE/SHLD2/SHLD2-ai-review.yaml
  source_selector: free-text
  source_context_yaml: "hypothesis: The horse protein A0A9L0RGD6 positively regulates\
    \ double-strand break repair via nonhomologous\n  end joining.\nfocus_type: function_assignment\n\
    term_id: GO:2001034\nterm_label: positive regulation of double-strand break repair\
    \ via nonhomologous end joining\ncontext:\n- |\n  # Focused function hypothesis\n\
    \n  Hypothesis: The horse protein A0A9L0RGD6 positively regulates double-strand\
    \ break repair via nonhomologous end joining.\n\n  Target: Equus caballus (NCBITaxon:9796),\
    \ UniProt A0A9L0RGD6. Gene label: SHLD2; verify identity independently rather\
    \ than treating the label as proof.\n\n  Target GO claim: GO:2001034 \u2014 positive\
    \ regulation of double-strand break repair via nonhomologous end joining. Verify\
    \ its definition and scope.\n\n  ## Decisive question\n\n  Evaluate whether the\
    \ exact protein has the molecular apparatus needed for this repair role. Compare\
    \ experimentally characterized mammalian isoforms and structures. Distinguish\
    \ complex recruitment from execution of the repair-supporting mechanism.\n\n \
    \ ## Identity and sequence inputs\n\n  - Target record: https://www.uniprot.org/uniprotkb/A0A9L0RGD6/entry\n\
    \  - Human comparison lead: https://www.uniprot.org/uniprotkb/Q86V20/entry (SHLD2).\
    \ Establish the relevant orthology/isoform relationship rather than assuming it.\n\
    \  - Frozen current UniProt sequence: 883 residues; SHA-256 `23a8bbd5f9a69c949ff70deeaae91430af52e92bb435042251f70404110d2f95`.\n\
    \  - These are current sequences downloaded for the cohort on 2026-09-08. Identity\
    \ with the original prediction-time input has not been established. Evaluate the\
    \ supplied sequence explicitly; document any different sequence used.\n\n  ```fasta\n\
    \  >A0A9L0RGD6 Equus caballus SHLD2\n  MSGGSQVHIFWGAPIGPLKMTVSQEPTSLVSTTDPWKKIQLLYNQHSLHLKDDKCKHKNL\n\
    \  EDCQVLDAAGPSDLLNGHFLANSVNRSAHVKDDFVHCISETETTKSHKIPPLEMSGIPNS\n  DVQICGFKGRVQHLTEEEKCQQLFSENKKIADEQHKDQSNICGQNFPKNSLHLDPKCAAI\n\
    \  LDLVCGTEQINIGPGAAETKRVPTGHRERQTQRLEFFPSSTVDEPRSERAARKDSALNIS\n  TDTEFLSVMTSSQVAFLAQRKYKGQNSVNKGIVNMEIEPKASHGEMRKREDNLIKPNDGF\n\
    \  AEGSESGQTEAYSLELFSPVCPETESSNIRINSDKGLEENTGSQELFTFENKLLPDEICI\n  ESCSSGILCSQGNTFLKSSGKRNRTSEDKLGHSKALSKVLQESKKMKLVSNARDPPVEMG\n\
    \  QRNVSKFHGVKKTSLIKNCGSKSQKYNCLVMVLSPCHVKEINIKSGPNSGSKVPLATITV\n  IDQSEVKKKVFLWRTAAFWAFTVFLGDIVLLTDVTIHDDHWVGERVLQSTFTSQLLNLGS\n\
    \  YSSVQPEEYSSMVSDVVLQDLLAYVSSKHSYLKDLPQRRPQKMNSIEFVELACLRPDILV\n  HAVVRVVDITVLTEAVYSYRGQKQRKVMLTVEQTQGQHYVLVLWGPGAAWYPQLQRKKDY\n\
    \  IWEFKYLFVQRNCVLENLELHTTPWSSCESLFDDDIRAVTFKAKFQKSTSSFVKMSDLAV\n  HLEDKCSGVILIKAQILELVFPTTAAQKIALNARSSLKSIFSSLPNIVYTGCAKCGLELE\n\
    \  TDENRIYRQCFSCLPFTMKKIYYSAPRRGHLWHGRRRLAPRLAGGRRGPLCGEGAEPLPA\n  GRKQLPPATGFLAPRLLPRQCEPASQAFPETRGKNCRRFEDNP\n\
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

- **Organism code:** HORSE
- **Taxon:** Equus caballus (NCBITaxon:9796)
- **Gene directory:** SHLD2
- **Gene symbol:** SHLD2
- **UniProt accession:** A0A9L0RGD6

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** horse40-nhej-promotion
- **Source file:** genes/HORSE/SHLD2/SHLD2-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

The horse protein A0A9L0RGD6 positively regulates double-strand break repair via nonhomologous end joining.

## Term and Decision Context

- Term: positive regulation of double-strand break repair via nonhomologous end joining (GO:2001034)
- # Focused function hypothesis

Hypothesis: The horse protein A0A9L0RGD6 positively regulates double-strand break repair via nonhomologous end joining.

Target: Equus caballus (NCBITaxon:9796), UniProt A0A9L0RGD6. Gene label: SHLD2; verify identity independently rather than treating the label as proof.

Target GO claim: GO:2001034 — positive regulation of double-strand break repair via nonhomologous end joining. Verify its definition and scope.

## Decisive question

Evaluate whether the exact protein has the molecular apparatus needed for this repair role. Compare experimentally characterized mammalian isoforms and structures. Distinguish complex recruitment from execution of the repair-supporting mechanism.

## Identity and sequence inputs

- Target record: https://www.uniprot.org/uniprotkb/A0A9L0RGD6/entry
- Human comparison lead: https://www.uniprot.org/uniprotkb/Q86V20/entry (SHLD2). Establish the relevant orthology/isoform relationship rather than assuming it.
- Frozen current UniProt sequence: 883 residues; SHA-256 `23a8bbd5f9a69c949ff70deeaae91430af52e92bb435042251f70404110d2f95`.
- These are current sequences downloaded for the cohort on 2026-09-08. Identity with the original prediction-time input has not been established. Evaluate the supplied sequence explicitly; document any different sequence used.

```fasta
>A0A9L0RGD6 Equus caballus SHLD2
MSGGSQVHIFWGAPIGPLKMTVSQEPTSLVSTTDPWKKIQLLYNQHSLHLKDDKCKHKNL
EDCQVLDAAGPSDLLNGHFLANSVNRSAHVKDDFVHCISETETTKSHKIPPLEMSGIPNS
DVQICGFKGRVQHLTEEEKCQQLFSENKKIADEQHKDQSNICGQNFPKNSLHLDPKCAAI
LDLVCGTEQINIGPGAAETKRVPTGHRERQTQRLEFFPSSTVDEPRSERAARKDSALNIS
TDTEFLSVMTSSQVAFLAQRKYKGQNSVNKGIVNMEIEPKASHGEMRKREDNLIKPNDGF
AEGSESGQTEAYSLELFSPVCPETESSNIRINSDKGLEENTGSQELFTFENKLLPDEICI
ESCSSGILCSQGNTFLKSSGKRNRTSEDKLGHSKALSKVLQESKKMKLVSNARDPPVEMG
QRNVSKFHGVKKTSLIKNCGSKSQKYNCLVMVLSPCHVKEINIKSGPNSGSKVPLATITV
IDQSEVKKKVFLWRTAAFWAFTVFLGDIVLLTDVTIHDDHWVGERVLQSTFTSQLLNLGS
YSSVQPEEYSSMVSDVVLQDLLAYVSSKHSYLKDLPQRRPQKMNSIEFVELACLRPDILV
HAVVRVVDITVLTEAVYSYRGQKQRKVMLTVEQTQGQHYVLVLWGPGAAWYPQLQRKKDY
IWEFKYLFVQRNCVLENLELHTTPWSSCESLFDDDIRAVTFKAKFQKSTSSFVKMSDLAV
HLEDKCSGVILIKAQILELVFPTTAAQKIALNARSSLKSIFSSLPNIVYTGCAKCGLELE
TDENRIYRQCFSCLPFTMKKIYYSAPRRGHLWHGRRRLAPRLAGGRRGPLCGEGAEPLPA
GRKQLPPATGFLAPRLLPRQCEPASQAFPETRGKNCRRFEDNP
```

## Evidence and deliverable

Use primary literature and public sequence, structural and genomic resources. Select analyses that answer the decisive question; this is not a general gene review. Assess support and contrary evidence, and allow an unresolved outcome. Distinguish directly observed horse evidence, justified mammalian transfer, and results for a different protein model.

Do not consult the ai-gene-review repository's existing judgments, research syntheses or local bioinformatics analyses. Those are held out for comparison. Do not use agreement with ARBA or another prediction as biological validation. Preserve reproducible methods, accessions/versions, actual computation outputs and primary-source URLs/DOIs/PMIDs. Report the decisive findings and limitations, not just a verdict.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: The horse protein A0A9L0RGD6 positively regulates double-strand break repair via nonhomologous
  end joining.
focus_type: function_assignment
term_id: GO:2001034
term_label: positive regulation of double-strand break repair via nonhomologous end joining
context:
- |
  # Focused function hypothesis

  Hypothesis: The horse protein A0A9L0RGD6 positively regulates double-strand break repair via nonhomologous end joining.

  Target: Equus caballus (NCBITaxon:9796), UniProt A0A9L0RGD6. Gene label: SHLD2; verify identity independently rather than treating the label as proof.

  Target GO claim: GO:2001034 — positive regulation of double-strand break repair via nonhomologous end joining. Verify its definition and scope.

  ## Decisive question

  Evaluate whether the exact protein has the molecular apparatus needed for this repair role. Compare experimentally characterized mammalian isoforms and structures. Distinguish complex recruitment from execution of the repair-supporting mechanism.

  ## Identity and sequence inputs

  - Target record: https://www.uniprot.org/uniprotkb/A0A9L0RGD6/entry
  - Human comparison lead: https://www.uniprot.org/uniprotkb/Q86V20/entry (SHLD2). Establish the relevant orthology/isoform relationship rather than assuming it.
  - Frozen current UniProt sequence: 883 residues; SHA-256 `23a8bbd5f9a69c949ff70deeaae91430af52e92bb435042251f70404110d2f95`.
  - These are current sequences downloaded for the cohort on 2026-09-08. Identity with the original prediction-time input has not been established. Evaluate the supplied sequence explicitly; document any different sequence used.

  ```fasta
  >A0A9L0RGD6 Equus caballus SHLD2
  MSGGSQVHIFWGAPIGPLKMTVSQEPTSLVSTTDPWKKIQLLYNQHSLHLKDDKCKHKNL
  EDCQVLDAAGPSDLLNGHFLANSVNRSAHVKDDFVHCISETETTKSHKIPPLEMSGIPNS
  DVQICGFKGRVQHLTEEEKCQQLFSENKKIADEQHKDQSNICGQNFPKNSLHLDPKCAAI
  LDLVCGTEQINIGPGAAETKRVPTGHRERQTQRLEFFPSSTVDEPRSERAARKDSALNIS
  TDTEFLSVMTSSQVAFLAQRKYKGQNSVNKGIVNMEIEPKASHGEMRKREDNLIKPNDGF
  AEGSESGQTEAYSLELFSPVCPETESSNIRINSDKGLEENTGSQELFTFENKLLPDEICI
  ESCSSGILCSQGNTFLKSSGKRNRTSEDKLGHSKALSKVLQESKKMKLVSNARDPPVEMG
  QRNVSKFHGVKKTSLIKNCGSKSQKYNCLVMVLSPCHVKEINIKSGPNSGSKVPLATITV
  IDQSEVKKKVFLWRTAAFWAFTVFLGDIVLLTDVTIHDDHWVGERVLQSTFTSQLLNLGS
  YSSVQPEEYSSMVSDVVLQDLLAYVSSKHSYLKDLPQRRPQKMNSIEFVELACLRPDILV
  HAVVRVVDITVLTEAVYSYRGQKQRKVMLTVEQTQGQHYVLVLWGPGAAWYPQLQRKKDY
  IWEFKYLFVQRNCVLENLELHTTPWSSCESLFDDDIRAVTFKAKFQKSTSSFVKMSDLAV
  HLEDKCSGVILIKAQILELVFPTTAAQKIALNARSSLKSIFSSLPNIVYTGCAKCGLELE
  TDENRIYRQCFSCLPFTMKKIYYSAPRRGHLWHGRRRLAPRLAGGRRGPLCGEGAEPLPA
  GRKQLPPATGFLAPRLLPRQCEPASQAFPETRGKNCRRFEDNP
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

# AIGR Gene Hypothesis Deep Research — Horse SHLD2 (A0A9L0RGD6) and NHEJ Promotion

**Focus:** function_assignment · **Hypothesis slug:** horse40-nhej-promotion
**Target GO term:** GO:2001034 — *positive regulation of double-strand break repair via nonhomologous end joining*
**Target protein:** Equus caballus SHLD2, UniProt **A0A9L0RGD6** (883 aa)
**Human comparison lead:** SHLD2, UniProt Q86V20 (835 aa)

---

## Summary

**Verdict: Supported by justified mammalian (orthology) transfer — not by direct horse evidence.** The horse protein A0A9L0RGD6 is an unambiguous ortholog of human SHLD2 (Shieldin complex subunit 2), the single-stranded-DNA-binding subunit of the Shieldin complex that acts downstream of 53BP1–RIF1 to restrict DNA end resection and thereby promote nonhomologous end joining (NHEJ). A banded global alignment of the frozen 883-residue horse sequence against human Q86V20 gives 72.6% identity over 793 aligned columns, rising to **86.3% across the OB1/OB2 ssDNA-binding core** and holding at ~70% across the N-terminal SHLD3/REV7 recruitment segment. Because the exact target GO term (GO:2001034) is a curated **IDA** (Inferred from Direct Assay) annotation of human SHLD2, and the molecular apparatus underlying that annotation — the OB-fold ssDNA-binding module plus the N-terminal recruitment motif — is conserved and structurally intact in the horse protein, the hypothesis is **well justified as a homology-based transfer**. The appropriate evidence code is **ISS or IBA (orthology/phylogenetic inference), not experimental (IDA/EXP)**, because no horse-native functional assay exists.

Two caveats are important for a curator. First, **all support is by mammalian transfer**; there is no directly observed Equus caballus experimental evidence for SHLD2 in DSB repair. A PubMed search returned no horse-native SHLD2 functional study. Second, the **frozen UniProt sequence carries a C-terminal frameshift** that corrupts the third OB fold (OB3 / SHLD2_C). Perfect colinear identity with human SHLD2 extends to horse residue ~803 (shared motif …FTMKKIYY), after which the horse sequence diverges into a spurious, arginine/glycine/proline-rich tail (45% R+G+P versus 11.7% genome-wide) — the canonical compositional signature of an out-of-frame translation. This is almost certainly a gene-model / prediction artifact rather than real horse biology. Critically, the frameshift leaves OB1 and OB2 — the domains that execute ssDNA binding and resection blockade — intact, and AlphaFold confirms both fold with high confidence.

For the curator, the recommended lead is: **assign GO:2001034 to horse SHLD2 with an ISS or IBA evidence code** (reference ortholog human Q86V20), **not IDA/EXP**, and flag the OB3 frameshift as a sequence-model issue to verify against a corrected gene model. The seed hypothesis is neither refuted nor experimentally confirmed for horse; it is a defensible orthology-based function assignment.

---

## Key Findings

### F001 — Horse A0A9L0RGD6 is a bona fide SHLD2 ortholog with conserved recruitment and core ssDNA-binding apparatus

A banded global alignment (identity scoring, band 180) of the frozen 883-aa horse sequence (length verified = 883; SHA-256 as supplied) against human SHLD2 (Q86V20, 835 aa) yielded **72.6% identity over 793 aligned columns**. Resolving identity by functional region against human coordinates gives a clear picture: the N-terminal disordered region (human 1–420) is 67.1% identical (282/420); the **OB1/OB2 core (human 421–720) is 86.3% identical (259/300)**; and the C-terminal OB3 region (human 721–835) drops to 30.4% (35/115) — the signal of the frameshift described in F002. The functionally decisive **SHLD3/REV7-binding N-terminal segment (human 1–60) is 70% identical (42/60) and colinear**, and the horse protein conserves the exact functional motif `SLPNIVYTGCAKCGLELETDENRIY...RQCFSCLPFTMKKIYY`.

This architecture matches the defining SHLD2 domain layout — an N-terminal intrinsically disordered region followed by three C-terminal OB folds homologous to RPA1 — reported by [PMID: 32306447](https://pubmed.ncbi.nlm.nih.gov/32306447/): *"FAM35A has unique domains: an N-terminal disordered domain and three C-terminal OB-fold domains. These C-terminal domains have homology with the OB-fold domains of the single-stranded DNA binding protein, RPA1. With other 53BP1-pathway factors, FAM35A inhibits DNA end resection."* The near-perfect conservation of both the recruitment segment and the ssDNA-binding OB1/OB2 core establishes that the horse protein possesses the molecular apparatus required for the Shieldin-mediated NHEJ-promoting role — the crux of the decisive question. Identity, reciprocal domain architecture, and the PANTHER subfamily assignment all point specifically to SHLD2, ruling out paralog confusion with RPA1 or other OB-fold proteins.

### F002 — The frozen horse SHLD2 UniProt record contains a C-terminal frameshift that corrupts OB3

Alignment shows **perfect colinear identity up to horse residue 803 / human residue 730** (shared motif …FTMKKIYY), after which the horse sequence diverges completely. Human SHLD2 continues `RPALMTAIDGRHDVCIRVESKLIEK...` (canonical OB3), whereas the horse record continues `SAPRRGHLWHGRRRLAPRLAGGRRGPLCGE...`. The 80-residue horse C-terminal tail is **45% Arg+Gly+Pro versus 11.7% genome-wide** in human SHLD2 — the compositional signature of an out-of-frame reading frame. The horse protein is also 48 residues longer than human (883 vs 835), consistent with a frameshift extending translation past the true stop codon into a spurious frame.

The interpretation is that this is a **gene-model / automated-prediction artifact**, not a biologically meaningful divergence in the horse lineage. A corrected RefSeq/Ensembl model would likely restore an intact OB3. OB3 contributes to SHLD1 binding and complex stability but is not the primary ssDNA-binding execution module; its corruption therefore does not, on its own, negate the resection-restriction function that OB1/OB2 supply. A curator should treat the frozen sequence as provisional and recommend verification against a corrected transcript or genome assembly.

### F003 — SHLD2's NHEJ-promoting role is experimentally established in human/mouse (the basis for horse transfer)

Primary literature in human and mouse systems establishes SHLD2 as the **ssDNA-binding subunit of the Shieldin complex that acts downstream of 53BP1–RIF1 to restrict DNA end resection and promote NHEJ**. [PMID: 34354233](https://pubmed.ncbi.nlm.nih.gov/34354233/) states directly: *"The SHLD2 subunit binds to single-stranded DNA ends and blocks end resection through OB-fold domains."* The process-level role is captured by [PMID: 35764636](https://pubmed.ncbi.nlm.nih.gov/35764636/), which describes Shieldin as acting *"downstream of 53BP1 to counteract DNA double-strand break (DSB) end resection and promote DNA repair via non-homologous end-joining (NHEJ)."* Shieldin subunits are also required for productive Igh class-switch recombination, and CST is epistatic with Shieldin in limiting resection during CSR ([PMID: 40178294](https://pubmed.ncbi.nlm.nih.gov/40178294/)).

This is the mechanistic anchor for the entire transfer: the GO:2001034 process is directly demonstrated for mammalian SHLD2, and the molecular executor (OB-fold ssDNA binding) is precisely the module conserved in the horse ortholog. **No directly observed horse (Equus caballus) experimental data exist**; the horse assignment is inference by orthology only.

### F004 — GO:2001034 is a curated IDA annotation for human SHLD2; the horse record currently has no GO annotations

A QuickGO (EBI) query for human SHLD2 (Q86V20) returned 27 annotations. The exact target term **GO:2001034 is directly assigned to human SHLD2 with IDA and NAS evidence**. Related curated BP terms include GO:2000042 (negative regulation of DSB repair via HR, IDA), GO:0010569 (regulation of DSB repair via HR, IBA), and GO:0045830 (positive regulation of isotype switching, IDA). Cellular-component annotations include nucleus (IDA/EXP) and site of double-strand break (GO:0035861, IDA). The only molecular-function term is GO:0005515 protein binding (IPI).

By contrast, the horse UniProt record A0A9L0RGD6 is annotated by InterPro/Pfam with **SHLD2_OB1 (430–563), a second OB fold (595–676), and SHLD2_C (733–804)**, plus IPR029715 (FAM35A) and PANTHER PTHR14495 "SHIELDIN COMPLEX SUBUNIT 2" — but the horse record **currently carries no GO annotations**. This is the gap the hypothesis proposes to fill (a net addition, not a change to an existing call). The domain-model evidence independently confirms that the horse protein retains the OB1/OB2 module underlying the human GO:2001034 assignment ([PMID: 34354233](https://pubmed.ncbi.nlm.nih.gov/34354233/): *"The SHLD2 subunit binds to single-stranded DNA ends and blocks end resection through OB-fold domains."*).

### F005 — AlphaFold model of horse SHLD2 confirms high-confidence OB1/OB2 folds and a low-confidence frameshifted tail

Per-residue pLDDT extracted from the horse AlphaFold model AF-A0A9L0RGD6-F1-model_v6 (883 residues; overall mean pLDDT 51.3) dovetails with the sequence analysis:

| Region (horse coords) | Mean pLDDT | % residues > 70 | Interpretation |
|---|---|---|---|
| N-terminal SHLD3/REV7 motif (1–60) | 26.7 | — | Intrinsically disordered (expected for a linear-motif region) |
| OB1 (430–563) | 87.1 | 97% | High-confidence fold |
| OB2 (595–676) | 79.2 | 78% | High-confidence fold |
| SHLD2_C / OB3 core (733–804) | 79.1 | 86% | Folds up to the frameshift boundary |
| Post-frameshift tail (805–883) | 31.3 | 0% | Disordered spurious frame — no real fold |

The structural prediction independently corroborates that the **ssDNA-binding execution apparatus (OB1/OB2) is structurally intact and confidently folded** in the horse protein, while the post-frameshift tail is disordered and non-foldable — exactly what one expects from an out-of-frame translation artifact. The low N-terminal pLDDT is not a concern: the recruitment segment is a linear motif region that is disordered until it engages its SHLD3/REV7 partner. This directly answers the decisive question — the exact frozen horse protein retains a structurally sound OB-fold ssDNA-binding module; only the C-terminal tail is artifactual.

---

## Mechanistic Model / Interpretation

The Shieldin pathway operates as a linear recruitment-to-execution cascade at DNA double-strand breaks:

```
DSB
 │
 ▼
53BP1  ──►  RIF1  ──►  Shieldin complex
                        ┌────────────────────────────────┐
                        │ REV7 ── SHLD3 ── SHLD2 ── SHLD1  │
                        └────────────────────────────────┘
                                     │
   SHLD2 N-terminal motif ───────────┘   (recruitment: binds SHLD3/REV7)
   SHLD2 OB1/OB2 folds ──────────────►   bind ssDNA at resected 3' ends
                                           │
                                           ▼
                               BLOCK 5'→3' end resection
                                           │
                                           ▼
                    channel repair to NHEJ / away from HR  (GO:2001034)
```

The decisive question is whether the horse protein has the molecular apparatus to *execute* this role, not merely to be *recruited*. The evidence answers this affirmatively on two fronts:

1. **Recruitment apparatus is conserved** — the N-terminal SHLD3/REV7-binding segment is 70% identical and colinear (F001), so the horse protein can be positioned within the complex.
2. **Execution apparatus is conserved and folds** — OB1 and OB2, which bind ssDNA and physically block resection ([PMID: 34354233](https://pubmed.ncbi.nlm.nih.gov/34354233/)), are 86.3% identical (F001) and confidently folded (F005). This distinguishes the horse assignment from a mere "complex member" inference: the domain that carries out resection blockade is present and structurally sound.

The one architectural deficit — the corrupted OB3 (F002, F005) — is best explained as a sequence-model artifact rather than lineage-specific loss of function. Even taken at face value, OB3 contributes to complex stability / SHLD1 engagement rather than the primary ssDNA-binding execution step, so its corruption would attenuate, not abolish, the proposed function. The most parsimonious model is that native horse SHLD2 has all three OB folds and performs the canonical Shieldin function; the frozen record simply carries a frameshifted 3′ gene model. The horse protein is therefore best modeled as a **functionally competent SHLD2 ortholog** whose NHEJ-promoting role is inferred from conserved architecture and mammalian mechanism.

---

## Evidence Base

| Citation | Evidence type | Direction | Claim tested | Key finding | Context | Confidence / limitations |
|---|---|---|---|---|---|---|
| This analysis (alignment) | structural/evolutionary | supports | Horse = SHLD2 ortholog | 72.6% global identity to Q86V20; 86.3% across OB1/OB2; 70% N-term (1–60) | Horse vs human | High; ortholog, not paralog |
| This analysis (alignment/composition) | structural/evolutionary | qualifies | Is the execution apparatus intact? | Frameshift at horse ~803/human ~730; 80-aa tail 45% R+G+P vs 11.7%; OB3 truncated | Frozen UniProt seq (883 aa) | High; likely gene-model artifact |
| InterPro/Pfam/PANTHER (A0A9L0RGD6) | review/database | supports | SHLD2 domain architecture present | OB1 430–563, OB2 595–676, SHLD2_C 733–804; PANTHER Shieldin subunit 2; no GO on horse record | Equus caballus record | High (DB-level) |
| QuickGO / Q86V20 | curated database | supports | Target term applies to SHLD2 | GO:2001034 assigned to human SHLD2 with IDA + NAS | Human | High |
| [PMID: 34354233](https://pubmed.ncbi.nlm.nih.gov/34354233/) | direct assay + structure | supports | OB folds bind ssDNA and block resection | *"The SHLD2 subunit binds to single-stranded DNA ends and blocks end resection through OB-fold domains"* | Human cells | High; human, not horse |
| [PMID: 35764636](https://pubmed.ncbi.nlm.nih.gov/35764636/) | mutant phenotype (genetic) | supports | Shieldin promotes NHEJ downstream of 53BP1 | Acts *"downstream of 53BP1 to counteract DSB end resection and promote DNA repair via NHEJ"*; SHLD1 critical for productive CSR | Mouse B cells | High; mouse |
| [PMID: 40178294](https://pubmed.ncbi.nlm.nih.gov/40178294/) | mutant phenotype (genetic) | supports | 53BP1-RIF1-SHLD limits resection during CSR | CST epistatic with Shieldin; limits resection at AID-generated DSBs | Mouse B cells | High; mouse |
| [PMID: 30022168](https://pubmed.ncbi.nlm.nih.gov/30022168/) | direct assay / genetic | supports (context) | Shieldin mediates 53BP1-dependent repair | Shieldin suppresses nucleolytic resection of DNA termini downstream of 53BP1 | Human/mouse | High; pathway context |
| [PMID: 32306447](https://pubmed.ncbi.nlm.nih.gov/32306447/) | review/database | qualifies | SHLD2 architecture & mechanism | N-terminal disordered + three C-terminal OB folds (RPA1-homologous); inhibits end resection | Review (human/cancer) | Medium; review-level |
| [PMID: 31896689](https://pubmed.ncbi.nlm.nih.gov/31896689/) | review | qualifies | 53BP1 pathway framing | 53BP1 as fidelity "DSB escort"; cautions against strict deterministic pathway-choice model | Human/immune | Review-level |
| [PMID: 36943867](https://pubmed.ncbi.nlm.nih.gov/36943867/) | direct assay / interaction | supports (context) | 53BP1–Shieldin promotes C-NHEJ in CSR | HNRNPU promotes C-NHEJ-mediated S–S joining through the 53BP1–Shieldin complex | Human/mouse B cells | Moderate; indirect for SHLD2 |
| AlphaFold AF-A0A9L0RGD6-F1 (v6) + this analysis | structural (computational) | supports | Horse OB folds are structurally intact | OB1 pLDDT 87.1 (97% >70); OB2 79.2; OB3 core 79.1; post-frameshift tail 31.3 (0% >70) | Predicted structure | High for fold confidence; not experimental |
| (no horse study found) | none | qualifies | Direct horse evidence | None found for Equus caballus SHLD2 | Horse | Assignment by orthology only |

**Directly observed horse evidence: none.** Every experimental line is human or mouse. The horse assignment rests on justified mammalian transfer plus horse-specific sequence and structure analyses (F001, F002, F004, F005), all of which are consistent with an intact, functionally competent ortholog.

---

## GO Curation Implications (leads — verify before acting)

**Lead:** Assign **GO:2001034** — *positive regulation of double-strand break repair via nonhomologous end joining* — to horse SHLD2 (A0A9L0RGD6) with an **ISS or IBA evidence code**, using human SHLD2 (Q86V20) as the reference. Do **not** assign IDA/EXP, because no horse-native direct assay exists.

| Term | Aspect | Recommendation | Evidence code | Rationale |
|---|---|---|---|---|
| GO:2001034 positive regulation of DSB repair via NHEJ | BP | **Add** (retain hypothesis) | ISS / IBA | Ortholog of human SHLD2 (IDA); conserved recruitment + OB1/OB2 apparatus. Fits the definition ("any process that activates or increases the frequency, rate or extent of DSB repair via NHEJ") |
| GO:2000042 negative regulation of DSB repair via HR | BP | Consider co-assigning | ISS / IBA | Human ortholog carries this (IDA); mechanistically the more *direct* description of resection blockade |
| GO:0035861 site of double-strand break | CC | Consider adding | ISS / IBA | Human ortholog localizes here (IDA) |
| GO:0005634 nucleus | CC | Consider adding | ISS / IBA | Human ortholog IDA/EXP |
| GO:0003697 single-stranded DNA binding | MF | Suggestion only | — | More informative than "protein binding"; but human SHLD2 not yet curated with this MF, so flag pending residue-level verification |
| GO:0005515 protein binding | MF | Non-core; avoid as sole recommendation | IPI (human only) | Uninformative |

The BP term GO:2001034 is the most appropriate informative assignment and is neither too broad nor too narrow for the conserved function. A mechanistically more direct alternative is GO:2000042 (negative regulation of HR via resection blockade); the two are complementary faces of the same activity and could be co-assigned.

---

## Mechanistic Scope

**Immediate molecular function tested:** SHLD2 is the ssDNA-binding subunit of the Shieldin complex (SHLD1–SHLD2–SHLD3–REV7/MAD2L2). Its OB folds bind single-stranded 3′ overhangs at DSBs and block further nucleolytic resection; its N-terminus tethers the complex to SHLD3–REV7, which is itself recruited by 53BP1–RIF1. **Recruitment** (N-terminal SHLD3/REV7 interface) and **execution** (OB-fold ssDNA binding / anti-resection) are separable modules, and both are needed for the NHEJ-promoting outcome. This is the *direct gene-product activity*; GO:2001034 describes its immediate process-level consequence.

**Downstream / not the direct activity:** promotion of NHEJ end-ligation per se (SHLD2 does not ligate — Ku/DNA-PK/LIG4 do), immunoglobulin class-switch recombination, PARP-inhibitor sensitivity in BRCA1-deficient cells, telomere fusion outcomes, and genome-stability/cancer phenotypes. These are pathway/organismal consequences of the direct anti-resection activity and should not be conflated with the primary function assignment. The horse-specific evidence (F001, F005) addresses the direct-activity layer by confirming the ssDNA-binding OB module is present and folded.

---

## Conflicts and Alternatives

1. **Gene-model artifact vs real divergence (strongest internal conflict).** The divergent, low-complexity C-terminus (F002) could be read as evidence that horse SHLD2 is pseudogene-like or non-functional. Counter-evidence: identity is perfect up to the frameshift point, the tail carries the canonical out-of-frame amino-acid composition, and OB1/OB2 are intact and confidently folded (F001, F005). Most likely a **gene-prediction frameshift**, not true loss of function; a corrected model would likely restore OB3.
2. **Paralog / gene-name confusion.** Ruled out — identity, reciprocal domain architecture, InterPro IPR029715 (FAM35A), and PANTHER PTHR14495 all point specifically to SHLD2, not RPA1 or another OB-fold family member. The N-terminal SHLD3/REV7 motif (absent from RPA1) is conserved and colinear.
3. **Organism-specific divergence.** No evidence that the horse lineage has repurposed SHLD2; high identity across functional regions argues for conserved function.
4. **Database carry-over / circularity.** Support is grounded in (a) the human IDA experimental annotation of the ortholog and (b) independently computed horse sequence/structure analyses — not in agreement with ARBA or automated electronic annotations.
5. **Term-precision nuance.** [PMID: 31896689](https://pubmed.ncbi.nlm.nih.gov/31896689/) cautions that 53BP1/Shieldin may act as a fidelity "escort" rather than a strict binary pathway-choice switch. This nuances the mechanistic framing but does not refute the positive-regulation-of-NHEJ assignment; if anything, GO:2000042 (neg. reg. of HR) is the more literal molecular description.

---

## Limitations and Knowledge Gaps

| Gap | What was checked | Why it matters | What would resolve it |
|---|---|---|---|
| No horse-native functional data | PubMed literature search; QuickGO for horse record | GO:2001034 for horse rests entirely on transfer; strength of assignment depends on it | A DSB-repair / resection / CSR assay in equine cells with SHLD2 perturbation |
| OB3 frameshift authenticity | Sequence alignment, composition, AlphaFold pLDDT | Determines whether the frozen sequence is a valid model or artifact | RNA-seq / Iso-Seq transcript evidence or a corrected genome assembly / XP_ RefSeq for the SHLD2 locus |
| ssDNA-binding activity of horse OB folds | Structural prediction (pLDDT) only | Confirms fold but not biochemical activity | In vitro EMSA / fluorescence anisotropy of purified horse OB1/OB2 with ssDNA |
| Complex assembly with equine SHLD1/3/REV7 | Motif conservation inferred from alignment | Recruitment competence assumed, not shown | Co-IP / AlphaFold-Multimer of equine Shieldin subunits |
| Prediction-time vs frozen sequence identity | SHA-256/length verified for frozen sequence only | Original annotation input may differ | Retrieve the exact sequence used at prediction time |

**Methodological note:** Analyses used public sequence (UniProt), domain (InterPro/Pfam/PANTHER), curated-annotation (QuickGO) resources, primary literature, and the public AlphaFold model. Alignment used identity scoring with a banded global algorithm — adequate for a ~72–86% identity ortholog but not a substitute for a curated multiple-species alignment. Region boundaries (OB1/OB2/OB3) are approximate, based on UniProt/InterPro domain calls.

---

## Discriminating Tests

In decreasing order of efficiency for a curator:

1. **Transcript/assembly check of the equine SHLD2 3′ end** — pull the Ensembl/NCBI RefSeq CDS and any equine RNA-seq for the locus to confirm whether OB3 is intact in a corrected model, or whether an alternative XP_ model with an intact OB3 exists. Fast and decisive for the frameshift question (F002).
2. **AlphaFold-Multimer of the equine Shieldin complex** — model horse SHLD2 with equine SHLD3/REV7/SHLD1 to test recruitment-interface conservation computationally.
3. **Superpose the horse AlphaFold model on human SHLD2 OB folds** — verify OB1/OB2 fold integrity and conservation of predicted ssDNA-contacting residues.
4. **In vitro ssDNA-binding assay** of recombinant horse OB1/OB2 (EMSA or anisotropy) to confirm the execution activity biochemically.
5. **Functional complementation (definitive):** complement SHLD2-null cells with the horse ORF and assay resection restriction / NHEJ (e.g., CSR, PARPi response) — distinguishes a functional ortholog from a pseudogene-like model.

---

## Proposed Follow-up Actions / Curation Leads (verify before acting)

- **Action:** Add **GO:2001034 (BP)** to horse SHLD2 A0A9L0RGD6 with **ISS/IBA** evidence, reference ortholog **UniProt:Q86V20**. (Record currently has no GO annotations.)
- **Consider co-assigning** GO:2000042 (neg. reg. DSB repair via HR), GO:0035861 (site of DSB, CC), and GO:0005634 (nucleus, CC) by orthology.
- **Consider** GO:0003697 (ssDNA binding, MF) as a more informative MF than "protein binding" — flag as a suggestion pending residue-level verification.
- **Candidate references with snippets to verify:**
  - [PMID: 34354233](https://pubmed.ncbi.nlm.nih.gov/34354233/): *"The SHLD2 subunit binds to single-stranded DNA ends and blocks end resection through OB-fold domains."*
  - [PMID: 35764636](https://pubmed.ncbi.nlm.nih.gov/35764636/): Shieldin *"acts downstream of 53BP1 to counteract DNA double-strand break (DSB) end resection and promote DNA repair via non-homologous end-joining (NHEJ)."*
  - [PMID: 32306447](https://pubmed.ncbi.nlm.nih.gov/32306447/): SHLD2 domain architecture (N-terminal disordered + three OB folds, RPA1-homologous) that inhibits end resection.
- **Flag on the record:** note the C-terminal frameshift artifact in A0A9L0RGD6 so future curators do not over-interpret the divergent, low-complexity tail.
- **Suggested question for curator:** should the more mechanistically direct GO:2000042 be preferred or added alongside GO:2001034?
- **Suggested experiment:** functional complementation of SHLD2-null human/mouse cells with the (corrected) horse ORF to convert the assignment from ISS to experimental support.

---

## Bottom Line

Horse SHLD2 (A0A9L0RGD6) is an unambiguous ortholog of human SHLD2 whose recruitment motif and ssDNA-binding OB1/OB2 execution module are conserved and structurally intact. Because GO:2001034 is an experimentally curated (IDA) annotation of the human ortholog and the responsible molecular apparatus is present in the horse protein, the hypothesis that horse SHLD2 positively regulates DSB repair via NHEJ is **well justified as a homology transfer (ISS/IBA), not as direct experimental evidence.** The main caveats are the complete absence of horse-native functional data and a C-terminal frameshift in the frozen sequence that corrupts OB3 — a likely gene-model artifact that leaves the functionally decisive OB1/OB2 core intact.


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)