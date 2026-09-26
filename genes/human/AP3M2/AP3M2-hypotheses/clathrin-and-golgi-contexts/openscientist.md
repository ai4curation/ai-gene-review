---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-21T03:20:22.887034'
end_time: '2026-09-21T03:44:12.041910'
duration_seconds: 1429.16
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: human
  gene: AP3M2
  gene_symbol: AP3M2
  uniprot_accession: P53677
  taxon_id: NCBITaxon:9606
  taxon_label: Homo sapiens
  focus_type: function_assignment
  hypothesis_slug: clathrin-and-golgi-contexts
  hypothesis_text: Human AP3M2 P53677, the mu3B AP-3 subunit, retains trans-Golgi
    localization, Golgi-to-vacuole/lysosome trafficking, clathrin-adaptor-complex
    membership, clathrin-cargo adaptor activity and AP-3-dependent clathrin cargo
    loading, and AP-3-complex binding. Evaluate each separately using actual GO definitions
    and target/ortholog assays, distinguishing general cargo selection from specifically
    clathrin-dependent endocytic assembly. Actual PTHR10529 tree target PTN002540363
    descends from family-root PTN000055849 (TGN, Golgi-vacuole and clathrin-cargo
    IBD) through AP-3 node PTN002237676; the recovered AP2 TGN-loss node and other
    transport-loss node are outside this path. Broad ancestral placement must be examined,
    not rejected because extant seeds include AP1/AP4. Primary9545220 reports beta3
    clathrin binding and cellular colocalization; full primary39705307 explicitly
    discusses both clathrin-dependent and independent AP3 functions and states clathrin
    inhibition does not FULLY disrupt AP3 traffic. Its 9C5B human structure is AP3M1
    Q9Y2T2, NOT AP3M2; existing reproducible alignment transfers 8/9 cargo-contact
    residues plus conservative V405I. Primary15051738 localizes AP3 to tubular endosomes;
    determine whether it excludes conditional TGN action or principally identifies
    a major route. Primary34688652 is yeast AP3 Golgi reconstitution, not direct human
    AP3M2 evidence. Primary9748267 directly assays mu3A/mu3B tyrosine-signal selection,
    and11588176 shows neuronal AP3 endosomal vesicle budding. AP3-complex-binding
    source mouse Q8R2R9 has IDA19010779; read the full cross-linking/MS experiments
    and do not presume the GO binding definition requires an external ligand. Absence
    of a human-specific assay, constitutive subunit status or clathrin-independent
    competence alone is not refutation. Distinguish genuine term-scope problems, supported
    condition-specific capacity and unresolved evidence.
  term_context: No specific term context supplied.
  reference_context: No specific reference context supplied.
  source_file: genes/human/AP3M2/AP3M2-ai-review.yaml
  source_selector: free-text
  source_context_yaml: "hypothesis: Human AP3M2 P53677, the mu3B AP-3 subunit, retains\
    \ trans-Golgi localization, Golgi-to-vacuole/lysosome\n  trafficking, clathrin-adaptor-complex\
    \ membership, clathrin-cargo adaptor activity and AP-3-dependent\n  clathrin cargo\
    \ loading, and AP-3-complex binding. Evaluate each separately using actual GO\
    \ definitions\n  and target/ortholog assays, distinguishing general cargo selection\
    \ from specifically clathrin-dependent\n  endocytic assembly. Actual PTHR10529\
    \ tree target PTN002540363 descends from family-root PTN000055849\n  (TGN, Golgi-vacuole\
    \ and clathrin-cargo IBD) through AP-3 node PTN002237676; the recovered AP2 TGN-loss\n\
    \  node and other transport-loss node are outside this path. Broad ancestral placement\
    \ must be examined,\n  not rejected because extant seeds include AP1/AP4. Primary9545220\
    \ reports beta3 clathrin binding and\n  cellular colocalization; full primary39705307\
    \ explicitly discusses both clathrin-dependent and independent\n  AP3 functions\
    \ and states clathrin inhibition does not FULLY disrupt AP3 traffic. Its 9C5B\
    \ human structure\n  is AP3M1 Q9Y2T2, NOT AP3M2; existing reproducible alignment\
    \ transfers 8/9 cargo-contact residues plus\n  conservative V405I. Primary15051738\
    \ localizes AP3 to tubular endosomes; determine whether it excludes\n  conditional\
    \ TGN action or principally identifies a major route. Primary34688652 is yeast\
    \ AP3 Golgi reconstitution,\n  not direct human AP3M2 evidence. Primary9748267\
    \ directly assays mu3A/mu3B tyrosine-signal selection,\n  and11588176 shows neuronal\
    \ AP3 endosomal vesicle budding. AP3-complex-binding source mouse Q8R2R9 has\n\
    \  IDA19010779; read the full cross-linking/MS experiments and do not presume\
    \ the GO binding definition\n  requires an external ligand. Absence of a human-specific\
    \ assay, constitutive subunit status or clathrin-independent\n  competence alone\
    \ is not refutation. Distinguish genuine term-scope problems, supported condition-specific\n\
    \  capacity and unresolved evidence.\nfocus_type: function_assignment\ncontext:\
    \ []\nreference_id: []"
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
artifact_count: 6
artifact_sources:
  openscientist_artifacts_zip: 6
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
- filename: provenance_GO0035615_family_carryover.md
  path: openscientist_artifacts/provenance_GO0035615_family_carryover.md
  media_type: text/markdown
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist GO0035615 family carryover
- filename: provenance_ap3m1_vs_ap3m2_alignment_and_9C5B.md
  path: openscientist_artifacts/provenance_ap3m1_vs_ap3m2_alignment_and_9C5B.md
  media_type: text/markdown
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist ap3m1 vs ap3m2 alignment and 9C5B
- filename: provenance_evidence_matrix.csv
  path: openscientist_artifacts/provenance_evidence_matrix.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist evidence matrix
