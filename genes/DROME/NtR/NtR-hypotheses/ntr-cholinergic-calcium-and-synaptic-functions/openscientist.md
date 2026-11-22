---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-21T05:29:02.859306'
end_time: '2026-09-21T05:43:44.661766'
duration_seconds: 881.8
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: DROME
  gene: NtR
  gene_symbol: NtR
  uniprot_accession: Q9W288
  taxon_id: NCBITaxon:7227
  taxon_label: Drosophila melanogaster
  focus_type: function_assignment
  hypothesis_slug: ntr-cholinergic-calcium-and-synaptic-functions
  hypothesis_text: Drosophila melanogaster NtR (Q9W288; CG6698) belongs to an acetylcholine-gated
    channel complex, contributes_to acetylcholine-gated cation-selective channel activity,
    transports calcium or participates in cholinergic/synaptic signaling. Evaluate
    these independently and preserve the contributes_to qualifier. Matthews et al.
    PMID:30429615 Extended Data 10d places the NTR branch outside canonical nicotinic
    acetylcholine receptors; establish what this phylogenetic placement does and does
    not imply about ligand, ion selectivity and neuronal function. Use actual PAINT
    nodes, channel sequence features, primary functional assays and existing family
    evidence. Broad Cys-loop channel homology alone neither establishes acetylcholine
    specificity nor disproves synaptic roles.
  term_context: No specific term context supplied.
  reference_context: No specific reference context supplied.
  source_file: genes/DROME/NtR/NtR-ai-review.yaml
  source_selector: free-text
  source_context_yaml: "hypothesis: Drosophila melanogaster NtR (Q9W288; CG6698) belongs\
    \ to an acetylcholine-gated channel complex,\n  contributes_to acetylcholine-gated\
    \ cation-selective channel activity, transports calcium or participates\n  in\
    \ cholinergic/synaptic signaling. Evaluate these independently and preserve the\
    \ contributes_to qualifier.\n  Matthews et al. PMID:30429615 Extended Data 10d\
    \ places the NTR branch outside canonical nicotinic acetylcholine\n  receptors;\
    \ establish what this phylogenetic placement does and does not imply about ligand,\
    \ ion selectivity\n  and neuronal function. Use actual PAINT nodes, channel sequence\
    \ features, primary functional assays\n  and existing family evidence. Broad Cys-loop\
    \ channel homology alone neither establishes acetylcholine\n  specificity nor\
    \ disproves synaptic roles.\nfocus_type: function_assignment\ncontext: []\nreference_id:\
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
citation_count: 3
artifact_count: 3
artifact_sources:
  openscientist_artifacts_zip: 3
artifacts:
- filename: NtR_GO_decision_table.csv
  path: openscientist_artifacts/NtR_GO_decision_table.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist NtR GO decision table
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

- **Organism code:** DROME
- **Taxon:** Drosophila melanogaster (NCBITaxon:7227)
- **Gene directory:** NtR
- **Gene symbol:** NtR
- **UniProt accession:** Q9W288

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** ntr-cholinergic-calcium-and-synaptic-functions
- **Source file:** genes/DROME/NtR/NtR-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

Drosophila melanogaster NtR (Q9W288; CG6698) belongs to an acetylcholine-gated channel complex, contributes_to acetylcholine-gated cation-selective channel activity, transports calcium or participates in cholinergic/synaptic signaling. Evaluate these independently and preserve the contributes_to qualifier. Matthews et al. PMID:30429615 Extended Data 10d places the NTR branch outside canonical nicotinic acetylcholine receptors; establish what this phylogenetic placement does and does not imply about ligand, ion selectivity and neuronal function. Use actual PAINT nodes, channel sequence features, primary functional assays and existing family evidence. Broad Cys-loop channel homology alone neither establishes acetylcholine specificity nor disproves synaptic roles.

## Term and Decision Context

