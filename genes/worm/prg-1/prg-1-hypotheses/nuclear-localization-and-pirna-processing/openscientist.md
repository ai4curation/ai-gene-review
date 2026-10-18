---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-20T18:13:18.301264'
end_time: '2026-09-20T18:34:37.323073'
duration_seconds: 1279.02
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: worm
  gene: prg-1
  gene_symbol: prg-1
  uniprot_accession: P90786
  taxon_id: NCBITaxon:6239
  taxon_label: Caenorhabditis elegans
  focus_type: function_assignment
  hypothesis_slug: nuclear-localization-and-pirna-processing
  hypothesis_text: 'Caenorhabditis elegans PRG-1 localizes to the nucleus (GO:0005634)
    and participates in piRNA processing (GO:0034587). Adjudicate these independently:
    distinguish perinuclear germ granules from intranuclear protein, and test whether
    precursor loading/scaffolding contributes to processing versus stabilizing only
    mature piRNAs. Participation does not require the protein to catalyze cleavage
    itself. Inspect PARN-1-dependent maturation evidence.'
  term_context: No specific term context supplied.
  reference_context: No specific reference context supplied.
  source_file: genes/worm/prg-1/prg-1-ai-review.yaml
  source_selector: free-text
  source_context_yaml: "hypothesis: 'Caenorhabditis elegans PRG-1 localizes to the\
    \ nucleus (GO:0005634) and participates in piRNA\n  processing (GO:0034587). Adjudicate\
    \ these independently: distinguish perinuclear germ granules from\n  intranuclear\
    \ protein, and test whether precursor loading/scaffolding contributes to processing\
    \ versus\n  stabilizing only mature piRNAs. Participation does not require the\
    \ protein to catalyze cleavage itself.\n  Inspect PARN-1-dependent maturation\
    \ evidence.'\nfocus_type: function_assignment\ncontext: []\nreference_id: []"
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
citation_count: 11
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
- filename: prg1_current_go_annotations.csv
  path: openscientist_artifacts/prg1_current_go_annotations.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist prg1 current go annotations
- filename: prg1_evidence_matrix.csv
  path: openscientist_artifacts/prg1_evidence_matrix.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist prg1 evidence matrix
- filename: prg1_go_decision_table.csv
  path: openscientist_artifacts/prg1_go_decision_table.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist prg1 go decision table
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
- **Gene directory:** prg-1
- **Gene symbol:** prg-1
- **UniProt accession:** P90786

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** nuclear-localization-and-pirna-processing
- **Source file:** genes/worm/prg-1/prg-1-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

Caenorhabditis elegans PRG-1 localizes to the nucleus (GO:0005634) and participates in piRNA processing (GO:0034587). Adjudicate these independently: distinguish perinuclear germ granules from intranuclear protein, and test whether precursor loading/scaffolding contributes to processing versus stabilizing only mature piRNAs. Participation does not require the protein to catalyze cleavage itself. Inspect PARN-1-dependent maturation evidence.

## Term and Decision Context

No specific term context supplied.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: 'Caenorhabditis elegans PRG-1 localizes to the nucleus (GO:0005634) and participates in piRNA
  processing (GO:0034587). Adjudicate these independently: distinguish perinuclear germ granules from
  intranuclear protein, and test whether precursor loading/scaffolding contributes to processing versus
  stabilizing only mature piRNAs. Participation does not require the protein to catalyze cleavage itself.
  Inspect PARN-1-dependent maturation evidence.'
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

# PRG-1 (worm, UniProt P90786) — Adjudication of "Nuclear Localization and piRNA Processing"

**Focus:** function_assignment · **Hypothesis slug:** nuclear-localization-and-pirna-processing
**Source file:** genes/worm/prg-1/prg-1-ai-review.yaml · **Selector:** free-text
**Organism:** *Caenorhabditis elegans* (NCBITaxon:6239) · **Date:** 2026-09-21

---

## Summary

The seed hypothesis bundles two claims that must be adjudicated independently, and when they are, they resolve in opposite directions. PRG-1 is the *C. elegans* Piwi Argonaute that binds 21U-RNAs (piRNAs). The hypothesis asserts (1) that PRG-1 localizes to the **nucleus (GO:0005634)** and (2) that it participates in **piRNA processing (GO:0034587)**, and it explicitly asks the curator to distinguish perinuclear germ granules from intranuclear protein and to test whether PRG-1 contributes to precursor processing versus merely stabilizing mature piRNAs. The evidence answers both prompts cleanly.

