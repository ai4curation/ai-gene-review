---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-06T16:25:05.129146'
end_time: '2026-07-06T17:18:03.467821'
duration_seconds: 3178.34
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: yeast
  gene: CAF120
  gene_symbol: CAF120
  uniprot_accession: P53836
  taxon_id: NCBITaxon:559292
  taxon_label: Saccharomyces cerevisiae
  focus_type: function_assignment
  hypothesis_slug: function-hypothesis-go-0004672
  hypothesis_text: CAF120 has protein kinase activity (GO:0004672).
  term_context: '- Term: protein kinase activity (GO:0004672)

    - Evidence type: IBA

    - Original reference: GO_REF:0000033'
  reference_context: '- GO_REF:0000033'
  source_file: genes/yeast/CAF120/CAF120-ai-review.yaml
  source_selector: existing_annotations[1].function_hypothesis
  source_context_yaml: "term:\n  id: GO:0004672\n  label: protein kinase activity\n\
    evidence_type: IBA\noriginal_reference_id: GO_REF:0000033"
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 1
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

- **Organism code:** yeast
- **Taxon:** Saccharomyces cerevisiae (NCBITaxon:559292)
- **Gene directory:** CAF120
- **Gene symbol:** CAF120
- **UniProt accession:** P53836

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** function-hypothesis-go-0004672
- **Source file:** genes/yeast/CAF120/CAF120-ai-review.yaml
- **Source selector:** existing_annotations[1].function_hypothesis

## Seed Hypothesis

CAF120 has protein kinase activity (GO:0004672).

## Term and Decision Context

- Term: protein kinase activity (GO:0004672)
- Evidence type: IBA
- Original reference: GO_REF:0000033

## Reference Context

- GO_REF:0000033

## Source Context YAML

