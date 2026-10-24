---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-21T02:23:25.718886'
end_time: '2026-09-21T02:38:09.061186'
duration_seconds: 883.34
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: yeast
  gene: FUN19
  gene_symbol: FUN19
  uniprot_accession: P28003
  taxon_id: NCBITaxon:559292
  taxon_label: Saccharomyces cerevisiae
  focus_type: function_assignment
  hypothesis_slug: transcription-coactivation-after-ada2-saga-divergence
  hypothesis_text: Saccharomyces cerevisiae FUN19 (P28003; YAL034C) has transcription
    coactivator activity and positively regulates DNA-templated transcription. Actual
    PANTHER tree confirms target PTN000271934 below root function node PTN000271860
    and fungal PTN000271931. The latter retains Rpd3L-Expanded association but carries
    an explicit IRD loss of SAGA-type-complex membership (GO:0070461), not loss of
    coactivator activity. FUN19 lacks Ada2 ZZ/SANT domains but retains SWIRM; those
    losses may change complex context without eliminating every activation mechanism.
    Evaluate direct or ortholog evidence for transcriptional directionality and relevant
    interfaces. GO:0070210 is not fission-yeast-specific and chromatin remodeling
    does not require the target itself to be an ATPase. Distinguish generic chromatin/regulatory
    roles from positive coactivation and evaluate the actual ancestral judgment rather
    than treating a sibling-subfamily donor as automatically invalid.
  term_context: No specific term context supplied.
  reference_context: No specific reference context supplied.
  source_file: genes/yeast/FUN19/FUN19-ai-review.yaml
  source_selector: free-text
  source_context_yaml: "hypothesis: Saccharomyces cerevisiae FUN19 (P28003; YAL034C)\
    \ has transcription coactivator activity and\n  positively regulates DNA-templated\
    \ transcription. Actual PANTHER tree confirms target PTN000271934 below\n  root\
    \ function node PTN000271860 and fungal PTN000271931. The latter retains Rpd3L-Expanded\
    \ association\n  but carries an explicit IRD loss of SAGA-type-complex membership\
    \ (GO:0070461), not loss of coactivator\n  activity. FUN19 lacks Ada2 ZZ/SANT\
    \ domains but retains SWIRM; those losses may change complex context\n  without\
    \ eliminating every activation mechanism. Evaluate direct or ortholog evidence\
    \ for transcriptional\n  directionality and relevant interfaces. GO:0070210 is\
    \ not fission-yeast-specific and chromatin remodeling\n  does not require the\
    \ target itself to be an ATPase. Distinguish generic chromatin/regulatory roles\
    \ from\n  positive coactivation and evaluate the actual ancestral judgment rather\
    \ than treating a sibling-subfamily\n  donor as automatically invalid.\nfocus_type:\
    \ function_assignment\ncontext: []\nreference_id: []"
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
citation_count: 4
artifact_count: 5
artifact_sources:
  openscientist_artifacts_zip: 5
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
- filename: provenance_FUN19_GO_decision_table.csv
  path: openscientist_artifacts/provenance_FUN19_GO_decision_table.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist FUN19 GO decision table
- filename: provenance_FUN19_IntAct_curated_interactions.csv
  path: openscientist_artifacts/provenance_FUN19_IntAct_curated_interactions.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist FUN19 IntAct curated interactions
- filename: provenance_FUN19_STRING_partners.csv
  path: openscientist_artifacts/provenance_FUN19_STRING_partners.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist FUN19 STRING partners
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
- **Gene directory:** FUN19
- **Gene symbol:** FUN19
- **UniProt accession:** P28003

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** transcription-coactivation-after-ada2-saga-divergence
- **Source file:** genes/yeast/FUN19/FUN19-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

Saccharomyces cerevisiae FUN19 (P28003; YAL034C) has transcription coactivator activity and positively regulates DNA-templated transcription. Actual PANTHER tree confirms target PTN000271934 below root function node PTN000271860 and fungal PTN000271931. The latter retains Rpd3L-Expanded association but carries an explicit IRD loss of SAGA-type-complex membership (GO:0070461), not loss of coactivator activity. FUN19 lacks Ada2 ZZ/SANT domains but retains SWIRM; those losses may change complex context without eliminating every activation mechanism. Evaluate direct or ortholog evidence for transcriptional directionality and relevant interfaces. GO:0070210 is not fission-yeast-specific and chromatin remodeling does not require the target itself to be an ATPase. Distinguish generic chromatin/regulatory roles from positive coactivation and evaluate the actual ancestral judgment rather than treating a sibling-subfamily donor as automatically invalid.

