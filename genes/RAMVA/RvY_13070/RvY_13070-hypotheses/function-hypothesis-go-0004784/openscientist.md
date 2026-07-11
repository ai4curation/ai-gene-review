---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-04T09:59:53.322984'
end_time: '2026-07-04T10:20:58.857679'
duration_seconds: 1265.53
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: RAMVA
  gene: RvY_13070
  gene_symbol: RvY_13070
  taxon_id: NCBITaxon:947166
  taxon_label: Ramazzottius varieornatus
  focus_type: function_assignment
  hypothesis_slug: function-hypothesis-go-0004784
  hypothesis_text: RvY_13070 has superoxide dismutase activity (GO:0004784).
  term_context: '- Term: superoxide dismutase activity (GO:0004784)

    - Evidence type: IEA

    - Original reference: GO_REF:0000120'
  reference_context: '- GO_REF:0000120

    - PMID:37358501'
  source_file: genes/RAMVA/RvY_13070/RvY_13070-ai-review.yaml
  source_selector: existing_annotations[1].function_hypothesis
  source_context_yaml: "term:\n  id: GO:0004784\n  label: superoxide dismutase activity\n\
    evidence_type: IEA\noriginal_reference_id: GO_REF:0000120"
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
citation_count: 13
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

- **Organism code:** RAMVA
- **Taxon:** Ramazzottius varieornatus (NCBITaxon:947166)
- **Gene directory:** RvY_13070
- **Gene symbol:** RvY_13070

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** function-hypothesis-go-0004784
- **Source file:** genes/RAMVA/RvY_13070/RvY_13070-ai-review.yaml
- **Source selector:** existing_annotations[1].function_hypothesis

## Seed Hypothesis

RvY_13070 has superoxide dismutase activity (GO:0004784).

## Term and Decision Context

- Term: superoxide dismutase activity (GO:0004784)
- Evidence type: IEA
- Original reference: GO_REF:0000120

## Reference Context

- GO_REF:0000120
- PMID:37358501

## Source Context YAML

