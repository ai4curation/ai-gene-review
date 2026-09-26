---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-21T03:08:08.955853'
end_time: '2026-09-21T03:36:00.090140'
duration_seconds: 1671.13
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: NEUCR
  gene: glt-1
  gene_symbol: glt-1
  uniprot_accession: Q1K4S3
  taxon_id: NCBITaxon:367110
  taxon_label: Neurospora crassa (strain ATCC 24698 / 74-OR23-1A / CBS 708.71 / DSM
    1257 / FGSC 987)
  focus_type: function_assignment
  hypothesis_slug: glucose-transport-and-proton-coupling
  hypothesis_text: Neurospora crassa GLT-1 (NCU01633; Q1K4S3) retains carbohydrate-proton
    symport and proton transmembrane transport in addition to its established low-affinity
    glucose uptake. Evaluate against actual GO definitions, primary uptake/energetics
    measurements, and historical system-I assignment. PMID28115989 directly measures
    radioglucose kinetics and maps GLT-1 to historical system I; its Discussion distinguishes
    system-I diffusion from system-II proton coupling. Does the identification establish
    absence of proton coupling, or infer it from affinity/expression and earlier whole-cell
    work? Read relevant historical primary experiments, assay design and protein-specific
    evidence. Current PTHR48022 target leaf PTN002362095 is a descendant of the actual
    PTN000627328 IBD for GO0005351; there is no lineage loss row in the recovered
    path. Low affinity does not itself imply passive transport and absence of a target
    experiment alone does not invalidate ancestry. Distinguish glucose specificity
    from coupling mechanism.
  term_context: No specific term context supplied.
  reference_context: No specific reference context supplied.
  source_file: genes/NEUCR/glt-1/glt-1-ai-review.yaml
  source_selector: free-text
  source_context_yaml: "hypothesis: Neurospora crassa GLT-1 (NCU01633; Q1K4S3) retains\
    \ carbohydrate-proton symport and proton\n  transmembrane transport in addition\
    \ to its established low-affinity glucose uptake. Evaluate against\n  actual GO\
    \ definitions, primary uptake/energetics measurements, and historical system-I\
    \ assignment. PMID28115989\n  directly measures radioglucose kinetics and maps\
    \ GLT-1 to historical system I; its Discussion distinguishes\n  system-I diffusion\
    \ from system-II proton coupling. Does the identification establish absence of\
    \ proton\n  coupling, or infer it from affinity/expression and earlier whole-cell\
    \ work? Read relevant historical\n  primary experiments, assay design and protein-specific\
    \ evidence. Current PTHR48022 target leaf PTN002362095\n  is a descendant of the\
    \ actual PTN000627328 IBD for GO0005351; there is no lineage loss row in the recovered\n\
    \  path. Low affinity does not itself imply passive transport and absence of a\
    \ target experiment alone\n  does not invalidate ancestry. Distinguish glucose\
    \ specificity from coupling mechanism.\nfocus_type: function_assignment\ncontext:\
    \ []\nreference_id: []"
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
artifact_count: 5
artifact_sources:
  openscientist_artifacts_zip: 5
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
- filename: provenance_glt1_GO_decision_table.csv
  path: openscientist_artifacts/provenance_glt1_GO_decision_table.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist glt1 GO decision table
- filename: provenance_glt1_TM1_expanded_panel.csv
  path: openscientist_artifacts/provenance_glt1_TM1_expanded_panel.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist glt1 TM1 expanded panel
- filename: provenance_glt1_TM1_protonation_site_analysis.csv
  path: openscientist_artifacts/provenance_glt1_TM1_protonation_site_analysis.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist glt1 TM1 protonation site analysis
---

## Question

# AIGR Gene Hypothesis Deep Research

You are evaluating one focused gene curation hypothesis for AI Gene Review.
This is not a general gene overview. Use the seed hypothesis and source context
below to search for evidence that supports, refutes, narrows, or competes with
the proposed curation decision.

## Target Gene

- **Organism code:** NEUCR
- **Taxon:** Neurospora crassa (strain ATCC 24698 / 74-OR23-1A / CBS 708.71 / DSM 1257 / FGSC 987) (NCBITaxon:367110)
- **Gene directory:** glt-1
- **Gene symbol:** glt-1
- **UniProt accession:** Q1K4S3

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** glucose-transport-and-proton-coupling
- **Source file:** genes/NEUCR/glt-1/glt-1-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

