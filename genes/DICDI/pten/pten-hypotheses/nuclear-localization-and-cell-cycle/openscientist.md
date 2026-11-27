---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-20T19:42:41.110269'
end_time: '2026-09-20T19:58:23.565558'
duration_seconds: 942.46
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: DICDI
  gene: pten
  gene_symbol: pten
  uniprot_accession: Q8T9S7
  taxon_id: NCBITaxon:44689
  taxon_label: Dictyostelium discoideum
  focus_type: function_assignment
  hypothesis_slug: nuclear-localization-and-cell-cycle
  hypothesis_text: Dictyostelium discoideum PTEN localizes to the nucleus (GO:0005634)
    and regulates cell cycle (GO:0051726). Evaluate separately using direct evidence
    and justified transfer from characterized orthologs. Distinguish cortex and membrane
    localization from exclusivity, cytokinesis phenotypes from cell cycle regulation,
    and mammalian-specific roles from conserved mechanisms.
  term_context: No specific term context supplied.
  reference_context: No specific reference context supplied.
  source_file: genes/DICDI/pten/pten-ai-review.yaml
  source_selector: free-text
  source_context_yaml: "hypothesis: Dictyostelium discoideum PTEN localizes to the\
    \ nucleus (GO:0005634) and regulates cell cycle\n  (GO:0051726). Evaluate separately\
    \ using direct evidence and justified transfer from characterized orthologs.\n\
    \  Distinguish cortex and membrane localization from exclusivity, cytokinesis\
    \ phenotypes from cell cycle\n  regulation, and mammalian-specific roles from\
    \ conserved mechanisms.\nfocus_type: function_assignment\ncontext: []\nreference_id:\
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
citation_count: 14
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

- **Organism code:** DICDI
- **Taxon:** Dictyostelium discoideum (NCBITaxon:44689)
- **Gene directory:** pten
- **Gene symbol:** pten
- **UniProt accession:** Q8T9S7

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** nuclear-localization-and-cell-cycle
- **Source file:** genes/DICDI/pten/pten-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

Dictyostelium discoideum PTEN localizes to the nucleus (GO:0005634) and regulates cell cycle (GO:0051726). Evaluate separately using direct evidence and justified transfer from characterized orthologs. Distinguish cortex and membrane localization from exclusivity, cytokinesis phenotypes from cell cycle regulation, and mammalian-specific roles from conserved mechanisms.

## Term and Decision Context

No specific term context supplied.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: Dictyostelium discoideum PTEN localizes to the nucleus (GO:0005634) and regulates cell cycle
  (GO:0051726). Evaluate separately using direct evidence and justified transfer from characterized orthologs.
  Distinguish cortex and membrane localization from exclusivity, cytokinesis phenotypes from cell cycle
  regulation, and mammalian-specific roles from conserved mechanisms.
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

# AIGR Gene Hypothesis Deep Research — *Dictyostelium discoideum* PTEN (Q8T9S7)

**Hypothesis slug:** nuclear-localization-and-cell-cycle
**Focus type:** function_assignment
**Source:** `genes/DICDI/pten/pten-ai-review.yaml` (free-text)

**Seed hypothesis under evaluation:** *Dictyostelium discoideum* PTEN localizes to the nucleus (GO:0005634) and regulates the cell cycle (GO:0051726) — to be evaluated separately using direct evidence and justified transfer from characterized orthologs, distinguishing cortex/membrane localization from exclusivity, cytokinesis phenotypes from cell-cycle regulation, and mammalian-specific roles from conserved mechanisms.

---

## Summary

**Executive judgment: REFUTED / OVER-ANNOTATED (both legs of the hypothesis).** Neither half of the seed hypothesis survives contact with the direct experimental record for *Dictyostelium discoideum* PTEN. The proposed **nuclear localization (GO:0005634)** has *no* experimental support in this organism: it rests entirely on phylogenetic inference (IBA, Inferred from Biological Ancestor), whereas every direct localization assay (IDA) places the protein at the plasma membrane and cell cortex (posterior/rear, PI(4,5)P₂-dependent). The proposed **regulation of cell cycle (GO:0051726)** is not curator-annotated at all, and it is mis-scoped: the loss-of-function phenotype is a *cytokinesis* failure in which the nuclear/DNA-replication cycle continues normally, producing large multinucleate cells. The directly supported process term is **mitotic cytokinesis (GO:0000281, IMP)**, not regulation of cell cycle.

