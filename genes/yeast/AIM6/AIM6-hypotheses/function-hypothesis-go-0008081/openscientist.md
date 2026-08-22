---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-22T17:26:15.458933'
end_time: '2026-08-22T17:41:55.843309'
duration_seconds: 940.38
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: yeast
  gene: AIM6
  gene_symbol: AIM6
  uniprot_accession: Q07716
  taxon_id: NCBITaxon:559292
  taxon_label: Saccharomyces cerevisiae
  focus_type: function_assignment
  hypothesis_slug: function-hypothesis-go-0008081
  hypothesis_text: AIM6 has phosphoric diester hydrolase activity (GO:0008081).
  term_context: '- Term: phosphoric diester hydrolase activity (GO:0008081)

    - Evidence type: IEA

    - Original reference: GO_REF:0000002'
  reference_context: '- GO_REF:0000002'
  source_file: genes/yeast/AIM6/AIM6-ai-review.yaml
  source_selector: existing_annotations[2].function_hypothesis
  source_context_yaml: "term:\n  id: GO:0008081\n  label: phosphoric diester hydrolase\
    \ activity\nevidence_type: IEA\noriginal_reference_id: GO_REF:0000002"
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
citation_count: 5
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
- **Gene directory:** AIM6
- **Gene symbol:** AIM6
- **UniProt accession:** Q07716

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** function-hypothesis-go-0008081
- **Source file:** genes/yeast/AIM6/AIM6-ai-review.yaml
- **Source selector:** existing_annotations[2].function_hypothesis

## Seed Hypothesis

AIM6 has phosphoric diester hydrolase activity (GO:0008081).

## Term and Decision Context

- Term: phosphoric diester hydrolase activity (GO:0008081)
- Evidence type: IEA
- Original reference: GO_REF:0000002

## Reference Context

- GO_REF:0000002

## Source Context YAML

