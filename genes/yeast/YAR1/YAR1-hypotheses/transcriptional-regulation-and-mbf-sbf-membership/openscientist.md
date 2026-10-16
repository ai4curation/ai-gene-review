---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-21T00:11:52.953078'
end_time: '2026-09-21T00:23:32.612026'
duration_seconds: 699.66
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: yeast
  gene: YAR1
  gene_symbol: YAR1
  uniprot_accession: P46683
  taxon_id: NCBITaxon:559292
  taxon_label: Saccharomyces cerevisiae
  focus_type: function_assignment
  hypothesis_slug: transcriptional-regulation-and-mbf-sbf-membership
  hypothesis_text: Saccharomyces cerevisiae Yar1 promotes RNA polymerase II transcription
    or belongs to the MBF or SBF transcription complexes. Adjudicate these claims
    independently of DNA-binding transcription-activator activity and established
    Rps3 chaperoning. Lack of an APSES DNA-binding domain does not exclude non-DNA-binding
    recruitment or complex subunit roles, as illustrated by Swi6/Cdc10. Evaluate primary
    complex and regulatory evidence and phylogenetic source placement, distinguishing
    direct contribution from indirect effects of ribosome biogenesis. The existing
    DNA-binding-activator report does not resolve these separate claims.
  term_context: No specific term context supplied.
  reference_context: No specific reference context supplied.
  source_file: genes/yeast/YAR1/YAR1-ai-review.yaml
  source_selector: free-text
  source_context_yaml: "hypothesis: Saccharomyces cerevisiae Yar1 promotes RNA polymerase\
    \ II transcription or belongs to the MBF\n  or SBF transcription complexes. Adjudicate\
    \ these claims independently of DNA-binding transcription-activator\n  activity\
    \ and established Rps3 chaperoning. Lack of an APSES DNA-binding domain does not\
    \ exclude non-DNA-binding\n  recruitment or complex subunit roles, as illustrated\
    \ by Swi6/Cdc10. Evaluate primary complex and regulatory\n  evidence and phylogenetic\
    \ source placement, distinguishing direct contribution from indirect effects\n\
    \  of ribosome biogenesis. The existing DNA-binding-activator report does not\
    \ resolve these separate claims.\nfocus_type: function_assignment\ncontext: []\n\
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

- **Organism code:** yeast
- **Taxon:** Saccharomyces cerevisiae (NCBITaxon:559292)
- **Gene directory:** YAR1
- **Gene symbol:** YAR1
- **UniProt accession:** P46683

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** transcriptional-regulation-and-mbf-sbf-membership
- **Source file:** genes/yeast/YAR1/YAR1-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

Saccharomyces cerevisiae Yar1 promotes RNA polymerase II transcription or belongs to the MBF or SBF transcription complexes. Adjudicate these claims independently of DNA-binding transcription-activator activity and established Rps3 chaperoning. Lack of an APSES DNA-binding domain does not exclude non-DNA-binding recruitment or complex subunit roles, as illustrated by Swi6/Cdc10. Evaluate primary complex and regulatory evidence and phylogenetic source placement, distinguishing direct contribution from indirect effects of ribosome biogenesis. The existing DNA-binding-activator report does not resolve these separate claims.

## Term and Decision Context

No specific term context supplied.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: Saccharomyces cerevisiae Yar1 promotes RNA polymerase II transcription or belongs to the MBF
  or SBF transcription complexes. Adjudicate these claims independently of DNA-binding transcription-activator
  activity and established Rps3 chaperoning. Lack of an APSES DNA-binding domain does not exclude non-DNA-binding
  recruitment or complex subunit roles, as illustrated by Swi6/Cdc10. Evaluate primary complex and regulatory
  evidence and phylogenetic source placement, distinguishing direct contribution from indirect effects
  of ribosome biogenesis. The existing DNA-binding-activator report does not resolve these separate claims.
focus_type: function_assignment
context: []
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

# YAR1 (P46683) — Transcription / MBF–SBF Membership Hypothesis: Focused Curation Report