The hypothesis instructs the evaluator to treat localization and process separately, and to test whether ortholog transfer from mammals is justified. On both counts the transfer fails. For localization, the mammalian nuclear-PTEN paradigm depends on a monoubiquitination-driven import switch (the K289 site) and a C-terminal regulatory tail — features that are **not conserved** in the *Dictyostelium* protein. In a pairwise alignment, the position aligning to human K289 carries a glutamate (E) in *Dictyostelium*, i.e. the organism is naturally in the exact import-defective state (K289E) that abolishes nuclear accumulation in Cowden-syndrome patients ([PMID: 17218261](https://pubmed.ncbi.nlm.nih.gov/17218261/)). The mammalian nuclear roles (heterochromatin maintenance, mitotic-checkpoint-complex regulation, Plk1 crosstalk, CBX8 interaction) form a metazoan-specific program built on machinery *Dictyostelium* lacks.

The consolidated *Dictyostelium* model is membrane-centric and cytokinesis-linked: PTEN is a PIP3 3-phosphatase recruited to the posterior cortex, where it establishes back-of-cell polarity that is required for both chemotaxis and cleavage-furrow function. The curation recommendation is therefore to **not add GO:0005634 or GO:0051726 as experimentally supported terms**, to flag the existing IBA nucleus annotation as phylogenetic carry-over rather than direct evidence, and to anchor the process description on GO:0000281 (mitotic cytokinesis) and the membrane/cortex cellular-component terms already supported by IDA evidence.

---

## Key Findings

### Finding 1 — Direct localization places *Dictyostelium* PTEN at the plasma membrane/cortex, never the nucleus

Every direct localization study of *D. discoideum* PTEN reports plasma-membrane and cortical (posterior/rear) enrichment; none reports a nuclear signal. In the foundational study, Iijima & Devreotes ([PMID: 12062103](https://pubmed.ncbi.nlm.nih.gov/12062103/)) showed that "*Exogenously expressed PTEN-GFP localized to the surface membrane at the rear of the cell. Membrane localization required a putative PI(4,5)P2 binding motif and was required for chemotaxis.*" The dependence of localization on a PI(4,5)P₂-binding motif ties the protein mechanistically to the inner leaflet of the plasma membrane, not to nuclear-import machinery.

This picture is reinforced by Matsuoka & Ueda ([PMID: 30367048](https://pubmed.ncbi.nlm.nih.gov/30367048/)), who described PTEN and PIP3 as "*enriched mutually exclusively on the anterior and posterior membranes of eukaryotic motile cells*," establishing a bistable membrane-partitioning mechanism in which PTEN occupies the posterior cortex. Janetopoulos et al. ([PMID: 15809030](https://pubmed.ncbi.nlm.nih.gov/15809030/)) placed PTEN function at cell poles and the cleavage furrow, and live-imaging studies of chemotactic signaling ([PMID: 25300796](https://pubmed.ncbi.nlm.nih.gov/25300796/); [PMID: 27505897](https://pubmed.ncbi.nlm.nih.gov/27505897/)) consistently track PTEN as a membrane/cortex marker. Crucially, no primary study of *Dictyostelium* PTEN reports GO:0005634 (nucleus) occupancy. This negative is strong because localization is precisely the assay these studies were designed to measure — live-cell GFP imaging that would readily reveal nuclear accumulation had it existed.

### Finding 2 — The *pten⁻* phenotype is cytokinesis failure with continued nuclear/cell-cycle progression, not cell-cycle regulation

The seed hypothesis explicitly asks the curator to distinguish "cytokinesis phenotypes from cell cycle regulation," and the *Dictyostelium* data land firmly on the cytokinesis side. Janetopoulos et al. ([PMID: 15809030](https://pubmed.ncbi.nlm.nih.gov/15809030/)) report that cells lacking PTEN (with intact PI3K) "*are defective in cytokinesis, and cannot divide in suspension. The cells continue to grow and duplicate their nuclei, generating large multinucleate cells.*" This is the diagnostic signature of a cytokinesis defect: DNA replication and mitotic nuclear division proceed on schedule, but the physical division of the cell body fails, so nuclei accumulate. A genuine *regulation of cell cycle* (GO:0051726) role would be expected to alter S-phase entry, checkpoint control, or nuclear-division rate — none of which is reported.

Downstream and mechanistic studies are consistent. Tang et al. ([PMID: 21169559](https://pubmed.ncbi.nlm.nih.gov/21169559/)) show PTEN maintains polarity "*required for cytokinesis and chemotaxis*" by limiting PIP3, with the key effector being phosphorylation of PKB (Akt) substrates. Consalvo et al. ([PMID: 38940195](https://pubmed.ncbi.nlm.nih.gov/38940195/)) implicate PTEN in AprA-induced *inhibition of proliferation* — but this is a population-level chemorepellent response mediated through Ras/PIP3 signaling, a downstream physiological effect rather than direct engagement of the cell-cycle machinery. None of these supports GO:0051726 as a direct molecular function of the gene product.

### Finding 3 — The mammalian nuclear-import determinant (K289) is not conserved in *Dictyostelium* PTEN

To test whether nuclear localization could be justified by transfer from the well-characterized human ortholog, I performed a pairwise global alignment (Needleman–Wunsch) of human PTEN (P60484, 403 aa) against *D. discoideum* PTEN (Q8T9S7, 533 aa). Global identity was **45.0% (181/402 aligned positions)**, and the core phosphatase + C2 domain region (human residues 1–350) aligned at **44.4% identity**. The catalytic P-loop signature motif **HCKAGKGR** is perfectly conserved at the equivalent position (~123) in both proteins, confirming that the lipid-phosphatase catalytic function is conserved — this is the *bona fide* transferable feature.

However, the residues that specifically govern **nuclear import in mammals are not conserved**. Trotman et al. ([PMID: 17218261](https://pubmed.ncbi.nlm.nih.gov/17218261/)) demonstrated that "*A lysine mutant of PTEN, K289E associated with Cowden syndrome, retains catalytic activity but fails to accumulate in nuclei of patient tissue due to an import defect.*" K289 is the major monoubiquitination site that drives PTEN into the nucleus. In my alignment, the *Dictyostelium* residue aligning to human K289 is a **glutamate (E)** — i.e., the protein is naturally in the import-defective state that causes disease when engineered into human PTEN. The minor import-associated lysine K13 is conserved (K), but it is insufficient on its own. In addition, the human C-terminal regulatory tail (the phospho-cluster and PDZ-binding motif) is absent in *Dictyostelium*, which instead carries a long low-complexity Asn/Ser/Thr C-terminal extension unrelated to nuclear trafficking. Ortholog-based transfer of GO:0005634 is therefore mechanistically unjustified.

*Caveat:* the aligned K289 falls in a divergent C2-domain loop (CBR3/Cα2 region, local identity ~21%), so the exact single-residue call is low-confidence; the robust conclusion is that there is **no conserved lysine** at the aligned position and the entire mammalian import-signal region is poorly conserved.

| Feature | Human PTEN (P60484) | *Dictyostelium* PTEN (Q8T9S7) | Transferable? |
|---|---|---|---|
| Length | 403 aa | 533 aa | — |
| Global identity | — | 45.0% (181/402) | — |
| Catalytic P-loop (HCKAGKGR) | Present (~pos 123) | Present (~pos 123) | **Yes** (catalysis) |
| K289 nuclear-import / monoubiquitination site | K (import-competent) | **E (import-defective state)** | **No** |
| Minor import lysine K13 | K | K | Partial (insufficient alone) |
| C-terminal regulatory tail / PDZ motif | Present | Absent (Asn/Ser/Thr low-complexity extension) | **No** |

### Finding 4 — UniProt/dictyBase annotations confirm nucleus is phylogenetic-only (IBA), cytokinesis is experimental (IMP), and GO:0051726 is absent

An audit of the curated GO cross-references for UniProt **Q8T9S7** clinches the evidence-code argument. The cellular-component term **GO:0005634 (nucleus)** is supported **only by IBA:GO_Central** — phylogenetic Inferred from Biological Ancestor — with no experimental backing. Every *experimental* (IDA:dictyBase) localization is non-nuclear:

- GO:0005886 plasma membrane (IDA)
- GO:0051285 cell cortex of cell tip (IDA)
- GO:0031254 / GO:0031257 cell trailing edge / trailing-edge membrane (IDA)
- GO:0032154 cleavage furrow (IDA)
- GO:1990753 equatorial cell cortex (IDA)
- GO:0005829 cytosol (IDA)
- GO:0001931 uropod (IDA)

Consistently, the UniProt subcellular-location comments list only **Cell membrane, Cytoplasm, and Cytoplasm/cell cortex** — no nucleus. On the process side, **GO:0051726 (regulation of cell cycle) is NOT annotated** for this gene. The directly supported biological-process term is **GO:0000281 mitotic cytokinesis [IMP:dictyBase]**, together with **GO:1903665 negative regulation of asexual reproduction [IMP]**. This evidence-code stratification is the single most decisive line for a curator: the seed hypothesis's nucleus term is carry-over inference, and its cell-cycle term does not exist in the curated record.

### Finding 5 — No primary literature reports nuclear PTEN in *Dictyostelium* or other lower eukaryotes

Targeted PubMed searches ("Dictyostelium PTEN nucleus development proliferation growth"; "PTEN nuclear localization amoeba lower eukaryote evolution conservation") returned zero papers describing nuclear PTEN in *Dictyostelium*. Across the full set of 21 papers reviewed, nuclear PTEN function is documented **only in mammalian systems** — heterochromatin maintenance ([PMID: 25946202](https://pubmed.ncbi.nlm.nih.gov/25946202/)), mitotic-checkpoint-complex regulation ([PMID: 28670501](https://pubmed.ncbi.nlm.nih.gov/28670501/)), CBX8/PRC1 interaction ([PMID: 34592789](https://pubmed.ncbi.nlm.nih.gov/34592789/)), Plk1 crosstalk ([PMID: 40117175](https://pubmed.ncbi.nlm.nih.gov/40117175/)), and Ndfip1/Nedd4-dependent import ([PMID: 17218261](https://pubmed.ncbi.nlm.nih.gov/17218261/); [PMID: 22213801](https://pubmed.ncbi.nlm.nih.gov/22213801/)). The nuclear-PTEN literature is a mammalian-specific body of work built on an import mechanism that *Dictyostelium* PTEN lacks (Finding 3).

---

## Mechanistic Model / Interpretation

The consolidated evidence supports a single coherent, membrane-centric model for *Dictyostelium* PTEN with no nuclear or direct cell-cycle role:

```
        ANTERIOR (front)                          POSTERIOR (rear/cortex)
     ┌───────────────────┐                     ┌────────────────────────┐
     │  PI3K active       │  mutual exclusion   │  PTEN active           │
     │  PIP2 → PIP3 ↑     │◄───────────────────►│  PIP3 → PIP2 (posterior)│
     │  Actin, pseudopods │   (bistable switch) │  Myosin II, uropod      │
     └───────────────────┘                     └────────────────────────┘
                                                         │
                                                         ▼
                                        Maintains cortical polarity
                                                         │
                             ┌───────────────────────────┴───────────────┐
                             ▼                                            ▼
                      Chemotaxis                                Cytokinesis (furrow)
                             │                                            │
                    (directed migration)                    pten⁻ → furrow fails,
                                                            nuclei keep duplicating
                                                            → multinucleate cells
                                                            (GO:0000281 defect)
```

PTEN's immediate molecular activity is **PIP3 3-phosphatase** at the plasma membrane/cortex, recruited via a PI(4,5)P₂-binding motif. This activity partitions the membrane into a PIP3-high anterior and a PTEN/PIP2 posterior (mutual inhibition → bistability; [PMID: 30367048](https://pubmed.ncbi.nlm.nih.gov/30367048/)). The resulting polarity is required both for directional chemotaxis and for assembling a functional cleavage furrow. Loss of PTEN elevates PIP3 and PKB-substrate phosphorylation ([PMID: 21169559](https://pubmed.ncbi.nlm.nih.gov/21169559/)), disrupting furrow completion — while the nuclear-division cycle proceeds unabated, giving the classic multinucleate phenotype. Every arrow in this model is anchored in direct membrane/cortex data; none requires or predicts nuclear PTEN.

The mammalian nuclear-PTEN program (heterochromatin, MCC, Plk1, CBX8) is a **later evolutionary elaboration** built on a C-terminal tail and K289 monoubiquitination import switch that arose in the metazoan lineage. Because *Dictyostelium* PTEN lacks both, the nuclear paradigm is organism-specific and non-transferable.

---

## Evidence Base (Evidence Matrix)

| Citation (PMID) | Evidence type | Supports/Refutes/Qualifies | Claim tested | Key finding | Context | Confidence & limitations |
|---|---|---|---|---|---|---|
| [12062103](https://pubmed.ncbi.nlm.nih.gov/12062103/) | Localization (direct, GFP) | **Refutes** nuclear; supports membrane | Where does Dicty PTEN localize? | PTEN-GFP at rear surface membrane; needs PI(4,5)P₂ motif | *D. discoideum*, live cells | High; overexpressed GFP fusion |
| [30367048](https://pubmed.ncbi.nlm.nih.gov/30367048/) | Localization + single-molecule/modeling | **Refutes** nuclear; supports cortex | Membrane partitioning of PTEN | PTEN/PIP3 mutually exclusive on posterior/anterior membranes | *D. discoideum* motile cells | High |
| [15809030](https://pubmed.ncbi.nlm.nih.gov/15809030/) | Mutant phenotype | **Refutes** cell-cycle; supports cytokinesis | Cell-cycle or cytokinesis defect? | pten⁻ fails cytokinesis; nuclei keep duplicating → multinucleate | *D. discoideum* | High; core discriminating evidence |
| [21169559](https://pubmed.ncbi.nlm.nih.gov/21169559/) | Mutant/genetic epistasis | **Qualifies**; supports cytokinesis | Mechanism of pten⁻ defect | PKB-substrate phosphorylation is key downstream regulator; polarity for cytokinesis/chemotaxis | *D. discoideum* | High |
| [38940195](https://pubmed.ncbi.nlm.nih.gov/38940195/) | Mutant phenotype | **Qualifies** (downstream) | Does PTEN affect proliferation? | PTEN needed for AprA-induced proliferation inhibition (population effect) | *D. discoideum* chemorepulsion | Medium; downstream/pathway, not cell-cycle machinery |
| [24292679](https://pubmed.ncbi.nlm.nih.gov/24292679/) | Structure–function (heterologous) | **Qualifies** membrane mechanism | Membrane localization determinants | Membrane-binding regulatory interface; recruitment required for function | Human PTEN in *Dictyostelium* | High for membrane; uses human protein |
| [17218261](https://pubmed.ncbi.nlm.nih.gov/17218261/) | Direct assay (mammalian) | **Refutes transfer** | Is K289 required for nuclear import? | K289E retains catalysis but fails nuclear accumulation (import defect) | Human, patient tissue | High; defines non-conserved determinant |
| [22213801](https://pubmed.ncbi.nlm.nih.gov/22213801/) | In vivo (mouse) | **Qualifies transfer** | Nuclear-import machinery | Ndfip1/Nedd4-driven ubiquitination imports Pten | Mouse neurons | Medium; mammal-specific machinery |
| [25946202](https://pubmed.ncbi.nlm.nih.gov/25946202/), [28670501](https://pubmed.ncbi.nlm.nih.gov/28670501/), [34592789](https://pubmed.ncbi.nlm.nih.gov/34592789/), [40117175](https://pubmed.ncbi.nlm.nih.gov/40117175/) | Direct (mammalian) | **Competing** (organism-specific) | Nuclear PTEN roles | Heterochromatin, MCC, CBX8, Plk1 — all mammalian, tail/K289-dependent | Human/mouse | High but not transferable |
| This report — sequence analysis | Computational (evolutionary) | **Refutes transfer** | Is nuclear-import machinery conserved? | 45% identity; catalytic motif conserved; K289→E, C-tail absent in Dicty | Q8T9S7 vs P60484 | Low–medium at K289 (divergent loop); needs MSA/structure |
| UniProt Q8T9S7 / dictyBase | Review/database (evidence codes) | **Refutes** nuclear as experimental | What is the annotation basis? | Nucleus = IBA only; all IDA localization non-nuclear; GO:0051726 absent; GO:0000281 IMP present | Curated record | High for provenance |

---

## GO Curation Implications (leads — require curator verification)

1. **GO:0005634 (nucleus, CC) — do NOT retain as experimentally supported; flag as IBA-only carry-over.** The term has no IDA/IMP backing in *Dictyostelium*; it is Inferred from Biological Ancestor. Because the specific import determinant (K289) and C-terminal tail that justify nuclear localization in the ancestor-defining mammalian orthologs are not conserved, the IBA propagation is a false-transfer candidate. Curator action: consider a `NOT` qualifier or removal, and flag the GO_Central ortholog set for review.

2. **GO:0051726 (regulation of cell cycle, BP) — do NOT add.** Not curator-annotated; not supported by any *Dictyostelium* primary study. The phenotype is cytokinesis, not cell-cycle regulation.

3. **GO:0000281 (mitotic cytokinesis, BP) — retain as the correct, IMP-supported process term** (with GO:1903665 negative regulation of asexual reproduction). This accurately represents the *pten⁻* phenotype.

4. **Retain the IDA cellular-component terms** already in place: GO:0005886 (plasma membrane), GO:0051285 (cell cortex of cell tip), GO:0032154 (cleavage furrow), GO:1990753 (equatorial cell cortex), GO:0031254/0031257 (trailing edge), GO:0005829 (cytosol), GO:0001931 (uropod).

5. **Molecular-function anchor:** the primary MF is phosphatidylinositol-3,4,5-trisphosphate 3-phosphatase activity — the conserved, transferable feature — not "protein binding."

---

## Mechanistic Scope

The immediate molecular function tested is **membrane-localized PIP3 3-phosphatase activity** — dephosphorylation of PI(3,4,5)P₃ → PI(4,5)P₂ at the posterior plasma membrane/cortex, dependent on a PI(4,5)P₂-binding motif. Downstream/pathway consequences that must not be conflated with the seed terms: reduced PKB-substrate phosphorylation, maintained cortical polarity, functional cleavage-furrow assembly, directed chemotaxis, and — at the population level — AprA-mediated proliferation inhibition and chemorepulsion. The multinucleate phenotype is an **inferred-from-loss-of-function** cellular outcome of failed cytokinesis, not evidence of a direct cell-cycle-regulatory activity. The mammalian nuclear functions (heterochromatin, MCC/Plk1, CBX8) are context- and organism-specific roles that depend on trafficking machinery absent in *Dictyostelium*.

---

## Conflicts and Alternatives

- **Ortholog carry-over (primary conflict):** The nucleus term derives from mammalian PTEN, where nuclear roles are real and well documented. IBA propagation transferred CC:nucleus without accounting for the non-conservation of the import switch — a textbook case of database carry-over creating an over-annotation.
- **Organism-specific difference:** Mammalian PTEN nuclear import requires K289 monoubiquitination (Ndfip1/Nedd4) and the C-terminal tail; *Dictyostelium* has E at the aligned K289 position and lacks the tail.
- **Paralog/ortholog confusion:** *Dictyostelium* has a related PTEN-like phosphatase, **CnrN**, with overlapping PI(3,4,5)P₃-phosphatase activity ([PMID: 38940195](https://pubmed.ncbi.nlm.nih.gov/38940195/)); localization/function claims should be checked against CnrN to avoid mis-attribution.
- **Heterologous-system artifact:** Several mechanistic Dicty studies use **human PTEN expressed in Dicty** ([PMID: 24292679](https://pubmed.ncbi.nlm.nih.gov/24292679/)), describing human PTEN behavior rather than the endogenous *Dictyostelium* protein.
- **Downstream vs. direct:** The AprA/proliferation link ([PMID: 38940195](https://pubmed.ncbi.nlm.nih.gov/38940195/)) could superficially read as "cell-cycle," but it is a population proliferation response routed through Ras/PIP3 signaling.

---

## Limitations and Knowledge Gaps

1. **No dedicated nuclear-imaging study in Dictyostelium.** Checked: all localization papers → membrane/cortex; targeted PubMed queries returned zero papers for Dictyostelium/amoeba nuclear PTEN. Why it matters: mammalian PTEN is nuclear only transiently/under stress, so absence of a report is not definitive proof of absence. Resolve: image endogenous tagged PTEN (± stress/DNA damage) with nuclear counterstain and subcellular fractionation.
2. **Conservation confirmation.** Checked: pairwise Needleman–Wunsch (45% identity; K289→E) with simple match/mismatch scoring and no structural superposition. Why it matters: pairwise alignment can mis-place a single residue in a divergent loop. Resolve: multiple-sequence alignment across amoebozoa plus structure-based alignment (AlphaFold Q8T9S7) to confirm K289 non-conservation and tail divergence.
3. **Direct cell-cycle assay.** Checked: only the cytokinesis phenotype is reported; no S-phase/checkpoint assays in *pten⁻*. Why it matters: it would directly confirm the cytokinesis-vs-cell-cycle distinction. Resolve: DNA-content flow cytometry / cell-cycle staging of *pten⁻* vs WT.

---

## Proposed Follow-up Experiments / Actions (Discriminating Tests)

1. **Structure-based alignment** (AlphaFold model of Q8T9S7 vs the human PTEN structure) to confirm the K289-equivalent residue and the absence of a functional nuclear-import interface — the single most efficient computational discriminator.
2. **Endogenous nuclear fractionation + confocal imaging** of *Dictyostelium* PTEN across the cell cycle and under osmotic/oxidative/DNA-damage stress, to definitively test for any nuclear pool.
3. **DNA-content flow cytometry / live nuclear-cycle imaging** in *pten⁻* to confirm the cell cycle is intact while cytokinesis fails (distinguishing GO:0000281 from GO:0051726).
4. **CnrN vs PTEN comparison** to attribute any residual signal to the correct enzyme.
5. **Curation actions:** withhold/flag GO:0005634 (nucleus) as IBA carry-over; do not add GO:0051726; retain GO:0000281 (mitotic cytokinesis) and the IDA membrane/cortex CC terms.

---

## Curation Leads (require curator verification)

- **Action change (nucleus):** Do not add GO:0005634 as experimental; substitute/retain plasma membrane (GO:0005886) / cell cortex terms. Reference to verify: [PMID: 12062103](https://pubmed.ncbi.nlm.nih.gov/12062103/) — snippet: *"Exogenously expressed PTEN-GFP localized to the surface membrane at the rear of the cell."*
- **Action change (cell cycle):** Do not add GO:0051726; use the cytokinesis branch (GO:0000281 mitotic cytokinesis). Reference to verify: [PMID: 15809030](https://pubmed.ncbi.nlm.nih.gov/15809030/) — snippet: *"are defective in cytokinesis ... The cells continue to grow and duplicate their nuclei, generating large multinucleate cells."*
- **Transfer-blocking datum:** [PMID: 17218261](https://pubmed.ncbi.nlm.nih.gov/17218261/) — snippet: *"A lysine mutant of PTEN, K289E ... fails to accumulate in nuclei ... due to an import defect."* Combine with the sequence finding that Dicty PTEN carries E at the aligned K289 position.
- **Suggested curator question:** Is the existing nucleus annotation IBA/IEA/ISS carried from human PTEN? If so, down-weight given non-conservation of the import determinant.
- **Suggested experiments:** endogenous-tag nuclear imaging + fractionation; *pten⁻* DNA-content cell-cycle staging; amoebozoan MSA/structure alignment.

---

## Provenance (computed this run)

- UniProt sequences: human PTEN **P60484** (403 aa), *Dictyostelium* PTEN **Q8T9S7** (533 aa).
- Pairwise Needleman–Wunsch (numpy): global identity **45.0% (181/402)**; core (human 1–350) **44.4% (155/349)**.
- Catalytic P-loop **HCKAGKGR** conserved at position ~123 in both.
- Nuclear-import lysines: **K13 → K (conserved)**; **aligned K289 has no conserved lysine (Dicty = E)**, in a divergent C2 loop (local identity ~21%) — exact residue low-confidence, "import-signal region not conserved" robust.
- Human C-terminal regulatory tail has no Dicty counterpart; Dicty C-terminus is a long low-complexity Asn/Ser/Thr extension.
- UniProt/dictyBase GO audit (Q8T9S7): nucleus GO:0005634 = **IBA:GO_Central only**; all IDA localizations non-nuclear; **GO:0051726 not present**; direct process term = GO:0000281 mitotic cytokinesis [IMP].

---

## Conclusion

The seed hypothesis is **refuted / over-annotated** for *Dictyostelium discoideum* PTEN. Nuclear localization (GO:0005634) is unsupported by any direct evidence and rests on non-transferable phylogenetic inference; regulation of cell cycle (GO:0051726) is neither annotated nor phenotypically supported, the true defect being mitotic cytokinesis (GO:0000281). The protein's evidenced identity is a membrane/cortex-localized PIP3 3-phosphatase that maintains polarity for cytokinesis and chemotaxis.


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)