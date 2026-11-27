---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-20T23:24:56.486326'
end_time: '2026-09-20T23:49:39.007631'
duration_seconds: 1482.52
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: human
  gene: PIK3R4
  gene_symbol: PIK3R4
  uniprot_accession: Q99570
  taxon_id: NCBITaxon:9606
  taxon_label: Homo sapiens
  focus_type: function_assignment
  hypothesis_slug: protein-phosphorylation-complex-contribution
  hypothesis_text: 'Human PIK3R4/VPS15 Q99570 directly contributes to protein phosphorylation,
    potentially as a noncatalytic cofactor or scaffold rather than the phosphotransferase.
    Read full primary8999962 (JBC272:2477, doi10.1074/jbc.272.4.2477), especially
    TableI: an Sf9-produced affinity-purified GST-p150/VPS34 complex phosphorylated
    peptide/protein substrates with a manganese preference; individual autophosphorylation
    was not observed. Fig4 in-vivo labeling of p150 is only a substrate observation,
    a distinct assay. Compare the preparations, substrates, controls and attribution
    with primary39913640 modern human VPS15 GTP-binding pseudokinase structures, nucleotide
    HPLC/MS and phosphotransferase geometry, plus40442316 and relevant subsequent
    direct biochemistry. Determine whether complex activity establishes actual VPS15
    contribution, a distinct VPS34 protein-substrate reaction, unresolved associated
    activity, or evidence of contamination; do not infer contamination merely from
    an unexpected result or assign every complex activity to every subunit. Distinguish
    broad BP participation from direct MF protein kinase activity and from indirect
    regulation or VPS15 being phosphorylated by another kinase. Original GO0006468
    is NAS8999962, not IBA; the separate kinase IBA at actual family-root PTN000426471
    (PTHR17583, targetleafPTN002497817) should provide evolutionary context without
    equating loss of catalysis with loss of all noncatalytic participation. The already
    completed focused NVJ report did not investigate this chemistry; do not repeat
    NVJ research.'
  term_context: No specific term context supplied.
  reference_context: No specific reference context supplied.
  source_file: genes/human/PIK3R4/PIK3R4-ai-review.yaml
  source_selector: free-text
  source_context_yaml: "hypothesis: 'Human PIK3R4/VPS15 Q99570 directly contributes\
    \ to protein phosphorylation, potentially as\n  a noncatalytic cofactor or scaffold\
    \ rather than the phosphotransferase. Read full primary8999962 (JBC272:2477,\n\
    \  doi10.1074/jbc.272.4.2477), especially TableI: an Sf9-produced affinity-purified\
    \ GST-p150/VPS34 complex\n  phosphorylated peptide/protein substrates with a manganese\
    \ preference; individual autophosphorylation\n  was not observed. Fig4 in-vivo\
    \ labeling of p150 is only a substrate observation, a distinct assay. Compare\n\
    \  the preparations, substrates, controls and attribution with primary39913640\
    \ modern human VPS15 GTP-binding\n  pseudokinase structures, nucleotide HPLC/MS\
    \ and phosphotransferase geometry, plus40442316 and relevant\n  subsequent direct\
    \ biochemistry. Determine whether complex activity establishes actual VPS15 contribution,\n\
    \  a distinct VPS34 protein-substrate reaction, unresolved associated activity,\
    \ or evidence of contamination;\n  do not infer contamination merely from an unexpected\
    \ result or assign every complex activity to every\n  subunit. Distinguish broad\
    \ BP participation from direct MF protein kinase activity and from indirect\n\
    \  regulation or VPS15 being phosphorylated by another kinase. Original GO0006468\
    \ is NAS8999962, not IBA;\n  the separate kinase IBA at actual family-root PTN000426471\
    \ (PTHR17583, targetleafPTN002497817) should\n  provide evolutionary context without\
    \ equating loss of catalysis with loss of all noncatalytic participation.\n  The\
    \ already completed focused NVJ report did not investigate this chemistry; do\
    \ not repeat NVJ research.'\nfocus_type: function_assignment\ncontext: []\nreference_id:\
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

