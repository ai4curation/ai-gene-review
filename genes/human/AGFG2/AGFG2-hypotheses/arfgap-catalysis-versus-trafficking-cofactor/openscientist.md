---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-21T01:28:40.532070'
end_time: '2026-09-21T01:52:11.493199'
duration_seconds: 1410.96
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: human
  gene: AGFG2
  gene_symbol: AGFG2
  uniprot_accession: O95081
  taxon_id: NCBITaxon:9606
  taxon_label: Homo sapiens
  focus_type: function_assignment
  hypothesis_slug: arfgap-catalysis-versus-trafficking-cofactor
  hypothesis_text: Human AGFG2/HRBL (O95081) has physiologically relevant GTPase-activator
    activity, potentially toward an ARF substrate. Evaluate the molecular-function
    claim separately from its established vesicle-trafficking roles. The exact target
    retains Arg75, corresponding to ASAP3 Arg469, but carries Thr89 at the position
    aligned to ASAP3 Asp484. The existing reproducible MAFFT domain alignment records
    these coordinates. PMID23433073 proposes substantial catalytic divergence of AGFG
    domains including the Asp and conserved tryptophan positions, but explicitly also
    reports loss of the Asp-homologous site in all 18 GIT-family sequences. Primary
    PMID10788515 directly measures ARF GAP activity of GIT1 and GIT2, so this substitution
    cannot be assumed universally diagnostic of inactivity. Inspect primary structural/mutational
    PMID20510928 and relevant biochemical studies for whether the ASAP3 requirement
    generalizes to AGFG2 or reflects a particular catalytic mechanism. PMID34369554
    calls an R75Q construct GAP-dead and states that it still promotes Weibel-Palade
    body secretion, with those data not shown; the secretion assay is not itself a
    GTPase-hydrolysis assay. Determine whether any direct AGFG2 biochemical evidence
    establishes retained activity, altered specificity or loss, and distinguish absent
    assays from functional refutation. Consider a noncatalytic trafficking-cofactor
    model without assuming that this role and GAP catalysis are mutually exclusive.
  term_context: No specific term context supplied.
  reference_context: No specific reference context supplied.
  source_file: genes/human/AGFG2/AGFG2-ai-review.yaml
  source_selector: free-text
  source_context_yaml: "hypothesis: Human AGFG2/HRBL (O95081) has physiologically\
    \ relevant GTPase-activator activity, potentially\n  toward an ARF substrate.\
    \ Evaluate the molecular-function claim separately from its established vesicle-trafficking\n\
    \  roles. The exact target retains Arg75, corresponding to ASAP3 Arg469, but carries\
    \ Thr89 at the position\n  aligned to ASAP3 Asp484. The existing reproducible\
    \ MAFFT domain alignment records these coordinates.\n  PMID23433073 proposes substantial\
    \ catalytic divergence of AGFG domains including the Asp and conserved\n  tryptophan\
    \ positions, but explicitly also reports loss of the Asp-homologous site in all\
    \ 18 GIT-family\n  sequences. Primary PMID10788515 directly measures ARF GAP activity\
    \ of GIT1 and GIT2, so this substitution\n  cannot be assumed universally diagnostic\
    \ of inactivity. Inspect primary structural/mutational PMID20510928\n  and relevant\
    \ biochemical studies for whether the ASAP3 requirement generalizes to AGFG2 or\
    \ reflects\n  a particular catalytic mechanism. PMID34369554 calls an R75Q construct\
    \ GAP-dead and states that it still\n  promotes Weibel-Palade body secretion,\
    \ with those data not shown; the secretion assay is not itself\n  a GTPase-hydrolysis\
    \ assay. Determine whether any direct AGFG2 biochemical evidence establishes retained\n\
    \  activity, altered specificity or loss, and distinguish absent assays from functional\
    \ refutation. Consider\n  a noncatalytic trafficking-cofactor model without assuming\
    \ that this role and GAP catalysis are mutually\n  exclusive.\nfocus_type: function_assignment\n\
    context: []\nreference_id: []"
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
- **Gene directory:** AGFG2
- **Gene symbol:** AGFG2
- **UniProt accession:** O95081

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** arfgap-catalysis-versus-trafficking-cofactor
- **Source file:** genes/human/AGFG2/AGFG2-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

