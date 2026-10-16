---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-21T00:00:51.631294'
end_time: '2026-09-21T00:24:08.847890'
duration_seconds: 1397.22
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: human
  gene: SGMS2
  gene_symbol: SGMS2
  uniprot_accession: Q8NHU3
  taxon_id: NCBITaxon:9606
  taxon_label: Homo sapiens
  focus_type: function_assignment
  hypothesis_slug: wild-type-er-activity-and-export-signal
  hypothesis_text: Assess whether normal human SGMS2 Q8NHU3 and SGMS1 Q86VZ5 retain
    activity at ER membrane (GO0005789 is_active_in), separately from ER transit and
    disease-variant retention. Both exact PTHR21290 leaves (SGMS2 PTN002501709; SGMS1
    PTN002501710) descend from positive ER IBD PTN000480004. Source support includes
    SAMD8 Q96LT4 and fly FBgn0052380; donor identity, donor count, and a predominant
    Golgi/plasma-membrane location are not evidence of target-specific loss. Full
    primary36102623 Fig1 shows an autonomous ER-export signal through SMSr/SMS2 chimera
    experiments, and wild-type Golgi/PM distribution versus active ER-retained SMS2
    variants (also30779713). This is target-specific trafficking evidence that must
    be assessed, not dismissed as merely lack of a human experiment. Read full primary
    methods and later wild-type localization/activity literature. Distinguish capacity
    to catalyze when artificially retained from physiological ER activity; do not
    presume secretory transit implies catalysis. Judge ancestral node placement and
    actual conserved/lost localization without inventing MSA/residue claims. SGMS1
    has its own localization evidence; do not assume paralogs identical. Note30779713
    Arg50* interpretation is qualified by36102623 Discussion alternative initiation,
    explicitly unpublished data. Do not duplicate already resolved PC versus CDP-choline
    or PE versus CDP-ethanolamine chemistry questions.
  term_context: No specific term context supplied.
  reference_context: No specific reference context supplied.
  source_file: genes/human/SGMS2/SGMS2-ai-review.yaml
  source_selector: free-text
  source_context_yaml: "hypothesis: Assess whether normal human SGMS2 Q8NHU3 and SGMS1\
    \ Q86VZ5 retain activity at ER membrane (GO0005789\n  is_active_in), separately\
    \ from ER transit and disease-variant retention. Both exact PTHR21290 leaves\n\
    \  (SGMS2 PTN002501709; SGMS1 PTN002501710) descend from positive ER IBD PTN000480004.\
    \ Source support includes\n  SAMD8 Q96LT4 and fly FBgn0052380; donor identity,\
    \ donor count, and a predominant Golgi/plasma-membrane\n  location are not evidence\
    \ of target-specific loss. Full primary36102623 Fig1 shows an autonomous ER-export\n\
    \  signal through SMSr/SMS2 chimera experiments, and wild-type Golgi/PM distribution\
    \ versus active ER-retained\n  SMS2 variants (also30779713). This is target-specific\
    \ trafficking evidence that must be assessed, not\n  dismissed as merely lack\
    \ of a human experiment. Read full primary methods and later wild-type localization/activity\n\
    \  literature. Distinguish capacity to catalyze when artificially retained from\
    \ physiological ER activity;\n  do not presume secretory transit implies catalysis.\
    \ Judge ancestral node placement and actual conserved/lost\n  localization without\
    \ inventing MSA/residue claims. SGMS1 has its own localization evidence; do not\
    \ assume\n  paralogs identical. Note30779713 Arg50* interpretation is qualified\
    \ by36102623 Discussion alternative\n  initiation, explicitly unpublished data.\
    \ Do not duplicate already resolved PC versus CDP-choline or\n  PE versus CDP-ethanolamine\
    \ chemistry questions.\nfocus_type: function_assignment\ncontext: []\nreference_id:\
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
citation_count: 9
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

