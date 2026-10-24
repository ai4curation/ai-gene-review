---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-21T02:50:11.806883'
end_time: '2026-09-21T03:24:06.739679'
duration_seconds: 2034.93
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: human
  gene: LPAR2
  gene_symbol: LPAR2
  uniprot_accession: Q9HBW0
  taxon_id: NCBITaxon:9606
  taxon_label: Homo sapiens
  focus_type: function_assignment
  hypothesis_slug: conditional-adenylate-cyclase-activation
  hypothesis_text: Assess GO:0007189 adenylate cyclase-activating GPCR signaling for
    human LPAR2 Q9HBW0 and LPAR3 Q9UBY5 separately. Actual PTHR22750 tree places both
    inside positive PTN002733616; LPAR2 has two repeated accession leaves PTN009051918/PTN002503555
    and LPAR3 PTN002503536, all descending from that node. Donor count, one predominant
    Gi pathway, or absence of a human-native assay does not establish function loss.
    Full primary10488122 Methods/Results/Fig7 (author-deposited ResearchGate text
    accessible) shows human EDG4 and EDG7 enhance forskolin-stimulated cAMP in Sf9
    cells, PTX insensitive; assay includes 5uM forskolin and 0.5mM IBMX, then LPA.
    LPA alone was ineffective. GO7189 does not explicitly require Gs or universal
    activation in every cellular context. Full primary10727522 (indexed publisher
    full text) contrasts this with mammalian Rh7777 cAMP and HEK293T Gi2alpha/GTPgammaS
    assays, and proposes conditional cyclase-II/PKC mechanisms as a possible explanation,
    not a refutation. Read the complete assays and controls, receptor constructs and
    their sequences, and later primary coupling studies. Bandoh cloned EDG4 from human
    brain cDNA, not explicitly the initial ovarian-tumor clone; nonetheless PMID10729222
    identifies a C-terminal frameshift in an early EDG4 sequence, and Im10727522 corrected
    their construct to genomic consensus. Determine which construct each assay used
    rather than assume every EDG4 result represents either that variant or the canonical
    protein. Compare direct LPAR2 Gi/cAMP inhibition in16203867 without treating inhibition
    in one context as universal exclusion of activation in another. Separate conditional
    functional capacity, assay-system artifact or altered construct, and physiological
    prevalence. Is activating pathway annotation supported, merely non-core, or unresolved?
    Do not silently generalize activating to modulating simply because its direction
    is conditional.
  term_context: No specific term context supplied.
  reference_context: No specific reference context supplied.
  source_file: genes/human/LPAR2/LPAR2-ai-review.yaml
  source_selector: free-text
  source_context_yaml: "hypothesis: Assess GO:0007189 adenylate cyclase-activating\
    \ GPCR signaling for human LPAR2 Q9HBW0 and LPAR3\n  Q9UBY5 separately. Actual\
    \ PTHR22750 tree places both inside positive PTN002733616; LPAR2 has two repeated\n\
    \  accession leaves PTN009051918/PTN002503555 and LPAR3 PTN002503536, all descending\
    \ from that node. Donor\n  count, one predominant Gi pathway, or absence of a\
    \ human-native assay does not establish function loss.\n  Full primary10488122\
    \ Methods/Results/Fig7 (author-deposited ResearchGate text accessible) shows human\n\
    \  EDG4 and EDG7 enhance forskolin-stimulated cAMP in Sf9 cells, PTX insensitive;\
    \ assay includes 5uM forskolin\n  and 0.5mM IBMX, then LPA. LPA alone was ineffective.\
    \ GO7189 does not explicitly require Gs or universal\n  activation in every cellular\
    \ context. Full primary10727522 (indexed publisher full text) contrasts this\n\
    \  with mammalian Rh7777 cAMP and HEK293T Gi2alpha/GTPgammaS assays, and proposes\
    \ conditional cyclase-II/PKC\n  mechanisms as a possible explanation, not a refutation.\
    \ Read the complete assays and controls, receptor\n  constructs and their sequences,\
    \ and later primary coupling studies. Bandoh cloned EDG4 from human brain\n  cDNA,\
    \ not explicitly the initial ovarian-tumor clone; nonetheless PMID10729222 identifies\
    \ a C-terminal\n  frameshift in an early EDG4 sequence, and Im10727522 corrected\
    \ their construct to genomic consensus.\n  Determine which construct each assay\
    \ used rather than assume every EDG4 result represents either that\n  variant\
    \ or the canonical protein. Compare direct LPAR2 Gi/cAMP inhibition in16203867\
    \ without treating\n  inhibition in one context as universal exclusion of activation\
    \ in another. Separate conditional functional\n  capacity, assay-system artifact\
    \ or altered construct, and physiological prevalence. Is activating pathway\n\
    \  annotation supported, merely non-core, or unresolved? Do not silently generalize\
    \ activating to modulating\n  simply because its direction is conditional.\nfocus_type:\
    \ function_assignment\ncontext: []\nreference_id: []"
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
- filename: provenance_LPAR2_GO0007189_evidence_matrix.csv
  path: openscientist_artifacts/provenance_LPAR2_GO0007189_evidence_matrix.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist LPAR2 GO0007189 evidence matrix
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
- **Gene directory:** LPAR2
- **Gene symbol:** LPAR2
- **UniProt accession:** Q9HBW0

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** conditional-adenylate-cyclase-activation
- **Source file:** genes/human/LPAR2/LPAR2-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