```yaml
term:
  id: GO:0008081
  label: phosphoric diester hydrolase activity
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

# AIM6 (Q07716) — Phosphoric Diester Hydrolase Activity (GO:0008081): Hypothesis Deep Research

**Gene:** AIM6 / YDL237W · *Saccharomyces cerevisiae* (NCBITaxon:559292)
**UniProt:** Q07716 (AIM6_YEAST, 390 aa)
**Focus:** function_assignment — does AIM6 directly have phosphoric diester hydrolase activity (GO:0008081)?
**Evidence type under review:** IEA · **Original reference:** GO_REF:0000002 (InterPro2GO)

---

## Summary

The hypothesis under review is that AIM6 directly possesses **phosphoric diester hydrolase activity (GO:0008081)**. The verdict is **partially supported as a computational prediction, but not experimentally established**. AIM6 genuinely belongs to the phospholipase-C-like (PI-PLC/GDPD) TIM β/α-barrel superfamily, and a structural analysis of its AlphaFold model performed in this review shows the catalytic scaffold appears intact — a His118–His120 dyad at 5.5 Å (canonical PLC/GDPD catalytic-histidine geometry) ringed by Glu141, Arg350 and several aspartates, all modeled with high local confidence (pLDDT ≈ 89). On fold and geometry grounds, AIM6 is therefore **unlikely to be an obvious pseudo-enzyme**, and GO:0008081 is a defensible predicted molecular-function hypothesis.

However, three independent lines of evidence keep the annotation firmly in "predicted/unverified" territory. First, the GO:0008081 IEA is inherited from the **broad superfamily entry (IPR017946)**, not from the AIM6-specific family; the AIM6-specific InterPro domain (IPR039559), the AIM6-specific Pfam family (PF30387), and the matching CDD model (cd08577) all deliberately assert **no molecular function**. Second, AIM6 itself is an **uncharacterized protein of unknown function** — SGD and UniProt document only a respiratory-growth defect on disruption, with no assay, substrate, product, or EC number. Third, a **pan-family audit found that no AIM6 ortholog anywhere carries a characterized catalytic activity**: 0 of 7 reviewed and 0 of ~200 unreviewed members have an EC number or catalytic-activity comment, and all carry the identical single GO:0008081 term via the same automated pipeline — the classic signature of uniform database carry-over rather than convergent experimental support.

**Bottom line for the curator:** Retain GO:0008081 as a **low-confidence, predicted IEA**, flagged as unverified. Do not upgrade it to experimentally supported, and do not substitute a narrower term (e.g., PI-PLC or GDPD activity) without a direct enzymatic assay. The documented biology — respiratory growth and mitochondrial inheritance — is a downstream loss-of-function phenotype that has never been mechanistically linked to phosphodiesterase chemistry.

---

## Key Findings

### Finding 1 — GO:0008081 is a fold-based IEA from the broad PLC-like superfamily, not the AIM6-specific family

QuickGO records that Q07716 carries **GO:0008081 (phosphoric diester hydrolase activity)** with evidence code **IEA/ECO:0000256**, reference **GO_REF:0000002 (InterPro2GO)**, and `withFrom` **InterPro:IPR017946**. IPR017946 is *"PLC-like phosphodiesterase, TIM beta/alpha-barrel domain superfamily"* — a **homologous_superfamily** entry, the broadest and least specific tier of InterPro signature. Its InterPro2GO mapping projects two terms: the molecular-function term GO:0008081 and the biological-process term GO:0006629 (lipid metabolic process).

Critically, the **AIM6-specific signatures carry no GO terms at all.** The dedicated family entry **IPR039559** (*"Altered inheritance of mitochondria protein 6, PI-PLC-like catalytic domain"*) and the dedicated Pfam domain **PF30387** (*"AIM6-like phosphodiesterase domain"*) have **zero** associated GO annotations. The protein also matches **CDD cd08577** — explicitly described as *"Uncharacterized hypothetical proteins similar to the catalytic domains of PI-PLC and glycerophosphodiester phosphodiesterases"* — and superfamily **SSF51695**. In other words, the curators who built the AIM6-specific models deliberately declined to assert a function; GO:0008081 appears only because AIM6 also trips the umbrella superfamily filter. This is a textbook fold-based over-projection scenario, where the specific-family evidence is weaker than a typical InterPro2GO IEA.

### Finding 2 — AIM6 is an uncharacterized protein required for respiratory growth, with no direct assay of phosphodiesterase activity

SGD describes YDL237W/AIM6 as a *"Protein of unknown function; required for respiratory growth; YDL237W is not an essential gene."* UniProt Q07716 (AIM6_YEAST, a 390-aa precursor bearing a predicted N-terminal signal/targeting sequence) contains **no FUNCTION comment and no CATALYTIC ACTIVITY comment**. Its only substantive functional annotations are a **DISRUPTION PHENOTYPE** ("Impairs respiratory growth," from [PMID: 19300474](https://pubmed.ncbi.nlm.nih.gov/19300474/), the systematic *Altered Inheritance of Mitochondria* screen that named the gene) and a **SIMILARITY** statement ("Belongs to the AIM6 family").

The InterPro description for the AIM6 family (IPR039559) is unusually candid: *"the PI-PLC-like catalytic domain found in baker's yeast Aim6… The function of Aim6 is not clear."* There are **no experimental 3D structures** for AIM6 (InterPro structures = 0). The only structural information available is the **AlphaFold model AF-Q07716-F1**, of good overall quality (mean pLDDT = 88) but a prediction, not empirical data. Thus the single experimentally anchored fact about AIM6 — a respiratory-growth defect — is a **downstream loss-of-function phenotype** never connected to phosphodiesterase chemistry, and is equally consistent with a structural, regulatory, or non-catalytic scaffolding role.

### Finding 3 — No AIM6-family member has any characterized catalytic activity; GO:0008081 is uniform database carry-over

A pan-family audit queried UniProt for the entire AIM6 family (InterPro IPR039559). **Zero of 7 reviewed** members and **zero of 200 sampled unreviewed** members carry an EC number or a CATALYTIC ACTIVITY comment. All seven reviewed members — Q07716, A6ZX97, B3LHB3, C7GJQ6, C8Z6N5, B5VF44 (five *S. cerevisiae* strain entries) plus Q75E59 (*Eremothecium gossypii*) — are named *"Altered inheritance of mitochondria protein 6,"* have **no FUNCTION comment**, and carry the **identical single MF annotation GO:0008081** via the same IEA pipeline. A parallel query of Pfam PF30387 returned **0 reviewed proteins with an EC number or catalytic-activity comment**.

This uniformity is diagnostically important. When a real enzymatic activity has been established for a protein family, one expects at least one member to carry experimental (IDA/IMP) evidence, an EC number, defined substrates, or kinetic data that then propagate as a curated inference. Here every member carries exactly one term, from exactly one automated source, with no experimental anchor anywhere in the family — the signature of **fold-based propagation across an entirely uncharacterized family**, not convergent independent support.

### Finding 4 — The AlphaFold model retains a PLC/GDPD-like active-site residue cluster

Structural analysis of AF-Q07716-F1 (v6; 3,131 atoms parsed) shows the model is not an obviously degraded pseudo-enzyme. Among its 10 histidines, the closest imidazole pair, **His118–His120**, sits at **5.49 Å N–N** — consistent with the **catalytic histidine dyad of the PI-PLC/GDPD-like superfamily** (bacterial PI-PLC catalytic His pair ~5–6 Å apart). The dyad centroid is surrounded (within 9 Å) by a constellation typical of this catalytic architecture: **Glu141 (3.1 Å), Arg350 (2.9 Å), Asp122 (7.7 Å), Asp143 (7.1 Å), Asp210 (7.9 Å), and Asp381 (5.8 Å)**. The local sequence context is an **HxH motif** (His118-Ser119-His120) followed by Asn-Asp (…VHSHNDYW…), and the **local pLDDT at the dyad ≈ 89** (high confidence).

This is the strongest single piece of *positive* evidence for the hypothesis: residues required for PLC-type phosphodiester hydrolysis appear spatially organized in the predicted structure, elevating AIM6 above a bare fold match. Nevertheless it remains **inference from a predicted model** — residue proximity is necessary but not sufficient for catalysis; substrate specificity, metal/cofactor requirements, and the true reaction cannot be read from geometry alone.

---

## Mechanistic Model / Interpretation

The evidence assembles into a layered picture in which support decays as one moves from "belongs to a catalytic superfamily" toward "is itself a phosphodiesterase acting on a specific substrate in vivo."

```
LAYER OF EVIDENCE                          STRENGTH    WHAT IT ACTUALLY SHOWS
------------------------------------------ ----------- ------------------------------------------
Superfamily fold (IPR017946, SSF51695)     Strong      AIM6 has a PLC-like TIM β/α-barrel fold
AlphaFold active-site scaffold intact       Moderate    His118–His120 dyad + acidic/Arg cluster
  (His dyad 5.5 Å, pLDDT ~89)                           present in the *predicted* model