- **Organism code:** human
- **Taxon:** Homo sapiens (NCBITaxon:9606)
- **Gene directory:** SGMS2
- **Gene symbol:** SGMS2
- **UniProt accession:** Q8NHU3

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** wild-type-er-activity-and-export-signal
- **Source file:** genes/human/SGMS2/SGMS2-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

Assess whether normal human SGMS2 Q8NHU3 and SGMS1 Q86VZ5 retain activity at ER membrane (GO0005789 is_active_in), separately from ER transit and disease-variant retention. Both exact PTHR21290 leaves (SGMS2 PTN002501709; SGMS1 PTN002501710) descend from positive ER IBD PTN000480004. Source support includes SAMD8 Q96LT4 and fly FBgn0052380; donor identity, donor count, and a predominant Golgi/plasma-membrane location are not evidence of target-specific loss. Full primary36102623 Fig1 shows an autonomous ER-export signal through SMSr/SMS2 chimera experiments, and wild-type Golgi/PM distribution versus active ER-retained SMS2 variants (also30779713). This is target-specific trafficking evidence that must be assessed, not dismissed as merely lack of a human experiment. Read full primary methods and later wild-type localization/activity literature. Distinguish capacity to catalyze when artificially retained from physiological ER activity; do not presume secretory transit implies catalysis. Judge ancestral node placement and actual conserved/lost localization without inventing MSA/residue claims. SGMS1 has its own localization evidence; do not assume paralogs identical. Note30779713 Arg50* interpretation is qualified by36102623 Discussion alternative initiation, explicitly unpublished data. Do not duplicate already resolved PC versus CDP-choline or PE versus CDP-ethanolamine chemistry questions.

## Term and Decision Context

No specific term context supplied.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: Assess whether normal human SGMS2 Q8NHU3 and SGMS1 Q86VZ5 retain activity at ER membrane (GO0005789
  is_active_in), separately from ER transit and disease-variant retention. Both exact PTHR21290 leaves
  (SGMS2 PTN002501709; SGMS1 PTN002501710) descend from positive ER IBD PTN000480004. Source support includes
  SAMD8 Q96LT4 and fly FBgn0052380; donor identity, donor count, and a predominant Golgi/plasma-membrane
  location are not evidence of target-specific loss. Full primary36102623 Fig1 shows an autonomous ER-export
  signal through SMSr/SMS2 chimera experiments, and wild-type Golgi/PM distribution versus active ER-retained
  SMS2 variants (also30779713). This is target-specific trafficking evidence that must be assessed, not
  dismissed as merely lack of a human experiment. Read full primary methods and later wild-type localization/activity
  literature. Distinguish capacity to catalyze when artificially retained from physiological ER activity;
  do not presume secretory transit implies catalysis. Judge ancestral node placement and actual conserved/lost
  localization without inventing MSA/residue claims. SGMS1 has its own localization evidence; do not assume
  paralogs identical. Note30779713 Arg50* interpretation is qualified by36102623 Discussion alternative
  initiation, explicitly unpublished data. Do not duplicate already resolved PC versus CDP-choline or
  PE versus CDP-ethanolamine chemistry questions.
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

# SGMS2 (Q8NHU3) — "is_active_in ER membrane" (GO:0005789): Function-Assignment Review

**Hypothesis slug:** wild-type-er-activity-and-export-signal
**Focus type:** function_assignment
**Question:** Does wild-type human SGMS2 (SMS2, Q8NHU3) — and by extension SGMS1 (SMS1, Q86VZ5) — physiologically execute its catalytic (sphingomyelin synthase) function **at the ER membrane** (GO:0005789, `is_active_in`), separately from ER transit and disease-variant retention?

---

## Executive Judgment

**Verdict: Refuted for wild-type physiological ER activity (equivalently: the ER-membrane `is_active_in` annotation is over-annotated / a paralog IBD carry-over).**

