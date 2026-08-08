---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-12T12:05:26.496137'
end_time: '2026-07-12T12:23:54.981591'
duration_seconds: 1108.49
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: DICDI
  gene: iplA
  gene_symbol: iplA
  uniprot_accession: Q9NA13
  taxon_id: NCBITaxon:44689
  taxon_label: Dictyostelium discoideum
  focus_type: function_assignment
  hypothesis_slug: ipla-ip3-gated-channel
  hypothesis_text: IplA is an inositol 1,4,5-trisphosphate (IP3)-gated intracellular
    calcium-release channel
  term_context: No specific term context supplied.
  reference_context: No specific reference context supplied.
  source_file: ''
  source_selector: ''
  source_context_yaml: 'hypothesis: IplA is an inositol 1,4,5-trisphosphate (IP3)-gated
    intracellular calcium-release channel

    focus_type: function_assignment

    context: []

    reference_id: []'
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
citation_count: 8
artifact_count: 4
artifact_sources:
  openscientist_artifacts_zip: 4
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
- filename: ipla_evidence_matrix.csv
  path: openscientist_artifacts/ipla_evidence_matrix.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist ipla evidence matrix
- filename: ipla_go_decision_table.csv
  path: openscientist_artifacts/ipla_go_decision_table.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist ipla go decision table
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
- **Gene directory:** iplA
- **Gene symbol:** iplA
- **UniProt accession:** Q9NA13

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** ipla-ip3-gated-channel
- **Source file:** 
- **Source selector:** 

## Seed Hypothesis

IplA is an inositol 1,4,5-trisphosphate (IP3)-gated intracellular calcium-release channel

## Term and Decision Context

No specific term context supplied.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: IplA is an inositol 1,4,5-trisphosphate (IP3)-gated intracellular calcium-release channel
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

# AIGR Gene Hypothesis Deep Research — IplA (Q9NA13, *Dictyostelium discoideum*)

## Hypothesis under review

> **IplA is an inositol 1,4,5-trisphosphate (IP3)-gated intracellular calcium-release channel**
> (focus type: *function_assignment*; slug: `ipla-ip3-gated-channel`)

---

## Executive Judgment

**Verdict: PARTIALLY SUPPORTED — with the specific "IP3-gated" molecular function classified as INFERENCE-ONLY / OVER-ANNOTATED relative to direct evidence.**

The hypothesis splits cleanly into two claims that carry very different levels of support:

1. **"IplA is an intracellular calcium-release channel of the IP3R/RyR superfamily."** This is **well supported**. IplA (Q9NA13) is a 3,177-residue protein that is the single-copy structural ortholog of the inositol-1,4,5-trisphosphate receptor / ryanodine receptor (IP3R/RyR) channel superfamily in *Dictyostelium*. It carries the diagnostic RIH domain, the armadillo-type "IP3 receptor binding core, domain 2" fold, and a 6-transmembrane pore-forming C-terminus. It is genetically required for agonist-evoked and Ca²⁺-gradient-evoked cytosolic Ca²⁺ signalling. A channel/transporter identity is justified.

2. **"…that is IP3-gated"** — i.e., that the protein directly binds IP3 and that IP3 binding opens its conductance. This is **NOT directly supported**. The GO terms encoding this claim (GO:0005220 IP3-gated calcium channel activity; GO:0070679 IP3 binding) exist in UniProt **only as electronic family inference (IEA:InterPro)**. No primary study has ever demonstrated IP3 binding by IplA or IP3-gated conductance. Computational mapping of the canonical IP3-coordinating residues onto IplA failed (0 of 9 residues confidently mapped; the metazoan MIR domain is absent). Multiple Ca²⁺-release pathways in *Dictyostelium* are demonstrably iplA-*independent*, and the primary literature consistently hedges — calling it a "putative" IP3 receptor and offering a competing interpretation of IplA as a Ca²⁺-**sensing** receptor rather than an IP3-**gated** effector.

**Bottom line for the curator:** Retain the IP3R-family channel *identity* and the genetically-supported role in intracellular Ca²⁺ release, but flag the *"IP3-gated"* molecular function as inferred/unverified. The most defensible molecular-function annotation is a generalized **calcium transmembrane transporter / channel** term rather than the specific **IP3-gated calcium channel activity** term, unless and until direct IP3-binding or IP3-gating data are produced. This is a lead requiring curator verification.

---

## Key Findings