```yaml
term:
  id: GO:0004672
  label: protein kinase activity
evidence_type: IBA
original_reference_id: GO_REF:0000033
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
prompt so the report can be compared against them after the run.

Do not rely on literature alone. Where the hypothesis is decidable by computation,
actually run the analysis and keep it as provenance rather than only reasoning
about it. Match the analysis to the question, for example:

- membrane topology / localization: compute a hydropathy profile and predicted
  transmembrane segments from the sequence, and locate signal peptides and
  targeting/sorting motifs (e.g. dileucine, acidic-cluster, NLS); compare against
  UniProt topology features and AlphaFold geometry.
- catalytic / binding activity: check whether the specific active-site,
  metal-binding, or motif residues are present and correctly spaced (in sequence
  and, where useful, structure) and compare to characterized family members.
- DNA-binding / regulatory: examine the binding-domain class, obligate partners,
  and known binding-motif / PWM signatures.
- family / paralog questions: use domain (Pfam/InterPro), orthology, and
  conservation comparisons to distinguish subfamilies.

Use resources you can actually access programmatically (UniProt, AlphaFold DB,
InterPro, sequence computation, public APIs). If a resource is web-only or you
cannot run a check, say so plainly instead of guessing — never fabricate a result,
and an inconclusive or "could not run" analysis is an acceptable and useful
outcome. Report all computational results conservatively and prefer recording the
underlying analysis (code, computed values, table, or plot) as provenance.

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

# CAF120 (P53836) — Evaluation of "protein kinase activity" (GO:0004672)

**Gene:** CAF120 / YNL278W · *Saccharomyces cerevisiae* (NCBITaxon:559292)
**UniProt:** P53836 (CA120_YEAST), 1060 aa
**Focus type:** function_assignment — does the gene product directly have this molecular function?
**Hypothesis under review:** CAF120 has protein kinase activity (GO:0004672)
**Current annotation:** GO:0004672 · evidence IBA · reference GO_REF:0000033 (GO_Central phylogenetic annotation)

---

## Summary

The seed hypothesis that CAF120 possesses **protein kinase activity (GO:0004672)** is **refuted**. Three independent lines of evidence converge: (1) programmatic domain analysis shows P53836 carries **only a Pleckstrin-homology (PH) domain** and its fungal derivative — there is no protein-kinase domain of any kind; (2) a direct scan of the 1060-residue sequence finds **none** of the conserved eukaryotic protein-kinase (ePK) catalytic motifs required for phosphotransfer; and (3) the experimentally supported function of Caf120 is regulatory/adaptor in nature — a meiotic crossover regulator physically linked to the Exo1–MutLγ recombination machinery and, per UniProt curation, associated with the CCR4-NOT context — with no report of catalytic activity.

The GO:0004672 annotation is an **IBA phylogenetic mis-propagation**. It is co-annotated with GO:0007165 (signal transduction, also IBA) in the same record, and PH domains are shared with genuine kinases (e.g., AKT/PKB-type AGC kinases carry a PH module adjacent to their catalytic domain). The most parsimonious interpretation is that the GO_Central pipeline propagated "protein kinase activity + signal transduction" from a PH-domain-containing kinase clade to CAF120, which possesses the PH module but not the kinase domain.

The recommended curation action is to **remove** GO:0004672 from CAF120 — not to retain it, generalize it to a broader transferase/kinase term, or replace it with a more specific kinase term. This judgment is a structural-impossibility argument (the catalytic residues are physically absent) rather than merely "not yet tested," which makes the refutation strong. The residual uncertainty is limited to whether some wholly non-canonical catalytic mechanism could exist, for which there is no evidence.

---

## Key Findings

### Finding 1 — CAF120 has a PH-domain architecture with no kinase domain

Domain analysis via the InterPro API (queried this run) returns a single, internally consistent picture: **P53836 is a Pleckstrin-homology (PH) domain protein.** The matched signatures include Pfam **PF00169** (PH domain) and **PF25381** (fungal PH-like), PROSITE **PS50003** (PH profile), SMART **SM00233** (PH), Gene3D **2.30.29.30** (PH-domain-like β-sandwich fold), the InterPro PH-like superfamily **IPR011993**, and the dedicated fungal family **IPR058155 ("Skg3/CAF120-like PH domain")**.

Critically, **no kinase signatures are present at all.** There is no Pfam PF00069 (Pkinase), no InterPro IPR000719 (protein kinase domain), and no PANTHER protein-kinase family assignment. The PH-like β-sandwich fold is structurally unrelated to the bilobal α/β protein-kinase fold. A PH domain is a lipid/protein-interaction module that recruits proteins to membranes or partners; it confers no catalytic activity by itself. The existence of a *dedicated* fungal family term (IPR058155) built around the PH module — not a catalytic domain — indicates the correct family placement for CAF120 is a PH-adaptor family, not a kinase family.

### Finding 2 — The eukaryotic protein-kinase catalytic motifs are absent from the sequence

A direct motif scan of the full 1060-aa P53836 sequence tested each conserved catalytic element of the canonical ePK domain. All were absent:

| Catalytic element | Consensus | Function | Present in P53836? |
|-------------------|-----------|----------|--------------------|
| Glycine-rich loop (P-loop) | G-x-G-x-x-G | Positions ATP phosphates | **No** |
| β3 lysine (VAIK) | V-A-I-K | Anchors α/β phosphates of ATP | **No** |
| Catalytic loop | H-R-D | Catalytic aspartate (proton acceptor) | **No** |
| Mg-binding loop | D-F-G | Coordinates Mg²⁺ | Only stray "DFG" tripeptides in N-terminal/disordered region, not in a catalytic domain |
| PROSITE PS00107 | ATP-binding kinase signature | ATP binding | **No match** |
| PROSITE PS00108 | Ser/Thr kinase active-site signature | Catalysis | **No match** |

The simultaneous absence of the P-loop, the VAIK lysine, and the HRD aspartate is decisive. These form the minimal catalytic core: the P-loop and lysine bind and orient ATP, while the HRD aspartate is the catalytic base that deprotonates the substrate hydroxyl. Even pseudokinases — catalytically dead but retaining the fold — usually preserve recognizable remnants of these motifs. CAF120 has none of the scaffold ordered within a ~250–300-aa domain, indicating it does not belong to the protein-kinase superfamily at all. The two "DFG" tripeptides that occur by chance fall in the N-terminus and a disordered region rather than within any structured catalytic module, so they are not evidence of a kinase.

### Finding 3 — The experimentally supported role of Caf120 is regulatory, not catalytic

Two primary studies characterize Caf120, and neither reports or implies catalytic kinase activity:

- **Meiotic crossover regulation.** In a proteomic dissection of homologous-recombination enzyme networks, Caf120 was identified among the meiosis-specific interactors of the MutLγ–Exo1 crossover machinery and classified as a **regulator of crossing-over** ([PMID: 31351878](https://pubmed.ncbi.nlm.nih.gov/31351878/)). This places Caf120 in a physical/regulatory relationship with the recombination apparatus — an adaptor role, not an enzymatic one.

- **Stress-dependent relocalization.** In a proteome-wide survey of protein location and function under stress, Caf120 was one of several proteins that **change subcellular location under DNA-damaging conditions** ([PMID: 25028499](https://pubmed.ncbi.nlm.nih.gov/25028499/)). Regulated relocalization is consistent with a PH-domain adaptor redeployed in response to signals; no kinase activity is described.

UniProt further curates CAF120 within the CCR4-NOT context (transcription regulation / mRNA deadenylation) and notes it "Belongs to the CAF120 family." A "Phosphoprotein" keyword marks CAF120 as a kinase **substrate/target**, not a kinase — a common source of confusion, but the opposite of the hypothesis. None of these curated or experimental descriptions invokes phosphotransfer chemistry.

---

## Mechanistic Model / Interpretation

The evidence assembles into a clear model of how a spurious kinase annotation arose and why it should be removed.

```
   WHAT CAF120 ACTUALLY IS                    WHAT THE IBA CLAIMS
   ----------------------------               --------------------------
   1060-aa protein                            "protein kinase activity"
        |                                              |
   [ PH domain  (PF00169) ]                    requires bilobal ePK fold
   [ fungal Skg3/CAF120 PH ]                          |
   [   IPR058155 family    ]                    requires: GxGxxG P-loop
        |                                                VAIK Lys
   lipid / protein binding                              HRD Asp
   adaptor & recruitment                                DFG motif
        |                                              |
   regulatory / substrate roles:               NONE present in a catalytic
   - meiotic crossover regulation              domain in P53836
     (Exo1/MutLgamma, PMID 31351878)                   |
   - stress relocalization                     => structurally impossible
     (PMID 25028499)                              to catalyze phosphotransfer
   - CCR4-NOT context (UniProt)
   - phosphoprotein = KINASE TARGET,
     not kinase