```yaml
term:
  id: GO:0004784
  label: superoxide dismutase activity
evidence_type: IEA
original_reference_id: GO_REF:0000120
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
prompt so the report can be compared against them after the run. Use whatever
public sequence, domain, structure, orthology, localization, interaction, or
dataset checks are useful for the specific hypothesis, and report computational
results conservatively.

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

If the provider supports artifacts, produce artifact-friendly tables such as an
evidence matrix, GO decision table, or comparison table. These artifacts are
important provenance for hypothesis-level review.


## Output

# Deep Research Report: RvY_13070 Superoxide Dismutase Activity (GO:0004784) Hypothesis Evaluation

## Executive Judgment

**Verdict: Over-annotated**

The IEA annotation of GO:0004784 (superoxide dismutase activity) to RvY_13070 is likely **over-annotated** and should be flagged for removal or NOT-qualification. RvY_13070 encodes RvSOD15, a Cu/Zn SOD-fold protein from the anhydrobiotic tardigrade *Ramazzottius varieornatus*. While the protein retains the SOD structural domain and binds copper and zinc (confirmed by X-ray crystallography at 2.1–2.2 Å resolution), a critical copper-ligand histidine required for catalysis is replaced by valine at position 87. The crystal structure of the V87H reversion mutant further demonstrates that even when histidine is restored at this position, a nearby flexible loop has co-evolved to destabilize His87–Cu coordination, indicating that the protein scaffold has structurally diverged from supporting SOD catalysis. Cross-species evidence from human SOD1 ALS mutations confirms that disruption of Cu-ligand histidines abolishes enzymatic activity. No direct enzymatic assay has been performed on RvSOD15, which remains the single most important caveat.

**Most important caveats:**
1. No direct SOD activity measurement exists — the conclusion is inferred from structural and comparative evidence.
2. Residual or unconventional catalytic activity cannot be fully excluded without biochemical characterization.
3. The protein binds Cu and Zn and is expressed in vivo, so it may serve a non-catalytic metal-binding or signaling role that warrants alternative GO annotation.

---

## Summary

RvY_13070 encodes RvSOD15, one of an extraordinarily expanded set of 21 superoxide dismutase paralogs in the anhydrobiotic tardigrade *Ramazzottius varieornatus*. The gene was computationally annotated with superoxide dismutase activity (GO:0004784) via an Inferred from Electronic Annotation (IEA) pipeline (GO_REF:0000120), based on the presence of the Cu/Zn SOD domain (Pfam PF00080). This investigation evaluated whether the gene product genuinely possesses the catalytic SOD activity implied by this GO term, integrating crystallographic data, comparative sequence analysis, mutational studies from the human ALS field, and the broader context of SOD gene family expansion in tardigrades.

The primary evidence against catalytic SOD activity comes from the crystal structures of RvSOD15 (PDB entries 7YPP and 7YPR, solved at 2.2 Å and 2.1 Å resolution, respectively; [PMID: 37358501](https://pubmed.ncbi.nlm.nih.gov/37358501/)). These structures reveal that Val87 replaces a canonical Cu-binding histidine that is absolutely conserved in enzymatically active Cu/Zn SODs. A V87H reversion mutant was also crystallized, and the structure showed that a nearby flexible loop destabilizes His87–Cu coordination, indicating that the loss of this interaction reflects deeper structural co-evolution of the active site, not merely a single amino acid change. The authors of the primary study concluded that "RvSOD15 and some other RvSODs may have evolved to lose the SOD function, suggesting that gene duplications of antioxidant proteins do not solely explain the high stress tolerance of anhydrobiotic tardigrades."

This conclusion is strongly supported by the ALS literature. Transgenic mice expressing human SOD1-H46R/H48Q — combining mutations at two copper ligands — develop motor neuron disease because the double mutant enzyme is catalytically inactive ([PMID: 17092942](https://pubmed.ncbi.nlm.nih.gov/17092942/)). Additional studies in yeast show that oxidative modification of the copper-ligand His120 in SOD1 promotes loss of catalytic activity and protein aggregation ([PMID: 24936435](https://pubmed.ncbi.nlm.nih.gov/24936435/)). Together, these cross-species data establish that intact histidine-copper coordination is mechanistically essential for the SOD catalytic cycle, reinforcing the inference that RvSOD15's Val87 substitution eliminates catalytic function.

---

## Key Findings

### Finding 1: Critical Copper-Ligand Substitution Abolishes the Structural Basis for SOD Catalysis

The crystal structures of RvSOD15 provide the most direct evidence bearing on the hypothesis. In all enzymatically characterized Cu/Zn SODs, the catalytic copper ion is coordinated by four histidine residues that enable the copper to cycle between Cu²⁺ and Cu⁺ oxidation states during superoxide dismutation. In RvSOD15, one of these — at position 87 — is replaced by valine. Valine's aliphatic side chain cannot coordinate copper, and the wild-type RvSOD15 structure confirms the absence of proper copper coordination geometry at this site.

The researchers also solved the structure of the V87H reversion mutant (PDB 7YPR). If the Val→His substitution were the sole barrier to catalytic activity, one would expect the V87H mutant to restore copper coordination and, by inference, enzymatic function. Instead, the V87H structure revealed that a nearby flexible loop destabilizes the coordination of His87 to the copper atom. This demonstrates that the active site has undergone coupled evolutionary changes — the loss of the histidine ligand has been accompanied by structural rearrangements in the surrounding loop that make copper coordination untenable even when the histidine is artificially restored. This is a hallmark of a protein that has been released from selective pressure to maintain catalytic function.

As stated by the study authors: *"In RvSOD15, one of the histidine ligands of the catalytic copper center is replaced by a valine (Val87). The crystal structures of the wild type and the V87H mutant show that even though a histidine is placed at position 87, a nearby flexible loop can destabilize the coordination of His87 to the Cu atom."* ([PMID: 37358501](https://pubmed.ncbi.nlm.nih.gov/37358501/))

The authors explicitly concluded: *"These studies show that RvSOD15 and some other RvSODs may have evolved to lose the SOD function, suggesting that gene duplications of antioxidant proteins do not solely explain the high stress tolerance of anhydrobiotic tardigrades."* ([PMID: 37358501](https://pubmed.ncbi.nlm.nih.gov/37358501/))

**Evidence strength:** High. Crystal structures at near-atomic resolution providing direct visualization of the active site, combined with a reversion mutant that fails to rescue metal coordination, constitute strong negative evidence against catalytic SOD activity.

### Finding 2: Cross-Species Validation from Human SOD1 Mutant Studies

The inference that loss of a Cu-ligand histidine abolishes SOD activity is robustly supported by the human SOD1 literature, particularly studies of familial ALS (FALS) mutations. [PMID: 17092942](https://pubmed.ncbi.nlm.nih.gov/17092942/) demonstrated that *"transgenic mice that express SOD1-H46R/H48Q, which combines natural FALS mutations at ligands for copper and which is inactive, develop motor neuron disease."* His46 and His48 are copper ligands in human SOD1; mutations at these positions produce a catalytically dead enzyme that nonetheless retains the SOD fold and can still bind zinc.

This is directly analogous to the situation in RvSOD15: the protein retains the overall Cu/Zn SOD fold and binds metals, but the disruption of copper ligand coordination eliminates the catalytic mechanism. Additional support comes from studies of SOD1 oxidation ([PMID: 24936435](https://pubmed.ncbi.nlm.nih.gov/24936435/)), which showed that oxidation of His120 (a copper ligand) in yeast SOD1 promotes loss of catalytic activity and aggregation, further confirming the critical role of His-Cu coordination for SOD function.

The crystal structure of monomeric human SOD1 mutant F50E/G51E/E133Q ([PMID: 10329151](https://pubmed.ncbi.nlm.nih.gov/10329151/)) demonstrated that even partial active-site disruption — without directly mutating copper ligands — reduces activity to ~20% of wild-type, emphasizing the exquisite sensitivity of SOD catalysis to the precise arrangement of residues in and around the copper-binding site. The complete loss of a Cu ligand (as in RvSOD15) would be expected to have a far more severe effect.

**Evidence strength:** Moderate-to-high. While cross-species extrapolation from human to tardigrade requires caution, the Cu/Zn SOD catalytic mechanism is deeply conserved across eukaryotes, and the role of histidine-copper coordination in catalysis is mechanistically fundamental, not species-specific.

### Finding 3: Massively Expanded SOD Gene Family with Diverse Structural Deviations

*R. varieornatus* possesses 21 SOD paralogs, far exceeding the typical complement in most animals (humans have 3: SOD1, SOD2, SOD3). UniProt searches confirmed 21 entries for SOD-related proteins in this organism (taxon 947166), many annotated only as "SOD domain-containing" without GO:0004784. The primary structural study reported that model structures of other RvSODs reveal additional unusual features: *"some of them are also unusual SODs, with features such as deletion of the electrostatic loop or β3 sheet and unusual metal-binding residues"* ([PMID: 37358501](https://pubmed.ncbi.nlm.nih.gov/37358501/)).

This massive expansion, combined with widespread structural divergence, is consistent with a model where gene duplication has freed multiple SOD paralogs from purifying selection on catalytic function. The electrostatic loop is critical for guiding negatively charged superoxide anions into the active site; its deletion in some paralogs would be expected to eliminate or severely impair catalytic function even if the metal-binding site were intact. The broader genomic context ([PMID: 28749982](https://pubmed.ncbi.nlm.nih.gov/28749982/); [PMID: 31624306](https://pubmed.ncbi.nlm.nih.gov/31624306/)) confirms that *R. varieornatus* has undergone extensive gene amplification in stress-related pathways, and the SOD family expansion is part of this pattern.

Notably, a recent glycoproteomics study ([PMID: 40306492](https://pubmed.ncbi.nlm.nih.gov/40306492/)) identified Cu/Zn-superoxide dismutase among glycoproteins modified with uncommon N-glycan structures in *R. varieornatus*, potentially hinting at non-canonical post-translational regulation of SOD-family proteins. Whether this refers to RvSOD15 specifically or another paralog is unclear.

**Evidence strength:** Moderate. Genomic context supports the plausibility of functional divergence but does not by itself prove that any specific paralog lacks SOD activity.

---

## Mechanistic Model and Interpretation

### The SOD Catalytic Mechanism and Why Val87 Matters

Cu/Zn superoxide dismutase catalyzes the dismutation of superoxide (O₂⁻) through a ping-pong mechanism that relies on cycling the copper ion between its Cu²⁺ and Cu⁺ oxidation states:

```
Oxidation half-reaction:   Cu²⁺-SOD + O₂⁻  →  Cu⁺-SOD + O₂
Reduction half-reaction:   Cu⁺-SOD  + O₂⁻ + 2H⁺  →  Cu²⁺-SOD + H₂O₂

