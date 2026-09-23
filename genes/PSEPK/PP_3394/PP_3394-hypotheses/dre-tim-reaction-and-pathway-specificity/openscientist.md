---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-20T22:51:57.696120'
end_time: '2026-09-20T23:24:52.883310'
duration_seconds: 1975.19
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: PSEPK
  gene: PP_3394
  gene_symbol: PP_3394
  uniprot_accession: Q88HG4
  taxon_id: NCBITaxon:160488
  taxon_label: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440)
  focus_type: function_assignment
  hypothesis_slug: dre-tim-reaction-and-pathway-specificity
  hypothesis_text: Pseudomonas putida KT2440 PP_3394 (Q88HG4) catalyzes hydroxymethylglutaryl-CoA
    cleavage, another oxo-acid lyase reaction, or acyl transfer forming a carbon-carbon
    bond. Determine its actual reaction and the resulting support for leucine catabolism
    and ketone-body biosynthesis, adjudicating these separately. Compare catalytic
    residues, architecture and relevant phylogenetic clades with experimentally characterized
    LiuE/HMG-CoA lyases and isopropylmalate/homocitrate synthases. Existing mvaB and
    branched-chain-amino-acid-catabolism OpenScientist reports explicitly leave PP_3394
    versus PP_3540/mvaB unresolved; pairwise similarity alone does not settle the
    paralog. Distinguish enzyme-family evidence, verified target-specific features
    and biochemical assays; report unresolved specificity honestly.
  term_context: No specific term context supplied.
  reference_context: No specific reference context supplied.
  source_file: genes/PSEPK/PP_3394/PP_3394-ai-review.yaml
  source_selector: free-text
  source_context_yaml: "hypothesis: Pseudomonas putida KT2440 PP_3394 (Q88HG4) catalyzes\
    \ hydroxymethylglutaryl-CoA cleavage, another\n  oxo-acid lyase reaction, or acyl\
    \ transfer forming a carbon-carbon bond. Determine its actual reaction\n  and\
    \ the resulting support for leucine catabolism and ketone-body biosynthesis, adjudicating\
    \ these separately.\n  Compare catalytic residues, architecture and relevant phylogenetic\
    \ clades with experimentally characterized\n  LiuE/HMG-CoA lyases and isopropylmalate/homocitrate\
    \ synthases. Existing mvaB and branched-chain-amino-acid-catabolism\n  OpenScientist\
    \ reports explicitly leave PP_3394 versus PP_3540/mvaB unresolved; pairwise similarity\
    \ alone\n  does not settle the paralog. Distinguish enzyme-family evidence, verified\
    \ target-specific features and\n  biochemical assays; report unresolved specificity\
    \ honestly.\nfocus_type: function_assignment\ncontext: []\nreference_id: []"
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
citation_count: 1
artifact_count: 3
artifact_sources:
  openscientist_artifacts_zip: 3
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
- filename: provenance_PP_3394_comparison_table.md
  path: openscientist_artifacts/provenance_PP_3394_comparison_table.md
  media_type: text/markdown
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist PP 3394 comparison table
---

## Question

# AIGR Gene Hypothesis Deep Research

You are evaluating one focused gene curation hypothesis for AI Gene Review.
This is not a general gene overview. Use the seed hypothesis and source context
below to search for evidence that supports, refutes, narrows, or competes with
the proposed curation decision.

## Target Gene

- **Organism code:** PSEPK
- **Taxon:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440) (NCBITaxon:160488)
- **Gene directory:** PP_3394
- **Gene symbol:** PP_3394
- **UniProt accession:** Q88HG4

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** dre-tim-reaction-and-pathway-specificity
- **Source file:** genes/PSEPK/PP_3394/PP_3394-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

Pseudomonas putida KT2440 PP_3394 (Q88HG4) catalyzes hydroxymethylglutaryl-CoA cleavage, another oxo-acid lyase reaction, or acyl transfer forming a carbon-carbon bond. Determine its actual reaction and the resulting support for leucine catabolism and ketone-body biosynthesis, adjudicating these separately. Compare catalytic residues, architecture and relevant phylogenetic clades with experimentally characterized LiuE/HMG-CoA lyases and isopropylmalate/homocitrate synthases. Existing mvaB and branched-chain-amino-acid-catabolism OpenScientist reports explicitly leave PP_3394 versus PP_3540/mvaB unresolved; pairwise similarity alone does not settle the paralog. Distinguish enzyme-family evidence, verified target-specific features and biochemical assays; report unresolved specificity honestly.