**Gene:** YAR1 / *Saccharomyces cerevisiae* (NCBITaxon:559292) · UniProt **P46683** · 200 aa
**Focus:** function_assignment · slug `transcriptional-regulation-and-mbf-sbf-membership`
**Seed hypothesis:** Yar1 promotes RNA Pol II transcription or belongs to the MBF or SBF transcription complexes (to be adjudicated independently of DNA-binding transcription-activator activity and Rps3 chaperoning).

---

## Executive Judgment

**Verdict: REFUTED / OVER-ANNOTATED** (for the transcription and MBF/SBF claims).

There is **no primary experimental evidence** that Yar1 promotes RNA Pol II transcription or is a subunit of the MBF (Mbp1–Swi6) or SBF (Swi4–Swi6) complexes. Every transcription-related GO annotation on P46683 carries evidence code **IBA** (Inferred from Biological Ancestor, GO_Central/PANTHER) — i.e., phylogenetically propagated, not observed. In contrast, all **experimentally supported** annotations (IDA/IMP/HDA) describe Yar1's role as a **dedicated chaperone of ribosomal protein Rps3 in 40S small-subunit biogenesis and its nuclear import**, backed by genetics, biochemistry, and a 2.8 Å co-crystal structure.

The source of the misannotation is traceable: since 1996 it has been noted that Yar1's ankyrin (ANK) repeats are most similar to those of the cell-cycle transcription factor **Swi6**. Yar1 and the SBF/MBF ankyrin proteins therefore fall into the same broad ankyrin-repeat PANTHER family (PTHR24198), and Swi6/SBF/MBF transcription terms propagate to Yar1 by IBA. **Crucially, in Swi6/Swi4/Mbp1 DNA binding is conferred by the APSES (KilA-N/winged-helix) domain, not by the ANK repeats** — and Yar1 possesses only ankyrin repeats, i.e., the generic protein–protein interaction module that does *not* bind DNA. Thus the seed's own Swi6/Cdc10 analogy, examined carefully, argues *against* the transcription claim rather than for it.

**Most important caveat:** absence of positive evidence is not proof of impossibility. A non-DNA-binding, sub-stoichiometric recruitment role cannot be formally excluded by the current data, but nothing in the primary literature or complex-composition datasets places Yar1 in MBF/SBF or at Pol II promoters. The parsimonious, evidence-based interpretation is a ribosome-biogenesis chaperone whose nuclear presence reflects Rps3 import, not transcription.

---

## Evidence Matrix

