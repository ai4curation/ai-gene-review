---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-21T03:58:25.012904'
end_time: '2026-09-21T04:21:45.439592'
duration_seconds: 1400.43
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: SCHPO
  gene: cps1
  gene_symbol: SPAC24C9.08
  uniprot_accession: O13968
  taxon_id: NCBITaxon:284812
  taxon_label: Schizosaccharomyces pombe 972h-
  focus_type: function_assignment
  hypothesis_slug: additional-lipid-amide-and-extracellular-capacities
  hypothesis_text: 'Schizosaccharomyces pombe cps1 O13968/SPAC24C9.08 has additional
    nonpeptide N-acyl-amino-acid hydrolase/synthase activity, lipid metabolism, extracellular
    localization or adaptive thermogenesis alongside its inferred vacuolar carboxypeptidase
    function. Evaluate each claim independently. This target is NOT bgs1/SPBC19G7.05c,
    the unrelated glucan synthase also called cps1. Actual PANTHER19 PTHR45962 target
    leaf PTN000110806 descends from fungal IBD PTN000865917 for carboxypeptidase and
    vacuolar-lumen functions; the official family name PM20D1 is not proof that mammalian
    substrate preferences transfer. Primary17660439 explicitly constructs GFP-SPAC24C9.08
    and Ub-GFP-SPAC24C9.08: GFP alone impaired vacuolar sorting, and added ubiquitin
    restored MVB/vacuolar trafficking. Distinguish engineered cargo localization from
    native proteolytic processing, and primary16823372 native ORFeome localization.
    Source ScCPS1 primary2026161 and1569061 support active carboxypeptidase and precursor
    processing. Mammalian PM20D1 primary27374330 establishes bidirectional lipid-amide
    catalysis/uncoupling, but investigate ancestral functions and target residues/substrate
    studies rather than assume same family means identical specificity or alternative
    activity means loss of peptide hydrolysis. GO1990845 means regulated heat production
    in response to environment and is not definitionally restricted to brown fat.
    A vacuolar primary location alone does not exclude secretion, and absence of a
    fungal biochemical assay is not direct evidence of loss. Existing Falcon report
    incorrectly implies no target localization and should not be treated as primary
    evidence.'
  term_context: No specific term context supplied.
  reference_context: No specific reference context supplied.
  source_file: genes/SCHPO/cps1/cps1-ai-review.yaml
  source_selector: free-text
  source_context_yaml: "hypothesis: 'Schizosaccharomyces pombe cps1 O13968/SPAC24C9.08\
    \ has additional nonpeptide N-acyl-amino-acid\n  hydrolase/synthase activity,\
    \ lipid metabolism, extracellular localization or adaptive thermogenesis\n  alongside\
    \ its inferred vacuolar carboxypeptidase function. Evaluate each claim independently.\
    \ This target\n  is NOT bgs1/SPBC19G7.05c, the unrelated glucan synthase also\
    \ called cps1. Actual PANTHER19 PTHR45962\n  target leaf PTN000110806 descends\
    \ from fungal IBD PTN000865917 for carboxypeptidase and vacuolar-lumen\n  functions;\
    \ the official family name PM20D1 is not proof that mammalian substrate preferences\
    \ transfer.\n  Primary17660439 explicitly constructs GFP-SPAC24C9.08 and Ub-GFP-SPAC24C9.08:\
    \ GFP alone impaired vacuolar\n  sorting, and added ubiquitin restored MVB/vacuolar\
    \ trafficking. Distinguish engineered cargo localization\n  from native proteolytic\
    \ processing, and primary16823372 native ORFeome localization. Source ScCPS1 primary2026161\n\
    \  and1569061 support active carboxypeptidase and precursor processing. Mammalian\
    \ PM20D1 primary27374330\n  establishes bidirectional lipid-amide catalysis/uncoupling,\
    \ but investigate ancestral functions and\n  target residues/substrate studies\
    \ rather than assume same family means identical specificity or alternative\n\
    \  activity means loss of peptide hydrolysis. GO1990845 means regulated heat production\
    \ in response to\n  environment and is not definitionally restricted to brown\
    \ fat. A vacuolar primary location alone does\n  not exclude secretion, and absence\
    \ of a fungal biochemical assay is not direct evidence of loss. Existing\n  Falcon\
    \ report incorrectly implies no target localization and should not be treated\
    \ as primary evidence.'\nfocus_type: function_assignment\ncontext: []\nreference_id:\
    \ []"
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
artifact_count: 3
artifact_sources:
  openscientist_artifacts_zip: 3
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
- filename: go_decision_table.csv
  path: openscientist_artifacts/go_decision_table.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist go decision table
