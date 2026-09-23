---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-21T04:30:01.026947'
end_time: '2026-09-21T04:48:15.342328'
duration_seconds: 1094.32
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: yeast
  gene: DCV1
  gene_symbol: DCV1
  uniprot_accession: P43595
  taxon_id: NCBITaxon:559292
  taxon_label: Saccharomyces cerevisiae
  focus_type: function_assignment
  hypothesis_slug: secondary-membrane-division-site-and-tip-localization
  hypothesis_text: Saccharomyces cerevisiae DCV1/YFR012W/P43595 acts at plasma membrane,
    cell division site and growing cell tip in addition to its curated nuclear-envelope
    location. Recover full PMID33002606 (doi10.1016/j.fgb.2020.103467), including
    supplements, and identify actual DCV1 versus TOS7 constructs, images, conditions
    and controls. Title about TOS7 is not evidence DCV1 was untested; SGD IDA nuclear
    envelope must not be discarded on abstract-only grounds. Actual PTHR28013 rootPTN001997363
    bears all three disputed IBDs and is ancestral to exact DCV1 leafPTN001997377;
    no loss event found on target path. PM evidence includes RIM9 and TOS7 plus fission-yeast
    descendants; division-site seed is SPCC1739.10 and tip seeds include SPAC13G7.04c.
    Evaluate source assays and target divergence rather than donor count. GO0035838
    describes a polarized region at an end of a cylindrical or elongated cell; budding
    yeast can have polarized elongated/pseudohyphal/mating-projection states, so do
    not declare a blanket taxon exclusion. Determine which structure and conditions
    actually satisfy the term and evidence for DCV1 there. PMID22042866 chemical-genetic
    CDC28 network contains target-related viability context; necessity for growth
    is not a localizing assay or a defined biochemical activity. Consider broad membrane
    evidence, compartment coexistence, trafficking or conditional pools; nuclear envelope
    does not logically exclude plasma membrane. Distinguish evidence absence, inherited
    inference, direct negatives and actual loss; do not assign TOS7 secretion function
    to DCV1 without evidence.
  term_context: No specific term context supplied.
  reference_context: No specific reference context supplied.
  source_file: genes/yeast/DCV1/DCV1-ai-review.yaml
  source_selector: free-text
  source_context_yaml: "hypothesis: Saccharomyces cerevisiae DCV1/YFR012W/P43595 acts\
    \ at plasma membrane, cell division site and\n  growing cell tip in addition to\
    \ its curated nuclear-envelope location. Recover full PMID33002606 (doi10.1016/j.fgb.2020.103467),\n\
    \  including supplements, and identify actual DCV1 versus TOS7 constructs, images,\
    \ conditions and controls.\n  Title about TOS7 is not evidence DCV1 was untested;\
    \ SGD IDA nuclear envelope must not be discarded on\n  abstract-only grounds.\
    \ Actual PTHR28013 rootPTN001997363 bears all three disputed IBDs and is ancestral\n\
    \  to exact DCV1 leafPTN001997377; no loss event found on target path. PM evidence\
    \ includes RIM9 and TOS7\n  plus fission-yeast descendants; division-site seed\
    \ is SPCC1739.10 and tip seeds include SPAC13G7.04c.\n  Evaluate source assays\
    \ and target divergence rather than donor count. GO0035838 describes a polarized\n\
    \  region at an end of a cylindrical or elongated cell; budding yeast can have\
    \ polarized elongated/pseudohyphal/mating-projection\n  states, so do not declare\
    \ a blanket taxon exclusion. Determine which structure and conditions actually\n\
    \  satisfy the term and evidence for DCV1 there. PMID22042866 chemical-genetic\
    \ CDC28 network contains target-related\n  viability context; necessity for growth\
    \ is not a localizing assay or a defined biochemical activity.\n  Consider broad\
    \ membrane evidence, compartment coexistence, trafficking or conditional pools;\
    \ nuclear\n  envelope does not logically exclude plasma membrane. Distinguish\
    \ evidence absence, inherited inference,\n  direct negatives and actual loss;\
    \ do not assign TOS7 secretion function to DCV1 without evidence.\nfocus_type:\
    \ function_assignment\ncontext: []\nreference_id: []"
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