| Citation | Evidence type | Supports/Refutes/Qualifies | Claim tested | Key finding | Context | Confidence & limitations |
|---|---|---|---|---|---|---|
| **PMID 24021814** (Holzer, Ban, Klinge 2013) | Structural (co-crystal, direct) | **Refutes** transcription; supports chaperone | Primary molecular function of Yar1 | 2.8 Å Rps3–Yar1 structure; Yar1 keeps Rps3 soluble and mediates its nuclear import | *S. cerevisiae*, in vitro/structural | High. Direct structural mechanism; defines the real function |
| **PMID 15611164** (Loar et al 2004) | Mutant phenotype + interaction (direct) | **Refutes** transcription; supports 40S role | Whether Yar1 acts in transcription vs ribosome biogenesis | Yar1 binds Rps3 & Ltv1; Δyar1 has reduced 40S/excess free 60S; RPS3 overexpression rescues | *S. cerevisiae* genetics/biochem | High. Places Yar1 firmly in 40S production |
| **PMID 8675027** (Lycan et al 1996) | Sequence/original characterization | **Qualifies** (explains the artifact) | Origin of Swi6/SBF link | Yar1 ANK repeats "most similar to…Swi6"; non-essential; slow-growth/cold-sensitive Δyar1; no essential TF phenotype | *S. cerevisiae* | High for the similarity claim; note authors did **not** demonstrate TF activity |
| **PMID 16888326** (Seiser et al 2006) | Genetics/pathway (indirect) | Supports 40S/export context | Pathway context of Yar1 partners | Ltv1 (Yar1 partner) required for 40S nuclear export via Crm1 | *S. cerevisiae* | Medium. Contextual, about Ltv1 not Yar1 directly |
| **UniProt P46683 GO set** (database) | Database/annotation provenance | **Refutes** direct transcription support | Evidence basis of TF/MBF/SBF terms | MBF complex, SBF complex, DNA-binding TF activator activity, +reg Pol II transcription are **all IBA**; all experimental terms are ribosome/localization | GO_Central/PANTHER | High. IBA = phylogenetic inference, not assay |
| **InterPro/PANTHER (P46683)** (computational) | Structural/evolutionary | **Refutes** DNA-binding capacity | Does Yar1 have a DNA-binding domain? | Only ANK signatures (IPR002110, Pfam PF12796, PANTHER PTHR24198); **no APSES/KilA-N/winged-helix domain** | Public bioinformatics | High. Lack of any DNA-binding fold |
| **EBI Complex Portal CPX-946, CPX-950** (database, curated) | Interaction/complex composition | **Refutes** MBF/SBF membership | Is Yar1 a subunit of SBF or MBF? | SBF (CPX-946) = Swi4 + Swi6; MBF (CPX-950) = Mbp1 + Swi6; **Yar1/P46683 absent from both** | *S. cerevisiae*, manually curated | High. Authoritative complex definition |
| **UniProt domain comparison** (computational) | Structural/evolutionary | **Refutes/qualifies** | Does Yar1 share the DNA-binding module of SBF/MBF? | Swi4/Mbp1 carry APSES-type HTH + H-T-H DNA-binding motif; Yar1 (200 aa) has only 2 ANK repeats — the generic interaction module | Public bioinformatics | High. Yar1 lacks the DNA-contacting subunit's architecture |
| **IntAct interactome (P46683)** (database, interaction) | Interaction | **Refutes** transcription/complex link | Does Yar1 physically interact with SBF/MBF subunits? | 15 records; partners = Rps3, Ltv1 + Hsp70/Hsp40 chaperones (Ssa1/2, Ssb1, Sse1, Sis1, Ydj1, Hsp78/26, Erj5, Ess1, Sfm1); **no Swi4/Swi6/Mbp1** | *S. cerevisiae*, curated PPIs | High. No interaction evidence for a transcription role |

---

## GO Curation Implications (leads requiring curator verification)

| GO term | Aspect | Current evidence | Recommended action (lead) |
|---|---|---|---|
| GO:0001228 DNA-binding transcription activator activity, Pol II-specific | MF | IBA only; no APSES domain | **Remove / do not propagate.** Not supported; contradicted by domain architecture |
| GO:0030907 MBF transcription complex | CC | IBA only; no complex-composition data | **Remove / mark NOT.** No primary evidence Yar1 is an MBF subunit |
| GO:0033309 SBF transcription complex | CC | IBA only | **Remove / mark NOT.** No primary evidence Yar1 is an SBF subunit |
| GO:0045944 positive regulation of transcription by Pol II | BP | IBA only | **Remove / treat as non-core.** No direct evidence; any effect is downstream of ribosome biogenesis |
| GO:0042274 ribosomal small subunit biogenesis | BP | IMP (experimental) | **Retain (core).** |
| GO:0000056 ribosomal small subunit export from nucleus | BP | IMP | **Retain.** |
| GO:0005634 nucleus / GO:0005737 cytoplasm | CC | IDA/HDA | **Retain.** Nuclear signal reflects Rps3 import, not TF role |
| *(candidate addition)* protein chaperone / unfolded-protein binding on Rps3 | MF | Direct structure PMID 24021814 | **Consider adding** a chaperone MF term (e.g., unfolded/nascent-protein binding) — more informative than "protein binding" |

**Bottom line:** The four IBA transcription terms are over-annotations and are the strongest candidates for removal or a NOT qualifier; the ribosome-biogenesis terms are the core, experimentally supported function.

---

## Mechanistic Scope

