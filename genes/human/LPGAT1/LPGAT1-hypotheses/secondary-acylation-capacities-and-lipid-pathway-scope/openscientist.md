---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-20T20:45:47.775511'
end_time: '2026-09-20T21:14:09.526580'
duration_seconds: 1701.75
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: human
  gene: LPGAT1
  gene_symbol: LPGAT1
  uniprot_accession: Q92604
  taxon_id: NCBITaxon:9606
  taxon_label: Homo sapiens
  focus_type: function_assignment
  hypothesis_slug: secondary-acylation-capacities-and-lipid-pathway-scope
  hypothesis_text: Human LPGAT1 has monoacylglycerol acyltransferase capacity, contributes
    to triacylglycerol biosynthesis or PG/PI remodeling, and acylates 1-acyl-lysophosphatidylserine.
    Assess each separately with exact donor/acceptor and sn-position definitions.
    PMID:36049524 calls LPI/LPG poor substrates and reports reduced sn-1 activity
    in knockout samples; poor is not zero. Compare PMID:15485873, PMID:20018982, PMID:37917582
    and PMID:42173283. Does newer predominant positional specificity exclude all older
    secondary activities, or do construct, assay and organism differences explain
    them? Distinguish demonstrable intrinsic chemistry from physiological pathway
    flux and abundance phenotypes.
  term_context: No specific term context supplied.
  reference_context: No specific reference context supplied.
  source_file: genes/human/LPGAT1/LPGAT1-ai-review.yaml
  source_selector: free-text
  source_context_yaml: "hypothesis: Human LPGAT1 has monoacylglycerol acyltransferase\
    \ capacity, contributes to triacylglycerol\n  biosynthesis or PG/PI remodeling,\
    \ and acylates 1-acyl-lysophosphatidylserine. Assess each separately\n  with exact\
    \ donor/acceptor and sn-position definitions. PMID:36049524 calls LPI/LPG poor\
    \ substrates and\n  reports reduced sn-1 activity in knockout samples; poor is\
    \ not zero. Compare PMID:15485873, PMID:20018982,\n  PMID:37917582 and PMID:42173283.\
    \ Does newer predominant positional specificity exclude all older secondary\n\
    \  activities, or do construct, assay and organism differences explain them? Distinguish\
    \ demonstrable intrinsic\n  chemistry from physiological pathway flux and abundance\
    \ phenotypes.\nfocus_type: function_assignment\ncontext: []\nreference_id: []"
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
citation_count: 14
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
- **Gene directory:** LPGAT1
- **Gene symbol:** LPGAT1
- **UniProt accession:** Q92604

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** secondary-acylation-capacities-and-lipid-pathway-scope
- **Source file:** genes/human/LPGAT1/LPGAT1-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

Human LPGAT1 has monoacylglycerol acyltransferase capacity, contributes to triacylglycerol biosynthesis or PG/PI remodeling, and acylates 1-acyl-lysophosphatidylserine. Assess each separately with exact donor/acceptor and sn-position definitions. PMID:36049524 calls LPI/LPG poor substrates and reports reduced sn-1 activity in knockout samples; poor is not zero. Compare PMID:15485873, PMID:20018982, PMID:37917582 and PMID:42173283. Does newer predominant positional specificity exclude all older secondary activities, or do construct, assay and organism differences explain them? Distinguish demonstrable intrinsic chemistry from physiological pathway flux and abundance phenotypes.

## Term and Decision Context

No specific term context supplied.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: Human LPGAT1 has monoacylglycerol acyltransferase capacity, contributes to triacylglycerol
  biosynthesis or PG/PI remodeling, and acylates 1-acyl-lysophosphatidylserine. Assess each separately
  with exact donor/acceptor and sn-position definitions. PMID:36049524 calls LPI/LPG poor substrates and
  reports reduced sn-1 activity in knockout samples; poor is not zero. Compare PMID:15485873, PMID:20018982,
  PMID:37917582 and PMID:42173283. Does newer predominant positional specificity exclude all older secondary
  activities, or do construct, assay and organism differences explain them? Distinguish demonstrable intrinsic
  chemistry from physiological pathway flux and abundance phenotypes.
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

