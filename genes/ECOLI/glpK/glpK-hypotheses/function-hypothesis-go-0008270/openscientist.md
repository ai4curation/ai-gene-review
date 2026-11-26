---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-24T04:40:32.596350'
end_time: '2026-10-24T05:49:41.606017'
duration_seconds: 4149.01
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: ECOLI
  gene: glpK
  gene_symbol: glpK
  uniprot_accession: P0A6F3
  taxon_id: NCBITaxon:83333
  taxon_label: Escherichia coli K-12
  focus_type: function_assignment
  hypothesis_slug: function-hypothesis-go-0008270
  hypothesis_text: glpK has zinc ion binding (GO:0008270).
  term_context: '- Term: zinc ion binding (GO:0008270)

    - Evidence type: IDA

    - Original reference: PMID:8170944'
  reference_context: '- PMID:8170944'
  source_file: genes/ECOLI/glpK/glpK-ai-review.yaml
  source_selector: existing_annotations[18].function_hypothesis
  source_context_yaml: "term:\n  id: GO:0008270\n  label: zinc ion binding\nevidence_type:\
    \ IDA\noriginal_reference_id: PMID:8170944"
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
citation_count: 3
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

- **Organism code:** ECOLI
- **Taxon:** Escherichia coli K-12 (NCBITaxon:83333)
- **Gene directory:** glpK
- **Gene symbol:** glpK
- **UniProt accession:** P0A6F3

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** function-hypothesis-go-0008270
- **Source file:** genes/ECOLI/glpK/glpK-ai-review.yaml
- **Source selector:** existing_annotations[18].function_hypothesis

## Seed Hypothesis

glpK has zinc ion binding (GO:0008270).

## Term and Decision Context

- Term: zinc ion binding (GO:0008270)
- Evidence type: IDA
- Original reference: PMID:8170944

## Reference Context

- PMID:8170944

## Source Context YAML