- **Organism code:** human
- **Taxon:** Homo sapiens (NCBITaxon:9606)
- **Gene directory:** PIK3R4
- **Gene symbol:** PIK3R4
- **UniProt accession:** Q99570

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** protein-phosphorylation-complex-contribution
- **Source file:** genes/human/PIK3R4/PIK3R4-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

Human PIK3R4/VPS15 Q99570 directly contributes to protein phosphorylation, potentially as a noncatalytic cofactor or scaffold rather than the phosphotransferase. Read full primary8999962 (JBC272:2477, doi10.1074/jbc.272.4.2477), especially TableI: an Sf9-produced affinity-purified GST-p150/VPS34 complex phosphorylated peptide/protein substrates with a manganese preference; individual autophosphorylation was not observed. Fig4 in-vivo labeling of p150 is only a substrate observation, a distinct assay. Compare the preparations, substrates, controls and attribution with primary39913640 modern human VPS15 GTP-binding pseudokinase structures, nucleotide HPLC/MS and phosphotransferase geometry, plus40442316 and relevant subsequent direct biochemistry. Determine whether complex activity establishes actual VPS15 contribution, a distinct VPS34 protein-substrate reaction, unresolved associated activity, or evidence of contamination; do not infer contamination merely from an unexpected result or assign every complex activity to every subunit. Distinguish broad BP participation from direct MF protein kinase activity and from indirect regulation or VPS15 being phosphorylated by another kinase. Original GO0006468 is NAS8999962, not IBA; the separate kinase IBA at actual family-root PTN000426471 (PTHR17583, targetleafPTN002497817) should provide evolutionary context without equating loss of catalysis with loss of all noncatalytic participation. The already completed focused NVJ report did not investigate this chemistry; do not repeat NVJ research.

## Term and Decision Context

No specific term context supplied.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: 'Human PIK3R4/VPS15 Q99570 directly contributes to protein phosphorylation, potentially as
  a noncatalytic cofactor or scaffold rather than the phosphotransferase. Read full primary8999962 (JBC272:2477,
  doi10.1074/jbc.272.4.2477), especially TableI: an Sf9-produced affinity-purified GST-p150/VPS34 complex
  phosphorylated peptide/protein substrates with a manganese preference; individual autophosphorylation
  was not observed. Fig4 in-vivo labeling of p150 is only a substrate observation, a distinct assay. Compare
  the preparations, substrates, controls and attribution with primary39913640 modern human VPS15 GTP-binding
  pseudokinase structures, nucleotide HPLC/MS and phosphotransferase geometry, plus40442316 and relevant
  subsequent direct biochemistry. Determine whether complex activity establishes actual VPS15 contribution,
  a distinct VPS34 protein-substrate reaction, unresolved associated activity, or evidence of contamination;
  do not infer contamination merely from an unexpected result or assign every complex activity to every
  subunit. Distinguish broad BP participation from direct MF protein kinase activity and from indirect
  regulation or VPS15 being phosphorylated by another kinase. Original GO0006468 is NAS8999962, not IBA;
  the separate kinase IBA at actual family-root PTN000426471 (PTHR17583, targetleafPTN002497817) should
  provide evolutionary context without equating loss of catalysis with loss of all noncatalytic participation.
  The already completed focused NVJ report did not investigate this chemistry; do not repeat NVJ research.'
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

# Focused Curation Report — PIK3R4 / VPS15 (Q99570)

**Hypothesis (function_assignment / slug `protein-phosphorylation-complex-contribution`):**
Human PIK3R4/VPS15 directly contributes to protein phosphorylation (GO:0006468),
potentially as a noncatalytic cofactor/scaffold rather than the phosphotransferase.

**Source annotation under review:** GO:0006468 "protein phosphorylation" (BP),
evidence code **NAS**, reference **PMID:8999962**.

