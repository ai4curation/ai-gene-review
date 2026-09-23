---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-20T20:15:18.194670'
end_time: '2026-09-20T20:45:43.189877'
duration_seconds: 1825.0
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: yeast
  gene: ESL1
  gene_symbol: ESL1
  uniprot_accession: P40456
  taxon_id: NCBITaxon:559292
  taxon_label: Saccharomyces cerevisiae
  focus_type: function_assignment
  hypothesis_slug: telomerase-association-and-nucleic-acid-binding
  hypothesis_text: Saccharomyces cerevisiae Esl1 (P40456) retains telomerase-holoenzyme
    association, telomeric-repeat DNA binding or telomerase RNA binding. Evaluate
    each independently using actual ancestral placement, interfaces and direct biochemical/complex
    evidence. PMID:23893744 reports normal telomere maintenance in single/double deletion
    experiments; determine what this does and does not establish about binding capacity
    and complex participation. Do not treat a dispensable phenotype as a direct negative
    binding assay. Its separately tested NMD-substrate results are outside this question
    and must not be generalized to every RNA-related function.
  term_context: No specific term context supplied.
  reference_context: No specific reference context supplied.
  source_file: genes/yeast/ESL1/ESL1-ai-review.yaml
  source_selector: free-text
  source_context_yaml: "hypothesis: Saccharomyces cerevisiae Esl1 (P40456) retains\
    \ telomerase-holoenzyme association, telomeric-repeat\n  DNA binding or telomerase\
    \ RNA binding. Evaluate each independently using actual ancestral placement,\n\
    \  interfaces and direct biochemical/complex evidence. PMID:23893744 reports normal\
    \ telomere maintenance\n  in single/double deletion experiments; determine what\
    \ this does and does not establish about binding\n  capacity and complex participation.\
    \ Do not treat a dispensable phenotype as a direct negative binding\n  assay.\
    \ Its separately tested NMD-substrate results are outside this question and must\
    \ not be generalized\n  to every RNA-related function.\nfocus_type: function_assignment\n\
    context: []\nreference_id: []"
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
citation_count: 2
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
- filename: go_decision_table.csv
  path: openscientist_artifacts/go_decision_table.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist go decision table
- filename: sequence_identity_matrix.csv
  path: openscientist_artifacts/sequence_identity_matrix.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist sequence identity matrix
- filename: string_channel_provenance.csv
  path: openscientist_artifacts/string_channel_provenance.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist string channel provenance
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
- **Gene directory:** ESL1
- **Gene symbol:** ESL1
- **UniProt accession:** P40456

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** telomerase-association-and-nucleic-acid-binding
- **Source file:** genes/yeast/ESL1/ESL1-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

Saccharomyces cerevisiae Esl1 (P40456) retains telomerase-holoenzyme association, telomeric-repeat DNA binding or telomerase RNA binding. Evaluate each independently using actual ancestral placement, interfaces and direct biochemical/complex evidence. PMID:23893744 reports normal telomere maintenance in single/double deletion experiments; determine what this does and does not establish about binding capacity and complex participation. Do not treat a dispensable phenotype as a direct negative binding assay. Its separately tested NMD-substrate results are outside this question and must not be generalized to every RNA-related function.

## Term and Decision Context

No specific term context supplied.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: Saccharomyces cerevisiae Esl1 (P40456) retains telomerase-holoenzyme association, telomeric-repeat
  DNA binding or telomerase RNA binding. Evaluate each independently using actual ancestral placement,
  interfaces and direct biochemical/complex evidence. PMID:23893744 reports normal telomere maintenance
  in single/double deletion experiments; determine what this does and does not establish about binding
  capacity and complex participation. Do not treat a dispensable phenotype as a direct negative binding
  assay. Its separately tested NMD-substrate results are outside this question and must not be generalized
  to every RNA-related function.
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

# AIGR Gene Hypothesis Deep Research — ESL1 (P40456): Telomerase Association and Nucleic-Acid Binding

