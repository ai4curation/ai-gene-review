---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-20T21:26:44.194310'
end_time: '2026-09-20T21:54:34.546418'
duration_seconds: 1670.35
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: PYROR
  gene: PoMZ_10221
  gene_symbol: PoMZ_10221
  uniprot_accession: F8U970
  taxon_id: NCBITaxon:318829
  taxon_label: Pyricularia oryzae
  focus_type: function_assignment
  hypothesis_slug: rhamnose-enzyme-and-mat-regulatory-capacity
  hypothesis_text: Pyricularia oryzae PoMZ_10221 (F8U970; AEH41994.1/JF740057) retains
    methionine adenosyltransferase regulatory activity, MAT-complex membership and
    participation in SAM biosynthesis in addition to its experimentally supported
    UDP-rhamnose epimerase/reductase activity. Adjudicate each claim independently,
    including catalytic/regulatory coexistence and interaction architecture. PMID22102281
    characterizes the fungal bifunctional enzyme with NADPH-dependent UDP-rhamnose
    formation; cached HTML omits Methods/Results, so read the complete publisher/PMC
    text and exact accession mapping. This is not the fungal dihydroorotate dehydrogenase
    described by an erroneous existing OpenAI report. Frozen TreeGrafter source is
    PTN008946252 in PTHR10491 SF4. Current tree recovers that node in a plant branch
    below eukaryotic PTN000051875 carrying MAT-complex/SAM-biosynthesis IBDs from
    human MAT2B Q9NZL9; the exact fungal accession is absent from the reference tree.
    Current broad regulator IBD PTN000051877 is not in the recovered graft path. Resolve
    actual version/placement evidence rather than assuming all RmlD-fold proteins
    retain or lose MAT regulation. A proven alternative enzyme function is not by
    itself exclusion of a second capacity.
  term_context: No specific term context supplied.
  reference_context: No specific reference context supplied.
  source_file: genes/PYROR/PoMZ_10221/PoMZ_10221-ai-review.yaml
  source_selector: free-text
  source_context_yaml: "hypothesis: Pyricularia oryzae PoMZ_10221 (F8U970; AEH41994.1/JF740057)\
    \ retains methionine adenosyltransferase\n  regulatory activity, MAT-complex membership\
    \ and participation in SAM biosynthesis in addition to its\n  experimentally supported\
    \ UDP-rhamnose epimerase/reductase activity. Adjudicate each claim independently,\n\
    \  including catalytic/regulatory coexistence and interaction architecture. PMID22102281\
    \ characterizes\n  the fungal bifunctional enzyme with NADPH-dependent UDP-rhamnose\
    \ formation; cached HTML omits Methods/Results,\n  so read the complete publisher/PMC\
    \ text and exact accession mapping. This is not the fungal dihydroorotate\n  dehydrogenase\
    \ described by an erroneous existing OpenAI report. Frozen TreeGrafter source\
    \ is PTN008946252\n  in PTHR10491 SF4. Current tree recovers that node in a plant\
    \ branch below eukaryotic PTN000051875 carrying\n  MAT-complex/SAM-biosynthesis\
    \ IBDs from human MAT2B Q9NZL9; the exact fungal accession is absent from\n  the\
    \ reference tree. Current broad regulator IBD PTN000051877 is not in the recovered\
    \ graft path. Resolve\n  actual version/placement evidence rather than assuming\
    \ all RmlD-fold proteins retain or lose MAT regulation.\n  A proven alternative\
    \ enzyme function is not by itself exclusion of a second capacity.\nfocus_type:\
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

- **Organism code:** PYROR
- **Taxon:** Pyricularia oryzae (NCBITaxon:318829)
- **Gene directory:** PoMZ_10221
- **Gene symbol:** PoMZ_10221
- **UniProt accession:** F8U970

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** rhamnose-enzyme-and-mat-regulatory-capacity
- **Source file:** genes/PYROR/PoMZ_10221/PoMZ_10221-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

