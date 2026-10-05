---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-26T03:03:46.147759'
end_time: '2026-08-26T03:20:03.284753'
duration_seconds: 977.14
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: human
  gene: FLG
  gene_symbol: FLG
  uniprot_accession: P20930
  taxon_id: NCBITaxon:9606
  taxon_label: Homo sapiens
  focus_type: function_assignment
  hypothesis_slug: function-hypothesis-go-0046914
  hypothesis_text: FLG has transition metal ion binding (GO:0046914).
  term_context: '- Term: transition metal ion binding (GO:0046914)

    - Evidence type: IEA

    - Original reference: GO_REF:0000002'
  reference_context: '- GO_REF:0000002'
  source_file: genes/human/FLG/FLG-ai-review.yaml
  source_selector: existing_annotations[6].function_hypothesis
  source_context_yaml: "term:\n  id: GO:0046914\n  label: transition metal ion binding\n\
    evidence_type: IEA\noriginal_reference_id: GO_REF:0000002"
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
- **Hypothesis slug:** function-hypothesis-go-0046914
- **Source file:** genes/human/FLG/FLG-ai-review.yaml
- **Source selector:** existing_annotations[6].function_hypothesis

## Seed Hypothesis

FLG has transition metal ion binding (GO:0046914).

## Term and Decision Context

- Term: transition metal ion binding (GO:0046914)
- Evidence type: IEA
- Original reference: GO_REF:0000002

## Reference Context

- GO_REF:0000002

## Source Context YAML

