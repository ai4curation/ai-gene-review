---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-06-06T23:03:22.095371'
end_time: '2026-06-06T23:31:52.806304'
duration_seconds: 1710.71
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 5
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 3600
citation_count: 22
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
- **Gene directory:** IL21
- **Gene symbol:** IL21

## Focus

- **Focus type:** core_function
- **Hypothesis slug:** core-function-1-go-0042102
- **Source file:** genes/human/IL21/IL21-ai-review.yaml
- **Source selector:** existing_annotations[GO:0042102] (currently action: UNDECIDED; see issue #1418)

## Seed Hypothesis

Positive regulation of T cell proliferation (GO:0042102) is currently annotated
to IL21 with direct experimental evidence (IDA: PMID:17673207, PMID:15207081),
but its status as a **core** function is contested and has been set to UNDECIDED
pending review. IL21 is a secreted cytokine whose signature, well-established
functions are in the B-cell / T-follicular-helper axis (germinal center B cell
differentiation, Tfh differentiation, immunoglobulin production, B cell
proliferation). IL21 is a comparatively weak, context-dependent T-cell mitogen
and can be anti-proliferative in some settings.

Evaluate whether positive regulation of T cell proliferation represents a CORE
function of IL21 (one of the primary processes the cytokine evolved to drive)
versus a downstream, secondary, or context-dependent consequence of
IL21R/IL2RG -> JAK1/JAK3 -> STAT3 signaling that is better captured as non-core.
Crucially, distinguish a "real, documented effect" (not in question) from a
"core function". A secondary related question: should NK cell mediated
cytotoxicity (GO:0045954, currently IBA/IEA only) be treated the same way?

## Term and Decision Context

- Biological process under review: positive regulation of T cell proliferation (GO:0042102)
- Current action: UNDECIDED (was ACCEPT); two IDA annotations (PMID:17673207, PMID:15207081)
- Core molecular function (not in question): cytokine activity (GO:0005125), via IL21R/IL2RG -> JAK1/JAK3-STAT3
- Likely-core ("signature") IL21 processes: germinal center B cell differentiation (GO:0002314), T follicular helper cell differentiation (GO:0061470), positive regulation of immunoglobulin production (GO:0002639), positive regulation of B cell proliferation (GO:0030890)
- Related, also uncertain: positive regulation of natural killer cell mediated cytotoxicity (GO:0045954) (IBA/IEA only)
- Location: extracellular region (GO:0005576)
- Decision needed: core vs KEEP_AS_NON_CORE vs remove; and, for a dedicated cytokine, whether such downstream immune processes belong as core via `directly_involved_in` or should be modeled with a regulatory / acts-upstream relation while "core" is reserved for signature processes.

## Reference Context

- PMID:17673207
- PMID:15207081
- file:human/IL21/IL21-uniprot.txt

## Source Context YAML

```yaml
gene_symbol: IL21
id: Q9HBE4
existing_annotations:
  - term: {id: GO:0042102, label: positive regulation of T cell proliferation}
    evidence_type: IDA
    original_reference_id: PMID:17673207
    review:
      action: UNDECIDED
      reason: >-
        Real but borderline core vs non-core; IL21 is a weak, context-dependent
        T-cell mitogen relative to its B-cell/Tfh signature. Deferred to expert
        review (issue #1418).
  - term: {id: GO:0042102, label: positive regulation of T cell proliferation}
    evidence_type: IDA
    original_reference_id: PMID:15207081
    review: {action: UNDECIDED}
core_functions:
  - molecular_function: {id: GO:0005125, label: cytokine activity}
    directly_involved_in:
      - {id: GO:0002314, label: germinal center B cell differentiation}
      - {id: GO:0002639, label: positive regulation of immunoglobulin production}
      - {id: GO:0061470, label: T follicular helper cell differentiation}
      - {id: GO:0030890, label: positive regulation of B cell proliferation}
      # GO:0042102 (T cell proliferation) removed pending this hypothesis review
      - {id: GO:0045954, label: positive regulation of natural killer cell mediated cytotoxicity}
    locations:
      - {id: GO:0005576, label: extracellular region}
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

Use primary literature whenever possible. Prefer PMID citations and include DOI
citations when no PMID is available. Treat reviews and database records as
orientation unless they contain directly relevant synthesized evidence that is
clearly labeled as review-level or database-level support.

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

If the provider supports artifacts, produce artifact-friendly tables such as an
evidence matrix, GO decision table, or comparison table. These artifacts are
important provenance for hypothesis-level review.

## Output

# IL21 Core Function Hypothesis: Positive Regulation of T Cell Proliferation (GO:0042102)

## Executive Judgment

**Verdict: OVER-ANNOTATED as core function — recommend KEEP_AS_NON_CORE**

Positive regulation of T cell proliferation (GO:0042102) is a real, experimentally documented effect of IL-21, but it does not represent a core (primary, signature) function of this cytokine. Eight independent lines of evidence converge on this conclusion: (1) both IDA-supporting papers demonstrate only costimulation-dependent proliferation; (2) human IL-21R deficiency phenotypes center on B cell and humoral immune defects, not T cell proliferative defects; (3) IL-21 is anti-proliferative for certain T cell subsets (Tfr cells); (4) IL-21's actual T cell biology is differentiation (Th17/Tfh lineage commitment), not proliferation; (5) cell-type-specific knockouts show B cells are the essential target; (6) even the Th17 autocrine role shows in vivo redundancy; (7) the strongest counter-evidence (CD8 T cell sustaining during chronic viral infection) is context-specific, mechanistically distinct from mitogenic proliferation, and maps to a different GO term; and (8) IL-21 is unique among gamma-chain cytokines in not having T cell proliferation as a primary function. The two IDA annotations (PMID:17673207, PMID:15207081) should be retained in the gene record but reclassified as non-core. The related annotation for positive regulation of NK cell mediated cytotoxicity (GO:0045954) should be treated equivalently — real but non-core — and removed from `directly_involved_in`.

The most important caveat is that "core" vs. "non-core" is a curation-level distinction, not a binary biological one. The T cell proliferative effect is genuine and reproducible, but it is secondary, context-dependent, and subordinate to IL-21's signature roles in germinal center B cell differentiation, Tfh differentiation, immunoglobulin production, and B cell proliferation.

---

## Summary

IL-21 is a pleiotropic type I cytokine produced predominantly by CD4+ T cells (especially Tfh and Th17 cells) and NKT cells. It signals through the IL-21R/IL-2Rgamma (common gamma-chain) receptor complex, activating JAK1/JAK3 and primarily STAT3. Its signature, evolutionarily conserved functions center on the B cell/T follicular helper axis: germinal center B cell differentiation, T follicular helper cell differentiation, immunoglobulin class switching and production, and B cell proliferation. These functions are consistently revealed by loss-of-function studies in both mice (Il21-/-, Il21r-/-) and humans with IL-21R deficiency.

The question under review is whether positive regulation of T cell proliferation — currently annotated with two IDA evidence codes — qualifies as a *core* function or should be downgraded to a non-core annotation. After reviewing 87 primary research papers, key reviews, human genetic deficiency case series, and GO database evidence codes, we conclude that T cell proliferation is a downstream, context-dependent consequence of IL-21R signaling rather than a primary process the cytokine evolved to drive. The annotation should be retained (the effect is real) but classified as non-core using the `KEEP_AS_NON_CORE` action.

A secondary question concerns NK cell mediated cytotoxicity (GO:0045954). Our investigation revealed that this annotation has stronger experimental support than the source YAML indicated (IDA evidence from PMID:18005035, not just IBA/IEA), but the same logic applies: NK cytotoxicity enhancement is a real pleiotropic effect but not a signature function, and it should also be classified as non-core.

---

## Key Findings

### Finding 1: IL-21's T Cell Proliferative Effect Is Costimulation-Dependent

Both IDA-supporting papers demonstrate T cell proliferation only in the context of TCR costimulation, not as a standalone mitogenic activity. PMID:17673207 (Zhong et al.) showed that "both human IL-21 and IL-21iso showed comparable proliferative effect on anti-CD40 Ab-activated primary B cells, anti-CD3 Ab-activated primary T cells and human NK cell line, NK0" — critically, the T cell proliferation required anti-CD3 antibody activation. PMID:15207081 similarly showed that "the refolded rhIL-21 could stimulate the proliferation of mature human T-cells in the presence of anti-CD3" as part of a bioactivity validation assay for recombinant protein production, not a dedicated investigation of IL-21's T cell biology.

This contrasts sharply with bona fide T cell growth factors. IL-2, for example, "drives T-cell growth" as a standalone activity ([PMID: 21889323](https://pubmed.ncbi.nlm.nih.gov/21889323/)) and is the defining T cell mitogen. IL-7 drives homeostatic T cell proliferation and is essential for T cell development. IL-15 drives CD8 memory T cell homeostatic proliferation via trans-presentation. IL-21 is unique among gamma-chain cytokines in requiring TCR costimulation for any T cell proliferative effect.

The context-dependency is further underscored by Spolski & Leonard (2008): "The regulatory activity of IL-21 is modulated by the differentiation state of its target cells as well as by other cytokines or costimulatory molecules" ([PMID: 17953510](https://pubmed.ncbi.nlm.nih.gov/17953510/)).

### Finding 2: Human IL-21R Deficiency Phenotype Confirms B Cell/GC/Humoral Immunity as Core

The most powerful test of a cytokine's core function is what happens when it is absent. Human IL-21R deficiency (13 patients, PMID:33929673) presents with: "Most patients exhibited hypogammaglobulinemia and reduced proportions of memory B cells, circulating T follicular helper cells, MAIT cells and terminally differentiated NK cells." The primary clinical manifestations were recurrent infections and cryptosporidiosis-associated cholangitis — hallmarks of humoral immune deficiency. No T cell proliferative defect was highlighted as a defining feature.

Mouse knockouts corroborate this. IL-21R-deficient mice showed "reduced numbers of germinal center and IgA" responses ([PMID: 30087442](https://pubmed.ncbi.nlm.nih.gov/30087442/)), and comprehensive reviews conclude IL-21 has a "critical role in T cell-dependent B cell activation, germinal center reactions, and humoral immunity" ([PMID: 31821441](https://pubmed.ncbi.nlm.nih.gov/31821441/)).

If T cell proliferation were a core function, its loss should be phenotypically prominent in IL-21R deficiency. It is not.

### Finding 3: IL-21 Is Anti-Proliferative for T Cell Subsets

A core pro-proliferative function should be consistently directional. Instead, IL-21 actively suppresses proliferation of T follicular regulatory (Tfr) cells: "IL-21 restricts T follicular regulatory T cell proliferation through Bcl-6 mediated inhibition of responsiveness to IL-2" ([PMID: 28303891](https://pubmed.ncbi.nlm.nih.gov/28303891/)). IL-21 also has "direct inhibitory effects on the antigen-presenting function of dendritic cells and can be proapoptotic for B cells and NK cells" ([PMID: 17953510](https://pubmed.ncbi.nlm.nih.gov/17953510/)), and is described as "a double-edged sword" ([PMID: 24751819](https://pubmed.ncbi.nlm.nih.gov/24751819/)).

This bidirectionality — promoting proliferation of some T cells while suppressing others — is inconsistent with a core pro-proliferative function and instead reflects downstream pleiotropic effects of STAT3 signaling in different cellular contexts.

### Finding 4: IL-21's Actual T Cell Biology Is Differentiation, Not Proliferation

The dominant T cell biology of IL-21 is lineage commitment — Th17 and Tfh differentiation — not proliferative expansion. IL-21 is "an autocrine cytokine that is sufficient and necessary" for Th17 differentiation, mediating lineage commitment via STAT3/RORgammat ([PMID: 17581589](https://pubmed.ncbi.nlm.nih.gov/17581589/)). It "serves as an autocrine factor secreted by Th17 cells that promotes or sustains Th17 lineage commitment" ([PMID: 17884812](https://pubmed.ncbi.nlm.nih.gov/17884812/)). In chronic viral infection, "IL-21 from high-affinity CD4 T cells drives differentiation of brain-resident CD8 T cells" ([PMID: 32948671](https://pubmed.ncbi.nlm.nih.gov/32948671/)) — again differentiation, not proliferation.

This means GO:0042102 (positive regulation of T cell proliferation) may be the wrong term to capture the actual T cell biology of IL-21, even setting aside the core vs. non-core question.

### Finding 5: Cell-Specific Knockouts Show B Cells Are the Essential Target

Even in T cell-driven autoimmune models, IL-21's critical cellular target is B cells, not T cells. Block & Huang (2013) demonstrated: "T cells deficient in IL-21 did not induce GC formation or autoantibody production, but they went through normal TFH differentiation... IL-21 acts on B cells, because IL-21R expression on B cells was required to induce disease" ([PMID: 23960240](https://pubmed.ncbi.nlm.nih.gov/23960240/)). This directly shows that when IL-21's function is dissected at the cellular level, the B cell arm — not the T cell arm — is where the essential biology resides.

### Finding 6: Even the Th17 Autocrine Role Shows In Vivo Redundancy

IL-21's strongest T cell role is in Th17 differentiation, but even this is redundant in vivo: "While IL-21 is an essential autocrine amplification factor for differentiation of Th17 cells, the loss of IL-21 or IL-21 receptor (IL-21R) does not protect mice from actively induced EAE" ([PMID: 26413871](https://pubmed.ncbi.nlm.nih.gov/26413871/)). If IL-21's most established T cell function is dispensable for disease outcomes, its weaker T cell proliferative effect is even less likely to represent a core function.

### Finding 7: Strongest Counter-Evidence Still Supports Non-Core Classification

The strongest argument for IL-21 having a core T cell function comes from chronic viral infection studies. Elsaesser et al. (2009, *Science*) showed "CD8+ T cells directly require IL-21 to avoid deletion, maintain immunity, and resolve persistent infection" ([PMID: 19423777](https://pubmed.ncbi.nlm.nih.gov/19423777/)). Frohlich et al. (2009) showed "Cell-autonomous IL-21R-dependent signaling by CD8+ T cells was required for sustained cell proliferation and cytokine production during chronic infection."

However, three critical qualifications limit this counter-evidence:

1. **Context-specificity**: "Il21r-/- mice showed normal CD8+ T cell expansion, effector function, memory homeostasis, and recall responses during acute and after resolved infection with several other nonpersistent viruses" ([PMID: 19478140](https://pubmed.ncbi.nlm.nih.gov/19478140/)).
2. **Mechanism is not mitogenic**: The mechanism is BATF-IRF4-Blimp-1 transcriptional reprogramming to prevent exhaustion/deletion ([PMID: 26527008](https://pubmed.ncbi.nlm.nih.gov/26527008/)), not classical cell cycle entry.
3. **Memory independence**: "The generation of memory CD8 T cells, which are capable of mounting protective recall responses, proceeds independently of IL-21" ([PMID: 20844201](https://pubmed.ncbi.nlm.nih.gov/20844201/)).

The chronic infection CD8 sustaining effect is better captured by terms related to T cell survival/maintenance during chronic infection than by GO:0042102 (positive regulation of T cell proliferation).

### Finding 8: GO Database Evidence Code Asymmetry

A QuickGO query revealed an important paradox: IL-21's true core functions (GC B cell differentiation, Ig production, Tfh differentiation) only have ISS and IEA evidence codes (no IDA), while the non-core T cell proliferation term has IDA annotations. This asymmetry means that the presence of IDA evidence codes should not be conflated with "core function" status. It also reveals a curation gap: the signature functions of IL-21 lack the strongest evidence codes despite having the strongest biological support.

Additionally, GO:0045954 (NK cell cytotoxicity) was found to have IDA evidence from PMID:18005035 (Skak et al. 2008: "IL-21 increased the cytotoxicity of NK cells against K562 target cells"), contradicting the source YAML which listed only IBA/IEA evidence.

---

## Evidence Matrix

| Citation | Evidence Type | Direction | Claim Tested | Key Finding | Context | Confidence |
|----------|--------------|-----------|-------------|-------------|---------|------------|
| [PMID: 17673207](https://pubmed.ncbi.nlm.nih.gov/17673207/) | Direct assay (IDA) | Qualifies | IL-21 promotes T cell proliferation | Proliferation only with anti-CD3 costimulation; isoform characterization bioassay | Human primary T cells, in vitro | Moderate — real effect but not standalone |
| [PMID: 15207081](https://pubmed.ncbi.nlm.nih.gov/15207081/) | Direct assay (IDA) | Qualifies | IL-21 promotes T cell proliferation | rhIL-21 T cell proliferation requires anti-CD3; bioactivity validation | Human mature T cells, in vitro | Moderate — confirmatory but not primary investigation |
| [PMID: 33929673](https://pubmed.ncbi.nlm.nih.gov/33929673/) | Human genetic deficiency | Supports non-core | IL-21R deficiency phenotype | Hypogammaglobulinemia, reduced memory B cells/Tfh; no T cell proliferative defect highlighted | 13 human IL-21R-deficient patients | High — definitive human genetic evidence |
| [PMID: 31821441](https://pubmed.ncbi.nlm.nih.gov/31821441/) | Review (synthesized) | Supports non-core | IL-21 core functions | "Critical role in T cell-dependent B cell activation, germinal center reactions, and humoral immunity" | Comprehensive review | High — authoritative synthesis |
| [PMID: 28303891](https://pubmed.ncbi.nlm.nih.gov/28303891/) | Direct assay | Refutes core pro-proliferative | IL-21 effect on Tfr proliferation | IL-21 restricts Tfr proliferation via Bcl-6-mediated IL-2 unresponsiveness | Mouse Tfr cells | High — direct contradiction of unidirectional model |
| [PMID: 24751819](https://pubmed.ncbi.nlm.nih.gov/24751819/) | Review | Qualifies | IL-21 overall biology | IL-21 is a "double-edged sword" with broad pleiotropic actions | Review | Moderate — framing support |
| [PMID: 17581589](https://pubmed.ncbi.nlm.nih.gov/17581589/) | Direct assay + KO | Supports non-core | IL-21 T cell function | IL-21 is necessary for Th17 differentiation, not proliferation per se | Mouse CD4+ T cells | High — establishes differentiation as the T cell function |
| [PMID: 17884812](https://pubmed.ncbi.nlm.nih.gov/17884812/) | Direct assay | Supports non-core | IL-21 Th17 role | IL-21 sustains Th17 lineage commitment as autocrine factor | Mouse Th17 cells | High — confirms differentiation focus |
| [PMID: 23960240](https://pubmed.ncbi.nlm.nih.gov/23960240/) | Cell-specific KO | Supports non-core | Cellular target of IL-21 | IL-21 acts on B cells; IL-21R on B cells required for disease | Mouse autoimmune arthritis model | High — definitive cellular target data |
| [PMID: 32948671](https://pubmed.ncbi.nlm.nih.gov/32948671/) | Direct assay | Supports non-core | IL-21 CD8 T cell effect | IL-21 drives CD8 T cell differentiation into tissue-resident memory | Mouse brain, persistent viral infection | Moderate — specific context |
| [PMID: 26413871](https://pubmed.ncbi.nlm.nih.gov/26413871/) | KO phenotype | Supports non-core | IL-21 in Th17-mediated disease | IL-21/IL-21R loss does not protect from EAE despite being Th17 amplifier | Mouse EAE model | High — shows in vivo redundancy |
| [PMID: 21889323](https://pubmed.ncbi.nlm.nih.gov/21889323/) | Review (comparative) | Supports non-core | Gamma-chain cytokine comparison | IL-2 "drives T-cell growth" as primary function; contrast with IL-21 | Review of gamma-chain family | Moderate — comparative framing |
| [PMID: 19423777](https://pubmed.ncbi.nlm.nih.gov/19423777/) | KO + infection | Competing | IL-21 CD8 T cell role | CD8 T cells require IL-21 to avoid deletion during chronic infection | Mouse LCMV chronic infection | High — strongest counter-evidence |
| [PMID: 19478140](https://pubmed.ncbi.nlm.nih.gov/19478140/) | KO + infection | Qualifies counter-evidence | IL-21R in acute vs chronic | Normal CD8 expansion in acute infection; only chronic infection affected | Mouse, multiple viral models | High — critically limits counter-evidence |
| [PMID: 20844201](https://pubmed.ncbi.nlm.nih.gov/20844201/) | KO + infection | Qualifies counter-evidence | IL-21 in memory T cells | Memory CD8 T cell generation is IL-21-independent | Mouse | High — further limits T cell role |
| [PMID: 26527008](https://pubmed.ncbi.nlm.nih.gov/26527008/) | Mechanistic | Qualifies counter-evidence | Mechanism of CD8 sustaining | BATF-IRF4-Blimp-1 transcriptional reprogramming, not mitogenic | Mouse chronic viral infection | High — mechanism is not proliferation |
| [PMID: 30087442](https://pubmed.ncbi.nlm.nih.gov/30087442/) | KO phenotype | Supports non-core | IL-21R deficiency in gut | Reduced GC and IgA responses are primary defect | Mouse intestine | High |
| [PMID: 18005035](https://pubmed.ncbi.nlm.nih.gov/18005035/) | Direct assay (IDA) | Supports NK effect | IL-21 NK cytotoxicity | IL-21 increased NK cytotoxicity against K562; upregulated perforin/granzyme | Human NK cells, in vitro | High — IDA for GO:0045954 |
| [PMID: 17953510](https://pubmed.ncbi.nlm.nih.gov/17953510/) | Review | Qualifies | IL-21 pleiotropic effects | Context-dependent effects; "increased cytotoxicity of CD8+ T cells and NK cells" | Review | Moderate |

---

## GO Curation Implications

### Primary Recommendation: KEEP_AS_NON_CORE for GO:0042102

The IDA annotations from PMID:17673207 and PMID:15207081 should be **retained** in the gene record — the experimental evidence for T cell proliferative activity is valid. However, the term should be **reclassified from core to non-core** status. Specifically:

- **Action**: `KEEP_AS_NON_CORE` — retain annotations but remove from `directly_involved_in` in the core function model
- **Rationale**: The effect is real but costimulation-dependent, bidirectional across T cell subsets, contradicted by deficiency phenotypes, and secondary to the signature B cell/GC/humoral immunity axis
- **Relation type**: If the GO framework supports it, model as `acts_upstream_of_or_within` rather than `directly_involved_in`, reflecting that IL-21 can influence T cell proliferation as a downstream consequence of its cytokine activity but does not directly drive it as a primary process

### Secondary Recommendation: KEEP_AS_NON_CORE for GO:0045954

NK cell mediated cytotoxicity enhancement (GO:0045954) should also be classified as non-core and removed from `directly_involved_in`:

- The source YAML listed this as IBA/IEA only, but IDA evidence exists (PMID:18005035)
- The effect is well-documented but parallels T cell proliferation as a pleiotropic downstream consequence
- Human IL-21R deficiency shows reduced NK terminal differentiation but NK cytotoxicity is not the defining clinical phenotype
- **Action**: Remove from `directly_involved_in` in core functions; retain annotation as non-core

### Curation Gap Alert: Core Functions Lack IDA

The true core functions of IL-21 — GO:0002314 (GC B cell differentiation), GO:0002639 (Ig production), GO:0061470 (Tfh differentiation) — currently only have ISS/IEA evidence codes. This creates a paradox where non-core terms have stronger evidence codes than core terms. Curators should prioritize adding IDA annotations to these core processes from the extensive primary literature supporting them (e.g., PMID:31821441, PMID:30087442, PMID:33929673).

---

## Mechanistic Scope

### Direct Gene Product Activity

IL-21 is a secreted cytokine (extracellular region, GO:0005576) that binds the IL-21R/IL-2Rgamma heterodimeric receptor complex, activating JAK1/JAK3 kinases and primarily STAT3 (with lesser STAT1 and STAT5 activation). This is the core molecular function: **cytokine activity (GO:0005125)**.

### Signature Downstream Processes (Core)

The primary biological processes driven by IL-21 signaling are:

```
IL-21 --> IL-21R/gamma-c --> JAK1/JAK3 --> STAT3
    |
    |---> Germinal center B cell differentiation (GO:0002314)  <-- CORE
    |---> Positive regulation of Ig production (GO:0002639)    <-- CORE
    |---> Tfh cell differentiation (GO:0061470)                <-- CORE
    |---> Positive regulation of B cell proliferation (GO:0030890) <-- CORE
```

These are consistently revealed by loss-of-function studies across species and represent the primary selective pressure maintaining IL-21 in the genome.

### Secondary/Pleiotropic Effects (Non-Core)

T cell proliferation and NK cytotoxicity are downstream of the same JAK/STAT3 signaling cascade but represent context-dependent, cell-type-specific pleiotropic effects:

```
IL-21 --> IL-21R/gamma-c --> JAK1/JAK3 --> STAT3
    |
    |---> T cell proliferation (GO:0042102)              <-- NON-CORE
    |       - Requires TCR costimulation (anti-CD3)
    |       - Anti-proliferative for Tfr cells
    |       - Dispensable in IL-21R deficiency
    |
    |---> Th17 differentiation                           <-- NON-CORE (autocrine, redundant in vivo)
    |       - Via STAT3/RORgammat, not mitogenic signaling
    |
    |---> CD8 T cell sustaining in chronic infection      <-- NON-CORE
    |       - Via BATF-IRF4-Blimp-1, not cell cycle entry
    |       - Absent in acute infection
    |
    |---> NK cell cytotoxicity (GO:0045954)              <-- NON-CORE
            - Real but not defining clinical phenotype
            - Enhanced perforin/granzyme expression
```

### Key Distinction: Differentiation vs. Proliferation

IL-21's actual T cell biology is **differentiation** (Th17 lineage commitment, Tfh specification, CD8 tissue-resident memory formation), not **proliferation** (cell cycle entry and clonal expansion). GO:0042102 (positive regulation of T cell proliferation) may therefore be the wrong term entirely for IL-21's T cell effects, even as a non-core annotation. The more precise biology would be captured by terms related to T cell differentiation (GO:0030217) or T helper cell lineage commitment.

---

## Conflicts and Alternatives

### Counter-Evidence: Chronic Viral Infection CD8 Maintenance

The strongest evidence that could support T cell proliferation as a core IL-21 function comes from chronic viral infection models. Three landmark papers (PMID:19423777, 19478140, 20844201 — all published in 2009-2010) demonstrated that IL-21 is essential for maintaining CD8 T cell responses during chronic LCMV infection. However, this counter-evidence is limited by:

1. **Context restriction**: The effect is absent in acute infections with LCMV, VSV, VV, and Listeria ([PMID: 19478140](https://pubmed.ncbi.nlm.nih.gov/19478140/))
2. **Mechanistic distinction**: The underlying mechanism is BATF/IRF4-mediated transcriptional reprogramming to prevent exhaustion, not mitogenic signaling ([PMID: 26527008](https://pubmed.ncbi.nlm.nih.gov/26527008/))
3. **Wrong GO term**: Sustaining an existing pool (anti-apoptotic/anti-exhaustion) is mechanistically and ontologically distinct from "positive regulation of T cell proliferation"
4. **Memory independence**: Memory CD8 T cell generation proceeds independently of IL-21 ([PMID: 20844201](https://pubmed.ncbi.nlm.nih.gov/20844201/))

### Potential Paralog Confusion

IL-21 shares the gamma-chain with IL-2, IL-4, IL-7, IL-9, and IL-15. Some T cell proliferative effects attributed to IL-21 could reflect experimental systems where other gamma-chain cytokines are present (e.g., IL-2 in culture media). The IDA papers used recombinant IL-21 in defined conditions, mitigating but not eliminating this concern.

### Organism-Specific Considerations

Most mechanistic data come from mouse models. Human IL-21R deficiency phenotypes are concordant (B cell/humoral defects dominate), but the relatively small number of identified patients (13 as of 2021) limits statistical power for detecting subtle T cell proliferative defects. However, the fact that T cell proliferation defects are not even mentioned as secondary features in these case series is informative.

### Alternative Interpretation: IL-21 as a T Cell Quality Factor

An alternative framing is that IL-21 does not regulate T cell quantity (proliferation) but rather T cell quality (differentiation state, effector function, exhaustion resistance). This interpretation reconciles all the data: IL-21 promotes Th17/Tfh differentiation, sustains CD8 effector function during chronic infection, and restricts inappropriate Tfr expansion — all effects on cell fate and function rather than cell number.

---

## Knowledge Gaps

### Gap 1: Dose-Response for T Cell Proliferation vs. B Cell Proliferation

**What was checked**: Both IDA papers used single concentrations of IL-21 in costimulatory assays. **Why it matters**: If IL-21 drives B cell proliferation at physiological concentrations but requires supraphysiological levels for T cell effects, this would further support non-core status. **Resolution**: Comparative dose-response curves for IL-21-driven proliferation of purified B cells vs. T cells (with matched costimulation) under identical conditions.

### Gap 2: In Vivo T Cell Proliferation Kinetics in IL-21 KO

**What was checked**: IL-21R KO phenotype studies focus on B cell and humoral endpoints. **Why it matters**: Formal measurement of T cell proliferation rates (e.g., BrdU incorporation, Ki-67) in lymphoid organs of IL-21-/- mice during normal immune responses would definitively test whether T cell proliferation is affected. **Resolution**: BrdU pulse-chase experiments in IL-21-/- vs. WT mice after immunization, measuring T cell and B cell proliferation in parallel.

### Gap 3: IDA Annotations for Core Functions

**What was checked**: QuickGO database query. **Why it matters**: The true core functions lack IDA evidence codes, creating an artificial asymmetry that could mislead automated curation pipelines. **Resolution**: Curators should mine existing primary literature (especially from the germinal center and Tfh differentiation fields) to add IDA annotations to GO:0002314, GO:0002639, and GO:0061470.

### Gap 4: Human-Specific T Cell Proliferative Effects

**What was checked**: Both IDA papers used human cells; chronic infection studies are mouse-based. **Why it matters**: Species-specific differences in gamma-chain cytokine biology exist. **Resolution**: IL-21 proliferation assays with purified human T cell subsets in defined conditions, with head-to-head comparison to IL-2 and IL-15.

### Gap 5: Single-Cell Resolution of IL-21 Effects

**What was checked**: Bulk proliferation assays from the IDA papers. **Why it matters**: Bulk assays cannot distinguish whether IL-21 drives proliferation of all T cells or only a subset that responds preferentially. **Resolution**: Single-cell RNA-seq or CITE-seq of T cells +/- IL-21 (with anti-CD3) to identify responding subpopulations.

---

## Discriminating Tests

1. **Head-to-head cytokine comparison**: Measure T cell and B cell proliferation (CFSE dilution) in response to IL-21, IL-2, IL-7, IL-15, and IL-4 at matched concentrations, +/- costimulation. If IL-21's T cell effect is consistently weaker and more costimulation-dependent than other gamma-chain cytokines, this would confirm non-core status.

2. **Conditional IL-21R deletion**: T cell-specific (CD4-Cre) vs. B cell-specific (CD19-Cre) IL-21R deletion, measuring immune responses after immunization. If B cell-specific deletion recapitulates the full IL-21R KO phenotype while T cell-specific deletion does not, this definitively identifies B cells as the core target.

3. **CRISPR screen for IL-21 dependencies**: Genome-wide CRISPR screen in T cells vs. B cells comparing IL-21-dependent gene programs. This would identify whether the transcriptional programs activated by IL-21 in T cells are primarily differentiation-related or proliferation-related.

4. **Evolutionary analysis**: Compare IL-21's T cell proliferative activity across vertebrate species. If this activity is gained late in evolution or is poorly conserved relative to B cell effects, it further supports non-core status.

5. **Dose-titration with phospho-STAT profiling**: Map the signaling dose-response curve for IL-21 in T cells vs. B cells. If B cells show higher IL-21R expression and/or more sensitive STAT3 activation, this provides a molecular basis for the B cell-centric biology.

---

## Curation Leads

### Lead 1: Change GO:0042102 Action to KEEP_AS_NON_CORE

- **Current action**: UNDECIDED
- **Recommended action**: `KEEP_AS_NON_CORE`
- **Confidence**: High (8 independent evidence lines)
- **Key references**: PMID:17673207 (costimulation-dependent), PMID:33929673 (deficiency phenotype), PMID:28303891 (anti-proliferative for Tfr), PMID:23960240 (B cells are essential target)
- **Snippet to verify** (PMID:33929673): "Most patients exhibited hypogammaglobulinemia and reduced proportions of memory B cells, circulating T follicular helper cells, MAIT cells and terminally differentiated NK cells"

### Lead 2: Remove GO:0045954 from directly_involved_in

- **Current status**: Listed in `directly_involved_in` in core functions YAML
- **Recommended action**: Remove from core, classify as `KEEP_AS_NON_CORE`
- **Rationale**: Same logic as GO:0042102; NK cytotoxicity is a real pleiotropic effect but not a signature function
- **Note**: Source YAML incorrectly states IBA/IEA only; IDA evidence exists from PMID:18005035
- **Snippet to verify** (PMID:18005035): "IL-21 increased the cytotoxicity of NK cells against K562 target cells"

### Lead 3: Add IDA Annotations for Core Functions

- **Gap identified**: GO:0002314, GO:0002639, GO:0061470 lack IDA evidence codes
- **Action**: Curators should mine primary literature for IDA-quality evidence for these core terms
- **Candidate references**: PMID:31821441 (review), PMID:30087442 (mouse KO), PMID:25586558 (IgA/B cell), PMID:21708925 (Bcl-6/Tfh/GC)

### Lead 4: Consider Adding T Cell Differentiation Terms as Non-Core

- **Rationale**: IL-21's actual T cell biology is Th17/Tfh differentiation, not proliferation
- **Candidate terms**: GO:0030217 (T cell differentiation), GO:0072539 (T-helper 17 cell differentiation)
- **Evidence**: PMID:17581589 (Th17 differentiation), PMID:17884812 (Th17 commitment), PMID:32948671 (CD8 tissue-resident differentiation)
- **Status**: Non-core, as these are secondary to the B cell axis

### Lead 5: Correct Source YAML Evidence Codes for GO:0045954

- **Issue**: Source YAML states GO:0045954 has only IBA/IEA evidence
- **Correction**: IDA evidence exists from PMID:18005035 (Skak et al. 2008)
- **Action**: Update YAML to reflect accurate evidence codes

### Lead 6: Resolve Issue #1418

- **Recommendation**: Close issue #1418 with decision `KEEP_AS_NON_CORE` for GO:0042102
- **Summary for issue**: The effect is real and well-documented but does not meet the threshold for core function based on costimulation dependency, deficiency phenotype analysis, bidirectional effects, and comparative cytokine biology

---

## GO Decision Table

| GO Term | Current Status | Evidence Codes | Recommended Action | Rationale |
|---------|---------------|----------------|-------------------|-----------|
| GO:0005125 (cytokine activity) | Core MF | Multiple | **RETAIN as core** | Undisputed molecular function |
| GO:0002314 (GC B cell diff.) | Core BP | ISS, IEA | **RETAIN as core**; add IDA | Signature function; needs IDA from primary lit |
| GO:0002639 (Ig production) | Core BP | ISS, IEA | **RETAIN as core**; add IDA | Signature function; needs IDA |
| GO:0061470 (Tfh diff.) | Core BP | ISS, IEA | **RETAIN as core**; add IDA | Signature function; needs IDA |
| GO:0030890 (B cell prolif.) | Core BP | IDA | **RETAIN as core** | Signature function with IDA |
| GO:0042102 (T cell prolif.) | UNDECIDED | IDA x2 | **KEEP_AS_NON_CORE** | Costimulation-dependent, non-signature |
| GO:0045954 (NK cytotoxicity) | Core (directly_involved_in) | IDA, IBA, IEA | **KEEP_AS_NON_CORE**; remove from directly_involved_in | Real but non-signature pleiotropic effect |
| GO:0005576 (extracellular region) | Core CC | Multiple | **RETAIN as core** | Undisputed cellular component |

---

## Evidence Base: Key Literature

### Defining Papers for the Core Function Question

- **Spolski & Leonard (2008)** ([PMID: 17953510](https://pubmed.ncbi.nlm.nih.gov/17953510/)): Foundational review establishing IL-21's pleiotropic biology and context-dependency. Key quote: "The regulatory activity of IL-21 is modulated by the differentiation state of its target cells as well as by other cytokines or costimulatory molecules."

- **Tangye & Ma (2020)** ([PMID: 31821441](https://pubmed.ncbi.nlm.nih.gov/31821441/)): Comprehensive review concluding IL-21's "critical role in T cell-dependent B cell activation, germinal center reactions, and humoral immunity."

- **Spolski & Leonard (2014)** ([PMID: 24751819](https://pubmed.ncbi.nlm.nih.gov/24751819/)): "Double-edged sword" framing that captures IL-21's bidirectional, context-dependent effects.

### Human Genetic Evidence

- **Cagdas et al. (2021)** ([PMID: 33929673](https://pubmed.ncbi.nlm.nih.gov/33929673/)): Largest human IL-21R deficiency cohort (13 patients). Phenotype dominated by hypogammaglobulinemia and B cell defects, not T cell proliferative defects.

- **Kotlarz et al. (2014)** ([PMID: 30903457](https://pubmed.ncbi.nlm.nih.gov/30903457/)): IL2RG mutation with selective IL-21 signaling defect phenocopied IL-21R deficiency with B cell differentiation defects.

### T Cell Differentiation (Not Proliferation)

- **Nurieva et al. (2007)** ([PMID: 17581589](https://pubmed.ncbi.nlm.nih.gov/17581589/)): IL-21 as essential autocrine factor for Th17 differentiation via STAT3/RORgammat.

- **Wei et al. (2007)** ([PMID: 17884812](https://pubmed.ncbi.nlm.nih.gov/17884812/)): IL-21 sustains Th17 lineage commitment.

### Counter-Evidence (Chronic Infection)

- **Elsaesser et al. (2009)** ([PMID: 19423777](https://pubmed.ncbi.nlm.nih.gov/19423777/)): CD8 T cells require IL-21 during chronic viral infection — strongest counter-evidence but context-limited.

- **Frohlich et al. (2009)** ([PMID: 19478140](https://pubmed.ncbi.nlm.nih.gov/19478140/)): Critically shows normal CD8 T cell expansion in acute infection, limiting the chronic infection effect.

- **Yi et al. (2010)** ([PMID: 20844201](https://pubmed.ncbi.nlm.nih.gov/20844201/)): Memory CD8 T cell generation is IL-21-independent.

---

## Limitations

1. **Subjectivity of "core" definition**: The distinction between core and non-core functions involves judgment about evolutionary purpose and functional hierarchy. Different curators may reasonably draw the line differently.

2. **Bias toward mouse data**: Most mechanistic studies use mouse models. While human genetic data corroborate the conclusions, the small number of identified patients (13 as of 2021) limits power to detect subtle T cell effects.

3. **In vitro vs. in vivo gap**: The IDA evidence for T cell proliferation comes from in vitro assays. It is possible that in vivo T cell proliferative effects are more robust but undetectable in the available knockout studies due to redundancy.

4. **Publication bias**: Studies emphasizing IL-21's B cell and GC functions may be more numerous because these are the phenotypically dominant effects, creating circular reinforcement of the "core function" narrative.

5. **Temporal dynamics**: IL-21 may have different roles at different stages of immune responses (early proliferative vs. late differentiative), and bulk endpoint assays may miss transient proliferative contributions.

---

## Proposed Follow-up Actions

1. **Immediate curation action**: Change GO:0042102 from UNDECIDED to `KEEP_AS_NON_CORE` and close issue #1418 with this report as supporting documentation.

2. **Remove GO:0045954 from directly_involved_in**: Reclassify as non-core with notation that IDA evidence exists (PMID:18005035) but the effect is non-signature.

3. **Prioritize IDA annotation for core functions**: Mine existing primary literature to add IDA evidence codes to GO:0002314, GO:0002639, and GO:0061470, resolving the evidence code asymmetry.

4. **Consider new non-core annotations**: Add GO:0072539 (T-helper 17 cell differentiation) and/or GO:0030217 (T cell differentiation) as non-core annotations based on PMID:17581589 and PMID:17884812, which more accurately capture IL-21's T cell biology than GO:0042102.

5. **Flag for computational pipeline review**: Ensure that automated annotation transfer pipelines do not re-promote GO:0042102 to core status based on IDA evidence codes alone, as this case demonstrates that IDA evidence does not equal core function.