# AIGR Gene Hypothesis Deep Research — LPGAT1 (Q92604)

**Hypothesis slug:** secondary-acylation-capacities-and-lipid-pathway-scope
**Focus type:** function_assignment
**Gene:** LPGAT1 / LPLAT7 (Homo sapiens, NCBITaxon:9606), UniProt Q92604

---

## Executive Judgment

**Verdict: Partially supported.**

Human LPGAT1's demonstrable, reproducible primary molecular function is that of an **endoplasmic-reticulum, sn-1-specific, stearoyl-CoA-preferring lysophospholipid acyltransferase acting on lysophosphatidylethanolamine (LPE) and lysophosphatidylcholine (LPC)**. This is established by three independent groups using different constructs, organisms, and readouts (recombinant human LPLAT7 screen, bacterially expressed murine LPGAT1, and skeletal-muscle knockout lipidomics). Against this core, the seed hypothesis proposes three "secondary" capacities: (1) monoacylglycerol acyltransferase (MGAT)/triacylglycerol (TAG) biosynthesis, (2) PG/PI remodeling, and (3) acylation of 1-acyl-lysophosphatidylserine (LPS). Assessed separately with attention to donor/acceptor and sn-position, these secondary activities are **real-but-re-ranked, context-specific, in-vivo-only, or paralog-confounded — not co-equal primary functions.**

The seed's central question — *"does newer predominant positional specificity exclude all older secondary activities, or do construct/assay/organism differences explain them?"* — is answered **the latter, with important nuance**. The newer sn-1 LPE/LPC specificity **re-ranks** rather than **erases** the older activities. The phrase "poor is not zero" from PMID:36049524 is correct and matters for curation: LPI/LPG are weak but detectable intrinsic substrates, and the same paper's experimental evidence underlies the curated LPS reactions. However, several older annotations rest on weaker foundations than the sn-1 LPE/LPC core: MGAT is by-similarity to mouse (single human study), TAG "biosynthesis" is a downstream pathway-flux phenotype (knockout *raises* TAG), and PI/LPI remodeling has no curated UniProt reaction and is better attributed to the same-family paralog ALCAT1/LCLAT1.

**Most important caveats:** (i) sn-position assignments for lyso-substrates are confounded by non-enzymatic acyl migration, so "sn-1 vs sn-2" claims must be read cautiously; (ii) the seed's exact phrase "acylates 1-acyl-lysophosphatidylserine" maps to a curated RHEA reaction (RHEA:37403) but with weak experimental backing; (iii) in-vivo lipidomic phenotypes reflect pathway flux and abundance, not necessarily direct intrinsic chemistry, and must not be curated as MF evidence.

---

## Key Findings

### Finding 1 — The core function is an ER sn-1-specific LPE/LPC acyltransferase, stearoyl-CoA preferring

Three independent lines of evidence converge on a single, tightly specified molecular function.