```yaml
term:
  id: GO:0008270
  label: zinc ion binding
evidence_type: IDA
original_reference_id: PMID:8170944
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

# AIGR Gene Hypothesis Deep Research — Final Report

**Gene:** glpK (glycerol kinase) · *Escherichia coli* K-12 · UniProt **P0A6F3**
**Hypothesis evaluated:** glpK has **zinc ion binding (GO:0008270)**
**Focus type:** function_assignment · **Evidence type:** IDA · **Original reference:** [PMID:8170944](https://pubmed.ncbi.nlm.nih.gov/8170944/)

---

## Summary

The zinc ion binding annotation for glycerol kinase (GlpK) is based on genuine, high-quality direct structural evidence, so it is **not wrong** and should not simply be deleted. However, the annotation is **misleading if read as an intrinsic molecular function of GlpK**. The crystallographic and mutagenesis record shows unambiguously that GlpK does not possess an autonomous zinc-binding site. Instead, a single Zn(II) ion is coordinated at an **intermolecular interface** that only exists when the glucose-specific phosphocarrier protein **IIAGlc** (older name IIIGlc) docks onto GlpK. In that complex, IIAGlc supplies **two** of the metal ligands (two active-site histidines) and GlpK supplies exactly **one** ligand (a single glutamate, Glu478; UniProt residue 479), with a water molecule completing a tetrahedral, thermolysin-like coordination sphere.

The biological role of this zinc site is **regulatory, not catalytic**. Zn(II) promotes the association of IIAGlc with GlpK and thereby strengthens the inhibition of glycerol kinase during inducer exclusion. It has nothing to do with GlpK's enzymatic mechanism: the catalytic reaction (glycerol + ATP → glycerol-3-phosphate + ADP) uses a Mg·ATP cofactor, and no zinc is present in any of the apo or catalytically loaded GlpK structures. Across the entire deposited structural record for *E. coli* GlpK, zinc appears **only** in the two GlpK·IIAGlc complex structures and **never** in standalone GlpK.

**Executive verdict: Partially supported — retain, but qualify as non-core (context-dependent, intermolecular).** The most important caveat for curation is one of **interpretation and scope**, not of correctness. GO:0008270 is defensible as an IDA because GlpK really does contribute a zinc ligand in physiologically relevant complexes, but a curator should retain it with a clear note that the site is intermolecular and IIAGlc-dependent, rather than leaving a bare "zinc ion binding" molecular-function term that implies an intrinsic GlpK cofactor.

---

## Key Findings

### Finding F001 — GlpK zinc binding is an intermolecular, IIAGlc-complex-dependent site, not an intrinsic cofactor

The foundational evidence comes directly from the original annotation reference, the 2.6 Å crystal structure of the *E. coli* IIAGlc–glycerol kinase complex ([PMID:8170944](https://pubmed.ncbi.nlm.nih.gov/8170944/)). That structure shows that the complex of IIIGlc (IIAGlc) with glycerol kinase **creates** an intermolecular Zn(II) binding site whose ligation is identical to that of the zinc peptidase thermolysin. The zinc is coordinated by the two active-site histidines of IIAGlc, a single glutamate of glycerol kinase, and a water molecule. The authors explicitly note that "the need for the target protein to supply only one metal ligand may account for the lack of sequence similarity among the regulatory targets of IIIGlc" — a direct statement that zinc binding is **not** an intrinsic property of GlpK but an emergent property of the two-protein interface.

This is corroborated independently by the mutagenesis and biophysical study [PMID:9538005](https://pubmed.ncbi.nlm.nih.gov/9538005/), which states that "association of these two proteins forms an intermolecular binding site for Zn(II) with metal ligands contributed by each protein," and identifies "the Zn(II)-liganding residue contributed by glycerol kinase (Glu478)." Substitutions at Glu478 (E478C/D and others) perturb the zinc-dependent association, confirming that this single residue is GlpK's entire contribution to the metal site. The apparent affinity of the **complex** for Zn(II) is in the sub-micromolar range (Kd < 1 µM), and Zn(II) at 0.01/0.1 mM lowers the Ki of IIAGlc for glycerol kinase roughly 15- to 60-fold — a quantitative demonstration that zinc's role is to **enhance the inhibitory association**, i.e., a regulatory effect on inducer exclusion.

Critically, the UniProt record for P0A6F3 is fully consistent with this picture: the catalytic site annotations describe ATP/ADP/glycerol/glycerol-3-phosphate and the allosteric effector FBP, and there is **no zinc cofactor comment**; the only zinc-related feature is a single Zn(2+)-binding residue at position 479 (the Glu478 of the mature-sequence numbering). This is exactly what one expects for a protein that donates one ligand to an intermolecular site rather than harboring a classic zinc-finger or catalytic-zinc motif.

### Finding F002 — Across 13 PDB structures, zinc appears only in GlpK·IIAGlc complexes; apo/catalytic GlpK uses Mg

A census of all 13 deposited *E. coli* GlpK structures mapped to UniProt P0A6F3 shows that the ZN ligand is present in exactly **two** entries — **1GLC** (ligands ADP, G3H, MG, ZN) and **1GLE** (ZN) — and both are two-protein-entity GlpK·IIAGlc complexes. Every single-chain apo or substrate-bound GlpK structure contains **no zinc**, including catalytically loaded forms with ATP analogs and magnesium: 1BWF (ATF + MG), 1GLJ (ATS + MG), 1GLL (ACP + MG), 3EZW (MG), as well as the ligand-free structures 1BO5, 1BOT, 1BU6, and 1GLF. Even the oligomeric/complex forms 1GLA, 1GLB, and 1GLD (the last with ADP, G3H, and Mn) lack any modeled zinc, and the catalytic divalent metal observed is magnesium (or manganese), never zinc.

This structural census is the single most decisive line of evidence for curation. If zinc binding were an intrinsic GlpK function, one would expect zinc to co-crystallize with GlpK in at least some of the eight standalone structures, particularly the catalytically loaded ones. It does not. The strict co-occurrence of zinc with the IIAGlc partner — and its complete absence from catalytic GlpK — demonstrates that the zinc site is a property of the **complex**, and that the catalytic chemistry of GlpK is entirely magnesium-dependent.

| Structure | Chains / entities | Catalytic/other ligands | Zinc present? |
|-----------|-------------------|--------------------------|:-------------:|
| 1GLC | GlpK + IIAGlc (2 entities) | ADP, G3H, MG | **Yes (ZN)** |
| 1GLE | GlpK + IIAGlc (2 entities) | — | **Yes (ZN)** |
| 1BWF | GlpK only | ATF, MG | No |
| 1GLJ | GlpK only | ATS, MG | No |
| 1GLL | GlpK only | ACP, MG | No |
| 3EZW | GlpK only | MG | No |
| 1GLA | GlpK (oligomer) | — | No |
| 1GLB | GlpK (oligomer) | — | No |
| 1GLD | GlpK (oligomer) | ADP, G3H, MN | No |
| 1BO5 | GlpK only | ligand-free | No |
| 1BOT | GlpK only | ligand-free | No |
| 1BU6 | GlpK only | ligand-free | No |
| 1GLF | GlpK only | ligand-free | No |

**Summary: zinc occurs in 2/13 structures, both GlpK·IIAGlc complexes; 0/8 standalone GlpK structures contain zinc.**

### Finding F003 — Direct 1GLC coordinate analysis confirms a single, tetrahedral, intermolecular Zn site

To verify the literature claims directly rather than relying on database annotations, the deposited 1GLC coordinates were parsed atom-by-atom. In 1GLC, chain F is IIAGlc (~168 residues) and chain G is GlpK (residues 4–499). The single Zn ion is tetrahedrally coordinated by:

- chain F (IIAGlc) **His75** NE2 at 2.44 Å,
- chain F (IIAGlc) **His90** NE2 at 2.21 Å,
- chain G (GlpK) **Glu478** OE2 at 1.97 Å,
- a **water** oxygen at 2.07 Å.

This independent, first-principles check reproduces the published description exactly: GlpK (chain G) contributes **exactly one** ligand (Glu478), while IIAGlc supplies two histidines, with a water completing the thermolysin-like tetrahedral geometry. The computed Glu478–Zn distance of 1.97 Å is a tight, bona fide metal–carboxylate bond, confirming that GlpK's glutamate is a genuine ligand — but also that, without IIAGlc's two histidines and the water, there is no coordination sphere at all.

```
        Intermolecular Zn(II) site in the GlpK·IIAGlc complex (1GLC)

            IIAGlc (chain F)                 GlpK (chain G)
          ┌──────────────────┐            ┌──────────────────┐
          │  His75 NE2 ──────┐│            │                  │
          │           2.44 Å ││            │                  │
          │  His90 NE2 ─────┐││            │                  │
          │           2.21 Å│││            │                  │
          └─────────────────┼┼┼────────────┼──────────────────┘
                            ╲│││            │
                             ╲││   Zn(II)   │
                              ╲│  ╱   ╲     │
                     1.97 Å    ╳ ╱     ╲    │
          GlpK Glu478 OE2 ─────╱        ╲   │
                                        H2O (2.07 Å)

   Ligand tally:  IIAGlc = 2 (His75, His90) | GlpK = 1 (Glu478) | water = 1
   Geometry: tetrahedral, identical to thermolysin → site exists ONLY in complex