**Target gene:** *ESL1* (P40456), "EST/SMG-like protein 1", *Saccharomyces cerevisiae* (NCBITaxon:559292)
**Focus type:** function_assignment
**Hypothesis slug:** telomerase-association-and-nucleic-acid-binding
**Source review:** `genes/yeast/ESL1/ESL1-ai-review.yaml` (free-text)

---

## Summary

The seed hypothesis proposes that *S. cerevisiae* Esl1 (P40456) retains one or more activities inherited from the metazoan EST1A/SMG6 subfamily: telomerase-holoenzyme association (a cellular-component claim), telomeric-repeat DNA binding, or telomerase RNA binding (two molecular-function claims). The task was to evaluate each independently against actual GO evidence codes, orthology placement, interaction databases, and primary literature — and, critically, to distinguish a *dispensable phenotype* from a *direct negative binding assay*.

The evidence converges firmly against all three as retained functions in *S. cerevisiae*. Every telomerase-related GO term on P40456 carries the evidence code **IBA (Inferred from Biological Ancestor)** from GO_Central/PAINT (GO_REF:0000033); none rests on any experimental assay of yeast Esl1. These IBA terms are phylogenetic carry-overs from the EST1A/SMG6 branch (PANTHER PTHR15696:SF0 = "telomerase-binding protein EST1A"), whose *metazoan* members are documented telomerase-interacting proteins. Against this ancestral inference stands the only direct organism-specific study, [PMID:23893744](https://pubmed.ncbi.nlm.nih.gov/23893744/), which found that *esl1Δ*, *esl2Δ*, and *esl1Δ esl2Δ* mutants maintain normal telomeres and that Esl1/Esl2 instead act in environment-sensing gene-expression regulation. Comparative work ([PMID:22544908](https://pubmed.ncbi.nlm.nih.gov/22544908/)) localizes genuine telomerase-RNA binding to the **Est1/Ebs1 branch**, a different set of yeast paralogs.

Two computed checks reinforce this. First, in STRING v12 every telomerase-associated partner of ESL1 (EST1, EST2, EST3, POP1, POP6, POP7) has an experiments subscore of **0.000** and an identical database subscore of **0.540** — the fingerprint of an imported complex-membership annotation (the IBA term reflected back circularly), whereas the true co-paralog ESL2 carries a real experiments subscore of 0.225. Second, global pairwise alignment places Esl1 at only ~20–23% identity to *both* ScEst1 and human SMG6, too diverged to assume interface conservation from homology. Honoring the seed's caveat, the deletion result is a *dispensability* phenotype rather than a direct binding assay, so binding capacity is formally **unresolved by direct experiment** — but there is **no positive evidence** for any of the three functions in this organism, and the balance of evidence marks the IBA telomerase terms as **over-annotations** for ScEsl1.

**Verdict: Over-annotated (refuted as a core function; the isolated in-vitro binding capacity remains formally unresolved because no such assay has been performed).**

---

## Key Findings

### F001 — All telomerase GO terms on ESL1 are IBA phylogenetic inferences, not experimental observations

UniProt P40456 carries exactly three telomerase-related GO terms, and **all three share the evidence code IBA** (Inferred from Biological Ancestor, GO_Central): **GO:0005697** telomerase holoenzyme complex (CC), **GO:0070034** telomerase RNA binding (MF), and **GO:0042162** telomeric repeat DNA binding (MF). No EXP/IDA/IPI-coded telomerase annotation of any kind exists for this protein. The gene sits in PANTHER family **PTHR15696 (SMG-7-like)**, subfamily **PTHR15696:SF0 = "TELOMERASE-BINDING PROTEIN EST1A"** — the subfamily name itself is the origin of the propagated telomerase language. Domain architecture comprises an N-terminal TPR-like helical superfamily region (SSF48452, 14-3-3-like) and a C-terminal PINc (PilT N-terminus) domain (residues ~947–1087; Pfam PF13638; InterPro IPR045153 Est1/Ebs1-like, IPR002716 PIN_dom). Notably, the **curated UniProt FUNCTION line makes no telomerase claim** — it reads "May be involved in the regulation of gene expression responses of environment-sensing pathways," matching the experimental literature and not the propagated GO terms. This internal mismatch between the manual FUNCTION statement and the automated GO annotations is itself a signal that the telomerase terms are carry-over artifacts.

### F002 — Direct in-vivo experiment shows Esl1/Esl2 have no telomere-maintenance role; telomerase function resides in the separate Est1 paralog

[PMID:23893744](https://pubmed.ncbi.nlm.nih.gov/23893744/) (Lai et al., 2013) is the only direct functional characterization of the gene. The authors constructed *esl1Δ*, *esl2Δ*, and *esl1Δ esl2Δ* mutants and observed **normal telomere maintenance** in all cases, stating plainly that "unlike their metazoan orthologs, Esl1 and Esl2 were **not involved in nonsense-mediated mRNA decay or telomere maintenance pathways**." Instead, loss of both proteins deregulated ~50 metabolic/environment-responsive transcripts (>2-fold) — for instance, normally glucose-repressed genes were derepressed during high-glucose growth — and *esl1Δ esl2Δ* was synthetic sick with null mutations of *RIM8* and *DFG16*, components of the Rim101 pH-response environmental-sensing complex.

The complementary comparative evidence comes from [PMID:22544908](https://pubmed.ncbi.nlm.nih.gov/22544908/) (Hsu et al., 2012), which shows that the Est1/Ebs1-line homolog KlEst1 (in *Kluyveromyces lactis*) **does** associate with telomerase RNA (Ter1) and active telomerase and **is** required for telomere maintenance, mediated by its N-terminal TPR + DSH (downstream helical) subdomains; a UV-crosslink assay established direct physical interaction with a Ter1 stem-loop. This maps telomerase-RNA binding to the **Est1/Ebs1 branch** of the family, not the Esl1/Esl2 (SMG5/6-like) branch to which ESL1 belongs. The functional split within the family is therefore clean: telomerase → Est1/Ebs1; environment-sensing gene regulation → Esl1/Esl2.

### F003 — No experimental interaction evidence links ESL1 to telomerase; STRING links are pure database carry-over

STRING v12 (*S. cerevisiae*, taxid 4932) lists telomerase and telomerase-associated proteins among ESL1's partners — EST1 (0.667), EST2 (0.556), EST3 (0.540), POP1 (0.554), POP6 (0.540), POP7 (0.553). Decomposing these combined scores into channels is decisive: **every one of these partners has an experiments subscore of escore = 0.000**, and they all share an **identical database subscore of dscore = 0.540** — the signature of an imported complex/pathway-membership annotation, i.e., the IBA "telomerase holoenzyme complex" term reflected back through STRING's database channel. This is circular and non-independent. Only negligible coexpression (ascore 0.00–0.08) and, for EST1 alone, some textmining (tscore 0.291) add signal. The internal control is compelling: the true co-paralog **ESL2 carries a real experimental subscore of escore = 0.225**, showing STRING does surface genuine physical evidence when it exists — and reports **zero** for every telomerase component. Curators should therefore treat STRING telomerase links for ESL1 as non-evidence.

### F004 — ESL1 is a deeply diverged Est1-family member roughly equidistant from telomerase Est1 and human SMG6

Global Needleman–Wunsch pairwise identities computed in this investigation place ESL1 as follows:

| Comparison | % identity (shorter length) | % identity (over alignment) |
|---|---|---|
| ScEsl1 vs ScEsl2 (co-paralog) | 51.5% | 47.1% |
| ScEsl1 vs ScEst1 (telomerase) | 37.1% | 23.0% |
| ScEsl1 vs ScEbs1 | 28.2% | 22.1% |
| ScEsl1 vs hSMG6 | 27.8% | 21.7% |
| ScEsl1 vs hSMG5 | 23.1% | 20.5% |
| ScEsl1 vs hSMG7 | 21.1% | 19.7% |

Over the aligned region, Esl1 is only ~20–23% identical to **both** ScEst1 and hSMG6 — roughly equidistant from and deeply diverged from both functional branches — while its clear closest relative is ScEsl2 (the whole-genome-duplication pair). The practical consequence for curation is that sequence identity at this level is **too low to confirm or exclude** retention of a specific telomerase-RNA or telomeric-DNA binding interface. The SMG7-family assignment comes from HMM/PANTHER profiles, not from raw pairwise identity; sequence alone can neither rescue the IBA annotation nor, by itself, formally refute binding capacity, which is why the direct experimental evidence (F002) carries the weight.

### F005 — Complete GO set is 4 IBA + 3 ND with zero experimental annotations; the co-propagated NMD IBA is directly refuted

QuickGO for P40456 returns 7 annotations. The four substantive terms are all IBA from GO_Central/PAINT (GO_REF:0000033): GO:0042162 (telomeric repeat DNA binding, MF), GO:0070034 (telomerase RNA binding, MF), GO:0005697 (telomerase holoenzyme complex, CC), and GO:0000184 (nonsense-mediated decay, BP). The remaining three are SGD root-node **ND ("No Data")** placeholders (GO:0003674, GO:0008150, GO:0005575). **There is not a single experimental GO annotation for ESL1.** The most instructive point is the **NMD term (GO:0000184)**: it was propagated by the same PAINT node as the telomerase terms, yet it is **directly contradicted** by PMID:23893744 ("not involved in nonsense-mediated mRNA decay"). This is a demonstrated case of the ancestral node over-propagating a function to the fungal Esl1/Esl2 members that experiment then refuted. Because the telomerase terms come from the same node, the demonstrated NMD failure is strong indirect evidence that the telomerase terms are similarly spurious for this specific gene.

---

## Mechanistic Model / Interpretation

The Est1/Ebs1/SMG family in budding yeast arose through gene duplications (including whole-genome duplication) and underwent functional partitioning. The evidence supports the following model:

```
                 Ancestral Est1/Ebs1/SMG multifunctional protein
                 (TPR-like helical N-term + PINc C-term)
                                  |
        ┌─────────────────────────┼─────────────────────────┐
        |                         |                          |
   Est1/Ebs1 branch          Esl1/Esl2 branch           Metazoan SMG5/6/7
   (telomerase +             (SMG5/6-like)              (NMD + telomerase
    translation/NMD)                                     via SMG6 PIN)
        |                         |
   ScEst1: TLC1/telomerase   ScEsl1 / ScEsl2:
   RNA binding, telomere     NO telomere role,
   maintenance               NO NMD role;
   KlEst1 (single copy):     environment-sensing
   binds Ter1 RNA +          adaptive gene expression
   active telomerase         (Rim101 pH pathway link;
   (PMID:22544908)           ~50 metabolic transcripts)
                             (PMID:23893744)
```

The immediate molecular/cellular function being *tested* by the hypothesis is direct physical association of the Esl1 gene product with telomerase RNA, telomeric-repeat DNA, or the telomerase holoenzyme. The evidence indicates that in *S. cerevisiae* this function was **retained on the Est1/Ebs1 sister branch and lost (or never present) on the Esl1/Esl2 branch**. The observed biology of Esl1/Esl2 is regulation of environment-sensing adaptive gene expression — mechanistically distinct from telomere maintenance and neither requiring nor predicting telomerase engagement.

The distinction between "dispensable phenotype" and "absence of binding capacity" is respected throughout. PMID:23893744 establishes **functional dispensability** for telomere maintenance, which downgrades the biological-process and cellular-component claims to non-core status. It does not, by itself, prove the Esl1 protein is biochemically incapable of contacting a nucleic acid in vitro. However, because (a) the GO terms rest solely on IBA, (b) no experimental interaction exists in STRING, (c) a co-propagated term from the same node (NMD) is experimentally refuted, and (d) sequence divergence is too large to assume interface conservation, the reasonable curation stance is that the telomerase MF/CC terms are unsupported for this gene and should not be presented as established functions.

---

## Evidence Base

| Citation | Evidence type | Direction | Claim tested | Key finding | Context | Confidence / limitations |
|---|---|---|---|---|---|---|
| UniProt P40456 (database) | review/database | qualifies | Provenance of telomerase terms | All 3 telomerase GO terms are **IBA**; curated FUNCTION is gene-expression regulation, no telomerase mention | *S. cerevisiae* record | High for provenance; IBA ≠ experimental |
| PANTHER PTHR15696:SF0 | computational/evolutionary | qualifies (source) | Origin of IBA propagation | Subfamily named "telomerase-binding protein EST1A"; ancestral node telomerase-annotated from metazoan SMG6/EST1A | Pan-eukaryotic family | Explains why IBA carries telomerase terms; family-level, not member-specific |
| InterPro IPR045153 / IPR002716 / SSF48452 | structural/evolutionary | qualifies | Domain architecture | Est1/Ebs1-like: N-terminal TPR-like helical + C-terminal PINc (PF13638, res 947–1087) | Sequence/domain | Shows Esl1 retains a fold compatible with RNA binding — cannot exclude binding a priori |
| **[PMID:23893744](https://pubmed.ncbi.nlm.nih.gov/23893744/)** (Lai 2013) | mutant phenotype (in vivo) | **refutes (function-level)** | Are Esl1/Esl2 needed for telomere maintenance/NMD? | *esl1Δ esl2Δ* telomeres normal; "not involved in … telomere maintenance pathways"; act in environment-sensing gene expression | *S. cerevisiae*, deletion mutants | Direct in-vivo test; **dispensability, not a binding assay** |
| **[PMID:22544908](https://pubmed.ncbi.nlm.nih.gov/22544908/)** (Hsu 2012) | direct assay (in vitro/in vivo) | competing / qualifies | Which paralog binds telomerase RNA? | KlEst1 (Est1/Ebs1 line) binds Ter1 + active telomerase via N-terminal TPR+DSH; required for telomere maintenance | *K. lactis* | Localizes telomerase-RNA binding to the **Est1/Ebs1 branch**, not Esl1/Esl2 |
| STRING v12 (computed) | interaction | **refutes (CC)** | Does Esl1 physically associate with telomerase? | EST1/EST2/EST3/POP1/6/7 all escore=0.000, uniform dscore=0.540 (imported); co-paralog ESL2 escore=0.225 | *S. cerevisiae* (taxid 4932) | No independent experimental interaction; links are IBA carry-over |
| Global NW identity (computed) | structural/evolutionary | qualifies | Is Esl1 in the Est1 or SMG5/6 branch? | Esl1 ~20–23% aln-identity to BOTH ScEst1 and hSMG6; closest to Esl2 (47–51%) | Sequence | Deep divergence → interface conservation not inferable from homology |

Key supporting quotes for curation:
- PMID:23893744 — *"unlike their metazoan orthologs, Esl1 and Esl2 were not involved in nonsense-mediated mRNA decay or telomere maintenance pathways."*
- PMID:22544908 — *"KlEst1 also associates with telomerase RNA (Ter1) and an active telomerase complex in cell extracts … require its N-terminal domain but not its C terminus."*

---

## GO Curation Implications

**Complete GO audit (QuickGO, P40456 — 7 annotations):** the substantive terms are *all* IBA from GO_Central/PAINT — the three telomerase terms plus GO:0000184 NMD (BP). The other three are SGD root-node **ND**. There is **not a single experimental GO annotation** for ESL1. Decisively, the one member of this IBA block that has been tested in yeast — NMD — is directly refuted by PMID:23893744, demonstrating that the PAINT node over-propagates to the fungal Esl1/Esl2 members; by parity, the three telomerase IBA terms should be viewed the same way.

| GO term | Aspect | Current evidence | Recommended lead (curator to verify) |
|---|---|---|---|
| GO:0005697 telomerase holoenzyme complex | CC | IBA only; STRING shows zero experimental support for any telomerase partner; *esl1Δ esl2Δ* telomeres normal | **Strongest removal case.** Remove / do-not-propagate — a complex-membership claim needs localization or physical-complex evidence, which is absent. |
| GO:0070034 telomerase RNA binding | MF | IBA only; homologous binding maps to Est1/Ebs1 branch (PMID:22544908); no direct Esl1 assay | Remove or downgrade to non-core. Frame as "unsupported for this gene," not a performed negative assay. |
| GO:0042162 telomeric repeat DNA binding | MF | IBA only; no direct assay; least supported even within the family | Remove or downgrade to non-core. |
| GO:0000184 NMD | BP | IBA; **experimentally refuted** (PMID:23893744) | Outside this hypothesis, but a clear "NOT" candidate — corroborates that the node over-propagates. |

Positively supported alternative (experimental, PMID:23893744): a **BP** annotation in the area of regulation of gene expression / cellular response to nutrient & pH environment (e.g., regulation of transcription; response to nutrient levels). The PIN/PilT N-terminus domain supports at most a **putative/predicted** RNA-nuclease MF label — the paper found no NMD activity, so any nuclease MF must be marked "predicted from domain," not asserted. Do **not** default to "protein binding."

---

## Mechanistic Scope

- **Immediate molecular identity:** Est1/Ebs1/SMG-like protein; N-terminal TPR-like helical (14-3-3-like) domain + C-terminal PINc domain. The fold is compatible with RNA binding and with the phosphoprotein-binding mode used by metazoan SMG5/6/7.
- **Demonstrated cellular function (direct):** regulation of environment-sensing adaptive gene expression (glucose repression; Rim101 pH-pathway genetic interactions).
- **Telomerase functions:** these are ancestral/paralog activities, not shown for ScEsl1. Telomere-maintenance dispensability is a loss-of-function phenotype and is downstream/indirect with respect to the binding MF claims — it does not directly measure binding.

---

## Conflicts and Alternatives

1. **Paralog/ancestral confusion (primary alternative).** The IBA terms derive from the EST1A/SMG6 subfamily whose *human* member is a genuine telomerase-associated protein. In budding yeast, telomerase function is split onto **Est1** (and partly Ebs1); Esl1/Esl2 are the SMG5/6-like regulatory branch. IBA propagation across the whole family over-reaches for this member.
2. **Database carry-over is demonstrable, not hypothetical.** STRING's telomerase neighborhood for Esl1 is built from an identical 0.540 database subscore with zero experimental support — the IBA annotation feeding a secondary resource that could be mistaken for independent corroboration.
3. **Organism-specific divergence.** PMID:23893744 explicitly contrasts Esl1/Esl2 with their metazoan orthologs ("unlike their metazoan orthologs"). Cross-phylum inference at ~20% identity is unreliable.
4. **Residual capacity caveat (the strongest pro-hypothesis argument).** Esl1 retains the Est1-family fold, so a latent, uncharacterized TLC1 or telomeric-DNA interaction cannot be formally excluded — but no data support it, and a phenotypically silent capacity would not justify a standing GO annotation.
5. **Sequence caveat cuts both ways.** Because Esl1 is ~equidistant from Est1 and SMG6, neither "obviously telomerase" nor "obviously SMG6/NMD" is defensible from raw identity; the family assignment comes from HMM/PANTHER profiles and functional data.

---

## Limitations and Knowledge Gaps

1. **Direct Esl1–TLC1 binding.** *Checked:* no RNA-binding/CLIP/UV-crosslink assay for ScEsl1 in the literature or UniProt. *Matters:* it is the exact MF asserted by IBA. *Resolve:* RIP/CLIP or in-vitro UV-crosslink of recombinant Esl1 vs TLC1 stem-loop (as done for KlEst1–Ter1).
2. **Esl1 in the telomerase complex.** *Checked:* no copurification with Est2/Est1/Est3/Cdc13 reported; STRING experiments = 0. *Matters:* underlies the CC term. *Resolve:* TAP/IP-MS of telomerase or of Esl1.
3. **Telomeric ssDNA binding.** *Checked:* none reported for Esl1. *Resolve:* EMSA with a telomeric G-tail oligo.
4. **PIN-domain RNase activity/substrate.** *Checked:* domain predicted; NMD activity ruled out (PMID:23893744). *Resolve:* in-vitro nuclease assay.

Additional scope limits: no local bioinformatics files were provided; public UniProt/InterPro/PANTHER/QuickGO/STRING records and PubMed abstracts were used (full text of the two primary papers was not read). Interaction mining relied on STRING and UniProt/IntAct rather than an exhaustive BioGRID screen. The verdict distinguishes *no positive evidence + contradicting in-vivo phenotype* (strong) from a *direct negative binding assay* (absent).

---

## Discriminating Tests

- **Esl1 IP-MS / telomerase TAP-MS** — presence/absence of Est2/Est1/Est3/Tlc1 discriminates complex membership (CC term) cleanly. Zero recovery strongly supports removing GO:0005697.
- **UV-crosslink / EMSA of recombinant Esl1** vs TLC1 stem-loop and vs telomeric ssDNA — tests the two MF terms independently of the dispensable-phenotype ambiguity, with ScEst1/KlEst1 as positive controls.
- **Interface mapping** — align the KlEst1 TPR+DSH Ter1-binding residues (and an AlphaFold Esl1 model) onto Esl1 to test whether the RNA-binding interface is conserved or degenerate.
- **Cross-branch complementation** — test whether *ESL1* rescues telomere shortening in *est1Δ*; failure reinforces branch-specific partitioning.

---

## Proposed Follow-up Actions (Curation Leads — require curator verification)

- **Candidate references to attach:**
  - PMID:23893744 — snippet: *"unlike their metazoan orthologs, Esl1 and Esl2 were not involved in nonsense-mediated mRNA decay or telomere maintenance pathways"* → supports removing/qualifying telomere-related annotations and adding a gene-expression-regulation BP term.
  - PMID:22544908 — snippet: *"KlEst1 also associates with telomerase RNA (Ter1) and an active telomerase complex in cell extracts … require its N-terminal domain but not its C terminus"* → the telomerase-RNA-binding function belongs to the Est1/Ebs1 branch (competing paralog evidence).
- **Candidate action changes:** flag GO:0005697, GO:0070034, GO:0042162 (all IBA) for **removal or member-specific NOT/review**; treat as **non-core**. Record GO:0000184 (NMD) as a documented over-propagation ("NOT" candidate).
- **Candidate replacement/new terms (experimental basis, PMID:23893744):** BP around **regulation of transcription / cellular response to nutrient & pH environment**; MF only as **putative PIN-domain nuclease (predicted, not asserted)**.
- **Suggested questions for the curator:** Was the IBA propagation reviewed against PMID:23893744? Should the yeast SMG5/6-branch members be split from the Est1/Ebs1 telomerase clade in the PAINT family tree?
- **Suggested experiments:** Esl1 IP-MS and Esl1–TLC1 crosslink/EMSA (above).

---

## Provenance Artifacts (computed this run)

Key computed values reproduced inline for provenance:
- **STRING v12** (ESL1, taxid 4932): EST1/EST2/EST3/POP1/POP6/POP7 → experiments-subscore **0.000**, database-subscore **0.540** (uniform, imported); ESL2 control → experiments **0.225**.
- **NW identity (over alignment):** Esl1–Esl2 47.1%; Esl1–Est1 23.0%; Esl1–SMG6 21.7%; Esl1–SMG5 20.5%; Esl1–SMG7 19.7%.
- **QuickGO** (P40456): 4 IBA (3 telomerase + NMD) + 3 ND; **0 experimental** annotations.

---

### Bottom line

The telomerase-association and nucleic-acid-binding hypothesis for *S. cerevisiae* Esl1 (P40456) is **over-annotated and not supported as a core function**: the three telomerase GO terms are IBA carry-overs from the metazoan EST1A/SMG6 subfamily with zero experimental support, no independent physical-interaction evidence, and direct in-vivo refutation of the associated telomere-maintenance role — while the genuine telomerase function belongs to the separate Est1/Ebs1 branch. The only residual, formally unresolved point is whether the Esl1 protein retains latent in-vitro nucleic-acid-binding capacity, which no study has directly tested; a latent, phenotypically silent capacity would nonetheless not justify a standing GO annotation.


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)
- [OpenScientist go decision table](openscientist_artifacts/go_decision_table.csv)
- [OpenScientist sequence identity matrix](openscientist_artifacts/sequence_identity_matrix.csv)
- [OpenScientist string channel provenance](openscientist_artifacts/string_channel_provenance.csv)