```yaml
term:
  id: GO:0046914
  label: transition metal ion binding
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

# FLG (P20930) — Transition Metal Ion Binding (GO:0046914): Hypothesis Review

**Focus type:** function_assignment · `existing_annotations[6].function_hypothesis`
**Seed hypothesis:** FLG has transition metal ion binding (GO:0046914)
**Term/evidence context:** GO:0046914 "transition metal ion binding", IEA, GO_REF:0000002 (InterPro2GO)
**Gene:** human FLG / Filaggrin / UniProt **P20930** (profilaggrin, 4,061 aa)

---

## Summary

The IEA annotation of FLG to **transition metal ion binding (GO:0046914)** is an **over-annotation** — a family-level InterPro2GO carry-over rather than a member-specific, experimentally supported molecular function of the filaggrin gene product. It should be treated as **non-core** and is a strong candidate for **removal or explicit flagging as unsupported** in the gene review. The annotation traces to a single InterPro signature, **IPR034325 "S-100"**, which is the only signature on P20930 mapped to GO:0046914 via the automated InterPro2GO pipeline (GO_REF:0000002). That entry's own description hedges — "*Many* S100 proteins have been found to bind transition metals, such as Zn²⁺ and Cu²⁺" — a statement about the family as a whole that is then applied uniformly to every S100-domain-containing member regardless of individual ligand chemistry.

Three independent lines of direct and comparative evidence converge to refute a real metal function. First, the **crystal structure of the profilaggrin N-terminal fused-type S100 domain** (PDB **4PCW**, 2.2 Å; [PMID: 25760235](https://pubmed.ncbi.nlm.nih.gov/25760235/)) was solved **with bound calcium ions** and functions through hydrophobic dimer-interface pockets that mediate protein–protein interactions (annexin II, stratifin/14-3-3σ, HSP27); a HETATM audit of the deposited coordinates finds **8 calcium atoms and zero transition-metal atoms**. Second, a **residue-level audit** shows the domain lacks the ligand chemistry that all characterized metal-binding S100 proteins use: only **2 histidines (His60, His65) and zero cysteines** in residues 1–91, versus the canonical His₃Asp/His₄–His₆ or Cys-cluster motifs required. Third, a **geometric analysis** confirms the two histidines lie 8–15 Å from any calcium site and cannot cluster to build a metal motif.

Finally, a **comparative annotation audit** demonstrates the artifact directly: all six human S100-fused-type structural proteins (FLG, TCHH, HRNR, RPTN, CRNN, FLG2) uniformly carry GO:0046914 as IEA:InterPro with no member-specific metal evidence, whereas the genuine transition-metal-binding S100 proteins (S100A7, S100A8, S100A9, S100B) instead carry the **specific, experimentally-backed child term GO:0008270 (zinc ion binding)** with NAS/TAS/IDA evidence. The most important caveat is that no study has *directly* assayed the profilaggrin S100 domain for Zn/Cu binding, so this is a strong structure-plus-sequence-plus-annotation inference rather than a direct negative experiment. The well-supported molecular function of this domain is **calcium ion binding (GO:0005509)** plus calcium-dependent protein binding.

**Verdict: Over-annotated (refuted as a direct, core function).**

---

## Key Findings

### Finding 1 — The GO:0046914 annotation is a single-signature, family-level InterPro over-annotation

The transition-metal-binding annotation on P20930 does not originate from any experiment on filaggrin or profilaggrin. It is produced automatically by the **InterPro2GO mapping (GO_REF:0000002)** from exactly one signature: **IPR034325 "S-100"**, a domain-level entry that is the *only* signature on the protein linked to GO:0046914. The InterPro entry's own text makes a family-generalizing statement — "Many S100 proteins have been found to bind transition metals, such as Zn²⁺ and Cu²⁺" — which the pipeline applies to every protein containing an S-100 domain, without regard to whether that individual member retains the necessary ligand residues.

Against this generic inference stands the **direct experimental characterization** of the domain. The profilaggrin N-terminal fused-type S100 domain was crystallized at 2.2 Å (PDB 4PCW) **with bound calcium ions** ([PMID: 25760235](https://pubmed.ncbi.nlm.nih.gov/25760235/)). Functionally, the domain operates as a **dimer with hydrophobic pockets that mediate protein–protein interactions** — its characterized partners are annexin II, stratifin (14-3-3σ), and HSP27. No zinc, copper, or other transition-metal binding was reported.

A computed sequence audit of the S100 domain (residues ~1–91) reinforces this: the domain contains **only 2 histidines (His60, His65)**, both located in the EF-hand-2 calcium loop/helix IV region, and **zero cysteines** across the entire N-terminal 212 residues. Canonical S100 transition-metal sites require either a **His₃Asp / His₄–His₆ cluster** (the "His-Zn" group; [PMID: 20306096](https://pubmed.ncbi.nlm.nih.gov/20306096/), [PMID: 23276281](https://pubmed.ncbi.nlm.nih.gov/23276281/)) or **cysteine ligands** (the "Cys-Zn" group; [PMID: 20306096](https://pubmed.ncbi.nlm.nih.gov/20306096/)) at the dimer interface. Profilaggrin's S100 domain possesses **neither**. UniProt's curated binding-site residues for the domain (positions 62, 64, 66, 68, 73 = Asp, Asp, Asn, Lys, Glu) are the **canonical EF-hand calcium ligands**, not metal-cluster residues.

### Finding 2 — Comparative paralog and structural audit confirms systematic family over-annotation

Two complementary audits confirm the annotation is a family artifact. A **direct HETATM audit of PDB 4PCW** finds **8 Ca atoms and 0 atoms of any transition metal** (no Zn/Cu/Mn/Fe/Ni); the only heteroatoms are calcium, a PEG fragment (2PE), and ordered waters. The structure that *defines* this domain's biophysics contains no transition metal.

A **paralog audit** shows that all six human S100-fused-type proteins carry GO:0046914 as IEA:InterPro, and none carries member-specific metal evidence — whereas the bona fide transition-metal-binding S100 proteins do not use the generic parent term at all, but the specific experimental child term GO:0008270 (zinc ion binding):

| Protein (UniProt) | Class | Real metal binder? | Metal GO term | Evidence |
|---|---|---|---|---|
| FLG / profilaggrin (P20930) | S100 fused-type | No; lacks ligands | GO:0046914 (generic) | IEA:InterPro |
| TCHH trichohyalin (Q07283) | S100 fused-type | No member-specific evidence | GO:0046914 | IEA:InterPro |
| HRNR hornerin (Q86YZ3) | S100 fused-type | No member-specific evidence | GO:0046914 | IEA:InterPro |
| RPTN repetin (Q6XPR3) | S100 fused-type | No member-specific evidence | GO:0046914 | IEA:InterPro |
| CRNN cornulin (Q9UBG3) | S100 fused-type | No member-specific evidence | GO:0046914 | IEA:InterPro |
| FLG2 filaggrin-2 (Q5D862) | S100 fused-type | No member-specific evidence | GO:0046914 | IEA:InterPro |
| S100A7 psoriasin (P31151) | Soluble S100 | **Yes** (Zn/Cu) | **GO:0008270** | NAS |
| S100A8 (P05109) | Soluble S100 (calprotectin) | **Yes** (Zn/Mn) | **GO:0008270** | TAS |
| S100A9 (P06702) | Soluble S100 (calprotectin) | **Yes** (Zn/Mn) | **GO:0008270** | TAS |
| S100B (P04271) | Soluble S100 | **Yes** (Zn) | **GO:0008270** | IDA |

Because GO:0008270 is an `is_a` child of GO:0046914, a **specific experimental term supersedes the generic IEA parent** under standard GO annotation practice. FLG displays only the generic IEA parent because it has **no experimental metal annotation to specialize it** — the fingerprint of automated propagation rather than curated function.

### Finding 3 — Structural geometry seals it: the two histidines cannot form a metal site

A coordinate-level geometric analysis of PDB 4PCW (four chains in the asymmetric unit) tested whether the domain's histidines could plausibly build a transition-metal site. The only resolved histidines are **His59 and His64** (PDB numbering; = UniProt His60/His65). Their imidazole nitrogen atoms lie **8–15 Å from the nearest bound Ca²⁺**, confirming they are not part of the EF-hand calcium sites.

Testing for a shared metal-coordination cluster found **no pair of distinct histidines within the ~3.5–5 Å required to jointly coordinate one metal**, except a single marginal His59–His59 cross-contact at ~5.2 Å that is a crystal-packing/tetramer contact rather than a functional site. All His64 pairs are >6 Å apart. There is **no cluster of ≥3 histidines** available to construct the canonical His₃Asp or His₄ S100 transition-metal motif. Geometry, not just sequence composition, excludes a metal site.

---

## Mechanistic Model / Interpretation

The evidence separates **the real function of the domain** from **the artifact of its annotation**:

```
   InterPro2GO pipeline (GO_REF:0000002, IEA)
                 │
                 ▼
   IPR034325 "S-100" domain signature
   ("Many S100 proteins bind transition metals...")
                 │  applied uniformly to ALL members
     ┌───────────┼───────────┬───────────┬───────────┬──────────┐
     ▼           ▼           ▼           ▼           ▼          ▼
   FLG         TCHH        HRNR        RPTN        CRNN       FLG2     ← all inherit GO:0046914 (IEA)
  (P20930)                                                             ← none has member-specific metal evidence

   ── vs ──

   Genuine metal-binding S100s (S100A7 / A8 / A9 / B)
     → carry SPECIFIC experimental term GO:0008270 (zinc ion binding)
       via His3Asp / His4–His6 interfacial clusters or Cys ligands
