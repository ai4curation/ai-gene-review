---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-20T23:17:04.139481'
end_time: '2026-09-20T23:37:57.212850'
duration_seconds: 1253.07
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: human
  gene: SAMD8
  gene_symbol: SAMD8
  uniprot_accession: Q96LT4
  taxon_id: NCBITaxon:9606
  taxon_label: Homo sapiens
  focus_type: function_assignment
  hypothesis_slug: lipid-reaction-spectrum-pathways-and-compartments
  hypothesis_text: Human SAMD8 (Q96LT4) has sphingomyelin synthase or ceramide cholinephosphotransferase
    activity, contributes to ceramide biosynthesis, or localizes to Golgi/plasma membrane.
    Assess each separately using actual GO definitions, primary substrate-product
    assays, reaction reversibility, and direct pathway-regulatory roles. Compare established
    CPE/ethanolamine transfer and SAM-dependent ER residence without assuming they
    exclude all alternative reactions, indirect but mechanistic biosynthetic roles,
    or secondary compartments. Distinguish native full-length protein from constructs
    and other SMS paralogs.
  term_context: No specific term context supplied.
  reference_context: No specific reference context supplied.
  source_file: genes/human/SAMD8/SAMD8-ai-review.yaml
  source_selector: free-text
  source_context_yaml: "hypothesis: Human SAMD8 (Q96LT4) has sphingomyelin synthase\
    \ or ceramide cholinephosphotransferase activity,\n  contributes to ceramide biosynthesis,\
    \ or localizes to Golgi/plasma membrane. Assess each separately\n  using actual\
    \ GO definitions, primary substrate-product assays, reaction reversibility, and\
    \ direct pathway-regulatory\n  roles. Compare established CPE/ethanolamine transfer\
    \ and SAM-dependent ER residence without assuming\n  they exclude all alternative\
    \ reactions, indirect but mechanistic biosynthetic roles, or secondary compartments.\n\
    \  Distinguish native full-length protein from constructs and other SMS paralogs.\n\
    focus_type: function_assignment\ncontext: []\nreference_id: []"
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
artifact_count: 3
artifact_sources:
  openscientist_artifacts_zip: 3
artifacts:
- filename: SAMD8_GO_decision_table.csv
  path: openscientist_artifacts/SAMD8_GO_decision_table.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist SAMD8 GO decision table
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
- **Gene directory:** SAMD8
- **Gene symbol:** SAMD8
- **UniProt accession:** Q96LT4

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** lipid-reaction-spectrum-pathways-and-compartments
- **Source file:** genes/human/SAMD8/SAMD8-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

Human SAMD8 (Q96LT4) has sphingomyelin synthase or ceramide cholinephosphotransferase activity, contributes to ceramide biosynthesis, or localizes to Golgi/plasma membrane. Assess each separately using actual GO definitions, primary substrate-product assays, reaction reversibility, and direct pathway-regulatory roles. Compare established CPE/ethanolamine transfer and SAM-dependent ER residence without assuming they exclude all alternative reactions, indirect but mechanistic biosynthetic roles, or secondary compartments. Distinguish native full-length protein from constructs and other SMS paralogs.

## Term and Decision Context

No specific term context supplied.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: Human SAMD8 (Q96LT4) has sphingomyelin synthase or ceramide cholinephosphotransferase activity,
  contributes to ceramide biosynthesis, or localizes to Golgi/plasma membrane. Assess each separately
  using actual GO definitions, primary substrate-product assays, reaction reversibility, and direct pathway-regulatory
  roles. Compare established CPE/ethanolamine transfer and SAM-dependent ER residence without assuming
  they exclude all alternative reactions, indirect but mechanistic biosynthetic roles, or secondary compartments.
  Distinguish native full-length protein from constructs and other SMS paralogs.
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

# SAMD8 (Q96LT4 / SMSr) — Function-Assignment Review

**Hypothesis slug:** lipid-reaction-spectrum-pathways-and-compartments
**Focus:** function_assignment
**Gene:** human SAMD8 (Sphingomyelin synthase-related protein 1, SMSr), UniProt Q96LT4, 415 aa

## Seed hypothesis (paraphrased)
Human SAMD8 has (a) sphingomyelin synthase or ceramide cholinephosphotransferase activity,
(b) contributes to ceramide biosynthesis, and/or (c) localizes to Golgi / plasma membrane.
Assess each component separately.

---

## Executive Judgment

**Verdict by component:**