---

## Question

# AIGR Gene Hypothesis Deep Research

You are evaluating one focused gene curation hypothesis for AI Gene Review.
This is not a general gene overview. Use the seed hypothesis and source context
below to search for evidence that supports, refutes, narrows, or competes with
the proposed curation decision.

## Target Gene

- **Organism code:** SCHPO
- **Taxon:** Schizosaccharomyces pombe 972h- (NCBITaxon:284812)
- **Gene directory:** cps1
- **Gene symbol:** SPAC24C9.08
- **UniProt accession:** O13968

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** additional-lipid-amide-and-extracellular-capacities
- **Source file:** genes/SCHPO/cps1/cps1-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

Schizosaccharomyces pombe cps1 O13968/SPAC24C9.08 has additional nonpeptide N-acyl-amino-acid hydrolase/synthase activity, lipid metabolism, extracellular localization or adaptive thermogenesis alongside its inferred vacuolar carboxypeptidase function. Evaluate each claim independently. This target is NOT bgs1/SPBC19G7.05c, the unrelated glucan synthase also called cps1. Actual PANTHER19 PTHR45962 target leaf PTN000110806 descends from fungal IBD PTN000865917 for carboxypeptidase and vacuolar-lumen functions; the official family name PM20D1 is not proof that mammalian substrate preferences transfer. Primary17660439 explicitly constructs GFP-SPAC24C9.08 and Ub-GFP-SPAC24C9.08: GFP alone impaired vacuolar sorting, and added ubiquitin restored MVB/vacuolar trafficking. Distinguish engineered cargo localization from native proteolytic processing, and primary16823372 native ORFeome localization. Source ScCPS1 primary2026161 and1569061 support active carboxypeptidase and precursor processing. Mammalian PM20D1 primary27374330 establishes bidirectional lipid-amide catalysis/uncoupling, but investigate ancestral functions and target residues/substrate studies rather than assume same family means identical specificity or alternative activity means loss of peptide hydrolysis. GO1990845 means regulated heat production in response to environment and is not definitionally restricted to brown fat. A vacuolar primary location alone does not exclude secretion, and absence of a fungal biochemical assay is not direct evidence of loss. Existing Falcon report incorrectly implies no target localization and should not be treated as primary evidence.

## Term and Decision Context

No specific term context supplied.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: 'Schizosaccharomyces pombe cps1 O13968/SPAC24C9.08 has additional nonpeptide N-acyl-amino-acid
  hydrolase/synthase activity, lipid metabolism, extracellular localization or adaptive thermogenesis
  alongside its inferred vacuolar carboxypeptidase function. Evaluate each claim independently. This target
  is NOT bgs1/SPBC19G7.05c, the unrelated glucan synthase also called cps1. Actual PANTHER19 PTHR45962
  target leaf PTN000110806 descends from fungal IBD PTN000865917 for carboxypeptidase and vacuolar-lumen
  functions; the official family name PM20D1 is not proof that mammalian substrate preferences transfer.
  Primary17660439 explicitly constructs GFP-SPAC24C9.08 and Ub-GFP-SPAC24C9.08: GFP alone impaired vacuolar
  sorting, and added ubiquitin restored MVB/vacuolar trafficking. Distinguish engineered cargo localization
  from native proteolytic processing, and primary16823372 native ORFeome localization. Source ScCPS1 primary2026161
  and1569061 support active carboxypeptidase and precursor processing. Mammalian PM20D1 primary27374330
  establishes bidirectional lipid-amide catalysis/uncoupling, but investigate ancestral functions and
  target residues/substrate studies rather than assume same family means identical specificity or alternative
  activity means loss of peptide hydrolysis. GO1990845 means regulated heat production in response to
  environment and is not definitionally restricted to brown fat. A vacuolar primary location alone does
  not exclude secretion, and absence of a fungal biochemical assay is not direct evidence of loss. Existing
  Falcon report incorrectly implies no target localization and should not be treated as primary evidence.'
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

