---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-26T03:03:23.063024'
end_time: '2026-08-26T03:13:33.970920'
duration_seconds: 610.91
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: human
  gene: FLG
  gene_symbol: FLG
  uniprot_accession: P20930
  taxon_id: NCBITaxon:9606
  taxon_label: Homo sapiens
  focus_type: function_assignment
  hypothesis_slug: function-hypothesis-go-0005509
  hypothesis_text: FLG has calcium ion binding (GO:0005509).
  term_context: '- Term: calcium ion binding (GO:0005509)

    - Evidence type: IEA

    - Original reference: GO_REF:0000002'
  reference_context: '- GO_REF:0000002'
  source_file: genes/human/FLG/FLG-ai-review.yaml
  source_selector: existing_annotations[5].function_hypothesis
  source_context_yaml: "term:\n  id: GO:0005509\n  label: calcium ion binding\nevidence_type:\
    \ IEA\noriginal_reference_id: GO_REF:0000002"
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
citation_count: 4
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
- **Gene directory:** FLG
- **Gene symbol:** FLG
- **UniProt accession:** P20930

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** function-hypothesis-go-0005509
- **Source file:** genes/human/FLG/FLG-ai-review.yaml
- **Source selector:** existing_annotations[5].function_hypothesis

## Seed Hypothesis

FLG has calcium ion binding (GO:0005509).

## Term and Decision Context

- Term: calcium ion binding (GO:0005509)
- Evidence type: IEA
- Original reference: GO_REF:0000002

## Reference Context

- GO_REF:0000002

## Source Context YAML

