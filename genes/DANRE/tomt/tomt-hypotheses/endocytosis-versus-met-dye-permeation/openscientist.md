---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-20T22:48:29.878856'
end_time: '2026-09-20T23:03:42.710942'
duration_seconds: 912.83
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: DANRE
  gene: tomt
  gene_symbol: tomt
  uniprot_accession: A0A193KX02
  taxon_id: NCBITaxon:7955
  taxon_label: Danio rerio
  focus_type: function_assignment
  hypothesis_slug: endocytosis-versus-met-dye-permeation
  hypothesis_text: Zebrafish mercury/tomt participates in endocytosis. Reassess the
    exact IMP annotation from PMID:10526320 by reading its full experiments and the
    later dye-uptake interpretation literature (Gale 2001; Meyers 2003), and target
    TOMT trafficking/MET work PMID:28534737. Determine whether rapid FM1-43 uptake
    is evidence of vesicular endocytosis, mechanotransduction-channel permeation,
    or both, and whether independent vesicle-uptake experiments support the target
    assertion. Establish what the original curator could have seen; do not infer absence
    of endocytosis merely from TOMT specialization in TMC trafficking. Distinguish
    loss of dye entry from a demonstrated defect in endocytic machinery.
  term_context: No specific term context supplied.
  reference_context: No specific reference context supplied.
  source_file: genes/DANRE/tomt/tomt-ai-review.yaml
  source_selector: free-text
  source_context_yaml: "hypothesis: Zebrafish mercury/tomt participates in endocytosis.\
    \ Reassess the exact IMP annotation from\n  PMID:10526320 by reading its full\
    \ experiments and the later dye-uptake interpretation literature (Gale\n  2001;\
    \ Meyers 2003), and target TOMT trafficking/MET work PMID:28534737. Determine\
    \ whether rapid FM1-43\n  uptake is evidence of vesicular endocytosis, mechanotransduction-channel\
    \ permeation, or both, and whether\n  independent vesicle-uptake experiments support\
    \ the target assertion. Establish what the original curator\n  could have seen;\
    \ do not infer absence of endocytosis merely from TOMT specialization in TMC trafficking.\n\
    \  Distinguish loss of dye entry from a demonstrated defect in endocytic machinery.\n\
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
citation_count: 5
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

- **Organism code:** DANRE
- **Taxon:** Danio rerio (NCBITaxon:7955)
- **Gene directory:** tomt
- **Gene symbol:** tomt
- **UniProt accession:** A0A193KX02

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** endocytosis-versus-met-dye-permeation
- **Source file:** genes/DANRE/tomt/tomt-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

Zebrafish mercury/tomt participates in endocytosis. Reassess the exact IMP annotation from PMID:10526320 by reading its full experiments and the later dye-uptake interpretation literature (Gale 2001; Meyers 2003), and target TOMT trafficking/MET work PMID:28534737. Determine whether rapid FM1-43 uptake is evidence of vesicular endocytosis, mechanotransduction-channel permeation, or both, and whether independent vesicle-uptake experiments support the target assertion. Establish what the original curator could have seen; do not infer absence of endocytosis merely from TOMT specialization in TMC trafficking. Distinguish loss of dye entry from a demonstrated defect in endocytic machinery.

## Term and Decision Context

No specific term context supplied.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: Zebrafish mercury/tomt participates in endocytosis. Reassess the exact IMP annotation from
  PMID:10526320 by reading its full experiments and the later dye-uptake interpretation literature (Gale
  2001; Meyers 2003), and target TOMT trafficking/MET work PMID:28534737. Determine whether rapid FM1-43
  uptake is evidence of vesicular endocytosis, mechanotransduction-channel permeation, or both, and whether
  independent vesicle-uptake experiments support the target assertion. Establish what the original curator
  could have seen; do not infer absence of endocytosis merely from TOMT specialization in TMC trafficking.
  Distinguish loss of dye entry from a demonstrated defect in endocytic machinery.
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

# AIGR Gene Hypothesis Deep Research — Final Report