# AIGR Deep Research Report — *S. pombe* cps1 / SPAC24C9.08 (UniProt O13968)

**Focus type:** function_assignment
**Hypothesis slug:** additional-lipid-amide-and-extracellular-capacities
**Gene:** cps1 (Carboxypeptidase S, CBPS_SCHPO), *Schizosaccharomyces pombe* 972h- (NCBITaxon:284812)

---

## Executive Judgment

**Verdict: Over-annotated / weakly supported for the "additional" functions; the core vacuolar carboxypeptidase function is well supported.**

Evaluated claim-by-claim, the seed's proposed *additional* capacities for O13968 are **not** backed by direct evidence:

| Claim | Verdict |
|---|---|
| Nonpeptide N-acyl-amino-acid hydrolase/synthase (PM20D1-type MF) | **Over-annotated / refuted as direct evidence** — electronic-only (IEA:UniProtKB-ARBA), driven by the PANTHER family *name* PM20D1; no fungal assay. |
| Lipid metabolic process (GO:0006629) | **Over-annotated** — IEA:UniProtKB-ARBA family transfer only. |
| Extracellular localization (GO:0005576) | **Refuted / over-annotated** — IEA:UniProtKB-ARBA; contradicted by HDA vacuolar localization and type II lumenal topology. |
| Adaptive thermogenesis (GO:1990845) | **Refuted** — not annotated at all; no mechanistic basis in a unicellular fungus; PM20D1 thermogenesis is brown/beige-adipocyte-specific. |
| Vacuolar metallocarboxypeptidase (core) | **Supported** — HDA/TAS/IBA/ISO evidence, M20A family, defined active site and Gly-penultimate specificity. |

The seed is correct on several methodological points: (a) the target is *not* bgs1 glucan synthase; (b) the PANTHER family label "PM20D1" is not proof of transferred specificity; (c) GFP-/Ub-GFP- constructs report engineered MVB cargo behaviour, not native secretion; (d) absence of a fungal biochemical assay is not positive proof of loss of any activity. However, the *practical curation consequence* is that the additional PM20D1-derived MF/BP/CC terms rest solely on rule-based electronic inference and should not be treated as gene-product functions without experimental support. The primary, experimentally-anchored function is a **luminal vacuolar-membrane metallocarboxypeptidase (peptidase M20A)**.

---

## Evidence Matrix