Assess GO:0007189 adenylate cyclase-activating GPCR signaling for human LPAR2 Q9HBW0 and LPAR3 Q9UBY5 separately. Actual PTHR22750 tree places both inside positive PTN002733616; LPAR2 has two repeated accession leaves PTN009051918/PTN002503555 and LPAR3 PTN002503536, all descending from that node. Donor count, one predominant Gi pathway, or absence of a human-native assay does not establish function loss. Full primary10488122 Methods/Results/Fig7 (author-deposited ResearchGate text accessible) shows human EDG4 and EDG7 enhance forskolin-stimulated cAMP in Sf9 cells, PTX insensitive; assay includes 5uM forskolin and 0.5mM IBMX, then LPA. LPA alone was ineffective. GO7189 does not explicitly require Gs or universal activation in every cellular context. Full primary10727522 (indexed publisher full text) contrasts this with mammalian Rh7777 cAMP and HEK293T Gi2alpha/GTPgammaS assays, and proposes conditional cyclase-II/PKC mechanisms as a possible explanation, not a refutation. Read the complete assays and controls, receptor constructs and their sequences, and later primary coupling studies. Bandoh cloned EDG4 from human brain cDNA, not explicitly the initial ovarian-tumor clone; nonetheless PMID10729222 identifies a C-terminal frameshift in an early EDG4 sequence, and Im10727522 corrected their construct to genomic consensus. Determine which construct each assay used rather than assume every EDG4 result represents either that variant or the canonical protein. Compare direct LPAR2 Gi/cAMP inhibition in16203867 without treating inhibition in one context as universal exclusion of activation in another. Separate conditional functional capacity, assay-system artifact or altered construct, and physiological prevalence. Is activating pathway annotation supported, merely non-core, or unresolved? Do not silently generalize activating to modulating simply because its direction is conditional.

## Term and Decision Context