---

## Executive Judgment

**Verdict: Weakly supported / over-annotated as written — recommend the GO:0006468
(NAS) annotation be treated as non-core and removed (or, at most, generalized), pending curator verification.**

The hypothesis correctly separates two claims that the original annotation conflates:

1. **A direct VPS15 protein-kinase molecular function (GO:0004672) — REFUTED.**
   Modern cryo-EM of the human class III PI3K complex explicitly designates VPS15 a
   **pseudokinase** (PMID:39913640, 2025); the seed further notes nucleotide HPLC/MS
   showing **GTP (not ATP) binding** and **degenerate phosphotransferase geometry**.
   UniProt Q99570 keeps a legacy "Protein kinase" domain (aa 26–324), an active-site
   "proton acceptor" (D148) and ATP-binding sites **annotated by similarity**, plus the
   keywords "Serine/threonine-protein kinase" and "Transferase" — **yet lists no
   catalytic-activity reaction**, and describes the protein's FUNCTION solely as a
   "Regulatory subunit." The catalytic residues are present as a fold relic, not a
   working active site.

2. **A broad BP "contribution to protein phosphorylation" via the complex — UNRESOLVED,
   and not established for VPS15 specifically by the cited evidence.**
   The protein-substrate phosphorylation in PMID:8999962 (Table I) is a property of the
   **co-purified GST‑p150·VPS34 complex**, with Mn²⁺ preference and **no individual
   autophosphorylation**. Attribution to VPS15 is not made by the authors; the more
   parsimonious catalyst is VPS34 (or an associated kinase). In the same paper, p150/VPS15
   appears as a **substrate** (Fig 4, in‑vivo labeling) — the opposite of being the kinase.
   The annotation is **NAS**, i.e. author assertion, not a traceable experimental
   attribution to VPS15. Subsequent direct biochemistry firms this direction: VPS15 is a
   **ULK substrate** (PMID:34121209, six ULK-dependent sites, major Ser861) whose
   phosphorylation regulates VPS34 activity, and a **GTP-binding** conformational regulator of
   VPS34 (PMID:40537377) — i.e. a phospho-target/regulator, not a protein phosphotransferase.

**Most important caveat (from the seed, and respected here):** a pseudokinase can still
participate noncatalytically. Loss of catalysis ≠ loss of all participation. So the
correct curation posture is not "VPS15 has nothing to do with phosphorylation," but
"the *specific* evidence does not establish a direct VPS15 phosphotransferase function,
and a bare BP 'protein phosphorylation' term mis-states VPS15's actual regulatory/scaffold role."

---

## Evidence Matrix