## Term and Decision Context

No specific term context supplied.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: Saccharomyces cerevisiae FUN19 (P28003; YAL034C) has transcription coactivator activity and
  positively regulates DNA-templated transcription. Actual PANTHER tree confirms target PTN000271934 below
  root function node PTN000271860 and fungal PTN000271931. The latter retains Rpd3L-Expanded association
  but carries an explicit IRD loss of SAGA-type-complex membership (GO:0070461), not loss of coactivator
  activity. FUN19 lacks Ada2 ZZ/SANT domains but retains SWIRM; those losses may change complex context
  without eliminating every activation mechanism. Evaluate direct or ortholog evidence for transcriptional
  directionality and relevant interfaces. GO:0070210 is not fission-yeast-specific and chromatin remodeling
  does not require the target itself to be an ATPase. Distinguish generic chromatin/regulatory roles from
  positive coactivation and evaluate the actual ancestral judgment rather than treating a sibling-subfamily
  donor as automatically invalid.
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

# FUN19 (P28003 / YAL034C) — Transcription Coactivation After Ada2/SAGA Divergence

**Focus type:** function_assignment
**Hypothesis slug:** transcription-coactivation-after-ada2-saga-divergence
**Target:** *Saccharomyces cerevisiae* FUN19 (UniProt P28003; systematic name YAL034C)

---

## Executive Judgment

**Verdict: REFUTED / OVER-ANNOTATED.**

The seed hypothesis proposes that FUN19 has **transcription coactivator activity** (GO:0003713) and **positively regulates DNA-templated transcription** (GO:0045893), reasoning that although FUN19 lost the Ada2 ZZ/SANT domains and SAGA-complex membership, it retained SWIRM and therefore may keep "some activation mechanism." The evidence assembled across three investigative iterations does not support this. Every strand of evidence — domain architecture, existing GO annotation set, and both aggregated (STRING) and curated (IntAct) interaction data — points away from positive coactivation and, where it points anywhere, points toward a **repressive (Rpd3L/Sin3 histone-deacetylase) context** or toward **chaperone/nuclear-import associations** that have nothing to do with transcriptional activation.

The core logical flaw in the seed hypothesis is that it treats the retained **SWIRM domain** as a residual activation module. Primary structural work on the SAGA HAT module shows the opposite: SWIRM is a **tethering/interaction module**, not a catalytic or intrinsically coactivating element. The domains that actually confer Ada2's coactivator function — the ZZ-type zinc finger and the SANT domain, which stabilize Gcn5 and the histone-acetyltransferase reaction — are exactly the domains FUN19 has **lost**. Retaining the "docking" piece while losing the "business end" is not a conservative basis for inferring retained activation.

The most important caveats: (1) FUN19 is an essentially **uncharacterized, non-essential gene** with no experimental FUNCTION or SUBUNIT annotation in UniProt, so the case is built on comparative/interaction inference rather than a direct assay that refutes coactivation; (2) all four current GO annotations are **IBA (phylogenetic inference, GO_Central)** with no experimental backing, so the annotation baseline itself is weak in both directions; and (3) the STRING SIN3 signal, while the strongest experimental partner, is aggregated high-throughput co-occurrence rather than a validated binary complex membership. The recommendation is therefore to **reject the coactivator / positive-regulation assignment** and retain only the neutral IBA-level chromatin terms pending direct experimental evidence.

---

## Key Findings

### F001 — FUN19 retained only SWIRM and lost the Ada2 domains that confer coactivator function