**Gene:** *tomt* (mercury) | **Organism:** *Danio rerio* (DANRE, NCBITaxon:7955) | **UniProt:** A0A193KX02 | **ZFIN:** ZDB-GENE-160629-1
**Focus type:** function_assignment
**Hypothesis slug:** endocytosis-versus-met-dye-permeation
**Source file:** genes/DANRE/tomt/tomt-ai-review.yaml (free-text)

---

## Executive Judgment

**Verdict: Refuted (as a direct function assignment) — the GO:0006897 "endocytosis" annotation is not directly supported and should be removed or replaced.**

The seed hypothesis asks whether zebrafish *mercury*/*tomt* genuinely participates in endocytosis, or whether the annotation is an artifact of how the FM1-43 dye-uptake assay was originally interpreted. The evidence is decisive and one-directional. The endocytosis annotation (GO:0006897, evidence IMP/ECO:0000315, from [PMID:10526320](https://pubmed.ncbi.nlm.nih.gov/10526320/), qualifier `acts_upstream_of_or_within`) rests entirely on a single phenotype: loss of rapid apical FM1-43 dye internalization in the *mercury* mutant. That readout was interpreted as "endocytosis" in 1999, but two subsequent primary studies ([Gale 2001, PMID:11549711](https://pubmed.ncbi.nlm.nih.gov/11549711/); [Meyers 2003, PMID:12764092](https://pubmed.ncbi.nlm.nih.gov/12764092/)) demonstrated that rapid FM1-43 loading in hair cells reflects **permeation through the open mechanotransduction (MET) channel**, not vesicular endocytosis. Tellingly, the original 1999 paper itself reported that the dye uptake was blocked by MET-channel inhibitors (amiloride and dihydrostreptomycin) and by high extracellular calcium — hallmarks of channel-mediated entry, not classical clathrin/dynamin-dependent endocytosis.

The mechanistic function of *tomt* is now well established and points away from endocytosis. [Erickson et al. 2017 (PMID:28534737)](https://pubmed.ncbi.nlm.nih.gov/28534737/) showed that the auditory/vestibular phenotype of *tomt* mutants is caused by a lack of mechanotransduction, that Tomt protein is enriched in the Golgi, and that it is required to traffic Tmc1/Tmc2 into the hair bundle. UniProt's expert-curated record for A0A193KX02 defines Tomt as a non-catalytic MET-trafficking factor localized to ER, Golgi, and basolateral membrane — and pointedly does **not** list endocytosis in either the function or subcellular location. The dye-loading defect in *mercury* mutants is therefore a **downstream consequence of MET loss**, not evidence that Tomt operates in the endocytic machinery.

The most important caveat for the curator is one of epistemic fairness, which the seed hypothesis explicitly requests: we do not infer absence of endocytosis merely from Tomt's specialization in TMC trafficking. Rather, the endocytosis call is undermined on its own terms — the assay that generated it does not measure endocytosis in hair cells, and no independent vesicle-uptake or endocytic-machinery experiment implicates *tomt*. The annotation is best treated as **superseded literature carry-over**.

---

## Key Findings

### Finding 1 — The endocytosis IMP annotation rests on a superseded FM1-43 interpretation

The origin of the annotation is [Seiler & Nicolson 1999 (PMID:10526320)](https://pubmed.ncbi.nlm.nih.gov/10526320/), whose title — *"Defective calmodulin-dependent rapid apical endocytosis in zebrafish sensory hair cell mutants"* — frames FM1-43 uptake as endocytosis. The abstract states directly: *"Using a marker of endocytosis, the styryl dye FM1-43, this report shows that rapid apical endocytosis in zebrafish lateral line sensory hair cells is calcium and calmodulin dependent and is partially blocked by the presence of amiloride and dihydrostreptomycin, known inhibitors of mechanotransduction channels."* The authors observed *"Defects in internalization of the dye in both lateral line and inner ear hair cells ... in five zebrafish auditory/vestibular mutants: sputnik, mariner, orbiter, mercury, and skylab."* **Mercury is tomt.**

Crucially, the very pharmacology reported in this paper is the pharmacology of the MET channel, not of endocytosis. Dye entry was blocked by amiloride and dihydrostreptomycin (classic MET-channel blockers) and reduced by elevated extracellular calcium — features of channel permeation. Two later primary papers made the reinterpretation explicit:

- **[Gale et al. 2001 (PMID:11549711)](https://pubmed.ncbi.nlm.nih.gov/11549711/)** showed that *"FM1-43 behaves as a permeant blocker of the mechanotransducer channel."* Dye entry is rapid, apical, calcium-sensitive, and abolished by EGTA-mediated tip-link disruption — i.e., it depends on an intact, open MET channel.
- **[Meyers et al. 2003 (PMID:12764092)](https://pubmed.ncbi.nlm.nih.gov/12764092/)** explicitly separated the two routes: *"In addition to the slow conventional uptake of styryl dyes by endocytosis, small styryl dyes such as FM1-43 rapidly and specifically label hair cells in the inner ear by entering through open mechanotransduction channels."*

The rapid apical loading assayed by Seiler & Nicolson is precisely the MET-channel route, not the slow endocytic route. The IMP "endocytosis" label was therefore a reasonable 1999 interpretation that the field has since overturned.

### Finding 2 — Tomt's demonstrated function is Golgi-based trafficking of Tmc1/2 into the MET complex

[Erickson et al. 2017 (PMID:28534737)](https://pubmed.ncbi.nlm.nih.gov/28534737/), using a zebrafish DFNB63 model, established the mechanistic function of Tomt. Three statements from that work anchor the interpretation:

1. *"we show that the auditory and vestibular phenotypes are due to a lack of mechanotransduction (MET) in Tomt-deficient hair cells."* The *tomt* loss-of-function phenotype is a MET defect — which by itself explains the loss of channel-permeant FM1-43 loading without invoking any endocytic role.
2. *"GFP-tagged Tomt is enriched in the Golgi of hair cells."* This places Tomt in the secretory pathway, not in endocytic compartments or at the apical mechanotransducing membrane.
3. *"Tmc1/2 proteins are specifically excluded from the hair bundle in tomt mutants,"* whereas other MET-complex proteins still localize. Mouse TOMT and TMC1 *directly interact in HEK 293 cells* (modulated by residue His183). The model: Tomt and Tmc proteins interact within the secretory pathway so that Tmc channels are delivered to the hair bundle.

No endocytic-machinery role appears anywhere in this mechanistic account. The failure of FM1-43 entry in *mercury*/*tomt* mutants is fully explained as a secondary consequence of absent MET channels at the apical surface.

