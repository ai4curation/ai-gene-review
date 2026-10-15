---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-09T18:29:14.962601'
end_time: '2026-10-09T18:56:15.398956'
duration_seconds: 1620.44
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: SPHCR
  gene: pcpB
  gene_symbol: pcpB
  uniprot_accession: P42535
  taxon_id: NCBITaxon:46429
  taxon_label: Sphingobium chlorophenolicum
  focus_type: free_text
  hypothesis_slug: ancestral-phenol-pocket-alphafold
  hypothesis_text: The ancestral substrate of Sphingobium chlorophenolicum PcpB (UniProt
    P42535) is a naturally occurring para-substituted phenol, and the substrate pocket
    of its AlphaFold model, combined with the published structure-activity determinants,
    should narrow the candidate set.
  term_context: '- Background the curator can state: this FAD-dependent monooxygenase
    hydroxylates pentachlorophenol, a pesticide introduced in the 1930s, and is the
    rate-limiting step of a degradation pathway that appears to have been assembled
    recently by patching horizontally acquired enzymes into existing metabolism. Its
    turnover number for pentachlorophenol is about 0.024 per second and the reaction
    uncouples extensively, producing hydrogen peroxide in a futile cycle. Published
    structure-activity work reports that substrate binding and activity are favoured
    by a low pKa for the phenolic proton, increased hydrophobicity, and a substituent
    ortho to the phenol hydroxyl.

    - Decide this with structural evidence. Retrieve the AlphaFold DB model for UniProt
    P42535 (https://alphafold.ebi.ac.uk/entry/P42535 ; mmCIF https://alphafold.ebi.ac.uk/files/AF-P42535-F1-model_v4.cif)
    and use experimental structures of flavin-dependent phenol hydroxylases in the
    PheA/TfdB family as the comparison point.

    - The single decisive analysis: locate the FAD site and the phenol-binding pocket
    in the model, measure the pocket, and determine which naturally occurring phenols
    satisfy both the pocket geometry and the published electronic and steric requirements.
    Consider explicitly biogenic halogenated phenols, nitrophenols, methoxyphenols
    and other plant or microbial phenolics, and rank the best candidates with the
    geometric or electronic reason for each.

    - Also address a mechanistic question the curator cares about: can the pocket
    geometry you measure explain why this enzyme uncouples so extensively, for instance
    by leaving the substrate poorly positioned relative to the C4a-hydroxyflavin?
    A structural explanation for poor coupling would be a substantive result.

    - Report per-residue pLDDT for the pocket and FAD site and state whether model
    confidence supports the conclusion. Run Foldseek or an equivalent search against
    the PDB and AlphaFold DB and list the nearest structural neighbours with their
    annotated reactions and known substrates.

    - Name every tool and database version actually invoked and show the real output.
    If a tool cannot be run programmatically, say so plainly rather than substituting
    an inferred result for a computed one. An honest inconclusive answer is preferable
    to an overstated one.'
  reference_context: No specific reference context supplied.
  source_file: genes/SPHCR/pcpB/pcpB-ai-review.yaml
  source_selector: free-text
  source_context_yaml: "hypothesis: The ancestral substrate of Sphingobium chlorophenolicum\
    \ PcpB (UniProt P42535) is a naturally\n  occurring para-substituted phenol, and\
    \ the substrate pocket of its AlphaFold model, combined with the\n  published\
    \ structure-activity determinants, should narrow the candidate set.\nfocus_type:\
    \ free_text\ncontext:\n- 'Background the curator can state: this FAD-dependent\
    \ monooxygenase hydroxylates pentachlorophenol,\n  a pesticide introduced in the\
    \ 1930s, and is the rate-limiting step of a degradation pathway that appears\n\
    \  to have been assembled recently by patching horizontally acquired enzymes into\
    \ existing metabolism.\n  Its turnover number for pentachlorophenol is about 0.024\
    \ per second and the reaction uncouples extensively,\n  producing hydrogen peroxide\
    \ in a futile cycle. Published structure-activity work reports that substrate\n\
    \  binding and activity are favoured by a low pKa for the phenolic proton, increased\
    \ hydrophobicity, and\n  a substituent ortho to the phenol hydroxyl.'\n- Decide\
    \ this with structural evidence. Retrieve the AlphaFold DB model for UniProt P42535\
    \ (https://alphafold.ebi.ac.uk/entry/P42535\n  ; mmCIF https://alphafold.ebi.ac.uk/files/AF-P42535-F1-model_v4.cif)\
    \ and use experimental structures\n  of flavin-dependent phenol hydroxylases in\
    \ the PheA/TfdB family as the comparison point.\n- 'The single decisive analysis:\
    \ locate the FAD site and the phenol-binding pocket in the model, measure\n  the\
    \ pocket, and determine which naturally occurring phenols satisfy both the pocket\
    \ geometry and the\n  published electronic and steric requirements. Consider explicitly\
    \ biogenic halogenated phenols, nitrophenols,\n  methoxyphenols and other plant\
    \ or microbial phenolics, and rank the best candidates with the geometric\n  or\
    \ electronic reason for each.'\n- 'Also address a mechanistic question the curator\
    \ cares about: can the pocket geometry you measure explain\n  why this enzyme\
    \ uncouples so extensively, for instance by leaving the substrate poorly positioned\
    \ relative\n  to the C4a-hydroxyflavin? A structural explanation for poor coupling\
    \ would be a substantive result.'\n- Report per-residue pLDDT for the pocket and\
    \ FAD site and state whether model confidence supports the\n  conclusion. Run\
    \ Foldseek or an equivalent search against the PDB and AlphaFold DB and list the\
    \ nearest\n  structural neighbours with their annotated reactions and known substrates.\n\
    - Name every tool and database version actually invoked and show the real output.\
    \ If a tool cannot be\n  run programmatically, say so plainly rather than substituting\
    \ an inferred result for a computed one.\n  An honest inconclusive answer is preferable\
    \ to an overstated one.\nreference_id: []"
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
- filename: analysis_pcpB_candidate_ranking.csv
  path: openscientist_artifacts/analysis_pcpB_candidate_ranking.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist pcpB candidate ranking
- filename: data_AF-P42535-F1-confidence.json
  path: openscientist_artifacts/data_AF-P42535-F1-confidence.json
  media_type: application/json
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist AF P42535 F1 confidence
- filename: data_AF-P42535-F1-pae.json
  path: openscientist_artifacts/data_AF-P42535-F1-pae.json
  media_type: application/json
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist AF P42535 F1 pae
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

- **Organism code:** SPHCR
- **Taxon:** Sphingobium chlorophenolicum (NCBITaxon:46429)
- **Gene directory:** pcpB
- **Gene symbol:** pcpB
- **UniProt accession:** P42535

## Focus

- **Focus type:** free_text
- **Hypothesis slug:** ancestral-phenol-pocket-alphafold
- **Source file:** genes/SPHCR/pcpB/pcpB-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

The ancestral substrate of Sphingobium chlorophenolicum PcpB (UniProt P42535) is a naturally occurring para-substituted phenol, and the substrate pocket of its AlphaFold model, combined with the published structure-activity determinants, should narrow the candidate set.

## Term and Decision Context

- Background the curator can state: this FAD-dependent monooxygenase hydroxylates pentachlorophenol, a pesticide introduced in the 1930s, and is the rate-limiting step of a degradation pathway that appears to have been assembled recently by patching horizontally acquired enzymes into existing metabolism. Its turnover number for pentachlorophenol is about 0.024 per second and the reaction uncouples extensively, producing hydrogen peroxide in a futile cycle. Published structure-activity work reports that substrate binding and activity are favoured by a low pKa for the phenolic proton, increased hydrophobicity, and a substituent ortho to the phenol hydroxyl.
- Decide this with structural evidence. Retrieve the AlphaFold DB model for UniProt P42535 (https://alphafold.ebi.ac.uk/entry/P42535 ; mmCIF https://alphafold.ebi.ac.uk/files/AF-P42535-F1-model_v4.cif) and use experimental structures of flavin-dependent phenol hydroxylases in the PheA/TfdB family as the comparison point.
- The single decisive analysis: locate the FAD site and the phenol-binding pocket in the model, measure the pocket, and determine which naturally occurring phenols satisfy both the pocket geometry and the published electronic and steric requirements. Consider explicitly biogenic halogenated phenols, nitrophenols, methoxyphenols and other plant or microbial phenolics, and rank the best candidates with the geometric or electronic reason for each.
- Also address a mechanistic question the curator cares about: can the pocket geometry you measure explain why this enzyme uncouples so extensively, for instance by leaving the substrate poorly positioned relative to the C4a-hydroxyflavin? A structural explanation for poor coupling would be a substantive result.
- Report per-residue pLDDT for the pocket and FAD site and state whether model confidence supports the conclusion. Run Foldseek or an equivalent search against the PDB and AlphaFold DB and list the nearest structural neighbours with their annotated reactions and known substrates.
- Name every tool and database version actually invoked and show the real output. If a tool cannot be run programmatically, say so plainly rather than substituting an inferred result for a computed one. An honest inconclusive answer is preferable to an overstated one.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: The ancestral substrate of Sphingobium chlorophenolicum PcpB (UniProt P42535) is a naturally
  occurring para-substituted phenol, and the substrate pocket of its AlphaFold model, combined with the
  published structure-activity determinants, should narrow the candidate set.
focus_type: free_text
context:
- 'Background the curator can state: this FAD-dependent monooxygenase hydroxylates pentachlorophenol,
  a pesticide introduced in the 1930s, and is the rate-limiting step of a degradation pathway that appears
  to have been assembled recently by patching horizontally acquired enzymes into existing metabolism.
  Its turnover number for pentachlorophenol is about 0.024 per second and the reaction uncouples extensively,
  producing hydrogen peroxide in a futile cycle. Published structure-activity work reports that substrate
  binding and activity are favoured by a low pKa for the phenolic proton, increased hydrophobicity, and
  a substituent ortho to the phenol hydroxyl.'
- Decide this with structural evidence. Retrieve the AlphaFold DB model for UniProt P42535 (https://alphafold.ebi.ac.uk/entry/P42535
  ; mmCIF https://alphafold.ebi.ac.uk/files/AF-P42535-F1-model_v4.cif) and use experimental structures
  of flavin-dependent phenol hydroxylases in the PheA/TfdB family as the comparison point.
- 'The single decisive analysis: locate the FAD site and the phenol-binding pocket in the model, measure
  the pocket, and determine which naturally occurring phenols satisfy both the pocket geometry and the
  published electronic and steric requirements. Consider explicitly biogenic halogenated phenols, nitrophenols,
  methoxyphenols and other plant or microbial phenolics, and rank the best candidates with the geometric
  or electronic reason for each.'
- 'Also address a mechanistic question the curator cares about: can the pocket geometry you measure explain
  why this enzyme uncouples so extensively, for instance by leaving the substrate poorly positioned relative
  to the C4a-hydroxyflavin? A structural explanation for poor coupling would be a substantive result.'
- Report per-residue pLDDT for the pocket and FAD site and state whether model confidence supports the
  conclusion. Run Foldseek or an equivalent search against the PDB and AlphaFold DB and list the nearest
  structural neighbours with their annotated reactions and known substrates.
- Name every tool and database version actually invoked and show the real output. If a tool cannot be
  run programmatically, say so plainly rather than substituting an inferred result for a computed one.
  An honest inconclusive answer is preferable to an overstated one.
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

# PcpB (P42535) — Ancestral para-substituted-phenol hypothesis: focused curation report

**Gene:** pcpB (pentachlorophenol 4-monooxygenase), *Sphingobium chlorophenolicum* (NCBITaxon:46429)
**UniProt:** P42535 (PCPB_SPHCR), 538 aa; EC 1.14.13.50; FAD cofactor; PheA/TfdB FAD monooxygenase family (Pfam PF01494 FAD_binding_3)
**Focus type:** free_text — hypothesis slug `ancestral-phenol-pocket-alphafold`
**Hypothesis:** The ancestral substrate of PcpB is a naturally occurring *para*-substituted phenol, and the AlphaFold pocket + published SAR should narrow the candidate set.

---

## Executive Judgment

**Verdict: Partially supported (biochemically well-supported premise; structurally unresolved by direct measurement).**

The *chemical* half of the hypothesis is strongly supported. PcpB is a *para*-specific phenol monooxygenase with documented promiscuity across *para*-substituted phenols (halo-, nitro-, amino-, cyano-), and its published structure–activity relationship (low phenolic pKa, hydrophobicity, an *ortho* substituent) plus the "recently assembled pathway" evolutionary context make it very plausible that the enzyme descends from one acting on a naturally occurring *para*-substituted phenol rather than on the man-made pesticide pentachlorophenol (PCP, introduced in the 1930s). An SAR-based ranking narrows the natural candidate set to **biogenic ortho-halogenated para-substituted phenols with free 3,5 positions** (2,4,6-tribromophenol, 2,4,6-trichlorophenol, 2,6-dichlorophenol, 2,4-dibromophenol), with nitrophenols as secondary candidates and methoxyphenols / plant alkyl-phenols essentially excluded on electronic or positional grounds.

The *structural* half — "measure the pocket in the AlphaFold model and read off which phenols fit its geometry" — **could not be delivered as a direct computation**, and I say so plainly. The AlphaFold model (AF-P42535-F1, v6) is high quality but contains **no FAD and no substrate**, and the nearest experimental structure (p-hydroxybenzoate hydroxylase, PHBH) is only ~20% identical, so a cross-identity superposition to import the flavin/substrate position failed (least-squares fit on 3 atoms). Consequently, pocket volume and the substrate-to-C4a-hydroxyflavin distance were **not measured de novo**; the candidate ranking rests on the *published SAR + handbook physicochemistry*, not on a pocket-geometry measurement. The mechanistic uncoupling explanation is therefore an SAR/electronic argument, not a structural distance measurement.

**Most important caveats:**
- The specific ancestral molecule is *unknowable* from current evidence; "a biogenic ortho-halophenol" is the best-constrained candidate *class*, not a proven identity.
- The seed-provided mmCIF URL (…model_v4.cif) is retired; the live model is **v6**. All results here use v6.
- Candidate scoring is a transparent, assumption-driven heuristic built from published SAR rules; it ranks plausibility, it does not prove turnover.

This is a **background/evolutionary insight**, not a function-assignment change. It should **not** alter the core experimentally-supported GO annotations (see GO Curation Implications).

---

## Evidence Matrix

| # | Citation (PMID) | Evidence type | Supports/Refutes/Qualifies | Claim tested | Key finding | Context | Confidence & limitations |
|---|---|---|---|---|---|---|---|
| 1 | 22482720 (Hlouchova et al. 2012, Biochemistry) | Direct assay + SAR | **Supports** (premise) | PcpB SAR; PCP is a poor/non-ancestral substrate | Binding/activity enhanced by low phenolic pKa, hydrophobicity, and an *ortho* substituent; kcat(PCP)=0.024/s "not well evolved"; pathway "assembled … by … horizontal gene transfer"; uncoupling 0–100%, ↑ by bulky 3/4/5 substituents, ↓ by ortho-Cl | Purified enzyme, in vitro | High. The decisive SAR source. |
| 2 | 10907421 (Zablotowicz et al. 1999) | Direct assay (recombinant) | **Supports** | Para-substituted-phenol substrate range | pcpB (in *E. coli*) acts on p-nitrophenol, p-nitrocatechol, 2,4-DNP, 4,6-dinitro-o-cresol; NOT 2,6-DNP, o-/m-nitrophenol, picric acid | *Sphingomonas* UG30 pcpB in *E. coli* | High for para-specificity; strain UG30 pcpB (near-identical ortholog). |
| 3 | UniProt P42535 (ECO:0000269|PubMed:12169590, 22482720) | Database (expert, exp-backed) | **Supports** | Para-specific hydroxylation | "removes hydrogen and nitro, amino, and cyano groups … at the para position in relation to the hydroxyl of phenol"; FAD cofactor; homodimer; PheA/TfdB family | Curated record | High; para-rule is explicit. |
| 4 | 23676275 (Yadid et al. 2013, PNAS) | Mechanistic/evolutionary | **Qualifies/Supports** | Why turnover is slow | Slow PcpB turnover (0.02/s) is maintained by selection so PcpD can sequester the toxic TCBQ intermediate | *S. chlorophenolicum* | High; shows slow kcat is partly adaptive, not purely "poorly evolved" — a competing nuance to the ancestral-substrate framing. |
| 5 | This work — AlphaFold DB AF-P42535-F1 **v6**; `parse_alphafold_confidence`; `phenix.molprobity` | Computational (structural) | **Supports** (fold/confidence) | Fold identity & model confidence | Mean pLDDT 91.5; FAD motifs res 16–45 (97.4) and 288–298 (97.3) very high; GxGxxG at 21–26; MolProbity 0.97, clashscore 2.04 | AlphaFold2 monomer v2.0 pipeline | High for fold; **no FAD/substrate in model**. |
| 6 | This work — Foldseek webserver (search.foldseek.com, 3Di; pdb100 + afdb-swissprot) | Computational (structural neighbours) | **Supports** (family) | Nearest structural neighbours | All FAD-dependent aromatic/phenol monooxygenases at 20–28% id: 6-methylpretetramide 4-MO (Q3S8Q4), OxyS (4k2x), PgaE (2qa1), VibO (7yj0), PieE+FAD+substrate (6u0s) | Group-A flavoprotein hydroxylase fold | High for fold class; no close (≥40%) experimental homolog ⇒ consistent with recent/HGT origin. |
| 7 | This work — `phenix.superpose_pdbs` vs PHBH (PDB 1PBE, FAD + p-hydroxybenzoate) | Computational (negative) | **Qualifies (limitation)** | Transfer flavin/substrate position to measure pocket | 20.1% identity, LS fit on **3 atoms** ⇒ degenerate; pocket geometry & substrate–C4a distance **not** measurable de novo | — | Honest inconclusive; direct "measure the pocket" step not achievable with available tools. |
| 8 | This work — SAR ranking (`analysis/pcpB_candidate_ranking.csv`) | Computational (heuristic) | **Supports (narrows set)** | Which natural phenols fit SAR | Top: 2,4,6-tribromophenol, 2,4,6-trichlorophenol, 2,6-dichlorophenol, 2,4-dibromophenol; nitrophenols secondary; methoxyphenols/plant alkylphenols excluded; PCP binds best but couples worst | Derived from SAR + handbook pKa/logP | Moderate; heuristic, not docking. |
| 9 | 21903310; 26517387 | Review/field data | **Supports** (biogenic availability) | Are top candidates naturally occurring? | 2,4,6-tribromophenol is a dominant natural marine product; brominated aromatics are biosynthesised by algae/sponges/cyanobacteria | Marine ecosystems | Moderate; establishes natural occurrence, not that *S. chlorophenolicum*'s ancestor met it. |

---

## GO Curation Implications (leads — require curator verification)

This hypothesis is **evolutionary background**, not a function reassignment. It does **not** justify removing or weakening the experimentally-supported core annotations.

| GO term | Aspect | Current basis | Recommended action (lead) |
|---|---|---|---|
| GO:0018677 pentachlorophenol monooxygenase activity | MF | IEA (UniProtKB-EC); experimentally backed (PMID 22482720, 25238136) | **Retain.** Experimentally demonstrated; PCP is the validated in vitro/in vivo substrate regardless of evolutionary origin. Can be upgraded from IEA to EXP/IDA with PMID 22482720. |
| GO:0071949 FAD binding | MF | IEA (InterPro) | **Retain.** Cofactor confirmed (PMID 22482720); FAD motifs at very high pLDDT. Upgradeable to IDA. |
| GO:0019338 pentachlorophenol catabolic process | BP | IEA (UniPathway) | **Retain**; rate-limiting step (PMID 22482720). |
| *Consider adding* — MF generalization | MF | Promiscuity data | **Lead:** the enzyme's demonstrated activity is broader than PCP. A parent/accompanying MF such as **GO:0018685 "alkane 1-monooxygenase"**-style is wrong; the correct broader parents are **GO:0016709** (oxidoreductase, acting on paired donors, with incorporation of one O, NAD(P)H as one donor) and the family term. A more informative lead is annotating the **para-nitrophenol / chlorophenol 4-monooxygenase** activity shown in PMID 10907421 if a suitable MF child exists. Verify ontology availability before use. |
| "Ancestral substrate = biogenic halophenol" | — | This analysis | **Do NOT add as an annotation.** It is a hypothesis about evolutionary history, not a current molecular function; at most a free-text note in the review. |

**Bottom line for curation:** keep the PCP monooxygenase, FAD-binding, and PCP catabolism annotations; optionally record (non-core, background) that PCP is a recently-acquired xenobiotic substrate of a para-specific phenol hydroxylase whose promiscuity spans natural para-substituted phenols. Avoid "protein binding" — a specific MF (PCP 4-monooxygenase activity; FAD binding) is well supported.

---

## Mechanistic Scope

**Direct molecular function (what is tested):** FAD-dependent, NADPH-consuming aromatic *para*-hydroxylation of phenols — a single-component Class A flavoprotein monooxygenase that forms a C4a-(hydro)peroxyflavin and hydroxylates the ring *para* to the phenolic –OH, replacing H, Cl, NO2, NH2 or CN. This is the gene product's primary, direct activity.

**Downstream / not the direct activity:** PCP detoxification, the assembled PCP catabolic pathway, growth on PCP, and the physiological H2O2/futile-cycle burden are pathway- and phenotype-level consequences. The "ancestral substrate" is an evolutionary inference about the enzyme's history and must be separated from its measured present-day activity.

**Uncoupling (mechanistic question):** The SAR gives a *substrate-electronic/steric* explanation — uncoupling rises with bulky substituents at ring positions 3/4/5 and falls with an ortho-chlorine (PMID 22482720). PCP is fully substituted (3,4,5-Cl present), which is exactly the pattern that maximises uncoupling; the ring is plausibly held sub-optimally relative to the C4a-hydroxyflavin so the oxygenating intermediate decays to H2O2. **I could not convert this into a measured substrate–flavin distance** because the model lacks FAD/substrate and the homolog superposition was degenerate (Finding 7). So the uncoupling account is SAR-based inference, not a structural measurement.

---

## Conflicts and Alternatives

1. **Slow kcat is partly adaptive, not merely "unevolved" (PMID 23676275).** Selection maintains slow PcpB turnover so PcpD can sequester the highly toxic TCBQ intermediate. This complicates the simple "PCP is a bad fit so the enzyme must be optimised for something else" narrative: some of the poor performance on PCP is *selected*, not just *ancestral mismatch*.
2. **Ortholog vs paralog / strain identity.** The broad para-phenol substrate data (PMID 10907421) come from *Sphingomonas* UG30 pcpB, a near-identical ortholog, not literally the ATCC 39723 P42535 protein. High identity makes transfer reasonable but should be verified.
3. **Natural availability ≠ ancestral exposure.** Biogenic tribromophenol is abundant in *marine* systems; *S. chlorophenolicum* is a soil organism. The ancestral enzyme more likely met *terrestrial* microbial/fungal chlorophenols or nitrophenols. The candidate *class* (ortho-halo/para-substituted phenol) is robust; the specific molecule is not.
4. **Methoxyphenols dismissed on electronics, not sterics.** Guaiacol/syringol are abundant natural (lignin) phenols but have high pKa (~9.9); they fail the "low pKa" SAR rule, so their exclusion depends on the electronic rule holding — worth an explicit assay.
5. **Heuristic scoring risk.** My ranking collapses binding and coupling into simple additive terms; a different weighting could reorder nitrophenols vs dihalophenols. The qualitative tiers (halophenols/nitrophenols » methoxyphenols » alkylphenols) are more robust than the exact numbers.

---

## Knowledge Gaps

| Gap | What was checked | Why it matters | What would resolve it |
|---|---|---|---|
| No experimental PcpB structure / no FAD-substrate complex | Foldseek + superposition; nearest exp. homolog ~20% id | Prevents direct pocket measurement and docking | Crystal/cryo-EM of PcpB + FAD + substrate analog; or AlphaFold3/Boltz with FAD+ligand |
| Pocket geometry not measured de novo | AlphaFold v6 has no ligand; superpose failed (3-atom fit) | The seed's "decisive analysis" is unmet | Ligand-aware modelling + cavity analysis (fpocket/CASTp) on a flavin-docked model |
| Actual ancestral substrate unknown | Literature + SAR ranking | Determines whether any specific GO/NTR note is warranted | Ancestral sequence reconstruction + resurrection kinetics across the TfdB/PheA clade |
| kcat/coupling for the predicted natural candidates | Only PCP/tetrachlorophenol/nitrophenols measured | Would test the ranking directly | Steady-state kcat + % uncoupling (H2O2/O2) for 2,4,6-tribromophenol, 2,4,6-trichlorophenol, 2,6-dichlorophenol |
| Soil vs marine source of natural halophenols | Marine biogenic data only | Ecological plausibility of ancestral exposure | Survey terrestrial microbial/fungal chloro-/nitro-phenol production |

---

## Discriminating Tests

1. **Kinetic coupling screen (most decisive):** measure kcat, KM and % uncoupling (H2O2 production per NADPH) for the ranked natural candidates — predict high coupling + reasonable kcat for 2,4,6-trihalophenols and 2,6-dichlorophenol, high uncoupling for PCP, poor binding for guaiacol/syringol, and no turnover for p-cresol.
2. **Ligand-aware structure prediction:** AlphaFold3/Boltz-1 of PcpB + FAD (+ candidate phenol), then cavity analysis (fpocket/CASTp) and measurement of the ring-C4 to flavin-C4a distance across substrates — the structural step this run could not complete.
3. **Ancestral sequence reconstruction (ASR):** reconstruct and resurrect ancestral nodes of the PcpB/TfdB/PheA clade; assay substrate profiles to read the ancestral preference directly.
4. **Active-site mutagenesis:** probe predicted pocket residues (e.g., the aromatic/hydrophobic residues lining the flavin cleft) for effects on uncoupling vs turnover.

---

## Curation Leads (require curator verification)

- **Candidate references to cite in the review (verify snippets):**
  - PMID **22482720** — "substrate binding and activity are enhanced by a low pK(a) for the phenolic proton, increased hydrophobicity, and the presence of a substituent ortho to the hydroxyl group of the phenol"; and "…increased by the presence of bulky substituents at position 3, 4, or 5 and decreased by the presence of a chlorine in the ortho position."
  - PMID **10907421** — "oxidatively metabolized certain other p-substituted nitrophenols, i.e., p-nitrocatechol, 2,4-dinitrophenol (2,4-DNP), and 4,6-dinitrocresol…"; "…were also suitable substrates for the UG30 PCP-4-monooxygenase (pcpB gene expressed in Escherichia coli)."
  - PMID **23676275** — "The toxicity of TCBQ may have exerted selective pressure to maintain slow turnover of PcpB (0.02 s(-1))."
  - PMID **21903310** — "2,4,6-triBPh was dominant isomer in all cetaceans" (biogenic halophenol availability).
- **GO actions:** Retain GO:0018677 (MF), GO:0071949 (MF), GO:0019338 (BP); consider EXP/IDA upgrades from PMID 22482720. Do **not** add any "ancestral/biogenic halophenol" GO term — keep as free-text background only.
- **Suggested questions for the curator:** (a) Should the review note that PCP is a *recently acquired xenobiotic* substrate of a para-specific phenol hydroxylase (promiscuity spans natural para-substituted phenols)? (b) Is a broader MF (para-substituted phenol 4-monooxygenase) desired alongside the PCP-specific term, given PMID 10907421?
- **Suggested experiments:** the kinetic coupling screen and ligand-aware modelling above.

---

## Tools and versions actually invoked (provenance)

- **AlphaFold DB:** entry P42535; model **AF-P42535-F1 version 6** (model date 2025-08-01; AlphaFold Monomer v2.0 pipeline; global pLDDT 91.44). *Note:* the seed-cited `…model_v4.cif` URL returns NoSuchKey (retired); v6 used. Files: model_v6.cif/.pdb, confidence_v6.json, PAE_v6.json.
- **UniProt REST:** P42535.txt (entry v106, 2026-06-10).
- **`parse_alphafold_confidence`** (MCP): mean pLDDT 91.5; per-region values as reported.
- **`phenix.molprobity`** (Phenix): MolProbity 0.97; clashscore 2.04; Rama favored 98.13%.
- **`phenix.superpose_pdbs`** (Phenix): PcpB vs PDB **1PBE** (PHBH); 20.1% id; degenerate 3-atom LS fit (inconclusive).
- **Foldseek webserver** (search.foldseek.com, 3Di mode) vs **pdb100** and **afdb-swissprot**: neighbour list as reported (ran 2026-10-09).
- **Experimental references fetched (RCSB):** 1PBE, 2QA1 (PgaE), 6U0S (PieE).
- **PubMed** (MCP search_pubmed): PMIDs 22482720, 10907421, 23676275, 21903310, 26517387, 18452974.
- **Custom Python** (pandas/numpy/matplotlib): SAR candidate ranking → `analysis/pcpB_candidate_ranking.csv` + figures.

### Candidate ranking (computed; top rows)

| Phenol | Class | pKa | logP | ortho-sub | para OK | ortho-halogen | bulky 3/4/5 | Binding fit | Coupling qual | Ancestral plausibility | Biogenic? |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2,4,6-tribromophenol | biogenic halophenol | 6.10 | 4.13 | Y | Y | Y | 0 | 5.10 | 2.0 | **5.10** | Yes (marine) |
| 2,4,6-trichlorophenol | halophenol | 6.23 | 3.69 | Y | Y | Y | 0 | 4.86 | 2.0 | **4.86** | Partly |
| 2,6-dichlorophenol | biogenic halophenol | 6.79 | 2.75 | Y | Y | Y | 0 | 4.20 | 2.0 | **4.20** | Yes (tick pheromone) |
| 2,4-dibromophenol | biogenic halophenol | 7.80 | 3.50 | Y | Y | Y | 0 | 4.00 | 2.0 | **4.00** | Yes (marine) |
| 4-nitrocatechol | nitrophenol | 6.70 | 1.10 | Y | Y | N | 0 | 3.59 | 1.0 | 1.80 | Yes (microbial) |
| 4-nitrophenol | nitrophenol | 7.15 | 1.91 | N | Y | N | 0 | 2.19 | 1.0 | 1.10 | Yes (microbial) |
| guaiacol | methoxyphenol | 9.93 | 1.32 | Y | Y | N | 0 | 2.06 | 1.0 | 1.03 | Yes (lignin) |
| **pentachlorophenol** | xenobiotic | 4.70 | 5.12 | Y | Y | Y | 3 | **6.15** | **0.2** | 0.62 | **No (1930s)** |
| p-cresol | plant phenolic | 10.26 | 1.94 | N | **N** | N | 0 | 0.00 | 1.0 | 0.00 | Yes |
| tyrosol | plant phenolic | 10.40 | 0.50 | N | **N** | N | 0 | 0.00 | 1.0 | 0.00 | Yes |

*Binding fit and coupling quality are transparent heuristics from published SAR + handbook physicochemistry, not docking scores. PCP = best binder, worst coupler (mechanistic signature of its extensive uncoupling).*


## Artifacts

- [OpenScientist pcpB candidate ranking](openscientist_artifacts/analysis_pcpB_candidate_ranking.csv)
- [OpenScientist AF P42535 F1 confidence](openscientist_artifacts/data_AF-P42535-F1-confidence.json)
- [OpenScientist AF P42535 F1 pae](openscientist_artifacts/data_AF-P42535-F1-pae.json)
- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)