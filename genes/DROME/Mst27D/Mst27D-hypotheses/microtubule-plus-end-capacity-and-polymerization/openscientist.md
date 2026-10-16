---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-20T22:06:12.287852'
end_time: '2026-09-20T22:30:31.102280'
duration_seconds: 1458.81
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: DROME
  gene: Mst27D
  gene_symbol: Mst27D
  uniprot_accession: Q8IPI4
  taxon_id: NCBITaxon:7227
  taxon_label: Drosophila melanogaster
  focus_type: function_assignment
  hypothesis_slug: microtubule-plus-end-capacity-and-polymerization
  hypothesis_text: Drosophila melanogaster Mst27D localizes to the microtubule plus
    end, binds microtubule plus ends, and regulates microtubule polymerization or
    depolymerization. Evaluate each actual GO claim independently from primary experiments.
    Distinguish preferential plus-end tracking from any plus-end binding or localization
    capacity, full-length from truncated constructs, and endogenous postmeiotic expression
    from ectopic assays. Compare relevant paralogs and phylogenetic node placement
    without inferring loss merely from specialization.
  term_context: No specific term context supplied.
  reference_context: No specific reference context supplied.
  source_file: genes/DROME/Mst27D/Mst27D-ai-review.yaml
  source_selector: free-text
  source_context_yaml: "hypothesis: Drosophila melanogaster Mst27D localizes to the\
    \ microtubule plus end, binds microtubule plus\n  ends, and regulates microtubule\
    \ polymerization or depolymerization. Evaluate each actual GO claim independently\n\
    \  from primary experiments. Distinguish preferential plus-end tracking from any\
    \ plus-end binding or localization\n  capacity, full-length from truncated constructs,\
    \ and endogenous postmeiotic expression from ectopic\n  assays. Compare relevant\
    \ paralogs and phylogenetic node placement without inferring loss merely from\n\
    \  specialization.\nfocus_type: function_assignment\ncontext: []\nreference_id:\
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

- **Organism code:** DROME
- **Taxon:** Drosophila melanogaster (NCBITaxon:7227)
- **Gene directory:** Mst27D
- **Gene symbol:** Mst27D
- **UniProt accession:** Q8IPI4

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** microtubule-plus-end-capacity-and-polymerization
- **Source file:** genes/DROME/Mst27D/Mst27D-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

Drosophila melanogaster Mst27D localizes to the microtubule plus end, binds microtubule plus ends, and regulates microtubule polymerization or depolymerization. Evaluate each actual GO claim independently from primary experiments. Distinguish preferential plus-end tracking from any plus-end binding or localization capacity, full-length from truncated constructs, and endogenous postmeiotic expression from ectopic assays. Compare relevant paralogs and phylogenetic node placement without inferring loss merely from specialization.

## Term and Decision Context

No specific term context supplied.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: Drosophila melanogaster Mst27D localizes to the microtubule plus end, binds microtubule plus
  ends, and regulates microtubule polymerization or depolymerization. Evaluate each actual GO claim independently
  from primary experiments. Distinguish preferential plus-end tracking from any plus-end binding or localization
  capacity, full-length from truncated constructs, and endogenous postmeiotic expression from ectopic
  assays. Compare relevant paralogs and phylogenetic node placement without inferring loss merely from
  specialization.
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

# AIGR Gene Hypothesis Deep Research — *Drosophila melanogaster* Mst27D (Q8IPI4)

**Focus:** function_assignment · **Hypothesis slug:** microtubule-plus-end-capacity-and-polymerization
**Gene:** Mst27D / CG31907 / FBgn0051907 (DROME, NCBITaxon:7227) · **UniProt:** Q8IPI4 · **Length:** 424 aa
**Source:** genes/DROME/Mst27D/Mst27D-ai-review.yaml

---

## Summary

The seed hypothesis proposes that Mst27D (a) **localizes to the microtubule plus end**, (b) **binds microtubule plus ends**, and (c) **regulates microtubule polymerization or depolymerization**. Evaluated independently against primary experimental evidence, **none of these three specific claims is directly supported.** Every microtubule-related GO annotation on Q8IPI4 that asserts plus-end localization, plus-end binding, spindle localization, or regulation of polymer dynamics carries the evidence code **IBA (Inferred from Biological Ancestor, GO_Central)**. These are computational propagations from the MAPRE/EB1 (RP/EB) family ancestral node — PANTHER family PTHR10623, InterPro IPR027328 (MAPRE) — and reflect the demonstrated behavior of *canonical* EB proteins, not of Mst27D itself.