```yaml
term:
  id: GO:0005509
  label: calcium ion binding
evidence_type: IEA
original_reference_id: GO_REF:0000002
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

# FLG (Profilaggrin) Calcium Ion Binding (GO:0005509) — Hypothesis Deep Research Report

**Gene:** FLG (filaggrin / profilaggrin) · **Organism:** *Homo sapiens* (NCBITaxon:9606) · **UniProt:** [P20930](https://www.uniprot.org/uniprotkb/P20930)
**Focus type:** function_assignment · **Hypothesis slug:** function-hypothesis-go-0005509
**Seed hypothesis:** *FLG has calcium ion binding (GO:0005509).*
**Term under review:** calcium ion binding (GO:0005509) · **Evidence type:** IEA · **Original reference:** GO_REF:0000002

---

## Summary

The seed hypothesis — that FLG (profilaggrin, P20930) directly binds calcium ion (GO:0005509) — is **SUPPORTED** by convergent structural, biochemical, sequence, and evolutionary evidence. Calcium binding is a genuine, direct molecular function of the gene product, localized to the **N-terminal profilaggrin S100 "fused-type" domain**, which contains two EF-hand motifs. The single strongest piece of evidence is a **2.2 Å-resolution crystal structure of the human profilaggrin N-terminal S100 domain solved with bound calcium ions** ([PMID: 25760235](https://pubmed.ncbi.nlm.nih.gov/25760235/); PDB 4PCW). This is corroborated by curated UniProt features (two EF-hand domains and five annotated Ca²⁺-coordinating residues), matching InterPro/Pfam/PROSITE signatures, a canonical EF-hand loop sequence carrying the hallmark bidentate glutamate (Glu73), and calcium-dependent target-binding assays.

Because the current annotation rests only on an IEA (electronically inferred) code tied to GO_REF:0000002 (InterPro2GO), the appropriate curation action is **not removal but retention with an evidence upgrade** — from IEA to an experimental code (IDA) citing the crystal structure. A family-wide paralog audit of the human S100 fused-type protein (SFTP) cluster (FLG2, HRNR, RPTN, TCHH, CRNN) shows the EF-hand/S100 module and GO:0005509 are shared across the whole clade, confirming a **domain-anchored, family-consistent annotation** rather than an FLG-specific electronic misassignment or paralog carry-over.

The one nuance a curator must record is **scope**: calcium binding is a property of the **N-terminal S100/EF-hand region of the profilaggrin precursor**, not of the mature filaggrin repeat units that aggregate keratin in the cornified envelope. GO:0005509 is therefore a valid **regulatory molecular function** — accurate and directly demonstrated — but it is not FLG's single "core" barrier-forming activity. No refuting evidence was found.

---

## Key Findings

### Finding 1 — FLG/profilaggrin directly binds calcium via its N-terminal S100/EF-hand domain (GO:0005509 supported)

Profilaggrin carries at its N-terminus a **fused-type S100 domain containing two EF-hand calcium-binding motifs**, documented at three independent levels of evidence.

**Curated sequence features.** UniProt P20930 annotates two EF-hand domains (residues ~6–43 and ~49–84) and **five explicit Ca²⁺ binding-site residues** at positions 62, 64, 66, 68, and 73. These map onto matching domain signatures across every major protein-family resource: InterPro IPR002048 (EF-hand domain), IPR018247 (EF_Hand_1_Ca_BS), and IPR001751 (S100/CaBP7/8-like); Pfam PF01023 (S_100); and PROSITE PS00018/PS50222 (EF_HAND) and PS00303 (S100_CABP). The convergence of independent bioinformatic signatures on the same region is precisely the pattern expected for a real, conserved calcium-binding module — and it is exactly the InterPro2GO basis (GO_REF:0000002) for the current IEA annotation.

**Direct structural evidence.** A **2.2 Å-resolution crystal structure of the N-terminal fused-type S100 domain of human profilaggrin was solved with bound calcium ions** ([PMID: 25760235](https://pubmed.ncbi.nlm.nih.gov/25760235/)). The deposited coordinates (PDB 4PCW, residues ~1–92) contain explicit "CA" calcium ligand atoms. Direct visualization of a bound metal ion in an experimental structure is the highest tier of proof for a metal-ion-binding molecular-function annotation.

**Biochemical/functional evidence.** The same domain mediates **calcium-dependent target binding**: the profilaggrin B domain cooperates with the S100 domain to bind annexin II and keratin intermediate filaments in a calcium-dependent manner ([PMID: 32893105](https://pubmed.ncbi.nlm.nih.gov/32893105/)), and the crystallographic study additionally identified annexin II, stratifin (14-3-3σ), and HSP27 as calcium-domain targets ([PMID: 25760235](https://pubmed.ncbi.nlm.nih.gov/25760235/)). Calcium dependence of these interactions is the functional signature of a genuine EF-hand calcium sensor.

**Historical characterization.** The original characterization of the human epidermal profilaggrin gene identified "an 81-residue segment which shows significant homology to the S-100 family of EF hand-containing calcium-binding proteins" ([PMID: 1429717](https://pubmed.ncbi.nlm.nih.gov/1429717/)); follow-up work confirmed "an N-terminal S100-like Ca²⁺-binding domain containing two EF-hands" conserved across human, mouse, and rat ([PMID: 12230510](https://pubmed.ncbi.nlm.nih.gov/12230510/)).

Taken together, structural, biochemical, sequence, and evolutionary lines of evidence all converge: **GO:0005509 is a directly demonstrated molecular function of the FLG gene product.**

### Finding 2 — EF-hand 2 is a canonical Ca²⁺-binding loop, and the annotation is family-consistent (no paralog misassignment)

A residue-level sequence analysis of P20930 confirms the annotation maps to a **textbook canonical EF-hand loop** rather than a generic domain guess. The 12-residue loop at residues **62–73** matches the canonical EF-hand coordination consensus:

| Loop position | Residue | Canonical role |
|---|---|---|
| 1 (X) | Asp62 | Side-chain O coordinates Ca²⁺ |
| 3 (Y) | Asp64 | Side-chain O coordinates Ca²⁺ |
| 5 (Z) | Asn66 | Side-chain O coordinates Ca²⁺ |
| 7 (−Y) | Lys68 | Backbone carbonyl coordinates Ca²⁺ |
| 9 (−X) | Asp70 | Via bridging water |
| 12 (−Z) | **Glu73** | **Bidentate glutamate — the EF-hand hallmark** |

The **bidentate glutamate at position 12 (Glu73)** is the single most diagnostic feature of a functional canonical EF-hand, and it coincides exactly with the UniProt-annotated Ca²⁺ sites (62, 64, 66, 68, 73). EF-hand 1 (residues ~6–43) is the **S100-type non-canonical/"pseudo" EF-hand** that coordinates calcium mainly through backbone carbonyls and carries no discrete annotated Ca²⁺ sites — exactly the architecture expected for an S100 domain, which pairs one canonical and one pseudo EF-hand.

A **paralog audit** of the human S100 fused-type protein (SFTP) family — FLG (P20930), FLG2 (Q5D862), HRNR (Q86YZ3), RPTN (Q6XPR3), TCHH (Q07283), CRNN (Q9UBG3) — shows that **all members carry an N-terminal EF-hand/S100 module and all are annotated with GO:0005509**. Rather than a red flag for over-annotation, this is evidence *for* correctness: the calcium-binding module is a conserved, defining feature of the entire SFTP clade, the domain is authentically present in FLG's own sequence, and FLG additionally has a direct crystal structure. There is therefore no paralog carry-over risk here.

---

## Mechanistic Model / Interpretation

Profilaggrin is a large, highly repetitive precursor of the epidermal differentiation complex, with a **regulatory N-terminus** separated from a **structural repeat body**:

```
   Profilaggrin (P20930)
   ┌───────────────────────────────────────────────────────────────┐
   │  N-terminal region          │   Filaggrin repeats (10–12)      │
   │  ┌───────────┬───────────┐  │   [FLG][FLG][FLG]...[FLG]        │
   │  │ S100 "A"  │  "B"      │  │                                  │
   │  │ domain    │  domain   │  │   keratin-aggregating units      │
   │  │ EF-hand1  │           │  │   (mature filaggrin monomers)    │
   │  │ (pseudo)  │           │  │                                  │
   │  │ EF-hand2  │           │  │                                  │
   │  │ 62–73 CA  │           │  │                                  │
   │  └───────────┴───────────┘  │                                  │
   │        ▲                     │                                  │
   │   Ca²⁺ binding (GO:0005509)  │   Ca²⁺ binding NOT here          │
   └───────────────────────────────────────────────────────────────┘
        │                                    │
        ▼                                    ▼
   Ca²⁺-dependent binding of            Proteolytic release of
   annexin II/A2, keratin IFs,          filaggrin monomers →
   stratifin (14-3-3σ), HSP27;          keratin bundling in the
   nuclear/cytoplasmic sorting          cornified envelope; later
   of the N-terminal peptide            breakdown to NMF amino acids