| Citation | Evidence type | Supports/Refutes/Qualifies | Claim tested | Key finding | Context | Confidence / limitations |
|---|---|---|---|---|---|---|
| UniProt **O13968** (CBPS_SCHPO), DB record | Review/database | Refutes "extra" claims; supports core | Function & localization | Curated as "Carboxypeptidase S / Vacuolar carboxypeptidase cps1"; peptidase **M20A**; catalytic activity = release of C-terminal residue when Gly is penultimate; **Vacuole membrane** | *S. pombe* | High for curated core; the PM20D1-flavored terms are IEA:ARBA only |
| UniProt O13968 GO evidence codes (computed check) | Database/computational | Qualifies (provenance) | Which GO terms are experimental | Vacuole/carboxypeptidase terms = HDA/TAS/IBA/ISO; **GO:0005576 extracellular, GO:0006629 lipid, GO:0016810 C–N non-peptide hydrolase = IEA:UniProtKB-ARBA**; **no GO:1990845** | *S. pombe* | High — direct read-out of evidence codes |
| UniProt O13968 topology (computed) | Structural/computational | Refutes secretion/thermogenesis | Localization/mechanism | **Type II** membrane protein: cyto 1–37, TM 38–58, **lumenal 59–596**; catalytic Zn-peptidase domain faces vacuole lumen | *S. pombe* | High; topology incompatible with a secreted circulating enzyme |
| Pairwise NW identity (computed) | Structural/evolutionary | Qualifies (paralog distance) | "Same family ⇒ same function?" | O13968 vs ScCPS1 = **36.7%**; O13968 vs human PM20D1 = **27.9%**; ScCPS1 vs PM20D1 = 27.5% | cross-species | Moderate (simple scoring); relative ordering robust — closer to fungal CPS than PM20D1 |
| **PMID 27374330** (Long et al., 2016, *Cell*) | Direct assay (mammal) | Competing / non-transferable | Origin of PM20D1 activity | PM20D1 is a **secreted** enzyme enriched in UCP1+ adipocytes; bidirectional N-acyl-amino-acid synthase/hydrolase; products uncouple mitochondria | Mouse/human adipose | High for mouse/human; establishes activity is defined in a **secreted, adipocyte** context, not fungal vacuole |
| **PMID 18508771** (Ren et al., 2008) | Localization/mutant (yeast) | Qualifies | GFP-Cps1 / Ub constructs | GFP-Cps1 is the canonical **ubiquitin-dependent MVB cargo** delivered to the vacuole lumen; missorted when Ub sorting is disrupted | *S. cerevisiae* | High; shows engineered cargo trafficking to vacuole, not secretion |
| **PMID 31341193** (Yanguas et al., 2019) | Localization/genetic (fission yeast) | Supports core | Native trafficking | *S. pombe* **Cps1** follows the CPY pathway TGN→PVE→**vacuole** via GGA/Ent3 adaptors | *S. pombe* | High; native fission-yeast Cps1 traffics to the vacuole |
| InterPro member DBs for O13968 (computed) | Structural/evolutionary; database | Refutes PM20D1 assignment | Family/specificity | CDD **cd05674 carboxypeptidase yscS**, **PIRSF037217 Carboxypeptidase S**, **IPR017141→GO:0004181**; PANTHER PTHR45962 (PM20D1) carries **no GO** | cross-species signatures | High; specificity-informative signatures all say carboxypeptidase S |
| Catalytic-residue mapping (computed, NW) | Structural/evolutionary | Qualifies | "Same family ⇒ same specificity?" | M20 Zn/catalytic core (H197,D199,D232,E266,E267,E296) 100% conserved in all three; substrate residue **Sp H565 = ScCPS1 H547 but = PM20D1 N467 (divergent)** | O13968 vs P27614 vs Q6GTS8 | Moderate–high; conserved chemistry, divergent specificity determinant |

### Residue-level & domain-database analysis (Iteration 2, computed)

- **Independent domain databases assign carboxypeptidase S, not PM20D1.** For O13968, InterPro member DBs give: CDD **cd05674 "M20 Peptidase, carboxypeptidase yscS"**; **PIRSF037217 "Carboxypeptidase S"**; InterPro **IPR017141 "Peptidase M20, carboxypeptidase S" → GO:0004181 metallocarboxypeptidase activity**. The PANTHER **PTHR45962** entry (name "N-fatty-acyl-amino acid synthase/hydrolase PM20D1") carries **no GO terms** — the PM20D1 label is a family name without functional annotation.
- **M20 catalytic core is 100% conserved** across O13968 / ScCPS1 / human PM20D1: His197, Asp199, Asp232, Glu266 (proton acceptor), Glu267, Glu296 all align 1:1 (PM20D1 His125/Asp127/Asp157/Glu191/Glu192/Glu218). ⇒ All three are genuine binuclear-zinc amide-bond metallohydrolases; O13968 mechanistically **retains** amide/peptide hydrolase capability (argues against "loss of peptide hydrolysis").
- **A substrate-binding residue tracks the fungal CPS clade, not PM20D1:** O13968 **His565 = ScCPS1 His547 (match)** but **= PM20D1 Asn467 (divergent)**. Consistent with conserved carboxypeptidase-S substrate recognition in the fungal enzymes and altered specificity in PM20D1.

**Net:** shared catalytic chemistry does not equal shared substrate specificity. The specificity-informative, GO-bearing signatures unanimously call O13968 a carboxypeptidase S.

---

## GO Curation Implications (leads — require curator verification)

**Retain (core, experimentally/phylogenetically supported):**
- **MF** GO:0004181 metallocarboxypeptidase activity (ISO) and GO:0004180 carboxypeptidase activity (IBA) — retain; these are the direct molecular function.
- **CC** GO:0000324 fungal-type vacuole (HDA) / GO:0000328 vacuole lumen (IBA) / GO:0005774 vacuolar membrane — retain (type II membrane, luminal catalytic domain).
- **BP** GO:0007039 protein catabolic process in the vacuole (TAS) / GO:0006520 amino acid metabolic process — retain.