No specific term context supplied.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: Assess GO:0007189 adenylate cyclase-activating GPCR signaling for human LPAR2 Q9HBW0 and LPAR3
  Q9UBY5 separately. Actual PTHR22750 tree places both inside positive PTN002733616; LPAR2 has two repeated
  accession leaves PTN009051918/PTN002503555 and LPAR3 PTN002503536, all descending from that node. Donor
  count, one predominant Gi pathway, or absence of a human-native assay does not establish function loss.
  Full primary10488122 Methods/Results/Fig7 (author-deposited ResearchGate text accessible) shows human
  EDG4 and EDG7 enhance forskolin-stimulated cAMP in Sf9 cells, PTX insensitive; assay includes 5uM forskolin
  and 0.5mM IBMX, then LPA. LPA alone was ineffective. GO7189 does not explicitly require Gs or universal
  activation in every cellular context. Full primary10727522 (indexed publisher full text) contrasts this
  with mammalian Rh7777 cAMP and HEK293T Gi2alpha/GTPgammaS assays, and proposes conditional cyclase-II/PKC
  mechanisms as a possible explanation, not a refutation. Read the complete assays and controls, receptor
  constructs and their sequences, and later primary coupling studies. Bandoh cloned EDG4 from human brain
  cDNA, not explicitly the initial ovarian-tumor clone; nonetheless PMID10729222 identifies a C-terminal
  frameshift in an early EDG4 sequence, and Im10727522 corrected their construct to genomic consensus.
  Determine which construct each assay used rather than assume every EDG4 result represents either that
  variant or the canonical protein. Compare direct LPAR2 Gi/cAMP inhibition in16203867 without treating
  inhibition in one context as universal exclusion of activation in another. Separate conditional functional
  capacity, assay-system artifact or altered construct, and physiological prevalence. Is activating pathway
  annotation supported, merely non-core, or unresolved? Do not silently generalize activating to modulating
  simply because its direction is conditional.
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

# LPAR2 (Q9HBW0) — GO:0007189 "adenylate cyclase-activating GPCR signaling pathway": Focused Curation Review

**Focus type:** function_assignment · **Hypothesis slug:** conditional-adenylate-cyclase-activation
**Gene:** LPAR2 (human), UniProt Q9HBW0 · **Paralog cross-checked:** LPAR3 / Q9UBY5 (EDG7)
**Iteration:** 3 (final) · **Date:** 2026-09-21

---

## Executive Judgment

**Verdict: Weakly / partially supported — the activating annotation is a phylogenetic over-propagation (from melanocortin receptors) whose only direct experimental anchor for LPAR2 is a conditional, heterologous in-vitro effect; it should be treated as non-core (context-qualified), not as a primary human function. Native mammalian physiology points the opposite direction (cAMP-lowering / Gi, plus Gq and G12/13).**

Three lines of evidence, weighed together:

1. **The current annotation's basis is melanocortin receptors, not LPA data (decisive, new in Iteration 2).** QuickGO shows the single GO:0007189 annotation on Q9HBW0 is `IBA` (GO_REF:0000033, PANTHER node **PTN002733616**). Its experimental `withFrom` source set resolves to **MC1R, MC2R, MC3R, MC4R, MC5R** (all Gs-coupled, cAMP-*activating* melanocortin receptors) **plus GPR3** (a constitutively Gs-active orphan). **No LPA receptor is among the sources.** LPAR2 simply co-resides with melanocortins in PANTHER family **PTHR22750** (the functionally heterogeneous "MECA" δ-branch: Melanocortin/EDG-LPA-S1P/Cannabinoid/Adenosine). This is a textbook paralog over-annotation: a Gs/cAMP-up function experimentally proven in melanocortin receptors is inherited by LPA receptors whose real coupling is different.

2. **The only direct LPAR2 pro-cAMP datum is conditional and heterologous.** Bandoh et al. 1999 (PMID 10488122): in EDG4/LPAR2-expressing **Sf9 insect cells**, LPA **enhanced forskolin-stimulated cAMP**, absent in EDG2/LPAR1, and **PTX-insensitive**; **LPA alone was ineffective** (required 5 µM forskolin + 0.5 mM IBMX priming). This is real direct evidence but reflects **potentiation of an already-activated cyclase** — consistent with a conditional Gq/PKC → adenylyl-cyclase-type-II mechanism (the "cyclase-II/PKC" idea raised for the paralog by Im 2000, PMID 10727522) — not canonical Gs activation. Bandoh's own abstract frames LPA action as *"modulation of adenylyl cyclase."*