Human AGFG2/HRBL (O95081) has physiologically relevant GTPase-activator activity, potentially toward an ARF substrate. Evaluate the molecular-function claim separately from its established vesicle-trafficking roles. The exact target retains Arg75, corresponding to ASAP3 Arg469, but carries Thr89 at the position aligned to ASAP3 Asp484. The existing reproducible MAFFT domain alignment records these coordinates. PMID23433073 proposes substantial catalytic divergence of AGFG domains including the Asp and conserved tryptophan positions, but explicitly also reports loss of the Asp-homologous site in all 18 GIT-family sequences. Primary PMID10788515 directly measures ARF GAP activity of GIT1 and GIT2, so this substitution cannot be assumed universally diagnostic of inactivity. Inspect primary structural/mutational PMID20510928 and relevant biochemical studies for whether the ASAP3 requirement generalizes to AGFG2 or reflects a particular catalytic mechanism. PMID34369554 calls an R75Q construct GAP-dead and states that it still promotes Weibel-Palade body secretion, with those data not shown; the secretion assay is not itself a GTPase-hydrolysis assay. Determine whether any direct AGFG2 biochemical evidence establishes retained activity, altered specificity or loss, and distinguish absent assays from functional refutation. Consider a noncatalytic trafficking-cofactor model without assuming that this role and GAP catalysis are mutually exclusive.

## Term and Decision Context

No specific term context supplied.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: Human AGFG2/HRBL (O95081) has physiologically relevant GTPase-activator activity, potentially
  toward an ARF substrate. Evaluate the molecular-function claim separately from its established vesicle-trafficking
  roles. The exact target retains Arg75, corresponding to ASAP3 Arg469, but carries Thr89 at the position
  aligned to ASAP3 Asp484. The existing reproducible MAFFT domain alignment records these coordinates.
  PMID23433073 proposes substantial catalytic divergence of AGFG domains including the Asp and conserved
  tryptophan positions, but explicitly also reports loss of the Asp-homologous site in all 18 GIT-family
  sequences. Primary PMID10788515 directly measures ARF GAP activity of GIT1 and GIT2, so this substitution
  cannot be assumed universally diagnostic of inactivity. Inspect primary structural/mutational PMID20510928
  and relevant biochemical studies for whether the ASAP3 requirement generalizes to AGFG2 or reflects
  a particular catalytic mechanism. PMID34369554 calls an R75Q construct GAP-dead and states that it still
  promotes Weibel-Palade body secretion, with those data not shown; the secretion assay is not itself
  a GTPase-hydrolysis assay. Determine whether any direct AGFG2 biochemical evidence establishes retained
  activity, altered specificity or loss, and distinguish absent assays from functional refutation. Consider
  a noncatalytic trafficking-cofactor model without assuming that this role and GAP catalysis are mutually
  exclusive.
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

# AGFG2 (O95081) — ArfGAP Catalysis vs. Trafficking Cofactor

**Focus type:** function_assignment
**Hypothesis slug:** arfgap-catalysis-versus-trafficking-cofactor
**Question:** Does human AGFG2/HRBL directly possess GTPase-activator (ArfGAP) activity, warranting a molecular-function annotation, or is its established role a non-catalytic vesicle-trafficking cofactor?

---

## Executive Judgment

**Verdict: UNRESOLVED (leaning "unsupported as an experimental MF; not refuted at the sequence level").**

There is **no direct biochemical evidence** that AGFG2 accelerates GTP hydrolysis on any ARF (or other) GTPase. The molecular-function claim of catalytic ArfGAP activity therefore cannot be asserted as experimentally supported. At the same time, it **cannot be refuted on sequence grounds**: AGFG2 retains an intact Arf-GAP zinc-finger domain and, critically, the catalytic **arginine finger (Arg75)** that the transition-state structure of ASAP3–Arf6 identifies as the key catalytic residue (PMID20510928). The one divergence highlighted by the seed — **Thr89** where ASAP3 has **Asp484** — is not, by itself, diagnostic of inactivity, because the GIT-family ArfGAPs lack that same aspartate-homologous site (PMID23433073) yet display measured ARF GAP activity (PMID10788515).

The only functional data on AGFG2 (PMID34369554) is a knockdown secretion phenotype (von Willebrand factor exocytosis from Weibel–Palade bodies), which is **not a GTPase-hydrolysis assay**. The "GAP-dead" R75Q construct in that paper still promoted secretion, but those data are marked "not shown." Thus the evidence-supported role of AGFG2 is a **trafficking cofactor**, while catalytic ArfGAP activity remains an untested computational inference. Absent assays are not equivalent to functional refutation.

