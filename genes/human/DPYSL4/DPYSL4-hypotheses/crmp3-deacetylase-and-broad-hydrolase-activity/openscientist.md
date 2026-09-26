---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-20T18:11:19.219703'
end_time: '2026-09-20T18:52:23.951083'
duration_seconds: 2464.73
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: human
  gene: DPYSL4
  gene_symbol: DPYSL4
  uniprot_accession: O14531
  taxon_id: NCBITaxon:9606
  taxon_label: Homo sapiens
  focus_type: function_assignment
  hypothesis_slug: crmp3-deacetylase-and-broad-hydrolase-activity
  hypothesis_text: Human DPYSL4/CRMP3 (O14531) has hydrolase activity (GO:0016787),
    specifically hydrolase activity acting on carbon-nitrogen bonds other than peptide
    bonds (GO:0016810). Evaluate the primary 2013 CRMP3 histone-H4 deacetylation study
    (PMC3583001) for exact gene/ortholog identity, protein construct, processing,
    purity and substrate assays; seek independent corroboration or conflicting evidence.
    Determine whether the reported deacetylase activity supports these broad parents
    even if cyclic-amide dihydropyrimidinase activity is lost. Loss of one substrate-specific
    ancestral activity does not establish loss of every hydrolase activity.
  term_context: No specific term context supplied.
  reference_context: No specific reference context supplied.
  source_file: genes/human/DPYSL4/DPYSL4-ai-review.yaml
  source_selector: free-text
  source_context_yaml: "hypothesis: Human DPYSL4/CRMP3 (O14531) has hydrolase activity\
    \ (GO:0016787), specifically hydrolase activity\n  acting on carbon-nitrogen bonds\
    \ other than peptide bonds (GO:0016810). Evaluate the primary 2013 CRMP3\n  histone-H4\
    \ deacetylation study (PMC3583001) for exact gene/ortholog identity, protein construct,\
    \ processing,\n  purity and substrate assays; seek independent corroboration or\
    \ conflicting evidence. Determine whether\n  the reported deacetylase activity\
    \ supports these broad parents even if cyclic-amide dihydropyrimidinase\n  activity\
    \ is lost. Loss of one substrate-specific ancestral activity does not establish\
    \ loss of every\n  hydrolase activity.\nfocus_type: function_assignment\ncontext:\
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
citation_count: 2
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

- **Organism code:** human
- **Taxon:** Homo sapiens (NCBITaxon:9606)
- **Gene directory:** DPYSL4
- **Gene symbol:** DPYSL4
- **UniProt accession:** O14531

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** crmp3-deacetylase-and-broad-hydrolase-activity
- **Source file:** genes/human/DPYSL4/DPYSL4-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

Human DPYSL4/CRMP3 (O14531) has hydrolase activity (GO:0016787), specifically hydrolase activity acting on carbon-nitrogen bonds other than peptide bonds (GO:0016810). Evaluate the primary 2013 CRMP3 histone-H4 deacetylation study (PMC3583001) for exact gene/ortholog identity, protein construct, processing, purity and substrate assays; seek independent corroboration or conflicting evidence. Determine whether the reported deacetylase activity supports these broad parents even if cyclic-amide dihydropyrimidinase activity is lost. Loss of one substrate-specific ancestral activity does not establish loss of every hydrolase activity.

## Term and Decision Context

No specific term context supplied.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: Human DPYSL4/CRMP3 (O14531) has hydrolase activity (GO:0016787), specifically hydrolase activity
  acting on carbon-nitrogen bonds other than peptide bonds (GO:0016810). Evaluate the primary 2013 CRMP3
  histone-H4 deacetylation study (PMC3583001) for exact gene/ortholog identity, protein construct, processing,
  purity and substrate assays; seek independent corroboration or conflicting evidence. Determine whether
  the reported deacetylase activity supports these broad parents even if cyclic-amide dihydropyrimidinase
  activity is lost. Loss of one substrate-specific ancestral activity does not establish loss of every
  hydrolase activity.
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

# DPYSL4/CRMP3 (O14531): Evaluation of Broad Hydrolase Activity Assignment

**Focus:** function_assignment — does human DPYSL4/CRMP3 directly have hydrolase activity (GO:0016787), specifically hydrolase acting on C–N bonds other than peptide bonds (GO:0016810), on the strength of the 2013 CRMP3 histone-H4 deacetylation study (PMID 23443259 / PMC3583001)?