3. **Native mammalian evidence shows Gi-mediated cAMP LOWERING and Gq/G12 (strengthened in Iteration 3).** The seed-cited **PMID 16203867** (Li 2005, J Exp Med) — retrieved via Europe PMC — states directly that apical intestinal **"LPA inhibited CFTR-dependent iodide efflux through LPA2-mediated Gi pathway,"** reducing cholera-toxin-induced secretion. Concordantly, disrupting LPA2–NHERF2 *raises* cAMP near CFTR (i.e., intact LPA2 lowers it; PMID 21299497); LPA **inhibits** forskolin-stimulated HCO₃⁻ secretion NHERF2-dependently (PMID 19221439); LPA2 couples to **Gαq** (NHERF-2) and **Gα12** (MAGI-3) in colon cancer (PMID 21134377) and to **Gi** (PTX-sensitive) in dendritic cells (PMID 16769764). None report Gs/cAMP activation.

4. **Both paralogs share the identical melanocortin-derived IBA (Iteration 3).** QuickGO confirms **LPAR3 (Q9UBY5)** carries GO:0007189 with the *same* IBA code, *same* GO_REF:0000033, *same* PANTHER node PTN002733616, and the *same* `withFrom` set (MC1R–MC5R + GPR3) as LPAR2 — i.e., uniform family-level propagation, not paralog-specific experimental support, exactly as the seed's tree analysis implied.

**Answer to the seed's explicit question ("supported, merely non-core, or unresolved?"): the activating annotation is real as a conditional in-vitro capacity but non-core; as currently coded (IBA from melanocortin receptors) it is over-propagated.** Do not silently rename "activating" to "modulating" — but do (a) re-ground it on the Bandoh IDA with a context qualifier, and (b) add the missing inhibitory (Gi) annotation so the record reflects dominant physiology. The direction is conditional, but the *basis* of the present annotation is a paralog artifact.

---

## Evidence Matrix