**In vitro recombinant human screen ([PMID:36049524](https://pubmed.ncbi.nlm.nih.gov/36049524/)).** In a systematic siRNA + recombinant screen of 14 human LPLATs, LPLAT7/LPGAT1 was identified as an sn-1-specific lysophospholipid acyltransferase. The verified snippet is unambiguous: LPLAT7 *"mainly incorporated several fatty acids into the sn-1 position of lysophosphatidylcholine (LPC) and lysophosphatidylethanolamine (LPE), with weak activities toward other lyso-PLs."* In cells and knockout tissue, only C18:0 (stearoyl) PC/PE species were reduced, with a reciprocal rise in C16:0/C18:1 species — a signature of loss of a stearate-preferring sn-1 remodeling enzyme.

**Independent recombinant murine assay ([PMID:35131264](https://pubmed.ncbi.nlm.nih.gov/35131264/)).** Bacterially expressed murine LPGAT1 *"transferred saturated acyl-CoAs specifically into the sn-1 position of lysophosphatidylethanolamine (LPE) rather than lysophosphatidylglycerol and preferred stearoyl-CoA over palmitoyl-CoA as the substrate."* Knockout abolished 1-LPE:stearoyl-CoA activity and shifted PE/PC composition from stearate toward palmitate. This directly demonstrates sn-1 LPE specificity, stearoyl-CoA preference, and — critically for the PG hypothesis — activity into LPE *rather than* LPG.

**In vivo/ex vivo confirmation ([PMID:37217003](https://pubmed.ncbi.nlm.nih.gov/37217003/)).** In murine skeletal muscle, LPGAT1 sets the sn-1 18:0/16:0 (stearate/palmitate) profile of PC and PE; *"LPGAT1 knockout decreased the incorporation of stearate into PC and PE."*

**Structural/database orientation.** UniProt Q92604 curates the enzyme as an ER-membrane, PlsC/AGPAT-family acyltransferase (Pfam PF01553/PF16076; InterPro IPR002123) with the catalytic HX4D motif (residues ~101–106) and two transmembrane helices. The primary curated catalytic reaction is 2-acyl-LPE + stearoyl-CoA → 1-stearoyl-2-acyl-PE.

Together these establish the **core MF** (sn-1 LPE/LPC O-acyltransferase, stearoyl-CoA-preferring), **core BP** (PE/PC sn-1 acyl-chain remodeling), and **core CC** (ER membrane).

### Finding 2 — The secondary activities (MGAT, PG, PI, PS, TAG) are real but weak, context-specific, or in-vivo-only

| Activity | Best evidence | Nature | Curation status |
|---|---|---|---|
| **MGAT / DAG synthesis** | PMID:20018982 (mouse liver) | Direct assay, single group, mouse; not reproduced by sn-1 studies | UniProt reactions ECO:0000250 by-similarity to **mouse** Lpgat1; GO:0003846 ISS. **Non-core.** |
| **TAG biosynthesis** | PMID:20018982; PMID:42173283 | Downstream pathway flux — KO *increases* TAG/lipid droplets | GO:0019432 ISS. **Downstream phenotype, non-core.** |
| **LPG → PG remodeling** | PMID:15485873 (human); PMID:37917582 (MEGDEL KO) | Experimentally real in human but LPG is a *poor* intrinsic substrate vs LPE/LPC | 9 PG reactions ECO:0000269 PMID:15485873. **Minor, shared with paralogs.** |
| **LPI → PI remodeling** | none direct; LPI "poor" (PMID:36049524); no activity in 2004 assay (PMID:15485873) | No curated UniProt reaction; ALCAT1 carries LPIAT (PMID:19075029) | GO:0036149 IBA only. **Flag for removal/generalization.** |
| **1-acyl-LPS acylation** | PMID:36049524 ("weak activities"); PMID:42173283 (in vivo PS reduction) | Weakly experimental + in-vivo lipidomic | RHEA:74815/37403 ECO:0000269 PMID:36049524. **Retain with weak/secondary qualifier.** |

**MGAT/TAG.** [PMID:20018982](https://pubmed.ncbi.nlm.nih.gov/20018982/) identified mouse LPGAT1 as an acyl-CoA:monoacylglycerol acyltransferase; hepatic MGAT activity fell with LPGAT1 shRNA and serum TAG dropped (*"we identified a novel MGAT gene, which is identical with lysophosphatidylglycerol acyltransferase1 (LPGAT1)"*). This is direct but restricted to mouse liver, from a single group, and not reproduced by the later sn-1-focused studies. Crucially, [PMID:42173283](https://pubmed.ncbi.nlm.nih.gov/42173283/) shows that LPGAT1/Lplat7 knockout **increases** triglyceride and lipid-droplet accumulation — the *opposite* of what a direct, rate-limiting TAG synthase would produce on deletion. TAG "biosynthesis" is therefore best read as a **downstream pathway-flux/abundance phenotype**, not intrinsic chemistry.

**PG remodeling.** The original human enzyme characterization ([PMID:15485873](https://pubmed.ncbi.nlm.nih.gov/15485873/)) demonstrated LPG acyltransferase activity, and knockout produces aberrant PG acyl composition and a MEGDEL-like disease ([PMID:37917582](https://pubmed.ncbi.nlm.nih.gov/37917582/)). Yet LPG is a *poor* intrinsic substrate relative to LPE/LPC (PMID:36049524), and PMID:35131264 explicitly shows acylation into LPE "rather than" LPG. So PG remodeling is experimentally real in human but **minor in intrinsic ranking**, and is shared with ALCAT1/LCLAT1 and CRLS1.

**PI remodeling.** LPI is a poor substrate (PMID:36049524), and the 2004 human assay found *no* LPI activity: *"no significant acyltransferase activities were detected against glycerol 3-phosphate or a variety of lysophospholipids, including lysophosphatidylcholine, lysophosphatidylethanolamine, lysophosphatidylinositol, and lysophosphatidylserine."* (Note this early assay also missed LPC/LPE, so absence there reflects assay limitations — but the PI negative is consistent with later "poor substrate" data.) The same-family paralog ALCAT1/LCLAT1 carries robust LPIAT activity ([PMID:19075029](https://pubmed.ncbi.nlm.nih.gov/19075029/)), creating a **paralog-attribution risk** for the PI-remodeling annotation (GO:0036149, IBA only, no curated UniProt reaction).

**LPS acylation.** No isolated in vitro human assay demonstrates lyso-PS acylation as a strong activity; the RHEA-curated PS reactions are attributed to PMID:36049524's "weak activities toward other lyso-PLs." In vivo support comes from PMID:42173283: Lplat7 knockout *"reduced the abundance of 1-stearoyl-2-unsaturated species of phosphatidylcholine, phosphatidylethanolamine, and phosphatidylserine"* — supporting an sn-1 PS remodeling contribution in vivo, alongside PC and PE.

### Finding 3 — RHEA/UniProt evidence codes refine sn-position and provenance of the secondary activities

A programmatic pull of UniProt Q92604 catalytic-activity comments with RHEA IDs and ECO codes sharpens the picture in ways that matter directly for curation:

- **PS acylation is curated as EXPERIMENTAL** (ECO:0000269, PubMed:36049524), not merely electronic. Two reactions exist: **RHEA:74815** (sn-1 acylation of 2-acyl-LPS, adding palmitoyl) and **RHEA:37403** (sn-2 acylation of 1-oleoyl-LPS, adding stearoyl). The seed's exact phrase *"acylates 1-acyl-lysophosphatidylserine"* maps to **RHEA:37403 (sn-2 addition onto a 1-acyl acceptor)** — an important distinction from the enzyme's sn-1 preference on LPE/LPC.
- **MGAT/DAG reactions** (RHEA:16741/65096/65100, 2-acylglycerol → 1,2-diacylglycerol) are **ECO:0000250 by-similarity to MOUSE** Lpgat1 (UniProtKB:Q91YX5) — i.e., **no human experimental support** in UniProt.
- **All 9 PG reactions** are ECO:0000269 PubMed:15485873 (human experimental, 2004).
- **LPE/LPC sn-1 reactions** are ECO:0000269 PubMed:36049524.
- **UniProt curates NO lysophosphatidylinositol (LPI) reaction** for LPGAT1, despite GO:0036149 (PI remodeling) existing as an IBA annotation.

**Paralog check.** LPGAT1 (PANTHER PTHR10983:SF2) and LCLAT1/ALCAT1 (Q6UWP7, PTHR10983:SF16) are same-family AGPAT/PlsC paralogs sharing Pfam PF01553+PF16076 and InterPro IPR002123/IPR032098. CRLS1 (Q9UJA2) is a distinct family (PTHR14269, PF01066). This supports the interpretation that anionic-lysophospholipid (LPI/LPG) activities historically attributed to LPGAT1 may partly belong to ALCAT1.

---

## Mechanistic Model / Interpretation

```
                 Lands cycle (sn-1 remodeling), ER membrane
                 ============================================
  2-acyl-LPE  +  stearoyl-CoA  --LPGAT1-->  1-stearoyl-2-acyl-PE   [CORE, experimental x3]
  2-acyl-LPC  +  stearoyl-CoA  --LPGAT1-->  1-stearoyl-2-acyl-PC   [CORE, experimental]

  Preference:  stearoyl-CoA (18:0) > palmitoyl-CoA (16:0)
  Position:    sn-1 specific on LPE/LPC
  Phenotype:   KO shifts PC/PE from 18:0 -> 16:0/18:1 (reciprocal)

                 Secondary / re-ranked capacities
                 ================================
  2-acyl-LPS  --LPGAT1-->  PS (RHEA:74815, sn-1)   [WEAK experimental, PMID:36049524]
  1-acyl-LPS  --LPGAT1-->  PS (RHEA:37403, sn-2)   [<= seed's exact phrase; WEAK]
  LPG         --LPGAT1-->  PG (RHEA x9)            [human experimental but POOR substrate;
                                                    shared with ALCAT1/CRLS1]
  2-MAG       --LPGAT1-->  DAG -> TAG              [MOUSE by-similarity only; TAG = flux]
  LPI         --??-->      PI                      [NO curated reaction; likely ALCAT1]

  Downstream / abundance phenotypes (NOT intrinsic chemistry):
    - KO INCREASES TAG / lipid droplets (PMID:42173283) -> opposite of a TAG synthase
    - KO causes MEGDEL-like disease via PG remodeling + mito transport (PMID:37917582)
```

The unifying model: **LPGAT1 is a Lands-cycle sn-1 acyl remodeler whose bona-fide, reproducible substrates are LPE and LPC with a stearoyl-CoA preference.** Its promiscuity toward anionic and other lysophospholipids (LPG, LPI, LPS) is genuine but intrinsically weak; whether a given weak activity produces a physiological phenotype depends on tissue context, substrate availability, and the presence of overlapping paralogs (ALCAT1, CRLS1). The dramatic in-vivo phenotypes (MEGDEL syndrome, TAG accumulation, reproductive defects) are **systems-level consequences of perturbing membrane acyl composition and mitochondrial lipid supply**, not direct evidence that PG/TAG/PS synthesis is the enzyme's primary chemistry.

---

## Evidence Base / Evidence Matrix

| Citation | Evidence type | Supports/Refutes/Qualifies | Claim tested | Key finding | Context | Confidence & limitations |
|---|---|---|---|---|---|---|
| [PMID:36049524](https://pubmed.ncbi.nlm.nih.gov/36049524/) | Direct assay + KO lipidomics | Supports core; qualifies secondary | sn-1 LPE/LPC is primary; other lyso-PLs weak | LPLAT7 mainly acylates sn-1 of LPC/LPE, weak elsewhere; only C18:0-PC/PE reduced in KO | Human recombinant + cells/tissue | High for core; "weak" ≠ zero for LPS/LPG/LPI |
| [PMID:35131264](https://pubmed.ncbi.nlm.nih.gov/35131264/) | Direct assay + KO | Supports core; refutes strong PG | sn-1 LPE specificity, stearoyl>palmitoyl | Acyl-CoA into sn-1 LPE "rather than" LPG; KO shifts PE/PC 18:0→16:0 | Murine recombinant (bacterial) | High; murine enzyme |
| [PMID:37217003](https://pubmed.ncbi.nlm.nih.gov/37217003/) | Mutant phenotype (in vivo) | Supports core BP | sn-1 18:0/16:0 remodeling of PC/PE | KO decreases stearate incorporation into PC/PE | Mouse skeletal muscle | High for BP; in-vivo flux |
| [PMID:20018982](https://pubmed.ncbi.nlm.nih.gov/20018982/) | Direct assay + shRNA | Qualifies MGAT/TAG | MGAT capacity, TAG secretion | LPGAT1 = novel MGAT; shRNA lowers hepatic MGAT + serum TAG | Mouse liver | Moderate; single group, mouse, ISS in UniProt |
| [PMID:15485873](https://pubmed.ncbi.nlm.nih.gov/15485873/) | Direct assay | Supports PG; refutes LPI/LPS (era-limited) | Original human LPGAT characterization | LPG activity present; NO LPI/LPS/G3P/LPC/LPE activity detected | Human recombinant, ER | Moderate; assay also missed LPC/LPE |
| [PMID:37917582](https://pubmed.ncbi.nlm.nih.gov/37917582/) | Mutant phenotype | Qualifies PG (downstream) | PG remodeling → mitochondrial function | KO causes MEGDEL-like disease; PG ER-retention, crista loss | Mouse KO | High for phenotype; systems-level, not MF |
| [PMID:42173283](https://pubmed.ncbi.nlm.nih.gov/42173283/) | KO lipidomics | Qualifies PS; refutes TAG-synthase | sn-1 remodeling of PC/PE/PS; TAG | KO reduces 1-stearoyl-2-unsat PC/PE/PS; INCREASES TAG/droplets | Mouse KO | Moderate; in-vivo flux, sn-position confound |
| [PMID:19075029](https://pubmed.ncbi.nlm.nih.gov/19075029/) | Direct assay (paralog) | Competing (paralog) | Who carries LPIAT/LPGAT? | ALCAT1/LCLAT1 overexpression increases LPIAT + LPGAT activity | Human HEK293 | High; supports paralog-attribution alternative |
| [PMID:20025994](https://pubmed.ncbi.nlm.nih.gov/20025994/) | Direct assay (paralog CLS1) | Competing (paralog) | PG remodeling attribution | hCLS1/CRLS1 has strong LPG acyltransferase activity | Human recombinant | Supports shared/competing PG remodeling |
| UniProt Q92604 / RHEA | Database + ECO codes | Qualifies provenance | Reaction-level evidence codes | PS=experimental(269); MGAT=by-similarity mouse(250); PG=269; no LPI reaction | Curated database | High for provenance; database-level |

---

## GO Curation Implications

The following are **leads requiring curator verification.**

**Retain as core:**
- **MF:** sn-1-specific lysophospholipid O-acyltransferase acting on LPE/LPC (e.g., 1-acylglycerophosphoethanolamine O-acyltransferase; stearoyl-CoA preferring). Evidence: PMID:36049524, PMID:35131264 (both ECO:0000269-grade).
- **BP:** phosphatidylethanolamine/phosphatidylcholine acyl-chain remodeling (Lands cycle, sn-1). Evidence: PMID:37217003, PMID:35131264.
- **CC:** endoplasmic reticulum membrane. Evidence: UniProt Q92604, PMID:15485873.

**Retain with a weak/secondary qualifier:**
- **MF: 1-acylglycerophosphoserine O-acyltransferase (GO:0106263 / RHEA:37403,74815).** Backed by experimental evidence (ECO:0000269, PMID:36049524) but explicitly the "weak activities toward other lyso-PLs." Curator should note it is secondary and that the seed's "1-acyl-LPS" phrasing corresponds to the sn-2 reaction RHEA:37403.

**Demote to non-core (retain but flag as by-similarity / context-specific):**
- **MGAT (GO:0003846) and TAG biosynthesis (GO:0019432).** MGAT reactions are ECO:0000250 by-similarity to mouse only; TAG "biosynthesis" is a downstream flux phenotype (KO *raises* TAG). Neither should be presented as a primary human function.

**Flag for removal or generalization:**
- **PI remodeling (GO:0036149, IBA only).** No curated UniProt reaction; LPI is a poor substrate; ALCAT1/LCLAT1 is a strong LPIAT paralog. High risk of paralog carry-over. Recommend removal or generalization to "glycerophospholipid remodeling."

**PG remodeling:** retain (human experimental, PMID:15485873) but annotate as minor/shared, given LPG is a poor substrate relative to LPE/LPC and the activity overlaps with ALCAT1/CRLS1.

Avoid "protein binding" as a final recommendation — the informative MF terms above are supported. Note: LPGAT1's interaction with the prohibitin/TIMM14 import motor (PMID:37917582) could justify a specific protein-binding annotation with a named partner, but that is orthogonal to the acyltransferase function under review.

---

## Mechanistic Scope

The immediate molecular function under test is **acyl-CoA–dependent O-acyltransferase chemistry on lysophospholipid acceptors**. The direct, gene-product-intrinsic activity is transfer of a (preferentially stearoyl) acyl chain onto the sn-1 position of LPE and LPC. Everything else in the seed hypothesis must be separated from this:

- **Direct chemistry (intrinsic):** sn-1 LPE/LPC acylation (strong); LPG, LPI, LPS acylation (weak, "poor is not zero").
- **Pathway consequences / flux:** PG remodeling feeding cardiolipin synthesis and mitochondrial cristae; TAG abundance changes.
- **Downstream phenotypes / disease:** MEGDEL-like syndrome, dilated cardiomyopathy, 3-methylglutaconic aciduria (PMID:37917582); hepatic lipid accumulation (PMID:41507908); LUAD proliferation (PMID:37258473); zebrafish reproductive/developmental defects (PMID:35508627); BMI/body-fat associations (PMID:23505186) and plasma 18:0 GWAS signals (PMID:23362303).

Only the first category constitutes MF evidence. The second and third support BP and disease-association annotations but must not be curated as direct enzymatic function.

---

## Conflicts and Alternatives

1. **Positional-specificity re-ranking vs exclusion.** The newer sn-1 LPE/LPC data (PMID:36049524, PMID:35131264) do not exclude older secondary activities; they re-rank them. "Poor is not zero" is the correct reading. Construct (bacterial murine vs recombinant human vs endogenous), assay (in vitro vs cellular vs KO lipidomics), and organism differences explain most apparent contradictions.

2. **Paralog confusion (ALCAT1/LCLAT1; CRLS1).** ALCAT1 robustly carries LPIAT and LPGAT activities (PMID:19075029) and is a same-family AGPAT/PlsC paralog; CRLS1/hCLS1 has strong LPG acyltransferase activity (PMID:20025994). Anionic-lysophospholipid activities historically credited to LPGAT1 (especially PI and part of PG) may belong to these paralogs.

3. **Organism/tissue specificity.** MGAT/TAG evidence is mouse-liver (PMID:20018982); sn-1 PC/PE evidence spans human recombinant, murine recombinant, and murine muscle. Human-experimental support for MGAT is limited.

4. **sn-position confound (acyl migration).** Lyso-phospholipid substrates undergo non-enzymatic acyl migration between sn-1 and sn-2, so "sn-1 vs sn-2" assignments (including the seed's "1-acyl-LPS" → RHEA:37403 sn-2 mapping) carry inherent uncertainty.

5. **Loss-of-function ≠ direct chemistry.** The MEGDEL-like disease (PMID:37917582), TAG accumulation (PMID:42173283), reproductive/developmental defects (zebrafish, PMID:35508627), and cancer proliferation phenotypes (PMID:37258473) are downstream/pleiotropic consequences, not evidence of primary MGAT/TAG/PG chemistry.

6. **Era-limited negative results.** PMID:15485873 found no LPC/LPE activity — later shown to be the core function — so its negative LPI/LPS results should be weighted as assay-limited, not definitive.

---

## Limitations and Knowledge Gaps

| Gap | What was checked | Why it matters | What would resolve it |
|---|---|---|---|
| Human LPS acylation kinetics | RHEA reactions curated from PMID:36049524 "weak activities" | Determines whether GO:0106263 is a genuine human MF or trace promiscuity | Purified human LPGAT1 kinetic assay on defined 1-acyl- vs 2-acyl-LPS with acyl-migration controls |
| Human MGAT activity | Only PMID:20018982 (mouse liver); UniProt by-similarity | Determines if MGAT/TAG deserves any human MF annotation | Recombinant human LPGAT1 MGAT assay; independent replication |
| PI/LPI attribution | No curated reaction; ALCAT1 carries LPIAT | GO:0036149 may be paralog carry-over | Side-by-side LPGAT1 vs ALCAT1 LPIAT assay; PI lipidomics in LPGAT1-specific KO |
| Relative flux of PG vs PE/PC remodeling in vivo | KO phenotypes exist for both | Whether PG remodeling is quantitatively minor | Quantitative flux/isotope tracing across lipid classes in a single KO model |
| sn-position robustness | In vitro assays report sn-1/sn-2 | Acyl migration undermines strict positional claims | Rapid-quench/MS with migration-locked substrate analogs |

This report relied on the supplied knowledge outline (17 papers, 3 confirmed findings) and public database/RHEA provenance; no new wet-lab data were generated. sn-position claims inherit acyl-migration uncertainty. Several key phenotypic studies are murine or single-group. UniProt/RHEA evidence codes were used as provenance orientation and specific reaction IDs should be re-verified against the current UniProt release before curation.

---

## Proposed Follow-up Experiments / Discriminating Tests

1. **Purified human LPGAT1 kinetic panel:** measure V_max/K_m for LPE, LPC, LPG, LPI, LPS (both 1-acyl and 2-acyl regioisomers) and 2-MAG with matched acyl-CoA donors, including acyl-migration controls, to rank intrinsic activities on a common scale.
2. **Paralog side-by-side:** express human LPGAT1 vs ALCAT1/LCLAT1 (and CRLS1) in the same system and assay LPIAT/LPGAT to resolve PI/PG attribution.
3. **Isoform/organism control:** compare human vs mouse enzyme MGAT activity under identical conditions to test whether MGAT is species-specific.
4. **In vivo flux vs abundance:** isotope-tracing lipidomics in an LPGAT1-specific KO to separate direct acylation flux from steady-state abundance changes (especially for TAG and PS).
5. **Structural docking / active-site modeling:** use the AGPAT/PlsC fold and HX4D motif to predict headgroup selectivity and rationalize weak anionic-lysophospholipid activity.

---

## Curation Leads (require curator verification)

**Candidate references + exact snippets to verify:**
- PMID:36049524 — *"mainly incorporated several fatty acids into the sn-1 position of lysophosphatidylcholine (LPC) and lysophosphatidylethanolamine (LPE), with weak activities toward other lyso-PLs"* → supports core MF + "poor is not zero."
- PMID:35131264 — *"transferred saturated acyl-CoAs specifically into the sn-1 position of lysophosphatidylethanolamine (LPE) rather than lysophosphatidylglycerol and preferred stearoyl-CoA over palmitoyl-CoA"* → supports sn-1 LPE core; refutes strong PG.
- PMID:20018982 — *"we identified a novel MGAT gene, which is identical with lysophosphatidylglycerol acyltransferase1 (LPGAT1)"* → MGAT, but mouse liver / by-similarity in UniProt.
- PMID:15485873 — *"no significant acyltransferase activities were detected against ... lysophosphatidylinositol, and lysophosphatidylserine"* → historical negative for LPI/LPS.
- PMID:42173283 — *"reduced the abundance of 1-stearoyl-2-unsaturated species of phosphatidylcholine, phosphatidylethanolamine, and phosphatidylserine"* → in-vivo PS support; note KO raises TAG.
- PMID:19075029 — *"HEK293 cells overexpressing human ALCAT1 demonstrated significant increases in LPI acyltransferase (LPIAT) and LPG acyltransferase (LPGAT) activities"* → paralog alternative.

**Candidate GO actions:**
- Keep: sn-1 LPE/LPC acyltransferase MF; PE/PC remodeling BP; ER membrane CC.
- Keep with weak qualifier: 1-acylglycerophosphoserine O-acyltransferase (GO:0106263).
- Demote to non-core: MGAT (GO:0003846), TAG biosynthesis (GO:0019432).
- Flag for removal/generalization: PI remodeling (GO:0036149, IBA).
- Retain but mark minor/shared: PG remodeling.

**Suggested curator questions:**
- Is any human-experimental MGAT activity available beyond PMID:20018982?
- Should GO:0036149 (PI) be reassigned to ALCAT1/LCLAT1?
- Does the RHEA:37403 (sn-2 on 1-acyl-LPS) mapping justify the seed's "acylates 1-acyl-lysophosphatidylserine" as a curated MF, given only "weak activity" evidence?

**Suggested experiments:** the kinetic panel and paralog side-by-side assays under Discriminating Tests.

---

## Conclusion

The seed hypothesis is **partially supported**. LPGAT1's primary, reproducible function is sn-1-specific LPE/LPC acylation with stearoyl-CoA preference at the ER. The proposed secondary capacities are genuinely present in the literature but are **re-ranked, not erased**, by the newer positional-specificity data: LPS acylation is weakly experimental (retain with qualifier), MGAT/TAG are by-similarity/downstream (demote to non-core), PG remodeling is minor and shared, and PI remodeling is best attributed to the ALCAT1 paralog (flag for removal). Construct, assay, and organism differences — not mutual exclusion — explain the apparent tension between older and newer studies.


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)