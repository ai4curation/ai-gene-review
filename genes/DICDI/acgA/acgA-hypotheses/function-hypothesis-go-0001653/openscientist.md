---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-20T19:45:13.893266'
end_time: '2026-09-20T20:04:59.012463'
duration_seconds: 1185.12
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: DICDI
  gene: acgA
  gene_symbol: acgA
  uniprot_accession: Q03101
  taxon_id: NCBITaxon:44689
  taxon_label: Dictyostelium discoideum
  focus_type: function_assignment
  hypothesis_slug: function-hypothesis-go-0001653
  hypothesis_text: Dictyostelium discoideum ACG/acgA has peptide receptor activity
    (GO:0001653). Assess whether phosphopeptide SDF-1 is sensed by ACG itself or another
    receptor upstream of ACG, distinguishing dependence from direct receptor action
    and considering orthology, topology and primary experiments. An established osmosensor
    role does not itself exclude peptide sensing.
  term_context: No specific term context supplied.
  reference_context: No specific reference context supplied.
  source_file: genes/DICDI/acgA/acgA-ai-review.yaml
  source_selector: free-text
  source_context_yaml: "hypothesis: Dictyostelium discoideum ACG/acgA has peptide\
    \ receptor activity (GO:0001653). Assess whether\n  phosphopeptide SDF-1 is sensed\
    \ by ACG itself or another receptor upstream of ACG, distinguishing dependence\n\
    \  from direct receptor action and considering orthology, topology and primary\
    \ experiments. An established\n  osmosensor role does not itself exclude peptide\
    \ sensing.\nfocus_type: function_assignment\ncontext: []\nreference_id: []"
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
citation_count: 7
artifact_count: 4
artifact_sources:
  openscientist_artifacts_zip: 4
artifacts:
- filename: artifact_GO_decision_table.csv
  path: openscientist_artifacts/artifact_GO_decision_table.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist artifact GO decision table
- filename: artifact_IBA_provenance_GO0001653.csv
  path: openscientist_artifacts/artifact_IBA_provenance_GO0001653.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist artifact IBA provenance GO0001653
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

- **Organism code:** DICDI
- **Taxon:** Dictyostelium discoideum (NCBITaxon:44689)
- **Gene directory:** acgA
- **Gene symbol:** acgA
- **UniProt accession:** Q03101

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** function-hypothesis-go-0001653
- **Source file:** genes/DICDI/acgA/acgA-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

Dictyostelium discoideum ACG/acgA has peptide receptor activity (GO:0001653). Assess whether phosphopeptide SDF-1 is sensed by ACG itself or another receptor upstream of ACG, distinguishing dependence from direct receptor action and considering orthology, topology and primary experiments. An established osmosensor role does not itself exclude peptide sensing.

## Term and Decision Context

No specific term context supplied.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: Dictyostelium discoideum ACG/acgA has peptide receptor activity (GO:0001653). Assess whether
  phosphopeptide SDF-1 is sensed by ACG itself or another receptor upstream of ACG, distinguishing dependence
  from direct receptor action and considering orthology, topology and primary experiments. An established
  osmosensor role does not itself exclude peptide sensing.
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

# AIGR Gene Hypothesis Deep Research — *Dictyostelium discoideum* ACG/acgA (UniProt Q03101)

**Focus:** function_assignment — does ACG directly have **peptide receptor activity (GO:0001653)**?
**Hypothesis slug:** function-hypothesis-go-0001653
**Source:** genes/DICDI/acgA/acgA-ai-review.yaml (free-text)

---

## Summary

The GO:0001653 "peptide receptor activity" annotation on *Dictyostelium discoideum* ACG/acgA is **over-annotated** and should be flagged by a curator for **removal or NOT-qualification** (or at minimum demoted to non-core, low-confidence status). The annotation is supported **only by phylogenetic inference (IBA:GO_Central)**, whereas ACG's experimentally characterized molecular functions — adenylate cyclase activity, osmosensor activity, and dimerization — rest on direct assays. Decisively, the QuickGO provenance shows the peptide-receptor term was **propagated within PANTHER family PTN000229249 from mammalian natriuretic peptide receptors NPR1 (P16066) and NPR2 (P20594)** — receptor guanylyl cyclases that are the *genuine* peptide receptors — simply because ACG shares their "extracellular sensor + single transmembrane + class-III cyclase" architecture.