Target-specific human evidence does not support wild-type SMS2 catalysis at the ER. On the contrary, the most direct evidence — an **autonomous ER-export signal** in SMS2 — shows the protein is actively removed from the ER, and its physiological sphingomyelin (SM) synthesis occurs downstream at the **trans-Golgi and plasma membrane**. ER-localized catalysis is observed **only** for export-defective pathogenic variants (p.Ile62Ser, p.Met64Arg), where it is a **pathological gain of location**, not the wild-type function. The ER-positive PANTHER IBD ancestral node (PTN000480004) is anchored by the genuinely ER-resident sibling **SMSr/SAMD8** (a ceramide-phosphoethanolamine synthase) and a fly ortholog; propagating that ER activity to the SMS2/SMS1 leaves is classic paralog over-annotation.

**Most important caveats.** (1) This is a location-of-function judgment, not a catalytic-capacity judgment: when artificially/pathologically retained in the ER, SMS2 *can* catalyze SM synthesis there ("retain full enzymatic activity"). The GO `is_active_in ER membrane` claim for the **wild-type** gene product nonetheless fails because physiological activity is spatially restricted away from the ER by the export signal. (2) SGMS1 has its own (Golgi) localization evidence and should not be assumed identical to SGMS2; neither paralog has positive wild-type ER-activity evidence. (3) The seed's request to treat the trafficking data as "target-specific evidence to be assessed, not dismissed" is honored — and when read fully, that trafficking evidence argues *against* wild-type ER activity.

---

## Evidence Matrix

| Citation | Evidence type | Stance | Claim tested | Key finding | Context | Confidence / limitations |
|---|---|---|---|---|---|---|
| **PMID:36102623** (Sokoya, Parolek, Holthuis et al., *eLife* 2022) | Direct assay + mutant phenotype + trafficking (SMSr/SMS2 chimera, Fig 1) | **Refutes WT ER activity / qualifies** | Where does WT SMS2 execute catalysis; is ER activity WT or variant-specific | WT SMS2 carries an **autonomous ER-export signal** and leaves the ER; severe pathogenic variants (I62S, M64R) "retain full enzymatic activity but fail to leave the ER owing to a defective autonomous ER export signal," accumulating SM in the ER. Physiological SM production is in the **trans-Golgi**. | Human SMS2 + chimeras; patient-derived fibroblasts | High. This is a *human, target-specific* study. It is the strongest evidence and it points away from WT ER activity. |
| **PMID:30779713** (Pekkinen et al., *JCI Insight* 2019; also fig cited by seed) | Mutant phenotype + localization | **Refutes WT ER activity / qualifies** | Origin of ER SM synthesis | SMS2 is described as **plasma-membrane-resident**; p.Ile62Ser and p.Met64Arg "enhanced the rate of de novo sphingomyelin production **by blocking export of a functional enzyme from the endoplasmic reticulum**"; p.Arg50* is **catalytically inactive**. | 6 families; osteoporosis / spondylometaphyseal dysplasia | High for the export-block mechanism. Arg50* alternative-initiation nuance (see Conflicts) does not affect the ER-activity verdict. |
| **PMID:14685263** (Huitema, van den Dikkenberg, Brouwers, Holthuis, *EMBO J* 2004) | Localization / functional cloning | **Refutes ER `is_active_in`** | WT physiological site of SMS2/SMS1 | "human SMS1 is localised to the Golgi, SMS2 resides primarily at the plasma membrane"; "SM synthesis occurs in the lumen of the Golgi as well as on the cell surface." | Human/mouse/C. elegans; yeast complementation | High. Foundational localization paper. No ER catalysis attributed to SMS1/SMS2. |
| **PMID:19506037** (Vacaru et al., *J Cell Biol* 2009) | Localization / direct assay | **Refutes (for SMS1) / competing** | Where SMS1 makes SM; identity of ER member | Ceramide is made on the cytosolic ER surface and "transported by ceramide transfer protein to the Golgi for conversion to sphingomyelin (SM) by SM synthase SMS1"; SMSr makes CPE in the **ER lumen** (~300× less product). | Human/mammalian cells | High. Places **SMS1 (SGMS1) SM synthesis at the Golgi**, ER member is SMSr. |
| **PMID:24259670** (Tafesse/Holthuis) | Localization / mutant | **Competing / provenance of ER term** | Identity of ER-resident family member | "SMSr **(SAMD8), an ER-resident** ceramide phosphoethanolamine (CPE) synthase"; ER ceramide-homeostasis sensor. | Mammalian cells | High. Confirms SAMD8/SMSr as the true ER member = the IBD donor. |
| **PMID:21980337** (Subathra et al.) | Localization | **Refutes ER `is_active_in`** | WT localization of SMS1 & SMS2 | "SMS1 localizes at the Golgi while SMS2 localizes both at the Golgi and the plasma membrane." | Mammalian cells | High. Independent-lab confirmation; neither paralog ER-localized. |
| **PANTHER PTN000480004** (ER-positive IBD ancestral node) → leaves SMS2 PTN002501709, SMS1 PTN002501710 | Evolutionary / computational (IBD) | **Competing / source of over-annotation** | Whether ER activity should be inherited by SMS2/SMS1 | ER-positive call is anchored by **SAMD8/SMSr (Q96LT4)** — a genuinely ER-resident CPE synthase (PMID:19506037, 24259670) — and fly **FBgn0052380**. SMS1/SMS2 evolved Golgi/PM residence (SMS2 via an ER-export signal), so IBD inheritance mislocates the function. | Ortholog inference; not a target-specific assay | Medium-high as an *explanation* for the annotation's provenance; low as *support* for WT SMS1/SMS2 ER activity. |