No specific term context supplied.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: Drosophila melanogaster NtR (Q9W288; CG6698) belongs to an acetylcholine-gated channel complex,
  contributes_to acetylcholine-gated cation-selective channel activity, transports calcium or participates
  in cholinergic/synaptic signaling. Evaluate these independently and preserve the contributes_to qualifier.
  Matthews et al. PMID:30429615 Extended Data 10d places the NTR branch outside canonical nicotinic acetylcholine
  receptors; establish what this phylogenetic placement does and does not imply about ligand, ion selectivity
  and neuronal function. Use actual PAINT nodes, channel sequence features, primary functional assays
  and existing family evidence. Broad Cys-loop channel homology alone neither establishes acetylcholine
  specificity nor disproves synaptic roles.
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

# NtR (Q9W288 / CG6698, *Drosophila melanogaster*) — Function-Assignment Review

**Focus:** Does NtR *directly* have the assigned functions — acetylcholine-gated channel complex (GO:0005892), *contributes_to* acetylcholine-gated cation-selective channel activity (GO:0022848), calcium ion transport (GO:0006816), cholinergic/synaptic signaling (GO:0007271)?

**Hypothesis slug:** ntr-cholinergic-calcium-and-synaptic-functions
**Source:** genes/DROME/NtR/NtR-ai-review.yaml (free-text)

---

## Executive Judgment

**Verdict: Partially supported / over-annotated at the specificity level (homology-only).**

NtR is a *bona fide* member of the Cys-loop ligand-gated ion channel (LGIC) superfamily: it has a *bona fide* extracellular neurotransmitter-gated ion-channel ligand-binding domain (Pfam PF02931), one canonical Cys-loop signature (C337–x13–C351), and a four-transmembrane-helix C-terminal region (M1–M4) in the expected Cys-loop topology. At a **general** level, terms describing it as a **ligand-gated / cation-permeable ion channel of the Cys-loop family localized to the plasma membrane** are defensible.

However, the **specific** claims in the seed hypothesis — that the ligand is **acetylcholine**, that it is a **calcium** transporter, and that it functions in **cholinergic synaptic** transmission — are **not supported by any primary experimental evidence**. Every one of the 15 current GO annotations for Q9W288 is computational: the cholinergic/calcium/synaptic core is **IBA (phylogenetic inference, ECO:0000318)** propagated from the PANTHER subfamily, and the general channel terms are **IEA** from InterPro. There is **no IDA/IMP/IPI/EXP annotation, no electrophysiology, no heterologous-expression assay, and no mutant phenotype** for NtR.

Two independent lines of computational evidence **actively undercut the ACh-specific inheritance**:
1. NtR sits in its **own PANTHER family (PTHR36695)**, *not* the canonical insect nAChR family — consistent with Matthews et al. 2018 (PMID:30429615, Extended Data 10d) placing the NTR branch **outside** canonical nicotinic AChRs.
2. NtR **lacks the loop-C vicinal cysteines** that define α-type ACh-binding subunits, and its **transmembrane/pore region is divergent** (it does not receive the canonical Neur_chan_memb pore fold; it gets a generic AcrB-like TM structural label). Cation-vs-anion selectivity and Ca²⁺ permeability therefore cannot be inferred from homology.

**Bottom line for the curator:** The Matthews phylogenetic placement means broad Cys-loop homology **cannot** be used to justify the ACh-, calcium-, and cholinergic-specific terms. These should be **generalized, flagged as non-core, or down-qualified** (retaining the `contributes_to` hedge where a subunit-level channel term is kept). The general LGIC/ion-channel/plasma-membrane terms may be retained. The hypothesis is **not refuted** (a synaptic role remains possible and is not disproven), but it is **not established** either.

---

## Evidence Matrix