**Most important caveat:** the central factual question — has anyone ever purified AGFG2 (or its paralog AGFG1) and measured GAP activity? — appears to be answered "no" in the retrievable literature. The MF annotation therefore rests on domain homology (IEA/ISS), not on experiment.

---

## Evidence Matrix

| Citation | Evidence type | Supports/Refutes/Qualifies | Claim tested | Key finding | Context | Confidence & limitations |
|---|---|---|---|---|---|---|
| PMID20510928 (Ismail 2010) | Structural (transition-state X-ray) | Qualifies | Which residues define the ArfGAP catalytic mechanism | Arginine finger (ASAP3 **Arg469**) + Arf6 glutamine + a Ca²⁺ ion are the key catalytic residues; the Asp position (=AGFG2 Thr89) is **not** listed among essential catalytic residues | ASAP3–Arf6 fusion, in vitro | High for ASAP3; does not test AGFG2. Ca²⁺ stimulation is ASAP-specific |
| PMID10788515 (Vitale 2000) | Direct biochemical assay | Qualifies / supports feasibility | Is the Asp-homologous site required for catalysis? | GIT1/GIT2 show **ARF6 GAP activity**; zinc finger required; 1 Zn²⁺/molecule | Recombinant human proteins, in vitro | High; paralog precedent, not AGFG2 itself |
| PMID23433073 (Schlacht 2013) | Evolutionary / comparative | Qualifies | Catalytic-residue conservation across the ArfGAP family | AGFG domains show catalytic divergence (Asp and conserved Trp); the Asp-homologous site is **lost in all 18 GIT sequences** | Multi-eukaryote sequence phylogeny | High for evolution; predicts, does not assay activity |
| PMID34369554 (Watanabe 2021) | Knockdown / mutant phenotype | Qualifies (not an MF assay) | Does AGFG2 function in secretion; is catalysis required? | AGFG2 KD inhibits stimulated vWF exocytosis; **R75Q "GAP-dead" still promotes secretion (data not shown)** | HUVEC/endothelial, cell-based | Moderate; secretion assay ≠ hydrolysis assay; key data not shown |
| This work | Computational alignment (NW/BLOSUM62) | Qualifies | Verify AGFG2↔ASAP3 catalytic-residue mapping | AGFG2 **Arg75↔ASAP3 Arg469** (arginine finger conserved); AGFG2 **Thr89↔ASAP3 Asp484**; C4 zinc-finger cysteines intact | UniProt O95081 (dom 27–153, ZnF 47–70) vs Q8TDY4 (dom 426–551, ZnF 441–464) | Reproducible; inference, not assay |
| This work | Computational alignment vs canonical active GAP | Qualifies | Cross-check arginine finger + tryptophan conservation | Reciprocal best match **AGFG2 Arg75↔ARFGAP1 Arg50** (independent confirmation of arg finger); a Trp in the ARFGAP1 catalytic core does **not** align to a Trp in AGFG2 (consistent with PMID23433073 Trp divergence) | UniProt O95081 vs ARFGAP1 Q8N6T3 (dom 7–124) | Ragged loop regions; arg-finger call robust, Trp call suggestive |
| UniProt O95081 / P52594 | Database record | Qualifies | Provenance of existing GAP annotation | GO:0005096 is **IEA:InterPro** for both AGFG2 and AGFG1 (no experimental GAP); vWF/WPB secretion not yet in GO | Human, database | Database-level; confirms homology-only status |

---

## GO Curation Implications (leads — require curator verification)

**Curation baseline (verified from UniProt O95081, iteration 2):** The existing MF term **GO:0005096 "GTPase activator activity" is annotated `IEA:InterPro`** (from ArfGAP domain IPR001164 / PF01412) — i.e., pure domain-based inference, no experimental support. AGFG2's curated BP terms are all `IBA:GO_Central` (acrosome assembly, intermediate filament organization, spermatid nucleus differentiation); **the experimentally demonstrated regulated-exocytosis role (PMID34369554, vWF/Weibel-Palade body) is NOT yet in GO.** The paralog **AGFG1 (P52594) also carries GO:0005096 only as `IEA:InterPro`**, while its experimental annotations are nucleus / cytoplasmic vesicle / RNA binding / mRNA export — so *neither* AGFG paralog has an experimentally supported GAP annotation.