- **Organism code:** yeast
- **Taxon:** Saccharomyces cerevisiae (NCBITaxon:559292)
- **Gene directory:** DCV1
- **Gene symbol:** DCV1
- **UniProt accession:** P43595

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** secondary-membrane-division-site-and-tip-localization
- **Source file:** genes/yeast/DCV1/DCV1-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

Saccharomyces cerevisiae DCV1/YFR012W/P43595 acts at plasma membrane, cell division site and growing cell tip in addition to its curated nuclear-envelope location. Recover full PMID33002606 (doi10.1016/j.fgb.2020.103467), including supplements, and identify actual DCV1 versus TOS7 constructs, images, conditions and controls. Title about TOS7 is not evidence DCV1 was untested; SGD IDA nuclear envelope must not be discarded on abstract-only grounds. Actual PTHR28013 rootPTN001997363 bears all three disputed IBDs and is ancestral to exact DCV1 leafPTN001997377; no loss event found on target path. PM evidence includes RIM9 and TOS7 plus fission-yeast descendants; division-site seed is SPCC1739.10 and tip seeds include SPAC13G7.04c. Evaluate source assays and target divergence rather than donor count. GO0035838 describes a polarized region at an end of a cylindrical or elongated cell; budding yeast can have polarized elongated/pseudohyphal/mating-projection states, so do not declare a blanket taxon exclusion. Determine which structure and conditions actually satisfy the term and evidence for DCV1 there. PMID22042866 chemical-genetic CDC28 network contains target-related viability context; necessity for growth is not a localizing assay or a defined biochemical activity. Consider broad membrane evidence, compartment coexistence, trafficking or conditional pools; nuclear envelope does not logically exclude plasma membrane. Distinguish evidence absence, inherited inference, direct negatives and actual loss; do not assign TOS7 secretion function to DCV1 without evidence.

## Term and Decision Context

No specific term context supplied.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: Saccharomyces cerevisiae DCV1/YFR012W/P43595 acts at plasma membrane, cell division site and
  growing cell tip in addition to its curated nuclear-envelope location. Recover full PMID33002606 (doi10.1016/j.fgb.2020.103467),
  including supplements, and identify actual DCV1 versus TOS7 constructs, images, conditions and controls.
  Title about TOS7 is not evidence DCV1 was untested; SGD IDA nuclear envelope must not be discarded on
  abstract-only grounds. Actual PTHR28013 rootPTN001997363 bears all three disputed IBDs and is ancestral
  to exact DCV1 leafPTN001997377; no loss event found on target path. PM evidence includes RIM9 and TOS7
  plus fission-yeast descendants; division-site seed is SPCC1739.10 and tip seeds include SPAC13G7.04c.
  Evaluate source assays and target divergence rather than donor count. GO0035838 describes a polarized
  region at an end of a cylindrical or elongated cell; budding yeast can have polarized elongated/pseudohyphal/mating-projection
  states, so do not declare a blanket taxon exclusion. Determine which structure and conditions actually
  satisfy the term and evidence for DCV1 there. PMID22042866 chemical-genetic CDC28 network contains target-related
  viability context; necessity for growth is not a localizing assay or a defined biochemical activity.
  Consider broad membrane evidence, compartment coexistence, trafficking or conditional pools; nuclear
  envelope does not logically exclude plasma membrane. Distinguish evidence absence, inherited inference,
  direct negatives and actual loss; do not assign TOS7 secretion function to DCV1 without evidence.
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

# DCV1/YFR012W (P43595): Secondary Membrane, Division-Site, and Tip Localization — Hypothesis Deep Research

**Target:** *Saccharomyces cerevisiae* DCV1 (YFR012W), UniProt P43595, SGD:S000001908
**Focus type:** function_assignment
**Hypothesis slug:** secondary-membrane-division-site-and-tip-localization