ACG's real molecular biology contradicts a direct peptide-receptor role. It is a **primary osmosensor**: expressed in a yeast adenylyl-cyclase-null background, it reconstitutes osmotic activation with no Dictyostelium-specific ligand or auxiliary sensor, proving the sensor is **intramolecular and ligand-independent**. Its extracellular module is a **CHASE small-molecule sensory domain** (Pfam PF03924), a domain family characterized as binding small molecules such as cytokinins — not peptides — and in Dictyostelium cytokinins are sensed by the histidine kinase DhkB, not ACG.

On the specific SDF-1 sub-question, the answer is clear: **there is no evidence that the phosphopeptide SDF-1 is sensed by ACG**, directly or as an upstream dependency. SDF-1 is a PKA-substrate phosphopeptide that acts through an **intracellular PKA-dependent pathway** at a *different developmental stage* (prespore→spore encapsulation) than ACG (osmolarity-dependent inhibition of mature-spore germination). SDF-1's receptor has never been identified, but no primary study links it to ACG. The most important caveat is that "refuted" reflects an evidence-of-absence plus positive-provenance argument — no published assay has tested and excluded ACG peptide binding directly — so the recommendation is stated conservatively.

---

## Executive Judgment

**Verdict: Over-annotated / Refuted for the seed hypothesis as stated (direct peptide receptor activity).**

Three converging lines of evidence support removal or NOT-qualification of GO:0001653 on ACG:

1. **The annotation is phylogenetic, not experimental.** In UniProt Q03101, GO:0001653 carries evidence code **IBA:GO_Central** (Inferred from Biological Ancestor, GO_REF:0000033). ACG's experimentally supported functions carry IDA/IPI codes. No IDA/IMP/IPI annotation supports peptide receptor activity.

2. **The provenance is a family carry-over from bona fide peptide receptors.** QuickGO shows the IBA term was propagated within PANTHER family PTN000229249 from human/mouse/rat natriuretic peptide receptors NPR1/NPR2 — receptor guanylyl cyclases that truly bind natriuretic peptides.

3. **ACG's real sensory mechanism is intramolecular and ligand-independent.** ACG reconstitutes osmotic activation in yeast with no partner, and its extracellular module is a CHASE small-molecule domain, not a peptide-binding fold.

Regarding SDF-1: there is no evidence it is sensed by ACG; it acts intracellularly via PKA at a different stage, and its receptor is unidentified but explicitly not ACG in any primary study.

**Most important caveat:** "Refuted" means the direct-receptor claim is unsupported and the GO annotation is family carry-over. It does **not** mean ACG was experimentally tested and shown unable to bind any peptide — no such negative binding assay exists. The osmosensor role does not logically exclude peptide sensing, but the hypothesis requires positive evidence that is simply absent.

---

## Key Findings

### Finding 1 — GO:0001653 rests only on phylogenetic inference (IBA), not experiment

The UniProt Q03101 GO cross-references show that **GO:0001653 (peptide receptor activity) carries evidence code IBA:GO_Central** — an annotation inferred phylogenetically from an ancestral protein via the GO_Central/PAINT pipeline (GO_REF:0000033). This is a computational/curatorial inference, not a wet-lab result. By contrast, ACG's molecular-function annotations with experimental backing are:

| GO term | Name | Evidence code | Basis |
|---|---|---|---|
| GO:0004016 | adenylate cyclase activity | IDA | Direct enzymatic assay |
| GO:0005034 | osmosensor activity | IDA | Direct osmotic-stimulation assay |
| GO:0042802 | identical protein binding | IPI | Dimerization (physical interaction) |
| **GO:0001653** | **peptide receptor activity** | **IBA** | **Phylogenetic inference only** |

