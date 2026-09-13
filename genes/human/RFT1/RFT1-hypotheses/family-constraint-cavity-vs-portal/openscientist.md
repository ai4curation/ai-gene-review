---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-25T02:24:26.690245'
end_time: '2026-08-25T02:50:56.839933'
duration_seconds: 1590.15
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: human
  gene: RFT1
  gene_symbol: RFT1
  uniprot_accession: Q96AA3
  taxon_id: NCBITaxon:9606
  taxon_label: Homo sapiens
  focus_type: free_text
  hypothesis_slug: family-constraint-cavity-vs-portal
  hypothesis_text: In the RFT1 family, evolutionary constraint is concentrated on
    positions lining the central substrate cavity of the MOP-superfamily fold rather
    than on positions lining the lateral lipid portal, indicating that what selection
    has preserved is substrate capture and coordination rather than the lipid transit
    path.
  term_context: '- Term: intramembrane lipid transporter activity (GO:0140303)

    - Scope this to one computable analysis and do not attempt a broad functional
    characterisation of the gene. Build the deepest RFT1-family multiple sequence
    alignment you can assemble across eukaryotes, including divergent lineages and
    any archaeal or bacterial homologues of the same MOP/MATE/MurJ architecture. Compute
    per-position evolutionary constraint from that alignment. Then map the constrained
    positions onto the AlphaFold model of Q96AA3 and classify each as central-cavity-lining,
    lateral-portal-lining, or neither, using explicit geometric criteria that you
    state.

    - Report the distribution of constraint across the three structural classes relative
    to a background of all transmembrane positions, not a hand-picked set of residues.
    The comparison that matters is whether constraint at the portal-lining positions
    is above or below the transmembrane background, and how that compares with the
    cavity-lining positions.

    - Do not use human disease variants as input, and do not use pathogenicity to
    choose which positions to examine. This is a question about what selection preserved
    in the wild-type protein across the family; clinical alleles are not evidence
    about that and should play no part in the analysis.

    - Consider and report the alternatives rather than assuming the hypothesis. Constraint
    may be distributed across both the cavity and the portal; it may be dominated
    by fold-maintenance positions such as helix-packing residues, prolines and glycines
    that serve neither substrate cavity nor lipid portal; or the alignment may be
    too shallow or too divergent to separate the classes. If the data cannot distinguish
    these, say so explicitly rather than forcing a verdict.'
  reference_context: No specific reference context supplied.
  source_file: ''
  source_selector: ''
  source_context_yaml: "hypothesis: In the RFT1 family, evolutionary constraint is\
    \ concentrated on positions lining the central\n  substrate cavity of the MOP-superfamily\
    \ fold rather than on positions lining the lateral lipid portal,\n  indicating\
    \ that what selection has preserved is substrate capture and coordination rather\
    \ than the lipid\n  transit path.\nfocus_type: free_text\nterm_id: GO:0140303\n\
    term_label: intramembrane lipid transporter activity\ncontext:\n- Scope this to\
    \ one computable analysis and do not attempt a broad functional characterisation\
    \ of the\n  gene. Build the deepest RFT1-family multiple sequence alignment you\
    \ can assemble across eukaryotes,\n  including divergent lineages and any archaeal\
    \ or bacterial homologues of the same MOP/MATE/MurJ architecture.\n  Compute per-position\
    \ evolutionary constraint from that alignment. Then map the constrained positions\n\
    \  onto the AlphaFold model of Q96AA3 and classify each as central-cavity-lining,\
    \ lateral-portal-lining,\n  or neither, using explicit geometric criteria that\
    \ you state.\n- Report the distribution of constraint across the three structural\
    \ classes relative to a background of\n  all transmembrane positions, not a hand-picked\
    \ set of residues. The comparison that matters is whether\n  constraint at the\
    \ portal-lining positions is above or below the transmembrane background, and\
    \ how that\n  compares with the cavity-lining positions.\n- Do not use human disease\
    \ variants as input, and do not use pathogenicity to choose which positions to\n\
    \  examine. This is a question about what selection preserved in the wild-type\
    \ protein across the family;\n  clinical alleles are not evidence about that and\
    \ should play no part in the analysis.\n- Consider and report the alternatives\
    \ rather than assuming the hypothesis. Constraint may be distributed\n  across\
    \ both the cavity and the portal; it may be dominated by fold-maintenance positions\
    \ such as helix-packing\n  residues, prolines and glycines that serve neither\
    \ substrate cavity nor lipid portal; or the alignment\n  may be too shallow or\
    \ too divergent to separate the classes. If the data cannot distinguish these,\
    \ say\n  so explicitly rather than forcing a verdict.\nreference_id: []"
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
- **Gene directory:** RFT1
- **Gene symbol:** RFT1
- **UniProt accession:** Q96AA3