Neurospora crassa GLT-1 (NCU01633; Q1K4S3) retains carbohydrate-proton symport and proton transmembrane transport in addition to its established low-affinity glucose uptake. Evaluate against actual GO definitions, primary uptake/energetics measurements, and historical system-I assignment. PMID28115989 directly measures radioglucose kinetics and maps GLT-1 to historical system I; its Discussion distinguishes system-I diffusion from system-II proton coupling. Does the identification establish absence of proton coupling, or infer it from affinity/expression and earlier whole-cell work? Read relevant historical primary experiments, assay design and protein-specific evidence. Current PTHR48022 target leaf PTN002362095 is a descendant of the actual PTN000627328 IBD for GO0005351; there is no lineage loss row in the recovered path. Low affinity does not itself imply passive transport and absence of a target experiment alone does not invalidate ancestry. Distinguish glucose specificity from coupling mechanism.

## Term and Decision Context

No specific term context supplied.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: Neurospora crassa GLT-1 (NCU01633; Q1K4S3) retains carbohydrate-proton symport and proton
  transmembrane transport in addition to its established low-affinity glucose uptake. Evaluate against
  actual GO definitions, primary uptake/energetics measurements, and historical system-I assignment. PMID28115989
  directly measures radioglucose kinetics and maps GLT-1 to historical system I; its Discussion distinguishes
  system-I diffusion from system-II proton coupling. Does the identification establish absence of proton
  coupling, or infer it from affinity/expression and earlier whole-cell work? Read relevant historical
  primary experiments, assay design and protein-specific evidence. Current PTHR48022 target leaf PTN002362095
  is a descendant of the actual PTN000627328 IBD for GO0005351; there is no lineage loss row in the recovered
  path. Low affinity does not itself imply passive transport and absence of a target experiment alone
  does not invalidate ancestry. Distinguish glucose specificity from coupling mechanism.
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

# Focused Curation Report — GLT-1 (NEUCR, Q1K4S3): "glucose transport and proton coupling"

**Gene:** glt-1 / NCU01633 / Q1K4S3 (*Neurospora crassa*)
**Focus type:** function_assignment
**Hypothesis slug:** glucose-transport-and-proton-coupling
**Disputed function:** carbohydrate:proton symporter activity (GO:0005351) + proton transmembrane transport, in addition to established low-affinity glucose uptake.

---

## Executive Judgment

**Verdict: Weakly supported / over-annotated as a specific mechanistic claim.**

The seed hypothesis — that GLT-1 *retains* carbohydrate:proton symport in addition to low-affinity glucose uptake — rests entirely on **ancestry (PANTHER IBD/IBA) inference, not on any protein-specific measurement**. Three independent lines of evidence argue that the proton-symporter molecular function is not the gene product's actual activity:

1. **Annotation provenance.** Every GO term on Q1K4S3 is evidence code **IBA:GO_Central** (PANTHER PAINT), including GO:0005351. There is no experimental (EXP/IDA/IMP) support for proton coupling.
2. **Family logic.** GLT-1 belongs to the MFS **Sugar Porter family** (PTHR48022; Pfam PF00083), which contains *both* proton symporters (XylE, plant STP) *and* facilitated-diffusion uniporters (mammalian GLUT/SLC2, yeast HXT). Mechanism is **not conserved** across this family, so a family-level "sugar:proton symporter activity" cannot be assumed for a given member (PMID 24847886).
3. **Direct sequence discriminator, with an intra-organism control.** GLT-1 **lacks the acidic TM1 protonation-site residue** that is obligatory for sugar:H⁺ symport. At the position that is Asp27 in the symporter XylE and Asp40 in the symporter STP1 (and Asn29 in the uniporter GLUT1), GLT-1 has a **non-protonatable Val48** — even less symport-compatible than GLUT. Critically, the **same scan run on the *Neurospora* high-affinity paralogs shows they RETAIN the acidic residue** — HGT-1 (Q7S0I5) Asp52, HGT-2 (Q7S3Q4) Asp35 — while only the low-affinity GLT-1 has lost it. Within one genome, proton-coupling capacity thus segregates to the high-affinity (system-II-like) transporters, exactly matching the classical physiology, and pinpoints GLT-1 as the member that specifically lost the coupling determinant. A valine cannot act as proton donor/acceptor (diagnostic per PMID 28617850).

The seed's fair caveat holds: the identification paper (PMID 28115989) infers system-I assignment from affinity/expression and did **not** run a GLT-1-specific proton-flux/electrophysiology assay, so it does not *experimentally* refute symport at the protein level. Hence "refuted" is too strong; but the convergent structural/evolutionary evidence makes proton-coupled symport the **less likely** mechanism. **Curation recommendation: do not assert GO:0005351 as a core/experimental function; treat it as IBA-only and preferably generalize the MF to glucose/carbohydrate transmembrane transporter activity (uniporter).** This is a lead requiring curator verification.