- filename: provenance_go_decision_table.csv
  path: openscientist_artifacts/provenance_go_decision_table.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist go decision table
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
- **Gene directory:** AP3M2
- **Gene symbol:** AP3M2
- **UniProt accession:** P53677

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** clathrin-and-golgi-contexts
- **Source file:** genes/human/AP3M2/AP3M2-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

Human AP3M2 P53677, the mu3B AP-3 subunit, retains trans-Golgi localization, Golgi-to-vacuole/lysosome trafficking, clathrin-adaptor-complex membership, clathrin-cargo adaptor activity and AP-3-dependent clathrin cargo loading, and AP-3-complex binding. Evaluate each separately using actual GO definitions and target/ortholog assays, distinguishing general cargo selection from specifically clathrin-dependent endocytic assembly. Actual PTHR10529 tree target PTN002540363 descends from family-root PTN000055849 (TGN, Golgi-vacuole and clathrin-cargo IBD) through AP-3 node PTN002237676; the recovered AP2 TGN-loss node and other transport-loss node are outside this path. Broad ancestral placement must be examined, not rejected because extant seeds include AP1/AP4. Primary9545220 reports beta3 clathrin binding and cellular colocalization; full primary39705307 explicitly discusses both clathrin-dependent and independent AP3 functions and states clathrin inhibition does not FULLY disrupt AP3 traffic. Its 9C5B human structure is AP3M1 Q9Y2T2, NOT AP3M2; existing reproducible alignment transfers 8/9 cargo-contact residues plus conservative V405I. Primary15051738 localizes AP3 to tubular endosomes; determine whether it excludes conditional TGN action or principally identifies a major route. Primary34688652 is yeast AP3 Golgi reconstitution, not direct human AP3M2 evidence. Primary9748267 directly assays mu3A/mu3B tyrosine-signal selection, and11588176 shows neuronal AP3 endosomal vesicle budding. AP3-complex-binding source mouse Q8R2R9 has IDA19010779; read the full cross-linking/MS experiments and do not presume the GO binding definition requires an external ligand. Absence of a human-specific assay, constitutive subunit status or clathrin-independent competence alone is not refutation. Distinguish genuine term-scope problems, supported condition-specific capacity and unresolved evidence.

## Term and Decision Context

No specific term context supplied.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: Human AP3M2 P53677, the mu3B AP-3 subunit, retains trans-Golgi localization, Golgi-to-vacuole/lysosome
  trafficking, clathrin-adaptor-complex membership, clathrin-cargo adaptor activity and AP-3-dependent
  clathrin cargo loading, and AP-3-complex binding. Evaluate each separately using actual GO definitions
  and target/ortholog assays, distinguishing general cargo selection from specifically clathrin-dependent
  endocytic assembly. Actual PTHR10529 tree target PTN002540363 descends from family-root PTN000055849
  (TGN, Golgi-vacuole and clathrin-cargo IBD) through AP-3 node PTN002237676; the recovered AP2 TGN-loss
  node and other transport-loss node are outside this path. Broad ancestral placement must be examined,
  not rejected because extant seeds include AP1/AP4. Primary9545220 reports beta3 clathrin binding and
  cellular colocalization; full primary39705307 explicitly discusses both clathrin-dependent and independent
  AP3 functions and states clathrin inhibition does not FULLY disrupt AP3 traffic. Its 9C5B human structure
  is AP3M1 Q9Y2T2, NOT AP3M2; existing reproducible alignment transfers 8/9 cargo-contact residues plus
  conservative V405I. Primary15051738 localizes AP3 to tubular endosomes; determine whether it excludes
  conditional TGN action or principally identifies a major route. Primary34688652 is yeast AP3 Golgi reconstitution,
  not direct human AP3M2 evidence. Primary9748267 directly assays mu3A/mu3B tyrosine-signal selection,
  and11588176 shows neuronal AP3 endosomal vesicle budding. AP3-complex-binding source mouse Q8R2R9 has
  IDA19010779; read the full cross-linking/MS experiments and do not presume the GO binding definition
  requires an external ligand. Absence of a human-specific assay, constitutive subunit status or clathrin-independent
  competence alone is not refutation. Distinguish genuine term-scope problems, supported condition-specific
  capacity and unresolved evidence.
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

# AIGR Deep Research Report: AP3M2 (P53677) — "Clathrin and Golgi Contexts" Function-Assignment Hypothesis

**Target gene:** AP3M2 (mu3B AP-3 subunit), *Homo sapiens* (NCBITaxon:9606)
**UniProt:** P53677
**Focus type:** function_assignment
**Hypothesis slug:** clathrin-and-golgi-contexts
**Source:** `genes/human/AP3M2/AP3M2-ai-review.yaml` (free-text)

---

## Summary