**The piRNA-processing clause is supported as non-catalytic participation.** PRG-1 loads and stabilizes the untrimmed 21U pre-piRNA precursor and provides the platform on which 3′-end maturation occurs. The catalytic trimming step is performed by the ribonuclease **PARN-1**, with **HENN-1** adding a protective 2′-O-methyl group — PRG-1 itself does not catalyze cleavage or trimming. Because GO conventions permit non-catalytic participation, GO:0034587 is defensible, but the experimentally grounded, worm-specific term **GO:0034585 "21U-RNA metabolic process" (IMP)** is the better-supported and more precise choice for this protein.

**The nuclear-localization clause is over-annotated.** GO:0005634 "nucleus" on PRG-1 rests **only** on a phylogenetic IBA inference propagated across the PIWI clade (GO_REF:0000033), with no experimental *C. elegans* backing. This is independently contradicted by UniProtKB's own curated subcellular-location comment for P90786, which lists **Cytoplasm only** (no Nucleus location or keyword), and by direct experimental IDA evidence placing PRG-1 in **perinuclear P granules (GO:0043186)**, a cytoplasm-facing condensate docked on the outer nuclear envelope. The pathway's genuine nuclear silencing arm is executed **downstream** by the nuclear Argonautes HRDE-1/NRDE-3 loaded with 22G-RNAs — a pathway consequence, not PRG-1's own localization. The net recommendation is to **split the hypothesis**: keep the processing/participation claim (preferring the 21U term) and flag/demote the nucleus claim as IBA carry-over.

---

## Key Findings

### F001 — The nucleus annotation (GO:0005634) is IBA carry-over, not experimental fact