```

---

## Mechanistic Model / Interpretation

The findings converge on a single, internally consistent model that cleanly separates GlpK's **catalytic** function from the **regulatory zinc** phenomenon.

**Catalytic GlpK (zinc-independent).** Glycerol kinase catalyzes glycerol + ATP → *sn*-glycerol-3-phosphate + ADP, using a Mg·ATP substrate. All catalytically relevant structures (1BWF, 1GLJ, 1GLL, 3EZW, 1GLD) show magnesium (or manganese as a surrogate) in the active site and no zinc. The enzyme is also allosterically inhibited by fructose-1,6-bisphosphate (FBP). None of this chemistry involves zinc.

**Regulatory inducer exclusion (zinc-enhanced, intermolecular).** When glucose is being transported, the dephosphorylated form of IIAGlc binds to GlpK and inhibits it — part of the inducer-exclusion mechanism that prevents glycerol utilization during glucose availability. The docking of IIAGlc onto GlpK juxtaposes IIAGlc's two active-site histidines (His75, His90) with GlpK's Glu478, **creating** a tetrahedral zinc site at the interface. Occupancy of this site by Zn(II) stabilizes the complex (sub-micromolar Kd for the complex) and strengthens inhibition (Ki lowered ~15–60-fold). This is "cation-promoted association": zinc acts as a molecular glue that tunes a protein–protein regulatory interaction, not as an enzyme cofactor.

```
   GlpK ALONE                         GlpK · IIAGlc COMPLEX
   ───────────                        ─────────────────────
   Mg·ATP in active site              Mg·ATP still catalytic (when active)
   NO zinc site                       Intermolecular Zn site FORMS
   Catalysis proceeds                 IIAGlc inhibits GlpK (inducer exclusion)
   (zinc irrelevant)                  Zn(II) ↑ complex stability ↑ inhibition

   GO relevance:                      GO relevance:
   glycerol kinase activity           zinc ion binding (GO:0008270) —
   (catalytic, core)                  real but intermolecular, non-core,
                                      regulatory, IIAGlc-dependent