The seed hypothesis bundles six distinct claims about human AP3M2/mu3B: (1) trans-Golgi localization, (2) Golgi-to-vacuole/lysosome trafficking, (3) clathrin-adaptor-complex membership, (4) clathrin-cargo adaptor activity, (5) AP-3-dependent clathrin cargo loading, and (6) AP-3-complex binding. The research objective is to evaluate whether the gene product *directly* holds each of these functions, separating genuine mu3B activity from paralog over-annotation, organism-specific attributes, and clathrin claims that are propagated by phylogenetic inference rather than experiment.

**Overall verdict: partially supported.** When each claim is evaluated separately, three cluster as supported (retain), three as over-annotations (remove/generalize/qualify), and localization as real-but-organism-weighted. AP3M2/mu3B is a genuine constitutive AP-3 medium subunit whose directly assayed molecular function is **YXXΦ tyrosine-based sorting-signal (cargo) recognition** (PMID 9748267), acting in **AP-3-mediated endosome/Golgi-to-lysosome/vacuole trafficking** (PMID 15051738, 11588176, 39705307) and neuronal endosome-derived vesicle budding. Those claims hold. In contrast, the **clathrin-specific annotations** — clathrin adaptor complex (GO:0030131), clathrin-cargo adaptor activity (GO:0035615), and the "clathrin-coated" qualifier of GO:0035654 — are over-annotations: UniProt's curated record states AP-3 is "not clathrin-associated," GO's own definitions hedge on AP-3/clathrin, and the best modern mechanism data (human 9C5B / PMID 39705307 and yeast PMID 34688652) show an Arf1-driven, self-polymerizing, clathrin-free coat.

Two structural caveats are decisive for the curator. First, the clathrin-cargo adaptor MF term (GO:0035615) has experimental (IDA) support in this family **only for AP2M1**; on AP3M2 — and on AP3M1, AP1M1, and even the clathrin-independent AP4M1 — it is **IBA-only phylogenetic carry-over** across the PTHR10529 family, the textbook signature of paralog over-annotation. Second, the 9C5B cryo-EM structure invoked by the seed is the **paralog AP3M1 (Q9Y2T2), not AP3M2**; the two mu paralogs are 84.2% identical, which supports transfer of cargo-contact residues but creates no clathrin evidence for mu3B. trans-Golgi localization is real but largely a yeast-derived attribute; the demonstrated human/neuronal mu3B site is the tubular sorting endosome.

---

## Executive Judgment

**Verdict: Partially supported — with specific clathrin terms flagged for removal or qualification.**

Evaluated claim-by-claim:

1. **Supported (retain):** AP-3-complex membership; the directly assayed cargo-selection activity (YXXΦ tyrosine-based sorting-signal recognition); and AP-3-mediated Golgi/endosome-to-vacuole/lysosome trafficking.
2. **Over-annotated (remove / generalize / add "NOT clathrin"):** clathrin adaptor complex (GO:0030131), clathrin-cargo adaptor activity (GO:0035615), and the "clathrin-coated" flavor of GO:0035654.
3. **Real but organism-weighted (qualify):** trans-Golgi localization — genuine but yeast-weighted; the demonstrated human/neuronal mu3B site is the tubular sorting endosome en route to lysosomes/lysosome-related organelles (LROs).

Most important caveat: the strongest "pro-clathrin" primary evidence (PMID 9545220) is an **in-vitro beta3-appendage/clathrin binding** result on the *beta3* subunit — not mu3B — explicitly hedged ("AP-3 function in protein sorting **may** depend on clathrin"). Absence of a human-specific mu3B assay is not itself refutation, but the affirmative clathrin annotations are not carried by any AP3M2-specific experimental evidence.

---

## Key Findings

### Finding 1 — The clathrin-flavored GO terms conflict with the curated "AP-3 is not clathrin-associated" statement and with GO's own hedged definitions

UniProt P53677's curated FUNCTION describes AP-3 as "an adaptor-related complex which is **not** clathrin-associated." This is not an oversight — GO's own definitions are explicitly hedged for AP-3:

- **GO:0030123 (AP-3 adaptor complex):** "AP-3 does **not appear to associate with clathrin** in all organisms."
- **GO:0030119 (AP-type membrane coat adaptor complex):** AP complexes link clathrin "(**or another coat-forming molecule, as hypothesized for AP-3 and AP-4**)."
- **GO:0035654 (clathrin-coated vesicle cargo…):** AP-3 links clathrin only "**in some organisms**."
- **GO:0035615 (clathrin-cargo adaptor activity):** defined specifically as "Bringing together a cargo protein with clathrin, responsible for the formation of **endocytic vesicles**" — the AP-2 job description (plasma-membrane endocytic vesicle formation), not AP-3's endosome/Golgi-to-lysosome sorting role.