---

## GO Curation Implications (leads — require curator verification)

**Lead 1 — Do not assert wild-type ER-membrane `is_active_in` for SGMS2.**
- **CC (location of function):** GO:0005789 (endoplasmic reticulum membrane) with `is_active_in` should be **removed / not asserted** for wild-type SGMS2. If any ER relationship is kept, it should at most be a transient `located_in` reflecting biogenesis/transit — which is not a function-execution statement and is generally not curated as `is_active_in`.
- **Preferred CC `is_active_in` for SGMS2:** **GO:0005886** (plasma membrane) and **GO:0000139** (Golgi membrane) / trans-Golgi network membrane. (PMID:14685263; PMID:36102623.)
- **Preferred CC `is_active_in` for SGMS1:** **GO:0000139** (Golgi membrane). Do not copy an ER term from SGMS2 or from the IBD node.
- **MF (unchanged, not the focus):** **GO:0033188** sphingomyelin synthase activity. The seed explicitly asks not to re-litigate PC-vs-CDP-choline chemistry; MF is retained.
- **Disease-variant ER activity** (I62S, M64R) is a **variant/pathological** observation and should not become a wild-type gene-product CC annotation. If captured, it belongs in variant/phenotype curation (GO-CAM disease model), not as `is_active_in ER membrane` for the reference gene product.

**Lead 2 — Flag the IBD node (confirmed by QuickGO evidence codes, Iteration 3).** Direct QuickGO retrieval shows the ER-membrane term on the human leaves is **IBA-only**, propagated from the ancestral node whose ER call is experimentally anchored by the ER-resident sibling SAMD8/SMSr and the fly ortholog. Curators should down-weight this IBA-only ER support and rely on the direct experimental (IDA) evidence, which places SGMS2/SGMS1 at Golgi/PM.

**GO decision table (grounded in current QuickGO evidence codes; leads requiring curator verification):**

