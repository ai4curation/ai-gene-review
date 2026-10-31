---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-04T18:37:47.900888'
end_time: '2026-10-04T19:01:17.775924'
duration_seconds: 1409.88
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: worm
  gene: gei-17
  gene_symbol: gei-17
  uniprot_accession: Q94361
  taxon_id: NCBITaxon:6239
  taxon_label: Caenorhabditis elegans
  focus_type: function_assignment
  hypothesis_slug: gei17-sap-sim-coregulator
  hypothesis_text: 'C. elegans GEI-17 (UniProt Q94361) retains the PIAS N-terminal
    SAP domain and SUMO-interacting motifs (SIMs) that mediate ligase-independent
    transcriptional co-repressor activity in human PIAS1, and so could act as a transcription
    regulator inhibitor independently of its SP-RING ligase. Test this with one decisive
    sequence analysis: align GEI-17 to human PIAS1 (O75925), PIAS4 and Drosophila
    Su(var)2-10, and assess conservation of the SAP domain (including its DNA-binding
    LXXLL/helix residues) and the SIM motifs.'
  term_context: '- Term: transcription regulator inhibitor activity (GO:0140416)'
  reference_context: No specific reference context supplied.
  source_file: genes/worm/gei-17/gei-17-ai-review.yaml
  source_selector: free-text
  source_context_yaml: "hypothesis: 'C. elegans GEI-17 (UniProt Q94361) retains the\
    \ PIAS N-terminal SAP domain and SUMO-interacting\n  motifs (SIMs) that mediate\
    \ ligase-independent transcriptional co-repressor activity in human PIAS1,\n \
    \ and so could act as a transcription regulator inhibitor independently of its\
    \ SP-RING ligase. Test this\n  with one decisive sequence analysis: align GEI-17\
    \ to human PIAS1 (O75925), PIAS4 and Drosophila Su(var)2-10,\n  and assess conservation\
    \ of the SAP domain (including its DNA-binding LXXLL/helix residues) and the SIM\n\
    \  motifs.'\nfocus_type: function_assignment\nterm_id: GO:0140416\nterm_label:\
    \ transcription regulator inhibitor activity\ncontext: []\nreference_id: []"
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
- **Gene directory:** gei-17
- **Gene symbol:** gei-17
- **UniProt accession:** Q94361

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** gei17-sap-sim-coregulator
- **Source file:** genes/worm/gei-17/gei-17-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

C. elegans GEI-17 (UniProt Q94361) retains the PIAS N-terminal SAP domain and SUMO-interacting motifs (SIMs) that mediate ligase-independent transcriptional co-repressor activity in human PIAS1, and so could act as a transcription regulator inhibitor independently of its SP-RING ligase. Test this with one decisive sequence analysis: align GEI-17 to human PIAS1 (O75925), PIAS4 and Drosophila Su(var)2-10, and assess conservation of the SAP domain (including its DNA-binding LXXLL/helix residues) and the SIM motifs.

## Term and Decision Context

- Term: transcription regulator inhibitor activity (GO:0140416)

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: 'C. elegans GEI-17 (UniProt Q94361) retains the PIAS N-terminal SAP domain and SUMO-interacting
  motifs (SIMs) that mediate ligase-independent transcriptional co-repressor activity in human PIAS1,
  and so could act as a transcription regulator inhibitor independently of its SP-RING ligase. Test this
  with one decisive sequence analysis: align GEI-17 to human PIAS1 (O75925), PIAS4 and Drosophila Su(var)2-10,
  and assess conservation of the SAP domain (including its DNA-binding LXXLL/helix residues) and the SIM
  motifs.'
focus_type: function_assignment
term_id: GO:0140416
term_label: transcription regulator inhibitor activity
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

# AIGR Gene Hypothesis Deep Research — GEI-17 (Q94361): SAP/SIM-Mediated Ligase-Independent Transcription-Inhibitor Activity

**Target:** *Caenorhabditis elegans* GEI-17 (UniProt Q94361) · **Term under evaluation:** transcription regulator inhibitor activity (GO:0140416) · **Focus:** function_assignment · **Hypothesis slug:** gei17-sap-sim-coregulator

---

## Executive Judgment

**Verdict: REFUTED as a molecular-function mechanism / OVER-ANNOTATED as a GO MF term — despite a partially correct structural premise.**

The seed hypothesis makes a three-part claim: (1) GEI-17 retains the PIAS N-terminal **SAP domain**; (2) it retains **SUMO-interacting motifs (SIMs)**; and (3) these modules together confer a **ligase-independent transcriptional co-repressor / transcription-regulator-inhibitor activity** (GO:0140416) analogous to human PIAS1, operating **independently of the SP-RING SUMO ligase**. Our investigation finds that the structural premise is partly salvageable but the functional conclusion does not hold, for three convergent reasons:

1. **The SAP premise is sequence-undetectable but structurally plausible.** No sequence-profile method (Pfam PF02037, PROSITE PS50800, CATH-Gene3D, SUPERFAMILY) calls a SAP domain in GEI-17, whereas all three reference orthologs (human PIAS1, PIAS4, Drosophila Su(var)2-10) are annotated by multiple independent methods. However, AlphaFold shows GEI-17 retains a confidently folded, helix-hairpin-helix N-terminal module that superposes onto the PIAS1 SAP core at **1.55 Å Cα-RMSD**. So a cryptic, highly diverged SAP-like fold is present — but the **DNA-binding helix-2 and the LXXLL motif invoked by the hypothesis are degenerate** (GEI-17 "LQSII" vs PIAS1 "LQVLL").

2. **The SAP domain is the wrong module even in human PIAS1.** Decisively, the ligase-independent transcription-inhibitor activity of human PIAS1 does **not** map to the SAP domain. A SAP-domain mutant and a catalytically dead (ligase-dead) PIAS1 **both retain** IRF3 inhibition, which instead maps to a **C-terminal acidic region** (PMID:24036127). The original human PIAS1 GO:0140416 basis (PMID:9724754) is **STAT1 sequestration** — a protein-protein mechanism, not SAP–DNA co-repression. So even if GEI-17's SAP-like fold were intact, SAP conservation would not establish GO:0140416.

3. **GEI-17's only documented worm transcription-repressive role is ligase-DEPENDENT.** GEI-17 does inhibit transcription in *C. elegans* — specifically piRNA transcription (PMID:40316696) — but this operates through its **SUMO E3 ligase (SP-RING) activity** and SUMOylation-driven condensate regulation, **directly contradicting** the hypothesis's "independent of its SP-RING ligase" claim.

**Bottom line for the curator:** GEI-17's GO:0140416 annotation is **IBA-only** (phylogenetic propagation from the PIAS/PANTHER node), with **no experimental *C. elegans* support**. The gene product's primary, experimentally-grounded molecular function is **SUMO E3 ligase activity (GO:0061665)**. Any transcriptional repression GEI-17 mediates is best captured as a **downstream biological process** (e.g., negative regulation of transcription, GO:0045892) executed *via* its catalytic ligase activity — **not** as a direct, ligase-independent transcription-regulator-inhibitor molecular function. The most important caveat is that the structural SAP-like fold is genuinely present (so a curator should not claim "SAP is absent"); the point is that its presence does not license the MF term.

---

## Key Findings

### Finding 1 — GEI-17 lacks a sequence-detectable SAP domain, unlike all three reference orthologs

InterPro integrated annotation calls the SAP domain (IPR003034) in human PIAS1 (O75925, residues 11–45), PIAS4 (Q8N2W9, 12–46) and Drosophila Su(var)2-10 (Q7KNF5, 2–36) by **multiple independent methods** — Pfam PF02037, PROSITE PS50800, CATH-Gene3D G3DSA:1.10.720.30, and SUPERFAMILY SSF68906. For GEI-17 (Q94361), **none** of these methods call a SAP domain; only the PINIT domain (residues 203–367) and the SP-RING/MIZ zinc-finger (400–485) are detected. GEI-17 carries a long, largely disordered N-terminal extension — PINIT begins at residue ~203 versus ~119–124 in the orthologs.

Direct Smith–Waterman alignment (BLOSUM62) of the PIAS1 SAP core (residues 6–46) against each N-terminus quantifies the divergence: PIAS1-vs-PIAS4 scores 133 (63% identity); PIAS1-vs-Su(var)2-10 scores 61 (41% identity); PIAS1-vs-GEI-17 scores only 36 over a 27-aa window (37% identity). A shuffle null model (n=300 shuffles) gives GEI-17 an observed **z = 3.93, p ≈ 0.003** — a statistically detectable but weak remnant, confined to **SAP helix-1** (GEI-17 "VMKLRVHDLQSII" vs PIAS1 "VMSLRVSELQVLL"). Critically, the **DNA-binding second helix** ("RNKHGRKHELLTKALHLLK" in PIAS1) and the **LXXLL motif** are **not** conserved (GEI-17 "LQSII" vs PIAS1 "LQVLL"). This is the first and most direct refutation of the hypothesis's sequence premise: the specific DNA-contacting residues that the seed invokes are gone.

### Finding 2 — GO:0140416 is IBA-only in GEI-17; the human basis is STAT1 sequestration, not SAP co-repression