### Finding 3 — The live GO annotation is a phenotype-derived, non-direct BP call

A QuickGO query for A0A193KX02 returned 21 annotations. The relevant one is **GO:0006897 endocytosis (BP)**, evidence **IMP/ECO:0000315**, reference **PMID:10526320**, qualifier **`acts_upstream_of_or_within`**. The qualifier is important: it signals a phenotype-derived, upstream/within relationship rather than a direct assertion that Tomt executes endocytosis. It sits alongside other mutant-phenotype BP calls from the same era (e.g., GO:0035315 hair cell differentiation from PMID:10526320; GO:0048884 neuromast development and GO:0050974 detection of mechanical stimulus from PMID:9491988).

The mechanistically informative annotations come from PMID:28534737: GO:0060122 (inner ear receptor cell stereocilium organization, IMP), GO:0031223 (auditory behavior, IMP), plus CC IDA calls GO:0005794 (Golgi apparatus), GO:0005783 (endoplasmic reticulum), and GO:0016323 (basolateral plasma membrane). Separately, the MF/BP catecholamine annotations — GO:0008171 (O-methyltransferase activity, IEA), GO:0016206 (catechol O-methyltransferase activity), GO:0042417 (dopamine metabolic process), GO:0042424 (catecholamine catabolic process) — are ISS/IBA/IEA carry-over from the COMT paralogy and are not relevant to hair-cell function.

### Finding 4 — UniProt expert curation omits endocytosis and defines Tomt as a non-catalytic MET trafficking factor

