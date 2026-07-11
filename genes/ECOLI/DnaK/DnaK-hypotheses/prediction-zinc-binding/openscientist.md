---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-10T03:17:31.359431'
end_time: '2026-07-10T03:28:43.768333'
duration_seconds: 672.41
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: ECOLI
  gene: DnaK
  gene_symbol: DnaK
  uniprot_accession: P0A6Y8
  taxon_id: NCBITaxon:83333
  taxon_label: Escherichia coli (strain K12)
  focus_type: computational_prediction
  hypothesis_slug: prediction-zinc-binding
  hypothesis_text: BioReason-Pro SFT predicts zinc ion binding (GO:0008270) for the
    Escherichia coli chaperone DnaK (P0A6Y8). Independently assess whether DnaK --
    an Hsp70-family chaperone with an N-terminal nucleotide-binding domain (NBD) and
    a C-terminal substrate-binding domain (SBD) -- contains a zinc-binding motif or
    coordinating site, or whether it lacks any zinc center (the zinc-finger of the
    DnaK/DnaJ chaperone system belongs to the co-chaperone DnaJ, not DnaK), which
    would make the zinc-ion-binding prediction a misassignment. Determine whether
    the prediction is supported or refuted.
  term_context: '- Term: zinc ion binding (GO:0008270)'
  reference_context: '- doi:10.64898/2026.03.19.712954'
  source_file: ''
  source_selector: ''
  source_context_yaml: "hypothesis: BioReason-Pro SFT predicts zinc ion binding (GO:0008270)\
    \ for the Escherichia coli chaperone\n  DnaK (P0A6Y8). Independently assess whether\
    \ DnaK -- an Hsp70-family chaperone with an N-terminal nucleotide-binding\n  domain\
    \ (NBD) and a C-terminal substrate-binding domain (SBD) -- contains a zinc-binding\
    \ motif or coordinating\n  site, or whether it lacks any zinc center (the zinc-finger\
    \ of the DnaK/DnaJ chaperone system belongs\n  to the co-chaperone DnaJ, not DnaK),\
    \ which would make the zinc-ion-binding prediction a misassignment.\n  Determine\
    \ whether the prediction is supported or refuted.\nfocus_type: computational_prediction\n\
    term_id: GO:0008270\nterm_label: zinc ion binding\ncontext: []\nreference_id:\n\
    - doi:10.64898/2026.03.19.712954"
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
artifact_count: 4
artifact_sources:
  openscientist_artifacts_zip: 4
artifacts:
- filename: artifacts_evidence_matrix.csv
  path: openscientist_artifacts/artifacts_evidence_matrix.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist evidence matrix
- filename: artifacts_hsp70_cysteine_census.csv
  path: openscientist_artifacts/artifacts_hsp70_cysteine_census.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist hsp70 cysteine census
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

- **Organism code:** ECOLI
- **Taxon:** Escherichia coli (strain K12) (NCBITaxon:83333)
- **Gene directory:** DnaK
- **Gene symbol:** DnaK
- **UniProt accession:** P0A6Y8

## Focus

- **Focus type:** computational_prediction
- **Hypothesis slug:** prediction-zinc-binding
- **Source file:** 
- **Source selector:** 

## Seed Hypothesis

BioReason-Pro SFT predicts zinc ion binding (GO:0008270) for the Escherichia coli chaperone DnaK (P0A6Y8). Independently assess whether DnaK -- an Hsp70-family chaperone with an N-terminal nucleotide-binding domain (NBD) and a C-terminal substrate-binding domain (SBD) -- contains a zinc-binding motif or coordinating site, or whether it lacks any zinc center (the zinc-finger of the DnaK/DnaJ chaperone system belongs to the co-chaperone DnaJ, not DnaK), which would make the zinc-ion-binding prediction a misassignment. Determine whether the prediction is supported or refuted.

## Term and Decision Context

- Term: zinc ion binding (GO:0008270)

## Reference Context

- doi:10.64898/2026.03.19.712954

## Source Context YAML