Pyricularia oryzae PoMZ_10221 (F8U970; AEH41994.1/JF740057) retains methionine adenosyltransferase regulatory activity, MAT-complex membership and participation in SAM biosynthesis in addition to its experimentally supported UDP-rhamnose epimerase/reductase activity. Adjudicate each claim independently, including catalytic/regulatory coexistence and interaction architecture. PMID22102281 characterizes the fungal bifunctional enzyme with NADPH-dependent UDP-rhamnose formation; cached HTML omits Methods/Results, so read the complete publisher/PMC text and exact accession mapping. This is not the fungal dihydroorotate dehydrogenase described by an erroneous existing OpenAI report. Frozen TreeGrafter source is PTN008946252 in PTHR10491 SF4. Current tree recovers that node in a plant branch below eukaryotic PTN000051875 carrying MAT-complex/SAM-biosynthesis IBDs from human MAT2B Q9NZL9; the exact fungal accession is absent from the reference tree. Current broad regulator IBD PTN000051877 is not in the recovered graft path. Resolve actual version/placement evidence rather than assuming all RmlD-fold proteins retain or lose MAT regulation. A proven alternative enzyme function is not by itself exclusion of a second capacity.

## Term and Decision Context

No specific term context supplied.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: Pyricularia oryzae PoMZ_10221 (F8U970; AEH41994.1/JF740057) retains methionine adenosyltransferase
  regulatory activity, MAT-complex membership and participation in SAM biosynthesis in addition to its
  experimentally supported UDP-rhamnose epimerase/reductase activity. Adjudicate each claim independently,
  including catalytic/regulatory coexistence and interaction architecture. PMID22102281 characterizes
  the fungal bifunctional enzyme with NADPH-dependent UDP-rhamnose formation; cached HTML omits Methods/Results,
  so read the complete publisher/PMC text and exact accession mapping. This is not the fungal dihydroorotate
  dehydrogenase described by an erroneous existing OpenAI report. Frozen TreeGrafter source is PTN008946252
  in PTHR10491 SF4. Current tree recovers that node in a plant branch below eukaryotic PTN000051875 carrying
  MAT-complex/SAM-biosynthesis IBDs from human MAT2B Q9NZL9; the exact fungal accession is absent from
  the reference tree. Current broad regulator IBD PTN000051877 is not in the recovered graft path. Resolve
  actual version/placement evidence rather than assuming all RmlD-fold proteins retain or lose MAT regulation.
  A proven alternative enzyme function is not by itself exclusion of a second capacity.
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

# Focused Curation Report — *Pyricularia oryzae* PoMZ_10221 / F8U970

**Hypothesis slug:** rhamnose-enzyme-and-mat-regulatory-capacity
**Focus type:** function_assignment
**Gene:** PoMZ_10221 (UniProt **F8U970**, Swiss-Prot reviewed; EMBL **JF740057 / AEH41994.1**; genome **QBZ54521.1**)
**Organism:** *Pyricularia oryzae* (= *Magnaporthe grisea/oryzae*), NCBITaxon:318829

---

## Executive Judgment

**Verdict on the seed hypothesis: REFUTED (for the MAT claims) / the UDP-rhamnose claim is SUPPORTED.**

The seed proposes that F8U970 *retains* methionine adenosyltransferase (MAT) regulator activity, MAT-complex membership, and participation in S-adenosylmethionine (SAM) biosynthesis **in addition to** its experimentally supported UDP-rhamnose epimerase/reductase activity, and asks that each claim be adjudicated independently.

- The **UDP-rhamnose epimerase/reductase** function is **directly and experimentally supported** (IDA, PMID 22102281). This is the protein's primary, catalytically demonstrated function.
- The **three MAT-related claims** (MAT regulator activity, MAT complex, SAM biosynthesis) are **not supported by any direct, interaction, localization, or mutant evidence.** On F8U970 they exist **only as `IEA:TreeGrafter`** automated annotations propagated through PANTHER **PTHR10491:SF4** ("Methionine adenosyltransferase 2 subunit beta"). They are best explained as **phylogenetic-propagation (paralog-lumping) over-annotations**, not a genuine second capacity.