**Molecular Function — "ARF GTPase activator activity" (GO:0008060) / "GTPase activator activity" (GO:0005096):**
- **Recommended action: retain only as computational/IEA (or ISS) — do NOT upgrade to an experimental (EXP/IDA) MF annotation.** No direct assay supports catalysis for AGFG2; the current term is already IEA:InterPro, which is appropriately conservative.
- **Do not remove** the term solely on the Thr89 (Asp→Thr) substitution: the GIT precedent (PMID10788515 + PMID23433073) shows loss of that aspartate is not diagnostic of inactivity, and the catalytic arginine finger (Arg75) is retained.
- If an experimental MF annotation currently exists based on PMID34369554, it is **too strong** — that paper provides a cellular phenotype, not GAP activity; consider re-scoping to a BP annotation.

**Biological Process (evidence-supported, core):**
- **"regulated exocytosis" / "von Willebrand factor secretion" / "Weibel-Palade body" (e.g., GO:0060627 regulation of vesicle-mediated transport; GO:0002576-adjacent secretion terms; GO:0033093 Weibel-Palade body)** — supported by IMP/IGI from PMID34369554 (siRNA knockdown). This is the best-supported functional annotation.

**Cellular Component:** AGFG family carries FG-repeat / nucleoporin-related regions; localization annotations should follow direct evidence, not be inferred from the MF claim.

### GO Decision Table (leads — require curator verification)

| GO ID | Term | Current status | Recommended action (lead) | Rationale |
|---|---|---|---|---|
| GO:0005096 | MF: GTPase activator activity | **IEA:InterPro** (verified) | **Retain as IEA/ISS; do NOT upgrade to EXP** | No direct GAP assay on AGFG2; zinc-finger + arginine finger intact but Thr89/Trp divergence — homology-only inference |
| GO:0008060 | MF: ARF GTPase activator activity (more specific) | Not annotated | Optional ISS lead only | More specific, still unproven; substrate ARF isoform untested |
| GO:0032796 / regulated exocytosis (e.g. GO:0045055) | BP: regulated exocytosis / vWF secretion | **Not in GO** | **ADD as IMP (PMID34369554)** | Knockdown reduces stimulated vWF exocytosis — best-supported functional annotation |
| GO:0033093 | CC: Weibel-Palade body (context) | Not in GO | Consider as context; needs direct localization | Functional link shown; direct AGFG2 localization to WPB not established |

### Structural provenance of the catalytic scaffold (iteration 3)

Direct inspection of UniProt sequences shows the AGFG2 ArfGAP zinc finger (res 47–70) has four cysteines at 47, 50, 67, 70 with inter-cysteine gaps **[3, 17, 3]** — **identical spacing to canonical active ARFGAP1** (Cys 22, 25, 42, 45; gaps [3, 17, 3]; the C‑x2‑C‑x16‑C‑x2‑C ArfGAP zinc knuckle). The catalytic arginine finger sits immediately C‑terminal to the last cysteine in a conserved motif — AGFG2 `SGLLRGL` (R75), ARFGAP1 `SGRHRGL` (R50), ASAP3 `SGVHREL` (R469). **The zinc-coordinating scaffold and arginine finger of AGFG2 are therefore structurally canonical and intact**, so the MF claim cannot be refuted on structural grounds; divergence is confined to accessory positions (Thr89↔Asp484 and a non-conserved tryptophan).

**Bottom line for the curator:** the ArfGAP MF term is best treated as **non-core / homology-only**, and the gene's evidence-backed core is a **trafficking cofactor in ARF-regulated regulated secretion**. Avoid defaulting to "protein binding."

---

## Mechanistic Scope

- **Immediate molecular activity tested:** acceleration of GTP hydrolysis on an ARF substrate by the AGFG2 Arf-GAP zinc-finger domain (an MF, GO:0008060).
- **What is actually demonstrated:** a downstream **cellular phenotype** — loss of AGFG2 reduces stimulated vWF exocytosis (PMID34369554). This is separated from direct catalysis by at least two inferential steps (knockdown → pathway effect; not enzyme kinetics).
- **Structural inference:** catalysis in this family is driven by a GAP-supplied arginine finger acting on an Arf-supplied glutamine (PMID20510928); AGFG2 retains the arginine finger, so the catalytic machinery is not obviously broken, but this is inference, not measurement.

---

## Conflicts and Alternatives