```yaml
hypothesis: BioReason-Pro SFT predicts zinc ion binding (GO:0008270) for the Escherichia coli chaperone
  DnaK (P0A6Y8). Independently assess whether DnaK -- an Hsp70-family chaperone with an N-terminal nucleotide-binding
  domain (NBD) and a C-terminal substrate-binding domain (SBD) -- contains a zinc-binding motif or coordinating
  site, or whether it lacks any zinc center (the zinc-finger of the DnaK/DnaJ chaperone system belongs
  to the co-chaperone DnaJ, not DnaK), which would make the zinc-ion-binding prediction a misassignment.
  Determine whether the prediction is supported or refuted.
focus_type: computational_prediction
term_id: GO:0008270
term_label: zinc ion binding
context: []
reference_id:
- doi:10.64898/2026.03.19.712954
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

# DnaK (P0A6Y8) Zinc-Ion-Binding Prediction — Focused Curation Report

**Gene:** DnaK (Hsp70 chaperone) · *Escherichia coli* K-12 · UniProt **P0A6Y8**
**Prediction under review:** BioReason-Pro SFT → **zinc ion binding (GO:0008270)**
**Focus type:** computational_prediction · **Slug:** prediction-zinc-binding
**Reference context:** doi:10.64898/2026.03.19.712954

---

## Executive Judgment

**Verdict: Over-annotated / weakly supported — treat as a non-core, likely artifactual assignment (effectively refuted as a molecular function).**

DnaK does not possess a bona fide zinc-coordinating center. The prediction is not wholly baseless — there is a single existing IDA GO annotation (GO:0008270) on DnaK — but that annotation rests entirely on **one low-specificity, abundance-biased proteomic Zn-blot screen (PMID:11985624)** and is contradicted by DnaK's sequence and structure:

- DnaK has **only one cysteine (Cys15)** in 638 residues and **no CXXC / C4 zinc-finger motif** — it is structurally incapable of forming a classical cysteine-based zinc site.
- **0 of 63 DnaK PDB entries** contain a bound zinc ion, despite extensive structural characterization of both the NBD and SBD.
- The **genuine zinc-binding component of the DnaK/DnaJ/GrpE system is the co-chaperone DnaJ** (P08622), which has a CR-type zinc finger coordinating 2 Zn²⁺ via 8 cysteines. The prediction is best explained as **paralog/system confusion plus database carry-over**.

Recommended lead: **do not curate GO:0008270 as a DnaK function**; if retained at all, downgrade to a low-confidence, in-vitro-only/adventitious note, not a mechanistic MF.

**Most important caveat:** an existing curated IDA annotation does exist (EcoliWiki, PMID:11985624), so this is a case of challenging a weak legacy annotation rather than a term with zero support. The judgment rests on the low specificity of that assay and the absence of any structural/sequence basis.

---

## Evidence Matrix

| Citation | Evidence type | Stance | Claim tested | Key finding | Context | Confidence / limitations |
|---|---|---|---|---|---|---|
| UniProt P0A6Y8 (computed here) | Sequence/computational | **Refutes** | DnaK has a Cys-based zinc motif | Only 1 Cys (Cys15); 0 CXXC motifs; no Metal-binding/Zinc-finger feature | *E. coli* DnaK, 638 aa | High; sequence is definitive that no canonical C4/C2H2 Zn finger exists |
| RCSB (63 entries, queried here) | Structural | **Refutes** | Zinc is present in DnaK structures | 0/63 DnaK PDB entries contain a ZN ligand | NBD + SBD crystal/NMR structures | High; large structural sample, all zinc-free |
| PMID:11985624 (Katayama 2002) | Direct assay (proteomic ⁶⁵Zn-blot) | **Qualifies (sole support)** | DnaK binds Zn²⁺ in vitro | DnaK "newly identified" among 9 hits alongside AckA, GlyA, TktA/B, Tsf, ribosomal proteins | 2D-gel Zn-blot of total *E. coli* lysate | Low specificity; abundance-biased; many hits lack Zn-finger motifs |
| QuickGO annotation record (queried here) | Database | **Qualifies** | Provenance of DnaK Zn annotation | Only GO:0008270 on DnaK = IDA/EcoliWiki/PMID:11985624; identical ref also used for DnaJ | Annotation metadata | High; shows single-source, carry-over pattern |
| PMID:15683252 (Shi 2005) | Structural/biochemical | **Competing (DnaJ)** | Which system member binds Zn | DnaJ has two C4-type zinc fingers (C144/147/161/164/183/186/197/200) binding 2 Zn²⁺ | *E. coli* DnaJ | High; localizes zinc function to DnaJ, not DnaK |
| PMID:8662861 (Banecki 1996) | Direct assay (AAS/HgS titration) | **Competing (DnaJ)** | DnaJ zinc stoichiometry | Two Zn²⁺ per DnaJ monomer | *E. coli* DnaJ | High; establishes DnaJ as the zinc-binding partner |
| PMID:23708608 (Qi 2013); 34453889; 33950017 | Structural | **Refutes (by omission)** | DnaK core MF is Zn-dependent | Full-length ATP-bound and domain structures: ATPase NBD + peptide SBD; no zinc site | *E. coli* DnaK | High; mechanism is ATP/Mg²⁺/K⁺- and peptide-driven, not zinc |
| InterPro (queried Iter 2) | Structural/evolutionary | **Refutes** | DnaK has a zinc-finger domain | Only Hsp70 domains (IPR012725, PF00012, NBD/SBD/PBD); no zinc-finger/metal domain | *E. coli* DnaK | High; comprehensive signature database |
| Ortholog Cys census (queried Iter 2) | Evolutionary | **Refutes** | Zinc binding conserved in Hsp70 | DnaK orthologs carry 0–5 Cys, 0 CXXC; *M. tuberculosis* DnaK has **0 cysteines** | Hsp70 family (bacteria/yeast/human) | High; a zero-Cys ortholog cannot form a Cys zinc site |

---

## GO Curation Implications

- **GO:0008270 (zinc ion binding, MF):** Lead — **do not propagate / recommend removal or NOT-qualifier consideration** for DnaK. The single IDA source is a low-specificity proteomic screen; there is no motif, no structural zinc, and no mechanistic role. If curator policy forbids removing an IDA, at minimum it should **not** be treated as a core molecular function and should carry an explicit caveat that it derives from a whole-proteome Zn-blot with probable non-specific binding.
- **Do not** substitute a vaguer term (e.g., "metal ion binding" or "protein binding") — no informative metal-binding term is supported.
- **Well-supported core MF terms to prefer/retain instead:** ATP binding (GO:0005524), ATP hydrolysis activity (GO:0016887), ADP binding (GO:0043531), unfolded protein binding (GO:0051082), ATP-dependent protein folding chaperone (GO:0140662). These reflect DnaK's actual activities.
- **Paralog note for curators:** the zinc-ion-binding annotation is biologically correct **for DnaJ (P08622)**, and the shared PMID:11985624 reference suggests the DnaK entry is a co-annotation carry-over.

---

## Mechanistic Scope

The immediate molecular function being tested is **direct coordination of a Zn²⁺ ion by DnaK**. DnaK's actual direct activities are: (i) ATP binding and hydrolysis in the N-terminal nucleotide-binding domain (actin/hexokinase fold; uses Mg²⁺ and K⁺, not Zn²⁺), and (ii) binding of exposed hydrophobic segments of unfolded clients in the C-terminal substrate-binding domain, allosterically coupled to the nucleotide state. No step of this cycle requires or involves a structural zinc. Any zinc signal observed in a lysate blot is a **downstream in vitro observation** on an abundant protein, not a mechanistic feature of the chaperone cycle.

---

## Conflicts and Alternatives

- **Paralog confusion (most likely):** DnaJ, the obligate co-chaperone in the DnaK/DnaJ/GrpE system, genuinely binds 2 Zn²⁺ via a CR-type zinc finger. Zinc binding is a real property of the *system* but resides in DnaJ.
- **Database carry-over / frequency bias:** the same reference (PMID:11985624) underlies the IDA on both DnaK and DnaJ; a model trained on such annotations would plausibly transfer "zinc ion binding" onto the more famous/abundant DnaK.
- **Assay artifact:** ⁶⁵Zn-blotting of 2D gels captures many abundant, acidic, or surface-exposed proteins non-specifically; the paper's own hit list (kinases, transketolase, ribosomal proteins, EF-Ts) is enriched for proteins with no canonical zinc-finger, signaling low specificity.
- **No organism/isoform escape hatch:** DnaK is a single-copy, well-conserved bacterial Hsp70; no isoform harbors extra cysteines that could form a zinc site.
- **Negative literature check (Iter 3):** targeted PubMed searches for a *functional* DnaK zinc/metal-binding site or a copper/zinc redox role returned no primary evidence (the only zinc-finger chaperone hit was thioredoxin-2, unrelated to DnaK). No study proposes zinc as mechanistically required for DnaK. The UniProt BP term "stress response to copper ion" (GO:1990169) reflects a physiological stress response, not direct metal coordination by DnaK.

---

## Knowledge Gaps

1. **Is the Katayama Zn signal specific or adventitious?** Checked: sequence (1 Cys), structure (0/63 PDB), and hit-list composition all argue non-specific. Matters because it is the sole primary support. Resolve with: purified DnaK ICP-MS/atomic-absorption zinc stoichiometry and competition/specificity controls (as were done for DnaJ).
2. **Does any DnaK conformer transiently bind Zn functionally?** Checked: allosteric-cycle structures show no zinc site. Matters only if a regulatory zinc were proposed. Resolve with: metal-content analysis across ADP/ATP states.
3. **What exactly does EcoliWiki's IDA claim?** Checked provenance (PMID:11985624 only). Matters for whether removal vs. caveat is appropriate. Resolve with: read full Katayama methods to confirm DnaK's measured affinity/specificity class.

---

## Discriminating Tests

- **ICP-MS / atomic absorption on purified recombinant DnaK** (apo vs. Zn-loaded) — quantify Zn:protein stoichiometry; expect ~0 for a genuine non-binder, ~2 for DnaJ control.
- **Cys15→Ser mutant + metal blot** — a genuine Cys-based site would lose signal; a non-specific surface interaction would not.
- **Side-by-side ⁶⁵Zn-blot of DnaK vs DnaJ vs a bona fide C4 zinc-finger control** with EDTA/competitor titration to grade specificity.
- **AlphaFold3/metal-aware docking or MIB/CHED metal-site prediction** on P0A6Y8 — expect no high-confidence zinc site (bioinformatic corroboration).

---

## Curation Leads (require curator verification)

- **Action change:** Flag GO:0008270 on DnaK as **not a core function**; propose removal or downgrade with an explicit provenance caveat. Do **not** replace with "metal ion binding" or "protein binding."
- **Candidate references to verify (exact snippets):**
  - PMID:11985624 — *"nine zinc-binding proteins were newly identified including: acetate kinase (AckA), DnaK, serine hydroxymethyltransferase (GlyA)…"* (verify this is the sole basis and note low specificity).
  - PMID:15683252 — *"which coordinate with two Zn(II) ions to form an unusual topology of two C4-type zinc fingers…"* (confirms zinc role belongs to DnaJ).
  - PMID:8662861 — *"two Zn(II) ions interact with each monomer of DnaJ."* (DnaJ stoichiometry).
- **Suggested curator questions:** (1) Is a single whole-proteome Zn-blot sufficient IDA support for a core MF given contradicting sequence/structure? (2) Should the DnaK/DnaJ shared reference trigger a carry-over review?
- **Suggested experiment:** purified-DnaK ICP-MS zinc stoichiometry with Cys15 mutant control.
- **Positive terms to keep:** ATP binding, ATP hydrolysis activity, unfolded protein binding, ATP-dependent protein folding chaperone.

---

*Artifacts (computed provenance):* `artifacts/evidence_matrix.csv`, `artifacts/hsp70_cysteine_census.csv`.

*Provenance:* All computed results (UniProt feature/GO parse, cysteine census, RCSB zinc-ligand query returning 0/63, QuickGO annotation provenance) were generated by executed code in Iteration 1; primary literature accessed via PubMed. No results were fabricated; the RCSB query returned HTTP 204 (empty) for DnaK-with-zinc.


## Artifacts

- [OpenScientist evidence matrix](openscientist_artifacts/artifacts_evidence_matrix.csv)
- [OpenScientist hsp70 cysteine census](openscientist_artifacts/artifacts_hsp70_cysteine_census.csv)
- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)