- **Direct molecular activity:** Yar1 is a small (200 aa) two-ANK-repeat protein that acts as a **dedicated chaperone binding ribosomal protein Rps3**, holding it in a soluble, import-competent state (co-crystal structure, PMID 24021814).
- **Cellular process:** couples Rps3 folding/solubility to **nuclear import and incorporation into the assembling 40S subunit** (PMID 15611164, 16888326).
- **Downstream/indirect only:** stress sensitivity, growth/cold-sensitivity of Δyar1, and any perturbation of gene-expression programs are **secondary consequences of impaired 40S biogenesis**, not evidence of a direct transcriptional function. Nuclear localization is expected for an Rps3 import chaperone and does not imply promoter association.

---

## Complex Composition & Domain Comparison (computed, Iteration 2)

**EBI Complex Portal (manually curated):**

| Complex | Accession | Subunits | Yar1 present? |
|---|---|---|---|
| SBF transcription complex | CPX-946 | Swi4 (P25302) + Swi6 (P09959) | **No** |
| MBF ("MBP") transcription complex | CPX-950 | Mbp1 (P39678) + Swi6 (P09959) | **No** |

**UniProt domain architecture:**

| Protein | Length | APSES/HTH DNA-binding domain | ANK repeats | Role |
|---|---|---|---|---|
| **Yar1** (P46683) | 200 aa | **None** | 2 | Rps3 chaperone (not a TF) |
| Swi6 (P09959) | 803 aa | None | 5 | Shared regulatory subunit (SBF+MBF) |
| Swi4 (P25302) | 1093 aa | **APSES-HTH (37–147) + H-T-H (71–92)** | 2 | SBF DNA-binding subunit |
| Mbp1 (P39678) | 833 aa | **APSES-HTH (5–111) + H-T-H (36–57)** | 2 | MBF DNA-binding subunit |

**Interpretation:** Yar1 is absent from both curated complexes. The seed's Swi6/Cdc10 precedent (a subunit lacking APSES) is technically real — Swi6 indeed has no APSES domain — but it does **not** transfer to Yar1: Swi6 is an 803-aa subunit with direct experimental complex-membership evidence, whereas Yar1 is a 200-aa protein with none. The **only** feature Yar1 shares with any SBF/MBF subunit is the generic ANK repeat, and Yar1's ANK repeats are structurally documented to bind **Rps3** (PMID 24021814), not Swi4/Swi6/Mbp1. Shared ANK possession — the driver of the IBA propagation — is not evidence of shared complex membership.

## Conflicts and Alternatives

- **Paralog/family confusion (primary artifact):** Yar1 shares the ankyrin-repeat module with genuine SBF/MBF subunit **Swi6**. Broad PANTHER family PTHR24198 grouping drives IBA propagation of Swi6-derived transcription terms.
- **Domain-logic conflict:** DNA binding in APSES transcription factors (Swi4/Mbp1) resides in the **APSES/KilA-N domain**, absent from Yar1; Swi6 itself contributes regulation via ANK-mediated protein interactions but is not the DNA-contacting subunit. So the "ANK repeats ≈ transcription factor" inference is unsound.
- **Alternative interpretation fully consistent with all data:** Yar1 = ribosome-assembly chaperone; no competing primary dataset supports an MBF/SBF or Pol II role.
- The seed's Swi6/Cdc10 precedent (non-DNA-binding complex membership) is a valid *general* caution but has **no gene-specific support** for Yar1.

---

## Knowledge Gaps