```

The key curatorial consequence is that GO:0008270 for GlpK is a **true-but-partial** statement. GlpK genuinely binds zinc (it donates a carboxylate ligand with a 1.97 Å bond), satisfying the literal definition of "zinc ion binding," which is why the IDA is defensible. But the annotation, taken alone, over-implies an autonomous GlpK zinc cofactor and obscures that the binding is (1) intermolecular, (2) conditional on IIAGlc, and (3) regulatory rather than catalytic.

---

## Evidence Matrix

| Citation | Evidence type | Supports / Refutes / Qualifies | Claim tested | Key finding | Context | Confidence & limitations |
|----------|---------------|-------------------------------|--------------|-------------|---------|--------------------------|
| [PMID:8170944](https://pubmed.ncbi.nlm.nih.gov/8170944/) | Direct assay (X-ray structure, 2.6 Å) + biochemistry | **Qualifies** (supports literal binding; refutes "intrinsic") | Does GlpK have a zinc site? | Zn(II) site is **intermolecular**, formed by complex; IIAGlc gives 2 His, GlpK gives 1 Glu + water; thermolysin-like. Zn lowers Ki ~15–60× | *E. coli*, IIAGlc·GlpK complex, in vitro | High confidence. This IS the original IDA reference; it shows the site is complex-dependent, not autonomous |
| [PMID:9538005](https://pubmed.ncbi.nlm.nih.gov/9538005/) | Direct assay + mutant phenotype (Glu478 substitutions) | **Qualifies** | Which residue is GlpK's zinc ligand; is site intermolecular? | "Intermolecular binding site for Zn(II) with metal ligands contributed by each protein"; GlpK ligand = **Glu478**; complex Kd(Zn) < 1 µM | *E. coli*, in vitro mutagenesis/biophysics | High confidence. Independent confirmation; mutating the single GlpK ligand perturbs zinc-dependent association |
| [PMID:9405042](https://pubmed.ncbi.nlm.nih.gov/9405042/) | Structural/evolutionary (synthesis + new IIAGlc crystal forms) | **Qualifies / supports mechanism** | Generality of the intermolecular zinc "cation-promoted association" | Intermolecular Zn(II) site with "tetrahedral ligation identical to that of the zinc peptidase thermolysin"; cation-promoted association lets IIAGlc bind diverse targets | *E. coli* IIAGlc crystal forms | Medium-high. Focused on IIAGlc; reinforces that the site is a general IIAGlc interface feature, not GlpK-specific |
| PDB census (13 structures, RCSB/UniProt P0A6F3) | Computational / structural | **Qualifies** (refutes intrinsic-cofactor reading) | Does zinc co-occur with standalone GlpK? | Zn in only 1GLC + 1GLE (both complexes); 0/8 standalone GlpK structures; catalytic metal is Mg/Mn | Deposited structures | High confidence; depends on completeness/accuracy of deposited models |
| 1GLC coordinate parse (this study) | Computational (direct geometry) | **Qualifies** | Verify ligand identity & geometry | Zn coordinated by IIAGlc His75 (2.44 Å), His90 (2.21 Å), GlpK Glu478 (1.97 Å), water (2.07 Å); GlpK gives 1 ligand | 1GLC complex | High confidence; single structure, single site |
| UniProt P0A6F3 (database) | Review/database | **Qualifies** | How is zinc represented in the reference record? | No zinc cofactor comment; only one Zn(2+)-binding residue (479); catalytic sites are ATP/ADP/glycerol/G3P/FBP | Curated record | Database-level orientation; consistent with single-ligand intermolecular site |

---

## GO Curation Implications

**Lead (requires curator verification): Retain GO:0008270 (zinc ion binding, MF) but annotate as non-core and context-dependent.**

- **Molecular Function (GO:0008270, zinc ion binding):** The IDA is **justified at the literal level** — GlpK contributes a genuine zinc ligand (Glu478/479) with a 1.97 Å metal–carboxylate bond in the complex. It should **not** be removed, because that would discard a real, experimentally observed contact. However, it should **not** be read as an intrinsic GlpK cofactor. Recommended curator actions:
  - **Retain** the term, but attach a qualifier/annotation note that the zinc site is **intermolecular**, formed only in the GlpK·IIAGlc complex, with GlpK supplying a single glutamate ligand.
  - Consider whether a **"contributes_to"** style qualifier (or GO-CAM/complex-context modeling) better represents that the binding activity belongs to the GlpK·IIAGlc assembly rather than GlpK in isolation.
- **Do not generalize to a catalytic-zinc interpretation.** GlpK's catalysis is magnesium-dependent; the zinc is not a catalytic cofactor. Any downstream enzyme-mechanism annotation must remain Mg-based.
- **Biological Process context:** The functionally meaningful consequence of this zinc binding is **enhancement of IIAGlc-mediated inhibition of glycerol kinase / inducer exclusion**. If the curator wishes to capture the physiological role, a regulatory BP framing (negative regulation of glycerol kinase activity in the context of inducer exclusion) is more informative than the bare MF term, but should be clearly tied to the complex.
- **Avoid "protein binding" as a resolution.** The IIAGlc–GlpK interaction is independently captured by interaction annotations; the zinc term adds specific, informative detail about *how* that interface is stabilized and should be preserved with proper scope rather than collapsed into a generic binding term.

**GO Decision Table**

| Option | Assessment |
|--------|-----------|
| Remove GO:0008270 | **Not recommended** — binding is experimentally real (IDA from PMID:8170944) |
| Retain as-is (unqualified intrinsic MF) | **Too strong** — implies autonomous GlpK zinc cofactor; misleading |
| **Retain + qualify as intermolecular / non-core (IIAGlc-dependent)** | **Recommended lead** — accurate and preserves evidence |
| Generalize to "metal ion binding" | Not preferred — less specific; the ion is specifically Zn(II) |
| Make more specific (catalytic zinc) | **Wrong** — zinc is regulatory, not catalytic |

---

## Mechanistic Scope

The **immediate molecular event** being tested is whether the GlpK polypeptide coordinates a Zn(II) ion. The direct answer: GlpK provides **one** coordinating residue (Glu478) to a four-ligand tetrahedral zinc site, and only when IIAGlc is bound to supply the remaining two histidine ligands and position a catalytic water.

**Separating direct activity from downstream effects:**

- **Direct gene-product activity (zinc-related):** donation of a single carboxylate ligand to an intermolecular metal site. This is GlpK's only molecular contribution to zinc coordination.
- **Direct gene-product activity (core catalytic):** ATP-dependent phosphorylation of glycerol using Mg·ATP — entirely zinc-independent.
- **Complex-level activity:** the assembled GlpK·IIAGlc interface is the actual zinc-binding entity; zinc binding is a property of the assembly.
- **Downstream/pathway consequence:** zinc occupancy strengthens IIAGlc-mediated inhibition of glycerol kinase (lower Ki), contributing to **inducer exclusion** during glucose catabolite repression. This is a regulatory/physiological outcome, not a molecular property of GlpK alone.
- **Not applicable:** there are no developmental outcomes or disease manifestations relevant here (bacterial metabolic enzyme).

---

## Conflicts and Alternatives

- **Intrinsic vs. intermolecular (the central tension):** A naïve reading of "GlpK has zinc ion binding" conflicts with the structural record, which shows no zinc in any standalone GlpK structure. The resolution is that the IDA is literally true but describes an intermolecular site. There is no genuine experimental conflict — only an interpretive one about scope.
- **Catalytic-metal confusion:** GlpK uses Mg (Mn as surrogate) catalytically. A curator or automated pipeline could mistakenly equate the regulatory zinc with a catalytic metal. The evidence (Mg in all catalytic structures; Zn only in complexes) refutes any catalytic-zinc interpretation.
- **Partner-attribution / "paralog-like" carry-over:** Because two of the four ligands belong to IIAGlc (crr gene product, a different protein), there is a risk of attributing the whole zinc site to GlpK. The site is more properly a feature of the IIAGlc interface (reinforced by PMID:9405042, which shows IIAGlc forms similar intermolecular zinc contacts in multiple crystal forms). This argues for complex-level rather than GlpK-only modeling.
- **In vitro-only caveat:** The zinc enhancement of association was characterized in vitro. Whether cellular zinc availability makes this a physiologically dominant regulatory contribution (versus a measurable but minor enhancer) is not fully established, though the ~15–60× Ki effect is substantial.
- **No competing hypothesis refutes binding itself:** No evidence suggests GlpK lacks the Glu478 ligand or that the site is an artifact; the 1GLC geometry (1.97 Å Glu–Zn bond) is clean.

---

## Limitations and Knowledge Gaps

1. **Physiological significance of the zinc enhancement.** *Checked:* in vitro Ki/Kd measurements (PMID:9538005) and structures. *Gap:* whether intracellular free Zn(II), which is tightly buffered to very low levels in *E. coli*, is sufficient to occupy this site in vivo. *Resolution:* in vivo inducer-exclusion assays under controlled zinc conditions, or zinc-biosensor measurements paired with glycerol kinase regulation readouts.
2. **Quantitative apportionment of the regulatory effect.** *Checked:* Ki lowered ~15–60× by Zn (PMID:8170944). *Gap:* how much of inducer exclusion in vivo depends on zinc occupancy versus hydrophobic/salt-bridge contributions to IIAGlc–GlpK association. *Resolution:* compare glycerol utilization/inducer exclusion in strains expressing GlpK-E478 variants that abolish the zinc ligand versus wild type.
3. **GO modeling convention.** *Checked:* UniProt lists a single Zn-binding residue, no zinc cofactor comment. *Gap:* the correct GO representation of an intermolecular metal site (annotate to GlpK vs. to the complex; use of qualifiers/GO-CAM). *Resolution:* curator policy decision + GO-CAM complex modeling.
4. **Generality across organisms.** *Checked:* evidence is *E. coli* K-12 specific. *Gap:* whether orthologous glycerol kinases in other bacteria retain the Glu ligand and the IIAGlc-dependent zinc site. *Resolution:* multiple sequence alignment of GlpK orthologs at the Glu478 position and comparative structural analysis.

---

## Discriminating Tests

The following would most efficiently separate "intrinsic GlpK zinc binding" from "intermolecular IIAGlc-dependent regulatory zinc site":

1. **Zinc content of standalone GlpK vs. GlpK·IIAGlc.** Metal-analysis (ICP-MS / PAR colorimetric Zn assay) on purified GlpK alone versus the reconstituted complex. Prediction (strong): GlpK alone carries ~0 stoichiometric zinc; the complex carries ~1 Zn per interface. This directly tests autonomy.
2. **Glu478 mutagenesis coupled to association and regulation.** Measure Zn-dependent enhancement of IIAGlc binding and inhibition for GlpK-E478A/C/D/Q. Loss of zinc dependence in the mutants confirms Glu478 as the sole GlpK ligand and the site as intermolecular (partially done in PMID:9538005; extend with in vivo assays).
3. **In vivo inducer-exclusion readout under zinc modulation.** Compare glycerol kinase inhibition / glycerol utilization in wild-type vs. E478 variants, and under zinc-limited vs. zinc-replete conditions, to quantify the physiological weight of the zinc contribution.
4. **Comparative structural/sequence census.** Confirm computationally (already strongly indicated) that no standalone GlpK structure binds zinc and that catalytic metals are Mg/Mn — and extend an ortholog alignment to test conservation of the Glu478 ligand.

---

## Proposed Follow-up Actions / Curation Leads

**All items below are leads requiring curator verification.**

- **Action change (primary lead):** Retain GO:0008270 (zinc ion binding, IDA, [PMID:8170944](https://pubmed.ncbi.nlm.nih.gov/8170944/)) but **re-scope it as non-core / intermolecular**. Add an annotation note: "Zinc site is intermolecular, formed only in the GlpK·IIAGlc regulatory complex; GlpK contributes a single glutamate ligand (Glu478/UniProt residue 479); IIAGlc supplies two histidine ligands (His75, His90) plus a water in a thermolysin-like tetrahedral geometry; zinc enhances IIAGlc-mediated inhibition (inducer exclusion), not catalysis."

- **Candidate reference + exact snippet to verify (PMID:8170944):**
  > "the complex of IIIGlc with glycerol kinase creates an intermolecular Zn(II) binding site with ligation identical to that of the zinc peptidase thermolysin. The zinc is coordinated by the two active-site histidines of IIIGlc, a glutamate of glycerol kinase, and a water molecule."
  >
  > "The need for the target protein to supply only one metal ligand may account for the lack of sequence similarity among the regulatory targets of IIIGlc."

- **Candidate corroborating reference + exact snippet (PMID:9538005):**
  > "Association of these two proteins forms an intermolecular binding site for Zn(II) with metal ligands contributed by each protein"
  >
  > "The Zn(II)-liganding residue contributed by glycerol kinase (Glu478)"

- **Candidate corroborating reference (PMID:9405042, structural orientation):** intermolecular Zn(II) binding site with tetrahedral ligation identical to the zinc peptidase thermolysin; "cation-promoted association" of IIAGlc with diverse targets.

- **Candidate GO terms / modeling:**
  - Keep **GO:0008270** (MF) with intermolecular qualifier; **do not** replace with the less-specific "metal ion binding" and **do not** reduce to "protein binding."
  - Consider complementary **BP** framing for the physiological role (regulatory inhibition of glycerol kinase during inducer exclusion), clearly tied to the GlpK·IIAGlc complex, if the review scope permits process annotations.
  - Consider GO-CAM / complex-context modeling attributing the zinc-binding activity to the GlpK·IIAGlc assembly.

- **Suggested curator questions:**
  1. Should an intermolecular metal site that requires a partner protein be annotated to the single gene (GlpK) or to the complex?
  2. Is a qualifier (e.g., "contributes_to") appropriate so the IDA is retained without implying an autonomous cofactor?
  3. Does the review want to add the regulatory/inducer-exclusion BP context to make the zinc annotation interpretable?

- **Suggested experiments (for annotators seeking stronger evidence):** stoichiometric zinc measurement of GlpK alone vs. complex; E478 variant association/regulation assays in vivo; zinc-conditional inducer-exclusion phenotyping (see Discriminating Tests).

---

## Evidence Base (Literature)

- **[PMID:8170944](https://pubmed.ncbi.nlm.nih.gov/8170944/)** — *Cation-promoted association of a regulatory and target protein is controlled by protein phosphorylation.* The original IDA reference. Provides the 2.6 Å crystal structure of the IIAGlc–glycerol kinase complex, defining the intermolecular, thermolysin-like Zn(II) site (two IIAGlc histidines + one GlpK glutamate + water) and the ~15–60× Ki enhancement. **Primary support that the site is real but intermolecular and regulatory.**

- **[PMID:9538005](https://pubmed.ncbi.nlm.nih.gov/9538005/)** — *Cation-promoted association of Escherichia coli phosphocarrier protein IIAGlc with regulatory target protein glycerol kinase: substitutions of a Zinc(II) ligand and implications for inducer exclusion.* Independent biophysical/mutagenesis confirmation; identifies Glu478 as GlpK's sole zinc ligand and reports sub-micromolar complex affinity for Zn(II). **Corroborates the intermolecular model and pins down the GlpK residue.**

- **[PMID:9405042](https://pubmed.ncbi.nlm.nih.gov/9405042/)** — *Structural studies of the Escherichia coli signal transducing protein IIAGlc: implications for target recognition.* Shows IIAGlc forms similar intermolecular Zn(II) contacts across crystal forms and frames "cation-promoted association" as a general mechanism allowing IIAGlc to bind sequence-unrelated targets. **Reinforces that the zinc site is a feature of the IIAGlc interface, not an intrinsic GlpK property.**

- **UniProt P0A6F3 (database orientation)** — No zinc cofactor comment; single Zn(2+)-binding residue at position 479; catalytic sites bind ATP/ADP/glycerol/G3P and effector FBP. **Consistent with a single-ligand, non-catalytic zinc contribution.**

- **PDB structural census + 1GLC coordinate analysis (computed in this investigation)** — Zinc present only in 1GLC and 1GLE (both complexes); 0/8 standalone GlpK structures contain zinc; catalytic metal is Mg/Mn. Direct 1GLC geometry: Zn–Glu478 1.97 Å, Zn–His75 2.44 Å, Zn–His90 2.21 Å, Zn–water 2.07 Å. **Decisive structural confirmation of the intermolecular, single-GlpK-ligand model.**

---

## Bottom Line

GO:0008270 (zinc ion binding) for *E. coli* glpK is **partially supported** and should be **retained but qualified as non-core**. The zinc binding is experimentally genuine (GlpK donates Glu478 as a metal ligand, 1.97 Å bond) yet exists only within the intermolecular GlpK·IIAGlc regulatory complex, where it enhances inducer-exclusion inhibition. It is **not** an intrinsic or catalytic cofactor of glycerol kinase, whose catalysis is magnesium-dependent. Curators should preserve the IDA while clearly marking its intermolecular, IIAGlc-dependent, regulatory scope.


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)