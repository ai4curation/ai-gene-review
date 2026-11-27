---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-21T02:34:56.644734'
end_time: '2026-09-21T02:50:08.772387'
duration_seconds: 912.13
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: POPTR
  gene: ndhD
  gene_symbol: ndhD
  uniprot_accession: A4GYW6
  taxon_id: NCBITaxon:3694
  taxon_label: Populus trichocarpa
  focus_type: function_assignment
  hypothesis_slug: chlororespiratory-capacity-and-subunit-quinone-binding
  hypothesis_text: Populus chloroplast NDH subunits ndhB1 (P0CD34), ndhB2 (P0CD35),
    ndhD (A4GYW6) and ndhK (A4GYR4) retain respiratory electron transport and aerobic
    respiration through chlororespiration. Separately, NdhD itself binds ubiquinone.
    Evaluate each hypothesis against term definitions and full primary studies. Current
    exact target leaves descend from PTN000511884 (both NdhB copies), PTN000511780
    (NdhD) and PTN000242188 (NdhK); donor count is irrelevant. Chloroplast localization
    does not itself exclude respiration. PMID27066014 compares tobacco ndhJK/ndhCJK
    mutants and PTOX inhibition under heat stress; PMID28559282 demonstrates NDH proton
    pumping and discusses ATP-generating chlororespiration. Establish which respiratory
    steps and energy conservation are demonstrated rather than proposed, and whether
    conservation supports the Populus inference. Modern NDH uses ferredoxin and lacks
    the NADH-oxidizing module; that electron-donor correction is distinct from respiratory
    process scope. For NdhD binding, PMID39856350 places the plastoquinone pocket
    in NdhA/H/K, with antiporter-like NdhD elsewhere in the membrane arm. Does any
    direct, structural or ancestral evidence establish NdhD quinone binding? Whole-complex
    substrate specificity alone does not establish physical binding by every subunit;
    do not automatically substitute generic quinone binding.
  term_context: No specific term context supplied.
  reference_context: No specific reference context supplied.
  source_file: genes/POPTR/ndhD/ndhD-ai-review.yaml
  source_selector: free-text
  source_context_yaml: "hypothesis: Populus chloroplast NDH subunits ndhB1 (P0CD34),\
    \ ndhB2 (P0CD35), ndhD (A4GYW6) and ndhK (A4GYR4)\n  retain respiratory electron\
    \ transport and aerobic respiration through chlororespiration. Separately,\n \
    \ NdhD itself binds ubiquinone. Evaluate each hypothesis against term definitions\
    \ and full primary studies.\n  Current exact target leaves descend from PTN000511884\
    \ (both NdhB copies), PTN000511780 (NdhD) and PTN000242188\n  (NdhK); donor count\
    \ is irrelevant. Chloroplast localization does not itself exclude respiration.\
    \ PMID27066014\n  compares tobacco ndhJK/ndhCJK mutants and PTOX inhibition under\
    \ heat stress; PMID28559282 demonstrates\n  NDH proton pumping and discusses ATP-generating\
    \ chlororespiration. Establish which respiratory steps\n  and energy conservation\
    \ are demonstrated rather than proposed, and whether conservation supports the\n\
    \  Populus inference. Modern NDH uses ferredoxin and lacks the NADH-oxidizing\
    \ module; that electron-donor\n  correction is distinct from respiratory process\
    \ scope. For NdhD binding, PMID39856350 places the plastoquinone\n  pocket in\
    \ NdhA/H/K, with antiporter-like NdhD elsewhere in the membrane arm. Does any\
    \ direct, structural\n  or ancestral evidence establish NdhD quinone binding?\
    \ Whole-complex substrate specificity alone does\n  not establish physical binding\
    \ by every subunit; do not automatically substitute generic quinone binding.\n\
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
citation_count: 10
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

- **Organism code:** POPTR
- **Taxon:** Populus trichocarpa (NCBITaxon:3694)
- **Gene directory:** ndhD
- **Gene symbol:** ndhD
- **UniProt accession:** A4GYW6

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** chlororespiratory-capacity-and-subunit-quinone-binding
- **Source file:** genes/POPTR/ndhD/ndhD-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