**Most important caveat:** "Not proven" is not the same as "proven absent." No experiment has *tested* MAT-binding by F8U970. However, the burden of evidence, the twilight-zone homology to MAT2B (22%), the strong homology to true UDP-rhamnose synthases (63%), the absence of any MAT/SAM mention in the primary paper, and the biological implausibility of a MAT2B-type beta regulatory subunit in fungi together make the "retained MAT capacity" claim unsupported for curation purposes.

The seed is also correct on one negative point: **this protein is not the fungal dihydroorotate dehydrogenase** claimed by an earlier automated report — UniProt and the primary literature unambiguously assign UDP-rhamnose synthesis.

---

## Evidence Matrix

| # | Citation | Evidence type | Supports/Refutes/Qualifies | Claim tested | Key finding | Context | Confidence & limitations |
|---|----------|---------------|----------------------------|--------------|-------------|---------|--------------------------|
| 1 | PMID 22102281 (Martinez et al., 2012) | Direct biochemical assay (NMR, enzymology) | **Supports** UDP-rhamnose function; **Refutes** MAT relevance (silent) | Is F8U970 a UDP-rhamnose epimerase/reductase? | "The second gene encodes a bifunctional UDP-4-keto-6-deoxyglucose-3,5-epimerase/-4-reductase that converts UDP-4-keto-6-deoxyglucose to UDP-rhamnose." Fungal pathway needs only two genes. No mention of MAT or SAM. | *Magnaporthe grisea* / *Botryotinia fuckeliana*; in vitro + expression | High for MF; primary paper does not test MAT binding |
| 2 | UniProt F8U970 (Swiss-Prot) | Database (curated) | **Supports** UDP-rhamnose; **Qualifies** MAT terms | Which GO terms are experimental vs computational? | UDP-rhamnose terms GO:0010489, GO:0010490, GO:0019300 are **IDA**; MAT terms GO:0048269 (complex), GO:0048270 (regulator), GO:0006556 (SAM biosynthesis) are **IEA:TreeGrafter** only. Catalytic activities Rhea RHEA:56888 & RHEA:56892 (NADPH). | Reviewed entry | High |
| 3 | PANTHER PTHR10491 / SF4 (via UniProt DR) | Structural/evolutionary (family model) | **Competing / explains artifact** | Source of MAT propagation | Family PTHR10491 = "dTDP-4-dehydrorhamnose reductase"; subfamily **SF4 labeled "MAT2 subunit beta."** The family lumps UDP-/dTDP-sugar epimerase-reductases with the metazoan MAT2B regulator (shared NAD(P)-binding Rossmann/extended-SDR fold, IPR036291). | HMM/tree model | High; explains why MAT IBDs graft onto a sugar-nucleotide enzyme |
| 4 | This report — global NW alignment (BLOSUM62) | Computational (sequence) | **Refutes** MAT orthology; **Supports** UDP-rhamnose orthology | How close is F8U970 to MAT2B vs UDP-rhamnose synthases? | Identity to human **MAT2B (Q9NZL9) = 22.0%** (fold-level noise); to Arabidopsis **UDP-L-rhamnose synthase RHM1 (Q9SYM5) C-domain = 62.8%**. Yeast MAT (SAM2) 24.9% and human MAT2A 25.7% are alignment noise (different folds). | In silico | Medium-high; crude global aligner, but the 63% vs 22% contrast is unambiguous |
| 5 | InterPro IPR005913 (RmlD), IPR029903, Pfam PF04321 (RmlD_sub_bind); UniProt SIMILARITY | Structural/evolutionary | **Supports** UDP-rhamnose family assignment | What fold/family? | F8U970 "belongs to the dTDP-4-dehydrorhamnose reductase family" (RmlD-like, NAD(P)-binding Rossmann). This is the sugar-nucleotide reductase family, not a MAT catalytic fold. | Domain models | High |
| 6 | PMID 31496615 (Murray et al. 2019, review) | Review/database | **Qualifies / competing** | Is the MAT2A/MAT2B β-subunit system organism-general? | "Mammalian systems express two genes" for MATs; MATII = catalytic MAT2A + regulatory MAT2B β-subunit. The β-regulatory architecture is described in mammals, not fungi. | Human/mammalian liver | Medium (review-level) |
| 7 | PMID 32046373 (An et al. 2020) | Mutant/localization/interaction | **Qualifies / competing** | What does MAT2B actually do? | MAT2B is a regulatory subunit that "interacts with G protein-coupled receptor kinase interacting ArfGAP1 [GIT1] to increase the activity of extracellular signal-regulated kinases (ERKs)"; nuclear/cytoplasmic in oocytes. Its function is protein-interaction/signaling scaffolding — a metazoan role with no counterpart evidenced for the fungal enzyme. | Mouse oocytes | Medium-high (direct for MAT2B, not for F8U970) |
| 8 | UniProt G4NCL5 (this report) | Computational/database (genome inventory) | **Refutes** SAM-biosynthesis claim for F8U970 | Does F8U970 perform SAM biosynthesis in *P. oryzae*? | *P. oryzae* encodes a dedicated canonical S-adenosylmethionine synthase **G4NCL5** (EC 2.5.1.6; Pfam PF00438/PF02772/PF02773; PANTHER PTHR11964) — a different gene and a different fold from F8U970 (PF04321, PTHR10491). SAM biosynthesis is handled by G4NCL5, not the UDP-rhamnose enzyme. | *P. oryzae* proteome | High |
| 9 | UniProt G4ML22 (this report) | Computational/database (paralog) | **Competing / explains artifact** | Is the SF4 mislabel systematic? | A second *P. oryzae* RmlD-fold protein **G4ML22** (Pfam PF04321) carries the **identical** PANTHER **PTHR10491:SF4** "MAT2 subunit beta" assignment as F8U970. Multiple fungal sugar-nucleotide enzymes inherit the same spurious MAT label — direct evidence of systematic subfamily mis-annotation, not a genuine F8U970-specific second capacity. | *P. oryzae* proteome | High |