| Citation | Evidence type | Supports/Refutes/Qualifies | Claim tested | Key finding | Context | Confidence & limitations |
|---|---|---|---|---|---|---|
| PMID:8999962 (Panaretou 1997, JBC 272:2477) | Direct assay (in vitro), original NAS source | Qualifies / competing | Does p150/VPS15 directly phosphorylate protein substrates? | Affinity-purified **complex** phosphorylates peptide/protein substrates (Mn²⁺-preferring, Table I); **no** individual autophosphorylation; p150 is a **substrate** in vivo (Fig 4). Recombinant p150 stimulates VPS34 **lipid** kinase 2-fold. | Sf9-expressed GST-p150·human VPS34 complex | Med. Activity is complex-level; catalyst not resolved; abstract emphasizes adaptor/lipid-kinase-regulator role. |
| PMID:39913640 (Cook 2025) | Structural (cryo-EM) + biochemistry | Refutes (direct MF) | Is VPS15 a catalytic protein kinase? | VPS15 is a **pseudokinase**; its inactive conformation gates VPS34; GTP (not ATP) binding, degenerate active-site geometry (per seed). | Human PI3KC3-C1 | High for pseudokinase status. |
| PMID:40537377 (Duttenhefner 2025) | Structural/biochem synthesis | Refutes (direct MF) | Does VPS15 bind GTP and act catalytically? | "the VPS15 pseudokinase domain binds GTP and sequesters its covalently-linked N-terminal myristate"; stabilizes **inactive** VPS34 | Human PI3KC3-C1 | High; independent synthesis of Cook et al. |
| PMID:34121209 (Mercer 2021) | Direct assay (phosphoproteomics + mutants) | Competing / qualifies | Is VPS15 a kinase or a substrate? | VPS15 is a **ULK substrate**: "six ULK-dependent phosphorylation sites on VPS15, mutation of which reduces… VPS34 activity in vitro" (major Ser861) | Mouse embryonic fibroblasts; in vitro | High; VPS15 is the phospho-target, its phosphorylation regulates VPS34. |
| PMID:37414850 (Alkhoury 2023) | Mutant/localization | Qualifies (noncatalytic moonlighting) | Does VPS15 have non-complex roles? | Nuclear Vps15 coactivates Bmal1-Clock **independently of Vps34**; promotes Ppat transcription | Mouse liver/cells | Med; supports real noncatalytic participation. |
| PMID:40442316 (Chen 2025) | Structural (cryo-EM) | Supports (scaffold role) | What is VPS15's molecular role? | VPS15 is a **scaffold/interaction hub**, contacting FIP200 (ULK1C) and co-assembling the supercomplex; drives ULK1 dimerization. | Human ULK1C:PI3KC3-C1 supercomplex | High; no phosphotransferase role attributed to VPS15. |
| Catalytic-motif audit (this run, Q99570 vs PKA P17612) | Computational (sequence) | Refutes (direct MF) | Are canonical STK catalytic motifs intact? | Degenerate Gly-rich P-loop; DFG→DFA; only β3-Lys(K53) and catalytic-Asp(D148) retained | Human sequence audit | Med; corroborative, secondary to cryo-EM. |
| UniProt Q99570 (database) | Database record | Qualifies | Is a catalytic kinase function annotated? | Kinase domain + active site + ATP-binding **by similarity**; **no catalytic reaction**; FUNCTION = "Regulatory subunit." | Curated human record | Orientation-level; legacy homology annotation. |
| PANTHER PTHR17583 / root PTN000426471 (evolutionary) | Computational/evolutionary | Qualifies / competing | Should protein kinase activity propagate by ancestry? | Family-root kinase IBA gives evolutionary context but should not be equated with retained catalysis in the VPS15 leaf. | Ortholog family | Med; IBA MF propagation is an over-annotation risk for the human leaf. |

---

## Computed Provenance — VPS15 Kinase-Domain Catalytic-Motif Audit

I retrieved UniProt Q99570 (this run) and audited the kinase domain (aa 26–324) for the
canonical Ser/Thr-kinase catalytic elements, benchmarked against canonical PKA (P17612).
Executed code + output; table saved as `vps15_catalytic_motif_audit.csv`.

| Motif | VPS15 pos | Canonical requirement | VPS15 observed | Verdict |
|---|---|---|---|---|
| Glycine-rich P-loop (GxGxxG) | ~aa30–40 | GxGxxG positions ATP phosphates | `LGSTRFFKV` (no GxGxxG) | **DEGENERATE** |
| β3 lysine (VAIK) | K53 | Lys pairs α/β phosphates | `VVVK` (K53 present) | Retained |
| Catalytic loop (HRD; Asp = proton acceptor) | D148 | HRD | `HGD` (H146,G147,D148) | Asp retained; **HRD Arg→Gly** |
| Mg-binding DFG | ~D164 | DFG | `DFA` (Gly→Ala) | **ALTERED** |