Populus chloroplast NDH subunits ndhB1 (P0CD34), ndhB2 (P0CD35), ndhD (A4GYW6) and ndhK (A4GYR4) retain respiratory electron transport and aerobic respiration through chlororespiration. Separately, NdhD itself binds ubiquinone. Evaluate each hypothesis against term definitions and full primary studies. Current exact target leaves descend from PTN000511884 (both NdhB copies), PTN000511780 (NdhD) and PTN000242188 (NdhK); donor count is irrelevant. Chloroplast localization does not itself exclude respiration. PMID27066014 compares tobacco ndhJK/ndhCJK mutants and PTOX inhibition under heat stress; PMID28559282 demonstrates NDH proton pumping and discusses ATP-generating chlororespiration. Establish which respiratory steps and energy conservation are demonstrated rather than proposed, and whether conservation supports the Populus inference. Modern NDH uses ferredoxin and lacks the NADH-oxidizing module; that electron-donor correction is distinct from respiratory process scope. For NdhD binding, PMID39856350 places the plastoquinone pocket in NdhA/H/K, with antiporter-like NdhD elsewhere in the membrane arm. Does any direct, structural or ancestral evidence establish NdhD quinone binding? Whole-complex substrate specificity alone does not establish physical binding by every subunit; do not automatically substitute generic quinone binding.

## Term and Decision Context

No specific term context supplied.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: Populus chloroplast NDH subunits ndhB1 (P0CD34), ndhB2 (P0CD35), ndhD (A4GYW6) and ndhK (A4GYR4)
  retain respiratory electron transport and aerobic respiration through chlororespiration. Separately,
  NdhD itself binds ubiquinone. Evaluate each hypothesis against term definitions and full primary studies.
  Current exact target leaves descend from PTN000511884 (both NdhB copies), PTN000511780 (NdhD) and PTN000242188
  (NdhK); donor count is irrelevant. Chloroplast localization does not itself exclude respiration. PMID27066014
  compares tobacco ndhJK/ndhCJK mutants and PTOX inhibition under heat stress; PMID28559282 demonstrates
  NDH proton pumping and discusses ATP-generating chlororespiration. Establish which respiratory steps
  and energy conservation are demonstrated rather than proposed, and whether conservation supports the
  Populus inference. Modern NDH uses ferredoxin and lacks the NADH-oxidizing module; that electron-donor
  correction is distinct from respiratory process scope. For NdhD binding, PMID39856350 places the plastoquinone
  pocket in NdhA/H/K, with antiporter-like NdhD elsewhere in the membrane arm. Does any direct, structural
  or ancestral evidence establish NdhD quinone binding? Whole-complex substrate specificity alone does
  not establish physical binding by every subunit; do not automatically substitute generic quinone binding.
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

# AIGR Gene Hypothesis Deep Research — Populus trichocarpa *ndhD* (A4GYW6)

**Focus type:** function_assignment
**Hypothesis slug:** chlororespiratory-capacity-and-subunit-quinone-binding
**Source file:** `genes/POPTR/ndhD/ndhD-ai-review.yaml`

---

## Executive Judgment

**Verdict: REFUTED (for the two GO assignments attached specifically to NdhD) / OVER-ANNOTATED.**

The seed hypothesis bundles two distinct claims onto the Populus chloroplast NDH subunit NdhD (A4GYW6): (1) that NdhD, together with ndhB1/ndhB2 and ndhK, retains "respiratory electron transport and aerobic respiration through chlororespiration," and (2) that NdhD itself binds ubiquinone. Both claims fail when evaluated at the subunit level against protein-family classification, structural evidence, and the official GO term definitions.

First, **NdhD is the NuoM/ND4 antiporter-like, proton-translocating membrane subunit** of the plastid NADH-dehydrogenase-like (NDH) complex. Its family assignment (HAMAP MF_00491 NDH1_NuoM; Pfam PF00361 Proton_antipo_M; InterPro IPR010227) places it in the membrane arm, well away from the quinone-reduction chamber. The recent structural literature cited by the seed itself (PMID:39856350) locates the plastoquinone pocket in the NdhA/NdhH/NdhK module, not in NdhD. The GO:0048039 "ubiquinone binding" annotation on NdhD is therefore refuted twice over: NdhD does not form the quinone pocket, and plants use **plastoquinone**, not ubiquinone.