| Gene | GO term | Current evidence | Experimental support for ER? | Curation lead |
|---|---|---|---|---|
| SGMS2 Q8NHU3 | GO:0005789 ER membrane | **IBA only** (GO_REF:0000033; with = FBgn0052380, PANTHER PTN000480004, Q96LT4/SAMD8) | **None** | **Remove / do not assert `is_active_in`**; ER is transit-only at most |
| SGMS2 Q8NHU3 | GO:0000139 Golgi membrane | IDA PMID:14685263 (+ IBA/IEA) | Direct | Retain (`is_active_in`/`located_in`) |
| SGMS2 Q8NHU3 | GO:0005886 plasma membrane | IDA PMID:14685263, PMID:30779713; TAS Reactome | Direct | Retain (`is_active_in`/`located_in`) |
| SGMS1 Q86VZ5 | GO:0005789 ER membrane | **IBA only** (same with-list); old TAS GO:0005783 whole-ER PMID:14976195 | **None (membrane-level)** | **Remove / do not assert `is_active_in`** |
| SGMS1 Q86VZ5 | GO:0000139 / GO:1990676 Golgi (trans-cisterna) membrane | IDA PMID:14685263, PMID:30242129; EXP PMID:17449912 | Direct | Retain |
| SAMD8 Q96LT4 (SMSr) | GO:0005789 ER membrane | **IDA PMID:19506037** (+ IEA, TAS) | **Direct** | Retain — correct here; the true ER member / IBD donor |

*Provenance artifacts:* `/tmp/SGMS2_ER_evidence_matrix.csv`, `/tmp/SGMS2_GO_decision_table.csv` (generated from live QuickGO annotation queries this run).

Avoid "protein binding" as an endpoint here — the informative MF/CC terms above are supported.

---

## Mechanistic Scope

- **Immediate molecular function:** transfer of phosphocholine from phosphatidylcholine onto ceramide → sphingomyelin + diacylglycerol (sphingomyelin synthase; GO:0033188). Catalytic site faces the **lumenal/exoplasmic** leaflet.
- **Physiological location of that function:** trans-Golgi lumen (SMS1, SMS2) and cell-surface/plasma membrane (SMS2). SM production in the trans-Golgi builds the SM/sterol gradient of the secretory pathway (PMID:36102623 intro).
- **What is downstream / not direct gene-product function at the ER:** (a) the ER SM accumulation, disrupted transbilayer SM asymmetry, and altered cholesterol/glycerophospholipid order seen in patient cells are **consequences of variant ER retention**, not WT ER catalysis; (b) osteoporosis/skeletal dysplasia are organ-level disease manifestations, not molecular-function locations.

---

## Conflicts and Alternatives

1. **"Retained variants are active in the ER, so the enzyme *can* act there."** True but non-physiological. `is_active_in` for a reference gene product should reflect where the **wild-type** enzyme acts; the export signal restricts that to post-ER compartments. Catalytic *capacity* ≠ physiological *location of activity*. (The seed makes exactly this distinction.)
2. **Paralog confusion (the dominant alternative).** SMSr/SAMD8 is legitimately ER-active (CPE synthesis). An ER annotation is correct for SAMD8 and is the likely IBD source; it should not be transferred to SMS2/SMS1.
3. **Arg50* interpretation.** PMID:30779713 calls p.Arg50* catalytically inactive; PMID:36102623 Discussion qualifies this via possible alternative translation initiation (explicitly unpublished). This nuance concerns the *loss-of-function* variant, not the ER-activity question, and does not change the verdict.
4. **Secretory transit ≠ catalysis.** All secretory-pathway membrane enzymes fold in and traverse the ER; transit alone is not evidence of ER `is_active_in`. No study reports meaningful WT SM synthesis in the ER.
5. **Isoform/paralog specificity.** SGMS1 evidence is Golgi-specific; do not assume SGMS1 = SGMS2. Neither has positive WT ER-activity data.

---

## Knowledge Gaps

| Gap | What was checked | Why it matters | What would resolve it |
|---|---|---|---|
| Direct measurement of WT SMS2 SM-synthase activity *in the ER* vs Golgi/PM | Abstracts of PMID 36102623/30779713/14685263 | Confirms activity is spatially excluded from ER in WT | Organelle-resolved SM-synthase assays / proximity biosensors on WT vs export-defective SMS2 (partly done in 36102623 — full-text figures would quantify) |
| Exact provenance of the ER annotation in the GO record | Inferred as PANTHER IBD from node PTN000480004 | Determines whether removal is a clean IBD down-weight or overrides experimental evidence | Curator inspection of the SGMS2 GO evidence codes and GO-CAM model |
| SGMS1 (Q86VZ5) trafficking / any residual ER function | Now checked: Golgi localization confirmed independently (PMID:14685263, 21980337) and SM synthesis assigned to the Golgi (PMID:19506037); ER member is SMSr/SAMD8 | Seed warns paralogs may differ — addressed: SGMS1 also lacks WT ER-activity evidence | Direct SMS1 organelle-resolved activity assay would fully close it, but current evidence already argues against ER `is_active_in` for SGMS1 |
| Topology detail (leaflet facing) for SMS2 at PM vs Golgi | Not independently verified here | Supports lumenal/exoplasmic catalytic orientation consistent with Golgi/PM function | Cited in family literature; full-text/topology papers |