A live QuickGO annotation pull for P90786 (2026-09) shows that GO:0005634 "nucleus" is supported **only** by an IBA annotation — Inferred from Biological Ancestor (ECO:0000318; GO_Central; GO_REF:0000033). IBA is a phylogenetic inference: the term was propagated onto PRG-1 because other members of the PIWI Argonaute clade carry a nucleus annotation, not because anyone observed PRG-1 inside the *C. elegans* nucleoplasm. In the same annotation set, the cellular-component term **GO:0043186 "P granule" carries direct experimental IDA (ECO:0000314)** from two foundational papers ([PMID: 18501605](https://pubmed.ncbi.nlm.nih.gov/18501605/), [PMID: 18571452](https://pubmed.ncbi.nlm.nih.gov/18571452/)), while the generic cytoplasm term (GO:0005737) is IEA.

The primary literature is unanimous that PRG-1's native compartment is perinuclear. A 2026 study of unloaded-Argonaute degradation states that "the failure to load piRNAs disrupts PRG-1 localization to **perinuclear germ granules**" ([PMID: 41529195](https://pubmed.ncbi.nlm.nih.gov/41529195/)), naming the native compartment as perinuclear germ granules. A study of Piwi-mutant sterility observes that "sterile individuals consistently exhibit altered **perinuclear germ granules**" ([PMID: 33658512](https://pubmed.ncbi.nlm.nih.gov/33658512/)), again centering PRG-1 function on perinuclear granules rather than the nucleoplasm.

Crucially, the seed hypothesis's own request — distinguish perinuclear germ granules from intranuclear protein — is exactly the test that dissolves the nucleus annotation. P granules dock on the cytoplasmic face of the nuclear envelope over germ-cell nuclei; their perinuclear position is a cytoplasmic-facing localization and is not evidence of intranuclear (nucleoplasmic) PRG-1.

### F002 — PRG-1 participates in piRNA processing by loading/scaffolding precursors; PARN-1 catalyzes trimming

The mechanistic core of the processing clause is well established across three primary studies. Untrimmed pre-piRNAs — 21U precursors bearing 3′ extensions — are stably bound by PRG-1, and 3′-end maturation is carried out by the nuclease PARN-1, with HENN-1 methylation protecting the mature 3′ end. The foundational trimming study reports that "these longer piRNAs are stable and **associate with the Piwi protein PRG-1** but fail to robustly recruit downstream silencing factors" ([PMID: 26919432](https://pubmed.ncbi.nlm.nih.gov/26919432/)), showing that untrimmed precursors load onto PRG-1 while a separate activity performs the maturating trim. A later study confirms that "long isoforms of untrimmed piRNAs are preferentially **modified in parn-1 mutant animals**" ([PMID: 34469728](https://pubmed.ncbi.nlm.nih.gov/34469728/)), establishing PARN-1 as the 3′-trimming nuclease acting on PRG-1-associated precursors. A cross-species synthesis states that "the ribonuclease **PARN-1 and its orthologs mediate piRNA 3′ trimming** in worms, insects, and mammals" ([PMID: 38244197](https://pubmed.ncbi.nlm.nih.gov/38244197/)), assigning the catalytic trimming step to PARN-1, not PRG-1.

On the annotation side, QuickGO shows GO:0034587 "piRNA processing" for P90786 is **IBA + IEA only**, whereas the worm-specific term **GO:0034585 "21U-RNA metabolic process" carries experimental IMP (ECO:0000315)** from [PMID: 18571452](https://pubmed.ncbi.nlm.nih.gov/18571452/). PRG-1 is required for the stable accumulation of mature 21U-RNAs and provides the platform on which 3′ trimming occurs, but it does not itself catalyze the trimming/cleavage step. This directly answers the seed hypothesis's fork: PRG-1 binds the *precursor* (pre-piRNA), so its role exceeds passive stabilization of mature piRNAs — yet it is non-catalytic, so "participation" (not molecular-function catalysis) is the correct framing.

### F003 — UniProt's curated location for P90786 is Cytoplasm only, corroborating the IBA-carry-over conclusion

Independent of the GO annotation set, the UniProtKB record for **P90786 (824 aa)** lists a subcellular-location comment of **"Cytoplasm"** (ECO:0000256) with a keyword set of {Cytoplasm, Developmental protein, Hydrolase, RNA-binding, RNA-mediated gene silencing}. There is **no "Nucleus" subcellular-location annotation and no Nucleus keyword**. The domain architecture is a **PAZ domain (~220–331)** and a **PIWI domain (~499–810)** with an N-terminal disordered region (~1–24). Because UniProt curators arrive at their location comment through a pipeline distinct from GO_Central phylogenetic propagation, their convergence on "Cytoplasm only" is an orthogonal line of evidence that the GO:0005634 nucleus annotation is a PIWI-clade IBA artifact rather than a reflection of PRG-1's actual localization.

---

## Mechanistic Model / Interpretation

```
  21U pre-piRNA precursor (Pol II, capped, 3'-extended)
              │
              │  PETISCO / TOFU factors  ── 5' processing (largely upstream, PRG-1-independent)
              ▼
      ┌───────────────────────┐
      │  PRG-1 (Piwi)         │   ◄── LOADS + STABILIZES untrimmed precursor
      │  binds pre-piRNA      │       (scaffold / platform; NON-catalytic)
      └───────────┬───────────┘
                  │  PARN-1 ribonuclease  ── CATALYZES 3' trimming
                  ▼
      ┌───────────────────────┐
      │  Mature 21U-RNA on    │
      │  PRG-1  (piRISC)      │
      └───────────┬───────────┘
                  │  HENN-1  ── 2'-O-methylation (protects 3' end)
                  ▼
    Target scanning → 22G-RNA amplification (RdRP EGO-1)
                    → NUCLEAR silencing by HRDE-1 / NRDE-3  ◄── downstream, NOT PRG-1

  LOCALIZATION:  Perinuclear P granules (cytoplasmic face of nuclear pores) — NOT nucleoplasm
```

Two conclusions follow. **For the process (BP):** PRG-1's contribution is precursor loading, scaffolding, and stabilization — not enzymatic maturation. The trimming enzyme is PARN-1; the methyltransferase is HENN-1. "Participates in piRNA processing" does not require catalysis, so GO:0034587 is annotatable, but the phenotype-grounded worm term GO:0034585 (IMP) is more informative. **For the location (CC):** PRG-1 resides in perinuclear P granules. "Perinuclear" describes granules docked on the cytoplasmic face of the nuclear envelope; it is not intranuclear. The nuclear transcriptional silencing that piRNAs ultimately trigger is executed downstream by HRDE-1/NRDE-3, so the pathway's nuclear activity must not be back-attributed to PRG-1 as a localization.

### GO decision table

| Term | Aspect | Current evidence on PRG-1 | Recommended action (lead) |
|---|---|---|---|
| **GO:0005634 nucleus** | CC | **IBA only** (GO_REF:0000033); no worm experimental support | **Do not treat as core; candidate for removal / NOT.** Contradicted by IDA P-granule localization and UniProt "Cytoplasm only." If retained, restrict to IBA; do not cite as evidence of a direct nuclear pool. |
| **GO:0043186 P granule** | CC | **IDA** (PMID:18501605, 18571452) | **Retain** — the experimentally supported localization. |
| GO:0005737 cytoplasm | CC | IEA | Retain (consistent with UniProt and perinuclear condensate). |
| **GO:0034587 piRNA processing** | BP | IBA + IEA | Defensible as non-catalytic participation; if kept, frame as precursor loading/scaffolding, not catalysis. |
| **GO:0034585 21U-RNA metabolic process** | BP | **IMP** (PMID:18571452) | **Prefer/promote** — experimentally grounded, worm-specific. |
| GO:0034583/0034584 21U-RNA/piRNA binding | MF | IPI (exp) / IBA | Retain — the informative MF (precursor + mature 21U binding). |

Avoid "protein binding" as a recommendation; the informative MF is **21U-RNA/piRNA binding (GO:0034583/0034584)**.

---

## Evidence Base

### Evidence Matrix

| Citation | Type | Stance | Claim tested | Key finding | Context | Confidence / limits |
|---|---|---|---|---|---|---|
| [PMID: 41529195](https://pubmed.ncbi.nlm.nih.gov/41529195/) | Localization + mutant | Refutes nuclear / supports perinuclear | PRG-1 localization | Native PRG-1 sits in **perinuclear germ granules**; unloaded PRG-1 mislocalizes and is degraded | Germline | High for perinuclear; no nuclear-pool quantitation |
| [PMID: 33658512](https://pubmed.ncbi.nlm.nih.gov/33658512/) | Mutant phenotype | Supports perinuclear | Piwi function locus | Sterility tracks with **altered perinuclear germ granules** | Germline | High |
| [PMID: 18501605](https://pubmed.ncbi.nlm.nih.gov/18501605/) | Localization (IDA) | Supports perinuclear | PRG-1 CC term | Experimental basis for **GO:0043186 P granule (IDA)** | Germline | High; foundational |
| [PMID: 18571452](https://pubmed.ncbi.nlm.nih.gov/18571452/) | IDA/IMP/IPI | Supports perinuclear + 21U | P granule, 21U binding/metabolism | Basis for P granule (IDA), **21U-RNA binding (IPI)**, 21U metabolic process (IMP) | Germline | High; foundational |
| [PMID: 26919432](https://pubmed.ncbi.nlm.nih.gov/26919432/) | Direct assay + mutant | Qualifies processing | PRG-1 in maturation | Untrimmed pre-piRNAs stay **PRG-1-associated**; PARN-1 sets 21U length | Germline | High; PRG-1 scaffolds, PARN-1 catalyzes |
| [PMID: 34469728](https://pubmed.ncbi.nlm.nih.gov/34469728/) | Direct assay + mutant | Qualifies processing | 3′ maturation enzymes | **PARN-1 trims + HENN-1 methylates**; loss depletes piRNAs | Germline | High; PRG-1 non-catalytic |
| [PMID: 38244197](https://pubmed.ncbi.nlm.nih.gov/38244197/) | Direct assay / comparative | Qualifies processing | Conservation of trimming | **PARN-1 orthologs** mediate piRNA 3′ trimming across taxa | Cross-species | High |
| [PMID: 31147388](https://pubmed.ncbi.nlm.nih.gov/31147388/) | Complex + mutant | Competing (biogenesis) | 5′ precursor processing | **PETISCO** required for 21U biogenesis, upstream of PRG-1 | Germline | High; PRG-1-independent arm |
| [PMID: 34413138](https://pubmed.ncbi.nlm.nih.gov/34413138/) | Structural | Competing (biogenesis) | PETISCO assembly | Structural basis of PETISCO in piRNA biogenesis | — | Med-High |
| [PMID: 41414669](https://pubmed.ncbi.nlm.nih.gov/41414669/) | Mutant / SAR | Bounds processing scope | PRG-1 RG motifs | RG motifs drive downstream WAGO-siRNA production but are **not needed for localization or piRNA loading** | Germline | High; separates loading from silencing |
| [PMID: 37154856](https://pubmed.ncbi.nlm.nih.gov/37154856/) | IP-seq | Supports binding | PRG-1 sRNA partner | Of 20 Argonautes, **only PRG-1 binds piRNAs** | Germline | High |
| GO_REF:0000033 (IBA) | Computational | Over-annotation source | Nucleus & processing terms | GO:0005634 & GO:0034587 for PRG-1 are **IBA/IEA only** | PIWI phylogeny | Weak for direct localization |
| UniProtKB:P90786 | Database | Refutes nuclear | Curated location + domains | **Cytoplasm only (no Nucleus)**; **PAZ (220–331) + PIWI (499–810)**, 824 aa | UniProt (2026-09) | Location ECO:0000256 (automatic); independent of GO |

### Narrative on the evidence

The processing evidence forms a coherent three-paper mechanistic chain ([PMID: 26919432](https://pubmed.ncbi.nlm.nih.gov/26919432/), [PMID: 34469728](https://pubmed.ncbi.nlm.nih.gov/34469728/), [PMID: 38244197](https://pubmed.ncbi.nlm.nih.gov/38244197/)) that consistently places PRG-1 as the carrier/scaffold of the precursor and PARN-1 as the trimming nuclease. This is the strongest part of the evidence base and cleanly answers whether PRG-1 contributes to processing (it does — via precursor loading and stabilization) versus catalysis (it does not).

The localization evidence uniformly points away from the nucleoplasm. [PMID: 41529195](https://pubmed.ncbi.nlm.nih.gov/41529195/) and [PMID: 33658512](https://pubmed.ncbi.nlm.nih.gov/33658512/) both name perinuclear germ granules; UniProt lists cytoplasm only; the only experimentally supported CC GO term is P granule (IDA). The lone support for nucleus is a phylogenetic IBA inference. [PMID: 41414669](https://pubmed.ncbi.nlm.nih.gov/41414669/) adds that PRG-1 localization is robust even when N-terminal RG motifs are mutated, further underscoring that granule localization is the stable, defining feature of the protein and that downstream silencing (WAGO-siRNA production) is genetically separable from loading/localization.

---

## Mechanistic Scope

**Direct PRG-1 activity:** sequence-specific binding of 21U-RNAs/pre-piRNAs (MF), assembling piRISC in perinuclear P granules (CC). PRG-1 loads the untrimmed precursor and stabilizes it, licensing 3′ maturation.
**Adjacent, non-PRG-1 catalysis:** 5′ processing by PETISCO/PICS + TOFU factors (upstream); 3′ trimming by PARN-1; 2′-O-methylation by HENN-1.
**Downstream (not PRG-1 localization/activity):** target licensing → 22G-RNA amplification (RdRP EGO-1) → nuclear silencing by HRDE-1/NRDE-3. Transposon silencing, fertility loss, transgenerational sterility, and longevity are **loss-of-function phenotypes**, not molecular functions of PRG-1.

---

## Conflicts and Alternatives

- **Paralog/clade carry-over.** Some PIWI-clade proteins in other taxa are nuclear (e.g., mouse MIWI2/PIWIL4; Drosophila Piwi). The IBA "nucleus" call most plausibly propagates that clade property onto PRG-1, which is not experimentally nuclear in *C. elegans* — a classic over-annotation risk. (Used here as orientation for the carry-over argument; those cross-organism primary abstracts were not retrieved in this run and are not cited as retrieved evidence.)
- **"Processing" vs "stabilizing only."** The seed's fork resolves: PRG-1 binds the precursor (pre-piRNA), not only mature piRNA, so its role exceeds passive stabilization — but it does not catalyze trimming (PARN-1 does).
- **Biogenesis is partitioned.** PETISCO/TOFU (5′) act largely upstream/independent of PRG-1, so "piRNA processing" as a whole is not PRG-1-centric.

---

## Limitations and Knowledge Gaps

1. **Is there any bona-fide intranuclear PRG-1 pool?** Checked: QuickGO evidence tiers + all retrieved localization papers → only perinuclear IDA found; no experimental nuclear evidence. Matters because it determines keep/remove for GO:0005634. Resolve with quantitative subcellular fractionation or super-resolution/immuno-EM/APEX imaging distinguishing nucleoplasm from granule.
2. **Does PRG-1 loading constitute a required processing step, or merely precede it?** Checked: PARN-1/HENN-1 papers show trimming on PRG-1-bound precursors. Resolve with in-vitro reconstitution testing whether trimming requires PRG-1 loading.
3. **Term granularity.** Whether curators prefer GO:0034585 (21U) vs GO:0034587 (piRNA) is a nomenclature/consistency decision, not a biology gap.
4. **Provenance timing.** GO evidence tiers reflect a live QuickGO pull (2026-09) and may lag the newest primary literature; a curator should re-pull at curation time. PMIDs 18501605/18571452 were confirmed via QuickGO annotation references rather than re-read in full; their figures should be re-inspected. UniProt location evidence for P90786 is ECO:0000256 (automatic).

---

## Discriminating Tests

- **Cell fractionation / immuno-EM** of endogenously tagged PRG-1: quantify nucleoplasmic vs perinuclear-granule signal (directly tests GO:0005634).
- **In-vitro pre-piRNA trimming ± PRG-1 loading** with recombinant PARN-1: tests whether PRG-1 is a required processing scaffold vs a mere carrier.
- **Small-RNA-seq in *parn-1*, *henn-1*, *prg-1*, and PETISCO/TOFU mutants:** partitions PRG-1's contribution (loading/3′) from 5′ biogenesis.
- **Curator audit of the GO_Central IBA reference tree** for the PIWI clade to identify which ortholog(s) seeded the nucleus propagation and whether they have experimental nuclear support.

---

## Proposed Follow-up Actions / Curation Leads (verify before applying)

**Reference snippets to verify:**
- [PMID: 41529195](https://pubmed.ncbi.nlm.nih.gov/41529195/) — "the failure to load piRNAs disrupts PRG-1 localization to **perinuclear germ granules**."
- [PMID: 26919432](https://pubmed.ncbi.nlm.nih.gov/26919432/) — untrimmed piRNAs "are stable and **associate with the Piwi protein PRG-1** but fail to robustly recruit downstream silencing factors."
- [PMID: 34469728](https://pubmed.ncbi.nlm.nih.gov/34469728/) — "**long isoforms of untrimmed piRNAs are preferentially modified in parn-1 mutant animals**."
- [PMID: 38244197](https://pubmed.ncbi.nlm.nih.gov/38244197/) — "The ribonuclease **PARN-1** and its orthologs **mediate piRNA 3′ trimming** in worms, insects, and mammals."
- [PMID: 41414669](https://pubmed.ncbi.nlm.nih.gov/41414669/) — RG motifs "are not required for PRG-1 **expression, localization, or piRNA loading**."

**Candidate GO actions:**
- **Demote/remove GO:0005634 (nucleus, IBA-only)** — do not treat as a core direct-localization annotation.
- **Retain GO:0043186 (P granule, IDA)** as the primary CC and GO:0005737 (cytoplasm).
- **Prefer/promote GO:0034585 (21U-RNA metabolic process, IMP)**; if GO:0034587 (piRNA processing) is kept, frame it as non-catalytic participation (loading/scaffolding) with PARN-1 as the catalytic partner.
- **Retain GO:0034583/0034584 (21U/piRNA binding)** as the informative MF; do not fall back to "protein binding."

**Suggested curator questions:**
- Is any experimental nuclear-localization citation on file that would upgrade GO:0005634 beyond IBA?
- Should the review explicitly annotate PRG-1's processing role as *precursor loading/scaffolding* (non-catalytic) with PARN-1 named as the catalytic partner?

**Suggested experiments:** fractionation/imaging for a nuclear pool; in-vitro trimming ± PRG-1 loading; comparative small-RNA-seq across the maturation-pathway mutants above.

---

### Bottom line

Split the hypothesis. **Keep** the piRNA-processing participation (best expressed as the experimentally grounded 21U-RNA metabolic process term, with PRG-1 as non-catalytic scaffold/stabilizer and PARN-1 as the trimming nuclease). **Flag/demote** the nucleus localization as PIWI-clade IBA carry-over that conflicts with direct IDA P-granule evidence and UniProt's cytoplasm-only curated location. Perinuclear germ granules are cytoplasm-facing — they are not the nucleus.


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)
- [OpenScientist prg1 current go annotations](openscientist_artifacts/prg1_current_go_annotations.csv)
- [OpenScientist prg1 evidence matrix](openscientist_artifacts/prg1_evidence_matrix.csv)
- [OpenScientist prg1 go decision table](openscientist_artifacts/prg1_go_decision_table.csv)