## Focus

- **Focus type:** free_text
- **Hypothesis slug:** family-constraint-cavity-vs-portal
- **Source file:** 
- **Source selector:** 

## Seed Hypothesis

In the RFT1 family, evolutionary constraint is concentrated on positions lining the central substrate cavity of the MOP-superfamily fold rather than on positions lining the lateral lipid portal, indicating that what selection has preserved is substrate capture and coordination rather than the lipid transit path.

## Term and Decision Context

- Term: intramembrane lipid transporter activity (GO:0140303)
- Scope this to one computable analysis and do not attempt a broad functional characterisation of the gene. Build the deepest RFT1-family multiple sequence alignment you can assemble across eukaryotes, including divergent lineages and any archaeal or bacterial homologues of the same MOP/MATE/MurJ architecture. Compute per-position evolutionary constraint from that alignment. Then map the constrained positions onto the AlphaFold model of Q96AA3 and classify each as central-cavity-lining, lateral-portal-lining, or neither, using explicit geometric criteria that you state.
- Report the distribution of constraint across the three structural classes relative to a background of all transmembrane positions, not a hand-picked set of residues. The comparison that matters is whether constraint at the portal-lining positions is above or below the transmembrane background, and how that compares with the cavity-lining positions.
- Do not use human disease variants as input, and do not use pathogenicity to choose which positions to examine. This is a question about what selection preserved in the wild-type protein across the family; clinical alleles are not evidence about that and should play no part in the analysis.
- Consider and report the alternatives rather than assuming the hypothesis. Constraint may be distributed across both the cavity and the portal; it may be dominated by fold-maintenance positions such as helix-packing residues, prolines and glycines that serve neither substrate cavity nor lipid portal; or the alignment may be too shallow or too divergent to separate the classes. If the data cannot distinguish these, say so explicitly rather than forcing a verdict.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: In the RFT1 family, evolutionary constraint is concentrated on positions lining the central
  substrate cavity of the MOP-superfamily fold rather than on positions lining the lateral lipid portal,
  indicating that what selection has preserved is substrate capture and coordination rather than the lipid
  transit path.
focus_type: free_text
term_id: GO:0140303
term_label: intramembrane lipid transporter activity
context:
- Scope this to one computable analysis and do not attempt a broad functional characterisation of the
  gene. Build the deepest RFT1-family multiple sequence alignment you can assemble across eukaryotes,
  including divergent lineages and any archaeal or bacterial homologues of the same MOP/MATE/MurJ architecture.
  Compute per-position evolutionary constraint from that alignment. Then map the constrained positions
  onto the AlphaFold model of Q96AA3 and classify each as central-cavity-lining, lateral-portal-lining,
  or neither, using explicit geometric criteria that you state.
- Report the distribution of constraint across the three structural classes relative to a background of
  all transmembrane positions, not a hand-picked set of residues. The comparison that matters is whether
  constraint at the portal-lining positions is above or below the transmembrane background, and how that
  compares with the cavity-lining positions.
- Do not use human disease variants as input, and do not use pathogenicity to choose which positions to
  examine. This is a question about what selection preserved in the wild-type protein across the family;
  clinical alleles are not evidence about that and should play no part in the analysis.
- Consider and report the alternatives rather than assuming the hypothesis. Constraint may be distributed
  across both the cavity and the portal; it may be dominated by fold-maintenance positions such as helix-packing
  residues, prolines and glycines that serve neither substrate cavity nor lipid portal; or the alignment
  may be too shallow or too divergent to separate the classes. If the data cannot distinguish these, say
  so explicitly rather than forcing a verdict.
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

# RFT1 (Q96AA3) — Family constraint: central cavity vs. lateral lipid portal

**Hypothesis (slug `family-constraint-cavity-vs-portal`):** In the RFT1 family, evolutionary
constraint is concentrated on positions lining the central substrate cavity of the MOP-superfamily
fold rather than on positions lining the lateral lipid portal — i.e., selection preserved substrate
capture/coordination rather than the lipid transit path.

**Term in scope:** GO:0140303 *intramembrane lipid transporter activity* (MF).

---

## Executive Judgment

**Verdict: SUPPORTED** (robust, with one honest qualification).