| Seed component | Verdict |
|---|---|
| (a) Sphingomyelin synthase / ceramide **cholinephosphotransferase** activity | **Refuted / over-annotated** |
| (b) Contributes to **ceramide biosynthesis** (direct) | **Refuted as direct catalysis; weakly/indirectly supported as regulation** |
| (c) Localizes to **Golgi / plasma membrane** (native) | **Refuted / paralog-and-mutant artifact** |
| Established core: ER-resident **CPE synthase**, SAM-dependent ER residence | **Supported** |

Overall: the seed's three propositions are **not supported for the native full-length human protein**. SAMD8/SMSr is a monofunctional **ceramide phosphoethanolamine (CPE) synthase** (EC 2.7.8.-) resident in the **endoplasmic reticulum membrane**, with its catalytic site in the ER lumen. It is *not* a sphingomyelin synthase; it does *not* synthesize ceramide (its reaction consumes ceramide to make CPE); and it is *not* natively a Golgi/plasma-membrane protein — those localizations belong to the paralogs SMS1/SGMS1 (Golgi) and SMS2/SGMS2 (plasma membrane) and appear for SMSr only in oligomerization-defective SAM mutants. A newer biochemical body of work adds a promiscuous **glycerophospholipid hydrolase / PLC-PAP activity generating diacylglycerol**, which broadens the "reaction spectrum" but still does not include SM synthesis and reinforces a regulatory rather than biosynthetic-bulk role.

**Most important caveats:** (1) In-vivo mouse KO shows SMSr is dispensable for ceramide levels and development, qualifying its "ceramide homeostasis regulator" role as context-specific (cultured cells). (2) The newer PLC/PAP hydrolase activities are largely in-vitro (purified enzyme / overexpression) and should be curated cautiously. (3) The current UniProt/GO record already carries the exact over-annotated IBA terms this hypothesis probes (SM synthase, ceramide cholinephosphotransferase, Golgi membrane, plasma membrane).

---

## Evidence Matrix

| # | Citation (PMID) | Evidence type | Supports/Refutes/Qualifies | Claim tested | Key finding | Context | Confidence & limitations |
|---|---|---|---|---|---|---|---|
| 1 | 19506037 (Vacaru 2009, JCB) | Direct assay + localization + mutant | Refutes SM; Supports CPE/ER | Enzymatic identity & compartment | SMSr catalyzes **CPE** synthesis in the **ER lumen**, ~300× less product than SMS1-derived SM; blocking activity raises ER ceramide → "sensor rather than converter" | Human cells, heterologous + endogenous | High; foundational paper |
| 2 | 24259670 (Tafesse 2014, JBC) | Mutant phenotype + localization | Supports ER/CPE; Qualifies ceramide role | Is SMSr an SM synthase or ceramide-maker? | "SMSr (SAMD8), an **ER-resident** CPE synthase," suppressor of ceramide-induced mitochondrial apoptosis; SAM domain required | Human cultured cells | High (cell culture); phenotype is loss-of-function ceramide accumulation, not ceramide synthesis |
| 3 | 28120887 (Cabukusta 2017, JCB) | Localization + structural/biochemical | Supports ER; explains Golgi artifact | Native compartment & basis of ER residence | "SMSr/SAMD8 is an **ER-resident** CPE synthase"; ER residency via **SAM-domain** oligomerization; SAM mutants → **partial redistribution to Golgi** | Human cells; crosslinking, native PAGE | High; Golgi signal is mutant-dependent |
| 4 | 27729449 (Cabukusta 2016) | Biophysical (single-molecule) | Supports ER + oligomer | Oligomeric state of ER sensor | SMSr forms SAM-dependent oligomers in the ER | HeLa, TIRF photobleaching | Medium-high; supports sensor model |
| 5 | 25667419 (Bickert 2015, JLR) | Mutant phenotype (in vivo mouse) | Refutes bifunctional SM; Qualifies ceramide role | Monofunctional CPE vs SM; in-vivo ceramide role | "SMSr serves as **monofunctional CPE synthase**" (vs SMS2 bifunctional SM+CPE); CPE >300× lower than SM; **KO did not affect ceramide levels** in brain/tissues; no developmental phenotype | Mouse, multiple tissues | High; strongest in-vivo evidence; qualifies homeostasis role |
| 6 | 14685263 (Huitema 2004, EMBO Rep) | Direct assay + localization (paralogs) | Competing/explains paralog over-annotation | Where do SM synthases localize? | SM synthesis transfers **phosphocholine from PC**; **SMS1 = Golgi, SMS2 = plasma membrane** | Human/mouse/C. elegans | High; establishes that Golgi/PM + SM-synthase belong to paralogs |
| 7 | 33621517 (Murakami & Sakane 2021, JBC) | Direct assay (purified enzyme) | Qualifies/extends reaction spectrum | Additional activities beyond CPE | Purified SMSr hydrolyzes **PE, PA, PI, PC → DAG** in absence of ceramide; **PAP activity ~300× > CPE** activity | Purified human SMSr; COS-7 overexpression | Medium; in-vitro/overexpression, physiological relevance open |
| 8 | UniProt Q96LT4 (record; cites 33621517, 34332077, 38388831) | Database/curated | Supports ER + CPE + PLC; flags over-annotation | Curated function/location/GO | Single location: **ER membrane**; EC 2.7.8.-; SAM domain 12–78; 6 TM helices; **PLC on PE → phosphoethanolamine + DAG**, proposed **SPT-activating switch**; GO set contains over-annotated IBA terms | Human curated | Orientation-level; used to identify GO terms to re-examine |
| 9 | This work (computed, UniProt Q96LT4/Q86VZ5/Q8NHU3) | Structural/evolutionary (computational) | Qualifies — explains paralog over-annotation | Are SM-synthase/Golgi/PM terms paralog carry-over? | SAMD8 is the sequence outgroup (42–48% id to SGMS1/2, which are 64% to each other); shared 6-TM catalytic triad but distinct location/donor specificity | In silico pairwise alignment | Medium; NW with simple scoring, not a curated MSA; supports (not proves) carry-over hypothesis |