---

## GO Curation Implications

**Lead (requires curator verification):**

- **RETAIN (experimental, core):**
  - MF `GO:0010489` UDP-4-keto-6-deoxy-glucose-3,5-epimerase activity (IDA)
  - MF `GO:0010490` UDP-4-keto-rhamnose-4-keto-reductase activity (IDA)
  - BP `GO:0019300` rhamnose biosynthetic process (IDA)
  - (Consider also a general `nucleotide-sugar biosynthetic process` / dTDP-4-dehydrorhamnose reductase family MF if the curation model prefers it; NADP binding CC/MF is defensible from the reductase reaction.)

- **REMOVE / DO NOT PROPAGATE (over-annotation; `IEA:TreeGrafter` only):**
  - CC `GO:0048269` methionine adenosyltransferase complex
  - MF `GO:0048270` methionine adenosyltransferase regulator activity
  - BP `GO:0006556` S-adenosylmethionine biosynthetic process

  Rationale: no experimental/interaction/localization support; artifact of PTHR10491:SF4 lumping the fungal UDP-rhamnose enzyme with the divergent metazoan MAT2B regulator; biologically implausible in a fungus that lacks a MAT2B-type beta regulatory subunit. **Crucially, SAM biosynthesis in *P. oryzae* is performed by a separate dedicated canonical SAM synthase (G4NCL5, EC 2.5.1.6, PTHR11964), so GO:0006556 on F8U970 is redundant and incorrect.** A co-family paralog (G4ML22) carries the same spurious SF4 "MAT2 beta" tag, confirming the mislabel is systematic.

- **Do not recommend "protein binding"** — a specific, supported MF (the epimerase/reductase activities above) is available.