**Benchmark:** canonical PKA has an intact P-loop (`GTGSFG`@51) and `DFG`@185.
**Interpretation (conservative):** two core nucleotide-positioning/catalytic elements
(Gly-rich loop; DFG glycine) are degenerate in VPS15, consistent with impaired canonical
ATP-dependent phosphotransfer and the pseudokinase designation. The **retained** K53 and
D148 are the relics that drive UniProt's "by similarity" ATP-binding/active-site and the
PANTHER family-root kinase IBA — i.e. the legacy kinase labels are homology carry-over, not
demonstrated catalysis. This sequence audit is corroborative and secondary to the direct
cryo-EM structural evidence (PMID:39913640).

---

## GO Decision Table (leads — require curator verification)

| GO term | Aspect | Current | Evidence verdict | Recommended action |
|---|---|---|---|---|
| GO:0006468 protein phosphorylation | BP | Present (NAS, PMID:8999962) | Complex-level activity; VPS15 is substrate not catalyst; VPS15 = pseudokinase | **Remove / treat as non-core** (or at most generalize) |
| GO:0004672 / GO:0004674 protein (S/T) kinase activity | MF | Risk via IBA/ISS (PTHR17583 root) | Refuted: degenerate P-loop, DFG→DFA, GTP-binding pseudokinase | **Do not assign / remove** (evolutionary context only) |
| GO:0034271/0034272 PI3K complex, class III (type I/II) | CC | — | Strongly supported (structures) | **Add/retain** |
| GO:0000045 autophagosome assembly | BP | — | Supported (function, structures) | **Retain/add** |
| GO:0016192 vesicle-mediated transport | BP | — | Supported (UniProt function) | **Retain/add** |
| Enzyme-activator / kinase-regulator of VPS34 lipid kinase | MF | — | Supported (PMID:8999962 2-fold; PMID:34121209) | **Consider** (more informative than "protein binding") |
| GTP binding (GO:0005525) | MF | — | Supported by PMID:39913640 / PMID:40537377 | **Consider** (curator discretion) |

## GO Curation Implications (leads — require curator verification)

- **GO:0006468 "protein phosphorylation" (BP), NAS, PMID:8999962 — lead: REMOVE or down-rank to non-core.**
  The cited evidence demonstrates a *complex* activity, not a VPS15 molecular function, and
  modern structure shows VPS15 is a pseudokinase. A bare BP "protein phosphorylation" on a
  scaffold subunit mis-attributes a co-subunit's chemistry.
- **GO:0004672 / GO:0004674 "(serine/threonine) protein kinase activity" (MF) — if present via IBA/ISS, lead: REMOVE.**
  Refuted by pseudokinase evidence; keep only as evolutionary/fold context, not as active MF.
- **Do NOT downgrade to a bare "protein binding" term.** More informative supported terms exist:
  - **CC:** GO:0034271/GO:0034272 (phosphatidylinositol 3-kinase complex, class III, type I/II) — supported.
  - **BP:** GO:0000045 (autophagosome assembly), GO:0016192 (vesicle-mediated transport) — supported by function/structure.
  - **MF:** consider **enzyme regulator / kinase activator** style term for its stimulation of VPS34 lipid kinase (PMID:8999962), and note GTP-binding (from PMID:39913640) if curators accept it.

---

## Mechanistic Scope

Immediate molecular function tested: **phosphotransfer onto protein substrates by VPS15 itself.**
- **Direct VPS15 activity:** not demonstrated; fold present, catalysis absent (pseudokinase).
- **Complex activity (VPS34-containing):** protein-substrate phosphorylation observed in vitro, catalyst unresolved — a *distinct* reaction, not VPS15's MF.
- **Downstream/indirect (not the tested MF):** VPS15 scaffolds PI3KC3, activates VPS34 lipid
  (not protein) kinase, and is itself a phospho-substrate/regulatory target — regulatory
  participation in phosphorylation-linked processes, not a phosphotransferase role.

---

## Conflicts and Alternatives

- **Attribution artifact:** complex activity assigned to a subunit that is a substrate in the same paper.
- **Homology carry-over:** UniProt/PANTHER retain kinase/transferase labels by similarity; IBA at
  the family root risks propagating catalytic MF to a leaf that lost catalysis.