1. **Non-catalytic cofactor model (favored by available data).** The R75Q "GAP-dead" construct reportedly still promoting secretion (PMID34369554, data not shown) suggests the trafficking role may not require catalysis. Catalysis and cofactor roles are **not mutually exclusive**, but only the cofactor role has functional support.
2. **Paralog / family carry-over.** ArfGAP MF annotations propagate by InterPro domain (Arf-GAP, PF01412) across the whole family; AGFG2's term may be database carry-over rather than gene-specific evidence.
3. **Evolutionary divergence argument (PMID23433073).** Predicts AGFG catalytic weakening (Asp + Trp divergence). This is a prediction, self-limited by the authors' own GIT counterexample.
4. **Substrate ambiguity.** Even if AGFG2 is an active GAP, the target Arf isoform is unknown (GIT proteins prefer ARF6 over ARF1; AGFG2 substrate untested).
5. **AGFG1 context.** AGFG1/HRB was historically characterized as an HIV-Rev cofactor / FG-repeat nucleoporin-like protein, not as an assayed GAP — reinforcing that the family's "ArfGAP" label is largely domain-based.

---

## Knowledge Gaps

| Gap | What was checked | Why it matters | Resolving evidence |
|---|---|---|---|
| No purified-protein GAP assay for AGFG2 | PubMed searches (AGFG2, WPB, GIT/ArfGAP) returned no biochemical assay | Determines whether MF term is experimentally justifiable | In vitro GAP assay (single-turnover GTP hydrolysis) on ARF1/ARF5/ARF6 ± AGFG2 domain |
| Catalytic role of the Asp position | Structure (PMID20510928) lists arg finger + Arf Gln, not Asp; GIT lacks Asp yet active | Decides whether Thr89 refutes activity | Asp→Thr / Thr→Asp swap assays in an active ArfGAP scaffold |
| Whether R75/catalysis is needed for secretion | PMID34369554 states R75Q rescues, "data not shown" | Distinguishes catalytic vs scaffold mechanism | Published, quantified R75Q rescue with a validated GAP-dead control |
| Substrate identity | No AGFG2 substrate mapping found | Needed for a precise MF/substrate qualifier | GAP assay panel across ARF isoforms |

---

## Discriminating Tests

1. **Single-turnover GAP assay** with recombinant AGFG2 Arf-GAP domain (res ~27–153) against ARF1/ARF5/ARF6 loaded with GTP; include ASAP3 (positive) and a catalytic-Cys-mutant AGFG2 (negative). Direct readout of the MF claim.
2. **Structure-guided mutagenesis:** AGFG2 R75Q (arg-finger dead) and T89D (restore Asp) tested in the GAP assay to determine whether Thr89 limits activity.
3. **Rescue specificity in cells:** re-express WT vs R75Q vs zinc-finger-dead AGFG2 in AGFG2-depleted endothelial cells and quantify vWF exocytosis — resolves catalytic vs scaffold requirement.
4. **Comparative alignment/AlphaFold3 modeling** of AGFG2–ARF6 to check whether the catalytic geometry (arg finger, Ca²⁺/Asp pocket) is preserved.

---

## Curation Leads (require curator verification)

- **Candidate references to attach:**
  - PMID34369554 — AGFG2 in regulated vWF exocytosis (BP/IMP lead; note "GAP-dead" data not shown).
  - PMID20510928 — defines ArfGAP catalytic residues (arg finger; Asp not essential) — supports NOT refuting on Thr89.
  - PMID10788515 — GIT ArfGAP activity without the Asp-homologous site — counters over-reliance on the Asp substitution.
  - PMID23433073 — evolutionary divergence of AGFG catalytic residues — context for weakening (but self-caveated).
- **Candidate GO actions:**
  - MF GO:0008060 / GO:0005096 → keep as **IEA/ISS only; flag as unverified**; do not assign experimental evidence codes.
  - BP → add/retain **regulated exocytosis / vWF secretion / Weibel-Palade body** with IMP from PMID34369554.
- **Suggested curator questions:**
  - Is any existing experimental MF ArfGAP annotation on AGFG2 traceable to a real assay, or is it phenotype-based (PMID34369554)? If the latter, re-scope to BP.
  - Should the review add a "no direct catalytic assay available" note to prevent paralog-driven over-annotation?
- **Suggested experiments:** the single-turnover GAP assay + R75Q/T89D mutants above.

---

## Limitations

- Analysis is literature- and sequence-based; no wet-lab data were generated.
- The pivotal R75Q rescue in PMID34369554 is "data not shown," so its interpretation is provisional.
- The pairwise NW alignment reproduces the seed's MAFFT coordinates but is a two-sequence global alignment, not a full family MSA; conclusions about the arginine finger and Asp positions are robust because they are anchored on the ASAP3 crystal structure numbering.


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)