---

## Evidence Matrix

| Citation | Evidence type | Stance | Claim tested | Key finding | Context | Confidence / limitations |
|---|---|---|---|---|---|---|
| UniProt Q1K4S3 (DB record, fetched 2026-09-21) | review/database | qualifies | Basis of GO:0005351 on GLT-1 | GO:0005351, GO:0008643, GO:0016020 all **IBA:GO_Central**; PANTHER PTHR48022:SF92 "low affinity glucose transporter MstE" | Sugar Porter family record | High for provenance; IBA ≠ experimental |
| PMID 28617850 (Ke et al. 2017) | structural/evolutionary + biochem | refutes | TM1 residue determines symport vs uniport | "acidic residue (Asp27 in XylE) vs neutral (Asn29 in GLUT1)…key element for mechanistic divergence" | XylE/GLUT1 MD + mutagenesis | High for diagnostic; notes multiple residues fine-tune |
| PMID 24847886 (Deng et al. 2014) | structural | qualifies | Same fold hosts both mechanisms | GLUT1 uniporter vs XylE proton symporter share the sugar-porter fold | Human GLUT1 crystal structure | High; establishes non-conservation of mechanism |
| **This report — TM1 analysis** (provenance CSV/PY) | computational | refutes | Does GLT-1 carry the protonation-site Asp? | GLT-1 has **Val48** at the XylE-Asp27 position (XylE=D, STP1=D, GLUT1/4=N) | UniProt seqs, [FY]GY anchor | Medium-high; single-residue diagnostic, no wet-lab |
| **This report — paralog control** (provenance CSV) | computational/evolutionary | refutes (for GLT-1) / competing | Does coupling segregate to high-affinity paralogs? | *N. crassa* HGT-1 (Q7S0I5)=**Asp52**, HGT-2 (Q7S3Q4)=**Asp35** RETAIN the acidic residue; only low-affinity GLT-1 lost it | Intra-genome paralog comparison | Medium-high; lineage-controlled; residue-level, no electrophysiology |
| **This report — expanded 11-protein panel** (provenance CSV) | computational | qualifies | Is the Asp/neutral dichotomy systematic? | Symporters (XylE, STP1, HGT-1/-2)=acidic; uniporters GLUT1/3/5=neutral; **GLUT2 is an acidic-but-uniporter false-positive**; GLT-1=Val (non-protonatable) | Cross-family control set | Medium-high; shows diagnostic is asymmetric — *absence* of a protonatable residue is the robust signal |
| PMID 28115989 (Wang et al. 2017) | direct assay (heterologous) + mutant | qualifies/competing | GLT-1 function & system mapping | GLT-1 = **low-affinity** glucose transporter (system I); HGT-1/-2 = high-affinity; radioglucose kinetics in yeast EBY.VW4000 | *N. crassa* + yeast expression | High for low-affinity glucose uptake; proton coupling not directly assayed |
| PMID 24581151 (Li et al. 2014) | direct assay (heterologous) | supports (glucose uptake) | GLT-1 is a glucose transporter | NCU01633 characterized as glucose transporter in EBY.VW4000 | *N. crassa* | High for glucose specificity |
| PMID 33509260 (Li et al. 2021) | mutant/regulatory | supports (low-affinity role) | GLT-1 identity | Reaffirms GLT-1 = low-affinity transporter of the dual-affinity system | *N. crassa* | High |
| PMID 5573732 (Schneider & Wiley 1971) | direct assay (whole cell) | qualifies/competing | System I vs II energetics | System I Km≈25 mM (low-aff, constitutive); system II Km≈0.04 mM; only system II concentrates 3-O-MG | *N. crassa* mycelia | High; whole-cell (not protein-specific); both systems inhibited by DNP/azide (indirect energy dependence) |
| PMID 6444943 (Rand & Tatum 1980) | direct assay (whole cell) | competing | Which system is energy-coupled | Energy-requiring, concentrative general monosaccharide transport = high-affinity **system II**, not system I | *N. crassa* | High for locating active transport in system II |

---

## GO Curation Implications