I could not fetch every abstract via automated PubMed search (the endpoint returned no hits for some multi-term queries); I therefore retrieved the four decisive papers directly by PMID via NCBI E-utilities and quote them verbatim above. I did not access the eLife or JCI Insight full-text figures programmatically; figure-level claims (Fig 1 chimera design) are taken from the seed and the abstracts and are labeled as such.

---

## Discriminating Tests

1. **Organelle-resolved catalysis assay:** compartment-specific SM biosensors (e.g., EGFP-lysenin / EqtSM) or in-vitro SM-synthase assays on purified ER vs Golgi vs PM fractions, comparing WT SMS2 to an export-signal-ablated construct. Prediction: WT shows Golgi/PM activity, negligible ER; export mutant shows ER activity.
2. **Export-signal swap (already the crux of PMID:36102623):** confirm that grafting the SMS2 ER-export signal onto ER-resident SMSr relocalizes it, and that removing it retains SMS2 in the ER — directly separating "transit" from "activity."
3. **Retention-clamp control:** KDEL/ER-anchor–tagged WT SMS2 to demonstrate that ER catalysis is achievable but requires forced retention (i.e., non-physiological).
4. **SGMS1 parallel experiments** to test the paralog-difference assumption explicitly.

---

## Curation Leads (require curator verification)

- **Candidate action change:** Change/remove the wild-type SGMS2 `is_active_in` GO:0005789 (ER membrane) annotation; treat ER involvement as transit-only (`located_in`, transient) or as variant-specific pathology, not core function.
- **Candidate replacement CC terms (SGMS2):** GO:0005886 (plasma membrane) `is_active_in`; GO:0000139 (Golgi membrane) `is_active_in`.
- **Candidate CC term (SGMS1):** GO:0000139 (Golgi membrane) `is_active_in`; do not add ER by paralog inheritance.
- **Retain (not the focus):** GO:0033188 sphingomyelin synthase activity (MF).
- **Candidate references to verify with exact snippets:**
  - PMID:36102623 — "SMS2 variants linked to the most severe bone phenotypes retain full enzymatic activity but fail to leave the ER owing to a defective autonomous ER export signal."
  - PMID:30779713 — variants "enhanced the rate of de novo sphingomyelin production by blocking export of a functional enzyme from the endoplasmic reticulum"; "p.Arg50* mutation yielded a catalytically inactive enzyme."
  - PMID:14685263 — "human SMS1 is localised to the Golgi, SMS2 resides primarily at the plasma membrane."
- **Suggested curator questions:** (1) Did the ER-membrane term originate from PANTHER IBD node PTN000480004? (2) Is there any experimental (non-IBD) evidence code for ER `is_active_in` on SGMS2/SGMS1? If not, down-weight. (3) Should disease-variant ER activity be modeled in a separate GO-CAM disease context?
- **Suggested experiments:** organelle-resolved SM-synthase assay (WT vs export-defective SMS2); SGMS1 trafficking/activity mapping.

---

### One-line answer
For wild-type human SGMS2 (and SGMS1), physiological catalysis occurs at the Golgi/plasma membrane, not the ER; the ER-membrane `is_active_in` (GO:0005789) annotation is unsupported by target-specific evidence and is best explained as a PANTHER-IBD carry-over from the ER-resident paralog SMSr/SAMD8, with true ER catalysis seen only as a pathological consequence of export-defective disease variants.


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)