---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-11T06:48:13.732534'
end_time: '2026-07-11T06:59:56.051785'
duration_seconds: 702.32
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: worm
  gene: ire-1
  gene_symbol: ire-1
  uniprot_accession: Q09499
  taxon_id: NCBITaxon:6239
  taxon_label: Caenorhabditis elegans
  focus_type: computational_prediction
  hypothesis_slug: prediction-ester-bond-hydrolase
  hypothesis_text: GO-GPT (via BioReason-Pro) predicts hydrolase activity acting on
    ester bonds (GO:0016788) for C. elegans ire-1 (Q09499), the conserved ER unfolded-protein-response
    transmembrane sensor with a cytoplasmic kinase domain and a C-terminal endoribonuclease
    (RNase) domain. Independently assess whether ire-1 has hydrolase activity acting
    on ester bonds, and if so whether this reflects its site-specific endoribonuclease
    activity that cleaves xbp-1 mRNA at phosphodiester (ester) bonds to initiate non-conventional
    splicing of the UPR transcription factor -- which would make GO:0016788 a correct
    but high-level/less-precise parent of the specific endoribonuclease function (GO:0004521)
    -- or whether ire-1's ester-bond hydrolase activity is unsupported. Determine
    whether the prediction is supported or refuted, and at what level of specificity.
  term_context: '- Term: hydrolase activity, acting on ester bonds (GO:0016788)'
  reference_context: '- doi:10.64898/2026.03.19.712954'
  source_file: ''
  source_selector: ''
  source_context_yaml: "hypothesis: GO-GPT (via BioReason-Pro) predicts hydrolase\
    \ activity acting on ester bonds (GO:0016788)\n  for C. elegans ire-1 (Q09499),\
    \ the conserved ER unfolded-protein-response transmembrane sensor with\n  a cytoplasmic\
    \ kinase domain and a C-terminal endoribonuclease (RNase) domain. Independently\
    \ assess whether\n  ire-1 has hydrolase activity acting on ester bonds, and if\
    \ so whether this reflects its site-specific\n  endoribonuclease activity that\
    \ cleaves xbp-1 mRNA at phosphodiester (ester) bonds to initiate non-conventional\n\
    \  splicing of the UPR transcription factor -- which would make GO:0016788 a correct\
    \ but high-level/less-precise\n  parent of the specific endoribonuclease function\
    \ (GO:0004521) -- or whether ire-1's ester-bond hydrolase\n  activity is unsupported.\
    \ Determine whether the prediction is supported or refuted, and at what level\n\
    \  of specificity.\nfocus_type: computational_prediction\nterm_id: GO:0016788\n\
    term_label: hydrolase activity, acting on ester bonds\ncontext: []\nreference_id:\n\
    - doi:10.64898/2026.03.19.712954"
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
artifact_count: 4
artifact_sources:
  openscientist_artifacts_zip: 4
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
- filename: go_decision_table.csv
  path: openscientist_artifacts/go_decision_table.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist go decision table
- filename: ontology_relationship_tests.csv
  path: openscientist_artifacts/ontology_relationship_tests.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist ontology relationship tests
---

## Question

# AIGR Gene Hypothesis Deep Research

You are evaluating one focused gene curation hypothesis for AI Gene Review.
This is not a general gene overview. Use the seed hypothesis and source context
below to search for evidence that supports, refutes, narrows, or competes with
the proposed curation decision.

## Target Gene

- **Organism code:** worm
- **Taxon:** Caenorhabditis elegans (NCBITaxon:6239)
- **Gene directory:** ire-1
- **Gene symbol:** ire-1
- **UniProt accession:** Q09499

## Focus

- **Focus type:** computational_prediction
- **Hypothesis slug:** prediction-ester-bond-hydrolase
- **Source file:** 
- **Source selector:** 

## Seed Hypothesis