Second, the process actually demonstrated for the chloroplast NDH complex is **ferredoxin-to-plastoquinone cyclic electron flow (CEF) with proton pumping**, and PTOX-terminated **chlororespiration** — not mitochondrial aerobic respiration. The complex uses ferredoxin (not NADH), reduces plastoquinone (not ubiquinone), and lacks the NADH-oxidizing N-module entirely. The GO:0009060 "aerobic respiration" (IBA) annotation does not fit the official definition ("enzymatic release of energy from inorganic and organic compounds … which requires oxygen as the terminal electron acceptor") and is an over-annotation. The only well-supported functional/process/location annotations for NdhD are **proton translocation**, **photosynthesis / light reaction (CEF)**, and **thylakoid membrane** localization. The most important caveat: this is a **function-assignment / annotation-scope** judgment, not a claim that Populus NDH is non-functional. NDH is a genuine, biologically important cyclic-electron-flow complex, and NdhD is a bona fide subunit of it; the refutation concerns which specific GO terms belong on the **NdhD subunit** versus which are whole-complex or wrong-organelle carry-overs propagated by phylogenetic (IBA) and electronic (IEA) inference.

---

## Key Findings

### Finding 1 — NdhD is a NuoM/ND4 antiporter-like membrane subunit and does not form the quinone-binding pocket

UniProt A4GYW6 classifies NdhD in the **"complex I subunit 4 family"** with concordant domain signatures: HAMAP MF_00491 (NDH1_NuoM), Pfam PF00361 (Proton_antipo_M), and InterPro IPR010227 (NADH_Q_OxRdtase_chainM/4). In the architecture of respiratory Complex I and its plastid NDH-1 homolog, the three antiporter-like subunits (ND2/NuoN = NdhB, ND4/NuoM = NdhD, ND5/NuoL = NdhF) form the distal membrane arm and translocate protons; they do **not** contact the quinone substrate.