| Citation | Evidence type | Stance | Claim tested | Key finding | Context | Confidence / limitations |
|---|---|---|---|---|---|---|
| **PMID 10488122** (Bandoh 1999) | Direct assay (heterologous) | **Supports (conditional)** | LPAR2 activates adenylate cyclase | LPA raised **forskolin-stimulated cAMP** in EDG4/EDG7-Sf9 (not EDG2); **PTX-insensitive**; LPA alone ineffective | Sf9 insect cells, +5 µM forskolin/0.5 mM IBMX | Moderate; heterologous, forskolin-primed → potentiation, not canonical Gs |
| **QuickGO/UniProt Q9HBW0 IBA** (GO_REF:0000033, PTN002733616) | Structural/evolutionary (annotation provenance) | **Qualifies/Competing (over-propagation)** | Basis of the GO:0007189 IBA on LPAR2 | IBA `withFrom` = **MC1R/MC2R/MC3R/MC4R/MC5R + GPR3** (Gs cAMP-activating); **no LPA receptor** among sources; **LPAR3/Q9UBY5 shares identical IBA/withFrom** | PANTHER PTHR22750 (MECA family); queried 2026-09-21 | High; direct DB read — annotation inherited from melanocortins |
| **PMID 16203867** (Li 2005, J Exp Med) | Direct assay + mouse phenotype (native intestine) | **Competing (Gi / AC-inhibition)** | LPAR2 cAMP-relevant coupling natively | **"LPA inhibited CFTR-dependent iodide efflux through LPA2-mediated Gi pathway"**; reduced CTX-induced fluid secretion; LPA2-peptide reversible | Human/mouse intestinal epithelium, apical CFTR complex | High; direct native Gi (cAMP-lowering) coupling, opposite to GO:0007189 |
| **PMID 21299497** (Zhang 2011) | Perturbation (native epithelia) | Competing (cAMP-lowering) | LPAR2 raises vs lowers cAMP | Disrupting LPA2–NHERF2 **elevates cAMP** near CFTR → intact LPA2 **lowers** cAMP | Human airway epithelia | Moderate-high; opposite direction to GO:0007189 |
| **PMID 19221439** (Singh 2009) | Mutant phenotype (mouse) | Competing (Gi-type) | LPAR2 inhibits cAMP-dependent secretion | LPA **inhibited** forskolin-stimulated HCO₃⁻ secretion; lost in Nherf2⁻/⁻; "NHERF2 confers inhibitory signals" | Mouse duodenum in vivo | Moderate-high; native cAMP-lowering role |
| **PMID 21134377** (Lee 2011) | Interaction (native) | Competing (Gq/G12) | LPAR2 G-protein coupling | LPA2 couples to **Gαq** (NHERF-2) and **Gα12** (MAGI-3); no Gs | Human colon cancer (HCT116/SW480) | Moderate-high; Gq/G12 core |
| **PMID 10727522** (Im 2000) | Direct assay (mammalian) | Qualifies (paralog LPAR3) | LPAR3 cAMP/G coupling | EDG7-RH7777 show **no inhibition** of forskolin cAMP; HEK293T+Gi2α → GTPγS (Gi, EC₅₀ 195 nM) | RH7777, HEK293T | High for LPAR3; not a LPAR2 test |
| **PMID 10729222** (Contos & Chun 2000) | Sequence/genomic | Qualifies (construct) | Early EDG4 construct integrity | Ovarian-tumor EDG4 cDNA has a **G-deletion frameshift** near 3′ end → altered C-terminus | Human/mouse genomic vs cDNA | High; outcomes construct-dependent |
| **PMID 16769764** (Oz-Arslan 2006) | Native-cell pharmacology | Competing (Gi) | Native LPAR2 coupling | PTX + PKC/Rho inhibitors block LPL-induced ERK/cytokines in LPA2⁺ DCs | Human dendritic cells | Moderate; Gi/Gq/Rho dominance |
| **PMID 16504475** (Kim 2006) | Genetic/pharmacology | Competing (Gq) | LPA2 couples to Gq | Gq-inhibitor peptide attenuates LPA proliferation/ERK/Akt in LPA1/LPA2 VSMC | Mouse/rat VSMC | Moderate |
| **PMID 16904289** (Zhang 2007) | Interaction | Competing (G12/13-Rho) | LPA2 C-terminal PDZ routing | LPA2 C-terminus binds MAGI-3/NHERF2/PDZ-RhoGEF; regulates ERK/RhoA | SW480 colon cancer | Moderate |

*Provenance artifact:* `provenance/LPAR2_GO0007189_evidence_matrix.csv` (machine-readable). UniProt GO/sequence and QuickGO annotation provenance pulled programmatically via UniProt REST + EBI QuickGO REST (code executed in-session).

---

## GO Curation Implications

- **Term class:** GO:0007189 is a **Biological Process (BP)** term.
- **Lead (requires curator verification):** **Do not keep GO:0007189 as an unqualified IBA.** Two coherent options:
  1. **Re-ground and qualify:** replace the melanocortin-derived IBA with an **experimental annotation from PMID 10488122** (IDA in a heterologous system), explicitly qualified as a **forskolin-dependent, PTX-insensitive potentiation** (i.e., conditional/non-core). This preserves the genuine capacity without implying canonical Gs coupling.
  2. **Down-weight/flag as over-propagated:** because the IBA `withFrom` set is entirely melanocortin/GPR3 (Gs) receptors with **no LPA-receptor source**, a curator could reasonably treat the IBA as a phylogenetic artifact of the MECA family and remove or NOT-qualify it, retaining only the qualified experimental annotation.
