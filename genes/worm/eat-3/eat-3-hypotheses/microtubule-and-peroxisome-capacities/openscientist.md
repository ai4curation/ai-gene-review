---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-20T20:11:17.027635'
end_time: '2026-09-20T20:29:01.830822'
duration_seconds: 1064.8
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: worm
  gene: eat-3
  gene_symbol: eat-3
  uniprot_accession: Q18965
  taxon_id: NCBITaxon:6239
  taxon_label: Caenorhabditis elegans
  focus_type: function_assignment
  hypothesis_slug: microtubule-and-peroxisome-capacities
  hypothesis_text: Caenorhabditis elegans EAT-3 has microtubule localization/binding
    (PTN000170013) or participates in peroxisome fission (PTN008520527). Evaluate
    exact target lineage and whether targeting, mature membrane topology, processing/isoforms,
    sequence or direct functional assays establish loss or retain these ancestral
    capacities alongside mitochondrial inner-membrane fusion. Assess the three terms
    independently. Primary mitochondrial localization and absent worm-specific tests
    alone do not refute a considered ancestral IBD. Do not equate absence of a shared
    organelle phenotype with proof of no conditional physical interaction.
  term_context: No specific term context supplied.
  reference_context: No specific reference context supplied.
  source_file: genes/worm/eat-3/eat-3-ai-review.yaml
  source_selector: free-text
  source_context_yaml: "hypothesis: Caenorhabditis elegans EAT-3 has microtubule localization/binding\
    \ (PTN000170013) or participates\n  in peroxisome fission (PTN008520527). Evaluate\
    \ exact target lineage and whether targeting, mature membrane\n  topology, processing/isoforms,\
    \ sequence or direct functional assays establish loss or retain these ancestral\n\
    \  capacities alongside mitochondrial inner-membrane fusion. Assess the three\
    \ terms independently. Primary\n  mitochondrial localization and absent worm-specific\
    \ tests alone do not refute a considered ancestral\n  IBD. Do not equate absence\
    \ of a shared organelle phenotype with proof of no conditional physical interaction.\n\
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
citation_count: 6
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

- **Organism code:** worm
- **Taxon:** Caenorhabditis elegans (NCBITaxon:6239)
- **Gene directory:** eat-3
- **Gene symbol:** eat-3
- **UniProt accession:** Q18965

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** microtubule-and-peroxisome-capacities
- **Source file:** genes/worm/eat-3/eat-3-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

Caenorhabditis elegans EAT-3 has microtubule localization/binding (PTN000170013) or participates in peroxisome fission (PTN008520527). Evaluate exact target lineage and whether targeting, mature membrane topology, processing/isoforms, sequence or direct functional assays establish loss or retain these ancestral capacities alongside mitochondrial inner-membrane fusion. Assess the three terms independently. Primary mitochondrial localization and absent worm-specific tests alone do not refute a considered ancestral IBD. Do not equate absence of a shared organelle phenotype with proof of no conditional physical interaction.

## Term and Decision Context

No specific term context supplied.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: Caenorhabditis elegans EAT-3 has microtubule localization/binding (PTN000170013) or participates
  in peroxisome fission (PTN008520527). Evaluate exact target lineage and whether targeting, mature membrane
  topology, processing/isoforms, sequence or direct functional assays establish loss or retain these ancestral
  capacities alongside mitochondrial inner-membrane fusion. Assess the three terms independently. Primary
  mitochondrial localization and absent worm-specific tests alone do not refute a considered ancestral
  IBD. Do not equate absence of a shared organelle phenotype with proof of no conditional physical interaction.
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

# EAT-3 (Q18965) Function-Assignment Review: Microtubule Binding and Peroxisome Fission Capacities

**Gene:** *eat-3* / EAT-3 (UniProt Q18965) — *Caenorhabditis elegans* (NCBITaxon:6239)
**Focus:** function_assignment — hypothesis slug `microtubule-and-peroxisome-capacities`
**Contested terms:** GO:0008017 microtubule binding (PANTHER node PTN000170013); GO:0016559 peroxisome fission (PANTHER node PTN008520527); assessed independently alongside GO:0008053 mitochondrial inner-membrane fusion (OPA1-clade node PTN007514526).

---

## Summary

**Executive verdict: OVER-ANNOTATED (both contested terms) — the microtubule-binding and peroxisome-fission assignments are paralog-driven deep-node over-propagations, while mitochondrial inner-membrane fusion is EAT-3's genuine, directly supported core function.**