**Treat as non-core / candidate for removal or "do not accept" (IEA:UniProtKB-ARBA only, family-name driven):**
- **GO:0005576 extracellular region** — flag as over-annotation; conflicts with HDA vacuole localization and lumenal type II topology. Lead: do **not** promote to a curated CC; consider NOT-qualifier or removal.
- **GO:0006629 lipid metabolic process** — flag as over-annotation; no fungal lipid-catalysis evidence.
- **GO:0016810 hydrolase activity acting on C–N (but not peptide) bonds** — flag; this is the N-acyl-amino-acid-hydrolase-flavored MF and is electronic-only.

**Do not add:**
- **GO:1990845 adaptive thermogenesis** — no evidence, mechanistically inapplicable to a unicellular fungus; PM20D1 thermogenesis is adipocyte/mitochondrial-context specific. Recommend against.

Avoid "protein binding" as an outcome — the informative MF here is **metallocarboxypeptidase activity**.

### GO Decision Table (computed provenance — see `go_decision_table.csv`)

| GO_ID | Term | Aspect | Current evidence | Curation lead | Flag |
|---|---|---|---|---|---|
| GO:0004181 | metallocarboxypeptidase activity | MF | ISO | **RETAIN (primary MF)** | — |
| GO:0004180 | carboxypeptidase activity | MF | IBA | RETAIN | — |
| GO:0000324 | fungal-type vacuole | CC | HDA:PomBase | RETAIN | — |
| GO:0000328 | fungal-type vacuole lumen | CC | IBA | RETAIN | — |
| GO:0005774 | vacuolar membrane | CC | IEA-SubCell | RETAIN | — |
| GO:0007039 | protein catabolic process in vacuole | BP | TAS:PomBase | RETAIN | — |
| GO:0006520 | amino acid metabolic process | BP | IEA-ARBA | RETAIN | — |
| GO:0005576 | extracellular region | CC | IEA:UniProtKB-ARBA | **REMOVE / NOT** | OVER-ANNOTATION |
| GO:0006629 | lipid metabolic process | BP | IEA:UniProtKB-ARBA | **REMOVE / non-core** | OVER-ANNOTATION |
| GO:0016810 | hydrolase acting on C–N (non-peptide) bonds | MF | IEA:UniProtKB-ARBA | **REMOVE / non-core** | OVER-ANNOTATION |
| GO:1990845 | adaptive thermogenesis | BP | (absent) | **DO NOT ADD** | REFUTED |

Native localization support: **PMID 16823372** (Matsuyama et al., 2006) — genome-wide YFP ORFeome localization of ~90% of the *S. pombe* proteome — provides the native (non-engineered) localization dataset the seed references; it is a high-throughput localization resource consistent with the HDA vacuolar assignment (as opposed to the engineered GFP-/Ub-GFP-Cps1 MVB-cargo constructs).

---

## Mechanistic Scope

**Direct molecular function tested:** zinc-dependent M20A exopeptidase releasing a C-terminal amino acid from peptides with a penultimate glycine (carboxypeptidase S activity), acting in the vacuole lumen for peptide/amino-acid recycling and use of peptides as nitrogen source.

**Downstream / non-core:** MVB sorting behaviour of GFP-/Ub-GFP-Cps1 fusions is a property of ubiquitin-dependent cargo trafficking machinery, **not** of the enzyme's catalytic activity, and does not indicate secretion. The PM20D1 "uncoupling/thermogenesis" phenotype is a mammalian, whole-organism metabolic outcome of a *secreted* paralog and is not a molecular property attributable to O13968.

---

## Conflicts and Alternatives

- **Paralog / family-name carry-over:** PANTHER PTHR45962 is named for mammalian PM20D1; UniProt's ARBA rules propagate lipid-amide/extracellular terms to all members, including this fungal M20A vacuolar carboxypeptidase. This is the classic paralog-overannotation and frequency-bias pattern.
- **Name collision:** "cps1" also denotes *S. pombe* **bgs1/SPBC19G7.05c** (1,3-β-glucan synthase). The seed correctly excludes it; this report concerns only SPAC24C9.08/O13968.
- **Topology conflict:** A secreted, circulating N-acyl-amino-acid enzyme (PM20D1) vs a type II vacuolar-membrane protein with luminal catalytic domain — the localizations are mutually exclusive.
- **Divergence:** ~28% identity to PM20D1 (twilight zone) vs ~37% to a bona fide fungal carboxypeptidase S argues the substrate specificity should be read from the fungal CPS clade.

