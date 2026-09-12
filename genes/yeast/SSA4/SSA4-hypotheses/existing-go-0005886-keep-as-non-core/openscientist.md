---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-22T15:01:29.927923'
end_time: '2026-08-22T15:13:37.919346'
duration_seconds: 727.99
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: yeast
  gene: SSA4
  gene_symbol: SSA4
  uniprot_accession: P22202
  taxon_id: NCBITaxon:559292
  taxon_label: Saccharomyces cerevisiae
  focus_type: existing_go_annotation_decision
  hypothesis_slug: existing-go-0005886-keep-as-non-core
  hypothesis_text: 'The existing SSA4 GO annotation to plasma membrane (GO:0005886)
    should receive review action KEEP_AS_NON_CORE. Current rationale: Not supported
    as a primary site for Ssa4; plausible peripheral association only, so kept as
    non-core.'
  term_context: '- Term: plasma membrane (GO:0005886)

    - Evidence type: IBA

    - Original reference: GO_REF:0000033

    - Current review action: KEEP_AS_NON_CORE

    - Review summary: Plasma membrane is a phylogenetic (IBA) inference not specifically
    supported for

    Ssa4 in the falcon synthesis, which consistently localizes Ssa4 to the

    cytosol/cytoplasm. Some cytosolic Hsp70s are peripherally membrane-associated,
    so

    this is retained as a non-core, low-confidence localization rather than removed.

    - Review reason: Not supported as a primary site for Ssa4; plausible peripheral
    association only, so kept as non-core.'
  reference_context: '- GO_REF:0000033

    - file:yeast/SSA4/SSA4-deep-research-falcon.md'
  source_file: genes/yeast/SSA4/SSA4-ai-review.yaml
  source_selector: existing_annotations[3]
  source_context_yaml: "term:\n  id: GO:0005886\n  label: plasma membrane\nevidence_type:\
    \ IBA\noriginal_reference_id: GO_REF:0000033\nreview:\n  summary: |-\n    Plasma\
    \ membrane is a phylogenetic (IBA) inference not specifically supported for\n\
    \    Ssa4 in the falcon synthesis, which consistently localizes Ssa4 to the\n\
    \    cytosol/cytoplasm. Some cytosolic Hsp70s are peripherally membrane-associated,\
    \ so\n    this is retained as a non-core, low-confidence localization rather than\
    \ removed.\n  action: KEEP_AS_NON_CORE\n  reason: Not supported as a primary site\
    \ for Ssa4; plausible peripheral association only, so kept as\n    non-core.\n\
    \  additional_reference_ids:\n  - file:yeast/SSA4/SSA4-deep-research-falcon.md\n\
    \  supported_by:\n  - reference_id: file:yeast/SSA4/SSA4-deep-research-falcon.md\n\
    \    supporting_text: Ssa4 is consistently classified as a **cytosolic/cytoplasmic\
    \ Hsp70**\n    reference_section_type: RESULTS"
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

- **Organism code:** yeast
- **Taxon:** Saccharomyces cerevisiae (NCBITaxon:559292)
- **Gene directory:** SSA4
- **Gene symbol:** SSA4
- **UniProt accession:** P22202

## Focus

- **Focus type:** existing_go_annotation_decision
- **Hypothesis slug:** existing-go-0005886-keep-as-non-core
- **Source file:** genes/yeast/SSA4/SSA4-ai-review.yaml
- **Source selector:** existing_annotations[3]

## Seed Hypothesis

The existing SSA4 GO annotation to plasma membrane (GO:0005886) should receive review action KEEP_AS_NON_CORE. Current rationale: Not supported as a primary site for Ssa4; plausible peripheral association only, so kept as non-core.

## Term and Decision Context

- Term: plasma membrane (GO:0005886)
- Evidence type: IBA
- Original reference: GO_REF:0000033
- Current review action: KEEP_AS_NON_CORE
- Review summary: Plasma membrane is a phylogenetic (IBA) inference not specifically supported for
Ssa4 in the falcon synthesis, which consistently localizes Ssa4 to the
cytosol/cytoplasm. Some cytosolic Hsp70s are peripherally membrane-associated, so
this is retained as a non-core, low-confidence localization rather than removed.
- Review reason: Not supported as a primary site for Ssa4; plausible peripheral association only, so kept as non-core.