| # | Citation | Evidence type | Supports/Refutes/Qualifies | Claim tested | Key finding | Context | Confidence & limitations |
|---|----------|---------------|----------------------------|--------------|-------------|---------|--------------------------|
| 1 | UniProt Q9W288; QuickGO (GO_REF:0000033, :0000002, :0000108) | Computational (database) | **Qualifies** | Evidence basis of the annotations | All 15 GO annotations are IBA or IEA; **zero experimental** codes | *D. melanogaster* gene product record | High confidence in the fact; means specificity is inference-only |
| 2 | Matthews et al. 2018, **PMID:30429615** (ED Fig 10d; cited from seed) | Structural/evolutionary | **Qualifies / competing** | Is NtR a canonical nAChR? | NTR branch placed **outside** canonical nicotinic AChRs | Aedes/insect Cys-loop phylogeny | Figure not independently retrievable here; phylogeny undercuts ACh-inheritance |
| 3 | InterPro/Pfam for Q9W288 (PF02931; PANTHER PTHR36695) | Structural/evolutionary (computational) | **Qualifies** | Family placement | LBD confirms Cys-loop membership; but own PANTHER family PTHR36695, **not** nAChR family | Domain/orthology analysis | High confidence; supports "divergent, non-canonical" |
| 4 | This work — sequence analysis (Cys positions) | Structural/evolutionary (computational) | **Qualifies / refutes α-subunit** | ACh-binding α-subunit determinants | One Cys-loop (C337–C351); **no loop-C vicinal cysteines** → non-α subunit | 585-aa sequence | Heuristic; α-subunit ACh contact residues absent |
| 5 | This work — Kyte-Doolittle hydropathy | Structural/evolutionary (computational) | **Supports (general) / qualifies (specific)** | Channel topology | Signal peptide + LBD + 4 TM (M1–M4) → canonical Cys-loop architecture | 585-aa sequence | Supports general channel identity; pore selectivity unresolved |
| 6 | InterPro structural assignments (SSF63712 vs SSF82866; PF12248) | Structural/evolutionary (computational) | **Qualifies** | Is the pore a canonical channel pore? | LBD gets Cys-loop folds; TM region gets generic AcrB TM fold, **not** Neur_chan_memb pore | Domain analysis | Divergent pore → cation/Ca selectivity not inferable |
| 7 | Jones, Brown & Sattelle 2007, **PMID:17216517** | Review | **Qualifies** | Existence of divergent subunits | "each insect possesses at least one highly divergent nAChR subunit" | Insect nAChR gene families | Review-level; frames NtR as the expected divergent member |
| 8 | Dent 2006, **PMID:16586016** | Review/evolutionary | **Qualifies** | α vs non-α clades | Invertebrate nAChRs split into α-type and non-α clades; large divergent nAChR-like groups exist | Cross-species Cys-loop phylogeny | Review-level; supports non-α/divergent placement |
| 9 | FlyBase/mygene (gene 43935, FBgn0029147) | Database | **Qualifies** | Is there curated function? | No curated functional summary; only IBA/IEA GO | *D. melanogaster* | Absence of evidence, not evidence of absence |

*No primary functional assay, mutant phenotype, localization, or interaction study specific to NtR was found.*

---

## GO Curation Implications (leads — require curator verification)