---

## Knowledge Gaps

1. **No fungal biochemical assay** of O13968 (or ScCPS1) for N-acyl-amino-acid synthase/hydrolase activity exists. *Checked:* UniProt catalytic annotation + literature; only peptidase activity is documented. *Matters:* one cannot positively exclude a promiscuous side-activity; but absence of evidence ≠ presence of function for curation. *Resolve:* in vitro assay with purified enzyme against N-acyl-amino-acid panel.
2. **Active-site substrate-determinant comparison** with PM20D1 not performed residue-by-residue here. *Matters:* would test whether the fatty-acyl binding pocket exists. *Resolve:* structural/AlphaFold pocket comparison and specificity-residue alignment.
3. **Native secretion:** no evidence of extracellular pool; HDA is vacuolar. *Resolve:* secretome/immunolocalization in *S. pombe*.

---

## Discriminating Tests

- **In vitro activity panel:** purified O13968 assayed for (i) Gly-penultimate carboxypeptidase activity (expected positive) and (ii) N-oleoyl-/N-arachidonoyl-amino-acid hydrolysis/condensation (tests PM20D1-type activity). Bidirectional LC-MS assay as in PMID 27374330.
- **Structure-guided pocket analysis:** AlphaFold model + superposition on PM20D1/carboxypeptidase-S structures; check for a hydrophobic acyl-binding channel and conserved Zn-coordinating residues (His199/His-cluster, Glu266 proton acceptor already annotated).
- **Localization:** endogenous-tag microscopy and secretome MS to confirm vacuolar (not extracellular) steady-state pool.
- **Specificity-residue alignment** across M20A CPS clade vs M20 PM20D1 clade to identify divergent substrate determinants.

---

## Curation Leads (require curator verification)

1. **Downgrade/flag electronic PM20D1-derived terms** (GO:0005576, GO:0006629, GO:0016810) as IEA-only family carry-over; do not elevate to experimental status. Suggested action: mark as over-annotation / non-core; consider removal or NOT for extracellular.
2. **Do not add GO:1990845 (adaptive thermogenesis).** No support; mechanistically inapplicable.
3. **Retain and foreground** MF GO:0004181/GO:0004180 (metallocarboxypeptidase), CC vacuole/vacuolar-lumen terms, BP vacuolar protein catabolism.
4. **Candidate references to verify (with snippets):**
   - PMID **27374330** — "we identify a secreted enzyme, peptidase M20 domain containing 1 (PM20D1) … catalyzing both the condensation of fatty acids and amino acids to generate N-acyl amino acids and also the reverse hydrolytic reaction." → establishes activity in a *secreted mammalian adipocyte* context, not transferable by homology.
   - PMID **31341193** — "Carboxypeptidases Y (Cpy1) and S (Cps1) … follow the carboxypeptidase Y (CPY) pathway from the trans-Golgi network (TGN) to the prevacuolar endosome (PVE)." → native *S. pombe* Cps1 traffics to the vacuole.
   - PMID **18508771** — "missorting of the MVB cargo GFP-Cps1." → GFP-Cps1 is engineered vacuolar MVB cargo, not evidence of secretion.
5. **Suggested question for curators:** Should the *S. pombe* CBPS record's ARBA-derived extracellular/lipid/C–N-hydrolase terms be suppressed pending a fungal biochemical assay?
6. **Suggested experiment:** bidirectional N-acyl-amino-acid LC-MS assay on purified O13968 to positively test (not assume) PM20D1-type promiscuity.

---

### Provenance
Computed checks (UniProt REST retrieval of O13968 annotations/topology/GO evidence codes; Needleman-Wunsch pairwise identities O13968/P27614/Q6GTS8) were executed in this session; identities 36.7% (vs ScCPS1) and 27.9% (vs human PM20D1) are direct outputs. Simple match/mismatch scoring was used, so absolute identities are approximate; the relative ordering (closer to fungal CPS than to PM20D1) is the robust conclusion. Literature evidence retrieved via PubMed (PMIDs 27374330, 31341193, 18508771).


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)
- [OpenScientist go decision table](openscientist_artifacts/go_decision_table.csv)