```

**How the mis-annotation propagated.** GO:0004672 is annotated IBA (Inferred from Biological Ancestor) via GO_REF:0000033, the GO_Central phylogenetic pipeline, in which an experimentally supported annotation on one family member is propagated to un-characterized members in the same inferred ancestral clade. PH domains occur in many signaling proteins, and a subset of *bona fide* kinases — notably the AGC-family AKT/PKB — carry a PH module adjacent to their kinase domain. If the reference tree grouped CAF120's PH module with the PH modules of such kinases, "protein kinase activity" and "signal transduction" leaf annotations could propagate to CAF120 even though it has *only* the PH module. The co-occurrence of GO:0007165 (signal transduction) IBA in the same record is the fingerprint of exactly this PH-domain-driven mis-grouping.

**The correct molecular picture.** CAF120 is a non-catalytic PH-domain adaptor. Its PH β-sandwich most plausibly mediates membrane or protein interactions that position CAF120 within regulatory assemblies — the meiotic recombination network and the CCR4-NOT context. Its function is to *localize and connect*, not to *phosphorylate*.

---

## Evidence Base

| Citation | Evidence type | Supports/Refutes | Claim tested | Key finding | Context | Confidence / limitations |
|---|---|---|---|---|---|---|
| InterPro API (this run; IPR011993, IPR058155; Pfam PF00169, PF25381; PROSITE PS50003; SMART SM00233; Gene3D 2.30.29.30) | Structural/evolutionary (domain) | **Refutes** | Does CAF120 contain a protein-kinase domain? | Only PH domain + PH-like superfamily + fungal "Skg3/CAF120-like PH"; **no** kinase domain (no PF00069, no IPR000719, no PANTHER kinase family) | *S. cerevisiae* P53836 sequence | High. Absence of a kinase Pfam/InterPro hit is definitive for the ePK family |
| Sequence motif scan (this run) | Computational | **Refutes** | Are ePK catalytic motifs present? | **None** found: no GxGxxG P-loop, no VAIK Lys, no HRD, no PS00107/PS00108. Stray "DFG" tripeptides fall in N-terminal/disordered region, not a catalytic domain | 1060-aa sequence | High. Genuine ePKs require these motifs ordered within a ~250–300-aa domain |
| UniProt P53836 (Swiss-Prot, reviewed) | Review/database | **Competing (different function)** | What is CAF120's function? | CCR4-NOT context (transcription regulation / mRNA deadenylation); "Belongs to the CAF120 family"; keyword Phosphoprotein (substrate, not enzyme) | *S. cerevisiae* | High (manually curated). Function is adaptor/regulatory, not catalytic |
| [PMID: 31351878](https://pubmed.ncbi.nlm.nih.gov/31351878/) | Mutant/interaction (primary) | **Competing** | Native role of Caf120? | Identified as a **regulator of meiotic crossing-over**, a meiosis-specific interactor of the MutLγ–Exo1 recombination machinery | Yeast meiosis | Medium-high. No kinase activity implied |
| [PMID: 25028499](https://pubmed.ncbi.nlm.nih.gov/25028499/) | Localization (primary) | **Qualifies** | Condition-dependent behavior? | Caf120 changes subcellular location under DNA damage | Yeast stress proteomics | Medium. Regulatory relocalization, not enzymatic |
| GO:0004672 IBA + GO:0007165 IBA (GO_Central, GO_REF:0000033) | Computational (phylogenetic) | **Source of hypothesis** | Origin of kinase annotation | Both terms IBA from the same reference; kinase+signal-transduction pairing on a PH-only protein is a classic mis-propagation signature | GO_Central | The IBA is the artefact being evaluated, not independent support |

---

## GO Curation Implications

**Lead (requires curator verification): Remove GO:0004672 (protein kinase activity, MF)** from CAF120. The IBA lacks any catalytic-domain basis and conflicts with the curated molecular identity of the protein. Do **not** replace it with any other kinase/transferase MF term.

Reasoning by GO aspect:

- **Molecular Function (MF).** GO:0004672 is unsupported and contradicted by domain and motif analysis. If a positive MF term is desired, the only defensible option is a **PH-domain-based binding function** (lipid/phosphoinositide binding), and only if curator inspection of the PH ligand specificity supports it; otherwise leave MF unannotated rather than assert catalysis. Avoid the uninformative "protein binding" as a terminal recommendation.
- **Biological Process (BP).** The co-propagated GO:0007165 (signal transduction) IBA warrants the same scrutiny and is likely another mis-propagation. More defensible BP leads reflect the experimental literature — meiotic recombination / regulation of reciprocal meiotic recombination ([PMID: 31351878](https://pubmed.ncbi.nlm.nih.gov/31351878/)) — flagged for curator verification.
- **Cellular Component (CC).** Stress-dependent relocalization ([PMID: 25028499](https://pubmed.ncbi.nlm.nih.gov/25028499/)) and CCR4-NOT context (UniProt) are the relevant CC leads, not anything kinase-related.

**GO decision table:**

| Term | Aspect | Current | Recommended action | Basis |
|------|--------|---------|--------------------|-------|
| GO:0004672 protein kinase activity | MF | IBA (GO_REF:0000033) | **Remove** | No kinase domain; no catalytic residues |
| GO:0007165 signal transduction | BP | IBA (co-annotation) | **Flag / likely remove** | Same PH-domain mis-propagation signature |
| Meiotic recombination regulation | BP | — | **Candidate add** (curator verify) | PMID 31351878 |

---

## Mechanistic Scope

The molecular function under test is **catalytic transfer of a phosphate from ATP to a protein substrate** (phosphotransfer). This requires a spatially organized active site — a P-loop and β3 lysine to bind/orient ATP, an HRD aspartate as catalytic base, and a DFG aspartate to coordinate Mg²⁺. CAF120 lacks every one of these, so the *direct gene-product activity* hypothesized is physically precluded.

What CAF120 *does* have is a PH domain, whose direct molecular activity is **binding** (phosphoinositide lipids and/or protein partners) — a recruitment/scaffolding activity. Everything else attributed to CAF120 — regulation of meiotic crossovers, stress relocalization, CCR4-NOT association, and its status as a phosphoprotein — is either a **downstream, context-dependent regulatory role** mediated through interactions, or evidence that CAF120 is a kinase *target*. The kinase hypothesis conflates "participates in signaling/regulatory processes" (plausible for a PH adaptor) with "is itself a catalytic kinase" (unsupported and structurally impossible).

---

## Conflicts and Alternatives

- **Paralog / family confusion (most likely cause).** PH domains are present in many signaling kinases (AKT/PKB, PDK1, GRKs). A phylogenetic annotation propagated "protein kinase activity" down a reference tree from a PH-domain-containing kinase clade to CAF120, which shares only the non-catalytic PH module. This is the classic mechanism of IBA over-annotation.
- **Substrate-vs-enzyme confusion.** CAF120 is a phosphoprotein (target of kinases), not a kinase; the "Phosphoprotein" keyword can be misread as implying enzymatic activity.
- **Co-annotation artifact.** GO:0007165 appearing alongside GO:0004672 is itself evidence of a bundled mis-propagation rather than two independent, evidence-based calls.
- **No competing experimental claim.** There is no primary paper asserting kinase activity for CAF120; the annotation rests solely on the IBA inference, making the conflict one-sided.
- **Atypical/divergent kinase possibility (considered and rejected).** Highly diverged atypical kinases still adopt a nucleotide-binding kinase-like fold detectable by profile HMMs; InterPro/Pfam searches returned no kinase-related hit of any kind.

---

## Limitations and Knowledge Gaps

| Gap | What was checked | Why it matters | What would resolve it |
|---|---|---|---|
| Exact PANTHER/PAINT node that seeded the IBA | InterPro PANTHER endpoint returned no record this run | Confirms the propagation source and lets curators fix the tree annotation | Query GO_Central/PANTHER PAINT tree for the P53836 leaf and its annotated ancestral node |
| No direct in-vitro kinase assay exists for CAF120 | PubMed searches found only CCR4-NOT / meiosis / stress roles | A direct negative assay would be definitive, though absence of catalytic residues already predicts no activity | In-vitro autophosphorylation/substrate assay (predicted negative) |
| AlphaFold fold confirmation of non-PH regions | AF model exists (P53836); much of the sequence is predicted disordered | Rules out a cryptic kinase fold | Inspect AlphaFold pLDDT/domain segmentation; expect PH domain + long disordered tail, no kinase lobe |
| PH-domain ligand specificity | Domain identity clear, but specific ligand not determined here | A positive MF term depends on it | Structural docking / lipid-overlay (PIP-strip) assays |

Additional limitation: the refutation is primarily bioinformatic (domain + motif) plus the absence of any positive experimental kinase report. There is no wet-lab negative kinase assay in the literature; however, the physical absence of the catalytic residues provides a strong mechanism-based refutation, not merely an evidential one.

---

## Discriminating Tests

1. **PANTHER tree inspection (fastest).** Locate P53836 in its GO_Central PAINT tree and check whether the kinase MF was assigned at an ancestral node dominated by PH-domain kinases — confirms mis-propagation and gives curators the exact node to correct.
2. **HMMER/hmmscan against Pfam PF00069 (Pkinase / PK_Tyr_Ser-Thr).** Expected: no hit (corroborates the InterPro result with an independent tool).
3. **Structural superposition** of the CAF120 AlphaFold model onto a canonical kinase (e.g., PKA) catalytic domain. Expected: no bilobal match beyond incidental PH-fold.
4. **PH-domain ligand assay.** Lipid-overlay / liposome-binding to determine phosphoinositide specificity, supporting a correct positive binding MF term.
5. **(Definitive, low-priority) in-vitro kinase assay** with generic substrate + [γ-³²P]ATP. Predicted: negative.
6. **Family-wide IBA audit.** Pull all IPR058155 (Skg3/CAF120-like PH) members and check for GO:0004672 IBA to identify and correct systematic over-annotation.

---

## Proposed Follow-up Actions / Curation Leads (require curator verification)

- **Action:** Flag **GO:0004672 (protein kinase activity, IBA, GO_REF:0000033)** as an over-annotation for CAF120 and remove it from the gene review; do not replace with any other kinase MF term.
- **Also review (out of focus):** GO:0007165 (signal transduction, IBA) as the co-propagated term.
- **Candidate supporting references / snippets to verify:**
  - [PMID: 31351878](https://pubmed.ncbi.nlm.nih.gov/31351878/) — "*Functional analyses of meiosis-specific interactors of MutLγ-Exo1 identified Rtk1, Caf120, and Chd1 as regulators of crossing-over.*" (establishes a real, non-kinase function).
  - [PMID: 25028499](https://pubmed.ncbi.nlm.nih.gov/25028499/) — "*under DNA-damaging conditions, Tsr1, Caf120, Dip5, Skg6, Lte1, and Nnf2 change subcellular location.*" (regulatory relocalization, no catalytic activity).
  - UniProt P53836 FUNCTION/SIMILARITY blocks — "Belongs to the CAF120 family."
- **Suggested curator question:** Was the kinase MF asserted at a PH-domain-containing ancestral node in the PANTHER tree? If so, correct the ancestral annotation to stop propagation.
- **Suggested experiments (if any doubt remains):** in-vitro kinase assay (predicted negative); AlphaFold fold comparison to a kinase; PH-domain lipid-binding assay (to assign a correct positive MF).

### Provenance
Computational checks executed during this investigation:
- UniProt REST fetch of P53836 (function, features, GO, cross-references, sequence).
- InterPro API domain enumeration for P53836 (PH-only domain architecture; PF00169, PF25381, PS50003, SM00233, Gene3D 2.30.29.30, IPR011993, IPR058155; no kinase family).
- Regex/PROSITE scan of the 1060-aa sequence for ePK catalytic motifs (GxGxxG, VAIK, HRD, DFG, PS00107, PS00108) — all negative within a catalytic domain.

---

## Conclusion

CAF120 (P53836) is a Pleckstrin-homology-domain adaptor protein of the fungal Skg3/CAF120-like family, with experimentally supported regulatory roles in meiotic crossover control and stress-responsive relocalization, and a database-curated association with the CCR4-NOT context. It has no protein-kinase domain and lacks every conserved catalytic residue required for phosphotransfer. The GO:0004672 (protein kinase activity) IBA annotation is a PH-domain-driven phylogenetic over-annotation and should be **removed** rather than retained, generalized, or replaced with another catalytic term.


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)