### Finding 1 — IplA is the single-copy structural ortholog of the IP3R/RyR channel superfamily

IplA is annotated in UniProt (Q9NA13) as a 3,177-amino-acid "Inositol 1,4,5-trisphosphate receptor-like protein A," with the family-level SIMILARITY statement "Belongs to the InsP3 receptor family." Its domain architecture is unambiguously that of the IP3R/RyR intracellular Ca²⁺-release channel superfamily:

| Signature | Description |
|---|---|
| IPR000493 | InsP3 receptor (InsP3_rcpt) |
| IPR000699 / PF01365 | RIH domain (RyR and IP3R Homology) |
| IPR013662 / PF08454 | RIH-associated domain |
| IPR015925 | Ryanodine receptor / IP3 receptor |
| IPR035910 + SSF100909 | "IP3 receptor type 1 binding core, domain 2" (armadillo-type fold; 2 SUPFAM matches) |
| PF01365 (RYDR_ITPR ×2) | Ryanodine/IP3 receptor channel region |
| PANTHER PTHR13715:SF99 | IP3R/RyR family |
| PRINTS PR00779 | INSP3RECEPTR |

The topology matches the canonical channel fold: a large N-terminal cytoplasmic region (~residues 1–1175) followed by 6 transmembrane helices (~1176–3016) forming a pore-like C-terminus. Lam & Golstein (2008) describe iplA as "the only gene encoding an inositol 1,4,5-trisphosphate receptor (IP3R) in this organism" ([PMID: 18077554](https://pubmed.ncbi.nlm.nih.gov/18077554/)). *Dictyostelium* thus has a single-copy member of this family, which removes any concern about paralog confusion at the level of gene identity — there is exactly one IP3R-family gene, and IplA is it.

**This finding supports the channel/transporter half of the hypothesis.** The evolutionary and structural signal that IplA belongs to the IP3R/RyR fold is strong and internally consistent across InterPro, Pfam, SUPFAM, PANTHER, and PRINTS.

### Finding 2 — Genetic evidence links iplA to agonist-evoked Ca²⁺, but direct IP3-binding/gating has never been shown, and several Ca²⁺ pathways are iplA-independent

The genetic case for IplA in Ca²⁺ signalling is real but bounded:

- **Traynor et al. 2000** ([PMID: 10970875](https://pubmed.ncbi.nlm.nih.gov/10970875/)) disrupted iplA to make null cells "in which Ca²⁺ entry in response to chemoattractants is abolished." Importantly, resting cytosolic [Ca²⁺] was normal and chemotaxis to cAMP was unaffected — Ca²⁺ signalling was shown to be dispensable for cAMP chemotaxis.
- **Schaloske et al. 2005** ([PMID: 15760480](https://pubmed.ncbi.nlm.nih.gov/15760480/)) found that in iplA⁻ cells, **capacitative (store-operated) Ca²⁺ entry is fully operative**; cAMP still elicited extracellular Ca²⁺ influx and store liberation ("yet to a lesser extent"); agonist dose–responses were shifted ~100-fold in sensitivity; and ATP-induced Ca²⁺ uptake plus fatty-acid/Ca²⁺-ATPase-inhibitor-induced Ca²⁺ release from purified storage vesicles were similar to wild type.
- **Malchow et al. 2008** ([PMID: 17854889](https://pubmed.ncbi.nlm.nih.gov/17854889/)) reported that Ca²⁺-induced Ca²⁺ release (CICR) "was virtually unchanged in the iplA(-) strain that lacks a putative IP₃ or ryanodine receptor thought to be located at the endoplasmic reticulum."
- **Lam et al. 2008** ([PMID: 18077554](https://pubmed.ncbi.nlm.nih.gov/18077554/)) showed iplA is required to signal DIF-induced autophagic cell death.

Critically, the GO annotations that encode the *specific* mechanistic claim — **GO:0005220 (IP3-gated calcium channel activity)** and **GO:0070679 (IP3 binding)** — are present in UniProt **only as IEA:InterPro** (electronic family inference). There is no IDA (inferred from direct assay) supporting either. Consistently, the UniProt FUNCTION field is hedged: "*May* be a receptor for inositol 1,4,5-trisphosphate."

**This finding qualifies the hypothesis.** IplA is genetically necessary for a subset of Ca²⁺ responses, but "necessary for agonist-evoked Ca²⁺ entry" is not the same as "IP3-gated Ca²⁺-release channel." The observation that CICR and capacitative entry proceed normally without IplA shows that much of the cell's Ca²⁺-release machinery does not route through IplA.

### Finding 3 — The IP3R channel fold is present, but the specific IP3-coordinating residues cannot be confirmed and the MIR domain is absent

A direct interrogation of the sequence was performed (provenance file: `ipla_ip3_residue_alignment.txt`). The InterPro API returns 14 signatures for Q9NA13 confirming the channel/RIH binding-core fold, **but the MIR domain (PF02815 / IPR016093)** — a hallmark of the N-terminal IP3-binding/suppressor apparatus of metazoan IP3R and RyR — **is not matched**.

A custom Smith–Waterman alignment (BLOSUM62) of IplA residues 1–1300 against the human ITPR1 (P29994) N-terminus produced only one extendable local alignment, covering the suppressor-domain region (human ~81–246 vs IplA ~128–279) at just **28.7% identity**. Forcing an alignment across the IP3-binding core (human 224–604) yielded only a short 22-residue segment (45% over 22 aa) that did not extend. As a result, **0 of the 9 canonical IP3-coordinating residues** of human ITPR1 (R265, T266, R269, R504, K508, R511, Y567, R568, K569) could be confidently mapped onto IplA.

**This finding is the strongest computational argument against the specific "IP3-gated" molecular function.** The overall channel fold is conserved, but the ligand-recognition apparatus that *defines* IP3 gating in metazoans is not recognizably present. This is consistent with an ancient, divergent family member that retained the pore/channel architecture while its N-terminal ligand-sensing module diverged beyond recognition — leaving open whether IplA is gated by IP3 at all.

### Finding 4 — Primary literature consistently labels IplA "putative" and points to an alternative Ca²⁺-sensing role

A comprehensive NCBI eutils search of "iplA Dictyostelium" (15 records) found **no primary study demonstrating direct IP3 binding or IP3-gated conductance.** The recurring language and findings across the literature undercut a definitive IP3-gated assignment:

- **Lusche et al. 2012** ([PMID: 22375061](https://pubmed.ncbi.nlm.nih.gov/22375061/), *J Cell Sci*) call it "the putative IplA Ca²⁺ channel." iplA-null cells retain normal cAMP chemotaxis but lose chemotaxis in Ca²⁺ gradients, "suggesting that IplA is either the Ca²⁺ chemotaxis receptor or an essential component of the Ca²⁺ chemotaxis regulatory pathway." This proposes a **Ca²⁺-sensing receptor** role — mechanistically distinct from an IP3-gated Ca²⁺-release effector.
- **Ludlow et al. 2008** ([PMID: 18486207](https://pubmed.ncbi.nlm.nih.gov/18486207/), *Cell Calcium*): P2X/purinergic ATP/ADP-evoked Ca²⁺ influx is "not affected by deletion of either the single Gbeta or iplA genes" — another Ca²⁺ pathway that is iplA-independent.
- **Kim et al. 2025** ([PMID: 40295210](https://pubmed.ncbi.nlm.nih.gov/40295210/), *J Microbiol Biotechnol*): a significantly lower proportion of iplA-null cells respond to external Ca²⁺, and IplA "modulat[es] the timing and amplitude of calcium responses," with acidic stores partially contributing — again framing IplA as a *modulator/sensor* of Ca²⁺ responses.

**This finding reinforces the "inference-only" status of the IP3-gated claim** and identifies a credible competing hypothesis (Ca²⁺-sensing receptor) that the current evidence cannot exclude.

---

## Mechanistic Model / Interpretation

The evidence resolves into a two-layer model in which the *identity* claim is solid and the *gating mechanism* claim is unproven:

```
                    HYPOTHESIS: "IP3-gated intracellular Ca2+-release channel"
                    +----------------------------+-----------------------------+
                    |  LAYER 1: CHANNEL IDENTITY  |  LAYER 2: GATING MECHANISM   |
                    |        (SUPPORTED)          |     (INFERENCE-ONLY)         |
                    +----------------------------+-----------------------------+
 Sequence/domain    | RIH domain            [OK] | MIR domain ABSENT      [NO] |
                    | IP3R binding-core fold[OK] | 0/9 IP3-contact residues    |
                    | 6-TM pore             [OK] |   mappable             [NO] |
                    | single-copy IP3R ortholog  |                             |
                    +----------------------------+-----------------------------+
 Genetics           | iplA- abolishes agonist-   | Direct IP3 binding:         |
                    |  evoked Ca2+ entry    [OK] |   NEVER assayed        [NO] |
                    | required for DIF autophagic | IP3-gated conductance:      |
                    |  cell death           [OK] |   NEVER measured       [NO] |
                    +----------------------------+-----------------------------+
 Counter-evidence   |                            | CICR intact in iplA-        |
                    |                            | Capacitative entry intact   |
                    |                            | P2X purinergic influx intact|
                    |                            | Competing "Ca2+-sensor"model|
                    +----------------------------+-----------------------------+
                    GO:0005220 / GO:0070679 = IEA:InterPro ONLY (no IDA)
```

The most parsimonious reading is: **IplA is a genuine IP3R/RyR-fold intracellular Ca²⁺ channel that is genetically required for a specific branch of agonist-evoked Ca²⁺ signalling, but whether IP3 is its physiological gating ligand is untested and computationally doubtful.** The absence of the MIR domain and the non-mappability of IP3-contact residues suggest the ligand-sensing module has diverged substantially from the metazoan template. The "IP3-gated" label is a homology-based family inference propagated by InterPro, not a measured property of the *Dictyostelium* protein.

An important nuance from the pathway literature: *Dictyostelium* IP3/Ca²⁺ signalling **does** operate upstream of IplA in some contexts (e.g., polyphosphate → PLC → IP3 → cytosolic Ca²⁺ inhibits proliferation, and IplA is one of several components required — [PMID: 34154396](https://pubmed.ncbi.nlm.nih.gov/34154396/)). But "IplA acts in a pathway where IP3 is produced" is not evidence that "IplA is the IP3 receptor that IP3 gates." IplA could act downstream of, parallel to, or independent of the IP3 sensing step within these pathways.

---

## Evidence Base / Evidence Matrix

| Citation (PMID) | Evidence type | Supports / Refutes / Qualifies / Competing | Claim tested | Key finding | Context | Confidence & limitations |
|---|---|---|---|---|---|---|
| UniProt Q9NA13 + InterPro | Structural / evolutionary; database | Supports (identity); Qualifies (gating) | IplA belongs to IP3R/RyR channel family | RIH domain, IP3R binding-core fold, 6-TM pore; GO:0005220/GO:0070679 are IEA:InterPro only | Sequence/domain | High for family identity; the MF gating terms are electronic inference, not IDA |
| [PMID: 18077554](https://pubmed.ncbi.nlm.nih.gov/18077554/) (Lam & Golstein 2008) | Mutant phenotype; review-level statement | Supports (identity) | Single IP3R-family gene; role in cell death | "the only gene encoding an inositol 1,4,5-trisphosphate receptor (IP3R) in this organism"; iplA needed for DIF-induced autophagic cell death | *Dictyostelium* | High for single-copy identity; "IP3R" here is a family label, not a gating assay |
| [PMID: 10970875](https://pubmed.ncbi.nlm.nih.gov/10970875/) (Traynor et al. 2000) | Mutant phenotype | Supports (channel role); Qualifies (gating) | iplA required for agonist-evoked Ca²⁺ entry | iplA-null abolishes chemoattractant-evoked Ca²⁺ entry; resting [Ca²⁺] normal; chemotaxis unaffected | *Dictyostelium* aggregation | High for genetic requirement; does not test IP3 binding or gating |
| [PMID: 15760480](https://pubmed.ncbi.nlm.nih.gov/15760480/) (Schaloske et al. 2005) | Mutant phenotype | Qualifies / partly refutes | Which Ca²⁺ pathways need IplA | Capacitative entry fully operative in iplA⁻; store release still occurs; sensitivity shifted ~100× | *Dictyostelium* | High; shows multiple Ca²⁺ routes are IplA-independent |
| [PMID: 17854889](https://pubmed.ncbi.nlm.nih.gov/17854889/) (Malchow et al. 2008) | Mutant phenotype | Qualifies / refutes (for CICR) | Is CICR IplA-dependent? | CICR "virtually unchanged" in iplA⁻; calls IplA "putative IP3 or ryanodine receptor" | *Dictyostelium* | High; a major Ca²⁺-release mechanism does not require IplA |
| [PMID: 22375061](https://pubmed.ncbi.nlm.nih.gov/22375061/) (Lusche et al. 2012) | Mutant phenotype; competing model | Competing | Is IplA an IP3 effector or a Ca²⁺ sensor? | "putative IplA Ca²⁺ channel"; IplA "either the Ca²⁺ chemotaxis receptor or an essential component of the Ca²⁺ chemotaxis regulatory pathway" | *Dictyostelium* chemotaxis | High; explicitly offers a Ca²⁺-sensing alternative |
| [PMID: 18486207](https://pubmed.ncbi.nlm.nih.gov/18486207/) (Ludlow et al. 2008) | Mutant phenotype | Qualifies | Is purinergic Ca²⁺ influx IplA-dependent? | P2X ATP/ADP-evoked Ca²⁺ influx "not affected by deletion of… iplA" | *Dictyostelium* | High; another IplA-independent Ca²⁺ pathway |
| [PMID: 40295210](https://pubmed.ncbi.nlm.nih.gov/40295210/) (Kim et al. 2025) | Mutant phenotype | Qualifies / competing | IplA role in external-Ca²⁺ responses | Fewer iplA⁻ cells respond to external Ca²⁺; IplA "modulat[es] timing and amplitude"; acidic stores contribute | *Dictyostelium* | Moderate–high; frames IplA as modulator/sensor |
| [PMID: 34154396](https://pubmed.ncbi.nlm.nih.gov/34154396/) (autocrine feedback 2021) | Mutant phenotype; pathway | Qualifies | IplA in IP3/Ca²⁺ proliferation-inhibition pathway | iplA⁻ cells have reduced polyphosphate sensitivity; polyphosphate upregulates IP3 and cytosolic Ca²⁺ | *Dictyostelium* | Moderate; pathway context, not a direct gating assay |
| Custom Smith–Waterman alignment (this study; `ipla_ip3_residue_alignment.txt`) | Computational | Refutes (gating specificity) | Are IP3-contact residues conserved in IplA? | 0/9 canonical human ITPR1 IP3-coordinating residues mappable; MIR domain absent; best N-terminal identity 28.7% | In silico vs human ITPR1 P29994 | Moderate; local-alignment limitation, no experimental structure of IplA |

---

## GO Curation Implications

**Lead requiring curator verification.** The current UniProt annotations relevant to this hypothesis are:

| GO term | Aspect | Current evidence code | Recommended action (lead) |
|---|---|---|---|
| GO:0005220 — inositol 1,4,5-trisphosphate-gated calcium channel activity | MF | IEA:InterPro | **Do not promote to experimental.** Flag as inferred-only; consider **generalizing** to GO:0005262 (calcium channel activity) or GO:0015085 (calcium ion transmembrane transporter activity), which the phenotype data support without asserting the unproven IP3-gating mechanism. |
| GO:0070679 — inositol 1,4,5-trisphosphate binding | MF | IEA:InterPro | **Do not promote.** No direct binding assay exists; the ligand-binding residues are not computationally supported. Retain only as electronic inference or remove if the curator requires experimental backing for MF binding claims. |
| Intracellular Ca²⁺ release / calcium-mediated signalling | BP | Phenotype-supported | **Retain/support.** Genetic requirement for agonist-evoked Ca²⁺ entry (Traynor 2000) and DIF-induced autophagic cell death (Lam 2008) justify a BP annotation for Ca²⁺-mediated signalling. |
| Endoplasmic reticulum / intracellular membrane (CC) | CC | Homology/inference | **Retain as inferred**, consistent with an ER-localized IP3R/RyR-fold channel; note that direct localization data in *Dictyostelium* are limited. |

Guidance mapping to the focus type (function_assignment): the gene product **directly has** the broad channel/transporter function (well supported), but does **not** have demonstrated evidence for the *specific* IP3-gated activity or IP3 binding. The specific MF terms are therefore **too strong** for anything above IEA and should be retained only as electronic inference or generalized. Avoid defaulting to "protein binding" — the informative, defensible MF is a **calcium channel / calcium transmembrane transporter** term.

---

## Mechanistic Scope

**Immediate molecular function being tested:** whether the IplA polypeptide (a) binds IP3 and (b) conducts Ca²⁺ across an intracellular membrane in an IP3-dependent (gated) manner.

- **Direct gene-product activity with support:** membership in the IP3R/RyR channel family; presence of a pore-forming 6-TM domain and RIH binding-core fold consistent with a Ca²⁺-conducting channel.
- **Direct gene-product activity WITHOUT support:** IP3 binding (no assay); IP3-gated conductance (no electrophysiology or flux assay); conservation of IP3-recognition residues (computationally absent).
- **Downstream phenotypes (not the molecular function itself):** loss of agonist-evoked cytosolic Ca²⁺ rise, loss of Ca²⁺-gradient chemotaxis, reduced DIF-induced autophagic cell death, reduced polyphosphate-mediated proliferation inhibition, altered timing/amplitude of external-Ca²⁺ responses. These establish *involvement in Ca²⁺ signalling* but are loss-of-function readouts and do not localize the defect to an IP3-gating step within IplA itself.

The curatorial danger is conflating "iplA-null abolishes Ca²⁺ entry" (a downstream, pathway-level phenotype) with "IplA is the IP3-gated channel" (a direct molecular mechanism). The data support the former, not the latter.

---

## Conflicts and Alternatives

1. **Competing "Ca²⁺-sensing receptor" model.** Lusche et al. 2012 ([PMID: 22375061](https://pubmed.ncbi.nlm.nih.gov/22375061/)) explicitly propose IplA as the Ca²⁺ chemotaxis receptor or an essential component of Ca²⁺-sensing — a role in which Ca²⁺ (not IP3) is the relevant ligand/signal. Kim et al. 2025 ([PMID: 40295210](https://pubmed.ncbi.nlm.nih.gov/40295210/)) similarly frame IplA as a modulator of responses to external Ca²⁺.

2. **IplA-independent Ca²⁺ pathways.** Capacitative/store-operated entry (Schaloske 2005), CICR (Malchow 2008), and P2X purinergic influx (Ludlow 2008) all proceed without IplA. If IplA were the dominant IP3-gated ER Ca²⁺-release channel, one would expect broader disruption of store release; instead, store release is largely preserved.

3. **Divergent ligand-sensing module.** The absence of the MIR domain and non-conservation of IP3-contact residues raise the possibility that the *Dictyostelium* protein is gated by a different ligand or mechanism than metazoan IP3Rs. The family label "IP3 receptor-like" (note the "-like") reflects this uncertainty.

4. **Database carry-over / frequency bias.** The IP3-gated MF terms derive from InterPro family inference. Because the family is named after the metazoan IP3 receptor, the specific gating annotation propagates automatically to all members — a classic over-annotation risk when the defining ligand-binding residues are not verified in the target.

5. **No paralog confusion at the gene level.** There is only one IP3R-family gene in *Dictyostelium*, so the ambiguity is not "which paralog" but "does this single ortholog retain the ancestral IP3-gating mechanism."

---

## Limitations and Knowledge Gaps

| Gap | What was checked | Why it matters for curation | What would resolve it |
|---|---|---|---|
| No direct IP3-binding data | UniProt evidence codes; 15-record eutils literature sweep | GO:0070679 (IP3 binding) rests entirely on electronic inference | Radioligand or fluorescence-polarization IP3-binding assay on recombinant IplA N-terminus |
| No IP3-gated conductance data | Literature sweep; no electrophysiology found | GO:0005220 (IP3-gated channel) unproven at the protein level | Single-channel recording / Ca²⁺-flux assay of IplA reconstituted in bilayers or ER vesicles ± IP3 |
| IP3-contact residues not mappable | Custom Smith–Waterman vs human ITPR1; InterPro domain scan | Sequence divergence undermines the specific gating claim | Experimental or high-confidence predicted 3D structure of the IplA ligand-binding core; docking of IP3 |
| MIR domain absent | InterPro/Pfam scan (PF02815 not matched) | The metazoan IP3-sensing apparatus may not be present | Structural/biochemical characterization of the IplA N-terminus |
| Subcellular localization in *Dictyostelium* | Homology inference only | CC annotation (ER) is inferred, not directly shown | GFP-IplA localization / immuno-EM in *Dictyostelium* |
| Whether Ca²⁺ vs IP3 is the physiological gating signal | Competing-model literature (Lusche, Kim) | Determines correct MF term (IP3-gated vs Ca²⁺-sensing/CICR) | Structure–function assays testing gating by IP3 vs Ca²⁺ |

---

## Discriminating Tests / Proposed Follow-up Experiments

To distinguish "IP3-gated channel" from "Ca²⁺-sensing receptor" or "non-IP3 channel," the following are prioritized by decisiveness and feasibility:

1. **Direct IP3-binding assay** (highest priority): express the IplA N-terminal cytoplasmic region (residues ~1–1175) and test IP3 binding by radioligand ([³H]-IP3) competition or isothermal titration calorimetry. A negative result would strongly refute the IP3-gated claim; a positive result would convert GO:0070679 from IEA to IDA.

2. **IP3-gated conductance assay**: reconstitute full-length IplA into planar lipid bilayers or ER-derived vesicles and measure Ca²⁺ flux/single-channel activity in response to IP3 (and, as controls, Ca²⁺ and cADPR/NAADP). This directly tests GO:0005220.

3. **Structure-guided residue analysis**: obtain an experimental or AlphaFold structure of the IplA binding core, dock IP3, and test predicted contact residues by mutagenesis coupled to functional Ca²⁺ readout in iplA⁻ rescue.

4. **Rescue specificity**: complement iplA⁻ cells with wild-type IplA vs a putative binding-pocket mutant and ask whether agonist-evoked Ca²⁺ entry and DIF-induced cell death are restored only by the IP3-competent form.

5. **Comparative pathway epistasis**: manipulate PLC/IP3 levels (e.g., PLC-null, or acute IP3 uncaging) and measure IplA-dependent Ca²⁺ responses to test whether IP3 is upstream of IplA function specifically (vs merely present in the same pathway).

6. **Localization**: GFP-tagged IplA in *Dictyostelium* to confirm ER vs acidic-store vs plasma-membrane localization (relevant to the Ludlow/Kim acidic-store observations).

---

## Curation Leads (require curator verification)

- **Action change (MF):** Downgrade/flag **GO:0005220 (IP3-gated calcium channel activity)** and **GO:0070679 (IP3 binding)** as electronic-inference-only; do not treat as experimentally verified. Consider generalizing the retained MF to **GO:0005262 (calcium channel activity)** or **GO:0015085 (calcium ion transmembrane transporter activity)**, which the phenotype data support.
- **Retain (identity + BP):** Keep the IP3R/RyR-family identity and a Ca²⁺-mediated signalling BP annotation, supported by genetic phenotypes.
- **Candidate references + snippets to verify:**
  - [PMID: 10970875](https://pubmed.ncbi.nlm.nih.gov/10970875/): "we have disrupted an inositol 1,4,5-trisphosphate (InsP₃) receptor-like gene, iplA, to produce null cells in which Ca²⁺ entry in response to chemoattractants is abolished."
  - [PMID: 17854889](https://pubmed.ncbi.nlm.nih.gov/17854889/): "CIC was virtually unchanged in the iplA(-) strain that lacks a putative IP₃ or ryanodine receptor thought to be located at the endoplasmic reticulum."
  - [PMID: 22375061](https://pubmed.ncbi.nlm.nih.gov/22375061/): "suggesting that IplA is either the Ca²⁺ chemotaxis receptor or an essential component of the Ca²⁺ chemotaxis regulatory pathway."
  - [PMID: 18486207](https://pubmed.ncbi.nlm.nih.gov/18486207/): "were not affected by deletion of either the single Gbeta or iplA genes."
  - [PMID: 18077554](https://pubmed.ncbi.nlm.nih.gov/18077554/): "the only gene encoding an inositol 1,4,5-trisphosphate receptor (IP3R) in this organism."
- **Suggested curator questions:** Is any IDA-level IP3-binding or gating assay for IplA present in dictyBase or newer literature not captured here? Should the MF term be generalized pending direct evidence?
- **Suggested experiments:** the direct IP3-binding and reconstituted-conductance assays above (items 1–2), which would convert the annotation from inference to evidence-based.

---

## Provenance

- `ipla_ip3_residue_alignment.txt` — custom Smith–Waterman (BLOSUM62) alignment of IplA (1–1300) vs human ITPR1 (P29994), including the attempted mapping of the 9 canonical IP3-coordinating residues (0/9 confidently mapped) and the InterPro/Pfam domain scan showing the MIR domain absent. This is the computed basis for Finding 3.

---

*Prepared for AI Gene Review hypothesis-level curation. All experimental claims are attributed to the cited primary literature; all sequence/domain analyses are reported conservatively and distinguish direct results from homology inference.*


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)
- [OpenScientist ipla evidence matrix](openscientist_artifacts/ipla_evidence_matrix.csv)
- [OpenScientist ipla go decision table](openscientist_artifacts/ipla_go_decision_table.csv)