- **Complementary term to ADD:** **GO:0007193** ("adenylate cyclase-*inhibiting* GPCR signaling pathway") is currently **absent** from Q9HBW0 despite strong native-tissue support (PMID 21299497, 19221439, 16769764). Adding it would make the record reflect dominant LPAR2 physiology.
- **Well-supported existing MF/CC terms to retain:** GO:0070915 (LPA receptor activity), GO:0004930 (GPCR activity), GO:0030165 (PDZ domain binding), GO:0007204 (positive regulation of cytosolic Ca²⁺).
- **Avoid** collapsing to generic "protein binding."
- **Paralog note (LPAR3/Q9UBY5):** evaluate separately; its GO:0007189 rests on the *same* Sf9 experiment (PMID 10488122) and the *same* melanocortin-derived MECA IBA, and Im 2000 found no cAMP inhibition + clear Gi coupling — so the identical non-core qualifier applies.

---

## Mechanistic Scope

- **Immediate molecular function tested:** receptor-mediated *increase* in intracellular cAMP (positive coupling to adenylyl cyclase) after LPA binds LPAR2.
- **Direct gene-product activity:** the only positive datum (Bandoh Sf9) is **PTX-insensitive and forskolin-dependent** → indirect **potentiation** of already-active cyclase (plausibly Gq→PKC→AC type II), not autonomous Gs activation.
- **Native direction is inhibitory:** in epithelia LPAR2 *lowers* compartmentalized cAMP (Gi-type; PMID 21299497, 19221439) and drives Gq/G12-13 pathways (PMID 21134377, 16904289).
- **Separated from this MF:** Ca²⁺ mobilization (Gq), ERK/MAPK, RhoA-dependent migration/invasion, anti-apoptotic TRIP6/NHERF2 complexes (PMID 19293149), CFTR/NHE3 transport regulation, and tumor phenotypes are pathway/phenotypic consequences — not the AC-activation MF and must not be conflated with it.

---

## Conflicts and Alternatives

1. **Annotation provenance = paralog artifact (primary conflict):** the IBA is inherited from melanocortin receptors/GPR3 (Gs), not from LPA data — the strongest argument that the "activating" call is over-propagated.
2. **Direction conflict:** native LPAR2 *lowers* cAMP (Gi) and uses Gq/G12; the *activation* signal appears only under forskolin priming in Sf9.
3. **Species/system artifact:** Sf9 insect cells have a distinct G-protein/effector milieu; PTX-insensitive cAMP potentiation there may not recapitulate human native coupling.
4. **Construct provenance (PMID 10729222):** an early ovarian-tumor EDG4 clone had a C-terminal frameshift; the canonical Q9HBW0 C-terminus (`…DSTL`, intact PDZ motif) is the corrected genomic consensus. Which ORF Bandoh used (human brain cDNA) is not stated in the abstract and should be confirmed in the full text.

---

## Knowledge Gaps

| Gap | What was checked | Why it matters | What would resolve it |
|---|---|---|---|
| Exact EDG4 construct in Bandoh Sf9 assay | Abstracts PMID 10488122 & 10729222 (full texts not machine-accessible) | If the frameshifted C-terminal variant was used, the cAMP result may not represent canonical LPAR2 | Read Methods/sequence in PMID 10488122 full text; align ORF to Q9HBW0 |
| Gs vs Gq/PKC→AC-II mechanism | Bandoh abstract (PTX-insensitive, forskolin-dependent) | Determines whether GO:0007189 (Gs-type) is the correct term vs a modulation/inhibition term | Cholera-toxin/Gs-minus + PKC-inhibitor + AC-isoform reconstitution assays |
| Human-native cAMP *increase* | Native studies show cAMP *decrease*/Gi/Gq (PMID 21299497, 19221439, 21134377) | No human-native assay shows LPAR2 *activating* cAMP | cAMP biosensor in human cells, LPAR2 knock-in, ± PTX ± Gq inhibitor |
| GO:0007193 absent | UniProt/QuickGO Q9HBW0 | Record over-represents "activation," omits dominant inhibition | Curate Gi/AC-inhibition annotation from PMID 21299497/19221439 |
| PMID 16203867 — *resolved in Iteration 3* | Retrieved via Europe PMC; confirms LPA2-mediated **Gi** inhibition of CFTR (cAMP-lowering) in native intestine | Confirms dominant Gi/AC-inhibiting physiology; supports adding GO:0007193 and treating GO:0007189 as non-core | Already resolved; curator may verify full-text figures for magnitude/EC50 |