---

## GO Curation Implications (leads — require curator verification)

Current GO annotations on Q96LT4 (from UniProt cross-references) and recommended action:

| GO ID | Aspect / Term | Current evidence | Recommendation | Rationale |
|---|---|---|---|---|
| GO:0002950 | MF: **ceramide phosphoethanolamine synthase activity** | IEA:Ensembl | **Retain & strengthen** (upgrade to experimental, e.g. IDA from PMID 19506037/25667419) | This is the correct, primary catalytic identity |
| GO:0047493 | MF: **ceramide cholinephosphotransferase activity** | IBA:GO_Central | **Remove / do-not-annotate** (or NOT) | = SM-synthase reaction (uses phosphocholine); SMSr is monofunctional CPE synthase (PMID 25667419) |
| GO:0033188 | MF: **sphingomyelin synthase activity** | IBA:GO_Central | **Remove / do-not-annotate** | Paralog (SMS1/SMS2) activity; SMSr makes no SM (PMID 19506037, 25667419) |
| GO:0000139 | CC: **Golgi membrane** | IBA:GO_Central | **Remove / do-not-annotate** | Native protein is ER; Golgi only in SAM-mutant redistribution (PMID 28120887); Golgi = SMS1 (PMID 14685263) |
| GO:0005886 | CC: **plasma membrane** | IBA:GO_Central | **Remove / do-not-annotate** | Paralog SMS2 localization (PMID 14685263); no native SMSr PM evidence |
| GO:0006686 | BP: **sphingomyelin biosynthetic process** | NAS:UniProtKB | **Remove / re-examine** | SMSr does not make SM |
| GO:0046513 | BP: **ceramide biosynthetic process** | IDA:UniProtKB | **Re-examine / generalize** | SMSr's reaction *consumes* ceramide to make CPE; it does not biosynthesize ceramide. Prefer "ceramide metabolic process" / "sphingolipid biosynthetic process (CPE)" or a regulation term |
| GO:2000303 | BP: **regulation of ceramide biosynthetic process** | IDA:UniProtKB | **Retain** | Consistent with sensor role (PMID 19506037) and proposed SPT-activating switch |
| GO:0005783 / GO:0005789 | CC: **ER / ER membrane** | IDA:HPA / IDA:UniProtKB | **Retain (core CC)** | Well-supported native localization |

**Candidate NEW MF terms to consider (leads, in-vitro caution):** phospholipase C activity (GO:0004629) and/or phosphatidate phosphatase / lipid phosphatase activity, and diacylglycerol biosynthetic process — supported by PMID 33621517 but currently in-vitro/overexpression; annotate cautiously (e.g., IDA with a comment, or hold pending in-cell confirmation).