GO-GPT (via BioReason-Pro) predicts hydrolase activity acting on ester bonds (GO:0016788) for C. elegans ire-1 (Q09499), the conserved ER unfolded-protein-response transmembrane sensor with a cytoplasmic kinase domain and a C-terminal endoribonuclease (RNase) domain. Independently assess whether ire-1 has hydrolase activity acting on ester bonds, and if so whether this reflects its site-specific endoribonuclease activity that cleaves xbp-1 mRNA at phosphodiester (ester) bonds to initiate non-conventional splicing of the UPR transcription factor -- which would make GO:0016788 a correct but high-level/less-precise parent of the specific endoribonuclease function (GO:0004521) -- or whether ire-1's ester-bond hydrolase activity is unsupported. Determine whether the prediction is supported or refuted, and at what level of specificity.

## Term and Decision Context

- Term: hydrolase activity, acting on ester bonds (GO:0016788)

## Reference Context

- doi:10.64898/2026.03.19.712954

## Source Context YAML

```yaml
hypothesis: GO-GPT (via BioReason-Pro) predicts hydrolase activity acting on ester bonds (GO:0016788)
  for C. elegans ire-1 (Q09499), the conserved ER unfolded-protein-response transmembrane sensor with
  a cytoplasmic kinase domain and a C-terminal endoribonuclease (RNase) domain. Independently assess whether
  ire-1 has hydrolase activity acting on ester bonds, and if so whether this reflects its site-specific
  endoribonuclease activity that cleaves xbp-1 mRNA at phosphodiester (ester) bonds to initiate non-conventional
  splicing of the UPR transcription factor -- which would make GO:0016788 a correct but high-level/less-precise
  parent of the specific endoribonuclease function (GO:0004521) -- or whether ire-1's ester-bond hydrolase
  activity is unsupported. Determine whether the prediction is supported or refuted, and at what level
  of specificity.
focus_type: computational_prediction
term_id: GO:0016788
term_label: hydrolase activity, acting on ester bonds
context: []
reference_id:
- doi:10.64898/2026.03.19.712954
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

# AIGR Deep Research Report — *ire-1* (Q09499, *C. elegans*)
## Hypothesis: hydrolase activity, acting on ester bonds (GO:0016788)

**Focus type:** computational_prediction (GO-GPT / BioReason-Pro)
**Term under test:** GO:0016788 — *hydrolase activity, acting on ester bonds*
**Reference context:** doi:10.64898/2026.03.19.712954

---

## Executive Judgment

**Verdict: PARTIALLY SUPPORTED — but over-general and redundant; do NOT add GO:0016788 as an annotation.**

*ire-1* unambiguously carries a catalytic activity on nucleic-acid ester (phosphodiester)
bonds: its C-terminal KEN/RNase domain is a site-specific **endoribonuclease** that cleaves
*xbp-1* mRNA to drive non-conventional UPR splicing. In that loose biochemical sense the
prediction "acts on ester bonds" is not wrong. However, the prediction is the **wrong level
of specificity for annotation**, for three concrete reasons:

1. **A precise, experimentally-supported term already exists.** UniProt Q09499 already carries
   **GO:0004521 (RNA endonuclease activity, IMP:WormBase)** and **GO:0016787 (hydrolase, IEA-KW)**.
   GO:0016788 adds no information beyond these.
2. **In the current GO ontology, GO:0016788 is NOT an ancestor of GO:0004521.** QuickGO shows the
   RNA-endonuclease branch descends through *catalytic activity, acting on a nucleic acid*
   (GO:0140640) → nuclease (GO:0004518) → endonuclease (GO:0004519) → RNA endonuclease (GO:0004521),
   **not** through *hydrolase, acting on ester bonds*. So the seed's premise that GO:0016788 is a
   "correct high-level parent of GO:0004521" **does not hold in the current ontology**.
3. **Mechanistic mismatch — the closest analog is a LYASE, not a hydrolase.** IRE1-family RNases use a
   **metal-independent transesterification** (general acid/base His–Tyr pair) yielding a
   **2′,3′-cyclic phosphate + 5′-OH**, not a hydrolysis to a phosphomonoester. GO's own treatment of the
   enzyme class sharing this exact chemistry — **tRNA-intron lyase activity (GO:0000213)** — places it
   under **lyase / phosphorus-oxygen lyase (GO:0016829 / GO:0016849)** and under RNA endonuclease
   (GO:0004521), but **explicitly NOT under GO:0016788**. So GO:0016788 is not just off-branch; it is the
   mechanistically wrong high-level MF for a cyclic-phosphate-producing transesterase. (It also fails
   GO:0016788's own hydrolytic nuclease children GO:0016891/2, which require phosphomonoester products.)

**Bottom line for the curator:** the true, well-supported molecular function is the specific
IRE1-type endoribonuclease activity (GO:0004521 / more specifically an IRE1/tRNA-ligase-type
transesterifying endoribonuclease). GO:0016788 is a correct-but-imprecise generalization that is
**subsumed and redundant** and should **not** be added.

---

## Evidence Matrix

| Citation | Evidence type | Supports/Refutes/Qualifies | Claim tested | Key finding | Context | Confidence & limitations |
|---|---|---|---|---|---|---|
| PMID 11780124 (Calfon 2002, *Nature*) | Direct in-vitro assay + genetics | Qualifies (supports specific endoribonuclease, not the broad term) | Is IRE1 a direct endoribonuclease on xbp-1 mRNA? | "Purified mouse IRE1 accurately cleaved XBP-1 mRNA in vitro… a direct target of IRE1 endonucleolytic activity"; C. elegans ire-1/xbp-1 mutations abolish UPR splicing | Mouse IRE1 in vitro; *C. elegans* in vivo | High. Direct cleavage shown for mouse ortholog; worm shown genetically. |
| PMID 11779465 (Shen 2001, *Cell*) | Mutant phenotype (target organism) | Supports specific function | Does worm ire-1 mediate xbp-1 splicing? | "C. elegans requires ire-1-mediated splicing of xbp-1 mRNA for UPR gene transcription and survival upon ER stress" | *C. elegans* in vivo | High for BP link; MF is inferred from splicing requirement. |
| PMID 21729333 (Korennykh 2011) | Structural + enzymology | Qualifies (defines mechanism) | What is the catalytic mechanism of Ire1 RNase? | His1061/Tyr1043 general acid-base pair; Asn1057/Arg1056 coordinate the **scissile phosphate**; cleaves stem-loops of HAC1/Xbp1 and tRNA-Phe ASL | Yeast/general Ire1 RNase | High. Confirms phosphodiester (ester-bond) chemistry but via transesterification, not phosphomonoester-producing hydrolysis. |
| PMID 36389122 (De-Souza 2022) | Functional (target organism) | Supports | Is IRE-1 endoribonuclease activity operative in worm aging? | "IRE-1 endoribonuclease activity declines early in [aging]" | *C. elegans* | Medium-high. Confirms endoribonuclease framing for worm IRE-1. |
| PMID 30833722 / 32446294 | Structural/pharmacology (review-level orientation) | Qualifies | Is IRE1 a bifunctional kinase + RNase with a druggable RNase site? | RNase active site (Lys907/His910/Tyr892 in mIRE1) excises the 26-nt XBP1 intron | Mouse/human IRE1 | Medium. Ortholog structural context; not worm-specific. |
| UniProt Q09499 (database) | Curated record | Supports (existing precise annotation) | What MF terms are already assigned? | GO:0004521 RNA endonuclease (IMP:WormBase); GO:0004674 kinase (ISS); GO:0016787 hydrolase (IEA-KW); KEN/RNase domain 781–909, kinase 518–778 | *C. elegans* | High. Shows the specific term already present. |
| QuickGO ontology (database) | Ontology structure | Refutes seed's parentage premise | Is GO:0016788 an ancestor of GO:0004521? | No — GO:0004521 ancestry runs via GO:0140640/0004518/0004519, not GO:0016788 | Current GO | High. Direct ontology query. |
| QuickGO GO:0000213 (database) | Ontology structure / mechanistic analogy | Refutes hydrolase-branch fit | Where does GO place the transesterifying (2′,3′-cyclic-phosphate) RNase class? | tRNA-intron lyase (GO:0000213) is a child of RNA endonuclease (GO:0004521) AND lyase/phosphorus-oxygen lyase (GO:0016829/GO:0016849) — NOT under GO:0016788 | Current GO | High. GO classifies IRE1's mechanistic analog as a lyase, not an ester-bond hydrolase. |

---

## GO Curation Implications

**Molecular Function (MF).** The relevant, supported MF term is **GO:0004521 (RNA endonuclease
activity)** — already annotated to Q09499 with IMP:WormBase evidence, plus the kinase term
GO:0004674. A still-more-precise child (e.g. an IRE1/tRNA-ligase-type transesterifying
endoribonuclease term) would be ideal if available.

**Recommended action for the predicted term GO:0016788 (lead, requires curator verification):**
- **Do not add GO:0016788.** It is redundant with the already-present GO:0016787 (hydrolase) and,
  more importantly, is **superseded by** the specific GO:0004521 that captures the actual activity.
- Treat the GO-GPT prediction as **"correct in spirit, too general, and structurally off-branch."**
  It is not a false positive at the chemistry level, but it fails the *annotate-to-most-specific-term*
  principle and does not sit on the lineage of the experimentally supported term.
- If anything, the existing IEA GO:0016787 keyword annotation could itself be viewed as low-value
  given GO:0004521 is present, but that is a separate housekeeping matter.

This is **not** a "protein binding" fallback; a specific, informative MF (endoribonuclease) is
well supported.

---

## Mechanistic Scope

- **Direct gene-product activity (what the term should describe):** two catalytic activities on the
  cytoplasmic face — (i) a Ser/Thr **protein kinase** (autophosphorylation; a phosphotransferase,
  *not* a hydrolase) and (ii) a **site-specific endoribonuclease** (KEN domain) that cleaves two
  stem-loops in *xbp-1* mRNA, excising an intron. The endoribonuclease is the only activity relevant
  to GO:0016788.
- **Chemistry:** cleavage of an RNA **phosphodiester bond** (an ester bond) via general acid/base
  catalysis, producing a 2′,3′-cyclic phosphate and 5′-OH (transesterification), later re-ligated by
  RtcB-type ligase to yield spliced *xbp-1*.
- **Downstream (NOT the molecular function):** production of active XBP-1 transcription factor;
  transcriptional UPR; ER homeostasis; larval development; longevity in insulin/IGF-1 mutants;
  ER-stress apoptosis. These are BP/phenotype consequences, not the MF being tested.

---

## Conflicts and Alternatives

- **Ontology-structure conflict (primary):** The seed frames GO:0016788 as a valid parent of
  GO:0004521. Current GO places nuclease/endonuclease activity under GO:0140640 (*catalytic activity,
  acting on a nucleic acid*), **not** under GO:0016788. Thus GO:0016788 and GO:0004521 are in
  parallel branches, not parent–child. This weakens the "correct-but-less-precise parent" framing.
- **Mechanism conflict (hydrolase vs lyase):** GO:0016788 still owns hydrolytic nuclease children
  (GO:0016891/2) that specify phosphomonoester products; IRE1 produces cyclic-phosphate ends
  (transesterase/lyase-like, cf. EC reclassification of cyclizing RNases to EC 4.6.1). Decisively,
  GO classifies IRE1's mechanistic twin — **tRNA-intron lyase (GO:0000213)** — under **lyase
  (GO:0016829)/phosphorus-oxygen lyase (GO:0016849)** and RNA endonuclease (GO:0004521), **not** under
  GO:0016788. So IRE1 fits neither GO:0016891/2 nor the strict "hydrolase" reading; if a high-level
  chemistry parent beyond GO:0004521 were ever wanted, the lyase branch would be the better-motivated
  choice — further undercutting the GO:0016788 prediction.
- **Orthology/paralog caveat:** Direct biochemical cleavage assays (Calfon; Korennykh) were done on
  mouse/yeast IRE1; worm *ire-1* is supported genetically (Shen) and by conserved domain architecture.
  No paralog-overannotation risk (IRE1 is the single ER UPR IRE-branch sensor); low frequency-bias risk.
- **Not an in-vitro-only artifact:** function is corroborated in vivo in *C. elegans*.

---

## Knowledge Gaps

1. **Worm-specific direct cleavage assay.** Checked: worm evidence is genetic (IMP) + orthology;
   direct in-vitro cleavage was shown for mouse IRE1. Matters because MF assignment ideally rests on
   direct activity. Resolve with a purified *C. elegans* IRE-1 RNase cleavage assay on *xbp-1* stem-loops.
2. **Exact GO term granularity.** Checked: a QuickGO search found **no dedicated "IRE1 endoribonuclease"
   MF term**; GO:0004521 (RNA endonuclease activity) is the most specific applicable term and is already
   annotated (IMP:WormBase). A mechanism-precise child (analogous to the tRNA-intron *lyase* term
   GO:0000213) does not exist for IRE1. Matters only if maximal precision is desired; could be a new-term
   request but is not required for correct curation.
3. **Whether curators intend GO:0016788 as a mechanism-agnostic descriptor.** If a curation policy
   treats phosphodiester cleavage as "acting on ester bonds," the term becomes defensible-but-still-
   redundant. Resolve via GO editorial guidance.

---

## Discriminating Tests

- **Ontology audit:** confirm in the review's GO release whether GO:0016788 is an ancestor of
  GO:0004521 (it is not in current GO) — decisive for the "correct parent" claim.
- **Point-mutant RNase-dead worm** (KEN-domain catalytic His/Tyr equivalent) that abolishes *xbp-1*
  splicing while retaining kinase activity — isolates the endoribonuclease MF in vivo.
- **In-vitro cleavage** of a *C. elegans xbp-1* stem-loop by recombinant IRE-1 cytoplasmic module,
  with 2′,3′-cyclic-phosphate product characterization — confirms mechanism class.

---

## Curation Leads (require curator verification)

- **Lead 1 — Reject/de-prioritize GO:0016788 as an added annotation.** Rationale: redundant with
  existing GO:0016787 + GO:0004521; not on the lineage of the specific term in current GO;
  mechanism mismatch with its hydrolytic nuclease children.
- **Lead 2 — Retain/strengthen GO:0004521 (RNA endonuclease activity)** as the core MF, upgrading
  evidence with orthologous direct-assay references (PMID 11780124) if the review model permits
  ISS-with-mouse support alongside worm IMP.
- **Candidate references to verify:**
  - PMID **11780124** — snippet: *"Purified mouse IRE1 accurately cleaved XBP-1 mRNA in vitro… a direct target of IRE1 endonucleolytic activity."*
  - PMID **11779465** — snippet: *"C. elegans requires ire-1-mediated splicing of xbp-1 mRNA for UPR gene transcription and survival upon ER stress."*
  - PMID **21729333** — snippet: Ire1 RNase uses His1061/Tyr1043 general acid/base and coordinates the *scissile phosphate*.
  - PMID **36389122** — snippet: *"IRE-1 endoribonuclease activity declines early in"* (worm).
- **Suggested curator question:** "Does our GO release place GO:0016788 as an ancestor of GO:0004521?
  If not, GO:0016788 should not be represented as the specific term's parent."
- **Suggested experiment:** RNase-dead separation-of-function *ire-1* allele + in-vitro *xbp-1*
  stem-loop cleavage to nail the worm-specific direct MF and mechanism class.

---

### Provenance
Computed checks run (executed code + outputs retained in the job log):
UniProt Q09499 REST fetch (domains + 16 GO annotations); QuickGO ancestry queries for GO:0004521,
GO:0004518, GO:0004540, and GO:0000213; children of GO:0016788; QuickGO term search for
IRE1/endoribonuclease/tRNA-splicing terms (no dedicated IRE1 MF term exists). Literature via PubMed
(PMIDs above).
Where worm-specific direct biochemistry was unavailable, it is stated as such and not fabricated.

**Artifact files (computed provenance):**
- `go_decision_table.csv` — per-term GO curation decision table (predicted vs annotated terms, recommended actions, rationale).
- `ontology_relationship_tests.csv` — computed QuickGO ancestry tests (GO:0016788 is not an ancestor of GO:0004521; the mechanistic analog GO:0000213 is a lyase, not under GO:0016788).


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)
- [OpenScientist go decision table](openscientist_artifacts/go_decision_table.csv)
- [OpenScientist ontology relationship tests](openscientist_artifacts/ontology_relationship_tests.csv)