The only primary evidence pulling toward a clathrin link is (a) in-vitro beta3-appendage/clathrin binding ([PMID 9545220](https://pubmed.ncbi.nlm.nih.gov/9545220/)), hedged as "AP-3 function in protein sorting **may** depend on clathrin," and (b) partial colocalization ([PMID 15051738](https://pubmed.ncbi.nlm.nih.gov/15051738/)): "AP-3 colocalizes with clathrin, but **to a lesser extent than does AP-1**." Both are weak and indirect, and neither concerns mu3B. This motivates flagging the clathrin CC/MF terms as over-annotations.

### Finding 2 — Human AP-3 (including mu3B) acts principally at tubular sorting endosomes en route to lysosomes/LROs; "trans-Golgi" is largely a yeast-derived attribute

Immuno-EM in human cells ([PMID 15051738](https://pubmed.ncbi.nlm.nih.gov/15051738/)) localizes AP-3 to budding profiles from a **tubular endosomal compartment**, proposing "AP-3 defines a novel pathway by which lysosomal membrane proteins are transported from tubular sorting endosomes to lysosomes." The neuronal AP-3 form — which uses the mu3B/beta3B subunits — produces synaptic vesicles from **endosomes** in vitro ([PMID 11588176](https://pubmed.ncbi.nlm.nih.gov/11588176/): "only the neuronal form of AP-3 can produce synaptic vesicles from endosomes in vitro").

By contrast, the explicit trans-Golgi cargo-collection role is demonstrated in **yeast** AP-3 reconstitution ([PMID 34688652](https://pubmed.ncbi.nlm.nih.gov/34688652/)), and the recent human AP-3 cryo-EM mechanism paper ([PMID 39705307](https://pubmed.ncbi.nlm.nih.gov/39705307/)) describes cargo sorting "from endosomes to lysosomes" via an Arf1-driven, self-polymerizing coat **without invoking clathrin**. UniProt still annotates Golgi apparatus (IEA) and notes AP-3 is "associated with the Golgi region as well as more peripheral structures." So trans-Golgi localization is real but should be **qualified as organism-weighted**; the demonstrated human/neuronal mu3B site is the tubular sorting endosome. The founding AP-3 paper ([PMID 8666661](https://pubmed.ncbi.nlm.nih.gov/8666661/)) does place the complex at "non-clathrin-coated buds and vesicles associated with the TGN" — supporting a TGN role but explicitly as a **non-clathrin** coat.

### Finding 3 — The directly assayed molecular activity of mu3B/AP3M2 is tyrosine-based (YXXΦ) sorting-signal recognition, not clathrin bridging

Ohno et al. ([PMID 9748267](https://pubmed.ncbi.nlm.nih.gov/9748267/)) directly assayed mu3A and mu3B (AP3M1/AP3M2) in a combinatorial yeast two-hybrid screen and showed each medium subunit binds distinct-but-overlapping sets of **YXXΦ tyrosine-based sorting signals** ("each medium subunit favored specific sets of residues at the X and O positions"). This is the direct cargo-recognition function of the mu subunit and the correct, informative molecular-function description for AP3M2 — cargo/signal binding, not clathrin binding.

In-vivo cross-linking/MS of AP-3 ([PMID 19010779](https://pubmed.ncbi.nlm.nih.gov/19010779/)) co-isolated AP-3 with BLOC-1, BLOC-2, HOPS, clathrin, and PI4KIIalpha — documenting AP-3 subunit/complex associations. Because mu3B is a **constitutive component** of the AP-3 heterotetramer (UniProt SUBUNIT), the MF term GO:0035651 "AP-3 adaptor complex binding" describes subunit-within-complex association rather than binding of AP-3 as an external ligand. The seed correctly cautions against presuming the GO binding definition requires an external ligand; mu3B *is* part of AP-3, so "AP-3 complex binding" is best interpreted as structural membership.

### Finding 4 — The 9C5B human AP-3 structure uses mu3A (AP3M1), not mu3B (AP3M2); the paralogs are 84% identical

RCSB PDB **9C5B** (from [PMID 39705307](https://pubmed.ncbi.nlm.nih.gov/39705307/)) polymer entities map to Arf1 (P84077), AP3D1 delta (O14617), **AP3M1 mu-1 (Q9Y2T2)**, AP3S1 sigma (Q92572), LAMP1 cargo (P11279), and AP3B1 beta (O00203) — i.e., the medium subunit in the structure is **AP3M1, NOT AP3M2/P53677**. A pairwise Needleman–Wunsch alignment (P53677 vs Q9Y2T2, both 418 aa, ungapped) gives **352/418 = 84.2% identity**. At AP3M2 residue 405 the alignment shows Ile opposite AP3M1 Val (context m2 'KPFKGIKYMTK' vs m1 'KPFKGVKYVTK'), a conservative V→I substitution matching the seed's claim. Critically, the structure contains a **YXXΦ cargo (LAMP1) and Arf1 but no clathrin** — reinforcing that the modern mechanistic picture of AP-3 is a clathrin-free, Arf1-nucleated coat, and that any cargo-contact-residue transfer from mu3A to mu3B supports cargo recognition, not a clathrin role.

### Finding 5 — Clathrin association of AP-3 is genuinely mixed, not established

The AP-3 discovery paper (Simpson et al., [PMID 8666661](https://pubmed.ncbi.nlm.nih.gov/8666661/)) found "p47 is **not** enriched in preparations of clathrin-coated vesicles" and that the complex "is a component of a **novel type of coat**" at "**non-clathrin-coated** buds and vesicles associated with the TGN." Conversely, in melanocytes Theos et al. ([PMID 16162817](https://pubmed.ncbi.nlm.nih.gov/16162817/)) report that "AP-3 and AP-1 localize... primarily to **clathrin-coated buds** on tubular early endosomes" and recognize the tyrosinase **dileucine** signal, functioning partially redundantly with AP-1. In HPS2 (AP-3-deficient) cells, "blockage of the clathrin-mediated endocytic pathway... did **not** reverse the inhibited virus assembly" ([PMID 22875976](https://pubmed.ncbi.nlm.nih.gov/22875976/)), indicating AP-3 function is separable from clathrin-mediated endocytosis. Together with UniProt's curated "not clathrin-associated" statement and the clathrin-free human/yeast AP-3 structures, the balance of evidence is that clathrin association is **cell-type/condition-specific at best**, not a defining, constitutive property warranting a core GO term.

### Finding 6 — GO:0035615 (clathrin-cargo adaptor activity) has experimental support only for AP2M1 and is IBA-only carry-over on AP3M2

A QuickGO annotation query for **GO:0035615** across human AP mu subunits shows the term's evidence base is decisive:

| Gene | UniProt | GO:0035615 evidence codes |
|------|---------|---------------------------|
| **AP2M1** | Q96CW1 | **IDA (ECO:0000314) + TAS (ECO:0000304)** + IBA |
| AP1M1 | Q9BXS5 | **IBA only** (ECO:0000318) |
| AP3M1 | Q9Y2T2 | **IBA only** |
| **AP3M2** | **P53677** | **IBA only** |
| AP4M1 | O00189 | **IBA only** |

Only **AP2M1** — the genuine clathrin-mediated-endocytosis adaptor — has experimental (IDA) grounding for GO:0035615. AP4M1 carries the term by IBA despite AP-4 being an **established clathrin-INDEPENDENT** complex (Hirst 2011, [PMID 22022230](https://pubmed.ncbi.nlm.nih.gov/22022230/); Barois 2005, [PMID 15377281](https://pubmed.ncbi.nlm.nih.gov/15377281/)). This demonstrates that GO:0035615 is propagated across the PTHR10529 family by phylogenetic inference **irrespective of actual clathrin dependence** — the classic signature of paralog/family over-annotation. On AP3M2 the term is therefore an AP-2-anchored IBA carry-over, not AP-3-specific evidence.

---

## Mechanistic Model / Interpretation

The AP-3 complex is a heterotetramer (delta/AP3D1, beta3/AP3B1 or beta3B/AP3B2, mu3/AP3M1 or **mu3B/AP3M2**, sigma3/AP3S1). Its subunit-level division of labor is well established:

```
                     AP-3 heterotetramer
   ┌──────────────┬──────────────┬──────────────┬──────────────┐
   │  delta        │  beta3/3B     │  mu3/mu3B     │  sigma3       │
   │ (AP3D1)       │ (AP3B1/AP3B2) │ (AP3M1/AP3M2) │ (AP3S1)       │
   │ dileucine     │ appendage:    │  YXXΦ tyrosine │ small-subunit │
   │ signal / SNARE│ in-vitro      │  SORTING-SIGNAL│ structural    │
   │ (VAMP7)       │ clathrin bind │  RECOGNITION   │               │
   └──────────────┴──────────────┴──────────────┴──────────────┘
            │                           │
            │ recruited by Arf1-GTP + PI-lipids (BFA-sensitive)
            ▼                           ▼
   Tubular SORTING ENDOSOME  ──►  Lysosome / LRO (melanosome, synaptic vesicle)
        (major human/neuronal site)
   trans-Golgi network  ──►  vacuole   (major yeast site; human = "Golgi region")

   COAT = Arf1-driven, self-polymerizing, CLATHRIN-FREE (9C5B; yeast recon.)
   Clathrin colocalization = partial, cell-type-specific (melanocytes), NOT core
```

**Where the seed's claims land on this model:**

| Seed claim | Verdict | Basis |
|------------|---------|-------|
| AP-3-complex membership | **Supported** | mu3B is a constitutive subunit (UniProt SUBUNIT) |
| Cargo-adaptor / cargo selection | **Supported** (as YXXΦ recognition) | Direct assay PMID 9748267 |
| Golgi-to-vacuole/lysosome trafficking | **Supported** (endosome-to-lysosome in human) | PMID 15051738, 11588176, 39705307 |
| trans-Golgi localization | **Qualified** — real but yeast-weighted | PMID 34688652 (yeast), 8666661 (TGN, non-clathrin) |
| Clathrin-adaptor-complex membership (CC) | **Over-annotated** | UniProt "not clathrin-associated"; clathrin-free structures |
| Clathrin-cargo adaptor activity (MF, GO:0035615) | **Over-annotated (IBA carry-over)** | IDA only on AP2M1; IBA on AP3M2 |
| AP-3-dependent clathrin cargo loading | **Unresolved / not AP-3-specific** | Only in-vitro beta3 binding (PMID 9545220), hedged |

The key mechanistic distinction the seed asks for — **general cargo selection vs. specifically clathrin-dependent endocytic assembly** — resolves cleanly: mu3B performs *general (tyrosine-signal) cargo selection* within an Arf1-nucleated AP-3 coat, and there is **no direct evidence** that it participates in *clathrin-dependent endocytic vesicle assembly* (GO:0035615's actual definition, and AP-2's job).

---

## Evidence Base / Evidence Matrix

| Citation | Evidence type | Supports / Refutes / Qualifies / Competing | Claim tested | Key finding | Context | Confidence & limitations |
|----------|---------------|---------------------------------------------|--------------|-------------|---------|--------------------------|
| [PMID 9748267](https://pubmed.ncbi.nlm.nih.gov/9748267/) | Direct assay (Y2H) | **Supports** cargo selection; **refutes** clathrin-bridging as the mu activity | mu3B molecular function | mu3A/mu3B each recognize distinct/overlapping YXXΦ tyrosine sorting signals | Combinatorial yeast two-hybrid, mu3A & mu3B | High for cargo recognition; in-vitro binding |
| [PMID 39705307](https://pubmed.ncbi.nlm.nih.gov/39705307/) | Structural (cryo-EM) | **Supports** clathrin-free coat; **refutes** core clathrin role | AP-3 coat mechanism | Arf1-driven, self-polymerizing coat with LAMP1 cargo; no clathrin | Human AP-3 (structure uses **AP3M1**, not AP3M2) | High for mechanism; paralog mismatch (84.2% id) |
| [PMID 34688652](https://pubmed.ncbi.nlm.nih.gov/34688652/) | Reconstitution | **Qualifies** trans-Golgi (yeast); **supports** clathrin-free budding | Golgi-to-vacuole cargo collection | Yeast AP-3 collects cargo at Golgi without clathrin | *S. cerevisiae* in-vitro | High for yeast; not direct human AP3M2 evidence |
| [PMID 15051738](https://pubmed.ncbi.nlm.nih.gov/15051738/) | Localization (immuno-EM) | **Qualifies** localization & clathrin | AP-3 site in human cells | AP-3 buds from tubular sorting endosomes; clathrin colocalization "less than AP-1" | Human cells | High for endosome route; weak clathrin colocalization |
| [PMID 11588176](https://pubmed.ncbi.nlm.nih.gov/11588176/) | Direct assay (in-vitro budding) | **Supports** mu3B trafficking role | Neuronal AP-3 (mu3B) function | Neuronal AP-3 produces synaptic vesicles from endosomes | Neuronal AP-3 form | High; endosome-derived, not TGN |
| [PMID 9545220](https://pubmed.ncbi.nlm.nih.gov/9545220/) | Interaction (in-vitro) | **Competing / weakly supports** clathrin | AP-3–clathrin link | beta3 appendage binds clathrin; "**may** depend on clathrin" | In-vitro + colocalization | Low; beta3 not mu3B; hedged |
| [PMID 8666661](https://pubmed.ncbi.nlm.nih.gov/8666661/) | Biochemistry + localization | **Refutes** clathrin-coat identity; **supports** TGN | AP-3 coat identity | p47/mu3 complex is a "novel," **non-clathrin** coat at TGN buds | Rat/neuronal, founding paper | High; foundational |
| [PMID 16162817](https://pubmed.ncbi.nlm.nih.gov/16162817/) | Localization + function | **Competing** (pro-clathrin in melanocytes) | AP-3/clathrin in melanocytes | AP-3 at clathrin-coated buds; recognizes **dileucine** signal; redundant with AP-1 | Melanocytes | Moderate; cell-type-specific; dileucine (delta), not YXXΦ (mu) |
| [PMID 22875976](https://pubmed.ncbi.nlm.nih.gov/22875976/) | Mutant phenotype | **Refutes** clathrin-dependence of AP-3 function | AP-3 vs clathrin endocytosis | Blocking clathrin endocytosis did not reverse AP-3-deficient phenotype | HPS2 (AP3B1-null) human fibroblasts | High for separability |
| [PMID 19010779](https://pubmed.ncbi.nlm.nih.gov/19010779/) | Interaction (XL-MS, IDA) | **Supports** complex associations | AP-3 interactome | AP-3 co-isolates with BLOC-1/2, HOPS, clathrin, PI4KIIα | Mouse (Q8R2R9) in-vivo XL/MS | Moderate; clathrin co-isolation ≠ clathrin coat |
| [PMID 22022230](https://pubmed.ncbi.nlm.nih.gov/22022230/) | Primary/review | **Supports** family clathrin-independence | AP-4/AP-5 clathrin status | AP-4/AP-5 do not associate with clathrin; AP-3 basal complex | HeLa | Moderate; orientation for carry-over |
| [PMID 15377281](https://pubmed.ncbi.nlm.nih.gov/15377281/) | Localization | **Supports** family clathrin-independence context | AP-4 clathrin status | AP-4 studied as distinct from clathrin machinery | MDCK/MelJuSo | Moderate |
| UniProt P53677 (curated) | Database | **Refutes** clathrin association | AP-3 clathrin status | "adaptor-related complex which is **not** clathrin-associated" | Curated record | Curated; high weight |
| QuickGO GO:0035615 | Database (computed) | **Refutes** AP3M2 clathrin-cargo term | Evidence base of term | IDA only on AP2M1; IBA-only on AP3M2/AP3M1/AP1M1/AP4M1 | Human AP mu subunits | High; direct annotation query |

---

## GO Curation Implications

**Lead recommendations (require curator verification):**

1. **GO:0035615 — clathrin-cargo adaptor activity (MF):** *Recommend REMOVE or DOWNGRADE on AP3M2.* Evidence base is IBA-only phylogenetic carry-over from AP2M1 across PTHR10529; the definition ("bringing together a cargo protein with clathrin… formation of **endocytic vesicles**") describes AP-2's plasma-membrane endocytic role, not AP-3's endosome/Golgi-to-lysosome sorting. The same term sits by IBA on the clathrin-**independent** AP4M1, confirming propagation is definitional, not evidential. **Replace with a cargo-recognition MF** reflecting the direct assay — a "cargo receptor / sorting-signal binding"–style term capturing YXXΦ tyrosine-based signal recognition (PMID 9748267), which is more informative than bare "protein binding."

2. **GO:0030131 — clathrin adaptor complex (CC):** *Recommend REMOVE or replace with GO:0030123 (AP-3 adaptor complex).* AP-3 is not constitutively a clathrin adaptor complex; UniProt curates "not clathrin-associated" and the modern coat is Arf1-driven/clathrin-free. GO:0030123 is the correct, specific CC.

3. **GO:0035654 "clathrin-coated" qualifier:** *Recommend GENERALIZE / drop the clathrin qualifier.* The cargo-loading role is real; the "clathrin-coated" flavor is not supported for AP-3.

4. **AP-3 complex (CC, GO:0030123) and AP-3-mediated Golgi/endosome-to-lysosome/vacuole transport (BP):** *RETAIN.* Well supported; qualify localization to emphasize the **tubular sorting endosome → lysosome/LRO** route in human cells, with trans-Golgi as an organism-weighted (yeast) attribute.

5. **GO:0035651 — AP-3 adaptor complex binding (MF):** *RETAIN as subunit-within-complex membership*, noting it describes structural membership (mu3B is constitutive), not binding of AP-3 as an external ligand; the mouse IDA (PMID 19010779) is XL-MS of complex associations.

**Net:** evidence supports **MF = cargo/sorting-signal recognition** (not clathrin-cargo adaptor), **CC = AP-3 adaptor complex** (not clathrin adaptor complex), and **BP = AP-3-mediated endosome/Golgi-to-lysosome/LRO transport**. The clathrin-specific terms should be treated as **non-core over-annotations**.

---

## Mechanistic Scope

The immediate molecular function under test is **mu3B/AP3M2's cargo-recognition activity within the AP-3 heterotetramer**. Directly assayed, this is **YXXΦ tyrosine-based sorting-signal binding** (PMID 9748267) — a sequence-specific protein–protein recognition that selects transmembrane cargo for inclusion into AP-3 transport carriers. This is a genuine direct gene-product activity.

Distinguished from that direct activity:
- **Downstream phenotypes:** lysosome/LRO biogenesis defects, hypopigmentation (melanosome cargo mis-sorting), HPS2, and impaired HIV-1 assembly are **loss-of-function consequences** at the pathway/organism level, not mu3B molecular functions.
- **Coat assembly / vesicle budding** is a **complex-level** property driven by Arf1 and the beta3/delta subunits; mu3B contributes cargo selection, not coat polymerization.
- **Clathrin binding** (where reported) is a property of the **beta3 appendage** in vitro (PMID 9545220), not of mu3B, and is not required for AP-3 function (PMID 22875976).

---

## Conflicts and Alternatives

1. **Paralog confusion (most important):** the seed's cited 9C5B structure is **AP3M1 (mu3A)**, not AP3M2 (mu3B). Cargo-contact-residue transfer across the 84.2%-identical paralogs is reasonable for cargo binding but generates **no** clathrin evidence for mu3B.
2. **Family over-annotation:** GO:0035615 is IBA-propagated across PTHR10529 (AP1/AP2/AP3/AP4 mu subunits); only AP2M1 has experimental support. This is the mechanism by which AP3M2 inherited a clathrin term it does not merit.
3. **Organism-specific differences:** trans-Golgi cargo collection is best demonstrated in **yeast** (PMID 34688652); human/neuronal mu3B acts at **tubular sorting endosomes** (PMID 15051738, 11588176). GO's definitions explicitly note AP-3/clathrin differs "in some organisms."
4. **Cell-type-specific pro-clathrin data:** melanocyte imaging (PMID 16162817) places AP-3 at clathrin-coated buds and shows **dileucine** (delta-subunit) recognition — not the mu3B YXXΦ activity. Real but context-specific and subunit-mismatched.
5. **Interaction ≠ coat:** XL-MS co-isolation of clathrin with AP-3 (PMID 19010779) documents proximity/association, not that AP-3 forms a clathrin coat; clathrin blockade does not abolish AP-3 function (PMID 22875976).

---

## Limitations and Knowledge Gaps

| Gap | What was checked | Why it matters | What would resolve it |
|-----|------------------|----------------|-----------------------|
| No **human AP3M2-specific** localization/function assay | Human data are AP-3-complex-level or use mu3A structure | Curation is for AP3M2 specifically | mu3B-tagged immuno-EM / knock-in localization in human cells |
| trans-Golgi vs endosome primacy in human | PMID 15051738 (endosome), 8666661 (TGN, yeast/neuronal) | Determines CC localization terms | Quantitative colocalization of AP3M2 with TGN vs endosome markers |
| Direct mu3B–clathrin test absent | Only beta3 in-vitro binding (PMID 9545220) | Core question of the hypothesis | Direct mu3B/clathrin binding assay (though mu is definitionally a cargo-recognition subunit) |
| PMID 9545220 / 11588176 full text unread | Verified snippets; full methods not re-derived | Strength of strongest pro-clathrin claim | Full-text read of PMID 9545220 methods |
| PMID 15051738 full text partially unchecked | Snippet verified | Whether TGN action is excluded or just secondary | Full-text read |
| Functional redundancy mu3A/mu3B | Paralogs 84.2% identical, overlapping YXXΦ specificity | Whether AP3M2 terms should mirror AP3M1 | Isoform-specific knockdown/rescue with cargo panels |

---

## Discriminating Tests

1. **Direct mu3B cargo panel vs clathrin binding:** extend PMID 9748267-style Y2H or use ITC/SPR with purified mu3B against a YXXΦ cargo panel *and* against clathrin terminal domain — expect strong YXXΦ binding, no direct clathrin binding.
2. **AP3M2-specific localization:** endogenous-tag AP3M2 in human cells (neuronal + non-neuronal) and quantify colocalization with TGN46 (trans-Golgi) vs EEA1/tubular-endosome and LAMP1 markers.
3. **Clathrin-dependence of AP3M2 cargo delivery:** knock down clathrin heavy chain and test whether AP3M2-dependent LAMP1/LRO cargo delivery is impaired — prior HPS2 data (PMID 22875976) predict little effect.
4. **Cryo-EM of an AP3M2-containing (neuronal beta3B/mu3B) coat:** determine whether the mu3B coat, like the mu3A 9C5B structure, is clathrin-free and Arf1-nucleated.
5. **Cross-family GO audit:** confirm via QuickGO/PAINT that GO:0035615 IBA on AP3M2/AP4M1 traces to the AP2M1 experimental annotation, justifying an annotation-review request.

---

## Proposed Follow-up Actions / Curation Leads (require curator verification)

**Candidate action changes:**
- **Remove/downgrade** GO:0035615 (clathrin-cargo adaptor activity) on AP3M2 as IBA-only family carry-over from AP2M1; document rationale citing QuickGO evidence codes.
- **Replace** clathrin adaptor complex (GO:0030131) CC with **AP-3 adaptor complex (GO:0030123)**.
- **Generalize** GO:0035654 by dropping the "clathrin-coated" qualifier for AP-3.
- **Retain** AP-3 complex membership, AP-3-mediated Golgi/endosome-to-lysosome/vacuole transport (BP), and GO:0035651 (AP-3 adaptor complex binding, as structural membership).
- **Add/strengthen** an informative MF for **tyrosine-based (YXXΦ) sorting-signal / cargo recognition** grounded in PMID 9748267 (avoid bare "protein binding").
- **Qualify** trans-Golgi CC as organism-weighted; emphasize tubular sorting endosome → lysosome/LRO in human.

**Candidate references with exact snippets to verify:**
- PMID 9748267 — "interact with the medium (mu) subunits of clathrin adaptor (AP) complexes" (direct mu3B YXXΦ assay).
- PMID 9545220 — "AP-3 function in protein sorting **may** depend on clathrin"; "AP-3 is involved in signal-mediated protein sorting to endosomal-lysosomal organelles."
- PMID 15051738 — "AP-3 colocalizes with clathrin, but **to a lesser extent than does AP-1**."
- PMID 8666661 — "p47 is **not** enriched in preparations of clathrin-coated vesicles"; "non-clathrin-coated buds and vesicles associated with the TGN."
- PMID 22875976 — "Blockage of the clathrin-mediated endocytic pathway... did **not** reverse the inhibited virus assembly."
- UniProt P53677 FUNCTION — "adaptor-related complex which is **not** clathrin-associated."

**Suggested curator questions:**
- Does any AP3M2 clathrin term trace to experimental evidence, or only IBA/ISS from AP2M1?
- Should trans-Golgi CC be retained for the human protein given endosome-primacy data?
- Is GO:0035651 best interpreted as structural membership rather than external-ligand binding?

**Suggested experiments:** the five Discriminating Tests above, prioritizing (1) direct mu3B cargo-vs-clathrin binding and (2) AP3M2-specific human localization.

---

## Bottom Line

AP3M2/mu3B is a bona fide constitutive AP-3 medium subunit whose **directly assayed function is YXXΦ tyrosine-based cargo-signal recognition**, acting in **AP-3-mediated endosome/Golgi-to-lysosome/vacuole/LRO trafficking** and neuronal endosome-derived vesicle budding. Those claims (AP-3 membership, cargo selection, Golgi-to-vacuole/lysosome transport) are **supported**. The **clathrin-specific annotations** — clathrin adaptor complex (GO:0030131), clathrin-cargo adaptor activity (GO:0035615), and the "clathrin-coated" qualifier — are **over-annotations**: UniProt curates AP-3 as "not clathrin-associated," GO's own definitions hedge, GO:0035615 has experimental support only for AP2M1 (IBA-only on AP3M2 and even on clathrin-independent AP4M1), and the best modern mechanism data (clathrin-free Arf1-driven coat; note 9C5B is the paralog AP3M1) confirm no core clathrin role. trans-Golgi localization is real but **yeast-weighted**; the demonstrated human/neuronal mu3B site is the tubular sorting endosome.


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)
- [OpenScientist GO0035615 family carryover](openscientist_artifacts/provenance_GO0035615_family_carryover.md)
- [OpenScientist ap3m1 vs ap3m2 alignment and 9C5B](openscientist_artifacts/provenance_ap3m1_vs_ap3m2_alignment_and_9C5B.md)
- [OpenScientist evidence matrix](openscientist_artifacts/provenance_evidence_matrix.csv)
- [OpenScientist go decision table](openscientist_artifacts/provenance_go_decision_table.csv)