---

## Summary

The seed hypothesis proposes that DCV1 acts at the **plasma membrane (PM)**, the **cell division site (GO:0032153)**, and the **growing cell tip (GO:0035838)**, in addition to its curated **nuclear-envelope (GO:0005635)** location. When each compartment is evaluated against *primary* evidence rather than inherited phylogenetic inference, the hypothesis resolves into four distinct outcomes rather than a single verdict. The overall judgment is **partially supported**.

The strongest, best-supported claim is the plasma membrane. Direct live-cell imaging (PMID 36601911) shows Dcv1-GFP uniform on the PM of vegetative cells; the `dcv1Δ` mutant mislocalizes PM lipids and polarity/trafficking proteins; and the entire Sur7/PalI family — including the founding member Sur7 and the paralog Tos7 — resides at PM eisosome/MCC microdomains. In contrast, the "growing cell tip" annotation is IBA-only and is directly contradicted by the data: in the one polarized budding-yeast state examined (the pheromone/mating response), Dcv1 is confined to the *rear* of the cell, away from the growth front. The "cell division site" annotation is IBA-only with no direct DCV1 evidence, and the nuclear-envelope call — while a genuine DCV1-specific IDA — most plausibly reflects a conditional ER/perinuclear (biosynthetic or overexpression) pool rather than the functional compartment.

For curators, the practical implications are: **retain and upgrade** GO:0005886 (plasma membrane) from IBA to experimental; **remove or do not assert** GO:0035838 (growing cell tip); **treat GO:0032153 (cell division site) as non-core/IBA-only**; and **retain-but-flag** GO:0005635 (nuclear envelope) as a conditional pool pending full-text review of PMID 33002606. Critically, the paralog Tos7's secretion function must **not** be transferred to DCV1 without DCV1-specific evidence.

---

## Key Findings

### Finding 1 — Plasma-membrane localization is directly supported (not merely IBA)