- **Lipid- vs protein-kinase conflation:** the robust, reproducible VPS34-complex chemistry is
  *lipid* kinase (PtdIns→PtdIns3P); the "protein phosphorylation" claim rests on the weaker Table I assay.
- **Not contamination by default:** an unexpected Mn²⁺-preferring activity is *not* proof of
  contamination; it is best logged as unresolved associated activity, per the seed's caution.
- **VPS15 is the phospho-TARGET, not the enzyme:** PMID:34121209 shows VPS15 is a ULK substrate
  (six ULK-dependent sites; major Ser861), directly realizing the seed's "phosphorylated by another
  kinase" alternative. Its phosphorylation *regulates* VPS34 lipid-kinase output — a regulatory
  node in a phosphorylation pathway, not a protein phosphotransferase.
- **Real noncatalytic moonlighting:** PMID:37414850 shows a Vps34-independent nuclear coactivator
  role (Bmal1-Clock), confirming that "pseudokinase" ≠ "no function," but these functions are not
  "protein phosphorylation."

---

## Knowledge Gaps

1. **Which subunit is the Table I catalyst?** Checked: abstract + seed description; unresolved.
   Matters because it decides whether *any* protein-phosphorylation term belongs to VPS15.
   Resolve with: recombinant, individually purified catalytically-dead VPS34 vs VPS15 point mutants + substrate assays.
2. **Full text of PMID:39913640 nucleotide/geometry data.** Checked: abstract (truncated) + seed;
   full methods not retrieved here. Matters for firmness of "GTP-binding, no phosphotransfer."
3. **Current GO/UniProt evidence codes on the live record** (IBA vs NAS vs ISS). Checked: UniProt JSON
   (kinase keywords, no catalytic reaction); GO evidence-code audit needed for the exact annotation set.

---

## Discriminating Tests

- **Subunit-resolved kinase assay:** individually purified WT vs kinase-dead (D148A) VPS15 and
  VPS34 with peptide/protein substrates; ± Mn²⁺; test which subunit carries Table I activity.
- **Nucleotide-loading assay** (HPLC/MS or thermal shift) on isolated human VPS15 pseudokinase
  domain to confirm GTP-over-ATP preference and absence of γ-phosphate transfer.
- **Structure-guided catalytic-motif audit** (HRD, DFG, VAIK, glycine loop) on Q99570 vs bona fide STKs.
- **Orthology/PANTHER review** to reclassify the IBA MF at the leaf as pseudokinase.

---

## Curation Leads (require curator verification)

- **Candidate action:** Remove/retire GO:0006468 (NAS, PMID:8999962) as a VPS15 direct annotation;
  do not assign GO:0004672/GO:0004674 MF. Replace informativeness with PI3KC3 CC terms + autophagy/vesicle BP + a VPS34-lipid-kinase *regulator/activator* MF.
- **Candidate reference snippets to verify:**
  - PMID:39913640 — "The inactive conformation of the VPS15 pseudokinase stabilizes the inactive conformation…"
  - PMID:40442316 — "…extensive contacts between the FIP200 scaffold subunit of ULK1C and the VPS15, ATG14 and BECN1 subunits of PI3KC3-C1."
  - PMID:8999962 — "Recombinant p150 associated with PtdIns 3-kinase in vitro in a stable manner, resulting in a 2-fold increase in lipid kinase activity."
- **Suggested question for curators:** Is the NAS GO:0006468 meant to capture VPS15's own MF, or
  the complex's process participation? If the latter, a co-complex/regulatory annotation is more accurate than "protein phosphorylation."
- **Suggested experiment:** subunit-resolved catalytically-dead mutant kinase assay (above).

*Note:* This report deliberately did not re-run the previously completed NVJ analysis; it targets the
Panaretou-1997 vs modern-structure phosphotransfer chemistry, as instructed.


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)