The evidence supports **MF + BP** (catalysis and rhamnose biosynthesis) as **core**, and argues the **MAT MF/BP/CC as non-core and removable/excludable** (candidate `NOT`/exclusion or simply do-not-propagate).

---

## Mechanistic Scope

**Immediate molecular function (direct):** F8U970 catalyzes the committed epimerization + NADPH-dependent reduction step converting UDP-4-keto-6-deoxy-D-glucose → UDP-β-L-rhamnose (RHEA:56888 then RHEA:56892), the second enzyme of a two-gene fungal UDP-rhamnose pathway.

**Downstream/context (not the tested molecular activity):** rhamnose-containing glycans influence host–pathogen interactions (adhesion, recognition, virulence, biofilm). These are *pathway/phenotype consequences*, not molecular functions of this protein, and their tissue-specific regulation is a transcriptional observation.

**The MAT "function"** would require physical association with a MAT catalytic subunit and modulation of SAM synthase activity — none of which is demonstrated. It is inferred *only* from shared fold via automated propagation.

---

## Conflicts and Alternatives

- **Paralog/family lumping (primary alternative explanation):** PANTHER PTHR10491 contains both sugar-nucleotide epimerase-reductases (RmlD/RHM-type) and the metazoan MAT2B regulator, which share the extended-SDR / NAD(P)-binding Rossmann fold. TreeGrafter grafts F8U970 near a node carrying MAT2B-derived IBDs, exporting MAT terms onto a protein whose real neighbors are UDP-rhamnose synthases (63% identity to RHM1). The seed's own notes ("exact fungal accession absent from reference tree," "broad regulator IBD PTN000051877 not in the recovered graft path") are consistent with an unstable/over-reaching graft.
- **Organism-specific difference:** the source of the propagated IBDs, human MAT2B (Q9NZL9), is characterized specifically as the **mammalian** regulatory β-subunit of MATII (PMID 31496615: "Mammalian systems express two genes"), and its regulatory action operates through protein–protein interactions in metazoan signaling (binds GIT1, activates ERK; PMID 32046373). Fungal methionine adenosyltransferases (e.g., *S. cerevisiae* Sam1/Sam2) are single-subunit homo-oligomeric SAM synthetases without a MAT2B-type β regulatory subunit, so there is no α2β2 MAT complex for F8U970 to join in *P. oryzae*. (Stated as inference from the mammalian-restricted MAT2B literature; not directly disproven experimentally.)
- **Database carry-over:** a prior automated ("OpenAI") report mislabeled the protein as dihydroorotate dehydrogenase; that is a separate, clearly incorrect assignment and should not influence curation.
- **No competing experimental evidence** supports MAT function.

---

## Knowledge Gaps

1. **Direct test of MAT association.** Checked: no interaction/localization data in UniProt or the primary paper. Matters because the seed asks specifically about "catalytic/regulatory coexistence." Resolved by: co-IP / pull-down of F8U970 with *P. oryzae* SAM synthetase, or AlphaFold-Multimer interface scoring — neither currently in evidence.
2. **Exact TreeGrafter version/graft path.** Checked: UniProt reports the SF4 assignment and IEA terms but not the frozen graft node internals; I could not programmatically resolve the specific PTN008946252 vs PTN000051875/PTN000051877 IBD propagation logic. Matters for reproducing exactly which IBD exported the MAT terms. Resolved by: inspecting the PAINT/TreeGrafter annotation for PTHR10491 at the frozen version.
3. **NADP cofactor CC/MF specificity.** The reductase uses NADPH (RHEA:56892) but an explicit `NADP binding` MF is not asserted; low-priority, easily added.

---

## Discriminating Tests