```

What FLG's S100 domain actually does (direct evidence, PDB 4PCW):

```
  Profilaggrin N-terminal S100 domain
        │
        ├── binds CALCIUM via EF-hand ligands (D62,D64,N66,K68,E73)  → GO:0005509
        ├── forms a homodimer with hydrophobic binding pockets
        └── engages protein partners: annexin II, 14-3-3σ, HSP27,     → Ca²⁺-dependent
            keratin filaments (cooperates with B domain; PMID 32893105)  protein binding

  Ligand inventory of residues 1–91:  His × 2 (His60, His65), Cys × 0
  Requirement for an S100 metal site:  His3Asp / His4–His6 cluster OR Cys ligands
  ⇒ MISSING → no transition-metal site
```

The domain's biology is **calcium-sensing and calcium-dependent protein scaffolding** in granular-layer keratinocytes, supporting epidermal barrier function. The "transition metal ion binding" label is a **downstream consequence of automated family annotation**, not a molecular activity of the gene product — precisely the frequency-biased, paralog-driven over-annotation that hypothesis-level review is designed to catch.

---

## Evidence Base

| Citation | Evidence type | Direction | Claim tested | Key finding | Context | Confidence / limitations |
|---|---|---|---|---|---|---|
| [PMID: 25760235](https://pubmed.ncbi.nlm.nih.gov/25760235/) | Direct structural (X-ray, PDB 4PCW) | Refutes | Does the profilaggrin S100 domain bind transition metals? | 2.2 Å structure solved **with bound calcium**; dimer with hydrophobic pockets binding annexin II, 14-3-3σ, HSP27; no Zn/Cu | Human profilaggrin N-terminal S100 domain | High; Zn/Cu not explicitly tested |
| [PMID: 32893105](https://pubmed.ncbi.nlm.nih.gov/32893105/) | Structural / biochemical | Qualifies (real function) | Function of the S100 fused-type AB domain | AB domain binds annexin II & keratin in a **calcium-dependent** manner via exposed cationic surface; higher pocket hydrophobicity than soluble S100s | Human profilaggrin, keratinocytes | High |
| [PMID: 20306096](https://pubmed.ncbi.nlm.nih.gov/20306096/) | Review / structural (X-ray survey) | Qualifies (mechanism) | What ligands do metal-binding S100s use? | His-Zn group = **3 His + Asp**; Cys-Zn group = interfacial Cys; profilaggrin S100 has neither | S100 family X-ray structures | Review-level but mechanistically authoritative |
| [PMID: 23276281](https://pubmed.ncbi.nlm.nih.gov/23276281/) | Direct assay (Mn/Zn) | Qualifies (mechanism) | Architecture of the S100 transition-metal site | High-affinity Mn(II) site is a **His₄ motif at the dimer interface**, Ca-dependent | Human calprotectin S100A8/A9 | High; defines the motif FLG lacks |
| [PMID: 27541598](https://pubmed.ncbi.nlm.nih.gov/27541598/) | Direct assay (XAS) | Qualifies (mechanism) | Zn coordination in an S100 | Zn-His₆ hexahistidine motif at dimer interface binds Zn(II) | Human calprotectin | High; paralog, His-rich |
| [PMID: 23431180](https://pubmed.ncbi.nlm.nih.gov/23431180/) | Direct assay / structural | Qualifies (contrast) | Molecular basis of S100 metal sequestration | Six-histidine site from dimer asymmetry sequesters Mn(II) for nutritional immunity | Calprotectin, antimicrobial | High |
| [PMID: 18359862](https://pubmed.ncbi.nlm.nih.gov/18359862/) | Direct assay | Qualifies (analogy) | Can EF-hand proteins bind Zn via His? | Calbindin D28k binds Zn²⁺ via His80; single His can contribute | Calbindin (not S100-fused) | Moderate; FLG's His are Ca-loop residues far from any cluster |
| InterPro IPR034325 + GO_REF:0000002 | Computational / database | Competing (annotation source) | Basis of GO:0046914 on FLG | Sole signature mapping FLG→GO:0046914; description is a "Many S100 proteins" family generalization | InterPro2GO | This *is* the annotation origin; family-level |
| Computed residue audit (this run) | Computational (sequence) | Refutes | Does FLG's S100 domain have metal ligands? | S100 domain (1–91): 2 His (60,65), 0 Cys; EF-hand2 Ca ligands = D,D,N,K,E | UniProt P20930 | High for absence of canonical ligands |
| Computed HETATM audit (this run) | Structural (PDB 4PCW) | Refutes | Are transition metals present in the structure? | 8 Ca, 0 Zn/Cu/Mn/Fe/Ni (only Ca + PEG 2PE + waters) | Crystallized profilaggrin S100 domain | High; reflects crystallization conditions |
| Computed paralog audit (this run) | Computational (comparative) | Competing/refutes | Is GO:0046914 member-specific or family carry-over? | All 6 SFTP paralogs carry GO:0046914 IEA; true binders carry GO:0008270 (NAS/TAS/IDA) | Human S100 family | High; diagnostic of over-annotation |
| Computed His-geometry test (this run) | Structural (PDB 4PCW coords) | Refutes | Do the S100 His form a metal cluster? | His59/His64 sit 8–15 Å from Ca and do not cluster (no ≥3-His site) | 4-chain profilaggrin S100 crystal | High |

**How the literature fits together.** The one structural paper on the FLG gene product itself ([PMID: 25760235](https://pubmed.ncbi.nlm.nih.gov/25760235/)) shows calcium, not transition metal, and a protein-interaction function — the direct refutation. The biochemical follow-up ([PMID: 32893105](https://pubmed.ncbi.nlm.nih.gov/32893105/)) reinforces a calcium-dependent protein-scaffolding role. The calprotectin and S100-survey papers ([PMID: 20306096](https://pubmed.ncbi.nlm.nih.gov/20306096/), [PMID: 23276281](https://pubmed.ncbi.nlm.nih.gov/23276281/), [PMID: 27541598](https://pubmed.ncbi.nlm.nih.gov/27541598/), [PMID: 23431180](https://pubmed.ncbi.nlm.nih.gov/23431180/)) define the exact His/Cys ligand chemistry that real S100 metal-binders use and that FLG's domain provably lacks. The calbindin paper ([PMID: 18359862](https://pubmed.ncbi.nlm.nih.gov/18359862/)) is the only entry hinting that isolated His residues *can* coordinate Zn — a weak analogy that does not apply given FLG's dispersed, calcium-loop histidines.

---

## GO Curation Implications

**Lead (requires curator verification): remove or flag GO:0046914 on FLG as an unsupported InterPro2GO family over-annotation; do not promote it to a reviewed molecular-function annotation.**

| GO term | Aspect | Current | Evidence status | Recommended action |
|---|---|---|---|---|
| **GO:0046914** transition metal ion binding | MF | IEA:InterPro (GO_REF:0000002) | No member-specific evidence; contradicted by structure (Ca only in 4PCW), sequence (0 Cys, 2 dispersed His), geometry (no His cluster), and annotation pattern (family carry-over) | **Remove / treat as non-core** |
| **GO:0005509** calcium ion binding | MF | IEA:InterPro | Directly supported by Ca-bound structure 4PCW (PMID 25760235) | **Retain**; candidate to upgrade to structure-backed evidence |
| calcium-dependent protein binding (e.g. GO:0048306) | MF | not annotated | Supported by annexin II / 14-3-3σ / HSP27 / keratin binding (PMID 25760235, 32893105) | **Consider adding** (more informative than bare "protein binding") |
| GO:0008270 zinc ion binding | MF | not annotated | No evidence for FLG (this is the term real S100 binders carry) | **Do not add** |

- The term is **MF** aspect but derives from a **family-level InterPro signature** whose GO mapping reflects that *some* S100 proteins bind Zn/Cu — not that filaggrin does.
- The same removal/flag rationale should be considered for the paralogous IEA annotations on TCHH, HRNR, RPTN, CRNN, and FLG2 — this is a **systematic InterPro2GO family artifact**, and correcting FLG alone leaves the family inconsistent. The mapping IPR034325 → GO:0046914 is itself a candidate for InterPro2GO refinement.

---

## Mechanistic Scope

**Immediate molecular function under test:** direct coordination of a transition-metal ion (Zn²⁺/Cu²⁺/Mn²⁺/Fe) by the FLG gene product — necessarily via the N-terminal S100 domain, the only region with a candidate metal architecture.

- **Direct gene-product activity that IS supported:** Ca²⁺ binding by the N-terminal S100 (A) domain and calcium-modulated protein–protein interactions (annexin II, 14-3-3σ, HSP27, keratin) that regulate profilaggrin processing and cornified-envelope assembly.
- **What GO:0046914 asserts but is NOT demonstrated:** a folded, sequence-defined transition-metal coordination site on the profilaggrin gene product.
- **Downstream / not the tested function:** Filaggrin's canonical barrier role (proteolysis of profilaggrin into monomers, keratin aggregation, natural moisturizing factor generation) is a downstream processing pathway, not the S100 domain's metal chemistry. Serum zinc/selenium associations with atopic dermatitis severity ([PMID: 36090737](https://pubmed.ncbi.nlm.nih.gov/36090737/)) are whole-organism micronutrient epidemiology, not evidence of FLG protein binding metal. Any weak, nonspecific chelation by histidine-rich degradation products would be a downstream metabolic property, not a molecular-function site — and is **not** the basis of the current IEA (which comes only from the S100 domain signature). The metal-relevant S100 domain exists only in **profilaggrin**; mature filaggrin repeat monomers do not contain it, so the annotation cannot even apply to the processed product.

---

## Conflicts and Alternatives

- **Database carry-over / frequency bias (primary alternative):** GO:0046914 is an InterPro2GO generalization from the broad S-100 domain family. The transition-metal phenotype is concentrated in soluble, histidine-rich S100 paralogs (calprotectin S100A8/A9, S100A7, S100B), which drives the family mapping — classic over-annotation of a structural family member that lacks the site.
- **Paralog/subfamily distinction:** Profilaggrin is an **S100 fused-type protein (SFTP)** — a structural subgroup (with trichohyalin, hornerin, repetin, cornulin) whose S100 domain is specialized for hydrophobic-pocket protein binding ([PMID: 32893105](https://pubmed.ncbi.nlm.nih.gov/32893105/)), not metal sequestration.
- **Specific-term supersession pattern:** True metal-binders carry the specific experimental term GO:0008270 (zinc ion binding), which suppresses the redundant generic IEA parent. FLG shows GO:0046914 only because it has no experimental metal term to supersede it — an artifact of the redundancy-filtering pipeline, not positive evidence.
- **In-principle EF-hand His–Zn binding:** [PMID: 18359862](https://pubmed.ncbi.nlm.nih.gov/18359862/) shows calbindin D28k can bind Zn²⁺ via His80. This raises a theoretical possibility, but FLG's two histidines sit in the EF-hand-2 calcium loop 8–15 Å apart from any partner, and calbindin is not S100-fused — a weak, non-physiological analogy.
- **No conflicting positive evidence found:** No primary study reporting Zn/Cu/Mn binding by the FLG gene product was located, and the deposited structure (4PCW) contains only Ca²⁺.

---

## Limitations and Knowledge Gaps

1. **No direct metal-binding assay of the profilaggrin S100 domain.** Checked: PubMed and the 4PCW structure paper — only calcium was co-crystallized/tested. Matters because the verdict rests on inference from ligand absence rather than a direct negative experiment. Resolve with ITC/ICP-MS/XAS or a metal-competition fluorescence assay on the recombinant profilaggrin S100(AB) domain vs. Zn²⁺/Cu²⁺/Mn²⁺.
2. **Solution vs. crystal behavior.** Only the Ca-grown crystal is available; weak or transient transition-metal association could be missed. Resolve with metal-binding assays under varied conditions and metal-soaked XAS.
3. **Behavior of the histidine-rich repeats toward metals.** The full protein is globally histidine-rich, but the repeats have no S100 architecture and are not the basis of the IEA; any chelation would be nonspecific and downstream. Resolve with equilibrium dialysis/ICP-MS on a repeat construct (expected: weak, nonspecific).
4. **Family-wide curation consistency and InterPro2GO provenance.** Confirmed all six SFTP paralogs share the same IEA and that IPR034325 is the sole source. Matters because curators may prefer a mapping-level fix. Resolve by reviewing the IPR034325 → GO:0046914 mapping with InterPro/GOA.

---

## Discriminating Tests

1. **Recombinant profilaggrin S100(AB) metal titration** (ITC or competition with a fluorescent Zn chelator such as FluoZin/Mag-fura-2) ± saturating Ca²⁺ — the single most decisive experiment. Predicts no high-affinity (µM–nM) Zn/Cu site.
2. **Structural superposition** of 4PCW against a His-Zn S100 (e.g., S100A7, S100B-Zn, calprotectin) to confirm the interfacial His₃Asp geometry is absent (partly done here by residue and geometry audits).
3. **XAS/anomalous diffraction** of the domain soaked in Zn²⁺/Cu²⁺ to test for any adventitious site.
4. **Comparative InterPro2GO audit** across all SFTP paralogs — uniform inheritance of GO:0046914 with no member-specific metal data confirms systematic family over-annotation.

---

## Proposed Follow-up Actions / Curation Leads

**All items are leads requiring curator verification.**

- **Action change (lead):** Do **not** retain GO:0046914 as a reviewed MF for FLG; classify as non-core / uninformative IEA (remove or flag as unsupported by member-specific evidence). Extend the same review to TCHH, HRNR, RPTN, CRNN, FLG2.
- **Candidate reference to verify — [PMID: 25760235](https://pubmed.ncbi.nlm.nih.gov/25760235/):** snippet "*we determined a 2.2 Å-resolution crystal structure of the N-terminal fused-type S100 domain of human profilaggrin with bound calcium ions*" → supports **GO:0005509 calcium ion binding** (upgrade rationale) and refutes a transition-metal role.
- **Candidate replacement/kept MF term:** **GO:0005509 calcium ion binding** (well supported); optionally **calcium-dependent protein binding** for the annexin II / 14-3-3σ / HSP27 / keratin interactions ([PMID: 25760235](https://pubmed.ncbi.nlm.nih.gov/25760235/), [PMID: 32893105](https://pubmed.ncbi.nlm.nih.gov/32893105/)). Avoid bare "protein binding."
- **Mechanistic reference — [PMID: 20306096](https://pubmed.ncbi.nlm.nih.gov/20306096/):** snippet defining that metal-binding S100s use "*three histidines and an aspartic acid*" (His-Zn) or cysteines (Cys-Zn) — the ligand set FLG's S100 domain lacks (0 Cys, 2 His).
- **Suggested curator question:** "Is IPR034325 → GO:0046914 an appropriate mapping to propagate to structural S100-fused-type family members that lack the interfacial His/Cys metal ligands?" (candidate for InterPro2GO refinement / NOT qualifier).
- **Suggested experiment:** recombinant profilaggrin S100(AB) Zn²⁺/Cu²⁺ ITC/ICP-MS (Discriminating Tests #1).

---

## Provenance / Artifacts

Computed in this run (executed code + output captured in the iteration log):

- **S100 metal-ligand residue audit** — S100 domain res 1–91: 2 His (60, 65), 0 Cys; N-terminal 1–212: 0 Cys; EF-hand2 Ca ligands 62/64/66/68/73 = D,D,N,K,E.
- **PDB 4PCW HETATM metal audit** — 8× Ca, 0× Zn/Cu/Mn/Fe/Ni (ligands: CA, 2PE [PEG], HOH). The profilaggrin S100 crystal structure contains only calcium.
- **SFTP paralog + control annotation audit** — all 6 S100-fused-type paralogs carry GO:0046914 IEA:InterPro; S100A7/A8/A9/B carry GO:0008270 (zinc ion binding) via NAS/TAS/IDA instead.
- **PDB 4PCW His-geometry test** — resolved S100 histidines (His59, His64 in PDB numbering = UniProt His60/His65) lie 8–15 Å from calcium and do not cluster (His64···His64 all >6 Å; one marginal His59···His59 crystal contact at ~5.2 Å) — insufficient to build a canonical His3Asp/His4 site.
- **InterPro→GO mapping check** — IPR034325 "S-100" is the sole P20930 signature mapped to GO:0046914; IPR002048 (EF-hand) → GO:0005509; IPR003303 (Filaggrin) → GO:0005198.
- **UniProt GO set** for P20930 confirms both GO:0046914 and GO:0005509 are IEA:InterPro (no experimental MF metal annotation).

*Data sources: UniProt REST (P20930 + 8 comparators), InterPro REST (entry/protein), RCSB PDB 4PCW, PubMed.*


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)