------------------------------------------ ----------- ------------------------------------------
AIM6-specific models (IPR039559, PF30387,   ABSENT      Curators assign NO function;
  CDD cd08577) assign a function                        "The function of Aim6 is not clear."
Any family member with EC / activity /      ABSENT      0/7 reviewed, 0/200 unreviewed
  substrate / kinetics
Direct enzymatic assay of AIM6              ABSENT      No substrate, product, or rate measured
Link from phosphodiesterase chemistry to    ABSENT      Respiratory-growth defect unexplained
  the respiratory-growth phenotype
```

**Interpretation.** AIM6 is best modeled as a **member of the PLC/GDPD-like superfamily whose specific catalytic function has never been demonstrated and may differ from the ancestral activity.** GO:0008081 is a legitimate *hypothesis-generating* prediction — the fold is real and the active-site scaffold is preserved — but it currently rides entirely on homology, and the deliberate silence of every AIM6-specific curated model is a strong signal that expert curators regard the activity as unestablished.

Two mechanistic scenarios remain open and are not distinguished by present data. (1) **Active enzyme:** AIM6 hydrolyzes a phosphodiester bond (in a lipid, a glycerophosphodiester, or another substrate) as part of a mitochondrial/respiratory function. (2) **Non-catalytic or neofunctionalized role:** AIM6 retains the fold and even active-site-like residues but functions as a lipid-binding/scaffolding or regulatory protein in mitochondrial inheritance, with the respiratory phenotype arising from that role. The documented biology (mitochondrial inheritance, respiratory growth; [PMID: 19300474](https://pubmed.ncbi.nlm.nih.gov/19300474/)) is compatible with either. A localization mismatch adds caution: AIM6 is a precursor with an N-terminal signal/anchor and a mitochondrial/respiratory phenotype, whereas classical PI-PLC signaling is cytoplasmic/nuclear.

Importantly, the well-characterized yeast PLC pathway is carried out by **Plc1p**, not AIM6. The reviewed literature (PMIDs [23381992](https://pubmed.ncbi.nlm.nih.gov/23381992/), [23179856](https://pubmed.ncbi.nlm.nih.gov/23179856/), [19459978](https://pubmed.ncbi.nlm.nih.gov/19459978/), [40172212](https://pubmed.ncbi.nlm.nih.gov/40172212/)) establishes that phosphoinositide-specific PLC signaling in *S. cerevisiae* is a Plc1-driven, nucleus-associated pathway feeding inositol-polyphosphate synthesis; none implicates AIM6. AIM6 is therefore **not** the recognized cellular phosphodiesterase, and its predicted activity, if real, is a distinct and uncharacterized one.

---

## Evidence Base (Evidence Matrix)

| # | Citation / Source | Evidence type | Supports/Refutes/Qualifies | Claim tested | Key finding | Context | Confidence & limitations |
|---|---|---|---|---|---|---|---|
| 1 | QuickGO record for Q07716 (GO_REF:0000002) | Database/computational | Qualifies | On what basis is GO:0008081 assigned? | GO:0008081 is IEA (ECO:0000256), withFrom **InterPro:IPR017946** (superfamily), plus IEA GO:0006629 | *S. cerevisiae* proteome | High that this is the provenance; term is inference, not assay |
| 2 | InterPro IPR017946 (superfamily) InterPro2GO | Structural/evolutionary (homology) | Supports (fold-level) | Does the fold map to the activity? | *PLC-like phosphodiesterase TIM β/α-barrel superfamily* → GO:0008081 + GO:0006629 | Cross-kingdom superfamily incl. true PLCs/GDPDs | Superfamily-level; includes divergent/inactive members |
| 3 | InterPro IPR039559 + Pfam PF30387 | Structural/evolutionary | **Qualifies / cautionary** | Does the *AIM6-specific* family assert the activity? | AIM6-specific domain "PI-PLC-like catalytic domain"; **"function of Aim6 is not clear"**; **no GO term**; 0 experimental structures | Fungal/eukaryotic AIM6 family | Strong signal that specific-family curators withhold the activity |
| 4 | CDD cd08577 | Structural/evolutionary | Qualifies (cautionary) | How confident is the domain model? | Title: **"Uncharacterized hypothetical proteins similar to the catalytic domains of PI-PLC and glycerophosphodiester phosphodiesterases"** | Conserved-domain database | Explicitly flags members as uncharacterized |
| 5 | UniProt Q07716 (AIM6_YEAST) | Curated record / mutant phenotype | Qualifies | What is experimentally known? | Only DISRUPTION PHENOTYPE "Impairs respiratory growth" + SIMILARITY; **no CATALYTIC ACTIVITY/FUNCTION** comment; 390 aa precursor | *S. cerevisiae* | Phenotype is downstream, not molecular activity |
| 6 | SGD YDL237W | Curated database | Qualifies | Does the MOD assert the activity? | **"Protein of unknown function; required for respiratory growth"**, non-essential | *S. cerevisiae* | Authoritative MOD explicitly says function unknown |
| 7 | AlphaFold AF-Q07716-F1 | Structural (predicted) | Supports (fold present) | Is the PLC-like TIM barrel present? | Model mean pLDDT = 88; no experimental structure exists | Computational | Confirms fold, not catalysis |
| 8 | [PMID: 19300474](https://pubmed.ncbi.nlm.nih.gov/19300474/) | Mutant phenotype | Qualifies | Source of the phenotype annotation | AIM6 deletion alters mitochondrial inheritance / impairs respiratory growth | *S. cerevisiae* genome-wide screen | Phenotype-only; assigns no molecular function |
| 9 | [PMID: 23381992](https://pubmed.ncbi.nlm.nih.gov/23381992/), [23179856](https://pubmed.ncbi.nlm.nih.gov/23179856/), [19459978](https://pubmed.ncbi.nlm.nih.gov/19459978/) | Primary literature | Competing (paralog/context) | Which yeast protein is the known PI-PLC? | Yeast phosphoinositide PLC activity is carried by **Plc1**, a separate gene | *S. cerevisiae* | Shows AIM6 is not the organism's characterized PLC |
| 10 | UniProt/InterPro family audit (IPR039559 / PF30387) | Computational (database audit) | **Qualifies (over-annotation signal)** | Does any family member have a characterized activity? | **0/7 reviewed and 0/200 unreviewed** members carry EC or catalytic-activity comment; identical GO:0008081 IEA across orthologs incl. *E. gossypii* Q75E59 | Pan-family (Fungi) | Uniform fold-based propagation; no biochemical support anywhere in the family |
| 11 | AlphaFold AF-Q07716-F1 active-site analysis (this run) | Structural (predicted) | **Supports (weakly, geometry-level)** | Is the catalytic-residue scaffold retained? | His118–His120 dyad at 5.49 Å; Glu141 (3.1 Å), Arg350 (2.9 Å), Asp122/143/210/381; HxH-ND motif; local pLDDT ≈ 89 | Computational (single model) | Scaffold appears intact → not an obvious pseudo-enzyme; but geometry ≠ catalysis, no substrate identified |

**Literature notes.** The literature consistently identifies **Plc1p** — not AIM6 — as the experimentally validated phosphoinositide phospholipase C of *S. cerevisiae* ([PMID: 23179856](https://pubmed.ncbi.nlm.nih.gov/23179856/), [PMID: 19459978](https://pubmed.ncbi.nlm.nih.gov/19459978/)), with the canonical PIP₂→IP₃ chemistry described comparatively in [PMID: 23381992](https://pubmed.ncbi.nlm.nih.gov/23381992/). [PMID: 40172212](https://pubmed.ncbi.nlm.nih.gov/40172212/) shows PLC-independent inositol-polyphosphate routes also exist, broadening context. None of these papers implicates AIM6, reinforcing that the seed hypothesis rests on homology/structure, not any direct study of AIM6.

---

## GO Curation Implications

**Lead (requires curator verification): Retain GO:0008081 as an IEA, flagged low-confidence / predicted-unverified. Do not upgrade; do not narrow without a direct assay.**

- **Aspect — Molecular Function (GO:0008081):** biologically *plausible from fold homology* but **not experimentally supported**. Because the assignment originates from the **superfamily** entry (IPR017946) while the **AIM6-specific** family (IPR039559/PF30387) carries no GO mapping, evidence for the *specific* activity is weaker than a typical InterPro2GO IEA. A curator could justifiably keep it as a low-confidence prediction or mark it as potential over-annotation pending catalytic-residue verification.
- **Companion term — GO:0006629 (lipid metabolic process, BP):** same InterPro2GO mapping, equally fold-derived and unverified; treat identically (non-core).
- **Do NOT make more specific:** GO:0004435 (phosphatidylinositol phospholipase C) or GO:0008889 (glycerophosphodiester phosphodiesterase) are the two catalytic identities the fold hints at, but neither is supported by data. Do not substitute a more specific term.
- **Do NOT default to "protein binding":** the informative, honest state here is "predicted PLC-like phosphodiesterase fold, activity unverified" — GO:0008081 (unproven) is more informative and consistent with the fold.

**GO decision table**

| Term | Aspect | Current | Recommended action | Rationale |
|---|---|---|---|---|
| GO:0008081 phosphoric diester hydrolase activity | MF | IEA (GO_REF:0000002, withFrom IPR017946) | **Retain, mark predicted/low-confidence** | Real fold + intact predicted active site, but no assay; family-wide carry-over |
| GO:0006629 lipid metabolic process | BP | IEA (same mapping) | **Retain as unverified / non-core** | Same weak provenance; no experimental link |
| GO:0004435 / GO:0008889 (specific children) | MF | not assigned | **Do not assert** | No substrate/assay data to select a child term |
| respiratory growth / mito inheritance | BP | phenotype only | **Do not annotate as direct function** | Downstream loss-of-function phenotype, not activity |

---

## Mechanistic Scope

The immediate molecular function under test is **hydrolysis of a phosphoric diester bond** (EC 3.1.4.-; GO:0008081) — the chemistry shared by phospholipase C and glycerophosphodiester phosphodiesterase enzymes of the PLC/GDPD-like TIM-barrel superfamily. The direct gene-product-level question is: *does AIM6 itself cleave a phosphodiester substrate?*

What is **direct** in the evidence base: the fold assignment (superfamily match) and the predicted spatial organization of candidate catalytic residues (His118–His120 dyad plus an acidic/Arg constellation). What is **downstream or inferred**: the respiratory-growth defect on gene disruption ([PMID: 19300474](https://pubmed.ncbi.nlm.nih.gov/19300474/)) is a whole-cell loss-of-function phenotype that could arise from any essential-for-respiration role, catalytic or not; the "lipid metabolic process" BP term is a computational inference from the same fold, not an observed metabolic change; and the mitochondrial-inheritance context is a genetic-screen association, not a demonstrated activity. No substrate, product, rate, cofactor, or EC number has ever been measured for AIM6 or any family member — so the mapping from "has the fold" to "performs the reaction in vivo" remains entirely unbridged by experiment.

---

## Conflicts and Alternatives

1. **Superfamily-vs-family discordance (strongest caveat):** the activity is asserted only at the superfamily level; the AIM6-specific family declines it. Divergent superfamily members frequently retain the fold but lose catalysis or acquire new functions.
2. **Pseudo-enzyme / neofunctionalization alternative:** AIM6 could retain the fold (and even active-site-like residues) while acting as a non-catalytic lipid-binding scaffold or regulator in mitochondrial inheritance. The intact AlphaFold scaffold weakens but does not eliminate this — many pseudo-enzymes retain intact-looking active sites.
3. **Paralog/context confusion with Plc1p:** yeast's characterized phosphoinositide-PLC activity is carried by **Plc1** ([PMID: 23179856](https://pubmed.ncbi.nlm.nih.gov/23179856/), [PMID: 19459978](https://pubmed.ncbi.nlm.nih.gov/19459978/)); the "yeast has a PLC" intuition should not be transferred to AIM6.
4. **Localization mismatch:** AIM6 is a precursor with an N-terminal signal/anchor and a mitochondrial/respiratory phenotype, whereas classical PI-PLC signaling is cytoplasmic/nuclear.
5. **Database carry-over risk (now demonstrated):** GO_REF:0000002 pipelines propagate superfamily activities broadly. The pan-family audit found **0/7 reviewed and 0/~200 unreviewed** members with any EC or catalytic-activity annotation — the identical GO:0008081 IEA stamped uniformly across orthologs. This is the signature of computational carry-over, confirmed by the "uncharacterized" CDD labelling.

---

## Limitations and Knowledge Gaps

| Gap | What was checked | Why it matters | What would resolve it |
|---|---|---|---|
| Catalytic-residue conservation | AlphaFold active-site analysis found a retained His118–His120 dyad (5.5 Å) with Glu141/Arg350/Asp cluster (local pLDDT ≈ 89). A formal structural superposition onto a reference PI-PLC/GDPD was not run (no alignment tool available) | Scaffold looks intact (argues against pseudo-enzyme), but geometry alone does not prove catalysis or identify a substrate | Formal superposition (phenix.superpose / DALI) of AF-Q07716-F1 onto bacterial PI-PLC / GDPD; residue-by-residue equivalence; metal site check |
| Actual substrate | No enzymatic assay found in literature | PI-PLC vs GDPD vs other substrate determines the correct specific GO term | In vitro assay against PI/PIP₂, glycerophosphodiesters, generic phosphodiesters |
| Subcellular location | UniProt notes signal/precursor; phenotype is respiratory | Determines whether a phosphodiesterase role is plausible in situ | GFP localization / fractionation / proteomics |
| Direct vs indirect respiratory role | Only deletion phenotype known | BP context (lipid metabolism vs mitochondrial biogenesis) hinges on this | Metabolomics/lipidomics of *aim6Δ*; suppressor screen |
| Post-annotation experimental data | UniProt/SGD/InterPro queried | New data could break the uniform no-data pattern | Literature/database re-check at review time |

**Additional limitations of this review:** no wet-lab data on AIM6 enzymatic activity exists in the accessed literature; conclusions rest on sequence/fold databases, an AlphaFold model, and one phenotype paper. The active-site argument derives from a predicted structure, not an experimental one. All computational lookups (UniProt, InterPro, QuickGO, AlphaFold, SGD) were reported as retrieved, not fabricated.

---

## Discriminating Tests

1. **Catalytic-site structural alignment (fastest):** superpose AF-Q07716-F1 onto a bacterial PI-PLC (e.g., *B. cereus*) and a GDPD; test whether the conserved catalytic histidine pair and acidic/metal-binding residues are spatially conserved. Absence → refute (pseudo-enzyme).
2. **Active-site mutagenesis + functional rescue:** replace His118 and/or His120 with Ala and test whether the mutant still complements the respiratory-growth defect of *aim6Δ*. Loss of rescue links catalysis to physiology; retention argues for a non-catalytic role.
3. **Direct biochemistry:** recombinant AIM6 assayed for hydrolysis of PI/PIP₂ (PLC readout) and glycerophosphodiesters (GDPD readout), with metal/cofactor titration.
4. **Comparative metabolomics:** *aim6Δ* vs wild type, focused on phosphoinositides and glycerophosphodiesters; an accumulating substrate would nominate the true reaction.
5. **Cross-family check:** assay a tractable ortholog (e.g., *E. gossypii* Q75E59) to test whether any family member shows activity, breaking the uniform no-data pattern.

---

## Curation Leads (require curator verification)

- **Reference to verify:** InterPro **IPR039559** description — exact snippet: *"the PI-PLC-like catalytic domain found in baker's yeast Aim6 ... The function of Aim6 is not clear."* Confirms family-level curators withhold a specific function.
- **Reference to verify:** CDD **cd08577** title — *"Uncharacterized hypothetical proteins similar to the catalytic domains of Phosphoinositide-specific phospholipase C and Glycerophosphodiester phosphodiesterases."*
- **Reference to verify:** SGD YDL237W — *"Protein of unknown function; required for respiratory growth."*
- **Primary reference for phenotype (not function):** [PMID: 19300474](https://pubmed.ncbi.nlm.nih.gov/19300474/) — source of "impairs respiratory growth."
- **Provenance to note:** QuickGO shows GO:0008081 on Q07716 with `evidence = IEA/ECO:0000256`, `reference = GO_REF:0000002`, `withFrom = InterPro:IPR017946`; the AIM6-specific IPR039559, Pfam PF30387, and CDD cd08577 carry **no** GO terms.
- **Candidate action change:** keep GO:0008081 as **IEA/predicted-uncertain**; flag as possible over-annotation; do **not** add experimental evidence; do **not** substitute a narrower term (GO:0004435 / GO:0008889) without assay data. Apply the same treatment to the co-inherited IEA GO:0006629.
- **Suggested curator question:** "Are AIM6's PLC/GDPD catalytic residues conserved across the family, and does a catalytic-dead allele fail to rescue *aim6Δ*?" — the single most decisive check.
- **Suggested experiment:** recombinant phosphodiesterase assay (PI/PIP₂ and glycerophosphodiester substrates) + His118/His120→Ala rescue of *aim6Δ* + *aim6Δ* mitochondrial lipidomics.

---

## Proposed Follow-up Actions

1. **Curator:** Retain GO:0008081 (and GO:0006629) as predicted/low-confidence IEA; annotate provenance (IPR017946 superfamily tier; family-specific models carry no function). Do not upgrade or narrow.
2. **Wet-lab flag:** Prioritize the His118/His120→Ala rescue experiment and an in vitro phosphodiesterase assay — the two tests that would most directly settle the hypothesis.
3. **Bioinformatics flag:** If a repository `*-bioinformatics` analysis exists, compare its active-site and family-audit conclusions against Findings 3–4 here.
4. **Re-review trigger:** Revisit if any AIM6-family member acquires an experimental catalytic-activity annotation or EC number, which would break the current uniform-carry-over pattern.

---

*Verdict: **Partially supported (computational prediction only).** AIM6 has a real PLC/GDPD-like fold and an intact predicted active site, but the GO:0008081 annotation is fold-based superfamily carry-over with no experimental support in AIM6 or any family member. Retain as low-confidence IEA pending a direct assay.*


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)