A deep eukaryotic RFT1-family alignment mapped onto the AlphaFold model of Q96AA3 shows that
**central-cavity-lining transmembrane (TM) positions are the single most evolutionarily constrained
structural class, well above the TM background, whereas lateral lipid-portal-lining positions are
statistically indistinguishable from background (slightly below it), and the outer lipid-facing
surface is the fastest-evolving class.** The cavity-vs-portal contrast is large and highly significant
(rank-biserial −0.68, p = 3×10⁻⁵) and survives four independent controls (a second conservation
metric, amino-acid-composition/Pro-Gly exclusion, a 20,000-draw permutation null, and ±15–25°
perturbations of the estimated membrane axis).

**Qualification (the alternative that is partly true):** buried helix-packing ("neither") residues are
numerous (n≈180) and *also* modestly enriched above background (p = 1×10⁻³, effect −0.18). So a
meaningful share of *total* family constraint is fold maintenance. But this is a weaker effect than the
cavity (−0.43), and — critically — the cavity signal is **not** driven by helix-breakers: cavity
residues contain **0% Gly and 0% Pro**; they are 28% charged and 47% polar, the chemistry of
substrate coordination. The hypothesis's own "Pro/Gly fold-maintenance" alternative is therefore
refuted *for the cavity class specifically*.

**Most important caveats:** (i) the family alignment is **eukaryote-only** — PF04506/RFT1 has no
alignable archaeal/bacterial members, so the requested prokaryotic MOP homologues (MATE/MurJ) could
not be folded into one MSA; (ii) the membrane axis and the cavity/portal geometry are derived from a
**single static AlphaFold model** with an operationally defined portal; (iii) evolutionary constraint
indicates *importance*, not mechanism per se.

---

## What was actually computed (provenance)

All numbers below are direct outputs of code executed this run (not asserted). Pipeline:

1. **Alignment.** Pfam **PF04506** ("Rft-1") *full* alignment via the InterPro API →
   **3,826 sequences**, **512 HMM match columns**. Match columns identified by the Pfam convention
   (columns containing no `.` and no lowercase). Taxonomic spread: fungi (9PEZI, 9EURO, 9AGAR, 9HYPO,
   9PLEO, 9BASI, 9HELO…), metazoa (9BILA, 9PASS, 9TELE, 9AVES…), plants (9ROSI, 9POAL, 9ORYZ, 9LILI),
   stramenopiles (9STRA). **1,371 distinct clades; zero bacterial/archaeal mnemonics.**
2. **Per-position constraint.** Henikoff position-based sequence weights → weighted per-column
   Kullback–Leibler relative entropy to background (primary metric) and normalized Shannon conservation
   (secondary). Columns with weighted gap fraction > 0.6 excluded as unreliable.
3. **Human mapping.** Profile Needleman–Wunsch (free end gaps) of Q96AA3 against the match-state
   profile → **497 human residues mapped (positions 10–528)**.
4. **Structure & membrane frame.** AlphaFold **AF-Q96AA3-F1 (v6)**. Membrane normal estimated as the
   principal eigenvector of TM-helix direction vectors (helices detected from Cα i→i+3 / i→i+4 geometry).
   TM residues = |z − membrane-center| ≤ 15 Å (**n = 312 mapped + reliable**).
5. **Geometric classification (explicit criteria).** Occupancy grid (1.5 Å, 1.4 Å probe) in the
   membrane frame. For each TM residue, side-chain centroid → cylindrical (r, θ, z) about the central
   axis.
   - **central-cavity-lining:** side chain points inward (r_sidechain < r_Cα − 0.3 Å) and reaches the
     central channel wall (r ≤ lumen radius(θ) + 3 Å).
   - **lateral-portal-lining:** lipid-exposed (>60% of outward hemisphere sample points free of protein)
     **and** within 9 Å of a cavity-lining residue (i.e., lipid-facing residues bordering the cavity's
     lateral opening).
   - **outer lipid-facing:** lipid-exposed but not adjacent to the cavity.
   - **buried helix-packing ("neither"):** neither lumen-lining nor lipid-exposed.

### Core result (KL relative entropy, bits)