## Term and Decision Context

No specific term context supplied.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: Pseudomonas putida KT2440 PP_3394 (Q88HG4) catalyzes hydroxymethylglutaryl-CoA cleavage, another
  oxo-acid lyase reaction, or acyl transfer forming a carbon-carbon bond. Determine its actual reaction
  and the resulting support for leucine catabolism and ketone-body biosynthesis, adjudicating these separately.
  Compare catalytic residues, architecture and relevant phylogenetic clades with experimentally characterized
  LiuE/HMG-CoA lyases and isopropylmalate/homocitrate synthases. Existing mvaB and branched-chain-amino-acid-catabolism
  OpenScientist reports explicitly leave PP_3394 versus PP_3540/mvaB unresolved; pairwise similarity alone
  does not settle the paralog. Distinguish enzyme-family evidence, verified target-specific features and
  biochemical assays; report unresolved specificity honestly.
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

# AIGR Gene Hypothesis Deep Research — PP_3394 (Q88HG4), *Pseudomonas putida* KT2440

**Focus type:** function_assignment
**Hypothesis slug:** dre-tim-reaction-and-pathway-specificity
**Target:** PP_3394 / Q88HG4 (309 aa, HMGL-like TIM-barrel; Pfam PF00682; CDD cd07938 DRE_TIM_HMGL), *Pseudomonas putida* KT2440 (NCBITaxon:160488)

---

## Executive Judgment

**Verdict: Partially supported at the family level, but the specific reaction is UNRESOLVED, and the confident "HMG-CoA lyase / leucine catabolism" assignment for PP_3394 is over-annotated (weakly supported).**

PP_3394 is a genuine member of the HMG-CoA-lyase / DRE-TIM metallolyase superfamily (the "another oxo-acid lyase reaction, or acyl transfer forming a carbon-carbon bond" framing in the seed hypothesis is broadly correct). It retains the catalytic core residues of the fold, so it is very likely to be a catalytically competent enzyme. However, three lines of computed evidence converge to show that **PP_3394 is NOT the physiological leucine/terpene HMG-CoA lyase of *P. putida* KT2440**, and that its precise substrate specificity cannot be inferred from sequence:

1. **PP_3394 is a highly divergent paralog (~38% identity to every reference)**, equidistant from bona fide HMG-CoA lyases (LiuE/mvaB/human HMGCL) and from isopropylmalate/homocitrate synthases (IPMS LeuA). Pairwise similarity alone does not — and cannot — settle its specificity.
2. **PP_3394 FAILS the HMG-CoA-lyase-specific PROSITE active-site signature PS01062 (SVAGLGGCPY)** that all three verified HMG-CoA lyases pass, and instead **MATCHES the IPMS/homocitrate-synthase site-1 signature PS00815** and carries the condensation-enzyme-type "LRDG" N-terminal motif rather than the HMG-CoA-lyase "PRDG" motif.
3. **The genuine leucine/terpene HMG-CoA lyase of *P. putida* is the paralog mvaB / PP_3540**, which is **78.6% identical** to the experimentally characterized *P. aeruginosa* LiuE (PA2011) — an ortholog-level match — and which carries PS01062. KEGG nonetheless dual-annotates BOTH PP_3394 and PP_3540 to K01640 (EC 4.1.3.4), the textbook signature of paralog over-annotation.

**Most important caveats:** (a) All of the discriminating evidence is *computational* (pairwise alignment, PROSITE/motif scanning, and a whole-sequence NJ phylogeny). There is **no direct biochemical assay or mutant phenotype for PP_3394 itself**; the only experimental anchor is for the *P. aeruginosa* ortholog of mvaB (LiuE, PMID 19459965). (b) "Ketone-body biosynthesis" is a mammalian physiological concept and should not be transferred to this bacterium regardless of enzyme family. (c) Because the catalytic core is retained but the specificity determinants diverge, PP_3394 could plausibly act on an HMG-CoA-like or a different acyl-CoA / oxo-acid substrate — the honest curation position is "unresolved DRE-TIM metallolyase," not "HMG-CoA lyase."