QuickGO shows GEI-17 (Q94361) carries GO:0140416 (transcription regulator inhibitor activity) **solely with evidence code IBA** (GO_REF:0000033; phylogenetic propagation from the PANTHER PIAS-family node PTN000845825, family PTHR10782). There is **no experimental (IDA/IMP/IPI)** *C. elegans* annotation for this term. The human PIAS1 GO:0140416 annotation rests on an IDA from Liu et al. 1998 ([PMID:9724754](https://pubmed.ncbi.nlm.nih.gov/9724754/)): *"PIAS1, but not other PIAS proteins, blocked the DNA binding activity of Stat1 and inhibited Stat1-mediated gene activation in response to interferon."* This is a **protein-sequestration mechanism** dependent on the PIAS1–STAT1 interaction — **not** on SAP–DNA binding or the LXXLL motif invoked by the seed. Moreover, *C. elegans* lacks a canonical interferon/JAK–STAT1 axis, so the specific documented mechanism underlying the human annotation does not transfer to the worm. The IBA propagation therefore carries a function whose experimental anchor is both mechanistically and organismally mismatched to GEI-17.

### Finding 3 — GEI-17's SIMs are experimentally characterized for SUMO-scaffolding, not transcriptional repression

Pelisch et al. 2017 ([PMID:27939944](https://pubmed.ncbi.nlm.nih.gov/27939944/)) show experimentally that *"GEI-17 and another RC component, the kinase BUB-1, contain functional SUMO interaction motifs (SIMs), allowing them to recruit SUMO modified proteins, including KLP-19, into the RC [meiotic ring complex]."* Our motif scan of GEI-17 recovers acidic-flanked hydrophobic SIM-like cores (e.g., residues 472–475 and regions near 545–548 and 597–600 within C-terminal acidic/disordered stretches), consistent with SIM presence. **So the second structural premise of the hypothesis — that GEI-17 has SIMs — is correct.** However, these SIMs function in a **SUMO–SIM scaffolding network for chromosome congression during oocyte meiosis**, operating *downstream of* GEI-17's SUMO E3 ligase activity — not in transcriptional co-repression. All experimentally characterized GEI-17 roles (meiotic ring-complex assembly, PMID:27939944; mitotic chromosome assembly / cell-cycle progression, [PMID:25475837](https://pubmed.ncbi.nlm.nih.gov/25475837/)) are SUMO-ligase-dependent. The SIMs are real but repurposed for a catalytic/scaffolding pathway, not for the ligase-independent repression the seed proposes.

### Finding 4 — AlphaFold rescues the SAP-fold premise (1.55 Å RMSD) even though sequence profiles miss it

AlphaFold models show the PIAS SAP region is confidently folded in all orthologs (PIAS1 res 11–45 mean pLDDT 93.7; PIAS4 12–46, 93.5; Su(var)2-10 2–36, 89.0). GEI-17 (Q94361) likewise has a confidently folded N-terminal module at res ~21–80 (mean pLDDT ~86–89; 100% of res 21–60 above pLDDT 70), flanked by a long disordered linker (res 81–200, mean pLDDT ~36) before PINIT (203+). CA(i,i+4) helix mapping shows GEI-17 res 20–85 forms helical runs [7,11,8,10] and PIAS1 res 6–50 forms [4,11,12] — both consistent with a SAP **helix-hairpin-helix** core. Kabsch superposition of the sequence-aligned Cα atoms (PIAS1 SAP residues 11–36 ↔ GEI-17 27–47, 26 residue pairs) gives **Cα-RMSD = 1.55 Å**.

This is the key nuance for the curator: GEI-17 **retains a structurally SAP-like folded module** even though Pfam/PROSITE/CATH/SUPERFAMILY do not classify it as SAP, because the sequence has diverged beyond profile-detection limits. The structural premise of the hypothesis is therefore **partly vindicated** — but with the same retained caveat: the DNA-binding helix-2 and the LXXLL motif are not conserved. A fold without its functional residues does not recover the function.

### Finding 5 — Human PIAS ligase-independent transcription inhibition is SAP-INDEPENDENT, undercutting the seed's core mechanism

This is the decisive functional finding. Li et al. 2013 ([PMID:24036127](https://pubmed.ncbi.nlm.nih.gov/24036127/)) dissected exactly the ligase-independent transcription-inhibitor activity the seed invokes and found it is **neither ligase-dependent nor SAP-dependent**:

- **Ligase-independent:** *"SUMO E3 ligase activity dead mutant PIAS1/C350S still had the comparable inhibitory function with WT PIAS1."*
- **SAP-independent:** *"PIAS1 with a mutation in the SAP domain retained the inhibitory function in virus-induced IFN transcription."*
- **The responsible module is elsewhere:** *"The C-terminal region of PIAS1 around a cluster of acidic amino acids is critical for the interaction with IRF3 and the inhibitory functions of PIAS1."*

Consistent with this, Tolkunova et al. 2007 ([PMID:17991485](https://pubmed.ncbi.nlm.nih.gov/17991485/)) showed PIASy inhibits Oct4-mediated transcription by sequestering Oct4 to the nuclear periphery, and *"These modes of PIASy action are uncoupled from its sumoylation activity."* In other words, even where PIAS proteins do exhibit genuine ligase-independent transcriptional inhibition, the mechanism is **transcription-factor protein-protein sequestration via C-terminal/acidic regions**, not SAP-domain DNA binding or the LXXLL motif. The seed hypothesis's specific causal claim — that the SAP domain confers the activity — is directly contradicted in the very paralog it uses as its model.

### Finding 6 — GEI-17 does inhibit transcription in *C. elegans*, but via ligase-DEPENDENT condensate regulation

Zhu et al. 2025 ([PMID:40316696](https://pubmed.ncbi.nlm.nih.gov/40316696/)) provide the direct worm evidence that GEI-17 represses transcription — and show it is ligase-dependent. A screen for regulators of piRNA transcription *"isolated the SUMO E3 ligase GEI-17 as inhibiting and the SUMO protease TOFU-3 as promoting piRNA transcription foci formation, thereby regulating piRNA production."* The effect operates through **SUMOylation/deSUMOylation of the USTC transcription complex and phase-separation of transcriptional condensates** — i.e., GEI-17's SUMO E3 ligase (SP-RING) activity produces the transcription-inhibitory outcome (deSUMOylation by TOFU-3 *promotes* foci; SUMOylation by GEI-17 opposes them). This is the opposite of the hypothesis's "independent of its SP-RING ligase" claim. Reinforcing a ligase-dependent, transcription-factor-SUMOylation mode, Fergin et al. 2022 ([PMID:35666766](https://pubmed.ncbi.nlm.nih.gov/35666766/)) show GEI-17-dependent *"sumoylation of the ETS transcription factor LIN-1 at K169 is necessary for the proper contraction of the ventral vulA toroids"* during vulval development — GEI-17 acting on a transcription factor by catalytic SUMOylation, not by ligase-independent co-repression.

---

## Mechanistic Model / Interpretation

The investigation can be summarized as a decision tree in which the hypothesis is tested at three independent gates, failing the functional gates even where it passes a structural one:

```
SEED HYPOTHESIS: GEI-17 SAP + SIMs → ligase-INDEPENDENT
                 transcription-regulator-inhibitor activity (GO:0140416)
          │
   ┌──────┴───────────────────────────────────────────────┐
   │ GATE 1: Does GEI-17 retain the SAP domain?            │
   ├───────────────────────────────────────────────────────┤
   │ Sequence profiles (Pfam/PROSITE/CATH/SUPERFAMILY): NO │  F001
   │ AlphaFold fold superposition (1.55 Å RMSD):   PARTIAL │  F004
   │ DNA-binding helix-2 + LXXLL residues:              NO │  F001/F004
   │ → Fold cryptically present; functional residues GONE  │
   └──────┬────────────────────────────────────────────────┘
          │ (even granting the fold…)
   ┌──────┴────────────────────────────────────────────────┐
   │ GATE 2: Does the SAP domain confer the activity        │
   │         in the model paralog (human PIAS1)?           │
   ├────────────────────────────────────────────────────────┤
   │ PIAS1 ΔSAP mutant RETAINS IRF3 inhibition:          NO │  F005
   │ PIAS1 ligase-dead (C350S) RETAINS inhibition:       NO │  F005
   │ Activity maps to C-TERMINAL ACIDIC region:    (not SAP)│  F005
   │ Original GO basis = STAT1 SEQUESTRATION:      (not SAP)│  F002
   │ → SAP is the WRONG module; mechanism is TF seq.       │
   └──────┬─────────────────────────────────────────────────┘
          │ (so is GEI-17's worm repression ligase-independent?)
   ┌──────┴─────────────────────────────────────────────────┐
   │ GATE 3: In C. elegans, is GEI-17 repression            │
   │         independent of its SP-RING ligase?           │
   ├─────────────────────────────────────────────────────────┤
   │ piRNA transcription repression = SUMO-ligase DEPENDENT │  F006
   │ LIN-1 regulation = catalytic SUMOylation (K169):  DEP. │  F006
   │ SIMs = SUMO scaffolding of meiotic RC (ligase pathway) │  F003
   │ → Repression is a DOWNSTREAM BP of catalytic activity  │
   └─────────────────────────────────────────────────────────┘

CONCLUSION: GO:0140416 (MF) NOT supported for GEI-17.
Primary MF = SUMO E3 ligase (GO:0061665).
Transcription repression = downstream BP (e.g., GO:0045892),
                           executed VIA ligase activity.
```

The coherent narrative: GEI-17 is, first and foremost, the *C. elegans* PIAS-family **SUMO E3 ligase**. Its experimentally documented biology — meiotic ring-complex assembly, mitotic chromosome assembly, telomere anchoring, vulval LIN-1 regulation, and piRNA condensate control — is uniformly **ligase-dependent**. The seed hypothesis attempts to graft onto GEI-17 a *ligase-independent* co-repressor function borrowed from human PIAS1, routed through the SAP domain and LXXLL motif. But that route is a misreading of the human data: even in PIAS1 the ligase-independent transcription-inhibitor activity is SAP- and ligase-independent, mapping to a C-terminal acidic TF-sequestration module. GEI-17 retains a cryptic SAP-like *fold* but not its DNA-binding residues, and its worm repression runs entirely through catalysis. The GO:0140416 annotation is thus an IBA artifact of phylogenetic propagation from a family node whose experimental anchor (human STAT1/IRF3 inhibition) neither depends on the conserved module nor exists in the worm's signaling repertoire.

---

## Evidence Matrix

| Citation (PMID) | Evidence type | Supports / Refutes / Qualifies | Claim tested | Key finding | Context | Confidence & limitations |
|---|---|---|---|---|---|---|
| InterPro / Pfam / PROSITE / CATH / SUPERFAMILY | Structural/evolutionary; computational | **Refutes** sequence premise | Does GEI-17 retain a SAP domain by profile methods? | No SAP (IPR003034) called in GEI-17 by any method; called in all 3 orthologs by ≥4 methods. SW remnant weak (z=3.93, p≈0.003), helix-1 only; helix-2 + LXXLL not conserved | Protein sequence; cross-ortholog | High for "profiles miss it"; cannot exclude cryptic fold (see AlphaFold) |
| AlphaFold models | Structural/evolutionary; computational | **Qualifies** (partially supports structural premise) | Does GEI-17 retain a SAP-like 3D fold? | GEI-17 N-terminal module folds (pLDDT ~86–89); superposes on PIAS1 SAP at **1.55 Å Cα-RMSD** over 26 residues | Predicted structure | Moderate–high; predictions not experimental; DNA-binding residues still degenerate |
| [9724754](https://pubmed.ncbi.nlm.nih.gov/9724754/) | Direct assay (IDA) | **Qualifies/Refutes** mechanism | Experimental basis of human PIAS1 GO:0140416? | PIAS1 blocks STAT1 DNA binding and IFN-induced gene activation — **sequestration**, not SAP co-repression | Human cells, IFN signaling | High; mechanism is TF sequestration, and worm lacks JAK–STAT1 axis |
| [24036127](https://pubmed.ncbi.nlm.nih.gov/24036127/) | Direct assay (mutant mapping) | **Refutes** seed's core mechanism | Does SAP/ligase confer PIAS1 transcription inhibition? | ΔSAP mutant AND ligase-dead C350S **both retain** IRF3 inhibition; activity maps to **C-terminal acidic region** | Human cells, virus-induced IFN | High; decisive against SAP-mediated model |
| [17991485](https://pubmed.ncbi.nlm.nih.gov/17991485/) | Direct assay | **Refutes** SAP mechanism (supports alt) | Is PIAS ligase-independent repression SAP-mediated? | PIASy represses Oct4 by nuclear-periphery sequestration; *"uncoupled from its sumoylation activity"* | Human/mouse pluripotency | High; independent paralog, same conclusion (TF sequestration) |
| [27939944](https://pubmed.ncbi.nlm.nih.gov/27939944/) | Direct assay / interaction | **Qualifies** (SIMs real; wrong function) | Does GEI-17 have functional SIMs, and for what? | GEI-17 SIMs recruit SUMO-modified KLP-19 into the meiotic ring complex | *C. elegans* oocyte meiosis | High; SIMs confirmed but function is SUMO scaffolding, ligase-dependent |
| [40316696](https://pubmed.ncbi.nlm.nih.gov/40316696/) | Mutant phenotype / screen | **Refutes** "ligase-independent"; supports BP | Does GEI-17 repress worm transcription, and how? | GEI-17 inhibits piRNA transcription foci via SUMOylation of USTC / condensate control (ligase-dependent) | *C. elegans* germline, piRNA | High; direct worm transcription evidence, but ligase-DEPENDENT |
| [35666766](https://pubmed.ncbi.nlm.nih.gov/35666766/) | Mutant phenotype | **Supports** catalytic model | Does GEI-17 act on TFs by SUMOylation? | GEI-17-dependent SUMOylation of ETS TF LIN-1 at K169 required for vulA toroid contraction | *C. elegans* vulval development | High; catalytic (ligase-dependent) TF regulation |
| [25475837](https://pubmed.ncbi.nlm.nih.gov/25475837/) | Mutant phenotype | **Supports** primary function | What is GEI-17's core cellular role? | PIAS(GEI-17) SUMO E3 ligase required for mitotic chromosome alignment / cell-cycle progression | *C. elegans* embryo | High; reinforces SUMO-ligase as primary function |

---

## GO Curation Implications

**Lead for curator verification — likely action: do NOT retain GO:0140416 as a direct molecular-function annotation for GEI-17; treat as non-core / downstream.**

- **GO:0140416 (transcription regulator inhibitor activity, MF):** The evidence does **not** support this as a direct molecular function of GEI-17. It is **IBA-only**, propagated from the PIAS/PANTHER family node, whose experimental anchor (human PIAS1 STAT1/IRF3 inhibition) (i) is mechanistically a TF-sequestration activity mapping to a C-terminal acidic region rather than the conserved SAP domain, and (ii) does not depend on the module the seed invokes. Recommended action: **remove or demote** this MF annotation for GEI-17, or at minimum flag it as an uninformative IBA carry-over not supported by the worm's experimental record. If retained for phylogenetic-consistency reasons, it should carry a NOT/under-review qualifier pending experimental validation.

- **Primary molecular function — GO:0061665 (SUMO ligase activity) / SUMO transferase:** This is the experimentally supported MF and should be the anchor annotation (PMID:25475837; PMID:27939944; PMID:35666766; PMID:40316696 all rely on GEI-17 catalytic activity).

- **Biological process — GO:0045892 (negative regulation of DNA-templated transcription) or a piRNA-transcription-specific child:** GEI-17's documented transcription-repressive effect on piRNA genes (PMID:40316696) is real and supportable as a **BP**, but it is executed *via* SUMO ligase activity and condensate regulation — a downstream process, **not** a direct MF. A curator could add a BP term with IMP evidence from PMID:40316696, explicitly noting ligase dependence.

- **Avoid "protein binding" as a terminal recommendation:** The more informative supported terms are SUMO ligase activity (MF) and negative regulation of transcription (BP, ligase-dependent); these should be used rather than the uninformative generic binding term.

---

## Mechanistic Scope

**Immediate molecular activity being tested:** a *ligase-independent* transcription-regulator-inhibitor (co-repressor) activity attributed to the SAP domain + SIMs. **This direct activity is not supported.** What is directly supported is **SUMO E3 ligase (transferase) activity** (SP-RING/MIZ domain, res 400–485), aided by PINIT (203–367) substrate positioning and C-terminal SIMs for SUMO-chain/scaffold engagement.

**Separation of direct activity from downstream effects:**
- *Direct gene-product activity:* catalytic SUMO conjugation onto substrate lysines (e.g., LIN-1 K169); SIM-mediated recruitment of SUMO-modified partners (KLP-19) into higher-order assemblies.
- *Pathway/cellular consequence:* SUMOylation of the USTC transcription complex modulates phase-separated transcriptional condensates, thereby repressing piRNA transcription — a **downstream BP**, not a direct MF of binding/inhibiting the transcription machinery.
- *Developmental/phenotypic outcome:* meiotic chromosome congression, mitotic chromosome assembly, telomere anchoring, vulval toroid contraction — pleiotropic phenotypes of the catalytic ligase, not evidence for a distinct co-repressor MF.
- *Inferred-from-loss-of-function:* the piRNA screen phenotype (PMID:40316696) demonstrates repression but attributes it to ligase activity; no loss-of-function data isolate a ligase-independent SAP-driven repression.

---

## Conflicts and Alternatives

1. **Paralog over-generalization / frequency bias.** The hypothesis extrapolates from "human PIAS1 has GO:0140416" to "GEI-17 has it," but the human activity (a) does not require the SAP domain (PMID:24036127) and (b) originally rests on STAT1 sequestration (PMID:9724754), an axis absent in *C. elegans*. This is a classic IBA over-annotation pattern.

2. **Fold vs. function mismatch.** AlphaFold shows a conserved SAP-*like* fold (1.55 Å RMSD), which could tempt a curator toward the MF. But the DNA-binding helix-2 and LXXLL residues are degenerate, and the fold is not the functional determinant even in PIAS1. Structural conservation here is a red herring for GO:0140416.

3. **SIMs real but repurposed.** The hypothesis correctly predicts SIMs (PMID:27939944), but their documented role is SUMO-scaffolding of the meiotic ring complex — a ligase-pathway function — not transcriptional co-repression. Correct prediction, wrong functional attribution.

4. **Organism-specific mechanism.** *C. elegans* GEI-17 transcription repression (piRNA; PMID:40316696) is ligase-dependent, directly contradicting the seed's "independent of its SP-RING ligase." The worm mechanism is catalytic SUMOylation + condensate control, not DNA-binding co-repression.

5. **Alternative interpretation favored by the data:** GO:0140416's phenotypic signal in GEI-17 is fully explained as a **downstream consequence of SUMO ligase activity**, requiring no separate co-repressor MF.

---

## Limitations and Knowledge Gaps

| Gap | What was checked | Why it matters for curation | What would resolve it |
|---|---|---|---|
| No experimental test of a GEI-17 ligase-dead mutant for transcription repression | Literature + QuickGO; found only ligase-dependent assays | Directly adjudicates the seed's "ligase-independent" claim in the native organism | A GEI-17 SP-RING catalytic-dead (e.g., analogous to PIAS1 C350S) rescue in the piRNA / LIN-1 assays |
| AlphaFold fold not experimentally confirmed, and no DNA-binding assay for GEI-17 N-terminus | AlphaFold superposition (1.55 Å) + motif scan | Determines whether the cryptic SAP-like fold has any residual DNA-binding/chromatin activity | EMSA / chromatin-binding assay of the GEI-17 N-terminal module; cryo-EM/X-ray if feasible |
| SIM functional repertoire beyond meiosis untested for transcription | Motif scan + PMID:27939944 | Whether SIMs contribute to any repression independent of catalysis | SIM-point-mutant GEI-17 in transcription assays with ligase intact vs. dead |
| Whether GEI-17 physically contacts worm transcription factors independent of SUMOylation | Literature only | A C-terminal-acidic-style sequestration (as in PIAS1/PIASy) could exist in worm | Co-IP / proximity labeling of GEI-17 with germline TFs ± SUMOylation-site mutations |
| Exact boundaries/identity of GEI-17 "acidic" C-terminal region vs. PIAS1's IRF3-binding module | Partial (SIM scan found acidic/disordered C-terminal regions) | PIAS1's activity maps here; a worm homolog region could in principle sequester a TF | Deletion mapping of GEI-17 C-terminus in a repression assay |

---

## Discriminating Tests

1. **Ligase-dead rescue in the native assay (highest value).** Express catalytically dead GEI-17 (SP-RING Cys mutant) in a *gei-17* loss-of-function background and test rescue of piRNA transcription repression (PMID:40316696 assay) and LIN-1-dependent vulval phenotypes (PMID:35666766). If repression requires catalysis, the ligase-independent hypothesis is refuted *in vivo*; if a dead mutant still represses, the hypothesis gains support.

2. **SAP-module deletion/point mutants.** Delete the AlphaFold-defined N-terminal SAP-like module (res ~21–80) or mutate its residual helix-1 residues; test for any loss of transcription repression separable from catalysis. Parallels the decisive PIAS1 ΔSAP experiment (PMID:24036127).

3. **DNA/chromatin-binding assay of the isolated N-terminal module.** EMSA or chromatin pulldown to test whether the cryptic SAP-like fold binds DNA at all, given helix-2/LXXLL degeneracy.

4. **C-terminal acidic-region mapping.** By analogy to PIAS1's IRF3-binding region, test whether a GEI-17 C-terminal fragment sequesters any germline transcription factor independent of SUMOylation.

5. **Comparative orthology refinement.** Formal structure-guided alignment (e.g., Foldseek/DALI) of GEI-17 vs. PIAS1/PIAS4/Su(var)2-10 SAP folds to quantify which functional SAP residues are retained vs. lost — strengthens the "fold-present, function-absent" curation note.

---

## Curation Leads (require curator verification)

**Candidate action change:**
- **Remove / demote GO:0140416 (transcription regulator inhibitor activity, MF)** as a direct annotation for GEI-17; it is IBA-only with no worm experimental support and rests on a human mechanism (SAP- and ligase-independent TF sequestration) that neither transfers to the worm nor depends on the conserved module.
- **Retain/strengthen GO:0061665 (SUMO ligase activity, MF)** as the primary molecular function.
- **Consider adding GO:0045892 (negative regulation of DNA-templated transcription, BP)** with IMP evidence from PMID:40316696, annotated as ligase-dependent (downstream of catalytic activity).

**Candidate references with exact snippets to verify:**
- [PMID:24036127](https://pubmed.ncbi.nlm.nih.gov/24036127/): *"PIAS1 with a mutation in the SAP domain retained the inhibitory function in virus-induced IFN transcription"* and *"SUMO E3 ligase activity dead mutant PIAS1/C350S still had the comparable inhibitory function with WT PIAS1."* → SAP- and ligase-independence of the human activity.
- [PMID:9724754](https://pubmed.ncbi.nlm.nih.gov/9724754/): *"PIAS1, but not other PIAS proteins, blocked the DNA binding activity of Stat1 and inhibited Stat1-mediated gene activation in response to interferon."* → Human GO:0140416 basis is STAT1 sequestration.
- [PMID:40316696](https://pubmed.ncbi.nlm.nih.gov/40316696/): *"isolated the SUMO E3 ligase GEI-17 as inhibiting ... piRNA transcription foci formation."* → Worm repression is ligase-dependent.
- [PMID:27939944](https://pubmed.ncbi.nlm.nih.gov/27939944/): *"GEI-17 ... contain functional SUMO interaction motifs (SIMs), allowing them to recruit SUMO modified proteins ... into the RC."* → SIMs real, function is SUMO scaffolding.
- [PMID:35666766](https://pubmed.ncbi.nlm.nih.gov/35666766/): *"sumoylation of the ETS transcription factor LIN-1 at K169 is necessary for the proper contraction of the ventral vulA toroids."* → Catalytic TF regulation.

**Suggested curator questions:**
- Is the GEI-17 GO:0140416 IBA propagation appropriate given the family node's experimental anchor is SAP- and ligase-independent and organism-mismatched?
- Should the worm piRNA repression phenotype be annotated as a BP with explicit ligase dependence rather than inherited as an MF?

**Suggested experiments:** ligase-dead rescue (test #1 above) and SAP-module mutant (test #2) are the two most decisive and should be flagged as the experiments that would settle the annotation.

---

## Evidence Base Summary

The strongest primary-literature pillars, in order of decisiveness for this hypothesis:

1. **[PMID:24036127](https://pubmed.ncbi.nlm.nih.gov/24036127/)** (Li et al. 2013) — *decisive refutation of the SAP mechanism*: human PIAS1 ΔSAP and ligase-dead mutants both retain transcription inhibition; activity maps to the C-terminal acidic region.
2. **[PMID:40316696](https://pubmed.ncbi.nlm.nih.gov/40316696/)** (Zhu et al. 2025) — *decisive worm evidence against ligase-independence*: GEI-17 represses piRNA transcription via SUMO ligase activity and condensate regulation.
3. **[PMID:9724754](https://pubmed.ncbi.nlm.nih.gov/9724754/)** (Liu et al. 1998) — the human GO:0140416 IDA basis is STAT1 sequestration, not SAP co-repression.
4. **[PMID:17991485](https://pubmed.ncbi.nlm.nih.gov/17991485/)** (Tolkunova et al. 2007) — independent paralog confirms ligase-independent PIAS repression works by TF sequestration.
5. **[PMID:27939944](https://pubmed.ncbi.nlm.nih.gov/27939944/)** (Pelisch et al. 2017) — GEI-17 SIMs are real but function in SUMO scaffolding of the meiotic ring complex.
6. **[PMID:35666766](https://pubmed.ncbi.nlm.nih.gov/35666766/)** (Fergin et al. 2022) & **[PMID:25475837](https://pubmed.ncbi.nlm.nih.gov/25475837/)** — reinforce that GEI-17's TF/chromosome roles are catalytic SUMO-ligase functions.

Database/computational evidence (InterPro profile methods; AlphaFold superposition) establishes the "fold present, functional residues absent" structural picture: GEI-17 escapes SAP profile detection yet retains a 1.55 Å-RMSD SAP-like fold with a degenerate DNA-binding helix-2/LXXLL motif.

---

## Conclusion

The seed hypothesis is **refuted as a molecular-function mechanism and over-annotated as GO:0140416**, with a partially correct structural premise that must be stated carefully. GEI-17 does retain a cryptic, structurally SAP-like fold and genuine SIMs — but its DNA-binding residues are degenerate, the SAP domain is not the module that confers transcription-inhibitor activity even in human PIAS1, and GEI-17's only documented worm transcription-repressive role is SUMO-ligase-dependent. The curator should treat GO:0140416 as an unsupported IBA carry-over, anchor GEI-17's annotation on SUMO E3 ligase activity (GO:0061665), and, if desired, capture its transcription repression as a downstream, ligase-dependent biological process.


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)