Recommended primary MF for SAMD8 is **ceramide phosphoethanolamine synthase activity (GO:0002950)**; core CC is **endoplasmic reticulum membrane (GO:0005789)**; core BP is **regulation of ceramide/sphingolipid homeostasis**. "Protein binding" is not needed as a summary term.

---

## Paralog Comparison (computed provenance)

Sequences and features fetched from UniProt (Q96LT4, Q86VZ5, Q8NHU3); pairwise identity by Needleman–Wunsch (match +1 / mismatch −1 / gap −2).

| Protein | Acc | Length | TM helices | SAM domain | Active-site residues | Subcellular location |
|---|---|---|---|---|---|---|
| **SAMD8/SMSr** | Q96LT4 | 415 | 6 | Yes (12–78) | His301, His344, Asp348 | **ER membrane** |
| SGMS1/SMS1 | Q86VZ5 | 413 | 6 | Yes | 285, 328, 332 | Golgi membrane |
| SGMS2/SMS2 | Q8NHU3 | 365 | 6 | No | 229, 272, 276 | Plasma membrane; Golgi |

Pairwise identity: SAMD8–SGMS1 = **42.4%**, SAMD8–SGMS2 = **48.2%**, SGMS1–SGMS2 = **63.9%**.

**Interpretation:** The two bona fide SM synthases (SGMS1/SGMS2) are more similar to each other (64%) than either is to SAMD8 (42–48%), so SAMD8 is the divergent outgroup. All three share the 6-TM catalytic core and the conserved SMS/lipid-phosphate-phosphatase active-site triad — which is exactly why phylogenetic/automated pipelines propagate "sphingomyelin synthase activity" and "ceramide cholinephosphotransferase activity" onto SAMD8 (IBA/IEA). However, active-site conservation does **not** determine head-group donor specificity (PC vs PE); the experimental record shows SAMD8 is PE-specific (CPE synthase). Homology therefore cannot override direct substrate–product assays. *(Correction to earlier note: the SAM domain is shared with SGMS1 — it is not unique to SAMD8 — but SAMD8's SAM-driven oligomerization is what confers its ER residence.)*

---

## Mechanistic Scope

- **Immediate molecular function:** transfer of phosphoethanolamine from PE onto ceramide → **ceramide phosphoethanolamine (CPE) + DAG** (EC 2.7.8.-); additionally, promiscuous in-vitro hydrolysis of glycerophospholipids (PE/PA/PI/PC) → **DAG** (PLC/PAP-type). It removes/relocates phospho-head groups; it does **not** add phosphocholine to ceramide (i.e., no SM-synthase direction).
- **Cellular function:** ER-membrane enzyme with lumenal catalytic site; SAM-domain homo-oligomerization anchors it in the ER and underlies a proposed ceramide-sensing function.
- **Downstream/indirect (not direct MF):** suppression of ceramide-induced mitochondrial apoptosis, maintenance of ER-exit-site/secretory-pathway integrity, proposed activation of serine palmitoyltransferase and DAG signaling to DGKδ. These are consequences of loss-of-function or regulatory coupling, **not** direct catalytic outputs, and one (ceramide accumulation on loss) is not reproduced in vivo.

---

## Conflicts and Alternatives

- **Paralog confusion (primary risk):** SMS1/SGMS1 (Golgi SM synthase) and SMS2/SGMS2 (plasma-membrane, bifunctional SM+CPE) supply exactly the Golgi/PM and SM-synthase/cholinephosphotransferase signals seen as **IBA** annotations on SAMD8. These are family-tree propagations, not SAMD8-specific evidence.
- **Construct/mutant artifact:** Golgi localization of SMSr is observed only for SAM-domain oligomerization mutants (PMID 28120887); native full-length protein is ER.
- **In-vitro vs in-vivo:** ceramide accumulation on SMSr loss is a cultured-cell phenotype; mouse KO shows no ceramide change and no overt phenotype (PMID 25667419) — cautions against a strong "ceramide biosynthesis/homeostasis" BP call.
- **Reaction-spectrum ambiguity:** the purified enzyme's dominant in-vitro activity is DAG generation via lipid-phosphatase/PLC chemistry, not CPE synthesis (PMID 33621517); physiological weighting of these activities is unresolved.

---

## Knowledge Gaps

1. **Physiological substrate/direction in vivo.** Checked: in-vitro assays (CPE synthase; PAP/PLC). Gap matters because MF choice (CPE synthase vs lipid phosphatase/PLC) hinges on it. Resolve with cell-based lipidomics of SAMD8-null vs rescue, and inducible catalytic-dead rescue.
2. **SPT-activation switch.** Checked: UniProt "by similarity" note citing 34332077/38388831. Gap: whether SAMD8 directly regulates SPT in human cells. Resolve with SPT-activity/flux measurement upon SAMD8 modulation.
3. **Any bona fide non-ER pool.** Checked: HPA IDA ER; mutant-only Golgi. Gap: whether a minor native Golgi/ER-Golgi-interface pool exists. Resolve with high-resolution/APEX proximity localization of endogenous protein.
4. **Ceramide "biosynthetic process" IDA basis.** Checked: GO record. Gap: the direct experiment behind GO:0046513 IDA is unclear given SMSr consumes ceramide. Resolve by tracing the annotation's supporting figure.

---

## Discriminating Tests

- **Head-group donor assay:** side-by-side ceramide + PE vs ceramide + PC with purified SAMD8 and SMS2 control → confirms CPE-only vs SM (discriminates cholinephosphotransferase claim).
- **Endogenous localization:** knock-in tag or validated antibody + organelle markers/APEX → ER vs Golgi/PM (discriminates compartment claim).
- **Catalytic-dead rescue lipidomics** in SAMD8-KO human cells → whether ceramide/CPE/DAG/SM pools change (discriminates biosynthesis vs regulation).
- **Comparative paralog panel** (SGMS1/SGMS2/SAMD8) in the same assay → attributes SM/Golgi/PM properties to the correct gene, exposing IBA over-propagation.
- **In-vivo relevance:** re-examine mouse/tissue lipidomes (leveraging PMID 25667419) for CPE/DAG rather than ceramide endpoints.

---

## Curation Leads (require curator verification)

- **Action:** Reclassify SAMD8 MF away from SM-synthase family terms toward CPE-synthase.
  - Remove/flag as paralog over-annotation (IBA): GO:0033188 (SM synthase), GO:0047493 (ceramide cholinephosphotransferase), GO:0000139 (Golgi membrane), GO:0005886 (plasma membrane); re-examine GO:0006686 (SM biosynthetic process, NAS) and GO:0046513 (ceramide biosynthetic process, IDA).
  - Retain/strengthen: GO:0002950 (ceramide phosphoethanolamine synthase activity) — upgrade from IEA to experimental (IDA) using PMID 19506037 / 25667419; GO:0005789 (ER membrane); GO:2000303 (regulation of ceramide biosynthetic process).
  - Consider NEW (in-vitro caution): phospholipase C / lipid-phosphatase MF and diacylglycerol biosynthetic process from PMID 33621517.
- **Candidate references + verbatim snippets to verify:**
  - PMID 25667419: "SMS-related protein (SMSr) serves as monofunctional CPE synthase"; "blocking its catalytic activity did not affect ceramide levels ... in the brain or any other tissue."
  - PMID 19506037: "which catalyses the synthesis of the SM analogue ceramide phosphoethanolamine (CPE) in the ER lumen."
  - PMID 28120887: "SMSr/SAMD8 is an ER-resident ceramide phosphoethanolamine synthase"; "their substitution causes ... a partial redistribution of the enzyme to the Golgi."
  - PMID 14685263: "human SMS1 is localised to the Golgi, SMS2 resides primarily at the plasma membrane."
  - PMID 33621517: "purified SMSr showed a DG-generating activity via hydrolysis of PE, phosphatidic acid (PA), phosphatidylinositol (PI), and phosphatidylcholine (PC) in the absence of ceramide."
- **Suggested curator questions:** Is the GO:0046513 IDA traceable to a direct ceramide-synthesis experiment, or a regulatory observation? Are the SM-synthase/Golgi/PM IBA terms desirable to keep given monofunctional CPE + ER data? Should in-vitro PLC/PAP activity be annotated now or held?

---

## Limitations of this review
- Two of the three UniProt-cited PLC papers (PMID 34332077, 38388831) were not retrievable via the available PubMed search and are represented only through the UniProt curated summary (database-level orientation).
- Programmatic UniProt fetch succeeded (Q96LT4) and provided GO/feature provenance; no local bioinformatics files were provided, so sequence/structure claims rely on UniProt features (SAM domain 12–78, 6 TM helices, ER membrane) rather than a fresh de-novo analysis.


## Artifacts

- [OpenScientist SAMD8 GO decision table](openscientist_artifacts/SAMD8_GO_decision_table.csv)
- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)