- **GO:0005351 (MF, carbohydrate:proton symporter activity) — recommend: do NOT retain as an asserted/core function.** It is IBA-only, family-level, and is contradicted by the missing TM1 protonation-site residue. Options for the curator, in order of preference:
  1. **Generalize the MF** to an experimentally-safe, mechanism-agnostic term supported by the primary data — e.g., **D-glucose transmembrane transporter activity (GO:0055056)** / **glucose:proton symporter activity? NO** → prefer the non-coupled **glucose transmembrane transporter activity (GO:0005355)**. These capture the demonstrated low-affinity glucose uptake without the unsupported proton-coupling claim.
  2. If house style requires keeping the PANTHER IBA row, **retain GO:0005351 strictly as IBA** (do not promote to experimental, do not treat as core), and add the more precise experimentally-based glucose transporter MF above it.
- **Proton transmembrane transport (BP, GO:1902600 / GO:0015992) — recommend: remove / do not add.** No evidence; depends on the symport assumption that the sequence contradicts.
- **BP: carbohydrate/glucose transmembrane transport (GO:0008643 / GO:1904659) — retain** (well supported experimentally).
- **CC: membrane / plasma membrane (GO:0016020 / GO:0005886) — retain** (MFS integral membrane; plasma-membrane glucose uptake demonstrated).

Note on the seed's PANTHER argument: it is **factually correct** that PTN002362095 descends from the PTN000627328 IBD for GO:0005351 with no lineage-loss row, so the IBA annotation is *procedurally valid*. But procedural ancestry validity ≠ demonstrated mechanism; the curator should weight the protein-specific sequence and physiology evidence over an un-lost family default.

---

## Mechanistic Scope

- **Immediate molecular function (what is actually tested):** transmembrane movement of D-glucose across the plasma membrane, low affinity (system I). Established by heterologous radioglucose kinetics (PMID 28115989/24581151).
- **The disputed add-on (coupling mechanism):** whether that glucose movement is **coupled to inward H⁺ flux** (symport, concentrative, energized by the PM H⁺-ATPase gradient) versus **facilitated diffusion** (uniport, down-gradient). This is the crux — glucose *specificity* is not in question; *coupling* is.
- **Downstream / not the tested function:** GLT-1's roles in carbon catabolite signaling, cellulase regulation, and glucose-gradient sensing (PMID 33509260) are pleiotropic pathway consequences, not the transport mechanism, and should not be used to justify a symporter MF.

---

## Conflicts and Alternatives

- **Uniporter vs symporter (primary conflict).** Sequence (Val48 at the protonation site) and Sugar-Porter-family logic favor a **facilitated-diffusion uniporter**, aligning GLT-1 with low-affinity yeast HXT and mammalian GLUT rather than with H⁺-symporters. This competes directly with the IBA symporter default.
- **Whole-cell energy dependence artifact.** Schneider & Wiley (1971) found system I is *also* inhibited by azide/DNP. This could be misread as proton coupling, but uncouplers collapse membrane potential and cellular ATP and perturb *all* PM transport indirectly; it is not evidence of stoichiometric H⁺:glucose symport by GLT-1. Only system II concentrates 3-O-methylglucose.
- **System-to-gene mapping caveat.** The historical "system I/II" physiology was measured on whole mycelia (mixtures of transporters). Equating GLT-1 exactly with all of "system I" is itself an inference; the modern gene-level data (PMID 28115989) support low-affinity glucose uptake but did not isolate coupling.
- **Paralog / subfamily confusion (now with positive evidence).** PANTHER subfamily label "low affinity glucose transporter MstE" (Aspergillus) reinforces *low-affinity glucose uniport*, not symport. The high-affinity, proton-coupling-capable activity in *N. crassa* segregates to the **HGT-1/HGT-2** paralogs, which **retain the TM1 acidic residue (Asp52 / Asp35)** that GLT-1 has lost (Val48). This is a lineage-controlled contrast within one genome: the family-default symporter GO is appropriate (at the sequence level) for the high-affinity paralogs but not for GLT-1. Care is needed not to carry the paralogs' coupling determinant onto GLT-1 via family-level IBA.

---

## Knowledge Gaps

1. **No direct GLT-1 energetics assay.** Checked: no EXP GO, no electrophysiology in the retrieved literature. Matters because it is the only way to *prove* uniport vs symport. Resolve with: proteoliposome glucose flux ± ΔpH/Δψ, or two-electrode voltage clamp in *Xenopus* oocytes measuring glucose-evoked H⁺ current.
2. **Single-residue diagnostic is asymmetric.** Checked: an expanded 11-protein panel. The signal is directional: a **non-protonatable residue (GLT-1 Val48) is strong evidence against symport** (a proton donor/acceptor is physically required), whereas an **acidic residue is necessary but not sufficient** — human GLUT2 (P11168) is a bona fide uniporter yet carries Asp27 at this position (a false-positive for "symport"). GLT-1 sits on the robust side of this asymmetry (it lacks even the neutral amide of GLUT1/3/5). PMID 28617850 further cautions that multiple residues tune thermodynamics. Resolve with: full structure-based alignment / AlphaFold model + inspection of the complete proton-relay network (TM1/TM4/TM7/TM10) against XylE and GLUT1.
3. **Membrane-potential dependence of GLT-1 specifically.** Historical energy dependence is whole-cell. Resolve with: GLT-1-only heterologous system + protonophore controls.