The quinone/redox chemistry of Complex I / NDH-1 is instead carried out by a distinct set of subunits. As established in the comparative enzymology of [PMID: 11695831](https://pubmed.ncbi.nlm.nih.gov/11695831/), there are "significant and conserved sequence differences in the PSST/Nqo6/NuoB, 49kDa/Nqo4/NuoD, and ND1/Nqo8/NuoH subunit homologs" that define the cluster-N2/quinone redox core. In plastid NDH nomenclature these map to **NdhK (NuoB), NdhH (NuoD), and NdhA (NuoH)** — precisely the subunits that build the quinone chamber, and precisely *not* NdhD. The structure cited by the seed hypothesis (PMID:39856350) independently places the plastoquinone pocket in NdhA/H/K and puts antiporter-like NdhD elsewhere in the membrane arm.

Despite this, UniProt carries **GO:0048039 "ubiquinone binding" as an IBA (phylogenetic) annotation** on NdhD. This is an inference propagated across the Complex I family tree that does not respect subunit-level topology. Whole-complex substrate specificity does not license attributing physical quinone binding to every subunit — and NdhD is specifically the wrong subunit.

### Finding 2 — Plastid NDH is a ferredoxin:plastoquinone oxidoreductase / proton pump for cyclic electron flow and chlororespiration, not mitochondrial aerobic respiration

The demonstrated biochemistry of the chloroplast NDH complex is a proton-pumping oxidoreductase that moves electrons from ferredoxin to plastoquinone. [PMID: 28559282](https://pubmed.ncbi.nlm.nih.gov/28559282/) shows directly that the complex "pumps approximately two protons from the chloroplast stroma to the lumen per electron transferred from ferredoxin to plastoquinone," thereby increasing ATP production via cyclic electron flow around Photosystem I. This single sentence pins down both the **electron donor (ferredoxin, not NADH)** and the **electron acceptor (plastoquinone, not ubiquinone)**, and identifies the physiological output as CEF-driven proton-motive force.

The chlororespiratory role is supported genetically by [PMID: 27066014](https://pubmed.ncbi.nlm.nih.gov/27066014/), which reports that in tobacco "the chlororespiratory pathway was suppressed when NDH was inactivated" (ndhJK/ndhCJK mutants lose the chlororespiratory Fo rise and become more heat-sensitive). Critically, the O2-consuming terminal step of chlororespiration is catalyzed by a **separate enzyme, PTOX (plastid terminal oxidase)**, not by NDH itself. NDH's demonstrated contribution is the plastoquinone-reducing, proton-pumping arm of the chlororespiratory chain — not oxygen consumption.

Together these establish that the process NDH actually performs is **NDH-dependent CEF plus PTOX-terminated chlororespiration**, using ferredoxin and plastoquinone, with the NADH-oxidizing N-module absent from the plastid complex. UniProt A4GYW6 nonetheless carries **GO:0009060 aerobic respiration (IBA)** and **GO:0008137 NADH dehydrogenase (ubiquinone) activity (IEA)** — both framings imported from the mitochondrial/bacterial Complex I lineage that do not match the plastid enzyme.

### Finding 3 — Subunit-resolved UniProt comparison: only NdhD carries "ubiquinone binding"; NdhK is the genuine Q-chamber/redox subunit; NdhD lacks the photosynthesis BP its siblings have

A side-by-side comparison of the four subunits named in the seed sharpens the case. NdhD is an outlier for the two contested terms, and it is *missing* the term that its correctly-annotated siblings carry.

| Subunit | UniProt | Family / domains | Nature | Notable GO annotations |
|---|---|---|---|---|
| ndhB1 / ndhB2 | P0CD34 / P0CD35 | complex I subunit 2 family (HAMAP NDH1_NuoN, Pfam Proton_antipo_M) | Antiporter (ND2/NuoN) | GO:0022904 respiratory electron transport chain (IBA); **GO:0019684 photosynthesis, light reaction** (UniRule) |
| **ndhD** | **A4GYW6** | complex I subunit 4 family (HAMAP NDH1_NuoM, Pfam Proton_antipo_M) | Antiporter (ND4/NuoM) | **GO:0048039 ubiquinone binding (IBA)** ⚠; **GO:0009060 aerobic respiration (IBA)** ⚠; **NO GO:0019684** ⚠ |
| ndhK | A4GYR4 | complex I 20 kDa subunit family (HAMAP NDH1_NuoB, Pfam Oxidored_q6) | Redox subunit (NuoB) | GO:0051539 4Fe-4S cluster; GO:0005506 iron; **GO:0048038 quinone binding (IEA:InterPro)**; GO:0019684 photosynthesis, light reaction |

Three things stand out. (1) Among the four, **only NdhD carries "ubiquinone binding" (GO:0048039)** — the annotation is not shared by the other antiporter subunits, and it appears on the wrong subunit rather than on NdhK. (2) **NdhK is the genuine redox/quinone subunit**: it binds a 4Fe-4S cluster and iron and carries the more appropriate GO:0048038 "quinone binding." (3) NdhD, uniquely among these subunits, **lacks GO:0019684 "photosynthesis, light reaction,"** the plant-appropriate biological-process term that ndhB1/B2 and ndhK all carry. So NdhD simultaneously has two terms it should not (aerobic respiration, ubiquinone binding) and is missing the one it should (photosynthesis light reaction).

### Finding 4 — Official GO definitions confirm both contested terms are definitionally wrong for NdhD; photosynthesis light reaction is the correct BP

The QuickGO term definitions are decisive:

- **GO:0009060 aerobic respiration** = "enzymatic release of energy from inorganic and organic compounds … which requires oxygen as the terminal electron acceptor." Plastid NDH oxidizes ferredoxin and reduces plastoquinone; it does not catabolize carbohydrates or fats, and the O2-consuming step is handled by the separate PTOX enzyme. The definition does not fit — **remove or re-type.**
- **GO:0048039 ubiquinone binding** = "Binding to ubiquinone." Plants use **plastoquinone**, and NdhD is the NuoM antiporter subunit sitting outside the quinone pocket. The term fails on both counts — **remove.**
- **GO:0008137 NADH dehydrogenase (ubiquinone) activity** requires the NADH + ubiquinone reaction. Plastid NDH lacks the NADH-oxidizing N-module and uses a ferredoxin donor — the reaction it describes does not occur. **Remove or re-type** (IEA carry-over).
- **GO:0019684 photosynthesis, light reaction** explicitly covers thylakoid proton-motive-force generation and fits NDH's CEF role. **Add** (this is the BP NdhD is currently missing).
- **GO:0015990 electron transport coupled proton transport** (proton translocation) fits NdhD's actual antiporter mechanism. **Retain/add.**

---

## Mechanistic Model / Interpretation

The chloroplast NDH complex is best understood as a **ferredoxin:plastoquinone oxidoreductase and proton pump** that drives cyclic electron flow around Photosystem I. Its subunits divide cleanly by function, and NdhD sits in the proton-pumping membrane arm:

```
        STROMA (reduced Fd from PSI)
             |
       [ Ferredoxin ]  -- electrons -->  REDOX / QUINONE MODULE
                                          NdhA (NuoH) + NdhH (NuoD) + NdhK (NuoB)
                                          - 4Fe-4S clusters (NdhK)
                                          - plastoquinone-reduction pocket  <-- PQ
                                          '---------- conformational coupling ----------.
                                                                                         |
   MEMBRANE (ANTIPORTER) ARM  - proton translocation, NO quinone contact                 |
   +-------------+-------------+-------------+                                            |
   | NdhB (NuoN) |  NdhD (NuoM)|  NdhF (NuoL)|  <-- conformational wave pumps H+ ---------'
   +-------------+-------------+-------------+
             |                                       ~2 H+ / e- to lumen (PMID:28559282)
             v
        THYLAKOID LUMEN  -> proton-motive force -> extra ATP via ATP synthase (CEF)

   Chlororespiration terminal step:  PQH2 --> PTOX --> O2   (separate enzyme, NOT NdhD)
```

Under this model:

- **NdhD's molecular activity** is proton translocation (antiporter-like, ND4/NuoM). It is mechanically coupled to quinone chemistry happening ~tens of ångströms away in the NdhA/H/K module, but it neither binds nor reduces the quinone itself.
- **The correct substrate** is plastoquinone (PQ), reduced by ferredoxin-derived electrons — never ubiquinone, and never via NADH.
- **The correct biological process** is photosynthetic cyclic electron flow / light-reaction proton-motive-force generation, with a secondary role feeding chlororespiration (PQ pool reduction upstream of PTOX).
- **"Aerobic respiration"** is a category error: it imports the mitochondrial/bacterial Complex I framing onto a plastid enzyme that has lost the NADH module and whose only link to O2 is indirect (through the separate PTOX terminal oxidase).

The seed hypothesis's own logic supports this reading: it correctly notes that "modern NDH uses ferredoxin and lacks the NADH-oxidizing module," and that PMID:39856350 places the PQ pocket in NdhA/H/K. Following that logic to its conclusion refutes both the NdhD ubiquinone-binding claim and the aerobic-respiration process claim.

---

## Evidence Base / Evidence Matrix

| Citation | Evidence type | Direction | Claim tested | Key finding | Context | Confidence / limitations |
|---|---|---|---|---|---|---|
| [PMID: 11695831](https://pubmed.ncbi.nlm.nih.gov/11695831/) | Structural / evolutionary | **Refutes** NdhD Q-binding | Which subunits form the quinone/N2 redox core | "conserved sequence differences in the PSST/Nqo6/NuoB, 49kDa/Nqo4/NuoD, and ND1/Nqo8/NuoH subunit homologs" — redox core = NuoB/D/H = NdhK/H/A, not NuoM/NdhD | Comparative enzymology across Complex I / NDH-1 / hydrogenases | High for subunit topology; not Populus-specific |
| PMID:39856350 (cited in seed) | Structural (cryo-EM) | **Refutes** NdhD Q-binding | Location of plastoquinone pocket | PQ pocket in NdhA/H/K; antiporter-like NdhD elsewhere in membrane arm | Plant/algal NDH structure | High; not accessed programmatically here — relied on seed's characterization |
| [PMID: 28559282](https://pubmed.ncbi.nlm.nih.gov/28559282/) | Direct assay | **Refutes** aerobic respiration; supports CEF | Electron donor/acceptor & function of plastid NDH | "pumps approximately two protons … per electron transferred from ferredoxin to plastoquinone" → CEF, extra ATP | Higher-plant plastid NDH | High; whole-complex, not NdhD-resolved |
| [PMID: 27066014](https://pubmed.ncbi.nlm.nih.gov/27066014/) | Mutant phenotype | **Qualifies** chlororespiration; refutes NDH=O2 step | Is NDH required for chlororespiration; what consumes O2 | "chlororespiratory pathway was suppressed when NDH was inactivated"; PTOX mediates O2-consuming step | Tobacco ndhJK/ndhCJK mutants, heat stress | High; O2 step is PTOX not NDH |
| UniProt A4GYW6 + HAMAP/Pfam/InterPro | Computational / database | **Refutes** NdhD Q-binding | NdhD family classification | complex I subunit 4 family; NDH1_NuoM; Proton_antipo_M; IPR010227 → antiporter subunit | Sequence/domain | High for classification; annotations include IBA/IEA carry-overs |
| UniProt A4GYR4 (NdhK) | Computational / database | **Competing** (correct subunit) | Which subunit is the Q/redox subunit | NuoB family; 4Fe-4S (GO:0051539), iron (GO:0005506), quinone binding (GO:0048038) | Sequence/domain | High; supports moving Q terms to NdhK, not NdhD |
| QuickGO GO:0009060 / GO:0048039 / GO:0008137 / GO:0019684 | Review / database (definitions) | **Refutes** two terms; supports BP | Do term definitions fit NdhD | Aerobic respiration requires O2 terminal acceptor + catabolism (no fit); ubiquinone binding needs ubiquinone (plants use PQ); photosynthesis light reaction fits | GO ontology | High; definitional, not experimental |

Additional supporting literature confirms the NDH→CEF framing across systems: [PMID: 31245694](https://pubmed.ncbi.nlm.nih.gov/31245694/) (NDH "participates in one CEF route transferring electrons from ferredoxin back to the plastoquinone pool with concomitant proton pumping to the lumen"), and multiple C4-photosynthesis studies ([PMID: 27017612](https://pubmed.ncbi.nlm.nih.gov/27017612/), [PMID: 27497446](https://pubmed.ncbi.nlm.nih.gov/27497446/), [PMID: 36703198](https://pubmed.ncbi.nlm.nih.gov/36703198/), [PMID: 39036838](https://pubmed.ncbi.nlm.nih.gov/39036838/), [PMID: 41838822](https://pubmed.ncbi.nlm.nih.gov/41838822/)) that repeatedly frame NDH as the ATP-generating cyclic-electron-flow complex, never as a mitochondrial-style respiratory enzyme.

---

## GO Curation Implications

**Lead (requires curator verification).** The evidence supports **removing or re-typing** the two contested NdhD annotations and **adding** the missing plant-appropriate process term.

| GO term | Aspect | Current on A4GYW6 | Recommended action | Rationale |
|---|---|---|---|---|
| GO:0048039 ubiquinone binding | MF | IBA | **Remove** | Wrong subunit (NdhD = NuoM antiporter, not Q-pocket) and wrong quinone (plants use plastoquinone). Q-binding belongs on NdhK (GO:0048038, already present). |
| GO:0009060 aerobic respiration | BP | IBA | **Remove / re-type** | Definitional mismatch; NDH does CEF/chlororespiration (ferredoxin→PQ), O2 step is PTOX. Consider a cyclic-electron-flow / photosynthetic electron-transport term instead. |
| GO:0008137 NADH dehydrogenase (ubiquinone) activity | MF | IEA | **Remove / re-type** | Plastid NDH lacks the NADH N-module and uses ferredoxin; reaction described does not occur. |
| GO:0019684 photosynthesis, light reaction | BP | **absent** | **Add** | Present on ndhB1/B2 and ndhK; matches NDH's CEF role; NdhD is anomalously missing it. |
| GO:0015990 electron transport coupled proton transport | BP | (verify) | **Retain / add** | Matches NdhD's actual antiporter proton-translocation mechanism. |
| GO:0009535 chloroplast thylakoid membrane | CC | (verify) | **Retain** | Correct localization; chloroplast localization does not exclude the (photosynthetic) function. |

Do **not** substitute a generic "protein binding" or generic "quinone binding" term on NdhD — the specific evidence points to proton translocation and CEF, and the quinone chemistry maps to a different subunit.

---

## Mechanistic Scope

The immediate molecular function under test for NdhD is **membrane proton translocation** as the ND4/NuoM antiporter-like subunit of NDH. This is distinct from, and mechanically upstream-coupled to, the quinone-reduction chemistry performed by NdhA/H/K.

- **Direct gene-product activity (NdhD):** conformationally-driven proton translocation across the thylakoid membrane; structural participation in the NDH membrane arm.
- **Whole-complex activity (not NdhD alone):** ferredoxin:plastoquinone oxidoreductase, ~2 H+/e⁻ pumping (PMID:28559282).
- **Downstream/pathway consequences (not to be attributed to NdhD as MF):** cyclic electron flow, proton-motive force, extra ATP, chlororespiration (with PTOX), photoprotection, heat-stress tolerance (PMID:27066014).

The seed's two claims conflate these levels. "Ubiquinone binding" attributes a whole-complex substrate interaction to the wrong subunit; "aerobic respiration" attributes a downstream/mislabeled process to NdhD. Neither survives the direct-vs-downstream separation.

---

## Conflicts and Alternatives

1. **Paralog/homolog carry-over from mitochondrial Complex I.** The strongest driver of the erroneous annotations is phylogenetic inference across the Complex I superfamily. Mitochondrial/bacterial ND4 relatives sit in NADH:ubiquinone oxidoreductase, so IBA propagates ubiquinone binding and aerobic respiration onto the plastid ND4 homolog (NdhD) despite the plastid enzyme's ferredoxin donor and plastoquinone acceptor. This is database carry-over, not organism-specific evidence.

2. **Whole-complex vs subunit attribution.** Even where quinone binding is real for the complex, it is not real for NdhD. NdhK is the correct locus (already annotated GO:0048038). This is the central "do not substitute generic quinone binding" caveat raised by the seed, and the evidence honors it.

3. **Chlororespiration is real but does not rescue "aerobic respiration."** NDH genuinely feeds chlororespiration by reducing the PQ pool, but the O2-consuming terminal step is PTOX (PMID:27066014). Attributing "aerobic respiration" to NdhD conflates NDH's upstream role with PTOX's terminal oxidase activity.

4. **Ubiquinone vs plastoquinone.** Even setting subunit topology aside, the "ubiquinone" term is chemically wrong for a plant plastid enzyme — the physiological quinone is plastoquinone.

No accessed evidence competes *in favor* of the seed's two NdhD-specific claims; the seed's own cited structure (PMID:39856350) argues against NdhD quinone binding.

---

## Limitations and Knowledge Gaps

- **PMID:39856350 not independently retrieved here.** The report relies on the seed's characterization that this structure places the PQ pocket in NdhA/H/K with NdhD in the membrane arm. This is fully consistent with the family classification and PMID:11695831, but a curator should confirm the structure's figures directly. *Gap matters because it is the most direct structural evidence for NdhD's non-Q-binding role.*
- **Populus-specific experimental data absent.** All functional evidence is from tobacco/higher-plant/comparative systems. The Populus inference rests on strong orthology (NdhD is highly conserved; the seed's ancestral node PTN000511780 places A4GYW6 firmly in the NdhD/NuoM lineage), but no Populus-specific NDH assay was located. *Matters only mildly — subunit identity and mechanism are deeply conserved.*
- **IBA/IEA provenance not manually traced to the PAINT family tree.** The conclusion that GO:0048039 and GO:0009060 are carry-overs is inferred from their IBA evidence code plus definitional mismatch, not from inspecting the reference family annotations. *A curator verifying the PAINT node would close this.*
- **No wet-lab test of NdhD proton translocation in isolation** exists; proton pumping is a whole-complex measurement. This does not affect the removal recommendation but limits how specifically the proton-transport MF/BP can be asserted for NdhD alone.

---

## Proposed Follow-up Experiments / Actions (Discriminating Tests)

1. **Inspect the PMID:39856350 structure directly** (or any high-resolution plant NDH cryo-EM model, e.g., PDB entries for chloroplast NDH) and measure the distance from NdhD to the modeled plastoquinone pocket. A distance well outside van der Waals contact confirms NdhD does not bind quinone. *Most efficient single check.*
2. **Trace the PAINT/IBA reference family** for GO:0048039 and GO:0009060 to confirm they were propagated from mitochondrial Complex I nodes and are not subunit-specific experimental annotations.
3. **Cross-organism annotation audit:** compare NdhD orthologs (Arabidopsis, tobacco, Populus) for whether "ubiquinone binding" and "aerobic respiration" appear consistently or sporadically — sporadic appearance signals carry-over noise.
4. **Confirm NdhK retains the quinone-binding annotation** and, if appropriate, ensure the whole-complex quinone specificity is captured at the complex level (NDH complex) rather than smeared onto antiporter subunits.

---

## Curation Leads (require curator verification)

**Candidate action changes for A4GYW6 (NdhD):**
- **Remove** GO:0048039 "ubiquinone binding" (IBA) — refuted by subunit topology and plastoquinone usage.
- **Remove or re-type** GO:0009060 "aerobic respiration" (IBA) — definitional mismatch; consider a photosynthetic cyclic-electron-flow / electron-transport term.
- **Remove or re-type** GO:0008137 "NADH dehydrogenase (ubiquinone) activity" (IEA) — no NADH module in plastid NDH.
- **Add** GO:0019684 "photosynthesis, light reaction" — anomalously missing versus ndhB1/B2/ndhK.
- **Retain/add** GO:0015990 proton transport and GO:0009535 chloroplast thylakoid membrane.

**Candidate references with snippets to verify:**
- [PMID: 28559282](https://pubmed.ncbi.nlm.nih.gov/28559282/) — "pumps approximately two protons from the chloroplast stroma to the lumen per electron transferred from ferredoxin to plastoquinone." (Justifies CEF/proton-transport, refutes NADH/ubiquinone framing.)
- [PMID: 27066014](https://pubmed.ncbi.nlm.nih.gov/27066014/) — "the chlororespiratory pathway was suppressed when NDH was inactivated." (Places NDH in chlororespiration with PTOX as the O2 step.)
- [PMID: 11695831](https://pubmed.ncbi.nlm.nih.gov/11695831/) — "conserved sequence differences in the PSST/Nqo6/NuoB, 49kDa/Nqo4/NuoD, and ND1/Nqo8/NuoH subunit homologs." (Shows the redox/Q core = NdhK/H/A, not NdhD.)
- PMID:39856350 (seed-cited) — verify PQ pocket in NdhA/H/K, NdhD in membrane arm.

**Suggested curator questions:**
- Are GO:0048039 and GO:0009060 on A4GYW6 traceable to a PAINT node propagated from mitochondrial Complex I? If so, they are family-level carry-overs, not subunit evidence.
- Should whole-complex quinone specificity be represented at the NDH complex level rather than on the NdhD subunit?

**Suggested experiments:** structural distance measurement (NdhD ↔ PQ pocket); comparative annotation audit across NdhD orthologs.

---

## Summary Statement

For Populus *ndhD* (A4GYW6), both seed sub-claims fail at the subunit level. NdhD is the NuoM/ND4 antiporter-like proton-translocating subunit (HAMAP NDH1_NuoM, Pfam Proton_antipo_M); the quinone pocket of NDH-1 is formed by NdhA/H/K (PMID:11695831; PMID:39856350), so **GO:0048039 "ubiquinone binding" (IBA) is refuted and should be removed** (plants also use plastoquinone, not ubiquinone). The demonstrated process of the chloroplast NDH complex is ferredoxin-to-plastoquinone cyclic electron flow and PTOX-terminated chlororespiration (PMID:28559282; PMID:27066014), not mitochondrial aerobic respiration, so **GO:0009060 "aerobic respiration" (IBA) is an over-annotation** that should be removed or re-typed to a plastid cyclic-electron-flow term. Only proton-translocation, photosynthesis light-reaction, and thylakoid-membrane annotations are well supported for NdhD.


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)