**Iteration:** updated through Iteration 3 of 3.

---

## Executive Judgment

**Verdict: Over-annotated / refuted for intrinsic activity — assigning GO:0016787 and GO:0016810 to human DPYSL4 as experimentally-meaningful MF is NOT justified. In the live GO record these two terms already exist ONLY as InterPro2GO family-based IEA carry-over, and they coexist with curated `NOT` dihydropyrimidinase / `NOT` pyrimidine-catabolism annotations. The single deacetylase study does not establish intrinsic catalysis and does not upgrade them.**

**Decisive new evidence (Iteration 3, from the primary study's own full text, PMC3583001):** the reported "CRMP3 HDAC activity" was **completely inhibited by 1 μM Trichostatin A (TSA)**. TSA inhibits classical class I/II HDACs by chelating their catalytic **Zn²⁺** — a metal center that DPYSL4 structurally **cannot** possess (its amidohydrolase pocket has lost 4 of 6 Zn-coordinating residues). An activity that is both attributed to DPYSL4 *and* behaves exactly like a canonical zinc-HDAC is most parsimoniously explained by an **associated or co-purifying Zn-HDAC**, not by intrinsic DPYSL4 catalysis. The authors deserve credit for a genuine contamination control (re-expression in Sf9 insect cells), but insect cells also contain endogenous Zn-HDACs that can co-purify with an affinity-tagged bait, and **no catalytically-dead point mutant** was used to prove intrinsic catalysis (none is even designable, because the active site is degenerate). The paper's mechanistic rationale is also flawed: it lists "histone deacetylase (HDAC)" as a member of the "cyclic amidohydrolase superfamily," but HDACs are a structurally distinct arginase/deacetylase fold, so DPYSL4's dihydropyrimidinase-domain homology does not imply deacetylase capability.

Reasoning:
1. **The ancestral C–N hydrolase activity is demonstrably lost.** DPYSL4 belongs to the amidohydrolase/dihydropyrimidinase superfamily but has a **degenerate active site**: a computed global alignment against the active enzyme human dihydropyrimidinase (DPYS, Q14117) shows only **2 of 6 Zn²⁺-coordinating catalytic residues are conserved**. The metal-bridging carbamoylated lysine (DPYS Lys159) is replaced by Leu, and three of four catalytic histidines/aspartate are lost (His69→Arg, His248→Lys, Asp326→Ala). The binuclear zinc center — required for metal-dependent C–N bond hydrolysis — cannot form. Independent crystallography (Myllykoski et al. 2017, PMID 28044206) states outright that CRMPs "have lost the enzymatic active site." The primary study itself confirms rodent CRMPs "do not hydrolyze dihydropyrimidinase substrates."

2. **The deacetylase claim is single-source and mechanistically implausible.** Only one primary study reports the activity (Hou et al. 2013), it was performed on the **mouse ortholog** (Dpysl4, O35098 — 93.2% identical to human, catalytic residues identically degenerate), it comes from a **single laboratory** with **no independent replication**, and DPYSL4 lacks **any** catalytic machinery compatible with protein deacetylation (no Zn-dependent HDAC site, no NAD⁺-dependent sirtuin fold). Co-purifying contaminant deacetylase — a classic artifact for "novel deacetylase" claims — was not excluded.

3. **Technicality vs. warranted annotation.** Protein-lysine deacetylation *is* formally a hydrolysis of a carbon–nitrogen (amide) bond, so *if* the activity were genuine and intrinsic it would fall under GO:0016810. But the evidence is too weak, unreplicated, ortholog-based, and mechanistically unsupported to license an experimental MF annotation of the broad hydrolase parents to human DPYSL4. The seed argument ("loss of dihydropyrimidinase ≠ loss of all hydrolase activity") is logically valid but is not rescued by the deacetylase paper, because that paper does not establish a credible, replicated, intrinsic hydrolase activity for the human protein.

**Most important caveats:** The full text of PMC3583001 was retrieved (via NCBI efetch, Iteration 3) and the methods inspected directly. Constructs: recombinant mouse full-length CRMP3, calpain product p54, and the conserved dihydropyrimidinase "D domain," His6/S-tagged, affinity-purified from HEK293 and (as a control) Sf9 insect cells; assayed with a cell-free fluorescent HDAC assay on a histone-derived substrate. The residual uncertainty is interpretive, not descriptive: affinity purification of a tagged bait does not exclude a tightly-associated HDAC in either host, TSA sensitivity actively points to a Zn-HDAC mechanism the protein cannot supply, no catalytically-dead mutant was tested, no independent group has replicated the activity, and it was never measured on human O14531.

### Live GO record for O14531 (QuickGO, retrieved Iteration 2)

| GO ID | Name | Aspect | Evidence | Reference | Qualifier | Interpretation |
|---|---|---|---|---|---|---|
| GO:0016787 | hydrolase activity | MF | **IEA** ECO:0000256 | GO_REF:0000002 (InterPro2GO) | enables | Family-fold electronic transfer; not experimental |
| GO:0016810 | hydrolase acting on C–N bonds, non-peptide | MF | **IEA** ECO:0000256 | GO_REF:0000002 (InterPro2GO) | enables | Family-fold electronic transfer; **this is the hypothesis term** |
| GO:0016812 | hydrolase, C–N bonds, in cyclic amides | MF | IBA ECO:0000318 | GO_REF:0000033 | enables | Phylogenetic; internally inconsistent with the NOT below |
| GO:0004157 | dihydropyrimidinase activity | MF | IBA ECO:0000318 | GO_REF:0000033 | **NOT\|enables** | Curated absence of the specific ancestral activity |
| GO:0006208 | pyrimidine nucleobase catabolic process | BP | IBA ECO:0000318 | GO_REF:0000033 | **NOT\|involved_in** | Curated absence of the pathway |
| GO:0005515 | protein binding | MF | IPI | 5 PMIDs | enables | Better-supported MF than hydrolase |
| GO:0031005 | filamin binding | MF | IPI | PMID:25358863 | enables | Specific interaction |
| GO:0007399 | nervous system development | BP | TAS | PMID:9652388 | involved_in | Better-supported BP |
| GO:0005829 | cytosol | CC | IBA/TAS | Reactome | located_in/is_active_in | Localization |

**Key point:** the hypothesis's two target terms are precisely the automatic InterPro2GO predictions driven by the amidohydrolase fold (InterPro signatures PF01979 Amidohydrolase, IPR006680, IPR011778 D-phenylhydantoinase/dihydropyrimidinase, IPR050378/PTHR11647 Metallo-dependent Hydrolases, TIGR02033 dihydropyrimidinase). They are contradicted by the curated `NOT GO:0004157` / `NOT GO:0006208` calls and by the degenerate active site — a textbook pseudo-enzyme over-annotation.

---

## Evidence Matrix

| Citation (PMID) | Evidence type | Supports/Refutes/Qualifies | Claim tested | Key finding | Context | Confidence & limitations |
|---|---|---|---|---|---|---|
| 23443259 (Hou 2013, PMC3583001) | Direct in-vitro assay + cell/animal | **Supports** (the seed) but **qualifies** heavily | CRMP3 has histone H4 deacetylase activity | "mouse CRMP3 has robust histone H4 deacetylase activity"; truncated CRMP3 → H4 deacetylation → E2F1 de-repression → neuronal death | Mouse CRMP3/Dpysl4; excitotoxicity/ischemia; calpain-cleaved nuclear form | Single lab, single study, **mouse ortholog not human**; His6/S-tag affinity-purified; in-vitro; not replicated |
| 23443259 (full text, Iteration 3) | Direct assay detail — inhibitor profile | **Refutes** intrinsic activity (competing = contaminant Zn-HDAC) | Is the "CRMP3 HDAC" activity a classical zinc-HDAC? | "TSA (1 μM) completely inhibited CRMP3 HDAC activities" — full-length > D domain > p54; complete TSA (Zn-chelator) inhibition | HEK293- and Sf9-expressed recombinant protein, cell-free fluorescent HDAC assay | High mechanistic weight: TSA-sensitivity implies a Zn-HDAC center DPYSL4 cannot have → associated/contaminating HDAC most parsimonious; no catalytic-dead mutant control |
| 23443259 (full text) | Contamination control | **Qualifies** (partial support for authors) | Is activity from HEK293 host contaminants? | Re-expressed in Sf9 insect cells to exclude HEK293 contaminants; activity retained | Sf9 insect cells | Genuine control, but insect cells also have endogenous Zn-HDACs that can co-purify with a tagged bait |
| 23443259 (full text) | Rationale / classification | **Refutes** premise | Does DHPase-fold homology imply deacetylase capability? | Paper places "HDAC" inside the "cyclic amidohydrolase superfamily" — but HDACs are a distinct arginase/deacetylase fold | — | The homology argument underpinning the claim is structurally invalid |
| 23443259 (same) | Author statement | **Refutes** ancestral activity | Dihydropyrimidinase activity | "purified rodent brain CRMPs do not hydrolyze dihydropyrimidinase substrates" | Rodent brain CRMPs | High confidence the cyclic-amidase activity is absent |
| 28044206 (Myllykoski 2017) | Structural (1.25 Å X-ray) / evolutionary | **Refutes** intrinsic hydrolase | CRMPs retain a catalytic site | "belong to the dihydropyrimidinase family, they have lost the enzymatic active site" | Human CRMP2 (close paralog) | High; direct structural evidence for the family |
| Computed alignment DPYS(Q14117) vs DPYSL4(O14531) | Structural/evolutionary (this run) | **Refutes** C–N hydrolase | Are Zn-coordinating catalytic residues conserved? | Only 2/6 conserved; carbamoyl-Lys159→Leu, His69→Arg, His248→Lys, Asp326→Ala; 59.6% overall identity | Human sequences, UniProt | High for residue mapping; NW alignment (BLOSUM62), not a structural superposition |
| Computed mouse–human ortholog check (this run) | Computational | **Qualifies** | Is the assayed protein the true DPYSL4 ortholog? | Mouse Dpysl4 O35098 = 93.2% identical to human; catalytic residues identically degenerate | UniProt | High; confirms gene identity but also that mouse protein equally lacks the active site |
| 16495451 (Hou 2006), 19559021 (Aylsworth 2009) | Cell/animal mechanism | Context (competing interpretation) | Function of calpain-cleaved CRMP3 | Truncated CRMP3 → nuclear translocation, nuclear condensation, neuronal death; inhibits microtubule polymerization | Rodent neurons; same lab | Supports a *pro-death nuclear role* but not necessarily via an intrinsic hydrolase; all same group |

---

## GO Curation Implications (leads — require curator verification)

- **The two hypothesis terms already exist only as IEA InterPro2GO carry-over (GO_REF:0000002).** The curation question is therefore *not* "should we add them from the deacetylase paper" but "should the existing family-based IEA GO:0016787/GO:0016810 be trusted." Answer: **no / low-confidence** — they are automatic fold-based predictions for a pseudo-enzyme whose active site is degenerate, and they conflict with the curated `NOT GO:0004157` (dihydropyrimidinase) and `NOT GO:0006208` (pyrimidine catabolism) annotations. Recommend flagging GO:0016787/GO:0016810 as unreliable IEA (candidate for `NOT` or removal), pending curator judgment on how far to generalize the loss-of-activity.
- **Do NOT promote GO:0016787 / GO:0016810 to an experimentally-supported MF for DPYSL4** on the basis of PMID 23443259. Rationale: ancestral C–N hydrolase activity is lost (degenerate active site; author-confirmed absence of dihydropyrimidinase activity), and the deacetylase activity is single-source, ortholog-based, mechanistically implausible, and unreplicated. The deacetylase paper is not even the provenance of the current terms.
- **Resolve the internal inconsistency:** GO:0016812 (cyclic-amidase) is currently `enables` (IBA) while its child GO:0004157 is `NOT`. A curator should reconcile these — the biochemistry (no dihydropyrimidinase activity; degenerate site) argues the positive cyclic-amidase IBA is also questionable.
- **If a deacetylase-related term is considered at all**, it should be treated as **uncertain / non-core** and attributed with the appropriate ortholog/evidence caveat (mouse, in vitro) — not propagated as a confident human MF. The more specific term, if ever supported, would be **histone deacetylase activity (GO:0004407)**, itself a child of GO:0016810; but the current evidence does not meet the bar for an experimental (IDA) annotation, and IEA/homology transfer is contraindicated by the degenerate active site.
- **Dihydropyrimidinase / cyclic-amidase activity (GO:0004157 and related): should be treated as NOT present** (retain any existing "loss of function" / NOT annotation).
- **Better-supported terms for DPYSL4** are its cytoskeletal/neurodevelopmental roles (semaphorin signaling, neurite outgrowth regulation, microtubule/tubulin interaction) — BP/CC and interaction terms are more informative than a broad hydrolase MF. (Avoid "protein binding" as the endpoint; the vimentin/tubulin interactions and neurite-outgrowth BP are more specific.)

---

## Mechanistic Scope

- **Immediate molecular function tested:** intrinsic hydrolase (amidohydrolase) activity of the DPYSL4 polypeptide — either (a) cyclic-amide hydrolysis of dihydropyrimidines (ancestral) or (b) amide hydrolysis of acetyl-lysine (the proposed deacetylase).
- **Direct gene-product activity:** Sequence/structure indicate DPYSL4 lacks a functional metallo-hydrolase center; the ancestral (a) is lost. The proposed (b) is asserted for the mouse ortholog only, in vitro.
- **Downstream phenotypes (must be separated from MF):** calpain cleavage → nuclear translocation → nuclear condensation → E2F1 de-repression → neuronal death. These are cellular/organismal consequences and do not by themselves demonstrate that DPYSL4 is the direct catalytic deacetylase; the H4 deacetylation could be mediated by an associated/contaminating enzyme or an indirect chromatin effect.

---

## Conflicts and Alternatives

- **Paralog/family evidence conflicts with intrinsic catalysis:** the whole CRMP subfamily (DPYSL1–5) is structurally established to have lost the amidohydrolase active site (PMID 28044206). This is the strongest alternative: DPYSL4 is a pseudo-enzyme scaffold.
- **Organism/isoform:** activity shown for mouse Dpysl4 truncation product, not full-length human O14531. Even at 93% identity, the human MF is inferred, not measured.
- **Experimental artifact (now strongly indicated):** the activity was **completely inhibited by 1 μM TSA**, a Zn²⁺-chelating inhibitor of classical class I/II HDACs. Because DPYSL4 has no such zinc center, an associated/co-purifying Zn-HDAC is the leading alternative explanation. The authors' Sf9 dual-expression control reduces but does not eliminate this (insect cells have their own Zn-HDACs, and affinity-tagged CRMP3 could pull down an associated HDAC). No catalytically-dead mutant was used.
- **Invalid homology premise:** the paper justifies the activity by placing HDAC within the "cyclic amidohydrolase superfamily," but HDACs are an unrelated arginase/deacetylase fold; DPYSL4's dihydropyrimidinase-domain homology gives no basis for deacetylase chemistry.
- **Single-lab provenance:** all mechanistic CRMP3 death papers trace to one group (Hou/Zhou), raising the value of independent replication before curation.

---

## Knowledge Gaps

1. **Catalytic-dead control (RESOLVED as absent).** Checked: full-text methods (Iteration 3). The study used His6/S-tag affinity purification from HEK293 and Sf9, a TSA control, and HDAC-isoform comparisons, but **no catalytically-dead CRMP3 point mutant** — the single control that would prove intrinsic catalysis. None is readily designable because the active site is degenerate. Gap now: this control is missing and would be decisive; TSA-sensitivity meanwhile points away from intrinsic activity. Resolve: mass-spec of the affinity eluate for co-purifying HDACs; a mutant that ablates any candidate catalytic residue.
2. **Independent replication of DPYSL4 deacetylase activity.** Checked: PubMed — none found. Matters because a single source is below the bar for a confident MF. Resolve: targeted literature/citation search; any orthogonal biochemistry.
3. **Human O14531 direct assay.** Checked: not available. Matters for species-specific annotation. Resolve: assay recombinant human DPYSL4.
4. **Structural confirmation of pocket geometry.** Checked: alignment-based only (no superposition run here). Resolve: superpose an AlphaFold/experimental DPYSL4 model onto DPYS to confirm the metal site is non-functional (Phenix superpose / structure comparison).

---

## Discriminating Tests

- **Catalytically-dead mutant assay:** mutate a residue essential to any proposed DPYSL4 catalytic mechanism and show loss of deacetylase activity — distinguishes intrinsic activity from contaminant.
- **Rigorous recombinant purification + mass-spec of the prep** to detect co-purifying HDAC1/2/SIRT.
- **Inhibitor panel (partly already answered):** the reported activity is fully blocked by 1 μM TSA — i.e. it behaves as a class I/II Zn-HDAC, which DPYSL4 cannot be, implicating a contaminant/associated enzyme. A definitive test would add mass-spec of the eluate and a nicotinamide/sirtuin arm.
- **Structural superposition** (Phenix) of a DPYSL4 model onto DPYS/dihydropyrimidinase to quantify active-site collapse.
- **Human O14531 replication** of the H4 deacetylation assay.

---

## Curation Leads (require curator verification)

- **Candidate reference to verify:** PMID 23443259 — verify snippets: *"mouse CRMP3 has robust histone H4 deacetylase activity"*, *"purified rodent brain CRMPs do not hydrolyze dihydropyrimidinase substrates"*, and the decisive methods line *"TSA (1 μM) completely inhibited CRMP3 HDAC activities."* Confirm construct = mouse Dpysl4 (O35098), His6/S-tagged, expressed in HEK293 and Sf9; note the **absence of a catalytically-dead mutant control** and the invalid superfamily premise (HDAC listed within "cyclic amidohydrolase superfamily").
- **Candidate corroborating reference:** PMID 28044206 — verify snippet: *"belong to the dihydropyrimidinase family, they have lost the enzymatic active site."*
- **Candidate GO actions:**
  - Do **not** assert GO:0016787 / GO:0016810 as experimental MF for DPYSL4 (over-annotation risk).
  - If retained from a prior action, **generalize/qualify or remove**; at most treat deacetylase as an **uncertain, non-core** claim (would resolve to GO:0004407 if ever confirmed) with mouse/in-vitro caveats.
  - Confirm/retain **NOT dihydropyrimidinase activity** for the human protein.
- **Suggested questions for curator:** Was any prior MF hydrolase annotation on DPYSL4 IEA-by-homology from the DPYS active site? If so, it is contraindicated by the degenerate catalytic residues shown here.
- **Suggested experiments:** catalytically-dead mutant + inhibitor panel + human-protein replication (see Discriminating Tests).

---

### Provenance (analyses run, Iterations 1–3)
- **Iter 1:** UniProt REST fetch of O14531 (DPYSL4), Q14117 (DPYS), Q16555 (CRMP2), O35098 (mouse Dpysl4); DPYS catalytic/binding-site features extracted from UniProt. Needleman–Wunsch (BLOSUM62) global alignment DPYS vs DPYSL4: 59.6% identity; catalytic-residue mapping → 2/6 Zn-coordinating residues conserved (carbamoyl-Lys159→Leu, His69→Arg, His248→Lys, Asp326→Ala). Mouse–human DPYSL4 identity 93.2% with identical catalytic degeneracy. PubMed searches.
- **Iter 2:** QuickGO annotation retrieval for O14531 (all three aspects) → GO:0016787/0016810 are IEA/InterPro2GO; GO:0004157 and GO:0006208 are `NOT`. InterPro entry retrieval → amidohydrolase/dihydropyrimidinase family signatures (PF01979, IPR006680, IPR011778, IPR050378, PTHR11647, TIGR02033, cd01314) confirming the IEA provenance.
- **Iter 3:** NCBI efetch retrieval of PMC3583001 full text → construct/expression/purification details; decisive line "TSA (1 μM) completely inhibited CRMP3 HDAC activities"; Sf9 dual-expression contamination control; no catalytic-dead mutant; superfamily-premise error identified.

### Bottom line for the curator
The seed hypothesis's broad hydrolase terms (GO:0016787, GO:0016810) are **not** supported as intrinsic molecular functions of human DPYSL4. They presently exist only as automatic InterPro2GO fold-based IEA predictions that conflict with curated `NOT` annotations and with a degenerate active site, and the one deacetylase study that might justify them is single-lab, mouse-only, unreplicated, mechanistically implausible (TSA-sensitive activity in a protein lacking a Zn-HDAC center), and built on an invalid fold-homology premise. Recommended lead: do not promote to experimental MF; flag the IEA terms as low-confidence/candidate-for-`NOT`; record any deacetylase claim only as uncertain, non-core, with mouse/in-vitro caveats.


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)