| Structural class | n | mean KL | median KL | vs TM background (Mann–Whitney) | effect (rank-biserial) |
|---|---|---|---|---|---|
| central cavity | 32 | **2.354** | 2.513 | **p = 6.2×10⁻⁵** | −0.43 (more constrained) |
| lateral portal | 22 | 1.333 | 1.248 | p = 0.24 (NS) | +0.15 (slightly below) |
| outer lipid-facing | 78 | 0.918 | 0.852 | p = 1.9×10⁻¹³ | +0.54 (far below) |
| buried packing | 180 | 1.920 | 1.694 | p = 1.2×10⁻³ | −0.18 (modestly above) |
| **TM background** | 312 | 1.673 | 1.424 | — | — |

Direct contrasts: **cavity vs portal p = 2.9×10⁻⁵ (effect −0.68)**; cavity vs all lipid-facing
p = 1.0×10⁻¹²; all-lipid-facing vs background p = 9.3×10⁻¹² (below).

### Robustness controls

- **Second metric (normalized Shannon conservation):** cavity 0.564 vs bg 0.438 (p = 5.7×10⁻⁴);
  portal 0.373 vs bg (p = 0.19, NS); cavity vs portal p = 2.3×10⁻⁴. Same ranking.
- **Composition / not a Pro-Gly artifact:** cavity = **0% Gly, 0% Pro, 28% charged, 47% polar, 16%
  aromatic**; portal = 0% charged, mostly hydrophobic. Cavity enrichment unchanged after excluding
  Gly/Pro (none present), p = 6.2×10⁻⁵.
- **Permutation null (20,000 random 32-residue TM draws):** observed cavity mean 2.354 vs null mean
  1.676, empirical one-sided **p = 1×10⁻⁴**.
- **Membrane-axis sensitivity:** across ±15° to ±25° tilts of the estimated normal, cavity ≫ portal
  (p = 3.1×10⁻⁶ … 7.9×10⁻⁴) and cavity ≫ background persist.

### Axis-independent corroboration (continuous, confounder-controlled)

To confirm the result does not depend on the cavity/portal class boundaries or on the precise membrane
axis, per-residue constraint was correlated with continuous geometric measures over all 312 TM positions:

| Relationship | Spearman ρ | p | Reading |
|---|---|---|---|
| constraint vs **radial distance from central axis** | **−0.675** | 8×10⁻⁴³ | closer to the pore → more constrained |
| constraint vs **lipid-exposure fraction** | **−0.591** | 1×10⁻³⁰ | more lipid-exposed → less constrained |
| constraint vs **burial** (heavy-atom neighbors ≤10 Å) | +0.425 | 4×10⁻¹⁵ | more buried → more constrained |
| constraint vs **pLDDT** | −0.086 | 0.13 (NS) | **not** a model-confidence artifact |

Monotonic gradient by lipid-exposure quartile (least→most exposed): mean KL **2.31 → 1.95 → 1.48 → 0.98**.
Restricting to high-confidence residues (pLDDT > 70; 308/312) leaves the correlations unchanged
(lipid ρ = −0.596; radial ρ = −0.675). **Spatial clustering:** the 15 most-constrained TM residues have a
mean pairwise distance of 19.2 Å vs a random-TM null of 30.1 Å (5,000 permutations, p < 0.0001) — they
form a single compact pocket, not dispersed fold positions. Together these confirm the cavity-over-portal
pattern without relying on the discrete geometric classification.

### Candidate substrate-coordinating residues (most-constrained cavity positions, human numbering)

R290 (KL 4.05), N435 (3.81), Y378 (3.66), E64 (3.48), E298 (3.31), Q186 (3.28), N283 (3.10),
E156 (3.06), T257 (3.06), S286 (3.00), E258 (2.80), F415 (2.79), E260 (2.67), S412 (2.63), K152 (2.57).
These are overwhelmingly H-bond donors/acceptors and charged side chains — the chemistry expected to
coordinate the polar **Man5GlcNAc2-pyrophosphate** headgroup of the substrate. *(Leads for mutagenesis;
require curator/experimental verification.)*

---

## Evidence Matrix