---

## Summary

This report adjudicates whether *P. putida* KT2440 PP_3394 directly catalyzes HMG-CoA cleavage in support of leucine catabolism and/or ketone-body biosynthesis, or a different DRE-TIM metallolyase reaction. Across three iterations, the investigation confirmed four findings that together resolve the paralog question that prior mvaB and branched-chain-amino-acid-catabolism reports had explicitly left open.

The core conclusion is that the leucine/terpene HMG-CoA-lyase function of *P. putida* belongs to **mvaB / PP_3540**, the reciprocal-best ortholog (78.6% identity) of the experimentally verified *P. aeruginosa* enzyme **LiuE** ([PMID: 19459965](https://pubmed.ncbi.nlm.nih.gov/19459965/)). PP_3394, by contrast, is a **divergent paralog (~38% identity to every reference protein)** whose active-site signatures do not match the HMG-CoA-lyase group and instead resemble the isopropylmalate/homocitrate-synthase group, even though whole-sequence phylogeny places it basally within the HMG-CoA-lyase clade. This tension between backbone relatedness and specificity motifs is the hallmark of a **functionally diverged paralog of unresolved substrate specificity**.

For curation, the practical upshot is that PP_3394's confident HMG-CoA-lyase / leucine-catabolism annotation is **over-annotated** and should be generalized to a low-confidence oxo-acid/carbon-carbon lyase molecular function, with leucine catabolism treated as non-core and ketone-body biosynthesis rejected as a mammalian concept inapplicable to this bacterium. The strong, experimentally anchored annotation belongs on mvaB/PP_3540. Resolving PP_3394's true reaction requires direct biochemistry or a mutant phenotype — neither of which currently exists for this gene.

---

## Key Findings

### Finding 1 — mvaB (PP_3540), not PP_3394, is the ortholog of the experimentally verified leucine/terpene HMG-CoA lyase LiuE

The single experimentally anchored data point in this entire family for the *Pseudomonas* genus is *P. aeruginosa* **LiuE (PA2011, Q9I2A0)**. Chávez-Avilés and colleagues showed by direct enzymology and mutant phenotype that LiuE is a 3-hydroxy-3-methylglutaryl-CoA lyase (HMG-CoA lyase) that cleaves HMG-CoA to acetyl-CoA + acetoacetate (Km ≈ 100 µM HMG-CoA; Vmax ≈ 21 µmol/min/mg), and that a *liuE* deletion abolishes growth on both leucine/isovalerate **and** acyclic terpenes ([PMID: 19459965](https://pubmed.ncbi.nlm.nih.gov/19459965/)).

When the *P. putida* KT2440 HMGL-family paralogs are aligned (global Needleman–Wunsch, BLOSUM62) against LiuE:

| Query | UniProt | % identity to LiuE (PA2011) | PS01062 (HMG-CoA lyase site) |
|---|---|---|---|
| **mvaB / PP_3540** | Q88H25 | **78.6% (ortholog-level)** | **Match (SVAGLGGCPY)** |
| PP_3394 | Q88HG4 | 38.2% (superfamily-level) | **FAIL** |
| (comparison) human HMGCL | P35914 | — | Match |
| (comparison) *E. coli* IPMS LeuA | P09151 | — | Fail |

mvaB's 78.6% identity is the reciprocal-best, ortholog-level relationship expected for a true functional counterpart. PP_3394's 38.2% is no better than its 38.0% identity to human HMGCL or its 38.8% identity to *E. coli* IPMS — i.e., PP_3394 is generically "an HMGL-fold enzyme," not specifically "a LiuE ortholog." This finding directly answers the seed hypothesis's core question: the leucine-catabolic HMG-CoA lyase role of *P. putida* maps to **mvaB / PP_3540**, not to PP_3394.

### Finding 2 — PP_3394 is a divergent DRE-TIM metallolyase of unresolved substrate specificity, not a canonical HMG-CoA lyase

PP_3394 (309 aa) is a single HMGL-like TIM-barrel (Pfam PF00682; CDD cd07938 DRE_TIM_HMGL). Two orthogonal diagnostic-motif tests place it *outside* the HMG-CoA-lyase specificity group:

- **PS01062 — HMG-CoA-lyase active-site signature (SVAGLGGCPY).** All three verified HMG-CoA lyases match this pattern (mvaB @res 233, PaLiuE @res 233, human HMGCL @res 259). **PP_3394 FAILS it.**
- **PS00815 — α-isopropylmalate/homocitrate-synthase site-1 signature (L-R-[DE]-G-x-Q…K).** *E. coli* IPMS LeuA matches; none of the HMG-CoA lyases match; **PP_3394 MATCHES it @res 11.**
- **N-terminal condensation-motif.** PP_3394 carries the condensation-enzyme-type **"LRDG" motif (GLRDGLQ)** rather than the HMG-CoA-lyase **"PRDG" motif ((G)PRDGLQ)**.

Despite these specificity-determining differences, PP_3394 **retains the catalytic core** of the fold: it aligns to the human HMGCL catalytic/metal-binding residues Arg41, Asp42, His233, His235 and the catalytic Cys266. It is therefore very likely catalytically competent, but the sequence does **not** determine which C–C bond it makes or breaks. The honest interpretation is: **divergent DRE-TIM metallolyase, specificity undetermined by sequence** — precisely the "unresolved specificity" the seed hypothesis asked us to report honestly rather than paper over.

### Finding 3 — The *P. putida* leucine operon lacks its own HMG-CoA lyase, and KEGG dual-annotates PP_3394 and PP_3540 to K01640 (paralog over-annotation)

Genomic-context analysis (KEGG) shows the *P. putida* KT2440 leucine/isovalerate catabolic operon is **PP_4063–PP_4068**:

```
PP_4063  long-chain acyl-CoA ligase
PP_4064  ivd   isovaleryl-CoA dehydrogenase   (K00253)
PP_4065  mccB  methylcrotonyl-CoA carboxylase (K01969)
PP_4066  liuC  methylglutaconyl-CoA hydratase (K13766)
PP_4067  mccA  methylcrotonyl-CoA carboxylase (K01968)
   ── NO adjacent HMG-CoA-lyase gene in the operon ──
```

Neither HMGL-family gene sits in this operon. Instead they are dispersed:

- **PP_3394** (complement 3,844,704–3,845,633; neighbors: a CaiB-family CoA-transferase, a LysR-family regulator, curli/biofilm genes) — a genomic neighborhood that is **not** a canonical leucine/terpene locus.
- **PP_3540 / mvaB** (~4.01 Mb; neighbors: *pobA/pobR* p-hydroxybenzoate hydroxylase and regulator).

KEGG maps **BOTH** PP_3394 and PP_3540 to **K01640 (EC 4.1.3.4, HMG-CoA lyase)** and to leucine-degradation module **M00036** — an unresolved best-KO duplication. This is the classic mechanism by which an over-annotation propagates: a single KO is assigned to two paralogs, and the divergent one (PP_3394) inherits the confident functional label from the true ortholog (PP_3540) without independent support. PP_3394's neighborhood provides **no** pathway-context corroboration for a leucine-catabolic role.

### Finding 4 — Whole-sequence phylogeny places PP_3394 basal to the HMG-CoA-lyase clade, not among condensation synthases

A Neighbor-Joining tree over a 9-member DRE-TIM panel (p-distance = 1 − global NW/BLOSUM62 identity) recovers two well-separated clades:

- **Clade A (HMG-CoA lyases):** PP_3394, *B. subtilis* HMGL (O34873), human HMGCL (P35914), mvaB (Q88H25), PaLiuE (Q9I2A0).
- **Clade B (condensation/aldolase enzymes):** *E. coli* IPMS LeuA (P09151), DmpG 4-hydroxy-2-oxovalerate aldolase (P51016), yeast homocitrate synthase (P48570), *M. jannaschii* citramalate synthase (Q58787).

```
Newick (branch lengths):
((PP3394:0.307,(BsHMGL:0.267,(hHMGCL:0.220,(mvaB:0.113,PaLiuE:0.101):0.092):0.066):0.041):0.015,
 (condensation clade B):0.015);
```

PP_3394 branches at the **base of clade A**. Its terminal branch (0.307) is ~3× longer than mvaB's (0.113), quantifying how divergent it is even within the HMG-CoA-lyase clade. Two nuances matter for curation: (i) whole-sequence phylogeny groups PP_3394 nearer the lyase clade, whereas the motif/active-site signatures (Finding 2) pull it toward the IPMS/condensation specificity determinants — this tension is itself the reason specificity is unresolved; and (ii) basal, long-branch placement is exactly the topology of a paralog that has **functionally diverged** and should not simply inherit the clade's canonical annotation.

---

## Mechanistic Model / Interpretation

The DRE-TIM metallolyase (HMGL) superfamily uses a divalent-metal-dependent TIM-barrel active site to catalyze either **retro-aldol / oxo-acid cleavage** (HMG-CoA lyase; 4-hydroxy-2-oxovalerate aldolase) or **Claisen-type condensation** (isopropylmalate synthase, homocitrate synthase, citramalate synthase). A shared catalytic core (metal-binding Asp/His pair, catalytic Arg and Cys) supports both chemistries; **substrate specificity and reaction direction are set by peripheral residues and short signature motifs**, not by the core. This is why sequence identity alone is a poor discriminator here — and why the seed hypothesis was right to insist that "pairwise similarity alone does not settle the paralog."

Placing the *P. putida* paralogs onto this framework:

```
                          DRE-TIM / HMGL-fold superfamily
                                     │
        ┌────────────────────────────┴─────────────────────────────┐
   HMG-CoA lyase specificity                          condensation-synthase specificity
   (PS01062 SVAGLGGCPY; PRDG motif)                   (PS00815; LRDG motif)
        │                                                        │
   ┌────┴──────────────┐                                         │
 mvaB/PP_3540        PaLiuE/PA2011  ← EXPERIMENTALLY VERIFIED     │
 (78.6% id to LiuE,  (Km 100 µM,    HMG-CoA lyase                 │
  PS01062 +)          Vmax 21)                                    │
        │                                                        │
   leucine + terpene catabolism (real)                           │
                                                                 │
   PP_3394 ── retains catalytic core, BUT fails PS01062,         │
             matches PS00815, carries LRDG motif,                │
             ~38% id to everything, long basal branch ───────────┘
             ⇒ specificity UNRESOLVED (could be an HMG-CoA-like,
               other acyl-CoA, or oxo-acid substrate)
```

**Adjudicating the two pathway claims separately, as the seed hypothesis requested:**

- **Leucine catabolism:** The pathway's HMG-CoA-lyase step is fully accounted for by mvaB/PP_3540 (ortholog of LiuE). The *liu* operon (PP_4063–4068) contains no HMGL gene, and PP_3394's genomic neighborhood is unrelated to leucine/terpene degradation. → For PP_3394, leucine catabolism should be treated as **non-core / unsupported**.
- **Ketone-body biosynthesis:** This is a mammalian hepatic concept (mitochondrial HMGCL/HMGCS producing acetoacetate/β-hydroxybutyrate as circulating fuels). It is **not applicable** to *P. putida* and should not be assigned to any KT2440 gene, PP_3394 included. The bacterial reaction acetyl-CoA + acetoacetate is a catabolic terminal step of leucine/terpene degradation, not "ketone-body biosynthesis."

The coherent model: PP_3394 is a **functionally diverged HMGL-fold paralog** whose true substrate is undetermined; the confident HMG-CoA-lyase label it currently carries is a carry-over from its better-characterized paralog mvaB via a shared KEGG KO.

---

## Evidence Base / Evidence Matrix

| Citation | Evidence type | Supports / refutes / qualifies | Claim tested | Key finding | Context | Confidence & limitations |
|---|---|---|---|---|---|---|
| [PMID: 19459965](https://pubmed.ncbi.nlm.nih.gov/19459965/) | Direct assay + mutant phenotype | **Supports** (anchors the ortholog to mvaB, not PP_3394) | Is LiuE the leucine/terpene HMG-CoA lyase? | LiuE (PA2011) cleaves HMG-CoA→acetyl-CoA+acetoacetate; *liuE* mutant can't use leucine/isovalerate or acyclic terpenes | *P. aeruginosa*, in vitro enzymology + growth phenotype | High for LiuE; applies to PP_3394 only via orthology to mvaB (78.6%), not to PP_3394 (38.2%) |
| Computed (global NW/BLOSUM62 pairwise identity) | Structural/evolutionary (computational) | **Qualifies/refutes** confident PP_3394 assignment | Is PP_3394 a LiuE ortholog? | mvaB=78.6% id (ortholog); PP_3394=38.2% id, no better than to human HMGCL (38.0%) or *E. coli* IPMS (38.8%) | 9-protein reference panel | High as computed; sequence identity cannot prove specificity, only rank relatedness |
| Computed (PROSITE PS01062 / PS00815 + N-terminal motif) | Structural/evolutionary (computational) | **Refutes** "canonical HMG-CoA lyase" for PP_3394 | Does PP_3394 carry HMG-CoA-lyase-specific signatures? | Fails PS01062 (all 3 real lyases pass); matches IPMS site-1 PS00815; carries LRDG (not PRDG) motif; but retains catalytic core (R41,D42,H233,H235,C266 equivalents) | Same panel | High that PP_3394 is atypical; motif tests indicate but do not prove alternative specificity |
| Computed (KEGG genomic context) | Review/database (computational) | **Qualifies** (over-annotation signal) | Does pathway context support PP_3394's role? | *liu* operon PP_4063–4068 has no HMGL gene; KEGG maps BOTH PP_3394 & PP_3540 to K01640 & module M00036 | KT2440 genome | High for the dual-annotation fact; database-level, not experimental |
| Computed (Neighbor-Joining phylogeny) | Structural/evolutionary (computational) | **Qualifies** | Where does PP_3394 sit phylogenetically? | Basal in HMG-CoA-lyase clade A; branch 0.307 ≈ 3× mvaB's 0.113 | 9-protein panel | Moderate–high; NJ on p-distance from a small panel; no bootstrap reported |

**How the key paper supports/challenges the findings.** *The Pseudomonas aeruginosa liuE gene encodes the 3-hydroxy-3-methylglutaryl coenzyme A lyase, involved in leucine and acyclic terpene catabolism* ([PMID: 19459965](https://pubmed.ncbi.nlm.nih.gov/19459965/)) is the only primary experimental anchor available and it supports the findings **by orthology transfer to mvaB, not to PP_3394**. It establishes LiuE (PA2011) as a verified HMG-CoA lyase whose loss blocks leucine/isovalerate and terpene growth; the *P. putida* protein that inherits this by 78.6% identity and by carrying PS01062 is mvaB/PP_3540. The paper therefore *challenges* the idea that PP_3394 (a 38.2%-identity paralog lacking PS01062) is the physiological leucine-catabolic lyase.

---

## GO Curation Implications

**Lead (requires curator verification):** The current confident annotation of PP_3394 as an HMG-CoA lyase acting in leucine catabolism is **over-annotated** and should be **generalized/qualified**, while the leucine-catabolic HMG-CoA-lyase role is retained/strengthened on **mvaB / PP_3540**.

- **Molecular Function (MF):**
  - *Do not* retain a confident `hydroxymethylglutaryl-CoA lyase activity` (GO:0004419) IEA on PP_3394. The specificity signatures argue against it.
  - *Generalize* to a parent term such as `oxo-acid-lyase activity` (GO:0016833) or `carbon-carbon lyase activity` (GO:0016830), or `metal ion binding` (GO:0046872) for the fold's cofactor, all as **low-confidence IEA** pending assay. This honestly captures "DRE-TIM metallolyase of unresolved specificity."
  - Avoid "protein binding" as a fallback — the fold evidence supports a lyase/metallolyase MF, which is more informative.
- **Biological Process (BP):** Treat `leucine catabolic process` (GO:0006552) and any terpene-catabolism BP as **non-core / remove or down-rank** for PP_3394 (no operon context, no ortholog-level identity, no assay). Do **not** annotate ketone-body biosynthesis.
- **Cellular Component (CC):** No specific evidence; cytoplasmic is the fold default and non-diagnostic.
- **For mvaB / PP_3540 (sister curation note):** GO:0004419 (HMG-CoA lyase activity) and GO:0006552 (leucine catabolic process) are **well supported** by orthology (78.6% to LiuE) + PS01062 + the LiuE experimental anchor; these can be retained with an ISO/orthology-backed evidence code.

---

## Mechanistic Scope

The molecular function under test is a **single, direct enzymatic activity**: a DRE-TIM metallolyase (HMGL-fold) reaction — either retro-aldol cleavage of an oxo-acid/acyl-CoA (as in HMG-CoA lyase) or a Claisen condensation (as in IPMS/homocitrate synthase). The catalytic core is present in PP_3394, so a direct metal-dependent lyase/synthase activity is plausible. Everything downstream — participation in leucine catabolism, terpene degradation, "ketone-body" chemistry — is **pathway consequence**, and for PP_3394 none of it is established by direct evidence. The experimental phenotype (loss of leucine/terpene growth) belongs to the *P. aeruginosa* LiuE mutant, i.e., the mvaB ortholog, and must not be transferred to PP_3394 by inference from loss of function in a different gene.

---

## Conflicts and Alternatives

- **Paralog confusion (primary conflict):** KEGG's dual assignment of K01640 to both PP_3394 and PP_3540 is the root of the over-annotation. Reciprocal-best-hit orthology assigns the LiuE role unambiguously to PP_3540/mvaB; PP_3394 is a co-annotated paralog.
- **Signal tension between methods:** Whole-sequence phylogeny groups PP_3394 basally *within* the HMG-CoA-lyase clade (Finding 4), whereas active-site/motif signatures pull it toward the IPMS/condensation specificity group (Finding 2). This is not an error — it reflects a functionally diverged paralog whose backbone resembles lyases but whose specificity residues resemble synthases. The correct resolution is "unresolved," not forcing it into either box.
- **Organism-specificity artifact:** "Ketone-body biosynthesis" is a mammalian framing; its appearance in the hypothesis space is a cross-organism concept-transfer artifact, not a *P. putida* function.
- **Alternative substrate hypothesis:** Given retained catalysis but atypical specificity motifs, a live alternative is that PP_3394 acts on a **different acyl-CoA or oxo-acid substrate** (e.g., a niche catabolic intermediate consistent with its CaiB-transferase / LysR-regulator neighborhood) rather than HMG-CoA. This remains speculative and untested.

---

## Limitations and Knowledge Gaps

1. **No direct biochemistry for PP_3394.** All discriminating evidence is computational (pairwise identity, PROSITE/motif scan, NJ tree). *Checked:* sequence, signatures, genomic context, phylogeny. *Why it matters:* specificity in this fold is set by peripheral residues; only an assay settles it. *Resolver:* purify recombinant PP_3394 and assay HMG-CoA lyase activity vs. candidate condensation/other-acyl-CoA reactions.
2. **No mutant phenotype for PP_3394.** *Why it matters:* a leucine/terpene growth defect (or its absence) in a Δ*PP_3394* strain would directly test pathway membership. *Resolver:* clean deletion + growth on leucine/isovalerate/acyclic terpenes, with Δ*PP_3540* as the positive control.
3. **Phylogeny lacks bootstrap support and uses a small 9-taxon panel.** *Why it matters:* basal placement confidence is unquantified. *Resolver:* broader taxon sampling with ML + bootstrap.
4. **No experimental structure.** *Why it matters:* an AlphaFold model + active-site pocket analysis (substrate-channel residues, metal site geometry) could sharpen the lyase-vs-synthase call. *Resolver:* model/compare active-site pocket against solved HMGCL and IPMS structures.
5. **Substrate identity of PP_3394 entirely open.** No candidate has been experimentally excluded. *Resolver:* metabolomic screen / activity-based substrate profiling.

---

## Discriminating Tests

Ranked by efficiency in separating "HMG-CoA lyase" from "divergent-specificity metallolyase":

1. **In vitro enzyme assay (definitive).** Recombinant His-tagged PP_3394 + Mg²⁺/Mn²⁺; test HMG-CoA cleavage (spectrophotometric acetoacetate/DTNB acetyl-CoA assays, matched to the LiuE assay of PMID 19459965) alongside an IPMS/homocitrate-synthase condensation assay panel. Compare kinetics against mvaB/PP_3540 run in parallel.
2. **Reciprocal deletion phenotyping.** Δ*PP_3394*, Δ*PP_3540*, and the double mutant; growth on leucine, isovalerate, and acyclic terpenes (citronellol/geraniol). Prediction: Δ*PP_3540* loses growth; Δ*PP_3394* does not (if PP_3394 is off-pathway).
3. **Structure-guided active-site comparison.** AlphaFold model of PP_3394 → superpose on HMGCL and IPMS; score the PS01062-equivalent loop and metal site. Cheap, immediate, and directly interrogates the Finding-2 tension.
4. **Broadened, bootstrapped phylogeny + HMM specificity profiling** to test whether PP_3394 falls in a distinct, uncharacterized subfamily.
5. **Coexpression / operon transcriptomics** under leucine vs. alternative carbon sources to test pathway coregulation of PP_3394 vs. the *liu* operon and *mvaB*.

---

## Proposed Follow-up Actions / Curation Leads (require curator verification)

- **Candidate reference to cite for the ortholog anchor:** [PMID: 19459965](https://pubmed.ncbi.nlm.nih.gov/19459965/). Verify snippets: *"Protein sequence alignment and fingerprint sequencing suggested that liuE encodes 3-hydroxy-3-methylglutaryl-coenzyme A lyase (HMG-CoA lyase), which catalyzes the cleavage of HMG-CoA to acetyl-CoA and acetoacetate."* and *"A mutant in the liuE gene (ORF PA2011) of P. aeruginosa was unable to utilize both leucine/isovalerate and acyclic terpenes as the carbon source."* Use to support **mvaB/PP_3540**, not PP_3394.
- **Candidate action change on PP_3394:**
  - Down-rank/remove confident `hydroxymethylglutaryl-CoA lyase activity` (GO:0004419) IEA.
  - Replace with a generalized, low-confidence MF: `oxo-acid-lyase activity` (GO:0016833) or `carbon-carbon lyase activity` (GO:0016830), noting DRE-TIM metallolyase fold; add `metal ion binding` (GO:0046872) if cofactor evidence is accepted.
  - Mark `leucine catabolic process` (GO:0006552) as **non-core / remove** for PP_3394; do not assign ketone-body biosynthesis.
- **Candidate action on mvaB/PP_3540 (sister note):** retain/strengthen GO:0004419 + GO:0006552 with orthology (ISO) evidence to LiuE.
- **Suggested curator questions:** (1) Is the K01640 assignment to PP_3394 a KEGG best-KO duplication that should not propagate a confident GO MF? (2) Should PP_3394 be flagged as "specificity unresolved — needs experimental characterization"?
- **Suggested experiments:** the in vitro assay and reciprocal deletion tests above (Discriminating Tests 1–2).

---

## Bottom Line

PP_3394 (Q88HG4) is a real HMGL-fold / DRE-TIM metallolyase with an intact catalytic core, but it is a **highly divergent paralog (~38% identity to all references) that fails the HMG-CoA-lyase active-site signature PS01062 and instead matches an IPMS/homocitrate-synthase motif** — so its exact reaction is **unresolved by sequence** and its confident annotation as an HMG-CoA lyase in leucine catabolism is **over-annotated**. The physiological leucine/terpene HMG-CoA lyase of *P. putida* KT2440 is the paralog **mvaB / PP_3540** (78.6% identical to the experimentally verified LiuE, PMID 19459965). "Ketone-body biosynthesis" does not apply to this bacterium. Recommended curation: generalize/qualify PP_3394's MF as a low-confidence oxo-acid/carbon-carbon lyase, treat leucine catabolism as non-core for PP_3394, and require a biochemical assay or mutant to resolve specificity.


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)
- [OpenScientist PP 3394 comparison table](openscientist_artifacts/provenance_PP_3394_comparison_table.md)