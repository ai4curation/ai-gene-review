---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-20T22:32:55.379905'
end_time: '2026-09-20T23:16:58.016974'
duration_seconds: 2642.64
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: human
  gene: ABHD8
  gene_symbol: ABHD8
  uniprot_accession: Q96I13
  taxon_id: NCBITaxon:9606
  taxon_label: Homo sapiens
  focus_type: function_assignment
  hypothesis_slug: lipid-catalysis-versus-inflammasome-adaptor
  hypothesis_text: Human ABHD8 (Q96I13) retains glycerophospholipase activity, ester
    hydrolase activity, lysophosphatidic acid acyltransferase activity, phosphatidic
    acid biosynthesis participation, or lipid homeostasis. Adjudicate each separately
    from its demonstrated NLRP3 adaptor role. Examine target catalytic residues and
    biochemical assays, phylogenetic function placement and source-subfamily specificity.
    Adaptor function and absence of target substrate experiments do not by themselves
    establish catalytic or pathway loss.
  term_context: No specific term context supplied.
  reference_context: No specific reference context supplied.
  source_file: genes/human/ABHD8/ABHD8-ai-review.yaml
  source_selector: free-text
  source_context_yaml: "hypothesis: Human ABHD8 (Q96I13) retains glycerophospholipase\
    \ activity, ester hydrolase activity, lysophosphatidic\n  acid acyltransferase\
    \ activity, phosphatidic acid biosynthesis participation, or lipid homeostasis.\
    \ Adjudicate\n  each separately from its demonstrated NLRP3 adaptor role. Examine\
    \ target catalytic residues and biochemical\n  assays, phylogenetic function placement\
    \ and source-subfamily specificity. Adaptor function and absence\n  of target\
    \ substrate experiments do not by themselves establish catalytic or pathway loss.\n\
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

- **Organism code:** human
- **Taxon:** Homo sapiens (NCBITaxon:9606)
- **Gene directory:** ABHD8
- **Gene symbol:** ABHD8
- **UniProt accession:** Q96I13

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** lipid-catalysis-versus-inflammasome-adaptor
- **Source file:** genes/human/ABHD8/ABHD8-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

Human ABHD8 (Q96I13) retains glycerophospholipase activity, ester hydrolase activity, lysophosphatidic acid acyltransferase activity, phosphatidic acid biosynthesis participation, or lipid homeostasis. Adjudicate each separately from its demonstrated NLRP3 adaptor role. Examine target catalytic residues and biochemical assays, phylogenetic function placement and source-subfamily specificity. Adaptor function and absence of target substrate experiments do not by themselves establish catalytic or pathway loss.

## Term and Decision Context

No specific term context supplied.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: Human ABHD8 (Q96I13) retains glycerophospholipase activity, ester hydrolase activity, lysophosphatidic
  acid acyltransferase activity, phosphatidic acid biosynthesis participation, or lipid homeostasis. Adjudicate
  each separately from its demonstrated NLRP3 adaptor role. Examine target catalytic residues and biochemical
  assays, phylogenetic function placement and source-subfamily specificity. Adaptor function and absence
  of target substrate experiments do not by themselves establish catalytic or pathway loss.
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

# AIGR Deep Research Report: ABHD8 (Q96I13) — Lipid Catalysis versus Inflammasome Adaptor

**Gene:** ABHD8 | **Organism:** *Homo sapiens* (NCBITaxon:9606) | **UniProt:** Q96I13
**Focus type:** function_assignment | **Hypothesis slug:** lipid-catalysis-versus-inflammasome-adaptor
**Source:** `genes/human/ABHD8/ABHD8-ai-review.yaml` (free-text selector)

---

## Summary

The seed hypothesis proposes that human ABHD8 retains one or more specific lipid functions — glycerophospholipase activity, generic ester hydrolase activity, lysophosphatidic acid (LPA) acyltransferase activity, participation in phosphatidic acid biosynthesis, or lipid homeostasis — and asks that each be adjudicated separately from ABHD8's demonstrated NLRP3 adaptor role. It further argues, correctly as a methodological principle, that neither the presence of an adaptor function nor the absence of substrate experiments by itself establishes catalytic or pathway loss. After three iterations of sequence, domain, orthology, and literature analysis, the evidence resolves into a clean split between **catalytic *potential* (supported)** and **specific lipid *activities* (unsupported by direct evidence, and in one case mechanistically implausible)**.