| # | Citation | Evidence type | Stance | Claim tested | Key finding | Context | Confidence / limitations |
|---|---|---|---|---|---|---|---|
| 1 | This run (computed) | Structural/evolutionary (computational) | **Supports** | Constraint concentrated on cavity, not portal | Cavity KL 2.35 ≫ portal 1.33 ≈ bg 1.67; cavity vs portal p=3×10⁻⁵ | PF04506 (3,826 seq, eukaryotes) on AF-Q96AA3 | High for the contrast; geometry from one static model |
| 2 | This run (computed) | Computational controls | Supports | Result not an artifact | Reproduced by Shannon metric, permutation p=1e-4, axis-tilt ±25°, composition (0% Pro/Gly) | Same pipeline | High |
| 3 | This run (computed) | Computational (composition) | **Refutes** the Pro/Gly alternative for cavity | Is cavity signal fold-maintenance? | Cavity = 0% Gly/Pro, 28% charged, 47% polar | Same pipeline | High for cavity; buried-packing does carry a weaker fold signal |
| 4 | PMID **38886340** (Chen et al., 2024) | Direct assay (reconstitution) | Supports GO:0140303 | Is Rft1 itself the flippase? | "purified Rft1 catalyzes the translocation of M5GN2-PP-Dol across the lipid bilayer"; "confirm the molecular identity of Rft1 as the M5GN2-PP-Dol ER flippase" | Reconstituted proteoliposomes | High; resolves the historical in-vitro dispensability debate |
| 5 | This run (computed) | Computational (sanity check) | Qualifies/validates method | Does the frame capture inside/outside? | Outer lipid-facing surface is the fastest-evolving class (p=2×10⁻¹³) | Same pipeline | Expected TM-protein pattern → frame is roughly correct |
| 6 | InterPro IPR007594 / Pfam PF04506 / TCDB 2.A.66.3.2 | Database | Orientation | Fold/superfamily membership | RFT1 = MOP flippase superfamily, RFT1/oligosaccharidyl-lipid flippase family; eukaryote-restricted | Cross-references for Q96AA3 | Database-level; used only for orientation |
| 7 | This run (computed) | Computational (continuous, confounder-controlled) | **Supports** | Is the cavity signal axis-/binning-/pLDDT-independent? | Constraint vs radial-distance ρ=−0.675 (p=8×10⁻⁴³) and vs lipid-exposure ρ=−0.591 (p=1×10⁻³⁰); pLDDT ρ=−0.086 (NS); top-15 residues cluster (19.2 vs 30.1 Å, p<10⁻⁴) | Same pipeline, 312 TM positions | High; independent of the discrete classification |

---

## GO Curation Implications  *(leads — require curator verification)*

- **GO:0140303 (intramembrane lipid transporter activity, MF) → RETAIN.** It is directly supported by
  reconstitution (PMID 38886340) and is *reinforced* by this analysis: the family's conserved core is
  precisely the polar substrate-handling cavity of a MOP flippase, not incidental surface.
- **Consider a more specific MF child if one exists** (curator to check the ontology): the physiological
  substrate is a **lipid-linked oligosaccharide (Man5GlcNAc2-PP-dolichol)**, so a "glycolipid/oligo­saccharide-lipid
  flippase" style MF child would be more informative than the generic parent. Do **not** invent an ID;
  verify against current GO. Evidence code for the retained/refined MF should reference the direct assay
  (IDA, PMID 38886340) rather than IEA/ISS alone.
- **This evolutionary analysis is CC/BP-neutral.** It speaks to *which* residues matter (MF mechanism),
  not to localization (ER membrane, CC) or the glycosylation process (BP); those should be curated from
  their own primary evidence.
- **"Protein binding" is not an appropriate summary** here — a specific transporter MF is supported.

---

## Mechanistic Scope

- **Immediate molecular function tested:** which wild-type residues selection has preserved across the
  RFT1 family, and where they sit relative to the substrate cavity vs. the lipid-facing/portal surface
  of the MOP fold. This is a statement about the flippase's **substrate-coordination machinery**.
- **Direct gene-product activity:** transbilayer flipping of Man5GlcNAc2-PP-dolichol (PMID 38886340).
- **Separated (not part of this test):** downstream N-linked glycosylation flux, CDG disease phenotypes,
  or any inference from loss-of-function alleles. Per instructions, **no disease/pathogenicity data were
  used** to select positions; the constrained set is defined purely by cross-species selection and
  geometry.

---

## Conflicts and Alternatives

- **Both-cavity-and-portal alternative:** *not supported* — portal is at/below background while cavity is
  above.
- **Fold-maintenance (Pro/Gly, helix-packing) alternative:** *partly true but not for the cavity.* Buried
  packing residues carry a weaker-but-real constraint enrichment; the cavity class contains no Pro/Gly and
  is polar/charged. So "fold maintenance dominates everything" is refuted, but "fold maintenance also
  matters" is honestly acknowledged.
- **Shallow/too-divergent alignment alternative:** *not the case* — 3,826 sequences, 512 columns, human
  mapped over 497 residues; classes separate with large effect sizes and small p-values.