1. **AlphaFold-Multimer / co-IP:** test whether F8U970 forms a complex with the *P. oryzae* methionine adenosyltransferase catalytic subunit. Predicted result if hypothesis false: no stable interface (unlike human MAT2A–MAT2B).
2. **Reciprocal-best-hit / phylogeny with proper outgroups:** place F8U970 among fungal/plant UDP-rhamnose synthases vs MAT2B clade; expect robust grouping with RHM-type enzymes (consistent with 63% identity), not MAT2B.
3. **Δgene metabolite phenotype:** knockout should reduce UDP-rhamnose / rhamnoglycans (already implied by pathway), and should **not** perturb SAM pools if MAT function is absent.
4. **Active-site residue audit:** confirm RmlD reductase catalytic/NADP-binding residues are intact (they are, given retained catalysis), whereas MAT2B-specific regulatory-interface residues are absent.

---

## Curation Leads (verify before applying)

- **Action change:** downgrade/remove the MAT-related `IEA:TreeGrafter` terms (GO:0048269, GO:0048270, GO:0006556) as paralog-driven over-annotations; retain the IDA UDP-rhamnose terms as core.
- **Candidate reference to cite for core function:** **PMID 22102281** — verify snippet: *"The second gene encodes a bifunctional UDP-4-keto-6-deoxyglucose-3,5-epimerase/-4-reductase that converts UDP-4-keto-6-deoxyglucose to UDP-rhamnose."*
- **Candidate GO (retain/core):** GO:0010489, GO:0010490 (MF); GO:0019300 (BP). Optionally add `NADP binding`.
- **Candidate GO (exclude/non-core):** GO:0048269, GO:0048270, GO:0006556.
- **Suggested curator question:** Is there *any* organism-specific evidence (interaction, complexome, localization) that a MAT2B-type beta regulator exists in *P. oryzae*? If not, the CC term is untenable.
- **Suggested experiment:** AlphaFold-Multimer/co-IP of F8U970 with *P. oryzae* SAM synthetase to formally close the "coexistence" question.
- **Note:** flag and discard the earlier "dihydroorotate dehydrogenase" automated assignment as incorrect.

---

## Provenance

- Primary literature: PMID 22102281 abstract (PubMed).
- Records: UniProt Swiss-Prot F8U970 JSON (GO evidence codes, catalytic activities, PANTHER/InterPro/Pfam DR lines).
- Computed: global Needleman–Wunsch (BLOSUM62) pairwise identities — F8U970 vs Q9NZL9 (22.0%), P31153 (25.7%), P19358 (24.9%), Q9SYM5 (62.8%). Executed code and outputs are retained in this iteration's execution log.
- Computed (Iteration 3): UniProt proteome query of *P. oryzae* (taxon 318829) — the organism's canonical SAM synthase is **G4NCL5** (EC 2.5.1.6, Pfam PF00438/PF02772/PF02773, PTHR11964), distinct from F8U970; RmlD-fold paralog **G4ML22** (PF04321) shares the same spurious PTHR10491:SF4 "MAT2 beta" label. Executed code and outputs retained in the Iteration 3 execution log.

## Decision Table (leads — verify before applying)

| GO ID | Aspect | Term | Current evidence | Lead action |
|-------|--------|------|------------------|-------------|
| GO:0010489 | MF | UDP-4-keto-6-deoxy-glucose-3,5-epimerase activity | IDA (PMID 22102281) | **Retain (core)** |
| GO:0010490 | MF | UDP-4-keto-rhamnose-4-keto-reductase activity | IDA (PMID 22102281) | **Retain (core)** |
| GO:0019300 | BP | rhamnose biosynthetic process | IDA (PMID 22102281) | **Retain (core)** |
| GO:0048270 | MF | methionine adenosyltransferase regulator activity | IEA:TreeGrafter only | **Remove / do-not-propagate (over-annotation)** |
| GO:0048269 | CC | methionine adenosyltransferase complex | IEA:TreeGrafter only | **Remove / do-not-propagate (over-annotation)** |
| GO:0006556 | BP | S-adenosylmethionine biosynthetic process | IEA:TreeGrafter only | **Remove (redundant; SAM synthesis done by G4NCL5)** |
| (optional) | MF | NADP binding | inferable from RHEA:56892 reductase | Consider adding |


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)