```

The **molecular function under test (GO:0005509)** is localized entirely to the N-terminal S100 domain, and specifically to canonical EF-hand 2. Calcium binding here acts as a **conformational/regulatory switch**: it modulates calcium-dependent protein–protein interactions and the nuclear-versus-cytoplasmic distribution of the cleaved profilaggrin N-terminal peptide — the classic mode of action of an S100/EF-hand calcium sensor.

Critically, this function is **upstream of and distinct from** the barrier-forming role for which FLG is best known. The mature filaggrin repeats that bundle keratin, and their eventual proteolysis into natural moisturizing factor (NMF), do **not** depend on this EF-hand — they are downstream structural/processing events. A curator should treat GO:0005509 as a **directly supported regulatory MF** while recognizing it does not describe the protein's principal barrier phenotype.

---

## Evidence Base / Evidence Matrix

| Citation | Evidence type | Direction | Claim tested | Key finding | Context | Confidence / limits |
|---|---|---|---|---|---|---|
| [PMID: 25760235](https://pubmed.ncbi.nlm.nih.gov/25760235/) (Bunick et al. 2015); **PDB 4PCW** | Structural (X-ray) + biochem | **Supports** | Does the profilaggrin N-terminus bind Ca²⁺? | 2.2 Å crystal structure of human profilaggrin S100 domain (~res 1–92) **with bound Ca ligands** ("CA" nonpolymer confirmed); identifies annexin II, stratifin, HSP27 targets | Human, recombinant N-terminal domain | **High**; domain-level, isolated construct not full-length |
| [PMID: 32893105](https://pubmed.ncbi.nlm.nih.gov/32893105/) (Hinbest et al. 2020) | Biochemical / interaction | **Supports** (functional) | Is Ca²⁺ binding functionally relevant? | S100 + B domains bind annexin II & keratin IFs **in a calcium-dependent manner** | Human profilaggrin AB domain | **High** for function; indirect for stoichiometric Ca binding |
| [PMID: 12230510](https://pubmed.ncbi.nlm.nih.gov/12230510/) (Pearton et al. 2002) | Sequence / functional / evolutionary | **Supports** | Is the N-terminus a two-EF-hand Ca²⁺ module? | "N-terminal S100-like Ca²⁺-binding domain containing two EF-hands"; conserved human/mouse/rat; separate from repeats | Human/mouse/rat | **High**; establishes domain vs. repeat distinction |
| [PMID: 1429717](https://pubmed.ncbi.nlm.nih.gov/1429717/) (Presland et al. 1992) | Gene characterization / homology | **Supports** | Does FLG encode an S100/EF-hand domain? | N-terminal 81-aa segment homologous to S-100 EF-hand Ca-binding proteins | Human FLG gene | **High** for domain identity; predates direct binding proof |
| UniProt P20930 (curated) | Review/database | **Supports** | Are Ca-binding residues annotated? | Two EF-hand domains; five Ca²⁺ sites (62, 64, 66, 68, 73) | Human | **High** as orientation; backed by primary structure |
| InterPro IPR002048/IPR018247/IPR001751; Pfam PF01023; PROSITE PS00018/PS50222/PS00303 | Computational/domain | **Supports** | Basis of IEA call | EF-hand + S100/Ca-binding signatures present | Cross-species | This is the GO_REF:0000002 source; now corroborated experimentally |
| This work — EF-hand loop analysis of P20930 (62–73) | Computational (sequence) | **Supports** | Is the annotated loop a canonical Ca²⁺ site? | Canonical 12-residue loop with bidentate **Glu73**; matches all 5 UniProt Ca sites; EF-hand 1 = S100 pseudo EF-hand | Human, in silico | **High**; sequence-level, consistent with structure |
| This work — SFTP paralog audit | Computational (comparative) | **Qualifies (rules out artifact)** | Is GO:0005509 a paralog carry-over? | FLG, FLG2, HRNR, RPTN, TCHH, CRNN all carry the module + GO:0005509; domain authentically in FLG | Human family | **High**; rules out paralog over-annotation |

**No refuting evidence was found.** Every line of evidence supports the calcium-binding function or clarifies its scope.

---

## GO Curation Implications

**Recommended action (lead requiring curator verification): RETAIN GO:0005509 and UPGRADE the evidence from IEA (GO_REF:0000002) to an experimental code (IDA).**

- **Ontology aspect:** GO:0005509 is a **Molecular Function (MF)** term; the evidence directly supports an MF annotation.
- **Retain vs. remove:** **Retain** — the term is biologically correct and directly demonstrated.
- **Generalize vs. specialize:** No change to granularity. "Calcium ion binding" is the appropriate MF term for an EF-hand protein; there is no validated, more-specific child term that better describes the demonstrated activity.
- **Evidence upgrade:** The IEA/GO_REF:0000002 code understates the evidence. An **IDA** annotation with reference [PMID: 25760235](https://pubmed.ncbi.nlm.nih.gov/25760235/) is justified by the calcium-bound crystal structure; the calcium-dependent interactions from [PMID: 32893105](https://pubmed.ncbi.nlm.nih.gov/32893105/) provide supporting functional evidence.
- **Core vs. non-core framing:** Record as a **valid regulatory MF of the N-terminal profilaggrin S100 domain**, explicitly noting it is *not* the mature filaggrin keratin-aggregating activity. Do not present it as FLG's single core barrier function.
- **"protein binding" avoidance:** Not applicable — the recommendation is the informative EF-hand-specific term GO:0005509.

**GO decision table**

| Field | Current | Recommended |
|---|---|---|
| Term | GO:0005509 calcium ion binding | GO:0005509 calcium ion binding (unchanged) |
| Aspect | MF | MF |
| Evidence code | IEA | **IDA** (upgrade) |
| Reference | GO_REF:0000002 | **PMID:25760235** (+ PMID:32893105 supporting) |
| Action | — | **RETAIN + UPGRADE** |
| Scope note | none | "Property of N-terminal profilaggrin S100/EF-hand domain (EF-hand 2, residues 62–73); regulatory, not the mature filaggrin repeat function." |

---

## Mechanistic Scope

**Immediate molecular function tested:** Direct coordination of Ca²⁺ ions by the EF-hand loop(s) of the N-terminal profilaggrin S100 domain — a chemical binding event demonstrated crystallographically.

**Directly attributable to the gene product:**
- Ca²⁺ coordination by canonical EF-hand 2 (residues 62–73, bidentate Glu73).
- Calcium-dependent binding to annexin II/A2, keratin intermediate filaments, stratifin (14-3-3σ), and HSP27.
- Calcium-modulated nuclear/cytoplasmic distribution of the profilaggrin N-terminal peptide.

**Downstream / not the direct MF being annotated (do not conflate with GO:0005509):**
- Proteolytic processing of profilaggrin into filaggrin monomers.
- Keratin filament aggregation and cornified envelope formation by mature filaggrin repeats.
- Breakdown of filaggrin to natural moisturizing factor (NMF) and skin hydration.
- Barrier dysfunction phenotypes (ichthyosis vulgaris, atopic dermatitis) from FLG **loss-of-function** — disease manifestations, not evidence about the calcium-binding MF.

The distinction matters: GO:0005509 is supported by *direct positive assays on the N-terminal domain*, independent of the loss-of-function barrier phenotypes that dominate the FLG disease literature.

---

## Conflicts and Alternatives

No evidence conflicts with the seed hypothesis. The candidate alternatives were each examined and ruled out:

- **Paralog confusion / over-annotation:** Ruled out. The EF-hand/S100 module and GO:0005509 are shared across the entire SFTP family, and FLG itself has a direct crystal structure — so this is not a term propagated onto FLG from a better-characterized relative.
- **In-vitro-only artifact:** Partially applicable but not disqualifying. The crystal structure uses an isolated recombinant N-terminal domain and the calcium-dependent interactions are in vitro; however, cross-species conservation and canonical loop geometry argue for physiological relevance, and in vitro Ca²⁺ binding is exactly what an MF binding term encodes.
- **Isoform/region specificity:** A real, important qualifier rather than a conflict. Calcium binding is restricted to the N-terminal S100 domain; the mature filaggrin repeats do not bind calcium. Capture as a scope note.
- **Database carry-over bias:** The IEA rests on InterPro2GO (GO_REF:0000002), but the underlying domain call is corroborated by primary structural data, so the electronic annotation is correct rather than spurious.

---

## Limitations and Knowledge Gaps

| Gap | What was checked | Why it matters | What would resolve it |
|---|---|---|---|
| Ca²⁺ affinity / stoichiometry of full-length profilaggrin | Structure/biochem cover the isolated N-terminal domain (PDB 4PCW ligand + residue range) | Confirms physiological Ca binding in cellular context; distinguishes structural vs. regulatory site | ITC / equilibrium dialysis / Tb³⁺ luminescence on larger constructs; in situ Ca imaging |
| Which EF-hand carries physiological load | Sequence: EF-hand 2 canonical (Glu73), EF-hand 1 = S100 pseudo | Assigns the functionally relevant site | Site-directed mutagenesis of each loop |
| In vivo causal link to processing/localization | Epidermal Ca gradient known; direct causal test not in reviewed papers | Ties EF-hand occupancy to physiological outcome | EF-hand loss-of-binding mutant (Glu73→Gln) in keratinocyte models |
| Human isoform/CNV variation | FLG repeat number is polymorphic (10–12); N-terminus invariant | N-terminal Ca domain unaffected by repeat CNV | Confirmed conserved; low concern |

None of these gaps threatens the *existence* of the calcium-binding function; they concern its quantitative and physiological parameters.

---

## Discriminating Tests

1. **EF-hand point mutant (Glu73Gln / Glu73Ala):** abolish bidentate coordination; assay loss of Ca²⁺ binding (Tb³⁺ luminescence, ITC) and loss of calcium-dependent annexin II/keratin binding. A clean loss-of-binding phenotype directly ties the annotated residues to the function.
2. **Isothermal titration calorimetry (ITC)** of the wild-type N-terminal domain with Ca²⁺: quantify Kd and stoichiometry (expect ~1 Ca²⁺ per canonical EF-hand).
3. **Comparative structural confirmation:** re-examine PDB 4PCW coordination sphere; optionally compare apo vs. holo conformations for the calcium-induced conformational change typical of S100 sensors.
4. **Keratinocyte differentiation assay** across the physiological calcium gradient with wild-type vs. EF-hand-dead profilaggrin N-terminus, reading out nuclear/cytoplasmic partitioning and processing.
5. **Comparative annotation audit** across SFTP paralogs to confirm consistent, domain-anchored GO:0005509 assignments.

---

## Proposed Follow-up Experiments / Actions (Curation Leads)

All items below are **leads requiring curator verification.**

- **RETAIN** GO:0005509 (calcium ion binding, MF) for FLG/P20930 — biologically correct and specific.
- **UPGRADE** the evidence code from IEA/GO_REF:0000002 to **IDA**, primary reference **[PMID: 25760235](https://pubmed.ncbi.nlm.nih.gov/25760235/)**.
  - *Verify snippet:* "we determined a 2.2 Å-resolution crystal structure of the N-terminal fused-type S100 domain of human profilaggrin with bound calcium ions." Structure = **PDB 4PCW** (RCSB confirms bound "CA" calcium ligand).
- **ADD supporting reference** [PMID: 32893105](https://pubmed.ncbi.nlm.nih.gov/32893105/) for calcium-dependent function.
  - *Verify snippet:* "Profilaggrin B domain cooperates with the S100 domain to bind annexin II and keratin intermediate filaments in a calcium-dependent manner."
- **ADD historical/supporting references:** [PMID: 1429717](https://pubmed.ncbi.nlm.nih.gov/1429717/) ("...significant homology to the S-100 family of EF hand-containing calcium-binding proteins") and [PMID: 12230510](https://pubmed.ncbi.nlm.nih.gov/12230510/) ("...N-terminal S100-like Ca²⁺-binding domain containing two EF-hands").
- **ADD scope note:** calcium binding is a property of the **N-terminal profilaggrin S100/EF-hand domain (EF-hand 2, residues 62–73; hallmark bidentate Glu73)**, functioning as a regulatory calcium sensor — *not* the mature filaggrin keratin-aggregating repeats.
- **Suggested curator question:** Should the review additionally capture the specific calcium-dependent interactions (annexin II/A2, stratifin/14-3-3σ, HSP27) as separate IPI annotations, and/or mark this MF as non-core relative to keratin filament aggregation? (Recommendation: retain as a valid secondary/regulatory MF.)
- **Suggested experiments (for gaps):** ITC/Tb³⁺ titration for affinity/stoichiometry; Glu73 mutant to link annotated residues to function in a keratinocyte model.

---

## Conclusion

The IEA annotation of **calcium ion binding (GO:0005509)** on FLG is **correct and, if anything, under-credited**. It is supported by a calcium-bound crystal structure, calcium-dependent functional assays, canonical EF-hand sequence features with the hallmark bidentate Glu73, convergent InterPro/Pfam/PROSITE signatures, and a family-wide paralog audit that rules out over-annotation. The recommended curation action is to **retain the term and upgrade its evidence from IEA to an experimental (IDA) code**, while adding a scope note that the function belongs to the N-terminal profilaggrin S100 domain and is regulatory rather than the mature filaggrin barrier activity.

---

*Provenance:* UniProt P20930 feature/xref query executed via the public REST API (two EF-hand domains 6–43 & 49–84; Ca²⁺ sites 62/64/66/68/73; InterPro IPR001751/IPR002048/IPR018247, Pfam PF01023, PROSITE PS00303). EF-hand loop consensus and SFTP paralog audit performed in-house from sequence. PDB 4PCW cross-referenced from UniProt; RCSB confirms bound "CA" ligand. Literature via PubMed.


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)