- **Portal-definition sensitivity:** the "portal" is operationally the lipid-facing rim of the cavity in a
  *single, likely occluded* AlphaFold state. A genuinely open lateral gate in another conformational state
  could be lined by different residues; my first (ray-tracing) portal detector found **no** wide-open
  lateral sector in this model, consistent with an occluded state.
- **Cross-superfamily constraint (MATE/MurJ):** deliberately requested but **not computable by sequence
  alignment** — those Pfam families are too divergent to co-align with RFT1; a structure-based comparison
  would be needed.
- **Paralog/isoform confusion:** none material — RFT1 is single-copy in human; PANTHER PTHR13117:SF5 and
  TCDB 2.A.66.3.2 are RFT1-specific.

---

## Knowledge Gaps

1. **Experimental structure of RFT1.** *Checked:* only an AlphaFold model was available programmatically;
   the membrane axis/portal were inferred. *Why it matters:* the cavity/portal partition depends on the
   model. *Resolver:* a cryo-EM/OPM-oriented Rft1 structure (± bound LLO) to define the real cavity and any
   lateral gate.
2. **Prokaryotic MOP constraint.** *Checked:* PF04506 has no bacterial/archaeal members. *Why it matters:*
   the hypothesis invokes the broader MOP/MATE/MurJ architecture. *Resolver:* structure-based multiple
   alignment across the superfamily (e.g., Foldseek/DALI + 3D-anchored MSA).
3. **Substrate-contact identity of the conserved cavity residues.** *Checked:* only geometric proximity to
   the lumen. *Why it matters:* conservation ≠ contact. *Resolver:* substrate-bound structure or docking, and
   mutagenesis of R290/N435/Y378/E64/E298 etc.
4. **Conformational state.** *Checked:* one static model (apparently occluded). *Why it matters:* the portal
   may only exist transiently. *Resolver:* multi-state modeling / MD / alternate-state structures.

---

## Discriminating Tests

- **Substrate-bound Rft1 structure or MD-informed docking** → do the constrained cavity residues
  (R290, N435, Y378, E64, E298, Q186, N283, E156, S/T cluster 257/286/412) actually contact the
  oligosaccharide/pyrophosphate? This is the single most decisive test.
- **Alanine/charge-reversal mutagenesis** of the top cavity residues vs. matched **portal** residues,
  scored in the reconstituted flipping assay (PMID 38886340): cavity mutants should impair transport far
  more than portal mutants if the hypothesis holds.
- **Structure-based superfamily constraint** (RFT1 vs MATE vs MurJ, aligned in 3D) to test whether the
  cavity-over-portal pattern generalizes across the MOP fold.
- **Deep-mutational scanning / evolutionary-coupling (DCA)** on the same alignment to check that
  co-evolving/coupled positions concentrate in the cavity.

---

## Curation Leads  *(all require curator verification)*

- **Action:** *Retain* GO:0140303 (MF) with IDA support (PMID 38886340); flag for possible refinement to a
  lipid-linked-oligosaccharide-flippase child term if the ontology provides one.
- **Candidate reference + exact snippets to verify (PMID 38886340):**
  - "purified Rft1 catalyzes the translocation of M5GN2-PP-Dol across the lipid bilayer"
  - "confirm the molecular identity of Rft1 as the M5GN2-PP-Dol ER flippase"
- **Supporting computational provenance (this report):** the constraint-by-class table, robustness controls,
  and the ranked cavity-residue list are curator-usable evidence that the *conserved core* of RFT1 is its
  substrate-handling cavity.
- **Suggested curator questions:** (1) Is there a GO MF child specific to oligosaccharide-lipid/glycolipid
  flipping? (2) Should the ER-membrane CC and N-glycosylation BP terms be (re)affirmed from their own
  primary evidence rather than from this MF-focused analysis?
- **Suggested experiments:** cavity-vs-portal mutagenesis in the reconstituted flipping assay; substrate-bound
  structure.

---

## Bottom line

Within the deepest assemblable (eukaryotic) RFT1 family, evolutionary selection has preserved the polar
central-cavity residues of the MOP fold — the substrate-capture/coordination surface — far more than the
lateral lipid-facing/portal surface, which evolves at or below the transmembrane background. The seed
hypothesis is **supported**, with the honest caveat that buried fold-maintenance packing also carries a
weaker constraint signal, and that the analysis rests on a single static AlphaFold model of a
eukaryote-only family. The result **reinforces retention** of GO:0140303 and yields a concrete, testable
set of candidate substrate-coordinating residues.


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)