The **domain architecture** of ACG is fully consistent with a receptor-cyclase and provides no dedicated peptide-binding module: an N-terminal signal-anchor transmembrane segment (residues 19–41), an extracellular **CHASE sensory domain** (~86–317; Pfam **PF03924** / InterPro IPR006189), and a C-terminal **class-III adenylyl/guanylyl-cyclase catalytic domain** (~396–526; Pfam PF00211). An IBA-only molecular-function term that conflicts with the experimentally characterized function should be treated as low-confidence and reviewed for removal or NOT-qualification.

### Finding 2 — ACG's extracellular sensor is a CHASE (small-molecule) domain, and activation is intramolecular/osmotic, not peptide-mediated

Two primary papers establish ACG as a **self-contained osmosensor**:

- **Saran & Schaap, 2004** [PMID: 14718564](https://pubmed.ncbi.nlm.nih.gov/14718564/): When ACG cDNA is expressed in a **yeast adenylyl-cyclase-null mutant**, cAMP production is activated by high osmolality "similarly … as in Dictyostelium." Because yeast lacks any Dictyostelium-specific ligand or auxiliary sensor, this **demonstrates the osmosensor is intramolecular**. The authors conclude ACG is "the first characterized primary osmosensor in eukaryotes." They further show dimerization (via a region outside the catalytic domain) is required for catalytic activity, but the dimer/monomer ratio does not change with osmolality — osmotic activation is not mediated by ligand-induced dimerization.

- **van Es et al., 1996** [PMID: 8798577](https://pubmed.ncbi.nlm.nih.gov/8798577/): *acg⁻* spores lose osmolarity-dependent inhibition of germination; ACG activity (in *aca⁻*/ACG cells) is "strongly stimulated by high osmolarity with optimal stimulation occurring at 200 milliosmolar."

Mechanistically, ACG's extracellular module is a **CHASE domain** (Pfam PF03924). Characterized CHASE domains bind **small molecules** — most notably cytokinins in plant hybrid histidine-kinase receptors ([PMID: 17439640](https://pubmed.ncbi.nlm.nih.gov/17439640/), [PMID: 15498549](https://pubmed.ncbi.nlm.nih.gov/15498549/)) — not peptides. In Dictyostelium itself, cytokinins act through the histidine kinase **DhkB**, not ACG ([PMID: 18216168](https://pubmed.ncbi.nlm.nih.gov/18216168/)), underscoring that ACG's CHASE domain is not the organism's peptide/hormone receptor. ACG activation is therefore an osmotically driven intramolecular conformational change, with no evidence of peptide-ligand binding.

### Finding 3 — No evidence links phosphopeptide SDF-1 to ACG; SDF-1 acts intracellularly via PKA at a different developmental stage

The seed asks specifically whether the phosphopeptide **SDF-1** is sensed by ACG. Primary literature answers in the negative:

- **Anjard, van Bemmelen, Véron & Reymond, 1997** [PMID: 9373946](https://pubmed.ncbi.nlm.nih.gov/9373946/): SDF-1 is "a small, thermostable phospho-polypeptide." In-vitro dephosphorylation reduces its spore-differentiation activity, and PKA re-phosphorylation restores it — SDF-1 is a **PKA substrate**, and "the response of prespore cells to SDF involves an **intracellular pathway dependent on PKA**."

- **Anjard, Zeng, Loomis & Nellen, 1998** [PMID: 9473320](https://pubmed.ncbi.nlm.nih.gov/9473320/): *tagC⁻*, *dhkA⁻*, and *regA⁻* null strains **still sporulate in response to SDF-1**, showing SDF-1 does *not* use the DhkA two-component pathway (which transduces the distinct peptide SDF-2). SDF-1's receptor was not identified.

Crucially, **SDF-1 and ACG operate at different developmental stages**: SDF-1 governs prespore-cell encapsulation (sporulation), whereas ACG governs osmolarity-dependent **inhibition of mature-spore germination** ([PMID: 8798577](https://pubmed.ncbi.nlm.nih.gov/8798577/)). No primary study reports SDF-1 binding to or signaling through ACG. The seed's "distinguish dependence from direct receptor action" framing collapses: there is neither a demonstrated dependence of SDF-1 signaling on ACG nor any direct SDF-1–ACG interaction.

### Finding 4 — The IBA "peptide receptor activity" was propagated from natriuretic peptide receptors NPR1/NPR2

The decisive provenance comes from the **QuickGO annotation record** for Q03101 / GO:0001653 (evidence ECO:0000318/IBA, GO_REF:0000033, assignedBy GO_Central, PANTHER family **PTN000229249**). Its `withFrom` field lists the seed proteins:

| withFrom accession | Protein | True function |
|---|---|---|
| UniProtKB **P16066** | Human Atrial natriuretic peptide receptor 1 (NPR1 / GC-A) | Natriuretic peptide receptor + guanylate cyclase |
| UniProtKB **P20594** | Human Atrial natriuretic peptide receptor 2 (NPR2 / GC-B) | Natriuretic peptide receptor + guanylate cyclase |
| MGI:97372 | Mouse Npr1 | Natriuretic peptide receptor |
| RGD:69322 | Rat Npr1 | Natriuretic peptide receptor |
| FBgn0266136 | *Drosophila* receptor guanylyl cyclase | Receptor guanylyl cyclase |

P16066 and P20594 both carry **GO:0016941 (natriuretic peptide receptor activity)** and **GO:0004383 (guanylate cyclase activity)** — bona fide peptide (natriuretic) receptors. ACG shares the receptor-cyclase architecture (extracellular sensor + single TM + class-III cyclase catalytic domain, annotated PF00211 "Guanylate_cyc"), causing it to cluster in the **same PANTHER family** and to **inherit "peptide receptor activity"** by descent. This is a textbook case of family-level over-annotation: a genuine molecular function of the mammalian members is projected onto a divergent social-amoeba enzyme whose actual ligand is osmotic pressure, not a peptide.

---

## Mechanistic Model / Interpretation

The findings assemble into an internally consistent picture that separates **what ACG actually does** from **what the GO term claims**.

```
        ┌──────────────────────────────────────────────────────────┐
        │  ACG (Q03101) domain architecture                        │
        │                                                          │
        │   TM(19–41)   CHASE (86–317)        Class-III cyclase     │
        │   signal-     small-molecule/       catalytic (~396–526)  │
        │   anchor      osmo-sensory          PF00211               │
        │     │         PF03924                    │                │
        │  ───┴─────────[   sensor   ]────TM────[ ATP → cAMP ]      │
        └──────────────────────────────────────────────────────────┘
              ▲                                        │
      HIGH OSMOLALITY (intramolecular)                 ▼
      optimal ~200 mOsm  ──► conformational ──►  cAMP ↑ ──► PKA
      (reconstitutes in yeast, no ligand)                    │
                                                             ▼
                                          INHIBITION of spore germination
```

**ACG's verified role (spore germination, mature spore):** high external osmolality is sensed *intramolecularly* by ACG, stimulating adenylyl cyclase activity, raising cAMP, activating PKA, and keeping spores dormant until dispersal to low-osmolality environments. No peptide and no partner receptor is required — the yeast reconstitution proves it.

**The SDF-1 pathway is a separate module (sporulation, prespore cells):** SDF-1 is an intracellular PKA-substrate phosphopeptide promoting prespore→spore encapsulation. It does not use DhkA/TagC/RegA, and its surface receptor (if any) is unknown. It has no demonstrated connection to ACG.

```
  Peptide/ligand signaling in Dictyostelium sporulation (for contrast — NOT ACG):
    SDF-2 peptide  ──►  DhkA (histidine kinase receptor) ──┤ RegA PDE ──► cAMP↑ ──► PKA
    SDF-1 phospho- ──►  (unknown receptor) ── intracellular PKA-dependent pathway
      peptide
    GABA           ──►  GrlE (GPCR) ──► AcbA release ──► TagC cleaves ──► SDF-2
    cytokinins     ──►  DhkB (histidine kinase)
```

The seed hypothesis conflates two things: (a) ACG's *architectural* resemblance to mammalian peptide-receptor cyclases, and (b) the existence of peptide signals (SDF-1/SDF-2) *elsewhere* in Dictyostelium sporulation. Neither establishes that ACG is a peptide receptor. The genuine peptide receptor in this system is **DhkA** (for SDF-2), a histidine kinase — architecturally and mechanistically distinct from ACG.

**GO decision summary:**

| GO term | Aspect | Current evidence on ACG | Recommended action (curator lead) |
|---|---|---|---|
| GO:0001653 peptide receptor activity | MF | IBA only; family carry-over from NPR1/NPR2 | **Remove or NOT-qualify** (non-core; unsupported) |
| GO:0004016 adenylate cyclase activity | MF | IDA | Retain (core) |
| GO:0005034 osmosensor activity | MF | IDA | Retain (core) |
| GO:0042802 identical protein binding | MF | IPI (dimerization) | Retain |

---

## Evidence Base / Evidence Matrix

| Citation (PMID) | Evidence type | Supports/Refutes/Qualifies | Claim tested | Key finding | Context | Confidence & limitations |
|---|---|---|---|---|---|---|
| [14718564](https://pubmed.ncbi.nlm.nih.gov/14718564/) Saran & Schaap 2004 | Direct assay (heterologous reconstitution) | **Refutes** peptide-receptor need | Is ACG's sensor intramolecular or ligand/co-receptor dependent? | ACG reconstitutes osmotic activation in yeast AC-null; dimerization needed for catalysis but not osmosensing | *Dictyostelium* ACG in *S. cerevisiae* | High. Excludes need for auxiliary/peptide sensor. Does not test peptide binding per se. |
| [8798577](https://pubmed.ncbi.nlm.nih.gov/8798577/) van Es et al. 1996 | Mutant phenotype + enzyme assay | **Refutes** (defines true function) | What is ACG's physiological role? | *acg⁻* loses osmolarity-dependent germination inhibition; ACG stimulated by high osmolarity (opt. ~200 mOsm) | *Dictyostelium* spores | High. Osmosensor role at germination stage, distinct from SDF-1. |
| [9373946](https://pubmed.ncbi.nlm.nih.gov/9373946/) Anjard et al. 1997 | Biochemical (phosphorylation) | **Qualifies/Refutes** SDF-1–ACG link | Where does SDF-1 act? | SDF-1 is a thermostable phospho-polypeptide, PKA substrate; response via intracellular PKA pathway | *Dictyostelium* prespore cells | High for SDF-1 biochemistry; SDF-1 receptor not identified. |
| [9473320](https://pubmed.ncbi.nlm.nih.gov/9473320/) Anjard et al. 1998 | Genetic (null strains) | **Refutes** SDF-1 via two-component/ACG pathway | Does SDF-1 use DhkA/TagC/RegA? | *tagC⁻/dhkA⁻/regA⁻* still respond to SDF-1; receptor unidentified | *Dictyostelium* | High. Rules out known peptide-receptor pathway; ACG never implicated. |
| QuickGO record (GO_Central IBA), UniProt Q03101 | Review/database (provenance) | **Refutes** (explains over-annotation) | Where did GO:0001653 come from? | IBA propagated in PANTHER PTN000229249 from NPR1(P16066)/NPR2(P20594) etc. | Cross-species PAINT family | High for provenance; database-level, not experimental. |
| UniProt Q03101 GO cross-refs | Database (evidence codes) | **Qualifies** | Is peptide-receptor term experimental? | Peptide receptor = IBA; AC/osmosensor/dimerization = IDA/IPI | — | High. Evidence-code contrast is decisive. |
| [17439640](https://pubmed.ncbi.nlm.nih.gov/17439640/) CHASE cytokinin binding | Structural/evolutionary + binding assay | **Qualifies** (CHASE = small-molecule sensor) | What do CHASE domains bind? | CHASE domain binds cytokinin (small molecule); key residues identified | Plant/orphan receptors | Medium-high. Family-level, not tested on ACG's CHASE directly. |
| [15498549](https://pubmed.ncbi.nlm.nih.gov/15498549/) CHASE structure prediction | Structural/computational | **Qualifies** | CHASE fold & ligand pocket | CHASE resembles PAS/PYP-like small-molecule sensor domain | Bioinformatics | Medium. Prediction-level. |
| [18216168](https://pubmed.ncbi.nlm.nih.gov/18216168/) Cytokinins in Dictyostelium | Genetic/pathway | **Qualifies** | Which receptor senses cytokinins in Dictyostelium? | Cytokinins act via DhkB, not ACG | *Dictyostelium* | High. ACG's CHASE is not the organism's hormone receptor. |
| [15590560](https://pubmed.ncbi.nlm.nih.gov/15590560/) AC review | Review/database | Orientation | ACG's role among the 3 cyclases | ACG "acts as an osmosensor … controlling spore germination" | *Dictyostelium* | Review-level orientation. |
| [10373524](https://pubmed.ncbi.nlm.nih.gov/10373524/) DhkA/SDF-2 | Direct (topology, enzymology) | **Competing** (identifies the real peptide receptor) | What receptor senses peptide SDF-2? | DhkA histidine kinase with extracellular ligand loop transduces SDF-2 | *Dictyostelium* | High. Genuine peptide receptor is DhkA, not ACG. |

---

## GO Curation Implications

**Lead (requires curator verification):** Flag **GO:0001653 (peptide receptor activity)** on Q03101 for **removal or NOT-qualification**, or at minimum reclassify as **non-core, low-confidence propagated (IBA) annotation**.

- **Aspect:** Molecular Function.
- **Rationale:** The term is IBA-only and its `withFrom` provenance traces to natriuretic peptide receptors NPR1/NPR2. ACG's experimentally supported MF terms (adenylate cyclase, osmosensor) and its intramolecular, ligand-independent activation contradict a direct peptide-receptor function. This is family-level over-annotation driven by shared receptor-cyclase architecture and the PF00211 "Guanylate_cyc" catalytic-domain label.
- **Retain as core:** GO:0004016 (adenylate cyclase activity, IDA) and GO:0005034 (osmosensor activity, IDA).
- **Do not substitute "protein binding":** The informative, supported terms are the adenylate-cyclase and osmosensor activities; GO:0042802 (identical protein binding, IPI) captures dimerization but is not a substitute for core catalytic/sensory functions.
- **If NOT-qualification is preferred over deletion:** annotate GO:0001653 with a NOT qualifier and an ECO code reflecting curatorial review, citing the intramolecular osmosensor reconstitution ([PMID: 14718564](https://pubmed.ncbi.nlm.nih.gov/14718564/)) and the absence of any peptide-binding assay.

---

## Mechanistic Scope

The molecular function under test is **direct peptide receptor activity** — ACG binding an extracellular peptide ligand at its own extracellular domain and transducing that binding into a signaling output.

- **Direct gene-product activity (supported):** osmolality sensing (intramolecular) and ATP→cAMP catalysis — properties of the ACG polypeptide itself, demonstrated by heterologous reconstitution and enzyme assays.
- **Downstream / pathway consequences (not the MF being tested):** cAMP→PKA activation→inhibition of spore germination — a developmental output, not evidence of a receptor–peptide interaction.
- **Separate signaling modules (not ACG):** SDF-1 (intracellular PKA substrate), SDF-2 (peptide sensed by DhkA), GABA (via GrlE GPCR), cytokinins (via DhkB). None implicates ACG as a peptide receptor.

There is no experimental measurement of ACG at the level required to support GO:0001653 — a binding assay or a functional readout demonstrating peptide-dependent activation of ACG.

---

## Conflicts and Alternatives

1. **Paralog/family confusion (primary explanation).** ACG co-clusters in PANTHER PTN000229249 with mammalian natriuretic peptide receptors, which *are* peptide receptors; ACG is not. IBA cannot distinguish the divergence of the extracellular sensor (CHASE small-molecule/osmo-sensor in ACG vs. natriuretic-peptide-binding ectodomain in NPR1/2), so it over-projects the term.
2. **Architecture-driven false positive.** ACG's catalytic domain is annotated PF00211 ("Guanylate_cyc"), reinforcing the guanylyl-cyclase-receptor analogy even though ACG functions as an *adenylyl* cyclase — likely amplifying the mis-annotation.
3. **Organism-specific divergence.** Dictyostelium uses histidine-kinase receptors (DhkA, DhkB) and GPCRs (GrlE) for peptide/hormone signaling — not receptor guanylyl/adenylyl cyclases. The mammalian receptor-cyclase paradigm does not map onto ACG's biology.
4. **Alternative reading of the seed's "dependence" clause.** One could hypothesize SDF-1 signaling *depends on* ACG-generated cAMP. But SDF-1 acts in prespore cells during sporulation, whereas ACG functions in mature spores during germination; the stages and cell types differ, and no genetic epistasis links them. The dependence interpretation is unsupported.
5. **What would genuinely conflict with the refutation:** a direct SDF-1 (or other peptide) binding assay on ACG, or an *acg⁻* phenotype in SDF-1-driven sporulation. Neither exists in the literature reviewed.

---

## Limitations and Knowledge Gaps

| Gap | What was checked | Why it matters for curation | What would resolve it |
|---|---|---|---|
| No direct negative binding assay | Primary literature (osmosensor, SDF-1, SDF-2 papers) | "Refuted" rests on absence of positive evidence + provenance, not a published no-binding result | In-vitro peptide-binding assay (SPR/ITC) of ACG ectodomain vs. SDF-1/candidate peptides |
| SDF-1 receptor identity unknown | [PMID: 9373946](https://pubmed.ncbi.nlm.nih.gov/9373946/), [PMID: 9473320](https://pubmed.ncbi.nlm.nih.gov/9473320/) | If SDF-1's receptor were ever shown to be ACG, the hypothesis would revive | Identify SDF-1 surface receptor by crosslinking/genetics; test *acg⁻* SDF-1 response |
| CHASE ligand of ACG not directly assayed | CHASE family papers ([PMID: 17439640](https://pubmed.ncbi.nlm.nih.gov/17439640/), [15498549](https://pubmed.ncbi.nlm.nih.gov/15498549/)) | ACG's CHASE is inferred as small-molecule/osmo-sensor by homology, not directly tested for ligands | Ligand screen of purified ACG CHASE domain |
| QuickGO provenance read manually | QuickGO/UniProt records | Confirms carry-over but is database-level; PANTHER membership should be re-verified at curation time | Curator re-checks PTN000229249 tree and current IBA propagation |
| Structural model of ACG ectodomain not built here | Domain annotations only (Pfam/InterPro) | A structure could confirm the absence of a peptide-binding groove | AlphaFold model + pocket analysis of ACG residues 86–317 |

---

## Discriminating Tests

1. **Direct peptide-binding assay on ACG.** Purify the ACG extracellular/CHASE domain (~86–317) and test binding to SDF-1 and other candidate peptides by SPR, ITC, or MST. *No binding* → refutes conclusively; *specific binding* → reopens the hypothesis.
2. **Genetic epistasis of SDF-1 vs. ACG.** Test whether *acg⁻* cells retain a normal SDF-1 sporulation response. If yes, SDF-1 signaling is ACG-independent.
3. **Yeast reconstitution + peptide challenge.** Extend the Saran & Schaap yeast system ([PMID: 14718564](https://pubmed.ncbi.nlm.nih.gov/14718564/)) by adding candidate peptides to test for peptide-dependent ACG activation beyond osmotic stimulation.
4. **Structural pocket analysis.** Build an AlphaFold model of the ACG ectodomain and computationally dock SDF-1; compare its pocket geometry to the NPR1/NPR2 natriuretic-peptide-binding ectodomain to confirm fold divergence.
5. **PANTHER tree re-inspection.** Verify that GO:0001653 propagation in PTN000229249 originates solely from natriuretic peptide receptors and that no experimentally annotated non-mammalian member independently supports peptide binding.

---

## Proposed Follow-up Experiments / Actions (Curation Leads)

All items are **leads requiring curator verification.**

**Candidate action change:**
- Set **GO:0001653 (peptide receptor activity)** to **removed** or **NOT-qualified** for Q03101; document as IBA family carry-over from natriuretic peptide receptors. Retain GO:0004016 and GO:0005034 as core MF terms; retain GO:0042802 for dimerization.

**Candidate references + snippets to verify:**
- [PMID: 14718564](https://pubmed.ncbi.nlm.nih.gov/14718564/) — *"This strongly suggests that the ACG osmosensor is intramolecular, which would define ACG as the first characterized primary osmosensor in eukaryotes."*
- [PMID: 8798577](https://pubmed.ncbi.nlm.nih.gov/8798577/) — *"ACG is an osmosensor controlling spore germination through activation of protein kinase A."*
- [PMID: 9373946](https://pubmed.ncbi.nlm.nih.gov/9373946/) — *"the response of prespore cells to SDF involves an intracellular pathway dependent on PKA."*
- [PMID: 9473320](https://pubmed.ncbi.nlm.nih.gov/9473320/) — *tagC⁻/dhkA⁻/regA⁻* strains "all sporulated efficiently when SDF-1 was added."
- [PMID: 18216168](https://pubmed.ncbi.nlm.nih.gov/18216168/) — cytokinins act "through a different histidine kinase, DhkB."

**Candidate retained GO terms:**
- MF: GO:0004016 (adenylate cyclase activity) — retain, core.
- MF: GO:0005034 (osmosensor activity) — retain, core.
- MF: GO:0042802 (identical protein binding) — retain (dimerization).
- BP: consider osmosensory-signaling / regulation of spore germination terms consistent with [PMID: 8798577](https://pubmed.ncbi.nlm.nih.gov/8798577/).

**Suggested curator questions:**
- Does any experimentally annotated member of PANTHER PTN000229249 support GO:0001653 independently of natriuretic peptide receptors?
- Is there any post-2004 primary study assigning a peptide ligand to ACG? (None found here.)

**Suggested experiments:** Items 1–3 under *Discriminating Tests* (direct binding assay; *acg⁻* SDF-1 epistasis; yeast reconstitution + peptide challenge).

---

## Notes on Reproducibility and Provenance

The conclusions rest on (a) the **evidence-code contrast** in UniProt Q03101 (IBA for GO:0001653 vs. IDA/IPI for characterized functions), (b) the **QuickGO `withFrom` provenance** listing NPR1/NPR2 as the IBA seed proteins, and (c) primary experimental papers on ACG osmosensing and SDF-1 signaling. Where a specific value (e.g., PANTHER family ID PTN000229249) is quoted, it should be re-verified by the curator at the current database version, since IBA propagations can change over time. No peptide-binding assay for ACG exists in the literature reviewed; the refutation is therefore an evidence-of-absence plus positive-provenance argument, stated conservatively.

---

*Prepared for AI Gene Review — hypothesis-level curation support. All annotations flagged here are leads requiring curator verification.*


## Artifacts

- [OpenScientist artifact GO decision table](openscientist_artifacts/artifact_GO_decision_table.csv)
- [OpenScientist artifact IBA provenance GO0001653](openscientist_artifacts/artifact_IBA_provenance_GO0001653.csv)
- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)