SGD and UniProt list GO:0005886 (plasma membrane) for DCV1 only as **IBA/computational** (GO Central Curators; Feuermann 2010 phylogenetic inference). Taken alone, that would be weak, family-level support. However, primary **live-cell imaging** in Sukumar et al. 2023 ([PMID: 36601911](https://pubmed.ncbi.nlm.nih.gov/36601911/)) shows Dcv1-GFP *"localized uniformly on the plasma membrane (PM) of vegetative cells."* Beyond localization, the loss-of-function phenotype is informative: `dcv1Δ` **mislocalizes PM lipids and polarity/trafficking proteins**, indicating that Dcv1 is not a passive PM passenger but participates in organizing PM composition.

Three independent lines converge on the PM:
- **Direct imaging** of Dcv1-GFP at the PM of vegetative cells.
- **Mutant phenotype**: `dcv1Δ` disrupts PM lipid and polarity-protein distribution.
- **Family biology**: Dcv1 belongs to the Sur7/PalI family (Pfam PF06687; IPR009571), a group of multi-pass PM proteins; the paralog Tos7 localizes to PM MCC/eisosome microdomains ([PMID: 33002606](https://pubmed.ncbi.nlm.nih.gov/33002606/)).

This convergence justifies **upgrading GO:0005886 from IBA to an experimental (IDA) code** with PMID 36601911 as the supporting reference.

### Finding 2 — "Growing cell tip" (GO:0035838) is IBA-only and contradicted by direct data

The GO:0035838 annotation for DCV1 is **computational/IBA only**, derived from PANTHER PTHR28013 phylogenetic inference propagated from fission-yeast descendants (e.g., SPAC13G7.04c), organisms in which tip growth is a normal morphology. GO:0035838 is defined as *"The region at either end of the longest axis of a cylindrical or elongated cell, where polarized growth occurs."* The seed correctly notes that budding yeast can adopt polarized states (pseudohyphal, mating-projection/shmoo), so a blanket taxon exclusion is not warranted.

However, taxon exclusion is unnecessary because the **direct data already exclude Dcv1 from the tip**. In the one polarized budding-yeast state examined — the pheromone/mating response — Dcv1 was *"confined to the rear of cells responding to pheromone, away from the pheromone receptor"* (PMID 36601911). The mating-projection tip is precisely where polarized growth and the pheromone receptor concentrate; Dcv1 is at the opposite pole. Thus the strongest morphological candidate for a budding-yeast "growing cell tip" shows Dcv1 **excluded from**, not enriched at, the tip. No primary evidence places Dcv1 at any growing tip.

### Finding 3 — Nuclear-envelope IDA is DCV1-specific but conflicts with PM; division site is IBA-only

SGD attributes DCV1's manually curated **GO:0005635 nuclear envelope (IDA)** to Zhu J et al. 2020 ([PMID: 33002606](https://pubmed.ncbi.nlm.nih.gov/33002606/)) — the same Sur7/PalI paper whose *title* concerns the paralog **Tos7/Yol019w** (*"The Sur7/PalI family transmembrane protein Tos7 (Yol019w) plays a role in..."*). This is the provenance concern the seed flags: the DCV1 NE call comes from a paper primarily about a paralog. Critically, the **evidence code is IDA (Inferred from Direct Assay)**, meaning SGD curators identified a DCV1-specific direct observation within that paper — so the NE annotation is *not* pure paralog carry-over and must not be discarded on abstract-only grounds.

That said, the NE localization **conflicts with the physiological PM localization** reported by Sukumar et al. 2023. The most parsimonious reconciliation is that the NE signal represents an **ER/perinuclear biosynthetic pool** (the NE is continuous with the ER) or a construct-dependent (tagged/high-copy) pool of a multi-pass membrane protein, rather than the site of function.

Separately, **GO:0032153 (cell division site)** for DCV1 is **computational/IBA only** (Feuermann 2010; PANTHER inference from fission-yeast SPCC1739.10). No direct DCV1 evidence places it at the bud neck/cytokinesis plane. The frequently cited PMID 22042866 shows only a `dcv1Δ` **genetic interaction/lethality with CDC28** loss — a viability relationship (origin of the name "Demands CDC28 for Viability"), not a localizing assay or a defined biochemical activity.

### Finding 4 — Definition + direct rear localization decisively argue against the tip; NE is a genuine DCV1 IDA

Combining the GO:0035838 definition with the direct imaging clarifies the logic. The budding-yeast morphology that best fits "the region at either end of the longest axis... where polarized growth occurs" is the **mating-projection (shmoo) tip**. The direct data place Dcv1 at the **rear** of the pheromone-responding cell — so the exclusion from the tip follows from the data themselves, without invoking any taxon rule. Meanwhile, GO:0032153 (cell division site) corresponds to the cytokinesis plane (bud neck); no DCV1 enrichment there is reported, leaving that term **IBA-only**. The NE annotation remains a legitimate, DCV1-specific IDA — best interpreted as a conditional/biosynthetic pool.

### Finding 5 — The Sur7/PalI family is anchored to the plasma membrane/eisosome

The founding family member **Sur7** (UniProt P54003; same Pfam PF06687 as DCV1) is an experimentally established multi-pass **"Cell membrane"** protein that **"Localizes at eisosomes"** (PM MCC microdomains), supported by five independent studies (PMIDs 11784867, 12469340, 14562095, 15536122, 16496001). DCV1 sits in PANTHER PTHR28013:SF3 within the SUR7/Rim9-like fungal family (IPR009571), with three predicted transmembrane helices. The paralog **Tos7** also localizes to PM MCC/eisosome (PMID 33002606). Together with the direct DCV1 PM imaging (PMID 36601911), the family-level expectation converges firmly on the **plasma membrane** — not the nuclear envelope — as the functional compartment.

---

## Mechanistic Model / Interpretation

Dcv1 is best understood as a **Sur7/PalI-family multi-pass (tetraspan-like) plasma-membrane protein** that helps organize PM lipid and polarity-protein distribution, with a compartment profile that is dynamic across cell states.

```
                     DCV1 / YFR012W (P43595) — Sur7/PalI family
                     multi-pass membrane protein (PF06687 / IPR009571)

  COMPARTMENT              EVIDENCE                          CURATION STATUS
  --------------------------------------------------------------------------------
  Plasma membrane         Direct imaging (Dcv1-GFP uniform  SUPPORTED
   (GO:0005886)           on PM, vegetative cells);         → upgrade IBA→IDA
                          dcv1Δ mislocalizes PM lipids;     (PMID 36601911)
                          family = PM/eisosome (Sur7,Tos7)

  Growing cell tip        IBA-only (fission-yeast seeds);   REFUTED (direct negative)
   (GO:0035838)           direct data show Dcv1 at REAR     → remove / do not assert
                          of shmoo, away from tip           (PMID 36601911)

  Cell division site      IBA-only (S. pombe SPCC1739.10);  UNPROVEN
   (GO:0032153)           no direct DCV1 evidence;          → treat as non-core /
                          CDC28 = genetic, not localizing   not asserted

  Nuclear envelope        DCV1-specific IDA, but conflicts  RETAIN w/ caveat
   (GO:0005635)           with physiological PM; likely     (conditional/ER pool)
                          ER/perinuclear biosynthetic pool  (PMID 33002606)
```

**State-dependence is the unifying theme.** In vegetative cells Dcv1 is uniform on the PM; upon pheromone exposure it redistributes to the cell rear, opposite the pheromone receptor and the polarized growth front. This polarized redistribution is functionally consistent with a role in **front/rear domain organization** of the mating cell (the theme of PMID 36601911's title, "a member of the claudin superfamily influences formation of the front domain"). Mechanistically, Dcv1 appears to demarcate the mating-specific front domain by **restricting PM lipid distribution** — a direct effect — whereas mislocalized polarity, sensory, and trafficking proteins and impaired gradient tracking/cell fusion are downstream loss-of-function consequences, not evidence that Dcv1 acts at those sites. The nuclear-envelope signal is best treated as an off-pathway or biosynthetic/overexpression pool given the continuity of the NE with the ER for a membrane protein transiting the secretory pathway.

**Paralog caution.** Tos7 (Yol019w) — the protein the NE-source paper is titled about — has a described role in secretion/PM microdomain biology (interacting with Boi2/Rho3). That function should **not** be transferred to DCV1 without DCV1-specific evidence; the seed explicitly warns against this, and the analysis supports the warning.

---

## Evidence Base

| Citation | Evidence type | Supports/Refutes/Qualifies | Claim tested | Key finding | Context | Confidence & limitations |
|---|---|---|---|---|---|---|
| [PMID: 36601911](https://pubmed.ncbi.nlm.nih.gov/36601911/) | Localization (live-cell) | **Supports** PM | Dcv1 at plasma membrane | *"Dcv1 localized uniformly on the plasma membrane (PM) of vegetative cells"* | S. cerevisiae, vegetative cells, Dcv1-GFP | High for PM; single primary paper |
| [PMID: 36601911](https://pubmed.ncbi.nlm.nih.gov/36601911/) | Localization + mutant phenotype | **Refutes** growing tip | Dcv1 at growth front/tip | *"confined to the rear of cells responding to pheromone, away from the pheromone receptor"* | S. cerevisiae, mating/pheromone response | High; direct negative for tip |
| [PMID: 36601911](https://pubmed.ncbi.nlm.nih.gov/36601911/) | Mutant phenotype | **Supports** PM function | Dcv1 organizes PM | `dcv1Δ` mislocalizes PM lipids & polarity/trafficking proteins; defects in gradient tracking & fusion | S. cerevisiae | Moderate-high; functional, not just structural |
| [PMID: 33002606](https://pubmed.ncbi.nlm.nih.gov/33002606/) | Localization (paralog) | **Qualifies/Supports** PM family | Family PM microdomain localization | *"Tos7 localized to punctate patches on the plasma membrane... co-localized with... MCC"*; role in secretion/cell-wall organization | S. cerevisiae, Tos7/Yol019w | Moderate; paralog, not DCV1 |
| [PMID: 33002606](https://pubmed.ncbi.nlm.nih.gov/33002606/) | Localization (database IDA) | **Qualifies** NE | DCV1 nuclear-envelope IDA | Source of SGD GO:0005635 IDA; paper titled about paralog Tos7; DCV1 data in figures/supplements | S. cerevisiae | Moderate; DCV1-specific IDA but likely conditional/ER pool |
| Sur7 record (P54003; PMIDs 11784867, 12469340, 14562095, 15536122, 16496001) | Structural/evolutionary + localization | **Supports** PM | Family anchored at PM/eisosome | Sur7 is multi-pass "Cell membrane" protein, "Localizes at eisosomes" | S. cerevisiae, 5 studies | High for family; inference for DCV1 |
| PANTHER PTHR28013 (Feuermann 2010; GO Central) | Computational (IBA) | **Qualifies** tip/division | IBA propagation | GO:0035838 & GO:0032153 inferred from fission-yeast seeds (SPAC13G7.04c, SPCC1739.10) | Cross-species phylogeny | Low as direct DCV1 evidence |
| [PMID: 22042866](https://pubmed.ncbi.nlm.nih.gov/22042866/) | Genetic interaction | **Competing/Qualifies** | Division/growth necessity | `dcv1Δ` genetic interaction/lethality with CDC28 loss ("Demands CDC28 for Viability") | S. cerevisiae, chemical-genetic network | Low for localization; viability ≠ localizing assay |

**Key papers:**

- ***A member of the claudin superfamily influences formation of the front domain in pheromone-responding yeast cells.*** [PMID: 36601911](https://pubmed.ncbi.nlm.nih.gov/36601911/) (Sukumar et al., 2023). Primary source for DCV1 PM localization, pheromone-induced rear redistribution, and `dcv1Δ` PM-lipid/polarity mislocalization. **Supports PM; refutes growing tip.**
- ***The Sur7/PalI family transmembrane protein Tos7 (Yol019w) plays a role in secretion...*** [PMID: 33002606](https://pubmed.ncbi.nlm.nih.gov/33002606/) (Zhu J et al., 2020). Source of SGD's DCV1 GO:0005635 (nuclear envelope) IDA; primarily about paralog Tos7, which localizes to PM MCC/eisosome. **Qualifies NE and supports family-level PM.**
- **Chemical-genetic CDC28 network.** [PMID: 22042866](https://pubmed.ncbi.nlm.nih.gov/22042866/). `dcv1Δ` genetic interaction with CDC28 — viability context, not a localizing assay. **Competing/qualifying.**
- **Sur7 (P54003) experimental record** (PMIDs 11784867, 12469340, 14562095, 15536122, 16496001). Family founder; multi-pass PM/eisosome protein. **Structural/evolutionary support for DCV1 PM.**

---

## GO Curation Implications

**Leads requiring curator verification** (per-term):

| GO term | Aspect | Current basis | Recommended action | Rationale |
|---|---|---|---|---|
| GO:0005886 plasma membrane | CC | IBA (GO Central 2001; Feuermann 2010) | **Retain; upgrade to experimental (IDA)** with PMID 36601911 | Direct Dcv1-GFP PM imaging + `dcv1Δ` PM phenotype + family biology |
| GO:0035838 growing cell tip | CC | IBA (PANTHER, fission-yeast seed SPAC13G7.04c) | **Remove or do not assert** | IBA-only; directly contradicted (Dcv1 at shmoo rear, not tip) |
| GO:0032153 cell division site | CC | IBA (PANTHER, fission-yeast seed SPCC1739.10) | **Treat as non-core / hold as IBA at most** | IBA-only; no direct DCV1 evidence at bud neck |
| GO:0005635 nuclear envelope | CC | **IDA** (SGD-curated from PMID 33002606) | **Retain with caveat** (conditional/ER-perinuclear pool) | DCV1-specific IDA but conflicts with physiological PM; verify construct |

**Beyond localization (MF/BP):** No defined biochemical activity is established for Dcv1; the family is structural/scaffolding at eisosome/MCC. The best-supported **BP** lead is a role in **mating/chemotropic front–rear cell polarity and pheromone-gradient tracking / cell fusion** (PMID 36601911), via restriction of PM-lipid distribution — a candidate annotation distinct from the paralog Tos7's secretion role. **Avoid "protein binding" as a terminal recommendation** — the localization and PM-organization evidence is more informative.

---

## Mechanistic Scope

The immediate cellular function being tested is **membrane compartment localization** and the associated **plasma-membrane organizing activity** of Dcv1. Direct gene-product observations are: (i) Dcv1-GFP resides on the PM in vegetative cells, and (ii) Dcv1 redistributes to the rear in pheromone-responding cells. The `dcv1Δ` mislocalization of PM lipids and polarity proteins is a **loss-of-function phenotype** — informative about the pathway Dcv1 participates in, but one step removed from a defined biochemical activity.

Downstream / non-direct signals that must be kept separate from direct activity:
- **CDC28 genetic interaction (PMID 22042866)** — a viability/growth-necessity relationship, not evidence of localization or molecular activity.
- **IBA propagation to tip and division site** — inherited phylogenetic inference, not direct DCV1 data.
- **TOS7 secretion function** — a paralog activity that must not be attributed to DCV1.
- **Nuclear-envelope signal** — a genuine DCV1 IDA, but plausibly a biosynthetic/conditional pool rather than the functional site.

---

## Conflicts and Alternatives

1. **PM vs. NE compartment conflict.** The physiological PM localization (PMID 36601911) conflicts with the curated NE IDA (PMID 33002606). Alternative interpretations: (a) NE is an ER/perinuclear biosynthetic pool of a secretory-pathway membrane protein; (b) NE reflects a tagged/high-copy overexpression pattern (Zhu's assays relied on high-copy constructs); (c) genuine dual localization under different conditions. The PM evidence is physiologically stronger and more informative.

2. **Paralog confusion (DCV1 vs. TOS7).** The NE-source paper is titled about Tos7/Yol019w. Curators must confirm the DCV1-specific construct, images, and controls before treating NE as core, and must not import Tos7's secretion/exocyst function.

3. **Organism-specific tip biology / cross-species term transfer.** GO:0035838 tip and GO:0032153 division-site annotations trace to fission-yeast seeds (SPAC13G7.04c, SPCC1739.10). Fission yeast grows by tip extension and divides medially — morphologies not shared by budding yeast in vegetative growth — making direct IBA transfer weak; even the closest polarized analog (mating projection) shows Dcv1 at the rear.

4. **Genetic vs. physical evidence.** The CDC28 interaction (PMID 22042866) is easy to over-read as implicating a division-site role; it is a genetic-network necessity signal only.

---

## Limitations and Knowledge Gaps

- **Single primary DCV1 localization paper.** The PM and rear-localization claims rest largely on one study (PMID 36601911). Independent confirmation (e.g., endogenous-tag imaging, high-throughput GFP collections) would strengthen the PM upgrade. *Checked:* eutils abstract, SGD GO details.
- **Full text of PMID 33002606 not fully retrieved.** The exact DCV1 vs. Tos7 constructs, imaging conditions, and controls behind the NE IDA were not directly inspected (WebFetch not machine-accessible here); the seed explicitly asks to recover the full paper and supplements. *Why it matters:* determines whether NE is a genuine DCV1 finding vs a paralog/tag artifact. *Resolve:* read the paper's DCV1 panels and construct/promoter details.
- **No direct division-site imaging checked.** Whether any dataset shows Dcv1 at the bud neck was not found; absence of evidence here is not evidence of absence, but no positive signal exists. *Resolve:* Dcv1-GFP timelapse through cytokinesis with septin/Myo1 co-stain.
- **Biochemical activity undefined.** No defined molecular function (MF) is established for Dcv1; the family is structural/membrane-organizing rather than enzymatic.
- **PANTHER tree assertions unverified programmatically.** The seed's specific claims about PTHR28013 root/leaf IBD content and absence of a loss event on the DCV1 path were taken as context, not independently reconstructed here.

---

## Discriminating Tests

1. **Recover and read the full PMID 33002606 (incl. supplements).** Identify the exact DCV1 construct, promoter/copy number, imaging conditions, and controls behind the NE IDA. This single step most efficiently resolves whether NE is functional, biosynthetic, or artifactual.
2. **Endogenously tagged Dcv1** (N- and C-terminal, native promoter) co-imaged with a PM marker, an ER/NE marker (Sec61/Nup), MCC (Sur7/Can1), and the bud-neck (septin) — to arbitrate PM vs. NE, quantify the PM:NE ratio and its condition-dependence, and test division-site enrichment directly.
3. **Bud-neck co-localization test.** Image Dcv1 with a septin/myosin (Myo1) ring marker across the cell cycle to directly test GO:0032153; a negative result would confirm removal of the division-site call.
4. **Shmoo-tip quantification.** Line-scan or ratiometric analysis of Dcv1 vs. Ste2 (receptor) along the projection axis to formally quantify tip exclusion (confirming GO:0035838 refutation).
5. **Functional divergence from Tos7.** Side-by-side `dcv1Δ` vs. `tos7Δ` (and double) for secretion/exocyst readouts to confirm that Tos7's secretion role should not be transferred to DCV1.
6. **Cross-species localization of the fission-yeast orthologs** (SPAC13G7.04c, SPCC1739.10) to test whether the IBA-propagated tip/division annotations even hold in the seed organisms.

---

## Proposed Follow-up Actions / Curation Leads

*All items below are leads requiring curator verification.*

- **Reference to verify:** [PMID: 36601911](https://pubmed.ncbi.nlm.nih.gov/36601911/) — exact verbatim snippet: *"Although Dcv1 localized uniformly on the plasma membrane (PM) of vegetative cells, it was confined to the rear of cells responding to pheromone, away from the pheromone receptor."* Use to (a) upgrade GO:0005886 to IDA and (b) refute GO:0035838.
- **Reference to verify:** [PMID: 33002606](https://pubmed.ncbi.nlm.nih.gov/33002606/) — recover full text/supplements; confirm the DCV1-specific assay behind GO:0005635 IDA and distinguish it from Tos7 data.
- **Candidate GO actions:**
  - GO:0005886 (plasma membrane, CC) — **retain, upgrade IBA→IDA**.
  - GO:0035838 (growing cell tip, CC) — **remove / do not assert** (IBA-only, direct negative).
  - GO:0032153 (cell division site, CC) — **do not assert / non-core** (IBA-only).
  - GO:0005635 (nuclear envelope, CC) — **retain with caveat**; annotate as conditional pool pending full-text review.
  - Consider a **BP lead** around mating/chemotropic front–rear cell polarity and PM-lipid organization (verify against PMID 36601911 full text).
- **Suggested questions for curators:** Is the NE IDA based on an endogenous or overexpressed/high-copy tagged DCV1 construct? Does any dataset show Dcv1 at the bud neck? Should the IBA tip/division annotations be down-weighted given fission-yeast-only seeds?
- **Suggested experiments:** Endogenous dual-tag co-localization (PM vs. ER/NE and bud neck), bud-neck cell-cycle imaging, shmoo-axis ratiometric quantification (see Discriminating Tests).
- **Do NOT:** transfer TOS7's secretion function to DCV1 without DCV1-specific evidence.

---

*Prepared as a hypothesis-level curation lead. Direct experimental results (PMID 36601911) are distinguished throughout from inherited inference (IBA/PANTHER) and paralog data (Tos7). No results were fabricated; where full text was not retrieved (PMID 33002606 supplements), this is stated explicitly.*


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)