1. **Direct complex-composition/interaction test.** *Checked:* Yar1 absent from curated MBF/SBF (Complex Portal); Yar1's full IntAct interactome (Rps3, Ltv1, Hsp70/Hsp40 chaperones) contains **no** Swi4/Swi6/Mbp1. *Matters:* IBA terms would need a real subunit assignment to stand; none exists. *Status:* **largely resolved against the hypothesis.** *Further confirmation:* Yar1-TAP MS would be expected to recover Rps3/Ltv1/chaperones, not SBF/MBF.
2. **Promoter occupancy.** *Checked:* none found. *Matters:* required for "positive regulation of Pol II transcription." *Resolve:* Yar1 ChIP-seq/ChIP-exo — expect no specific promoter binding.
3. **Transcriptome specificity.** *Checked:* Δyar1 phenotypes are ribosome-linked. *Matters:* distinguishes direct TF role from indirect ribosome-biogenesis effects. *Resolve:* nascent-transcription (4tU/GRO-seq) in Δyar1 vs 40S-biogenesis controls — expect shared, indirect signature.
4. **Precise provenance of each IBA call.** *Checked:* confirmed all four are IBA/GO_Central. *Matters:* pinpoints the ancestral node for a targeted GO_Central fix. *Resolve:* inspect the PTHR24198 reference tree annotation node.

---

## Discriminating Tests

- **Yar1-TAP affinity-MS** in exponentially growing cells: predicted interactors Rps3, Ltv1, import factors — **not** Swi4/Swi6/Mbp1.
- **Reciprocal SBF/MBF pulldowns** (Swi6-, Swi4-, Mbp1-TAP): predicted absence of Yar1.
- **Yar1 ChIP-seq** at cell-cycle (SCB/MCB) promoters: predicted no enrichment.
- **Domain rescue logic:** Δyar1 growth defect is rescued by *RPS3* overexpression (already shown, PMID 15611164) — a transcription-factor loss would not be rescued this way.
- **Sequence/structure:** HHpred/InterProScan for an APSES domain in Yar1 — predicted none (consistent with our InterPro result).

---

## Curation Leads (verify before applying)

- **Action:** Downgrade/remove the four IBA transcription annotations (GO:0001228, GO:0030907, GO:0033309, GO:0045944) as phylogenetic over-annotation from a shared ankyrin-repeat family; consider NOT qualifiers if IBA cannot be locally suppressed.
- **Root-cause fix:** Flag PANTHER **PTHR24198** reference-tree node for GO_Central review — Swi6-derived transcription terms should not descend to the Yar1 chaperone lineage.
- **Retain as core:** GO:0042274 (small-subunit biogenesis), GO:0000056 (small-subunit nuclear export), nucleus/cytoplasm CC.
- **Candidate addition (MF):** a chaperone/unfolded-protein-binding term for Rps3 (avoid generic "protein binding"), supported by PMID 24021814.
- **Candidate references to cite in the review:** PMID **24021814** (co-crystal, chaperone mechanism), PMID **15611164** (40S genetics/interactions), PMID **8675027** (origin of Swi6 similarity; explicitly note no TF activity was shown).
- **Suggested reviewer question:** "Is there any dataset placing Yar1 in MBF/SBF or at Pol II promoters independent of its ankyrin-repeat homology to Swi6?" (Expected: no.)

---

### Provenance
Computed evidence (executed code + outputs retained in the job log):
- **Iter 1:** (1) UniProt P46683 REST pull listing GO evidence codes — all transcription terms = IBA, all experimental terms = ribosome/localization; (2) InterPro/PANTHER signature pull for P46683 — ankyrin-repeat signatures only (IPR002110, PF12796, PTHR24198), no APSES/DNA-binding domain.
- **Iter 2:** (3) EBI Complex Portal search + composition of CPX-946 (SBF = Swi4+Swi6) and CPX-950 (MBF = Mbp1+Swi6) — Yar1/P46683 absent from both; (4) UniProt domain comparison Yar1 vs Swi6/Swi4/Mbp1 — Yar1 has only ANK repeats, Swi4/Mbp1 carry APSES-HTH + H-T-H DNA-binding motifs.
- **Iter 3:** (5) IntAct/PSICQUIC interactome of P46683 (15 records) — partners = Rps3, Ltv1 + Hsp70/Hsp40 chaperone network (Ssa1/2, Ssb1, Sse1, Sis1, Ydj1, Hsp78/26, Erj5, Ess1, Sfm1); no Swi4/Swi6/Mbp1.

Literature via PubMed (PMIDs 8675027, 15611164, 16888326, 24021814).


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)