| GO ID | Term | Aspect | Current evidence | Lead action | Rationale |
|-------|------|--------|------------------|-------------|-----------|
| GO:0022848 | ACh-gated cation-selective channel activity | MF | IBA | **Generalize** to e.g. GO:0022824 (transmitter-gated monoatomic cation channel) or GO:0005230, **or** keep with `contributes_to` + explicit low-confidence note | ACh ligand not assayed; subfamily outside canonical nAChRs |
| GO:0005892 | acetylcholine-gated channel complex | CC | IBA | **Generalize / flag** | No evidence NtR co-assembles into an ACh receptor pentamer |
| GO:0006816 | calcium ion transport | BP | IBA | **Remove or generalize** to GO:0034220 ion transmembrane transport | Ca²⁺ permeability inherited from α7-like members; NtR pore divergent, untested |
| GO:0007271 | synaptic transmission, cholinergic | BP | IBA | **Generalize / treat as non-core** | Cholinergic identity unproven; no expression/synapse data |
| GO:0005230 | extracellular ligand-gated ion channel activity | MF | IEA | **Retain (general)** | Supported by LBD homology; conservative and defensible |
| GO:0034220 | monoatomic ion transmembrane transport | BP | IBA/IEA | **Retain (general)** | Defensible from 4-TM channel topology |
| GO:0042391 | regulation of membrane potential | BP | IBA | **Retain (general)** | Reasonable for an ion channel |
| GO:0005886 | plasma membrane | CC | IBA | **Retain** | Consistent with signal peptide + 4-TM membrane protein |
| GO:0045202 / 0098794 / 0060079 / 0099565 | synapse / postsynapse / EPSP / postsynaptic transmission | CC/BP | IEA (GOC auto) | **Treat as non-core / flag** | Auto-propagated from the cholinergic terms; no localization data |

**Preserve the `contributes_to` qualifier** wherever a channel-*activity* term is retained: NtR would at most be one subunit contributing to a multimeric channel's activity, so `contributes_to` is the correct hedge and should not be dropped.

**Do not** default to "protein binding" — the LBD-based ligand-gated-ion-channel and ion-transport terms are more informative and are homology-supported at the general level.

---

## Mechanistic Scope

- **Immediate molecular function actually tested by evidence:** membership in the Cys-loop LGIC superfamily via an extracellular ligand-binding domain and a 4-TM channel body. This supports a *general* "transmitter-gated ion channel subunit" identity.
- **Not established as direct activity:** (i) the identity of the gating ligand (acetylcholine vs GABA/histamine/glutamate/protons/orphan), (ii) cation vs anion selectivity, (iii) calcium permeability, (iv) participation in a specific ACh-receptor complex.
- **Downstream / inferred-only:** cholinergic synaptic transmission, EPSP generation, postsynaptic membrane-potential regulation — these are **propagated** from the (unproven) ACh assignment, not measured. They should be treated as pathway-context inferences, not core function.

---

## Conflicts and Alternatives

1. **Phylogenetic placement conflict:** Matthews et al. (PMID:30429615) ED10d and the independent PANTHER family assignment (PTHR36695, not the nAChR family) both place NtR **outside** canonical nAChRs. IBA propagation of ACh-specific terms across a branch that the tree itself separates from nAChRs is internally inconsistent and is the central reason to down-qualify.
2. **Non-α subunit:** absence of loop-C vicinal cysteines means NtR cannot supply the principal (+) ACh-binding face even if it were in an ACh receptor — it could only ever be a structural/complementary subunit.
3. **Divergent pore:** the TM region does not match the canonical channel-pore fold, so cation selectivity and Ca²⁺ transport (α7-like inheritance) are unsupported; NtR could be an anion channel or an orphan/atypical channel.
4. **Paralog/carry-over risk:** the ACh/calcium/synapse terms have the hallmark of homology carry-over from well-studied nAChR α-subunits onto a divergent "orphan" member — the classic over-annotation pattern the review is meant to catch.
5. **Alternative identity:** NtR resembles the "highly divergent" insect Cys-loop subunits (cf. pHCl, CG-series orphans) that are often **not** ACh-gated; several are pH-, GABA-, or ligand-unknown channels.

---

## Knowledge Gaps