ABHD8 possesses a fully intact, canonical serine-hydrolase catalytic triad — **Ser252 (nucleophile), Asp370 (acid), His398 (base)** — embedded in a classic GXSXG nucleophile elbow (the motif **GHSYG**) within a complete α/β-hydrolase (AB_hydrolase-1) domain. This triad is conserved across all reviewed vertebrate orthologs from human to *Xenopus*, spanning more than 360 million years of divergence, which indicates purifying selection to preserve catalytic competence. ABHD8 is therefore **not** a dead pseudoenzyme, and a blanket claim of catalytic or pathway loss would be unjustified. This directly vindicates the seed's caution.

At the same time, **no ABHD8-specific biochemical assay demonstrates any lipid substrate.** The specific lipid GO terms are phylogenetic/family inferences (IBA from GO_Central; IEA from InterPro), not experiments. The LPA-acyltransferase claim is mechanistically inconsistent with a Ser-His-Asp hydrolase fold and almost certainly reflects paralog/family carry-over. The **only** experimentally demonstrated function is the NLRP3 scaffold/adaptor role: ABHD8 recruits the palmitoyltransferase ZDHHC12 to NLRP3, promoting NLRP3 palmitoylation and chaperone-mediated-autophagy (CMA) degradation ([PMID: 39225180](https://pubmed.ncbi.nlm.nih.gov/39225180/)). Accordingly, curation should retain the NLRP3 term (GO:1900226, IMP) and cytoplasm (GO:0005737, IDA) as core, keep any lipid-catalysis annotation at most as generic hydrolase potential (GO:0003824, IEA), and treat the specific lipid terms as over-annotations pending direct substrate assays.

**Verdict: Partially supported / unresolved — leaning over-annotated for the specific lipid activities, while catalytic potential is genuinely supported.**

---

## Key Findings

### Finding 1 — ABHD8 has an intact canonical serine-hydrolase catalytic triad but no demonstrated substrate

UniProt Q96I13 annotates an **AB_hydrolase-1 domain** spanning residues ~177–279, with the nucleophile-elbow **GXSXG** motif present as **G250-H-S252-Y-G254 (GHSYG)**. The charge-relay / catalytic triad is annotated at **Ser252 (nucleophile), Asp370 (acid), His398 (base)**, and the residue identities S/D/H were confirmed directly from the sequence. The protein maps to **InterPro IPR000073 (AB_hydrolase_1)**, **Pfam PF00561**, and the ABHD8-specific PANTHER subfamily **PTHR42886:SF83**.

Critically, UniProt carries **no CATALYTIC ACTIVITY comment and no specific reaction** for ABHD8. The only FUNCTION comment is the NLRP3 scaffold role citing PMID 39225180. The molecular-function GO annotation is the generic **GO:0003824 (catalytic activity)** with evidence **IEA:InterPro** only. In other words, the domain architecture supports catalytic *capability*, but nothing in the primary record pins down what ABHD8 actually hydrolyzes. The presence of a textbook triad establishes potential; it does not establish any specific reaction. This is the crux of the adjudication: catalytic potential and demonstrated function are, at present, decoupled.

### Finding 2 — The specific lipid-pathway GO terms are phylogenetic/family inference, not experiment

The GO annotation profile for Q96I13 separates cleanly into "inferred" versus "experimental":

| GO term | Aspect | Evidence code | Status |
|---|---|---|---|
| GO:0006654 phosphatidic acid biosynthetic process | BP | IBA:GO_Central | Phylogenetic inference — no experimental support |
| GO:0003824 catalytic activity | MF | IEA:InterPro | Generic, electronic |
| GO:1900226 negative regulation of NLRP3 inflammasome complex assembly | BP | IMP:UniProtKB | **Experimental** |
| GO:0005737 cytoplasm | CC | IDA | **Experimental** |

The "phosphatidic acid biosynthetic process" term is **IBA (inferred from biological ancestor)** — it derives from the behavior of other members of the phylogenetic tree, not from any ABHD8 assay. The seed-listed activities (glycerophospholipase, ester hydrolase, LPA acyltransferase) have **no ABHD8-specific primary assay** anywhere in the reviewed literature. Furthermore, **LPA acyltransferase is an acyltransfer reaction that is mechanistically incompatible with a Ser-His-Asp hydrolase fold** — the α/β-hydrolase triad catalyzes hydrolysis, not the acyl-CoA-dependent acyltransfer of a canonical LPAAT. This annotation is therefore the strongest candidate for paralog/family carry-over error.

The only experimentally demonstrated function — the NLRP3 scaffold (PMID 39225180) — is an **adaptor/scaffold mechanism, not a demonstrated hydrolase reaction**: ABHD8 recruits palmitoyltransferase ZDHHC12 to NLRP3 to promote NLRP3 palmitoylation and CMA-mediated degradation.

### Finding 3 — The catalytic triad is conserved across vertebrate orthologs (purifying selection)

Across all five reviewed UniProt ABHD8 orthologs — *Homo sapiens* (Q96I13), *Mus musculus* (Q8R0P8), *Bos taurus* (Q17QP1), *Macaca fascicularis* (Q4R584), and *Xenopus laevis* (Q6AX59) — the **GHSYG** nucleophile-elbow motif (Ser nucleophile), the catalytic Asp (human context VHG-**M-HDK**-F), and the catalytic His (human context DEG-**S-HM**) are all present. The human→*Xenopus* comparison spans **>360 million years** of divergence, and retention of the complete Ser-His-Asp triad plus the GXSXG elbow across that span is strong evidence of **purifying selection to preserve catalytic competence**.

This is the single most important piece of evidence *for* the seed hypothesis: an enzyme whose catalytic machinery has been conserved for hundreds of millions of years is unlikely to be a mere structural relic. It argues that ABHD8 *does* have a genuine catalytic activity — we simply do not yet know its substrate. Conservation, however, cannot tell us *which* substrate, and it does not license the specific lipid terms currently annotated. It is entirely compatible with a hydrolase acting on a substrate class not yet tested.

### Finding 4 — Full text confirms the NLRP3 function is scaffold-only, with no catalysis invoked

The full abstract of PMID 39225180 (Yang et al., 2025, *Autophagy*) states that ABHD8 "acts as a scaffold to recruit palmitoyltransferase ZDHHC12 to NLRP3 for its palmitoylation as well as subsequent CMA-mediated degradation." **ABHD8 deficiency stabilizes NLRP3 and promotes inflammasome activation**; overexpression ameliorates LPS/alum-triggered activation *in vivo*; and the SARS-CoV-2 N protein disrupts the ABHD8–NLRP3 association. Crucially, the abstract contains **no mention of ABHD8 hydrolase or lipase enzymatic activity, no lipid substrate, no phosphatidic acid or LPAAT reaction, and no catalytic-site (Ser252Ala) mutant experiment**. The mechanism is entirely consistent with a scaffold/adaptor that positions an enzyme (ZDHHC12) next to its target (NLRP3) — ABHD8 itself need not be catalytically active to perform this role.

Two verified citation snippets anchor this finding:
- *"ABHD8 acts as a scaffold to recruit palmitoyltransferase ZDHHC12 to NLRP3 for its palmitoylation as well as subsequent CMA-mediated degradation."* — directly states the demonstrated mechanism is a scaffold/adaptor role, not a catalytic reaction.
- *"ABHD8 deficiency results in the stabilization of NLRP3 protein and promotes NLRP3 inflammasome activation"* — establishes the loss-of-function phenotype underpinning the GO:1900226 negative-regulation term without invoking catalytic activity.

---

## Mechanistic Model / Interpretation

The evidence supports a two-track model in which catalytic *potential* and demonstrated *function* are currently decoupled:

```
                         ABHD8 (Q96I13)
                              │
        ┌─────────────────────┴─────────────────────┐
        │                                            │
  CATALYTIC POTENTIAL                       DEMONSTRATED FUNCTION
  (structure / evolution)                   (experimental — PMID 39225180)
        │                                            │
  AB_hydrolase-1 domain                     NLRP3 inflammasome control
  GHSYG nucleophile elbow                          │
  Triad: Ser252–Asp370–His398          ABHD8 = scaffold ──► recruits
        │                              ZDHHC12 (palmitoyltransferase)
  Conserved human→Xenopus                            │
  (>360 Myr, purifying selection)        NLRP3 palmitoylation ──► CMA
        │                                degradation of NLRP3
  ⇒ NOT a dead pseudoenzyme                          │
        │                              ABHD8 loss ⇒ NLRP3 stabilized ⇒
  ✗ NO known substrate                 inflammasome activation ↑
  ✗ NO ABHD8-specific assay                          │
  ✗ Specific lipid GO = IBA/IEA         ⇒ GO:1900226 (neg. reg. NLRP3), IMP
        │                              ⇒ GO:0005737 (cytoplasm), IDA
  LPAAT term mechanistically
  INCONSISTENT with hydrolase fold
```

The key interpretive point is that **the demonstrated NLRP3 role does not require ABHD8 catalysis** — a scaffold that co-localizes an acyltransferase (ZDHHC12) with its substrate (NLRP3) can be catalytically silent. Conversely, **the conserved triad does not require the NLRP3 role to make sense** — it strongly implies a real (but undiscovered) hydrolase activity, possibly acting on a lipid or ester substrate that has simply never been assayed for ABHD8. These two tracks may or may not intersect: it is possible that ABHD8's hydrolase activity contributes to some aspect of the palmitoylation/degradation cycle, but no experiment has tested this.

A useful comparator is the paralog **ABHD16A/BAT5** ([PMID: 25290914](https://pubmed.ncbi.nlm.nih.gov/25290914/)), which was a "poorly characterized" ABHD-family serine hydrolase of unknown natural substrate until activity-based protein profiling and a fluorescent glycerol assay revealed it to be a genuine lipase preferring long-chain unsaturated monoacylglycerols (MAGs), with "only marginal" lysophospholipase, DAG, or TAG activity. This illustrates two things for ABHD8: (a) family membership alone did not predict the real substrate — it turned out to be MAGs, not the phospholipids one might guess — and (b) the substrate had to be found empirically. By analogy, transferring specific lipid-pathway terms to ABHD8 by phylogeny is exactly the kind of inference that direct assay of ABHD16A overturned.

---

## Evidence Base / Evidence Matrix

| # | Citation (PMID) | Evidence type | Direction | Claim tested | Key finding | Context | Confidence & limitations |
|---|---|---|---|---|---|---|---|
| 1 | UniProt Q96I13 (database) | Structural / database | Qualifies | ABHD8 has catalytic machinery | Intact AB_hydrolase-1 domain; GHSYG elbow; triad Ser252/Asp370/His398; **no** catalytic-activity comment; only NLRP3 FUNCTION | Human, in silico | High for triad presence; database-level, no reaction assigned |
| 2 | GO annotations for Q96I13 (database) | Computational / database | Refutes (specific terms) | Specific lipid GO terms are experimental | Phosphatidic acid biosynthesis = **IBA**; catalytic activity = **IEA**; only NLRP3 (IMP) and cytoplasm (IDA) are experimental | Human | High; IBA/IEA are non-experimental by definition |
| 3 | 5 ortholog UniProt records | Structural / evolutionary | Supports (catalytic potential) | Triad under purifying selection | GHSYG + catalytic Asp + catalytic His conserved human→*Xenopus* (>360 Myr) | Human, mouse, bovine, macaque, frog | High for conservation; cannot identify substrate |
| 4 | [PMID: 39225180](https://pubmed.ncbi.nlm.nih.gov/39225180/) | Interaction / mutant phenotype | Competing (with catalysis) | Demonstrated function of ABHD8 | ABHD8 is a **scaffold** recruiting ZDHHC12 to NLRP3 → palmitoylation → CMA degradation; deficiency activates inflammasome; N protein disrupts binding | Human/mouse cells, in vivo LPS/alum | High for scaffold role; **no** catalytic assay, no Ser252Ala mutant, no lipid substrate |
| 5 | [PMID: 25290914](https://pubmed.ncbi.nlm.nih.gov/25290914/) | Direct assay (paralog) | Qualifies / methodological | Family membership predicts substrate | ABHD16A/BAT5 is a genuine MAG lipase with only marginal lysophospholipase/DAG/TAG activity — substrate found only by direct assay | Human/mouse recombinant | High for paralog; cautionary analogy, not direct ABHD8 evidence |
| 6 | [PMID: 27601076](https://pubmed.ncbi.nlm.nih.gov/27601076/) | Genetic / expression | Competing (locus context) | ABHD8 role at 19p13.1 locus | Risk SNPs regulate ABHD8 expression (breast/ovarian cancer); chromosome-conformation and luciferase link SNPs to ABHD8 promoter | Human cohorts | High for eQTL/regulation; concerns expression, not enzymatic function |
| 7 | [PMID: 33667223](https://pubmed.ncbi.nlm.nih.gov/33667223/) | Genetic (GWAS) | Competing (locus context) | ABHD8 locus disease association | 19p13.11 (rs61494113, ABHD8) suggestive for aerodigestive SqCC | Human cohorts | Moderate; association only, not enzymatic |
| 8 | [PMID: 30704525](https://pubmed.ncbi.nlm.nih.gov/30704525/) | Genetic (GWAS) | Competing (locus context) | ABHD8 locus phenotype | SNPs in/around ABHD8 associate with mtDNA copy number in neonates (rs10424198, p=1.4e-14) | Human cohorts | Moderate; association only, no mechanism |

---

## GO Curation Implications

**Lead requiring curator verification.** The evidence supports the following curation actions:

| Aspect | Term | Current evidence | Recommended action (lead) | Rationale |
|---|---|---|---|---|
| MF | GO:0003824 catalytic activity | IEA:InterPro | **Retain, generic/weak** | Triad intact, but no substrate identified |
| MF | glycerophospholipase activity | seed / family | **Do not assert** | Over-annotation risk; no direct assay |
| MF | ester hydrolase activity | seed / family | **Plausible but unproven** | Best-supported broad MF given intact triad; keep at IEA level only |
| MF | LPA acyltransferase activity | seed / family | **Likely incorrect** | Acyltransfer mechanism inconsistent with Ser-His-Asp hydrolase fold |
| BP | GO:0006654 phosphatidic acid biosynthetic process | IBA:GO_Central | **Non-core / weak; candidate for removal** | Phylogenetic inference only |
| BP | GO:1900226 negative regulation of NLRP3 inflammasome complex assembly | IMP:UniProtKB | **Retain — core function** | PMID 39225180 |
| CC | GO:0005737 cytoplasm | IDA | **Retain** | Experimental |

**Net recommendation:** Treat the **NLRP3-degradation scaffold role as the primary, experimentally supported function** (GO:1900226, IMP), with cytoplasm (GO:0005737, IDA) as the supported localization. Keep any hydrolase MF at the most generic level (GO:0003824, IEA) explicitly flagged as "catalytic potential, substrate unknown." Do **not** promote glycerophospholipase, ester-hydrolase, LPA-acyltransferase, or phosphatidic-acid biosynthesis to experimental evidence codes. Do **not** downgrade the final recommendation to bare "protein binding" — if a binding term is added, name the interactant (ZDHHC12 / NLRP3); the informative annotation is GO:1900226, which should lead.

---

## Mechanistic Scope

The immediate molecular function actually demonstrated for ABHD8 is **protein scaffolding**: it physically bridges the palmitoyltransferase ZDHHC12 to NLRP3, enabling NLRP3 palmitoylation and its subsequent CMA degradation. This is a direct gene-product activity (a binding/adaptor function), distinct from:

- **Downstream pathway consequence:** reduced NLRP3 protein, attenuated inflammasome assembly, lower IL-1β — consequences of the scaffold activity, not a separate ABHD8 activity.
- **Loss-of-function phenotype:** ABHD8 deficiency → NLRP3 stabilization → inflammasome hyperactivation — this defines the negative-regulation BP term but is an inference from loss of the scaffold.
- **Disease manifestations:** GWAS/eQTL associations (breast/ovarian cancer 19p13.1, mtDNA copy number, aerodigestive SqCC) implicate ABHD8 *expression* but are **not** evidence of enzymatic function and must not be conflated with molecular activity.

The hypothesized lipid-hydrolase activity, by contrast, is **only inferred** from domain architecture and family membership. It has a strong structural/evolutionary basis (conserved triad) but **zero direct assay evidence** in ABHD8. It must therefore be scoped as "catalytic potential, substrate unknown," not as an established molecular function.

---

## Conflicts and Alternatives

1. **Paralog/family carry-over (most important).** The specific lipid terms most plausibly originate from generic α/β-hydrolase (Pfam PF00561, InterPro IPR000073) and PANTHER (PTHR42886) inheritance rather than from ABHD8 data. The ABHD16A/BAT5 case (PMID 25290914) shows that ABHD family members can be genuine lipases, but their real substrates are often *not* what family-level inference predicts. This both *supports* the idea that ABHD8 could be a real hydrolase and *undermines* confidence in any specific transferred substrate term.

2. **LPA acyltransferase is mechanistically inconsistent.** An α/β-hydrolase Ser-His-Asp triad performs hydrolysis, not the acyl-CoA-dependent acyltransfer of a canonical LPAAT. This term is the strongest candidate for an outright annotation error.

3. **Scaffold ≠ enzyme.** The NLRP3 mechanism (PMID 39225180) explicitly frames ABHD8 as a scaffold. A scaffold can be catalytically silent; the demonstrated function does not require or test hydrolase activity. This competes with the interpretation that ABHD8's biological importance flows from catalysis.

4. **Disease-genetics confounding.** Multiple GWAS/eQTL papers (PMIDs 27601076, 33667223, 30704525, 30559148) associate the ABHD8 locus with cancer risk, mtDNA copy number, and other traits — but these reflect **regulatory/expression** effects at 19p13.1 (a locus shared with ANKLE1 and BRCA-pathway neighbors), not ABHD8 enzymatic activity. They should not be read as evidence for the lipid-catalysis hypothesis.

5. **No isoform-specific catalytic data.** No study distinguishes catalytic behavior among ABHD8 isoforms; conservation analysis was at the canonical-sequence level only.

---

## Limitations and Knowledge Gaps

| Gap | What was checked | Why it matters for curation | What would resolve it |
|---|---|---|---|
| **No ABHD8 substrate assay** | UniProt (no CATALYTIC ACTIVITY comment/reaction); PubMed (no primary hydrolase assay) | Without a substrate, all specific MF/BP lipid terms are unsupported | Activity-based protein profiling (ABPP) + substrate panel (MAG/DAG/TAG/phospholipid/LPA) on recombinant ABHD8 |
| **No catalytic-mutant test of NLRP3 role** | Full abstract of PMID 39225180 — no Ser252Ala experiment | Cannot tell whether catalysis contributes to the scaffold function | Ser252Ala (or full-triad) mutant rescue of NLRP3 degradation in ABHD8-null cells |
| **LPAAT plausibility** | Mechanistic reasoning on triad chemistry | If truly LPAAT, it would need a distinct fold/mechanism — likely an error | Direct acyltransferase assay; if negative, remove the term |
| **Localization detail** | GO CC = cytoplasm (IDA) only | Membrane/organelle context would inform substrate hypotheses | Subcellular fractionation / imaging (ER, lipid droplets, endosomes) |
| **Structure not directly modeled** | Sequence/domain annotation only; no AlphaFold pocket analysis run | Active-site pocket geometry would constrain plausible substrates | AlphaFold model + pocket/electrostatics analysis; docking of candidate lipids |
| **Ortholog sampling limited to 5 species** | 5 UniProt orthologs | Broader sampling would strengthen the selection inference | dN/dS across a deeper alignment focused on triad codons |

The overarching limitation: this analysis is literature- and sequence/annotation-based (UniProt, GO, PubMed). No wet-lab data were generated; the intact-triad inference is computational. Local repository `*-bioinformatics` analyses were intentionally withheld and not consulted. Findings are reported conservatively, distinguishing direct results (triad presence; NLRP3 scaffold assay) from inference (specific lipid substrates).

---

## Proposed Follow-up Experiments / Actions

To most efficiently separate "genuine lipid hydrolase" from "catalytically silent scaffold," in rough priority order:

1. **Activity-based protein profiling (ABPP)** of recombinant human ABHD8 with fluorophosphonate/serine-hydrolase probes — a positive label directly demonstrates an active serine hydrolase, independent of substrate identity. This is exactly how ABHD16A/BAT5 was confirmed catalytically active (PMID 25290914).
2. **Substrate panel hydrolysis assay** (fluorescent glycerol / LC-MS lipidomics) across MAG, DAG, TAG, lysophospholipids, glycerophospholipids, and LPA to identify the preferred substrate — or to show ABHD8 is inactive on all tested lipids.
3. **Catalytic-dead rescue in the NLRP3 pathway:** re-express WT vs. Ser252Ala ABHD8 in ABHD8-null cells and measure NLRP3 palmitoylation/degradation and IL-1β. Full rescue by Ser252Ala implies the scaffold role is catalysis-independent; failure implies catalysis is mechanistically coupled.
4. **AlphaFold-based active-site pocket analysis + molecular docking** of candidate lipids to predict substrate class before wet-lab assay.
5. **Dedicated LPAAT assay** (acyl-CoA + LPA → PA) to directly test the mechanistically-suspect acyltransferase annotation; a negative result justifies removing the term.
6. **Lipidomics of ABHD8-KO vs. WT cells** to detect any endogenous lipid-homeostasis role (e.g., PA levels) attributable to ABHD8 and to test the phosphatidic-acid-biosynthesis IBA prediction directly.

### Curation Leads (verify before applying)

- **Candidate reference:** PMID 39225180 — snippet to verify: *"ABHD8 acts as a scaffold to recruit palmitoyltransferase ZDHHC12 to NLRP3 for its palmitoylation as well as subsequent CMA-mediated degradation."* → supports retaining GO:1900226 (IMP) as core and a scaffold/protein-bridging annotation over lipase.
- **Candidate reference (methodological/paralog):** PMID 25290914 — establishes the ABPP + substrate-panel assay standard that ABHD8 lacks.
- **Action-change leads:** (a) do not elevate glycerophospholipase / ester hydrolase / LPAAT beyond IEA; (b) flag LPA-acyltransferase as likely incorrect; (c) mark GO:0006654 (phosphatidic acid biosynthesis) as IBA / non-core / candidate removal; (d) retain GO:1900226 and GO:0005737.
- **Suggested curator questions:** Is the specific lipid MF an author statement or purely pipeline inference? Was any triad mutant tested for the NLRP3 phenotype? Where did the LPAAT assignment originate?

---

## Conclusion

Human ABHD8 (Q96I13) retains a fully intact, evolutionarily conserved serine-hydrolase catalytic triad, so it is **not** a dead pseudoenzyme and the seed's caution against inferring catalytic loss from adaptor function is justified. However, **no ABHD8-specific biochemical assay demonstrates any lipid substrate**: the specific terms (glycerophospholipase, ester hydrolase, LPA acyltransferase, phosphatidic acid biosynthesis, lipid homeostasis) are unproven family/phylogenetic inferences (IEA/IBA), with the LPA-acyltransferase term mechanistically inconsistent with the hydrolase fold. The only experimentally demonstrated function is the **NLRP3-degradation scaffold/adaptor role** (recruiting ZDHHC12 to NLRP3; GO:1900226 IMP, PMID 39225180). Curation should retain that core term and localization, keep lipid catalysis at most as generic hydrolase potential, and treat the specific lipid annotations as over-annotations pending direct substrate assays.


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)