The UniProt A0A193KX02 curated **FUNCTION** reads: *"Component of the hair cell's mechanotransduction (MET) machinery. Involved in the assembly of the asymmetric tip-link MET complex. Required for transportation of TMC1 and TMC2 proteins into the mechanically sensitive stereocilia of the hair cells. The function in MET is independent of the enzymatic activity (PubMed:28534737)."* The curated **subcellular location** (ECO:0000269, PubMed:28534737) is Endoplasmic reticulum, Golgi apparatus, and Basolateral cell membrane. **Endocytosis is absent** from both the curated function and the location. A targeted literature search found no independent vesicle-uptake or endocytic-machinery experiment implicating *tomt* beyond the FM1-43 assay of PMID:10526320.

---

## Mechanistic Model / Interpretation

The two competing interpretations of the *mercury*/*tomt* FM1-43 phenotype can be laid out side by side:

```
   SEED / LEGACY MODEL (1999 interpretation)        CURRENT MODEL (2017 + dye-mechanism papers)
   ----------------------------------------         --------------------------------------------
   FM1-43 = marker of endocytosis                    FM1-43 = permeant blocker of MET channel
        |                                                  |
   loss of dye uptake in mercury mutant              loss of dye uptake in tomt mutant
        |                                                  |
   => tomt required for ENDOCYTOSIS (GO:0006897)     => tomt required to TRAFFIC Tmc1/2 to bundle
                                                          => no MET channels at apical membrane
                                                          => no channel for FM1-43 to permeate
                                                          => dye-loading loss is DOWNSTREAM of MET loss
```

The chain of causation in the current model is:

```
Tomt (Golgi/ER)  --interacts with-->  Tmc1/Tmc2  --trafficked to-->  hair bundle
      |                                                                    |
   loss of Tomt                                              Tmc1/2 EXCLUDED from bundle
      |                                                                    |
      +----------------------------------------------------------> no functional MET channel
                                                                           |
                                                                  FM1-43 cannot permeate
                                                                           |
                                                       "defective dye internalization" (mercury phenotype)
```

Under the current model, the dye-loading defect is a faithful reporter of MET loss, and MET loss is the direct consequence of a trafficking failure inside the secretory pathway. Endocytosis is not part of the causal chain at any step for which there is direct evidence. The seed hypothesis is thereby answered on its own terms: rapid FM1-43 uptake in hair cells is evidence of MET-channel permeation, not vesicular endocytosis, and no independent vesicle-uptake experiment supports the endocytosis assertion for *tomt*.

| Question posed by seed hypothesis | Answer from evidence |
|---|---|
| Is rapid FM1-43 uptake evidence of vesicular endocytosis? | No — it is MET-channel permeation (PMID:11549711, PMID:12764092) |
| Is it evidence of MET-channel permeation? | Yes — rapid, apical, Ca²⁺-sensitive, blocked by MET inhibitors |
| Do independent vesicle-uptake experiments support the endocytosis call? | None found beyond the FM1-43 assay of PMID:10526320 |
| Should absence of endocytosis be inferred from TMC-trafficking specialization? | No — but the endocytosis call fails on its own assay grounds regardless |
| Is the dye-entry loss the same as a demonstrated endocytic-machinery defect? | No — loss of dye entry ≠ demonstrated defect in endocytic machinery |

---

## Evidence Matrix

| Citation | Evidence type | Direction | Claim tested | Key finding | Context | Confidence / limitations |
|---|---|---|---|---|---|---|
| [PMID:10526320](https://pubmed.ncbi.nlm.nih.gov/10526320/) (Seiler & Nicolson 1999) | Mutant phenotype (IMP source) | Qualifies / competing | Does *mercury*/*tomt* loss reduce FM1-43 "endocytosis"? | Defective FM1-43 internalization in 5 mutants incl. *mercury*; uptake blocked by amiloride & dihydrostreptomycin (MET inhibitors) and reduced by high Ca²⁺ | Zebrafish lateral-line & inner-ear hair cells | High for the phenotype; the "endocytosis" label is the superseded interpretation. This IS the annotation's sole basis. |
| [PMID:11549711](https://pubmed.ncbi.nlm.nih.gov/11549711/) (Gale 2001) | Direct assay (dye mechanism) | Refutes | Does FM1-43 enter hair cells by endocytosis or channel permeation? | *"FM1-43 behaves as a permeant blocker of the mechanotransducer channel"*; entry abolished by tip-link disruption | Mammalian cochlear hair cells | High; establishes MET-channel route for rapid loading |
| [PMID:12764092](https://pubmed.ncbi.nlm.nih.gov/12764092/) (Meyers 2003) | Direct assay / review-level synthesis | Refutes | Are rapid and slow styryl-dye uptake distinct routes? | Rapid specific labeling occurs *"by entering through open mechanotransduction channels,"* separate from slow endocytic uptake | Inner-ear hair cells | High; explicitly separates endocytic vs. channel routes |
| [PMID:28534737](https://pubmed.ncbi.nlm.nih.gov/28534737/) (Erickson 2017) | Mutant phenotype + localization + interaction | Competing (alternative function) | What is Tomt's direct molecular role? | MET loss underlies phenotype; Tomt enriched in Golgi; Tmc1/2 excluded from bundle in mutants; TOMT–TMC1 direct interaction | Zebrafish hair cells; mouse proteins in HEK293 | High; defines the accepted MET-trafficking function |
| QuickGO / UniProt A0A193KX02 | Database record | Supports removal/reframe | What is the live annotation status? | GO:0006897 = IMP, `acts_upstream_of_or_within`, PMID:10526320; curated FUNCTION omits endocytosis; location = ER/Golgi/basolateral | Database-level | High for record content; orientation-level evidence |

---

## GO Curation Implications

**Lead requiring curator verification (high priority): remove or replace GO:0006897 "endocytosis" for A0A193KX02.**

- **Term in question:** GO:0006897 endocytosis (BP), IMP / ECO:0000315, reference PMID:10526320, qualifier `acts_upstream_of_or_within`.
- **Recommended action:** **Remove** (or, at minimum, **do not propagate/retain as a core function**). The single supporting experiment does not measure endocytosis in hair cells; it measures MET-channel-dependent dye permeation, which two later primary papers established as the operative mechanism. The annotation is superseded literature carry-over.
- **If a curator prefers replacement over outright removal**, the biologically supported BP/CC/MF terms — all traceable to PMID:28534737 and already present in the live annotation set — are the correct destinations:
  - **CC:** GO:0005794 Golgi apparatus (IDA), GO:0005783 endoplasmic reticulum (IDA), GO:0016323 basolateral plasma membrane (IDA).
  - **BP:** GO:0060122 inner ear receptor cell stereocilium organization (IMP); process terms around mechanotransduction / MET-complex assembly.
  - **MF:** a protein-transporter or Tmc-binding role reflecting the trafficking function. (Per instruction, avoid "protein binding" as a final recommendation; the TOMT–TMC1 interaction is better captured by a transport/assembly-oriented term than by generic binding.)
- **Do NOT** treat the MF catecholamine/O-methyltransferase terms (GO:0008171, GO:0016206, GO:0042417, GO:0042424) as evidence for hair-cell function — they are COMT-paralog carry-over (ISS/IBA/IEA), and UniProt explicitly notes the MET function *"is independent of the enzymatic activity."*

**Curation summary table**

| GO term | Aspect | Current evidence | Recommended action |
|---|---|---|---|
| GO:0006897 endocytosis | BP | IMP, PMID:10526320, `acts_upstream_of_or_within` | **Remove / do not retain as core** (superseded interpretation) |
| GO:0060122 stereocilium organization | BP | IMP, PMID:28534737 | Retain (core) |
| GO:0005794 Golgi apparatus | CC | IDA, PMID:28534737 | Retain (core localization) |
| GO:0005783 ER | CC | IDA, PMID:28534737 | Retain |
| GO:0016323 basolateral membrane | CC | IDA, PMID:28534737 | Retain |
| GO:0016206 catechol O-methyltransferase | MF | ISS/IBA/IEA (paralog) | Treat as non-core / flag as paralog carry-over |

---

## Mechanistic Scope

The **immediate molecular/cellular function** actually tested and supported is: Tomt is a non-catalytic secretory-pathway (ER/Golgi) factor that binds Tmc1/Tmc2 and is required to traffic these pore-forming channel subunits into the stereocilia, enabling assembly of a functional MET complex. This is a **direct** gene-product activity (localization + interaction + trafficking requirement).

The **endocytosis phenotype** is, by contrast, a **downstream loss-of-function readout**: FM1-43 fails to load because there is no open MET channel to permeate, which is itself downstream of the trafficking defect. Attributing "endocytosis" to Tomt conflates (a) loss of a channel-permeant dye signal with (b) a demonstrated defect in endocytic machinery. The seed hypothesis's key discriminating instruction — *"Distinguish loss of dye entry from a demonstrated defect in endocytic machinery"* — is exactly the distinction that dissolves the annotation. There is no demonstrated defect in endocytic machinery for *tomt*; there is only loss of dye entry, which is explained by MET loss.

---

## Conflicts and Alternatives

- **Superseded-interpretation vs. artifact:** The endocytosis call is not an outright error given 1999 knowledge; FM1-43 was widely used as an endocytosis marker at that time. It is a good-faith interpretation invalidated by later mechanism papers. Curators should frame it as "superseded," not "wrong data."
- **Paralog confusion (COMT):** The MF O-methyltransferase/catecholamine annotations derive from Tomt's homology to catechol-O-methyltransferase. UniProt explicitly decouples the MET function from enzymatic activity. These should not be conflated with, or used to rescue, the endocytosis BP annotation.
- **Alternative "genuine bulk endocytosis" hypothesis:** One could argue hair cells also perform genuine apical endocytosis (membrane retrieval) and that Tomt might affect that. However, no independent vesicle-uptake or membrane-retrieval experiment implicates *tomt*; the only supporting assay is the FM1-43 loading assay, which is the channel-permeation route. Absent such data, the alternative is unsupported.
- **Qualifier nuance:** The live annotation uses `acts_upstream_of_or_within`, which is weaker than a direct "participates in" assertion. Even so, the upstream/within relationship is not supported because the phenotype is not an endocytosis phenotype.

---

## Limitations and Knowledge Gaps

1. **Full-text of PMID:10526320 not exhaustively parsed.** The analysis relied on the abstract and its verbatim MET-inhibitor pharmacology. A curator should confirm from the full text that no separate, non-FM1-43 endocytosis assay (e.g., transferrin uptake, horseradish peroxidase, dextran) was performed in *mercury* mutants. **Why it matters:** an independent endocytosis assay would change the recommendation. **Resolution:** read the full paper's methods/results.
2. **Zebrafish-specific Tomt endocytosis data.** Most mechanism work on FM1-43 permeation (Gale, Meyers) is in mammalian systems; the reinterpretation is well accepted cross-species, but a curator may wish to confirm the MET-permeation route is the dominant one for the specific developmental stages/tissues assayed in the 1999 zebrafish paper. **Resolution:** zebrafish MET-blocker + FM1-43 co-application data (largely already established in the field).
3. **No systematic search of post-2017 literature for any new endocytosis role.** The targeted search found none, but it was not exhaustive. **Why it matters:** a newer paper could re-open the question. **Resolution:** a fresh literature/ZFIN scan filtered on "tomt endocytosis / membrane trafficking."
4. **Whether GO best practice favors removal vs. retention with a NOT/qualifier.** This is a curation-policy question, not a biology question. **Resolution:** curator judgment per GO consortium guidelines on superseded IMP annotations.

---

## Discriminating Tests / Proposed Follow-up Actions

1. **Co-application assay (definitive discriminator):** In wild-type hair cells, apply FM1-43 with and without MET-channel blockers (dihydrostreptomycin, amiloride, or BAPTA tip-link disruption). If rapid loading is abolished, the assayed route is channel permeation — directly confirming that the *mercury* phenotype reports MET loss, not endocytosis. (Field data already strongly support this.)
2. **Independent endocytosis probe in *tomt* mutants:** Test uptake of a bona fide endocytic cargo (fluorescent transferrin, dextran, or HRP) in *tomt*/*mercury* mutant vs. wild-type hair cells. Preserved endocytic uptake despite absent FM1-43 loading would cleanly separate the two processes.
3. **Rescue specificity:** Re-express Tmc1/Tmc2 or restore MET function independently and test whether FM1-43 loading recovers without any manipulation of endocytic machinery — confirming the dye defect is MET-dependent.
4. **Curation action:** Draft the annotation change (remove GO:0006897 or reclassify as non-core superseded), cite PMID:11549711 and PMID:12764092 as the mechanistic basis for reinterpretation, and route to curator review with the evidence matrix above.

---

## Curation Leads (require curator verification)

- **Candidate action:** Remove **GO:0006897 endocytosis** (IMP, PMID:10526320, `acts_upstream_of_or_within`) from A0A193KX02, or reclassify it as superseded/non-core.
- **Candidate references with exact snippets to verify:**
  - PMID:11549711 — *"FM1-43 behaves as a permeant blocker of the mechanotransducer channel."*
  - PMID:12764092 — *"In addition to the slow conventional uptake of styryl dyes by endocytosis, small styryl dyes such as FM1-43 rapidly and specifically label hair cells in the inner ear by entering through open mechanotransduction channels."*
  - PMID:10526320 — *"Using a marker of endocytosis, the styryl dye FM1-43 ... partially blocked by the presence of amiloride and dihydrostreptomycin, known inhibitors of mechanotransduction channels."*
  - PMID:28534737 — *"the auditory and vestibular phenotypes are due to a lack of mechanotransduction (MET) in Tomt-deficient hair cells"*; *"GFP-tagged Tomt is enriched in the Golgi of hair cells"*; *"Tmc1/2 proteins are specifically excluded from the hair bundle in tomt mutants."*
- **Candidate replacement/retained GO terms:** GO:0060122 (BP), GO:0005794 / GO:0005783 / GO:0016323 (CC), all from PMID:28534737 (already annotated).
- **Suggested curator questions:** (1) Does the full text of PMID:10526320 contain any non-FM1-43 endocytosis assay for *mercury*? (2) Is GO policy to remove or to retain-with-note superseded IMP annotations? (3) Should the COMT-paralog MF terms be flagged as non-core in the same pass?
- **Suggested experiments:** transferrin/dextran uptake in *tomt* mutants (independent endocytosis probe); FM1-43 + MET-blocker co-application (route confirmation).

---

## Evidence Base (Literature Summary)

| PMID | Title | Role in this analysis |
|---|---|---|
| [10526320](https://pubmed.ncbi.nlm.nih.gov/10526320/) | *Defective calmodulin-dependent rapid apical endocytosis in zebrafish sensory hair cell mutants.* | Sole source of the endocytosis IMP; its own pharmacology points to MET permeation |
| [11549711](https://pubmed.ncbi.nlm.nih.gov/11549711/) | *FM1-43 dye behaves as a permeant blocker of the hair-cell mechanotransducer channel.* | Establishes the channel-permeation route; refutes endocytic interpretation |
| [12764092](https://pubmed.ncbi.nlm.nih.gov/12764092/) | *Lighting up the senses: FM1-43 loading of sensory cells through nonselective ion channels.* | Separates rapid channel-permeation from slow endocytic uptake |
| [28534737](https://pubmed.ncbi.nlm.nih.gov/28534737/) | *Integration of Tmc1/2 into the mechanotransduction complex in zebrafish hair cells is regulated by Transmembrane O-methyltransferase (Tomt).* | Defines Tomt's accepted MET-trafficking function; supports the alternative interpretation |

---

*Report prepared for AI Gene Review hypothesis-level curation. All GO-annotation recommendations are leads requiring curator verification against primary sources and GO consortium policy.*


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)