| Gap | What was checked | Why it matters | What would resolve it |
|-----|------------------|----------------|-----------------------|
| Gating ligand identity | Domains, phylogeny, sequence — no assay found | ACh-specific terms depend on it | Heterologous expression + agonist screen (ACh, GABA, Glu, His, protons) |
| Ion selectivity (cation vs anion; Ca²⁺) | Pore-fold divergence noted; M2 not confidently classifiable | Justifies "cation-selective" and "calcium transport" | Reversal-potential / ion-substitution electrophysiology |
| Subunit partners / complex | No interaction data | Justifies "acetylcholine-gated channel complex" | Co-IP / proteomics; co-expression functional reconstitution |
| Neuronal/synaptic expression | No curated expression summary retrieved | Justifies synaptic BP/CC terms | scRNA-seq brain atlas, reporter/antibody localization |
| Matthews ED10d specifics | Cited from seed; figure not retrievable here | Anchor for the "outside nAChR" claim | Curator to inspect PMID:30429615 ED Fig 10d and its PAINT nodes |

---

## Discriminating Tests

1. **Two-electrode voltage clamp / patch clamp** on NtR expressed in *Xenopus* oocytes or S2 cells, screening ACh vs GABA/Glu/histamine/protons — distinguishes ACh-gated from alternative-ligand or orphan channel.
2. **Ion-substitution reversal-potential experiments** and Ca²⁺-imaging under agonist — tests cation selectivity and calcium permeability directly.
3. **Co-assembly assay** (tagged NtR + canonical Dα/Dβ nAChR subunits) — tests membership in an ACh receptor complex.
4. **Single-cell brain/VNC expression atlas** query and endogenous tagging — tests neuronal/synaptic localization.
5. **Explicit inspection of the PANTHER PTHR36695 tree / PAINT annotations** — confirm which experimentally characterized node (if any) is the source of the IBA ACh terms; if no experimentally validated ACh-gated member exists in the subfamily, the IBA propagation is unsupported.

---

## Curation Leads (require curator verification)

- **Action change:** Down-qualify or generalize the ACh-specific MF (GO:0022848), CC (GO:0005892), and BP (GO:0006816 calcium; GO:0007271 cholinergic) terms from confident to **homology-only/non-core**; retain general channel terms (GO:0005230, GO:0034220, GO:0042391, GO:0005886). **Keep `contributes_to`** on any retained channel-activity term.
- **Candidate reference to verify — PMID:30429615** (Matthews et al. 2018), Extended Data Fig 10d: verify that the NTR branch is drawn outside the canonical nicotinic AChR clade. *(Snippet must be verified by the curator against the figure; abstract text was not programmatically retrievable in this run.)*
- **Candidate reference — PMID:17216517** (Jones, Brown & Sattelle 2007): snippet to verify — *"each insect possesses at least one highly divergent nAChR subunit."*
- **Candidate reference — PMID:16586016** (Dent 2006): snippet to verify — *"There are two clades of invertebrate nAChRs, one of alpha-type subunits and one of non-alpha subunits..."*
- **Candidate replacement GO terms:** GO:0005230 (extracellular ligand-gated monoatomic ion channel activity) or GO:0022824 (transmitter-gated monoatomic cation channel activity) in place of the ACh-specific GO:0022848, pending assay.
- **Suggested questions for curator:** (1) Does the PTHR36695 subfamily contain any experimentally characterized ACh-gated member that legitimizes the IBA? (2) Is there any transcriptomic evidence of neuronal expression? (3) Should the calcium-transport term be removed entirely given the divergent, untested pore?
- **Suggested experiments:** heterologous electrophysiology with a multi-ligand panel; ion-selectivity measurement; co-assembly test (as above).

---

## Limitations of this review

- No primary functional literature exists for NtR; conclusions rest on sequence/domain/phylogeny analysis plus database evidence codes.
- The Matthews ED10d figure and the PANTHER PAINT nodes were not programmatically retrievable in this run; the "outside canonical nAChR" placement is corroborated independently by the distinct PANTHER family (PTHR36695) but the exact figure should be curator-verified.
- TM/pore selectivity classification (cation vs anion) was not confidently resolvable from sequence alone.


## Artifacts

- [OpenScientist NtR GO decision table](openscientist_artifacts/NtR_GO_decision_table.csv)
- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)