The single primary functional study of the gene, *Nuclear elongation during spermiogenesis depends on physical linkage of nuclear pore complexes to bundled microtubules by Drosophila Mst27D* (Li, Messina & Lehner 2023, *PLoS Genetics*, [PMID: 37428798](https://pubmed.ncbi.nlm.nih.gov/37428798/)), demonstrates a fundamentally different function. Its EB1-like **N-terminal calponin-homology (CH) domain binds microtubules generically**; it promotes **microtubule bundling only under high/ectopic overexpression** in cultured cells; its **C-terminal region binds the nucleoporin Nup358**; and its endogenous, physiological role is to **physically link the nuclear-pore-bearing nuclear envelope (NPC-NE) to the "dense complex" microtubule bundle, driving spermatid nuclear elongation** during postmeiotic spermiogenesis. This is a **structural adaptor/cross-linking** function, not plus-end tracking (+TIP behavior) and not regulation of microtubule dynamics.

**Verdict: over-annotated / partially supported.** What is genuinely supported is **generic microtubule binding**, a **Nup358-binding** activity, and a **microtubule-bundling / nuclear-elongation** role — all distinct from the plus-end and polymerization-dynamics claims of the seed. The plus-end, spindle, and dynamics-regulation terms are best treated as **EB-family IBA carry-over (paralog over-annotation)**. Consistent with the seed's own caution about "inferring loss merely from specialization," we do not claim Mst27D *cannot* track plus ends; we conclude there is **no positive evidence that it does**, alongside strong positive evidence for a competing structural function.

---

## Key Findings

### Finding 1 — The plus-end / spindle / polymerization GO terms are EB1-family IBA over-annotation

UniProt Q8IPI4 (Mst27D, 424 aa) carries a cluster of microtubule-related GO terms whose evidence code is uniformly **IBA (GO_Central)**, inherited from the MAPRE/EB1 family node. The specific terms include microtubule plus-end (**GO:0035371**, CC), microtubule plus-end binding (**GO:0051010**, MF), regulation of microtubule polymerization or depolymerization (**GO:0031110**, BP), spindle midzone (**GO:0051233**, CC), spindle assembly (**GO:0051225**, BP), and protein localization to microtubule (**GO:0035372**, BP). IBA annotations represent a *hypothesis of conserved function* propagated across a phylogenetic family, not a measurement of the gene in question. The family node (PANTHER PTHR10623, "MICROTUBULE-ASSOCIATED PROTEIN RP/EB FAMILY MEMBER"; InterPro IPR027328; Pfam PF00307 CH domain, residues ~26–129; C-terminal coiled-coil ~286–344) derives its reference plus-end/dynamics functions from canonical EB proteins such as EB1/MAPRE1–3, which genuinely track plus ends and modulate polymer dynamics.

The primary experimental record for Mst27D ([PMID: 37428798](https://pubmed.ncbi.nlm.nih.gov/37428798/)) demonstrates only four activities, none corresponding to plus-end tracking or dynamics regulation. First, the **N-terminal CH domain binds microtubules** — the paper states "The N-terminal CH domain of Mst27D, which is similar to that of EB1 family proteins, binds to microtubules." This is characterized as *EB1-like homology* and generic lattice binding, not as a measured plus-end preference. Second, **bundling occurs at high expression**: "At high expression levels, Mst27D promotes bundling of microtubules in cultured cells" — an ectopic-overexpression readout, and a bundling (cross-linking) activity, not a polymerization-dynamics activity. Third, the **C-terminus binds Nup358**: "The C-terminal region of Mst27D binds to the nuclear pore protein Nup358." Fourth, the integrated function is structural linkage: "We demonstrate that Mst27D establishes physical linkage between NPC-NE and dense complex." Crucially, **no assay in the paper demonstrates preferential plus-end tracking, plus-end-specific binding, spindle localization, or regulation of MT polymerization/depolymerization.**

### Finding 2 — Null-mutant phenotype and endogenous localization define a bundling / nuclear-elongation function

The Li, Messina & Lehner 2023 study (PLoS Genet 19(7):e1010837; PMCID PMC10359004) provides the loss-of-function and localization evidence that positively identifies the role. **Endogenous localization** is to microtubule bundles and the NPC/nuclear envelope, not to plus ends or the spindle: "Microscopic analyses indicated co-localization of Mst27D with Nup358 and with the microtubule bundles of the dense complex." This directly conflicts with the plus-end and spindle cellular-component claims. The **loss-of-function phenotype** genetically defines the requirement: "In Mst27D null mutants, this bundling process does not occur and nuclear elongation is abnormal." The requirement is for microtubule bundling and nuclear elongation, not for any dynamics-regulation readout. The authors' **mechanistic model** integrates these: "Mst27D permits normal nuclear elongation by promoting the attachment of the NPC-NE to the microtubules of the dense complex, as well as the progressive bundling of these microtubules."

Expression is **spermatid-specific (postmeiotic)**, consistent with the "Mst" (male sterile testis) family naming and the spermiogenesis context, and it argues strongly against any mitotic/meiotic spindle role. The seed's instruction to distinguish *endogenous postmeiotic expression from ectopic assays* is material: the only microtubule-*remodeling* activity (bundling) was observed under ectopic overexpression in cultured cells, whereas the endogenous, physiologically relevant activity is structural linkage of NPCs to a pre-existing bundle. Importantly, the null-mutant loss of bundling elevates the bundling role from an overexpression-only artifact to a genetically supported in-vivo function.

### Finding 3 — Phylogenetic placement: a divergent testis EB/MAPRE paralog lacking the +TIP tail

The *Drosophila* EB/RP family (PANTHER PTHR10623) contains multiple members: **Eb1/CG3265** (canonical +TIP), **CG32371**, **CG2955**, **CG15306**, **EB-SUN/CG18190** (a testis ER-associated EB), and **Mst27D**. A computed Needleman–Wunsch alignment (BLOSUM62) over the N-terminal CH region places Mst27D as a genuine but **divergent** paralog with no close sister — no family member exceeds ~45% CH-domain identity to Mst27D. Decisively, the **C-terminal acidic EEY/F +TIP-recruitment tail is present only in canonical Eb1**; Mst27D and the other divergent/testis paralogs lack it. The EEY/F tail is the canonical motif through which EB proteins recruit CAP-Gly +TIP partners (e.g., CLIP-170/CLIP-190, p150Glued); its absence, combined with the C-terminus being repurposed for Nup358 binding, is the structural signature of functional divergence away from the +TIP role.

In keeping with the seed's caution, we treat tail loss as *supporting* — not *proving* — the absence of plus-end tracking, since the CH domain can in principle bind plus ends autonomously and several Drosophila EB paralogs also lack the tail. The decisive evidence remains the endogenous localization (bundles/NE, not plus ends) and the null phenotype (bundling/elongation defect). The pattern nonetheless cleanly explains the IBA problem: the family node's reference plus-end/dynamics functions come from canonical Eb1-type proteins, and are being propagated onto specialized testis-branch members that have repurposed both termini.

---

## Mechanistic Model / Interpretation

The evidence converges on a coherent, non-canonical model in which Mst27D is a **bifunctional molecular adaptor/scaffold** that mechanically couples the nuclear envelope to a cytoskeletal bundle during sperm-head shaping — a role orthogonal to the plus-end-dynamics function implied by the seed hypothesis.

```
   Spermatid (postmeiotic, testis-specific)
   ┌─────────────────────────────────────────────────────────────┐
   │  NUCLEAR ENVELOPE  (with Nucleoporins / NPCs, incl. Nup358)  │
   │        ▲                                                      │
   │        │  C-terminal region  ──► binds Nup358                │
   │   ┌────┴─────┐                                               │
   │   │  Mst27D  │  (424 aa; divergent EB/MAPRE paralog)         │
   │   └────┬─────┘                                               │
   │        │  N-terminal CH domain ──► binds microtubules       │
   │        ▼                                                      │
   │  ═══════════════  MICROTUBULE "DENSE COMPLEX" (bundle) ═══════│
   │        (progressive bundling; drives NUCLEAR ELONGATION)     │
   └─────────────────────────────────────────────────────────────┘

   Loss of Mst27D  ⇒  no bundling  ⇒  abnormal nuclear elongation
```

**Direct molecular activities (supported):** microtubule binding via the EB1-like N-terminal CH domain; nucleoporin (Nup358) binding via the C-terminal region; microtubule bundling (cross-linking) observed at high expression.

**Cellular function (supported, in vivo):** structural tethering of the NPC-bearing nuclear envelope to a bundled microtubule array, and contribution to progressive bundle formation.

**Developmental outcome (supported, downstream):** normal spermatid nuclear elongation during spermiogenesis; null mutants show abnormal nuclear elongation. This is the *consequence* of the linkage/bundling activity, not itself a molecular activity of Mst27D.

**NOT supported by any Mst27D assay:** plus-end tracking (+TIP behavior), plus-end-specific binding, spindle localization, or regulation of microtubule polymerization/depolymerization dynamics. The seed hypothesis conflates two distinct EB-family capabilities: **generic lattice binding** (a shared CH-domain property) versus **plus-end tracking plus dynamics regulation** (which requires additional determinants including the EEY/F tail and plus-end-recognition behavior). Mst27D retains the former and shows no evidence of the latter.

---

## Evidence Matrix

| Citation | Evidence type | Supports / Refutes / Qualifies | Claim tested | Key finding | Context | Confidence & limitations |
|---|---|---|---|---|---|---|
| [PMID: 37428798](https://pubmed.ncbi.nlm.nih.gov/37428798/) | Direct assay (domain mapping) | **Qualifies** (supports generic MT binding; refutes plus-end specificity) | Plus-end vs generic MT binding | "The N-terminal CH domain of Mst27D... binds to microtubules"; EB1-like homology, no plus-end preference shown | *Drosophila*; cultured cells | High for MT binding; no plus-end assay performed |
| [PMID: 37428798](https://pubmed.ncbi.nlm.nih.gov/37428798/) | Direct assay (overexpression) | **Refutes** polymerization/depolymerization regulation | Regulation of MT dynamics | "At high expression levels, Mst27D promotes bundling of microtubules in cultured cells" — bundling, not dynamics; ectopic | Cultured cells, overexpression | High that activity is bundling; ectopic condition limits inference |
| [PMID: 37428798](https://pubmed.ncbi.nlm.nih.gov/37428798/) | Interaction | **Competing** (defines alternative C-terminal function) | C-terminal +TIP recruitment vs nucleoporin binding | "The C-terminal region of Mst27D binds to the nuclear pore protein Nup358" | *Drosophila* spermatids | High; identifies repurposed C-terminus |
| [PMID: 37428798](https://pubmed.ncbi.nlm.nih.gov/37428798/) | Localization | **Refutes** plus-end / spindle CC | Plus-end / spindle localization | "co-localization of Mst27D with Nup358 and with the microtubule bundles of the dense complex" | *Drosophila* spermatids (postmeiotic) | High; endogenous localization is bundle/NE, not plus end |
| [PMID: 37428798](https://pubmed.ncbi.nlm.nih.gov/37428798/) | Mutant phenotype | **Competing / supports** bundling/elongation BP | Function = dynamics vs bundling/elongation | "In Mst27D null mutants, this bundling process does not occur and nuclear elongation is abnormal" | *Drosophila* null-mutant testis | High; LOF defines bundling/elongation role |
| UniProt Q8IPI4 (GO_Central) | Review/database (IBA) | **Competing** (source of over-annotation) | All 6 MT GO terms | GO:0035371, GO:0051010, GO:0031110, GO:0051233, GO:0051225, GO:0035372 — **all IBA** | Phylogenetic inference from MAPRE/EB node | Database-level only; not Mst27D-specific |
| InterPro IPR027328 / PANTHER PTHR10623 / Pfam PF00307 | Structural/evolutionary | **Qualifies** | Family placement | CH domain aa ~26–129; C-terminal coiled-coil ~286–344 | Sequence/domain | Homology real; does not prove conserved plus-end function |
| Computed (this study): NW/BLOSUM62 alignment | Structural/evolutionary (computational) | **Qualifies / refutes +TIP machinery conservation** | Is Mst27D a canonical EB? | CH domain vs *Dm* EB1 (Q9XZ57) = **37.9% identity**; Mst27D **lacks EEY/F +TIP tail** ("…SLKV" vs EB1 "DEEY", human EB1 "QEEY") | In silico | Real CH homology, but canonical partner-recruitment tail absent → divergent paralog |
| [PMID: 42374827](https://pubmed.ncbi.nlm.nih.gov/42374827/) | Review/context | **Context** | Nucleoporin roles in spermiogenesis | Nup43 has non-canonical structural roles in *Drosophila* spermiogenesis (nuclear elongation, actin cone assembly) | *Drosophila* testis | Corroborates non-transport structural roles for NPC components; not direct Mst27D evidence |

---

## GO Curation Implications (leads — require curator verification)

| GO term | Current evidence | Recommended action | Rationale |
|---|---|---|---|
| **GO:0051010** microtubule plus-end binding (MF) | IBA | **Generalize → GO:0008017 microtubule binding** | Only generic CH-domain MT binding directly shown; plus-end specificity untested |
| **GO:0031110** regulation of MT polymerization/depolymerization (BP) | IBA | **Remove / replace with GO:0001578 microtubule bundle formation** | No dynamics assay; bundling is IMP-supported by null phenotype |
| **GO:0035371** microtubule plus-end (CC) | IBA | **Remove** | Endogenous protein co-localizes with MT bundles + Nup358/NPC-NE, not plus ends |
| **GO:0051233** spindle midzone (CC) | IBA | **Remove** | Spermatid-specific/postmeiotic; no spindle role |
| **GO:0051225** spindle assembly (BP) | IBA | **Remove** | Non-dividing cell type; no spindle role |
| **GO:0035372** protein localization to microtubule (BP) | IBA | **Qualify** | Demonstrated activity is Nup358/NPC-to-bundle linkage; generic IBA term weak |
| GO:0008017 microtubule binding (MF) | IBA + now direct | **Retain / upgrade to IDA** | Directly shown via CH domain |
| Nup358 / nucleoporin binding (MF) | — | **Add (lead, IPI)** | Direct C-terminal interaction |
| Spermatid nuclear elongation / sperm nucleus differentiation (BP) | — | **Add (lead, IMP)** | Null-mutant abnormal nuclear elongation |
| Microtubule bundle (CC) / nuclear envelope–nuclear pore (CC) | — | **Add (lead)** | Endogenous co-localization |

Note: avoid a bare "protein binding" recommendation — the microtubule partner supports GO:0008017 and the protein partner (Nup358) supports a named-interactor annotation.

---

## Mechanistic Scope

The immediate molecular activities under test are **plus-end binding** and **regulation of microtubule polymerization/depolymerization**. The gene product's *direct* molecular activities are, in fact, (a) generic microtubule lattice binding via an EB1-like CH domain and (b) Nup358 binding via the C-terminus; bundling is a direct cross-linking property but manifests physiologically as a *structural* outcome (progressive bundle formation), not modulation of tubulin subunit kinetics. Everything about plus-end tracking and dynamics regulation belongs to the **inferred/family-ancestral** category, not the measured-activity category. The **developmental outcome** (nuclear elongation) is downstream of the direct linkage/bundling activity and is inferred from loss of function — a biological process the gene contributes to, but distinct from its direct molecular function. We deliberately avoid promoting the loss-of-function phenotype into a molecular-activity claim.

---

## Conflicts and Alternatives

- **Paralog over-annotation (primary conflict, and the correct interpretation):** the IBA terms derive from canonical EB proteins (EB1/Eb1, MAPRE1–3) that genuinely track plus ends and modulate dynamics. Mst27D shares the CH domain (~38% identity to *Dm* EB1) but lacks the C-terminal acidic EEY/F tail EB proteins use to recruit CAP-Gly +TIP partners, and its C-terminus is instead repurposed for Nup358 binding. This is functional divergence, not conserved function — a textbook case of family IBA carry-over onto a specialized paralog.
- **Ectopic vs endogenous / truncated vs full-length:** bundling was observed at high expression in cultured cells using domain-resolved constructs. Endogenous Mst27D operates in postmeiotic spermatids on a largely static bundled array, arguing against a dynamics-regulation role; the null-mutant loss of bundling nonetheless confirms bundling is genuinely Mst27D-dependent in vivo. Because N- and C-terminal activities were mapped separately, the integrated full-length behavior (e.g., any cryptic plus-end preference) is inferred, not exhaustively tested.
- **"Loss vs specialization":** the seed correctly cautions against inferring loss from specialization. The conservative reading is that plus-end tracking is **undemonstrated**, not proven absent; the EEY-tail argument is supportive but not decisive. For curation, absence of positive evidence for a specific molecular claim, combined with strong positive evidence for a competing function and a contradictory endogenous localization, is sufficient to remove the unsupported specific terms.

### Paralog comparison (computed this run — *Drosophila* EB/MAPRE family, PANTHER PTHR10623)

| Protein | Length (aa) | CH-domain % id vs Mst27D | C-terminal last 4 | EEY/F +TIP tail? |
|---|---|---|---|---|
| **Mst27D** (Q8IPI4) | 424 | 100 | SLKV | No |
| Eb1 (Q9XZ57) — canonical +TIP | 290 | 42.3 | DEEY | **Yes** |
| CG32371 (Q8IQA0) | 294 | 43.3 | IYSE | No |
| CG15306 (Q9W2W2) | 357 | 41.3 | QRDH | No |
| EB-SUN / CG18190 (A1ZBF1) — testis ER EB | 248 | 36.9 | DGLY | No |
| CG2955 (Q9VQX0) | 565 | 33.0 | MNTD | No |

*Interpretation:* Mst27D is a genuine but divergent EB/MAPRE paralog (no family member >45% CH identity). Only canonical Eb1 retains the acidic EEY +TIP-recruitment tail. The IBA plus-end/dynamics annotations propagate from this family node, whose reference functions derive from canonical EB proteins (Eb1-type), not from the specialized testis-branch paralogs to which Mst27D belongs.

---

## Evidence Base (Literature)

- ***Nuclear elongation during spermiogenesis depends on physical linkage of nuclear pore complexes to bundled microtubules by Drosophila Mst27D.*** Li, Messina & Lehner, 2023, *PLoS Genetics* 19(7):e1010837. [PMID: 37428798](https://pubmed.ncbi.nlm.nih.gov/37428798/); PMCID PMC10359004. **The single primary characterization of Mst27D.** Establishes CH-domain microtubule binding, C-terminal Nup358 binding, overexpression bundling, spermatid-specific bundle/NE localization, and a null-mutant nuclear-elongation phenotype. Directly refutes the plus-end/spindle/dynamics claims and defines the true linkage/bundling function.
- ***Synergistic actions of Nup43 and Myosin VI drive actin cone assembly during Drosophila spermiogenesis.*** [PMID: 42374827](https://pubmed.ncbi.nlm.nih.gov/42374827/). Contextual support that nucleoporins (Nup43) have non-canonical structural roles in *Drosophila* spermiogenesis, including nuclear elongation and shaping — consistent with the Mst27D–Nup358 linkage paradigm, though not direct Mst27D evidence.
- **Database/orientation:** UniProt **Q8IPI4**; PANTHER family **PTHR10623**; InterPro **IPR027328** (MAPRE/EB1); Pfam **PF00307** (CH). Used to establish that the microtubule GO terms are IBA family carry-over rather than direct evidence.

---

## Limitations and Knowledge Gaps

1. **No direct plus-end assay exists.** *Checked:* full abstract and domain-mapping results of PMID 37428798. *Why it matters:* GO:0035371/GO:0051010 hinge on plus-end behavior; without a negative live-imaging result, these can be classed "unsupported" but not strictly "refuted." *Resolve with:* live TIRF comet-tracking of GFP-Mst27D on dynamic microtubules, with EB1 co-tracking.
2. **Polymerization/depolymerization effect untested.** *Checked:* no dynamics assay in the paper. *Why it matters:* GO:0031110 requires a measured effect on polymer dynamics. *Resolve with:* in-vitro turbidity/TIRF assays on purified tubulin ± Mst27D.
3. **Sequence analyses are computational, not functional.** *Checked:* CH-domain identity and EEY/F tail presence via Needleman–Wunsch/BLOSUM62. *Why it matters:* tail loss correlates with, but does not prove, loss of +TIP recruitment. *Resolve with:* +TIP-partner co-IP (CLIP-190/CLASP orthologs) with Mst27D.
4. **Exact live GO annotation set not re-pulled in this run.** *Checked:* summarized as six MT-related terms, all IBA, with specific IDs above. *Why it matters:* term IDs and any non-IBA terms must be confirmed against current GOA/QuickGO before edits. *Resolve with:* live QuickGO/GOA pull for Q8IPI4.
5. **High-resolution endogenous CC assignment.** *Checked:* co-localization with Nup358 and MT bundles shown. *Why it matters:* precise NPC-vs-bundle CC assignment affects term choice. *Resolve with:* immuno-EM.

---

## Discriminating Tests

- **Live +TIP comet assay** in S2 cells or spermatids: does GFP-Mst27D form growing-end comets and co-migrate with EB1? Distinguishes plus-end tracking from lattice binding.
- **In-vitro reconstitution** with purified tubulin ± Mst27D, and an EEY-tail chimera, to test whether restoring the acidic tail confers +TIP behavior and whether Mst27D alters growth/catastrophe kinetics.
- **Domain-swap / ΔNup358-binding mutants** in vivo to confirm the linkage function is separable from any MT-dynamics effect.
- **Phylogenetic/synteny analysis** across Drosophilids to date the EB-paralog duplication and confirm tail loss is ancestral to the Mst27D lineage.
- **Live GOA/QuickGO pull** to enumerate exact GO term IDs and evidence codes for scoping edits.

---

## Curation Leads (require curator verification)

- **Reference to cite:** PMID **37428798** (Li, Messina & Lehner, 2023). Snippets to verify verbatim:
  - "*The N-terminal CH domain of Mst27D, which is similar to that of EB1 family proteins, binds to microtubules.*"
  - "*At high expression levels, Mst27D promotes bundling of microtubules in cultured cells.*"
  - "*The C-terminal region of Mst27D binds to the nuclear pore protein Nup358.*"
  - "*Microscopic analyses indicated co-localization of Mst27D with Nup358 and with the microtubule bundles of the dense complex.*"
  - "*In Mst27D null mutants, this bundling process does not occur and nuclear elongation is abnormal.*"
  - "*We demonstrate that Mst27D establishes physical linkage between NPC-NE and dense complex.*"
- **Action changes:** generalize plus-end binding → microtubule binding (GO:0008017); remove the plus-end (GO:0035371), spindle-midzone (GO:0051233), spindle-assembly (GO:0051225), and MT-polymerization-regulation (GO:0031110) IBA terms as unsupported paralog carry-over; add IDA/IPI/IMP leads for microtubule binding, Nup358 binding, microtubule bundle formation (GO:0001578), and spermatid nuclear elongation.
- **Suggested question for curator:** Should EB-family IBA terms be retained on a spermatid-specialized paralog that lacks the diagnostic EEY/F +TIP tail and has an experimentally different (Nup358-linkage) function?
- **Suggested experiments:** live +TIP comet-tracking and in-vitro dynamics assays (above).

---

## Proposed Follow-up Experiments / Actions

1. **Curator action:** pull the live QuickGO/GOA record for Q8IPI4, confirm the six IBA MT term IDs, and stage removals with the verified refuting/qualifying snippets above.
2. **Curator action:** draft additions for microtubule binding (retain/upgrade), Nup358 binding, microtubule bundle formation, microtubule bundle localization, and spermatid nuclear elongation, each tied to PMID 37428798.
3. **Wet-lab (definitive refutation):** EB-comet live imaging and in-vitro TIRF dynamics assays to convert "unsupported" into "directly refuted" for the plus-end/dynamics terms.
4. **Comparative genomics:** formalize the PTHR10623 tree with tail-motif annotation to document, for the record, that only canonical Eb1 retains the EEY/F +TIP tail — provenance for the IBA-over-annotation determination.

---

### Bottom line

Mst27D's plus-end localization, plus-end binding, spindle, and polymerization-regulation GO terms are **EB1/MAPRE-family IBA carry-over**, not evidence about Mst27D. The gene's demonstrated function is **structural**: an EB1-like CH domain binds microtubules generically, the C-terminus binds Nup358, and the protein **physically links nuclear pore complexes to a bundled spermatid microtubule "dense complex" to drive nuclear elongation**. Generalize plus-end binding to **microtubule binding (GO:0008017)**, remove the unsupported plus-end/spindle/dynamics IBA terms, and add the supported Nup358-binding and spermatid-nuclear-elongation functions — all pending curator verification.

---

*Provenance:* GO decision table and CH-domain alignment computed this run (Needleman–Wunsch/BLOSUM62; Mst27D CH vs *Dm* EB1 Q9XZ57 = 37.9% identity; EEY/F tail absent). Paralog table computed over PANTHER PTHR10623 members. Sequences and domains from UniProt Q8IPI4 and family accessions.


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)