---

## Discriminating Tests

- **Proteoliposome reconstitution** of purified GLT-1: measure glucose accumulation against a gradient with vs without an imposed ΔpH (inside-alkaline). Concentrative uptake requiring ΔpH ⇒ symport; equilibrative only ⇒ uniport. *Most decisive.*
- **Oocyte electrophysiology:** glucose-induced inward current that is H⁺-dependent ⇒ symport; electroneutral/no current ⇒ uniport.
- **Structure-guided mutagenesis:** if a symport-like acidic residue can be introduced at the Val48 position and confers H⁺ coupling, that would delimit the native mechanism.
- **Comparative bioinformatics (fast):** extend the TM1 protonation-site scan across all *N. crassa* Sugar Porter members and characterized fungal symporters/uniporters to confirm GLT-1 clusters with uniporters (partially done here for GLT-1 vs XylE/STP1/GLUT).

---

## Curation Leads (require curator verification)

- **Action change:** Downgrade/《do not assert》 **GO:0005351** on GLT-1 to IBA-only or replace with mechanism-agnostic **glucose transmembrane transporter activity (GO:0005355)** / **D-glucose transmembrane transporter activity (GO:0055056)**; **do not add proton transmembrane transport BP**.
- **Retain:** carbohydrate/glucose transmembrane transport BP (GO:0008643 / GO:1904659) and membrane CC (GO:0016020), with experimental support from PMID 28115989 / 24581151.
- **Candidate references + snippets to verify:**
  - PMID 28617850 — "the variation between an acidic residue (Asp27 in XylE) and a neutral one (Asn29 in GLUT1)…key element for their mechanistic divergence."
  - PMID 24847886 — "Structural comparison of the uniporter GLUT1 with its bacterial homologue XylE, a proton-coupled xylose symporter…"
  - PMID 5573732 — "The apparent K(m) for glucose uptake by system I and system II are 25 and 0.04 mm, respectively."
  - PMID 6444943 — "a second galactose transport activity…required energy, had a high affinity…was shown to be the same as glucose transport system II."
- **Suggested curator question:** Is there *any* GLT-1-specific proton-flux/voltage-clamp datum? If not, the symporter MF should not be a core assertion.
- **Suggested experiment:** proteoliposome ΔpH-dependence assay (see Discriminating Tests).

**Provenance artifacts:**
- `provenance/glt1_TM1_protonation_site_analysis.py` (executable) + `...analysis.csv` — core symporter/uniporter TM1 scan incl. Neurospora HGT-1/-2.
- `provenance/glt1_TM1_expanded_panel.csv` — 11-protein control panel (documents the GLUT2 acidic-but-uniporter caveat and the diagnostic's asymmetry).
- `provenance/glt1_GO_decision_table.csv` — per-term recommended curation actions.

**GO decision table (summary; leads requiring curator verification):**

| GO term | ID | Aspect | Current | Recommended action |
|---|---|---|---|---|
| carbohydrate:proton symporter activity | GO:0005351 | MF | IBA only | Do not assert as core; keep IBA-only or remove/generalize |
| D-glucose transmembrane transporter activity | GO:0055056 | MF | absent | ADD (EXP-supported, mechanism-agnostic) |
| glucose transmembrane transporter activity | GO:0005355 | MF | absent | ADD/alternative |
| proton transmembrane transport | GO:1902600 | BP | absent | Do NOT add |
| carbohydrate transport | GO:0008643 | BP | IBA | Retain |
| glucose transmembrane transport | GO:1904659 | BP | absent | Add/retain |
| membrane | GO:0016020 | CC | IBA | Retain |
| plasma membrane | GO:0005886 | CC | absent | ADD (lead) |


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)
- [OpenScientist glt1 GO decision table](openscientist_artifacts/provenance_glt1_GO_decision_table.csv)
- [OpenScientist glt1 TM1 expanded panel](openscientist_artifacts/provenance_glt1_TM1_expanded_panel.csv)
- [OpenScientist glt1 TM1 protonation site analysis](openscientist_artifacts/provenance_glt1_TM1_protonation_site_analysis.csv)