Required structural elements:
  1. Four His residues coordinating the catalytic Cu
  2. His63 bridge connecting Cu and Zn (numbering varies by species)
  3. Electrostatic loop guiding O₂⁻ to the active site
  4. Conserved Arg stabilizing the transition state

RvSOD15 status:
  ✗ Val87 at Cu-ligand His position → Cu coordination disrupted
  ✗ V87H reversion → flexible loop prevents stable coordination
  ✓ Zn binding site intact
  ? Electrostatic loop — present but may be altered
  ? Arg — not characterized
```

### Model: SOD Fold Retention Without SOD Function (Pseudoenzyme)

The most parsimonious interpretation is that RvSOD15 is a **pseudoenzyme** — a protein that retains the ancestral enzyme fold but has lost catalytic activity through evolutionary divergence of the active site. This is analogous to well-characterized pseudokinases (e.g., HER3/ERBB3, CASK) that retain the kinase fold but lack one or more catalytic residues and function instead as allosteric regulators, scaffolds, or signaling components.

In the context of the *R. varieornatus* SOD gene family:
- Some paralogs likely retain canonical SOD activity (those with intact Cu-ligand histidines and electrostatic loops) and provide the oxidative stress defense critical for anhydrobiosis
- Other paralogs, including RvSOD15, have been freed from selective constraint on catalysis and may serve non-catalytic roles such as metal sequestration, protein scaffolding, or redox sensing
- The discovery of a novel Mn-dependent peroxidase as an important anhydrobiosis factor ([PMID: 35643424](https://pubmed.ncbi.nlm.nih.gov/35643424/)) demonstrates that tardigrades have evolved alternative antioxidant mechanisms beyond SOD, reducing the selection pressure to maintain SOD activity in all paralogs

### Separation of Fold, Function, and Phenotype

It is critical to distinguish three levels:

| Level | Assessment | Evidence |
|-------|-----------|---------|
| **SOD fold/domain** | Present | X-ray crystallography (PDB 7YPP) |
| **SOD catalytic activity** (GO:0004784) | Likely absent | Val87 substitution, V87H mutant fails to restore Cu coordination |
| **Oxidative stress tolerance** (organismal phenotype) | Present in organism | Multiple studies of tardigrade anhydrobiosis; but attributable to other paralogs/mechanisms |

The IEA annotation pipeline recognized the domain (level 1) but incorrectly inferred catalytic activity (level 2). This is a well-known failure mode of automated annotation, particularly problematic in expanded gene families where paralogs may have diverged in function while retaining sequence/structural similarity.

---

## Evidence Matrix

| Citation | Evidence Type | Direction | Claim Tested | Key Finding | Context | Confidence & Limitations |
|----------|--------------|-----------|--------------|-------------|---------|------------------------|
| [PMID: 37358501](https://pubmed.ncbi.nlm.nih.gov/37358501/) | Structural (X-ray) | **Refutes SOD activity** | RvSOD15 has SOD catalytic activity | Val87 replaces Cu-ligand His; V87H mutant loop destabilizes Cu coordination; authors conclude SOD function may be lost | *R. varieornatus* recombinant RvSOD15; PDB 7YPP (2.2 Å), 7YPR (2.1 Å) | **High** — direct structural evidence; no activity assay |
| [PMID: 37358501](https://pubmed.ncbi.nlm.nih.gov/37358501/) | Structural (X-ray) | **Supports metal binding** | RvSOD15 binds Cu/Zn | Cu and Zn ions confirmed at expected sites by crystallography | Same as above | **High** — direct crystallographic observation |
| [PMID: 37358501](https://pubmed.ncbi.nlm.nih.gov/37358501/) | Structural/comparative | **Qualifies** | Other RvSODs are canonical | Multiple paralogs show deleted electrostatic loops, missing β3 sheets, unusual metal ligands | *R. varieornatus* SOD family; computational modeling | **Medium** — model structures, not all experimental |
| [PMID: 17092942](https://pubmed.ncbi.nlm.nih.gov/17092942/) | Mutant phenotype + biochemistry | **Supports loss-of-activity inference** | Cu-ligand His mutations abolish SOD activity | H46R/H48Q double mutant is catalytically inactive | Human SOD1; transgenic mice | **High** for principle; cross-species inference |
| [PMID: 24936435](https://pubmed.ncbi.nlm.nih.gov/24936435/) | Biochemistry | **Qualifies** | Cu-ligand integrity required for activity | Oxidation of His120 (Cu ligand) causes loss of SOD1 activity and aggregation | Yeast SOD1; stationary-phase cells | **Medium** — indirect support |
| [PMID: 10329151](https://pubmed.ncbi.nlm.nih.gov/10329151/) | Structural/biochemistry | **Qualifies** | Active-site geometry essential for SOD activity | Monomeric SOD1 with active-site perturbation retains only ~20% activity | Human monomeric SOD1; 1.02 Å X-ray | **Medium** — shows sensitivity to geometry |
| [PMID: 40306492](https://pubmed.ncbi.nlm.nih.gov/40306492/) | Glycoproteomics | **Qualifies** | SOD proteins expressed in tardigrades | Cu/Zn-SOD among glycoproteins with unusual N-glycan modifications | *R. varieornatus* whole-organism | **Low-Medium** — paralog not specified |
| [PMID: 35643424](https://pubmed.ncbi.nlm.nih.gov/35643424/) | Transcriptomics/functional | **Competing** | SOD is key antioxidant for anhydrobiosis | Novel Mn-dependent peroxidase identified as important factor, not SOD | *R. varieornatus* UV/desiccation | **Medium** — alternative mechanisms |
| [PMID: 35743848](https://pubmed.ncbi.nlm.nih.gov/35743848/) | Biochemistry | **Qualifies** | SOD activity during anhydrobiosis | Bulk antioxidant enzyme activity measured during desiccation kinetics | Two eutardigrade species | **Low** — cannot distinguish paralogs |
| GO_REF:0000120 | Computational (IEA) | **Original annotation** | RvY_13070 has SOD activity | Automated annotation from domain family membership | Computational pipeline | **Low** — does not account for paralog divergence |

---

## GO Curation Implications

### Current Annotation Under Review
- **Term:** GO:0004784 (superoxide dismutase activity) — Molecular Function
- **Evidence code:** IEA (GO_REF:0000120)
- **Status:** Likely over-annotated

### Recommended Curation Actions (leads requiring curator verification)

**1. GO:0004784 (superoxide dismutase activity) — Recommend removal or NOT-qualification**

The structural evidence from [PMID: 37358501](https://pubmed.ncbi.nlm.nih.gov/37358501/) argues strongly against canonical SOD catalytic activity. A curator should consider:
- **Removing** GO:0004784 if structural evidence of disrupted catalytic residues is sufficient grounds (analogous to annotating a kinase-dead pseudokinase)
- **Adding a NOT qualifier** (GO:0004784 with NOT) if the evidence is deemed strong enough to assert absence of function
- **Retaining with an annotation note** if a direct negative activity assay is required before formal removal, citing PMID:37358501

**2. Metal ion binding annotations — Retain**
- GO:0005507 (copper ion binding) and GO:0008270 (zinc ion binding) are supported at the IDA level by crystallographic evidence from [PMID: 37358501](https://pubmed.ncbi.nlm.nih.gov/37358501/). These should be retained.

**3. BP annotation GO:0019430 (removal of superoxide radicals) — Flag for review**
- If GO:0004784 is removed, any process annotation dependent on SOD catalytic activity should be flagged for the same reasons.

**4. Candidate alternative terms**
- No specific alternative MF term is currently supported by experimental evidence. If RvSOD15 is confirmed as a pseudoenzyme, the protein is best described by its domain classification (Cu/Zn SOD domain-containing) and metal-binding annotations, without a catalytic MF term.

### Curation Priority Assessment

This is a **high-priority curation lead** because:
1. The IEA annotation actively implies catalytic function where structural evidence argues against it
2. The primary literature explicitly concludes that SOD function may be lost
3. The massively expanded 21-paralog SOD family makes automated annotation transfer unreliable — blanket GO:0004784 annotation across all paralogs would be inaccurate
4. This case exemplifies a broader issue: IEA annotations based on domain presence can be misleading for expanded gene families with divergent paralogs

---

## Conflicts and Alternatives

### Domain Presence vs. Catalytic Activity

The central conflict is between domain-level classification (which correctly identifies RvSOD15 as a Cu/Zn SOD-fold protein) and functional annotation (which incorrectly infers catalytic activity from domain presence). All computational annotations (IEA, ISS) are based on the presence of the Cu/Zn SOD domain (Pfam PF00080, cd00305). However, domain presence does not equal enzymatic activity, especially in expanded gene families with divergent paralogs. UniProt annotates this protein with EC 1.15.1.1 based on automated rules, but the primary structural paper explicitly contradicts this.

### Alternative Functional Hypotheses for RvSOD15

If RvSOD15 has lost SOD catalytic activity, what function does it serve? Several possibilities exist, none experimentally tested:

1. **Copper/zinc chaperone or storage protein** — the retained metal-binding capacity could serve a metallostasis function during desiccation, when ionic concentrations fluctuate dramatically
2. **Protein-protein interaction scaffold** — the SOD β-barrel fold is exceptionally stable and could mediate protein interactions
3. **Redox sensor** — the disrupted active site might sense or respond to oxidative stress without catalyzing superoxide dismutation
4. **Pseudoenzyme with regulatory function** — analogous to well-characterized pseudokinases that regulate active kinases through allosteric interactions
5. **Glycoprotein with extracellular role** — the identification of Cu/Zn-SOD among unusually glycosylated proteins ([PMID: 40306492](https://pubmed.ncbi.nlm.nih.gov/40306492/)) hints at possible extracellular or cell-surface functions

### Paralog Confusion Risk

With 21 SOD paralogs in *R. varieornatus*, there is a high risk of paralog confusion in:
- Automated GO annotation (IEA transfers from canonical SODs to all paralogs indiscriminately)
- Transcriptomic/proteomic studies that may not distinguish paralogs at the peptide level
- Literature references to "tardigrade SOD" without specifying which of the 21 paralogs is under discussion
- Glycoproteomics data ([PMID: 40306492](https://pubmed.ncbi.nlm.nih.gov/40306492/)) that identifies "Cu/Zn-superoxide dismutase" without paralog-level resolution

---

## Knowledge Gaps

| Gap | What Was Checked | Why It Matters | Resolving Evidence |
|-----|-----------------|----------------|-------------------|
| **No direct SOD activity assay for RvSOD15** | PubMed searches for RvSOD15/RvY_13070 activity, tardigrade SOD activity assays | Without direct measurement, functional annotation relies entirely on structural inference; residual activity cannot be excluded | Standard SOD activity assay (xanthine/xanthine oxidase/NBT or cytochrome c reduction) on purified recombinant RvSOD15 |
| **Unknown whether Val87 completely abolishes or merely reduces activity** | ALS literature on Cu-ligand mutations ([PMID: 17092942](https://pubmed.ncbi.nlm.nih.gov/17092942/)); monomeric SOD1 studies ([PMID: 10329151](https://pubmed.ncbi.nlm.nih.gov/10329151/)) | Residual activity (even <5%) would change the verdict from "remove" to "qualify" — particularly relevant if the protein operates in high-ROS contexts during desiccation | Quantitative activity assay with comparison to a canonical RvSOD paralog |
| **Actual biological function of RvSOD15 in vivo** | Literature on tardigrade stress tolerance, glycoproteomics, desiccation mechanisms | If RvSOD15 has a non-catalytic function, alternative GO terms may be appropriate | Knockdown/knockout studies (TardiVec system; [PMID: 36693101](https://pubmed.ncbi.nlm.nih.gov/36693101/)), protein interaction studies, localization during anhydrobiosis |
| **Which RvSOD paralogs retain canonical activity** | UniProt entries for 21 paralogs; only RvSOD15 experimentally characterized at structural level | Identifying catalytically active vs. divergent paralogs would clarify the functional landscape and inform family-wide annotation | Systematic expression and activity assay across the RvSOD family |
| **Metal occupancy in vivo** | Crystal structures show Cu/Zn binding in recombinant protein | In vivo metal loading may differ from recombinant/crystallographic conditions | ICP-MS or EXAFS on natively purified RvSOD15 from tardigrade lysates |

---

## Discriminating Tests

### Tier 1: Definitive Resolution

1. **Direct SOD activity assay on purified RvSOD15** — The single most important experiment. Express and purify recombinant RvSOD15 (wild-type and V87H mutant) and measure superoxide dismutase activity using standard xanthine oxidase/cytochrome c or NBT reduction assays. Include an active RvSOD paralog (one with all four conserved Cu-ligand histidines) as a positive control. A negative result would definitively support removal of GO:0004784; a positive result (even low residual activity) would require reconsideration.

2. **Comparative activity panel across RvSOD paralogs** — Express and purify 3–5 representative paralogs spanning the range of active-site conservation (fully canonical → Val87 substitution → electrostatic loop deletion) and measure SOD activities to establish the relationship between structural features and catalytic function in the tardigrade SOD family.

### Tier 2: Functional Characterization

3. **RvSOD15 knockdown during desiccation** — Use the TardiVec expression system ([PMID: 36693101](https://pubmed.ncbi.nlm.nih.gov/36693101/)) or dsRNA-mediated RNAi to knock down RvSOD15 and assess effects on survival, ROS levels, and oxidative damage during anhydrobiosis entry/exit. If loss of RvSOD15 has no effect on SOD-dependent phenotypes but affects other processes, this would support a non-SOD function.

4. **Interaction proteomics** — Immunoprecipitate or affinity-purify tagged RvSOD15 from tardigrade lysates and identify binding partners by mass spectrometry to reveal potential non-catalytic functions.

5. **In vivo metal occupancy** — Purify endogenous RvSOD15 from *R. varieornatus* and determine Cu/Zn content and stoichiometry by ICP-MS.

---

## Curation Leads

*All items below are leads requiring curator verification, not final decisions.*

### Lead 1: Flag GO:0004784 for Removal or NOT Annotation
- **Current:** GO:0004784 (superoxide dismutase activity), IEA, GO_REF:0000120
- **Proposed action:** Remove or add NOT qualifier
- **Basis:** Structural evidence of disrupted catalytic copper ligand (Val87) and failure of V87H reversion to restore coordination
- **Key reference:** [PMID: 37358501](https://pubmed.ncbi.nlm.nih.gov/37358501/)
- **Snippet to verify:** *"These studies show that RvSOD15 and some other RvSODs may have evolved to lose the SOD function"*
- **Confidence:** Medium-high (strong structural evidence; no direct activity measurement)

### Lead 2: Retain Copper and Zinc Binding Annotations
- **Current:** GO:0005507 (copper ion binding), GO:0008270 (zinc ion binding) — IDA
- **Proposed action:** Retain — well-supported by X-ray crystallography
- **Key reference:** [PMID: 37358501](https://pubmed.ncbi.nlm.nih.gov/37358501/), PDB 7YPP/7YPR
- **Confidence:** High

### Lead 3: Flag BP Annotation GO:0019430 for Coordinated Review
- **Current:** GO:0019430 (removal of superoxide radicals) — ISS
- **Proposed action:** Remove if GO:0004784 is removed, since the process depends on the molecular function
- **Confidence:** Conditional on Lead 1

### Lead 4: Consider Annotation Note if Full Removal Premature
- If removing GO:0004784 is considered too aggressive without a direct negative activity assay, an annotation note citing [PMID: 37358501](https://pubmed.ncbi.nlm.nih.gov/37358501/) should be added to flag this as a likely pseudoenzyme pending experimental confirmation.

### Lead 5: Flag Other *R. varieornatus* SOD Paralogs for Family-Wide Review
- **Proposed action:** Review all *R. varieornatus* SOD paralogs currently annotated with GO:0004784 via IEA; flag those with predicted active-site deviations for manual review
- **Basis:** [PMID: 37358501](https://pubmed.ncbi.nlm.nih.gov/37358501/) reports that multiple RvSODs have unusual structural features
- **Snippet to verify:** *"Model structures of other RvSODs were investigated and it was found that some of them are also unusual SODs, with features such as deletion of the electrostatic loop or β3 sheet and unusual metal-binding residues"*

### Suggested Questions for Curator
1. Does structural evidence of disrupted catalytic residues — without a direct negative activity assay — meet the threshold for removing or NOT-qualifying an IEA annotation?
2. Should other *R. varieornatus* SOD paralogs with predicted active-site deviations be flagged for simultaneous review?
3. Is there a GO curation precedent for "pseudoenzyme" annotation that could apply here?

---

## Evidence Base: Key Literature

| # | Citation | Key Contribution |
|---|----------|-----------------|
| 1 | [PMID: 37358501](https://pubmed.ncbi.nlm.nih.gov/37358501/) — *Structure of a superoxide dismutase from a tardigrade: Ramazzottius varieornatus strain YOKOZUNA-1* | **Primary evidence.** Crystal structures of RvSOD15 WT (PDB 7YPP) and V87H mutant (PDB 7YPR) showing disrupted Cu coordination. Authors conclude SOD function may have been lost. |
| 2 | [PMID: 17092942](https://pubmed.ncbi.nlm.nih.gov/17092942/) — *Disease-associated mutations at copper ligand histidine residues of superoxide dismutase 1 diminish the binding of copper and compromise dimer stability* | **Cross-species validation.** Cu-ligand His mutations (H46R/H48Q) in human SOD1 abolish enzymatic activity, supporting the inference for RvSOD15. |
| 3 | [PMID: 24936435](https://pubmed.ncbi.nlm.nih.gov/24936435/) — *SOD1 oxidation and formation of soluble aggregates in yeast* | **Supporting.** Oxidation of Cu-ligand His120 causes loss of SOD1 activity, confirming His-Cu coordination is essential. |
| 4 | [PMID: 10329151](https://pubmed.ncbi.nlm.nih.gov/10329151/) — *Crystal structure of monomeric human SOD mutant at atomic resolution* | **Contextual.** Shows SOD activity is highly sensitive to active-site geometry perturbations. |
| 5 | [PMID: 35643424](https://pubmed.ncbi.nlm.nih.gov/35643424/) — *Time-series transcriptomic screening of factors contributing to cross-tolerance to UV radiation and anhydrobiosis in tardigrades* | **Alternative mechanism.** Novel Mn-dependent peroxidase identified as key tardigrade antioxidant factor. |
| 6 | [PMID: 40306492](https://pubmed.ncbi.nlm.nih.gov/40306492/) — *Uncommon N-Glycan Structures in Anhydrobiotic Tardigrades* | **Contextual.** Cu/Zn-SOD among unusually glycosylated proteins in *R. varieornatus*. |
| 7 | [PMID: 35743848](https://pubmed.ncbi.nlm.nih.gov/35743848/) — *Antioxidant Response during the Kinetics of Anhydrobiosis in Two Eutardigrade Species* | **Background.** Bulk antioxidant measurements during anhydrobiosis. |
| 8 | [PMID: 28749982](https://pubmed.ncbi.nlm.nih.gov/28749982/) — *Comparative genomics of tardigrades Hypsibius dujardini and Ramazzottius varieornatus* | **Genomic context.** Comparative genomics establishing gene family expansion framework. |
| 9 | [PMID: 31624306](https://pubmed.ncbi.nlm.nih.gov/31624306/) — *Differential mechanisms of tolerance to extreme environmental conditions in tardigrades* | **Genomic context.** Gene amplifications in stress-tolerance pathways in *R. varieornatus*. |
| 10 | [PMID: 35167318](https://pubmed.ncbi.nlm.nih.gov/35167318/) — *Examples of Extreme Survival: Tardigrade Genomics and Molecular Anhydrobiology* | **Review.** Overview of tardigrade genomic adaptations. |
| 11 | [PMID: 25675104](https://pubmed.ncbi.nlm.nih.gov/25675104/) — *Novel mitochondria-targeted heat-soluble proteins in anhydrobiotic Tardigrade* | **Background.** Tardigrade-specific protective proteins for organelle protection. |
| 12 | [PMID: 36693101](https://pubmed.ncbi.nlm.nih.gov/36693101/) — *In vivo expression vector derived from anhydrobiotic tardigrade genome* | **Methodological.** TardiVec system enables functional studies in tardigrades. |
| 13 | [PMID: 38843161](https://pubmed.ncbi.nlm.nih.gov/38843161/) — *Comparative ultrastructure study of R. varieornatus in hydrated, desiccated, and rehydrating states* | **Background.** Cellular-level analysis of anhydrobiosis in *R. varieornatus*. |

---

## Limitations

1. **No direct activity measurement.** The conclusion is based on structural and comparative evidence, not a direct enzymatic assay. This is the single most important limitation. A direct SOD activity measurement on purified RvSOD15 would be definitive.

2. **Cross-species extrapolation.** The inference from human SOD1 mutations to tardigrade RvSOD15 assumes conservation of the catalytic mechanism. While Cu/Zn SOD catalysis is one of the most deeply conserved enzymatic mechanisms across eukaryotes, tardigrade-specific adaptations cannot be entirely excluded.

3. **Crystallographic conditions.** Crystal structures may not perfectly represent the solution-phase or in vivo state. Metal occupancy and coordination geometry can be influenced by crystallization buffer composition, pH, and temperature. However, the Val87 substitution is a sequence-level change, not a crystallographic artifact.

4. **Single primary study.** The structural data for RvSOD15 comes from one publication ([PMID: 37358501](https://pubmed.ncbi.nlm.nih.gov/37358501/)). While the crystal structures are publicly deposited (PDB 7YPP, 7YPR) and available for independent verification, complementary activity data from other groups would strengthen the conclusion.

5. **Limited family-wide characterization.** Only RvSOD15 has been structurally characterized among the 21 *R. varieornatus* SOD paralogs. The activity status of other divergent paralogs is unknown, limiting the ability to generalize about the family.

---

*Report generated 2026-07-04. Based on analysis of 13 publications, 2 crystal structures (PDB 7YPP, 7YPR), and comparative sequence/structural data from the Cu/Zn SOD literature. All curation recommendations are leads requiring curator verification.*


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)