FUN19 (UniProt P28003; YAL034C; 413 aa) carries a **single annotated structured domain — SWIRM (residues 316–413; Pfam PF04433; PROSITE PS50934)** — plus three disordered/low-complexity regions. It has **no HAT domain, no bromodomain, no ZZ-type zinc finger, and no SANT domain**. This is in direct architectural contrast to yeast **ADA2 (UniProt Q02336; YDR448W; 434 aa)**, which carries a **ZZ-type zinc finger (residues 2–58), a SANT domain (60–112), and a SWIRM domain (349–434)**. ADA2 is one of the ~19 subunits of the SAGA coactivator complex (TRA1, SPT7, TAF5, NGG1/ADA3, ADA2, GCN5, …). **FUN19 is not in the SAGA subunit list.** Both proteins fall within PANTHER family PTHR12374 (ADA2-related), but FUN19 sits in the distinct **subfamily SF21 (FUN19-related)**, consistent with an ancient duplication/divergence event rather than orthology to functional Ada2.

The mechanistic significance of this domain loss is established by primary structural work on the SAGA HAT module ([PMID: 36965704](https://pubmed.ncbi.nlm.nih.gov/36965704/)):

> *"A minimal HAT module complex containing Gcn5 bound to Ada2 and Ada3 is required for full Gcn5 activity on nucleosomes."*

This establishes that Ada2's coactivator (histone-acetyltransferase) role depends on the assembled Ada2/Ada3/Gcn5 module. The domains Ada2 uses to build and stabilize that module — beyond SWIRM — are precisely the ZZ and SANT domains FUN19 lacks. The same paper further clarifies what SWIRM actually does:

> *"the SWIRM domain is required for incorporation of the HAT module into the yeast SAGA complex, but not the ADA complex."*

SWIRM is therefore a **tethering/interaction module** that helps dock the HAT module into SAGA — it is not a catalytic or intrinsically activating element. Its presence in FUN19 does **not** by itself imply any coactivator activity. The seed hypothesis's premise ("retains SWIRM; those losses may change complex context without eliminating every activation mechanism") is thus undermined at the structural level: FUN19 kept the docking peg and discarded the machine.

### F002 — Existing FUN19 GO annotations are neutral or repressive in context and are entirely IBA

All four current FUN19 (P28003) GO annotations are **IBA:GO_Central** — phylogenetic inference from GO Central, with **no experimental support**:

| Aspect | GO ID | Term | Directionality |
|--------|-------|------|----------------|
| CC | GO:0070210 | Rpd3L-Expanded complex | **Repressive (HDAC)** |
| MF | GO:0003682 | chromatin binding | Neutral |
| BP | GO:0006338 | chromatin remodeling | Neutral |
| BP | GO:0006357 | regulation of transcription by RNA Pol II | **Direction-neutral** |

Critically, **neither GO:0003713 (transcription coactivator activity, MF) nor GO:0045893 (positive regulation of DNA-templated transcription, BP) is currently annotated** to FUN19. The seed hypothesis is proposing to *add* activation-directional terms that the existing curated set does not contain. Moreover, the one complex context that *was* propagated — **Rpd3L-Expanded (GO:0070210)** — is a **histone-deacetylase (repressive) assembly**, i.e., opposite in sign to "positive" coactivation. UniProt lists **no experimental FUNCTION or SUBUNIT comment** for FUN19 (only that it is a non-essential gene and a phosphoprotein). The existing annotation baseline therefore offers no support for adding activation directionality and, if anything, its only complex-level context leans repressive.

### F003 — FUN19's strongest experimental interaction is SIN3 (co-repressor scaffold); SAGA links are database carry-over

STRING (*S. cerevisiae*, YAL034C) interaction partners were examined by evidence channel. The highest **experimental-evidence (escore)** partners are the **co-repressor scaffold SIN3 (escore = 0.755)**, KAP123 (0.727), TAF1 (0.668), ADH1 (0.625), and TAF5 (0.608). By contrast, **all recovered SAGA subunits** — GCN5, ADA2, NGG1/ADA3, SPT7, SPT20, SPT3, SPT8, TRA1, SGF29, SGF73, SUS1, HFI1 — have **escore = 0.000** and a uniform **dscore = 0.540**, meaning they derive from **database/complex co-annotation, not from any experiment**. In other words, the apparent "SAGA membership" that seeds the coactivator hypothesis is a **database artifact**: it is co-annotation transfer, not experimental co-purification. Among curated complex subunits, FUN19's only genuine experimental interaction signal maps to **SIN3**, the scaffold of the **Rpd3L/Rpd3S co-repressor** — again a repressive, not activating, context.

### F004 — Curated IntAct interactions place FUN19 with chaperones and nuclear-import factors, not any coactivator complex

Curated IntAct/PSICQUIC experimental interactions for P28003 are **dominated by molecular chaperones and folding machinery**: Ssa1 (Hsp70), Hsc82 (Hsp90), Hsp104, Sse2, Gim4 (prefoldin), Aha1, and Csa1 — recovered via tandem affinity purification in the chaperone interaction network ([PMID: 19536198](https://pubmed.ncbi.nlm.nih.gov/19536198/)) — plus **KAP123** (karyopherin/nuclear import; TAP, [PMID: 16429126](https://pubmed.ncbi.nlm.nih.gov/16429126/)) and a two-hybrid self-association ([PMID: 14690591](https://pubmed.ncbi.nlm.nih.gov/14690591/)). There is **no curated FUN19–Sin3 or FUN19–SAGA binary interaction** in IntAct. This has two implications. First, it further confirms that FUN19 is **not a validated member of any transcription coactivator complex**. Second, it tempers the STRING SIN3 signal: the escore of 0.755 reflects **aggregated high-throughput co-occurrence** rather than an established stable complex, so even the repressive-context lead should be treated as **suggestive, not proof** of Rpd3L subunit status. The chaperone-heavy interactome is more consistent with a protein that is metastable/poorly folded on its own, or that is captured non-specifically by folding machinery, than with a stably assembled transcriptional coactivator.

---

## Mechanistic Model / Interpretation

The seed hypothesis and the evidence can be summarized in a single comparative picture:

```
                 ZZ finger   SANT      SWIRM     HAT module role
                 --------    ------    ------    ----------------------------
  ADA2 (Q02336)    YES        YES       YES      Coactivator: stabilizes Gcn5,
   (SAGA subunit)                                 enables full HAT activity on
                                                  nucleosomes; SWIRM docks HAT
                                                  module into SAGA
  --------------------------------------------------------------------------
  FUN19 (P28003)   NO         NO        YES      Docking peg only; no catalytic
   (subfamily SF21)                              or activation domains retained
```

The logical chain the seed hypothesis relies on is: *SWIRM retained → some activation mechanism survives Ada2/SAGA divergence → assign coactivator + positive regulation.* Each link fails:

1. **SWIRM is not an activation module.** Structural work shows SWIRM tethers the HAT module into SAGA; it does not carry out or intrinsically drive acetylation/activation (PMID: 36965704). Retaining it does not retain activation.
2. **The activating domains were lost.** The ZZ and SANT domains — those that stabilize Gcn5 and enable full HAT activity — are absent from FUN19. Loss of the effector domains is the functionally decisive change, not the retained docking module.
3. **The complex context that survived is repressive.** The only propagated complex term is Rpd3L-Expanded (an HDAC assembly), and the only genuine experimental interaction among transcription factors is SIN3 (the Rpd3 co-repressor scaffold). If FUN19 has any residual chromatin role, the vector of evidence points **repressive**, not activating.
4. **The "SAGA membership" is an artifact.** STRING SAGA links have experimental score 0.000; they are co-annotation transfer. IntAct records no SAGA/Sin3 binary interaction at all.

The coherent interpretation is that FUN19 is a **divergent, largely uncharacterized paralog** within the ADA2 (PTHR12374) family that **lost the coactivator effector apparatus**. Its curated interactome (chaperones + a karyopherin) is that of a protein whose stable partners are folding/transport machinery, not a transcriptional activation module. Any transcription-related role is at best **neutral chromatin association**, and the strongest specific lead is a **repressive Sin3/Rpd3 context** — the opposite sign from the hypothesis.

### GO Decision Table (lead requiring curator verification)

| GO term | Aspect | Seed proposes | Evidence status | Recommended action |
|---------|--------|---------------|-----------------|--------------------|
| GO:0003713 transcription coactivator activity | MF | ADD | No experimental support; effector domains lost; interactome repressive/chaperone | **Do not add (reject)** |
| GO:0045893 positive regulation of DNA-templated transcription | BP | ADD | No experimental support; only complex context is repressive HDAC | **Do not add (reject)** |
| GO:0070461 SAGA-type complex (loss/IRD) | CC | (context) | SAGA links are DB artifact (escore 0.000); FUN19 not a SAGA subunit | Consistent with **no SAGA membership** |
| GO:0070210 Rpd3L-Expanded complex | CC | (retained) | IBA only; SIN3 is top experimental partner but HT co-occurrence | **Retain as IBA/non-core**, flag as unverified |
| GO:0003682 chromatin binding | MF | (retained) | IBA only | Retain as IBA, neutral |
| GO:0006338 chromatin remodeling | BP | (retained) | IBA only; does not require ATPase activity of target | Retain as IBA, neutral |
| GO:0006357 regulation of transcription by Pol II | BP | (retained) | IBA only; direction-neutral | Retain as IBA, neutral |

---

## Evidence Matrix

| Citation | Evidence type | Supports / Refutes / Qualifies | Claim tested | Key finding | Context | Confidence & limitations |
|----------|---------------|-------------------------------|--------------|-------------|---------|--------------------------|
| UniProt P28003 (FUN19) vs Q02336 (ADA2) | Structural / domain architecture | **Refutes** | FUN19 retains Ada2's coactivator machinery | FUN19 has only SWIRM (316–413); lacks ZZ, SANT, HAT, bromodomain that ADA2 carries | *S. cerevisiae* protein annotation | High for architecture; inference for function |
| [PMID: 36965704](https://pubmed.ncbi.nlm.nih.gov/36965704/) | Direct structural/biochemical | **Refutes (mechanism)** | SWIRM is an activation module | SWIRM is a tethering module (docks HAT into SAGA); coactivation needs Ada2/Ada3/Gcn5 module | Yeast SAGA HAT module | High; about ADA2, applied to FUN19 by analogy |
| Current GO annotation set (GO_Central IBA) | Review/database | **Refutes / qualifies** | Coactivator/positive terms already supported | No GO:0003713 or GO:0045893; only IBA terms; one context is repressive Rpd3L | *S. cerevisiae* | High for annotation state; IBA has no experimental weight |
| STRING YAL034C | Interaction (aggregated) | **Refutes / qualifies** | FUN19 is a SAGA coactivator member | SAGA subunits escore=0.000 (DB carry-over); top experimental partner is SIN3 (escore 0.755, co-repressor) | *S. cerevisiae* | Medium; SIN3 signal is HT co-occurrence, not binary |
| [PMID: 19536198](https://pubmed.ncbi.nlm.nih.gov/19536198/) | Interaction (curated, TAP) | **Refutes / competing** | FUN19 sits in a transcription coactivator complex | FUN19 interactome dominated by chaperones (Ssa1, Hsc82, Hsp104, prefoldin) | *S. cerevisiae* chaperone network | High for interaction; suggests folding-machinery association |
| [PMID: 16429126](https://pubmed.ncbi.nlm.nih.gov/16429126/) | Interaction (curated, TAP) | **Qualifies** | FUN19 nuclear-transcriptional role | FUN19–KAP123 (karyopherin/import) interaction | *S. cerevisiae* | Medium; consistent with nuclear localization, not activation |
| [PMID: 14690591](https://pubmed.ncbi.nlm.nih.gov/14690591/) | Interaction (curated, Y2H) | **Qualifies** | — | FUN19 self-association | *S. cerevisiae* two-hybrid | Low functional weight |

---

## Evidence Base (Literature)

**[PMID: 36965704](https://pubmed.ncbi.nlm.nih.gov/36965704/) — *The SAGA HAT module is tethered by its SWIRM domain and modulates activity of the SAGA DUB module.*** This is the pivotal mechanistic reference. It directly establishes (1) that full Gcn5/HAT activity on nucleosomes requires the assembled Gcn5–Ada2–Ada3 module, and (2) that the SWIRM domain is a **tethering** element that incorporates the HAT module into SAGA rather than a catalytic/activating element. Both quotes were verified against the abstract. Together they dismantle the seed hypothesis's central premise that retention of SWIRM implies retention of coactivation: the domain FUN19 kept is the docking module, while the domains it lost (ZZ, SANT) are those coupled to Gcn5 stabilization and HAT activity.

**[PMID: 19536198](https://pubmed.ncbi.nlm.nih.gov/19536198/)** (chaperone interaction network, TAP-MS) — source of the curated FUN19 interactions with Hsp70/Hsp90/Hsp104/prefoldin. Supports the interpretation that FUN19's stable curated partners are folding machinery, not a coactivator complex.

**[PMID: 16429126](https://pubmed.ncbi.nlm.nih.gov/16429126/)** (TAP) — FUN19–KAP123 (nuclear import) interaction. Consistent with nuclear localization but not with transcriptional activation.

**[PMID: 14690591](https://pubmed.ncbi.nlm.nih.gov/14690591/)** (Y2H) — FUN19 self-association; low functional weight but part of the curated interaction record.

Database-level orientation (STRING, IntAct/PSICQUIC, UniProt, PANTHER PTHR12374) is used as orientation, not as primary support, per the research directive — the STRING escore breakdown is treated as evidence of **artifactual** SAGA co-annotation rather than as positive interaction evidence.

---

## Conflicts and Alternatives

1. **Paralog over-annotation (most likely explanation).** FUN19 sits in PANTHER PTHR12374 (ADA2 family) but in a distinct subfamily (SF21). IBA propagation from the ADA2-containing family, plus STRING/complex co-annotation, generates the appearance of SAGA/coactivator association. The escore=0.000 for every SAGA subunit is the signature of database carry-over, not biology.

2. **Repressive alternative.** If FUN19 has any real chromatin function, the evidence sign is **repressive**: the only propagated complex is Rpd3L-Expanded (HDAC), and the top experimental interactor is the Sin3 co-repressor scaffold. This is the opposite of the seed hypothesis and is the more parsimonious residual-function lead.

3. **Non-transcriptional / chaperone-client alternative.** The curated IntAct interactome (Hsp70/Hsp90/Hsp104/prefoldin/karyopherin) is equally consistent with FUN19 being a poorly characterized, possibly metastable protein whose principal validated partners are folding and transport machinery — not a transcription factor at all.

4. **Weak baseline in both directions.** Because every GO annotation is IBA and there is no experimental FUNCTION comment, no interpretation is anchored on direct assay. The refutation is strong relative to the *added* claim (coactivation) but should not be overstated into a positive assignment of repressive function.

---

## Limitations and Knowledge Gaps

- **No direct functional assay for FUN19.** There is no reporter, ChIP, or transcriptome study establishing FUN19's effect on transcription in either direction. The case against coactivation is comparative and interaction-based, not a direct refuting experiment. *Resolution:* an inducible-reporter or nascent-transcription (e.g., 4tU-seq) assay in a *fun19Δ* strain.
- **STRING SIN3 signal is aggregated, not binary.** The escore of 0.755 is high-throughput co-occurrence; IntAct records no FUN19–Sin3 binary interaction. Whether FUN19 is a genuine Rpd3L/Sin3 subunit is unresolved. *Resolution:* co-IP / reciprocal TAP of Sin3 vs FUN19; size-exclusion co-migration.
- **SWIRM functional test in FUN19 context.** SWIRM tethers the HAT module in ADA2; whether FUN19's SWIRM binds any chromatin-modifying module is untested. *Resolution:* pulldown of FUN19-SWIRM against HAT/HDAC modules.
- **Localization confirmation.** KAP123 interaction suggests nuclear import but a direct GFP localization for FUN19 was not established in this analysis. *Resolution:* FUN19-GFP microscopy (or consult existing SGD localization data).
- **PANTHER IRD / ancestral judgment.** The seed cites an IRD loss of SAGA-type-complex membership (GO:0070461) at the fungal node. This was interpreted from the seed context, not independently re-derived from the PANTHER tree in these iterations. *Resolution:* directly inspect the PTHR12374 tree/IRD annotations.

---

## Discriminating Tests (most efficient)

1. **fun19Δ nascent-transcription / reporter assay.** A directional readout: if FUN19 were a coactivator, its deletion should decrease activated transcription. This is the single most decisive test to distinguish coactivation from a repressive or null role.
2. **Reciprocal co-IP of Sin3 and Gcn5/Ada2 with FUN19.** Distinguishes genuine Rpd3L/Sin3 (repressive) membership from artifactual SAGA (activating) co-annotation. Predicts Sin3 pulls down FUN19 while SAGA does not.
3. **FUN19-SWIRM biochemical pulldown vs HAT and HDAC modules.** Tests whether the retained SWIRM tethers FUN19 to any chromatin-modifying complex, and if so which sign.
4. **FUN19-GFP localization + KAP123-dependence.** Confirms nuclear vs cytoplasmic partitioning and whether the karyopherin interaction is functional.
5. **Comparative PANTHER/IRD re-derivation.** Independently confirm the ancestral judgment (SAGA-membership loss at the fungal node) rather than relying on the seed's summary.

---

## Curation Leads (require curator verification)

**Primary lead — reject the added activation terms.**
- **Do NOT add GO:0003713 (transcription coactivator activity, MF).** No experimental support; Ada2 effector domains (ZZ, SANT) are lost; SWIRM is a tether, not an activator; interactome is repressive/chaperone-dominated.
- **Do NOT add GO:0045893 (positive regulation of DNA-templated transcription, BP).** Same reasoning; the only propagated complex context is the repressive Rpd3L/Sin3 HDAC assembly.

**Secondary leads — annotation hygiene.**
- **Retain the existing IBA terms as non-core / unverified**: GO:0070210 (Rpd3L-Expanded), GO:0003682 (chromatin binding), GO:0006338 (chromatin remodeling), GO:0006357 (regulation of transcription by Pol II). Flag each as IBA-only, no experimental support.
- **Flag SAGA-membership propagation as artifactual.** Any pipeline that would transfer SAGA/coactivator terms to FUN19 from PTHR12374 should be blocked; STRING SAGA escore = 0.000 confirms these are co-annotation carry-over, and PANTHER records an IRD loss of SAGA-type-complex membership at the fungal node.
- **Note the repressive lead, but do not annotate it as fact.** The SIN3 (escore 0.755) association is the strongest experimental transcription-factor link and, with GO:0070210, suggests a repressive context — but IntAct shows no binary Sin3–FUN19 interaction, so this is a lead, not an assignment.

**Candidate references with snippets to verify:**
- [PMID: 36965704](https://pubmed.ncbi.nlm.nih.gov/36965704/): *"the SWIRM domain is required for incorporation of the HAT module into the yeast SAGA complex, but not the ADA complex"* — supports SWIRM = tether, not activator.
- [PMID: 36965704](https://pubmed.ncbi.nlm.nih.gov/36965704/): *"A minimal HAT module complex containing Gcn5 bound to Ada2 and Ada3 is required for full Gcn5 activity on nucleosomes."* — supports that coactivation requires the effector module FUN19 lacks.

**Suggested curator questions:**
- Is there any experimental (non-IBA) evidence anywhere in the literature for FUN19 affecting transcription in either direction?
- Should FUN19's IBA Rpd3L-Expanded annotation be retained given no binary Sin3 interaction in IntAct?

---

## Conclusion

The seed hypothesis that FUN19 has transcription coactivator activity and positively regulates transcription is **refuted / best treated as paralog-driven over-annotation**. FUN19 retained only Ada2's SWIRM tethering module while losing the ZZ and SANT domains that underpin coactivation; it is not a SAGA subunit; all current annotations are IBA; the only propagated complex context and the strongest experimental interactor are **repressive** (Rpd3L / Sin3), and curated interactions place FUN19 with chaperones and a karyopherin rather than any coactivator complex. Curators should **not** add GO:0003713 or GO:0045893 and should retain only the neutral IBA-level chromatin terms pending direct experimental validation.


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)
- [OpenScientist FUN19 GO decision table](openscientist_artifacts/provenance_FUN19_GO_decision_table.csv)
- [OpenScientist FUN19 IntAct curated interactions](openscientist_artifacts/provenance_FUN19_IntAct_curated_interactions.csv)
- [OpenScientist FUN19 STRING partners](openscientist_artifacts/provenance_FUN19_STRING_partners.csv)