EAT-3 is the *C. elegans* ortholog of human OPA1 / yeast Mgm1, a mitochondrial dynamin-family GTPase whose experimentally established role is fusion of the mitochondrial **inner** membrane. Loss-of-function *eat-3* mutants fragment their mitochondria and show inner-membrane septae — a phenotype diagnostic of an inner-membrane fusion defect ([PMID: 18454199](https://pubmed.ncbi.nlm.nih.gov/18454199/)) — and CED-9 promotes FZO-1/EAT-3–dependent fusion ([PMID: 19704021](https://pubmed.ncbi.nlm.nih.gov/19704021/)). This mitochondrial-fusion annotation (GO:0008053) is well supported by worm IMP evidence and should be retained.

The two contested capacities do not survive scrutiny. Tracing the GO provenance in QuickGO and parsing the PANTHER PTHR11566 family tree shows that **microtubule binding is annotated at the family ROOT node (PTN000170013)** — a node experimentally seeded by classical endocytic dynamin (*Drosophila* shibire, FB:FBgn0003392) — and **peroxisome fission at an ancestral DRP1-branch node (PTN008520527)** seeded by genuine fission dynamins (human DNM1L/DRP1 O00429, mouse Dnm1l MGI:1921256, yeast DNM1/VPS1 SGD S000001709/S000003924). Both nodes are strict *ancestors* of EAT-3's own OPA1 subfamily node (PTN007514526, "DYNAMIN-LIKE 120 KDA PROTEIN, MITOCHONDRIAL"), so EAT-3 inherited these terms only by deep-node IBD/IBA propagation across the whole dynamin superfamily, not from any evidence specific to the OPA1 clade.

Two independent mechanistic arguments corroborate the phylogenetic verdict. First, **domain architecture**: EAT-3 carries only Dynamin_N (GTPase) + OPA1_C and *lacks* the pleckstrin-homology (PH) domain, GTPase effector domain (GED), and proline-rich domain (PRD) that classical dynamin uses to engage microtubules and membranes. Second, **topology**: EAT-3 bears a mitochondrial transit peptide and is anchored in the inner membrane facing the intermembrane space (IMS) — a compartment physically incompatible with cytosolic microtubule binding or peroxisomal-membrane scission. Honoring the seed hypothesis's cautions, primary mitochondrial localization alone does not *refute* a conditional physical interaction; the recommended curation action is therefore to treat both terms as **paralog-driven over-annotations that should not be asserted** (rather than claiming positive proof of impossibility), assessed independently from the robustly supported fusion function.

---

## Key Findings

### Finding 1 — Microtubule-binding and peroxisome-fission IBA terms trace to paralog source proteins at deep ancestral nodes

QuickGO provenance for Q18965 (all under GO_REF:0000033, PANTHER PTHR11566) is unambiguous about *where the evidence came from*:

- **GO:0008017 microtubule binding** — evidence IBA, node **PTN000170013**, `withFrom` **FB:FBgn0003392** = *Drosophila* **shibire**, the classical endocytic dynamin. Microtubule binding is a hallmark of the *conventional* dynamin subfamily, not of the mitochondrial OPA1 clade.
- **GO:0016559 peroxisome fission** — evidence IBA, node **PTN008520527**, `withFrom` a set of *fission-branch* dynamins: human **DNM1L/DRP1** (O00429), mouse **Dnm1l** (MGI:1921256), and yeast **DNM1** and **VPS1** (SGD S000001709, S000003924). Peroxisomal fission is a documented DRP1 function, not an OPA1 function.

By contrast, the OPA1-clade node **PTN007514526** carries the biologically correct annotations for EAT-3: **GO:0008053 mitochondrial fusion** and **GO:0005758 intermembrane space**, sourced from bona fide OPA1 orthologs (human O60313; worm *eat-3* WBGene00001134) and independently reinforced by worm IMP evidence ([PMID: 18454199](https://pubmed.ncbi.nlm.nih.gov/18454199/), [PMID: 18722182](https://pubmed.ncbi.nlm.nih.gov/18722182/)).

Two literature anchors frame this cleanly. A model-organism synthesis of mitochondrial dynamics states that "*the functions of FZO/mitofusin and Mgm1/EAT-3/OPA1 in fusion and Dnm1/DRP1 in fission have been remarkably well conserved in yeasts, worms, flies and mammals*" ([PMID: 20006727](https://pubmed.ncbi.nlm.nih.gov/20006727/)) — establishing that fission (including peroxisomal fission) is the province of the Dnm1/DRP1 clade while EAT-3/OPA1 is a fusion protein. And OPA1 processing biology confirms EAT-3's compartment: "*Expression of Opa1 CTFs in the intermembrane space*" ([PMID: 25352671](https://pubmed.ncbi.nlm.nih.gov/25352671/)), consistent with an intramitochondrial IMS topology incompatible with cytosolic microtubule binding or peroxisomal fission.

### Finding 2 — EAT-3's core, directly supported function is mitochondrial inner-membrane fusion

EAT-3 is the *C. elegans* OPA1/Mgm1 homolog, a mitochondrial dynamin-family GTPase. The defining primary evidence: "*The C. elegans eat-3 gene encodes a mitochondrial dynamin family member homologous to Opa1 in humans and Mgm1 in yeast*" and the mutant phenotype is "*suggestive of a specific defect in fusion of the mitochondrial inner membrane*" ([PMID: 18454199](https://pubmed.ncbi.nlm.nih.gov/18454199/)). An independent study — "*the C. elegans Opa1 homologue EAT-3*" — showed CED-9 promotes FZO-1/Mfn1,2– and EAT-3/Opa1–dependent mitochondrial fusion ([PMID: 19704021](https://pubmed.ncbi.nlm.nih.gov/19704021/)).

UniProt Q18965 annotates GTP binding / GTPase activity (Dynamin-type G domain, residues ~284–560) and inner-membrane + intermembrane-space localization (IDA:WormBase, GO:0005739; IBA node PTN007514526). Critically, **worm IMP evidence exists for mitochondrial fusion but NOT for microtubule binding or peroxisome fission** — the asymmetry of experimental support across the three terms is itself decisive for curation.

### Finding 3 — EAT-3 lacks the PH/GED/PRD module that classical dynamin uses for microtubule and membrane engagement

An InterPro/UniProt domain comparison (computed this run) contrasts EAT-3 with the exact paralogs that seeded the contested terms:

| Protein (role) | Dynamin_N (GTPase) | Middle/stalk | **PH domain** | **GED** | Subfamily C-term | Engagement module |
|---|---|---|---|---|---|---|
| *Drosophila* **shibire** (P27619) — MT-binding IBA source | ✔ | ✔ (Dynamin_M) | **✔** | **✔** | — | Present (classical dynamin) |
| Human **DNM1L/DRP1** (O00429) — peroxisome-fission IBA source | ✔ | ✔ (Dynamin_M) | ✗ | **✔** | — | Fission dynamin |
| ***C. elegans* EAT-3** (Q18965) — target | **✔** | — (OPA1-type) | **✗** | **✗** | **OPA1_C** | **Absent** |

EAT-3 (964 aa) carries only **Dynamin_N (IPR045063 / PF00350)** + **OPA1_C (IPR045817 / PF19434)**, with **no PH domain, no GED, and no proline-rich features**. The PH domain and PRD are precisely the modules through which conventional dynamin contacts lipids and cytoskeletal/microtubule partners; their absence removes the structural basis for a direct microtubule interaction. DRP1's UniProt record independently annotates a mutation that "impairs mitochondrial division and induces changes in peroxisome morphology," confirming DRP1 — not EAT-3 — as the genuine peroxisome-fission actor.

### Finding 4 — PANTHER tree topology places both contested terms strictly upstream of EAT-3's subfamily node

Parsing the PANTHER PTHR11566 tree (v19, computed this run) resolves the exact-lineage question the seed hypothesis asks about:

```
PTHR11566 (dynamin superfamily)
│
├─ [depth 0] PTN000170013  ── GO:0008017 microtubule binding   ← FAMILY ROOT (shibire-seeded)
│    │
│    ├─ [depth 2] PTN008520527  ── GO:0016559 peroxisome fission  ← DRP1 branch
│    │      "DYNAMIN RELATED PROTEIN 1, ISOFORM A"                   (DNM1L/DNM1/VPS1-seeded)
│    │
│    └─ …
│          └─ [depth 5] PTN007514526  ── GO:0008053 mito fusion,   ← EAT-3's OPA1 node
│                 "DYNAMIN-LIKE 120 KDA PROTEIN, MITOCHONDRIAL"        GO:0005758 IMS
│                        │
│                        └─ EAT-3 (Q18965) / worm eat-3
```

- **PTN000170013 (microtubule binding)** is the **ROOT** of the whole family (depth 0).
- **PTN008520527 (peroxisome fission)** is an internal ancestral node at depth 2, reconstructed as "DYNAMIN RELATED PROTEIN 1, ISOFORM A" (the DRP1 branch).
- **PTN007514526 (EAT-3's OPA1 node)** is at depth 5 and is a strict **descendant** of both contested nodes — both appear in its ancestor chain, and the reverse is never true.

This confirms the terms were inherited by deep-node IBD/IBA propagation from ancestral/paralogous branches, not annotated at the OPA1 node where EAT-3 actually sits.

---

## Mechanistic Model / Interpretation

The three terms map onto three distinct branches of the dynamin superfamily, each with its own molecular job, compartment, and domain toolkit:

| Capacity (GO term) | Clade that owns it | Seed protein(s) | Compartment | Required module | Present in EAT-3? |
|---|---|---|---|---|---|
| Microtubule binding (GO:0008017) | Classical endocytic dynamin | *Drosophila* shibire | Cytosol / plasma membrane | PH + PRD + GED | **No** |
| Peroxisome fission (GO:0016559) | DRP1/Dnm1/Vps1 fission dynamins | DNM1L, DNM1, VPS1 | Cytosol → peroxisome/OMM surface | GED-driven self-assembly on cytosolic face | **No** |
| Mitochondrial inner-membrane fusion (GO:0008053) | OPA1/Mgm1 | OPA1, Mgm1, **EAT-3** | Mitochondrial inner membrane / IMS | Dynamin_N + OPA1_C, IMS-facing | **Yes — genuine** |

The narrative is coherent: EAT-3 is an OPA1-clade GTPase built for a job *inside* the mitochondrion. Its transit peptide targets it to mitochondria; it is anchored in the inner membrane with the bulk of the protein facing the intermembrane space, where it drives inner-membrane fusion (and, as in mammalian OPA1, cristae maintenance). Neither the microtubule-binding nor the peroxisome-fission activity is mechanistically reachable from this location and domain content: microtubule binding needs a cytosolic PH/PRD-bearing dynamin, and peroxisome fission needs a cytosolically recruited DRP1-type scission dynamin acting on the peroxisomal outer surface. EAT-3 has neither the address nor the hardware.

Importantly — and consistent with the seed hypothesis's cautions — this reasoning does not *prove* that EAT-3 can never, under any engineered or stress condition, contact a microtubule or a peroxisome. It establishes that (a) there is **no direct experimental evidence** in worm for either activity, (b) the annotations arose purely from **phylogenetic propagation off paralogs**, and (c) the **domain and topology make the direct activities mechanistically implausible**. That combination warrants "do not assert / over-annotation," not a fabricated positive refutation.

---

## Evidence Base

| # | Citation | Evidence type | Verdict | Claim tested | Key finding | Context | Confidence / limitation |
|---|---|---|---|---|---|---|---|
| 1 | [PMID: 18454199](https://pubmed.ncbi.nlm.nih.gov/18454199/) | Mutant phenotype / IMP | Supports (fusion); qualifies (contested) | EAT-3 core function | *eat-3* encodes OPA1/Mgm1 dynamin; loss → "specific defect in fusion of the mitochondrial inner membrane" | *C. elegans*, whole animal | High; primary in-organism evidence |
| 2 | [PMID: 19704021](https://pubmed.ncbi.nlm.nih.gov/19704021/) | Genetic interaction / IMP | Supports (fusion) | EAT-3 in fusion pathway | CED-9 promotes FZO-1– and EAT-3/Opa1–dependent mitochondrial fusion | *C. elegans* | High; independent confirmation |
| 3 | [PMID: 20006727](https://pubmed.ncbi.nlm.nih.gov/20006727/) | Review / synthesis | Qualifies (contested) | Clade division of labor | "Mgm1/EAT-3/OPA1 in fusion and Dnm1/DRP1 in fission … remarkably well conserved" | Yeast/worm/fly/mammal | High for clade assignment; review-level |
| 4 | [PMID: 25352671](https://pubmed.ncbi.nlm.nih.gov/25352671/) | Localization / processing | Refutes (contested) | EAT-3/OPA1 topology | OPA1 C-terminal fragments reside in the intermembrane space | Mouse liver / mammalian | High for topology; not worm |
| 5 | [PMID: 18722182](https://pubmed.ncbi.nlm.nih.gov/18722182/) | Mutant phenotype / IMP | Supports (fusion) | *eat-3* fusion function | Second worm IMP evidence line for GO:0008053 | *C. elegans* | Medium (cited via annotation) |
| 6 | QuickGO provenance (GO_REF:0000033) | Database / computational | Refutes (contested) | Source of contested terms | GO:0008017 seeded by shibire; GO:0016559 seeded by DNM1L/DNM1/VPS1 | PANTHER PTHR11566 | High; direct `withFrom` trace |
| 7 | PANTHER PTHR11566 tree (computed) | Structural / evolutionary | Refutes (contested) | Node lineage of terms vs EAT-3 | MT node = root; peroxisome node = DRP1 branch; both strict ancestors of EAT-3's OPA1 node | Superfamily phylogeny | High; reproducible tree parse |
| 8 | InterPro/UniProt domains (computed) | Structural / computational | Refutes (microtubule) | EAT-3 lacks engagement module | EAT-3 = Dynamin_N + OPA1_C only; no PH/GED/PRD | Sequence/domain | High; direct domain call |

**How the literature supports the findings.** [PMID: 18454199](https://pubmed.ncbi.nlm.nih.gov/18454199/) and [PMID: 19704021](https://pubmed.ncbi.nlm.nih.gov/19704021/) provide the two primary worm loss-of-function lines that anchor EAT-3's fusion function; these are the only direct experimental evidence lines among the three contested terms, and both point to inner-membrane fusion. [PMID: 20006727](https://pubmed.ncbi.nlm.nih.gov/20006727/) is used at review level to establish the deep, conserved division of labor between the fusion (Mgm1/EAT-3/OPA1) and fission (Dnm1/DRP1) clades — the conceptual basis for regarding a peroxisome-fission term on a fusion protein as paralog carry-over. [PMID: 25352671](https://pubmed.ncbi.nlm.nih.gov/25352671/) supplies the IMS-topology datum that makes cytosolic activities mechanistically implausible. The QuickGO provenance trace, PANTHER tree parse, and InterPro domain comparison are the computed provenance that convert "these look like paralog terms" into an explicit, reproducible lineage and architecture argument.

---

## GO Curation Implications (leads — require curator verification)

| GO term | Aspect | Current basis | Recommended action |
|---|---|---|---|
| GO:0008053 mitochondrial fusion | BP | IMP (worm) + IBA (OPA1 node) | **Retain** as the core BP function. Well supported. |
| GO:0005758 IMS / GO:0005743 inner membrane | CC | IBA / IEA / IDA | **Retain**; consistent with topology. |
| GO:0003924 GTPase / GO:0005525 GTP binding | MF | IEA:InterPro | **Retain**; foreground as the primary MF — a membrane-remodeling **GTPase**, more informative than "protein binding." |
| **GO:0008017 microtubule binding** | MF | IBA only (PTN000170013, from classical dynamin) | **Do not assert / treat as over-annotation.** Paralog-derived; topologically/architecturally implausible; no EAT-3 evidence. |
| **GO:0016559 peroxisome fission** | BP | IBA only (PTN008520527, from DRP1/Dnm1/Vps1) | **Do not assert / treat as over-annotation.** Fission-clade paralog-derived; EAT-3 is a fusion protein; worm peroxisome fission is DRP-1's role. |

Per guidance, "protein binding" is explicitly avoided as a fallback: the informative supported MF is the specific dynamin-family **GTPase activity driving inner-membrane fusion**, and the contested terms are recommended for non-assertion rather than replacement with a vaguer term.

---

## Mechanistic Scope

- **Direct molecular activity:** GTP-dependent, self-assembling dynamin-family GTPase that remodels/fuses the mitochondrial **inner** membrane (and shapes cristae), operating from the IMS side.
- **Downstream / pleiotropic (NOT the tested functions):** oxidative-phosphorylation competence, free-radical resistance, brood-size/growth, stress-response and lifespan phenotypes seen in *eat-3* mutants (PMIDs 18454199, 30840087, 32385951, 29748634) are consequences of failed inner-membrane fusion, not evidence of microtubule or peroxisomal activities.
- **Not supported as direct activities:** microtubule binding (a classical-dynamin/cytoskeletal function) and peroxisomal membrane scission (a DRP1/Dnm1/Vps1 function).

---

## Conflicts and Alternatives

- **Paralog confusion is the root cause.** PANTHER PTHR11566 lumps functionally divergent dynamins; deep-node IBD/IBA propagation carried classical-dynamin (microtubule) and fission-dynamin (peroxisome) capacities onto the OPA1 fusion clade. No conflicting primary evidence favors EAT-3 itself having these activities.
- **Alternative considered and rejected:** that EAT-3 retains an ancestral moonlighting microtubule interaction. No positive assay supports this; EAT-3 lacks the PRD/PH module and is topologically intramitochondrial.
- **Isoform biology:** OPA1 is processed into long/short forms with distinct roles (e.g., L-OPA1 regulating mitoflash biogenesis independently of fusion, [PMID: 28174208](https://pubmed.ncbi.nlm.nih.gov/28174208/)); these remain inner-membrane/IMS-localized and do not create a microtubule or peroxisomal function.
- **Organism-specificity:** even where experimental data exist (fly, mammals, yeast), microtubule binding and peroxisome fission map to shibire/DRP1/Dnm1/Vps1, not to OPA1/Mgm1. The seed's caveat is honored: absence of a worm test is not the basis for the call — paralog provenance and architecture are.

---

## Limitations and Knowledge Gaps

1. **Conditional microtubule interaction of processed EAT-3 fragments.** Checked: no assay found; provenance is paralog-based. Matters because the seed explicitly warns against over-claiming impossibility. Resolve with: microtubule co-sedimentation/TIRF binding of recombinant EAT-3 (full-length and IMS/short fragment); proximity labeling in worm.
2. **Worm peroxisome morphology in *eat-3* mutants.** Checked: not reported. Matters as a direct test. Resolve with: peroxisomal marker imaging (GFP-PTS1) in *eat-3* vs *drp-1* mutants.
3. **Isoform/processing map in worm.** Checked: mammalian OMA1/YME1L processing well documented; worm proteolytic isoforms less so. Matters because a hypothetical cytosol-exposed fragment is the only conceivable route to the contested functions. Resolve with: N-/C-terminomics and proteinase-protection of EAT-3 in *C. elegans*.
4. **Structure-based surface analysis** for a cryptic microtubule-binding patch was not formally run; the argument here is InterPro/domain-content based. Resolve with: AlphaFold surface comparison to a tubulin-binding dynamin.

---

## Proposed Follow-up Experiments / Actions

1. **Microtubule co-sedimentation / TIRF** of purified EAT-3 (and its IMS domain) ± taxol-stabilized microtubules — a positive would be required to rescue GO:0008017; expected negative.
2. **Peroxisome fission assay:** quantify peroxisome number/length in *eat-3(0)* vs *drp-1(0)* vs WT with GFP-PTS1; expected: *drp-1* perturbs peroxisomes, *eat-3* does not.
3. **Comparative phylogenetics / ancestral reconstruction** at PTHR11566 to formalize that PTN000170013 and PTN008520527 are ancestral to, and outside, the OPA1 subfamily node PTN007514526 (curation-grade provenance).
4. **Topology / proteinase-protection** to confirm no cytosol-exposed EAT-3 domain.
5. **Curation actions (leads):** (A) Flag GO:0008017 and GO:0016559 on Q18965 as paralog-driven IBA over-annotations — do not assert for this ortholog — citing QuickGO `withFrom` (shibire; DRP1/Dnm1/Vps1) plus IMS topology and absent PH/PRD. (B) Retain and foreground GO:0008053 with worm IMP evidence [PMID: 18454199](https://pubmed.ncbi.nlm.nih.gov/18454199/) and [PMID: 19704021](https://pubmed.ncbi.nlm.nih.gov/19704021/). (C) Prefer a specific MF (dynamin-family GTPase driving inner-membrane fusion) over "protein binding."

---

## Conclusion

Assessed independently as the seed hypothesis requires: **mitochondrial inner-membrane fusion is EAT-3's genuine, directly supported core function and should be retained; microtubule binding (GO:0008017) and peroxisome fission (GO:0016559) are paralog-driven deep-node over-annotations** — inherited by IBD/IBA from the family root (shibire) and the DRP1 branch (DNM1L/DNM1/VPS1), respectively, both strict ancestors of EAT-3's OPA1 subfamily node — and are mechanistically implausible given EAT-3's IMS-facing intramitochondrial topology and its lack of the PH/GED/PRD module. The recommended curation posture is non-assertion of the two contested terms (over-annotation), not a fabricated positive refutation, consistent with the absence of any direct worm assay either way.

---

*Provenance note:* Computational results above (UniProt/InterPro feature extraction, QuickGO `withFrom` provenance, and PANTHER PTHR11566 tree parsing) were executed live during this investigation; values are reproduced from the executed output, not hand-drawn.


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)