---

## Discriminating Tests

1. **Isoform-defined cAMP biosensor** in a human line expressing canonical Q9HBW0 (`…DSTL`), ± PTX, ± Gq inhibitor (YM-254890/FR900359), ± PKC inhibitor, ± forskolin — cleanly separates Gs activation vs Gq/PKC→AC-II potentiation vs Gi inhibition.
2. **Construct-controlled comparison:** canonical vs frameshifted C-terminal EDG4 side-by-side in Sf9 and mammalian cells.
3. **Gα knockout / minigene + BRET** G-protein dissociation panels to read which Gα LPAR2 engages natively.
4. **AC-isoform reconstitution** (AC-II vs AC-V/VI) to test the conditional cyclase-II hypothesis.
5. **Re-audit the PANTHER PTHR22750 node PTN002733616** to confirm the IBA propagates from melanocortin/GPR3 leaves — a curator-actionable check against family-level over-annotation.

---

## Curation Leads (require curator verification)

- **Action:** Reclassify GO:0007189 on Q9HBW0 as **non-core / context-qualified** and **re-ground it on experimental evidence (PMID 10488122)** rather than the melanocortin-derived IBA; optionally down-weight/flag the IBA as MECA-family over-propagation. **Add GO:0007193** to represent dominant cAMP-lowering physiology.
- **Candidate reference + exact snippets to verify:**
  - PMID 10488122: *"In EDG7- or EDG4-expressing Sf9 cells, LPA stimulated forskolin-induced increase in intracellular cAMP levels, which was not observed in EDG2-expressing cells."* / *"Neither the EDG7- nor EDG4-transduced Ca(2+) response or cAMP accumulation was inhibited by pertussis toxin."*
  - PMID 21299497 (for GO:0007193 lead): *"it elevates cAMP levels in proximity to CFTR and upregulates its channel activity"* (upon disrupting LPA2–NHERF2 → intact LPA2 lowers cAMP).
  - PMID 19221439: *"NHERF2 confers inhibitory signals by coupling the LPA receptor to CFTR."*
  - PMID 21134377: *"MAGI-3 increased the interaction of LPA(2) with Gα(12), whereas NHERF-2 preferentially promoted interaction between LPA(2) and Gα(q)."*
  - PMID 16203867 (for GO:0007193 lead): *"LPA inhibited CFTR-dependent iodide efflux through LPA2-mediated Gi pathway."*
- **Candidate qualifier note:** activation effect is heterologous (Sf9), forskolin-dependent, PTX-insensitive → conditional Gq/PKC→AC-II potentiation, not canonical Gs.
- **Suggested curator questions:** (1) Which EDG4 ORF did Bandoh use (canonical vs frameshift)? (2) Should the IBA GO:0007189 be dropped/qualified given its `withFrom` is entirely melanocortin/GPR3? (3) Should GO:0007193 be added? (4) Retrieve PMID 16203867 full text.
- **Suggested experiments:** the isoform-defined cAMP biosensor discriminating assay and PANTHER node audit above.

---

## Limitations

- Full texts of PMID 10488122 / 10727522 / 16203867 were not machine-accessible in this run; claims rely on complete abstracts plus the seed's Methods excerpt. All quoted snippets are verbatim from retrieved abstracts and should be re-verified against full text.
- Analysis is literature- and database-driven; no wet-lab validation. UniProt/QuickGO reads and the `withFrom` identity resolution are direct programmatic results; the Gq/PKC→AC-II mechanistic attribution is inference, clearly labeled as such.


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)
- [OpenScientist LPAR2 GO0007189 evidence matrix](openscientist_artifacts/provenance_LPAR2_GO0007189_evidence_matrix.csv)