## Reference Context

- GO_REF:0000033
- file:yeast/SSA4/SSA4-deep-research-falcon.md

## Source Context YAML

```yaml
term:
  id: GO:0005886
  label: plasma membrane
evidence_type: IBA
original_reference_id: GO_REF:0000033
review:
  summary: |-
    Plasma membrane is a phylogenetic (IBA) inference not specifically supported for
    Ssa4 in the falcon synthesis, which consistently localizes Ssa4 to the
    cytosol/cytoplasm. Some cytosolic Hsp70s are peripherally membrane-associated, so
    this is retained as a non-core, low-confidence localization rather than removed.
  action: KEEP_AS_NON_CORE
  reason: Not supported as a primary site for Ssa4; plausible peripheral association only, so kept as
    non-core.
  additional_reference_ids:
  - file:yeast/SSA4/SSA4-deep-research-falcon.md
  supported_by:
  - reference_id: file:yeast/SSA4/SSA4-deep-research-falcon.md
    supporting_text: Ssa4 is consistently classified as a **cytosolic/cytoplasmic Hsp70**
    reference_section_type: RESULTS
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

# SSA4 (P22202) — Plasma Membrane (GO:0005886) Annotation Review

**Focus:** existing_go_annotation_decision · `existing_annotations[3]` in `genes/yeast/SSA4/SSA4-ai-review.yaml`
**Seed hypothesis:** Keep the IBA plasma-membrane annotation as **KEEP_AS_NON_CORE**.
**Gene:** SSA4 / *Saccharomyces cerevisiae* stress-inducible cytosolic Hsp70 (SSA subfamily), 642 aa.

---

## Executive Judgment

**Verdict: Over-annotated — the seed KEEP_AS_NON_CORE action is defensible but arguably too weak; REMOVE is the better-supported lead.**

The plasma-membrane (GO:0005886) annotation on SSA4 is a **phylogenetic (IBA, GO_REF:0000033) inference with no yeast-specific support**. Three independent lines of evidence converge:

1. **No experimental support in yeast.** UniProt records SSA4 subcellular location as *Cytoplasm* only. The only experimental (IDA, PMID:11279056) cellular-component evidence is for cytoplasm and nucleus. SSA4 is a nucleocytoplasmic shuttling Hsp70 (PMID:17020589).
2. **The PM annotation is not present in the current GO release.** A live QuickGO query for P22202 returns six cellular-component annotations — nucleus, cytoplasm, cytosol (IDA/IEA/IBA) — and **no plasma-membrane annotation**. GO:0005886 survives only as a stale cross-reference in the cached UniProt entry. In other words, GO_Central/PAINT appears to have already dropped this term for the Hsp70 ancestral node relevant to Ssa4.
3. **The proximal source of the family PM signal is a single contamination-prone yeast PM-proteome study — which did not include Ssa4.** Live QuickGO shows PM (GO:0005886) annotations for the constitutive paralogs **Ssa1, Ssa2, and Ssb1**, all **HDA** evidence from **one** reference, **PMID:16622836** (Delom et al. 2006, stripped-PM-fraction mass-spec of ~90 proteins). Abundant cytosolic chaperones routinely co-purify in such membrane fractions. **Ssa4 was not detected** (it is stress-inducible with low basal abundance), so its PM term was purely phylogenetic (IBA) and is now absent from live GO. (A separate mammalian tumor-cell-surface Hsp70 phenomenon exists — Gb3/lipid-raft dependent, PMID:37932378, 30632067, 39015084 — but human HSPA1A itself carries no PM GO term, so this is not the direct source here.)

4. **The authoritative organism database (SGD) does not annotate Ssa4 to the plasma membrane.** SGD's GO details for YER103W (146 annotations) list cellular-component terms only for **cytoplasm and nucleus** (manually curated) plus cytoplasm/nucleus/cytosol (computational) — **no GO:0005886**. SGD's curated description attributes Ssa4's membrane role to "**SRP-dependent cotranslational protein-membrane targeting and translocation**" (i.e., the **ER**) and describes it as a "cytoplasmic protein that concentrates in nuclei upon starvation."

**Most important caveat:** Cytosolic Hsp70s (including yeast Ssa) genuinely engage membranes peripherally during protein/mRNA targeting — but at the **ER** (SRP-dependent cotranslational translocation, per SGD) and the **mitochondrial outer membrane** (Tom70-dependent mRNA/precursor delivery, PMID:22138184), **not the plasma membrane**. The paralog HDA "PM" detections are a weak, contamination-prone basis, and even they do not include Ssa4. So the "plausible peripheral association" rationale in the seed is real but thin, and does not specifically implicate Ssa4 at GO:0005886.

---

## Evidence Matrix

| Citation | Evidence type | Supports/Refutes | Claim tested | Key finding | Context | Confidence / limitations |
|---|---|---|---|---|---|---|
| UniProt P22202 (record) | Database | Refutes PM | Primary localization of Ssa4 | Subcellular location = "Cytoplasm" only | *S. cerevisiae* | High for curated summary; database-level |
| QuickGO live query (P22202) | Database/computational | Refutes PM | Does GO currently annotate PM? | 6 CC annotations (nucleus, cytoplasm, cytosol); **no GO:0005886** | GO_Central release | High; reflects current GO, may lag PAINT tree edits |
| PMID:11279056 (IDA, SGD) | Localization (experimental) | Qualifies | Experimental localization | IDA support only for cytoplasm and nucleus | *S. cerevisiae* | High for cyto/nucleus; silent on PM |
| PMID:17020589 | Localization / transport | Refutes PM | Where does Ssa4 reside? | Ssa4p shuttles nucleus↔cytoplasm; nuclear on stress via Msn5 export | *S. cerevisiae* | High; no membrane localization |
| PMID:22138184 | Mutant/mechanism | Qualifies | Membrane association of Ssa | Ssa1 targets mRNA to **mitochondrial outer membrane** (Tom70) | *S. cerevisiae* | Peripheral organellar, not plasma membrane |
| PMID:25853343 | Interaction/mechanism | Qualifies | Ssa membrane/pore contacts | Ssa2 binds nucleoporin Nup116 for tRNA import | *S. cerevisiae* | Nuclear pore, not plasma membrane |
| PMID:16622836 (Delom 2006) | Localization (HDA proteomics) | Qualifies / competing origin | Are yeast Hsp70s at the PM? | Ssa1/Ssa2/Ssb1 detected in stripped-PM fraction (~90 proteins); **Ssa4 not detected** | *S. cerevisiae* | HDA on paralogs only; abundant chaperones prone to co-purification; no Ssa4 |
| PMID:37932378 | Structural/biophysical | Competing (mammalian) | Basis of PM-Hsp70 | Hsp70 binds DOPC/DOPS bilayers; PM-Hsp70 specific to tumor cells | Mammalian/artificial membrane | Distinct phenomenon; human HSPA1A carries no PM GO term |
| PMID:30632067; PMID:39015084 | Localization (mammalian) | Competing (mammalian) | Where is surface Hsp70 seen? | mHsp70 on tumor-cell surface, Gb3/lipid-raft dependent | Human/mouse tumor | Organism/context-specific |
| QuickGO paralog scan (this run) | Computational/database | Qualifies | Which Hsp70s carry PM in GO? | PM present for Ssa1/Ssa2/Ssb1 (HDA, PMID:16622836); absent for Ssa4, Ssa3, human HSPA1A | GO_Central live | Direct query; reflects current release |
| SGD YER103W record (this run) | Review/database | Refutes PM | Does SGD place Ssa4 at PM? | CC = cytoplasm/nucleus/cytosol only; membrane role = SRP-dependent **ER** cotranslational targeting | *S. cerevisiae* | Authoritative organism DB; no PM term |

---

## GO Curation Implications

- **Term:** plasma membrane (GO:0005886), a **cellular component (CC)** term. Evidence type IBA / GO_REF:0000033.
- **Recommended lead (requires curator verification): REMOVE** the plasma-membrane annotation, or at minimum retain as **NON_CORE** only if the curator prefers strict conservatism. Rationale: (a) no yeast experimental support; (b) the term is absent from the current GO_Central set for P22202, suggesting the phylogenetic inference has already been retracted upstream; (c) the ancestral signal derives from mammalian tumor-cell-surface Hsp70, an organism/context-specific property.
- **Better-supported CC terms are already present and experimental:** cytoplasm (GO:0005737, IDA), nucleus (GO:0005634, IDA), cytosol (GO:0005829). These should be the core localizations.
- The seed action **KEEP_AS_NON_CORE is not wrong**, but it is **more generous than the evidence warrants**. The only yeast PM evidence for this family (HDA, PMID:16622836) covers the paralogs Ssa1/Ssa2/Ssb1, is contamination-prone, and **excludes Ssa4**; the genuine peripheral membrane roles of Ssa chaperones concern the **ER/mitochondrial outer membrane**, not the plasma membrane. If the curator prefers conservatism, KEEP_AS_NON_CORE is acceptable, but the annotation should be explicitly flagged as an IBA no longer present in the live GO release for Ssa4.

---

## Mechanistic Scope

- **Direct molecular function of Ssa4:** ATP-dependent Hsp70 chaperone (protein folding, nascent-chain and stress-denatured protein binding), operating in the **cytosol and nucleus**.
- **Genuine membrane-proximal roles (peripheral, transient):** delivery of precursor proteins/mRNAs to the **ER (Sec translocon)** and **mitochondrial outer membrane (Tom70)**; interaction with **nuclear pore** components (Nup116, Nup82) during nucleocytoplasmic shuttling. None of these are the plasma membrane.
- **Not supported as direct gene-product localization:** residence in/at the plasma membrane.

---

### Paralog / ortholog PM-annotation comparison (live QuickGO, this run)

| Protein | Accession | PM (GO:0005886)? | Evidence | Reference |
|---|---|---|---|---|
| Ssa4 (yeast, target) | P22202 | **No** | — | — (IBA only, now absent) |
| Ssa1 (yeast) | P10591 | Yes | HDA | PMID:16622836 |
| Ssa2 (yeast) | P10592 | Yes | HDA | PMID:16622836 |
| Ssa3 (yeast) | P09435 | No | — | — |
| Ssb1 (yeast) | P11484 | Yes | HDA | PMID:16622836 |
| Ssc1 (yeast, mito) | P12398 | No | — | — |
| HSPA1A (human) | P0DMV8 | No | — | — |
| HSPA8 (human) | P11142 | Yes | IEA/TAS | — |

## Conflicts and Alternatives

- **Real-but-weak yeast paralog evidence:** Unlike my initial mammalian-origin hypothesis, the yeast PM annotations for Ssa1/Ssa2/Ssb1 are experimental (HDA) — but all from **one** stripped-PM-fraction proteomics study (PMID:16622836) where abundant cytosolic chaperones commonly co-purify, and which **did not include Ssa4**. This is a contamination-prone, non-specific basis and is paralog-, not Ssa4-, specific.
- **Paralog/ortholog carry-over:** The Hsp70/HSPA PANTHER family mixes yeast Ssa, Ssb, Sse, mammalian HSPA1A/HSPA8, etc. The separate mammalian tumor-cell-surface Hsp70 biology belongs to inducible HSPA1A and should not be propagated to Ssa4; note HSPA1A itself carries no PM GO term.
- **Stale vs. live records:** UniProt's cached cross-reference still lists GO:0005886 (IBA), whereas live GO_Central/QuickGO does not — a database-lag artifact that could make the annotation look current when it is effectively retired.
- **Real-but-different membrane biology:** Ssa's authentic ER/mitochondrial-membrane peripheral associations could be mistaken as generic "membrane" support, but they map to distinct CC terms, not plasma membrane.

---

## Knowledge Gaps

1. **Is the PM annotation truly retracted upstream, or filtered by QuickGO?** — Checked: live QuickGO returns no GO:0005886 for P22202. Matters because it changes REMOVE vs KEEP. Resolution: inspect the current PAINT/PANTHER family tree (PTN node) annotations and the GO_Central GAF directly.
2. **Any high-throughput yeast plasma-membrane/proteomics hit for Ssa4?** — Not found in targeted literature. Matters because a peripheral PM proteomics signal could justify NON_CORE. Resolution: check membrane-proteome and BioID/proximity datasets (SGD, GFP-localization Huh et al.).
3. **Does any yeast Ssa localize to the plasma membrane under stress?** — No evidence found; stress redistributes Ssa4 to the nucleus, not the PM. Resolution: stress-condition live imaging.

---

## Discriminating Tests

- **GFP/mNeonGreen live imaging of Ssa4** under normal and heat/ethanol stress with a PM marker (e.g., Pma1) — expect cytosol/nucleus, no PM enrichment.
- **Cell-surface biotinylation / non-permeabilized immunostaining** for Ssa4 — expect negative (unlike mammalian tumor Hsp70).
- **Subcellular fractionation** (cytosol vs. PM vs. ER vs. mitochondria) with quantitative MS — expect cytosolic/nuclear, with minor ER/mito peripheral pools, not PM.
- **Inspect the current PANTHER PTN node GAF** to confirm whether GO:0005886 is still propagated to the Ssa4-containing subtree.

---

## Curation Leads (require curator verification)

- **Action change lead:** Consider **REMOVE** for GO:0005886 (IBA) rather than KEEP_AS_NON_CORE; if retained, keep strictly as NON_CORE, low-confidence.
- **Candidate references / snippets to verify:**
  - PMID:17020589 — "*Cytoplasmic hsp70s like yeast Ssa4p shuttle between nucleus and cytoplasm under normal growth conditions but accumulate in nuclei upon stress.*" (supports cytosol/nucleus as the real localizations).
  - PMID:37932378 — "*Membrane-bound heat shock protein 70 (Hsp70) apart from its intracellular localization was shown to be specifically expressed on the plasma membrane surface of tumor but not normal cells.*" (identifies mammalian tumor origin of PM-Hsp70).
  - PMID:11279056 — IDA source for cytoplasm and nucleus (SGD).
- **Candidate retained CC terms:** GO:0005737 (cytoplasm, IDA), GO:0005634 (nucleus, IDA), GO:0005829 (cytosol) as core.
- **Suggested question for curator:** Is the reviewed PM IBA still present in the GO_Central GAF/PAINT tree, or is it already retired (as live QuickGO suggests)? If retired upstream, the review row should note the annotation no longer exists and mark REMOVE/obsolete rather than KEEP.
- **Suggested experiment:** cell-surface biotinylation + fractionation MS to definitively exclude a yeast plasma-membrane pool.

---

## Provenance

- UniProt REST (`P22202.json`): subcellular location + GO cross-references (executed).
- QuickGO annotation API (`/annotation/search`, geneProductId=P22202): 20 total annotations, 6 CC, **no GO:0005886**; IBA `withFrom` ortholog list captured (executed).
- QuickGO paralog/ortholog scan (Ssa1/Ssa2/Ssa3/Ssb1/Ssc1, HSPA1A/HSPA8/mouse Hsp70): PM present only for Ssa1/Ssa2/Ssb1 (HDA, all PMID:16622836) (executed).
- SGD backend API (`/backend/locus/YER103W` + `/go_details`): 146 GO annotations, CC = cytoplasm/nucleus/cytosol only, no PM; curated description cites SRP-dependent ER cotranslational targeting (executed).
- PubMed searches: PMID 17020589, 11279056, 22138184, 25853343, 16622836, 37932378, 30632067, 39015084.

*All computational results above were executed against live public resources during this run; no results were fabricated. UniProt's cached GO cross-reference listing GO:0005886 (IBA) conflicts with the live QuickGO set, which is reported as a database-lag caveat rather than resolved definitively.*


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)