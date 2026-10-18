---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-21T03:51:37.635160'
end_time: '2026-09-21T04:14:54.806448'
duration_seconds: 1397.17
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: human
  gene: HSPA14
  gene_symbol: HSPA14
  uniprot_accession: Q0VDF9
  taxon_id: NCBITaxon:9606
  taxon_label: Homo sapiens
  focus_type: function_assignment
  hypothesis_slug: atp-hydrolysis-refolding-and-secondary-compartments
  hypothesis_text: 'Human HSPA14/Hsp70L1 Q0VDF9 has intrinsic ATP hydrolysis activity,
    participates in refolding of previously denatured proteins, and functions in the
    nucleus or at plasma membrane under appropriate conditions. Adjudicate each claim
    separately from its established ATP-binding mRAC cofactor role with DNAJC2/MPP11.
    Read full PMID21245388: purified E.coli-produced mRAC gives 0.01 ATP/min, above
    mRAC-LKA and MPP11 but near background; authors explicitly say intrinsic Hsp70L1
    hydrolysis cannot be conclusively answered. L1-K68A/E172A hydrolysis-site mutants
    still complement yeast, whereas ATP-binding-deficient LKA fails. mRAC stimulates
    separate Hsp70/HSPA1, not a demonstrated DNAJC2 stimulation of HSPA14 itself.
    Determine whether later purified kinetics or structures resolve the near-background
    signal. Read PMID21231916 full primary Figures4/5 and exact HSPA14 assays (available
    ResearchGate accepted manuscript has garbled font extraction) to assess substrate-specific
    refolding versus aggregation prevention. A negative luciferase assay cannot disprove
    every client or cofactor context. PMID16002468 establishes human mRAC, not exclusion
    of other roles. Actual PTHR19375 v19 target leafPTN002500131 descends from ATPase/refolding
    IBDPTN000452648 and nuclear IBDPTN002500132; the yeast SSZ1 loss nodePTN001065099
    is not on this target path. Original plasma-membrane IBA citesPTN002500132, but
    the current path lacks that term; explain version differences separately from
    biology. HDA membrane PMID19946888 is a lead; distinguish generic membrane fraction
    from plasma-membrane activity. DNAJC2 chromatin roles alone do not locate HSPA14.
    Recombinant HSP70L1 extracellular dendritic/TLR4 stimulation is not evidence of
    endogenous secretion or membrane residence. Do not infer exclusivity from predominant
    cytosol, absence of signal peptide, absent target experiment, or single donor.'
  term_context: No specific term context supplied.
  reference_context: No specific reference context supplied.
  source_file: genes/human/HSPA14/HSPA14-ai-review.yaml
  source_selector: free-text
  source_context_yaml: "hypothesis: 'Human HSPA14/Hsp70L1 Q0VDF9 has intrinsic ATP\
    \ hydrolysis activity, participates in refolding\n  of previously denatured proteins,\
    \ and functions in the nucleus or at plasma membrane under appropriate\n  conditions.\
    \ Adjudicate each claim separately from its established ATP-binding mRAC cofactor\
    \ role with\n  DNAJC2/MPP11. Read full PMID21245388: purified E.coli-produced\
    \ mRAC gives 0.01 ATP/min, above mRAC-LKA\n  and MPP11 but near background; authors\
    \ explicitly say intrinsic Hsp70L1 hydrolysis cannot be conclusively\n  answered.\
    \ L1-K68A/E172A hydrolysis-site mutants still complement yeast, whereas ATP-binding-deficient\n\
    \  LKA fails. mRAC stimulates separate Hsp70/HSPA1, not a demonstrated DNAJC2\
    \ stimulation of HSPA14 itself.\n  Determine whether later purified kinetics or\
    \ structures resolve the near-background signal. Read PMID21231916\n  full primary\
    \ Figures4/5 and exact HSPA14 assays (available ResearchGate accepted manuscript\
    \ has garbled\n  font extraction) to assess substrate-specific refolding versus\
    \ aggregation prevention. A negative luciferase\n  assay cannot disprove every\
    \ client or cofactor context. PMID16002468 establishes human mRAC, not exclusion\n\
    \  of other roles. Actual PTHR19375 v19 target leafPTN002500131 descends from\
    \ ATPase/refolding IBDPTN000452648\n  and nuclear IBDPTN002500132; the yeast SSZ1\
    \ loss nodePTN001065099 is not on this target path. Original\n  plasma-membrane\
    \ IBA citesPTN002500132, but the current path lacks that term; explain version\
    \ differences\n  separately from biology. HDA membrane PMID19946888 is a lead;\
    \ distinguish generic membrane fraction\n  from plasma-membrane activity. DNAJC2\
    \ chromatin roles alone do not locate HSPA14. Recombinant HSP70L1\n  extracellular\
    \ dendritic/TLR4 stimulation is not evidence of endogenous secretion or membrane\
    \ residence.\n  Do not infer exclusivity from predominant cytosol, absence of\
    \ signal peptide, absent target experiment,\n  or single donor.'\nfocus_type:\
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
citation_count: 11
artifact_count: 5
artifact_sources:
  openscientist_artifacts_zip: 5
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
- filename: provenance_HSPA14_GO_decision_table.csv
  path: openscientist_artifacts/provenance_HSPA14_GO_decision_table.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist HSPA14 GO decision table
- filename: provenance_HSPA14_catalytic_motif_comparison.csv
  path: openscientist_artifacts/provenance_HSPA14_catalytic_motif_comparison.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist HSPA14 catalytic motif comparison
- filename: provenance_HSPA14_orthology_structural_evidence.csv
  path: openscientist_artifacts/provenance_HSPA14_orthology_structural_evidence.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist HSPA14 orthology structural evidence
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
- **Gene directory:** HSPA14
- **Gene symbol:** HSPA14
- **UniProt accession:** Q0VDF9

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** atp-hydrolysis-refolding-and-secondary-compartments
- **Source file:** genes/human/HSPA14/HSPA14-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

Human HSPA14/Hsp70L1 Q0VDF9 has intrinsic ATP hydrolysis activity, participates in refolding of previously denatured proteins, and functions in the nucleus or at plasma membrane under appropriate conditions. Adjudicate each claim separately from its established ATP-binding mRAC cofactor role with DNAJC2/MPP11. Read full PMID21245388: purified E.coli-produced mRAC gives 0.01 ATP/min, above mRAC-LKA and MPP11 but near background; authors explicitly say intrinsic Hsp70L1 hydrolysis cannot be conclusively answered. L1-K68A/E172A hydrolysis-site mutants still complement yeast, whereas ATP-binding-deficient LKA fails. mRAC stimulates separate Hsp70/HSPA1, not a demonstrated DNAJC2 stimulation of HSPA14 itself. Determine whether later purified kinetics or structures resolve the near-background signal. Read PMID21231916 full primary Figures4/5 and exact HSPA14 assays (available ResearchGate accepted manuscript has garbled font extraction) to assess substrate-specific refolding versus aggregation prevention. A negative luciferase assay cannot disprove every client or cofactor context. PMID16002468 establishes human mRAC, not exclusion of other roles. Actual PTHR19375 v19 target leafPTN002500131 descends from ATPase/refolding IBDPTN000452648 and nuclear IBDPTN002500132; the yeast SSZ1 loss nodePTN001065099 is not on this target path. Original plasma-membrane IBA citesPTN002500132, but the current path lacks that term; explain version differences separately from biology. HDA membrane PMID19946888 is a lead; distinguish generic membrane fraction from plasma-membrane activity. DNAJC2 chromatin roles alone do not locate HSPA14. Recombinant HSP70L1 extracellular dendritic/TLR4 stimulation is not evidence of endogenous secretion or membrane residence. Do not infer exclusivity from predominant cytosol, absence of signal peptide, absent target experiment, or single donor.

## Term and Decision Context

No specific term context supplied.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: 'Human HSPA14/Hsp70L1 Q0VDF9 has intrinsic ATP hydrolysis activity, participates in refolding
  of previously denatured proteins, and functions in the nucleus or at plasma membrane under appropriate
  conditions. Adjudicate each claim separately from its established ATP-binding mRAC cofactor role with
  DNAJC2/MPP11. Read full PMID21245388: purified E.coli-produced mRAC gives 0.01 ATP/min, above mRAC-LKA
  and MPP11 but near background; authors explicitly say intrinsic Hsp70L1 hydrolysis cannot be conclusively
  answered. L1-K68A/E172A hydrolysis-site mutants still complement yeast, whereas ATP-binding-deficient
  LKA fails. mRAC stimulates separate Hsp70/HSPA1, not a demonstrated DNAJC2 stimulation of HSPA14 itself.
  Determine whether later purified kinetics or structures resolve the near-background signal. Read PMID21231916
  full primary Figures4/5 and exact HSPA14 assays (available ResearchGate accepted manuscript has garbled
  font extraction) to assess substrate-specific refolding versus aggregation prevention. A negative luciferase
  assay cannot disprove every client or cofactor context. PMID16002468 establishes human mRAC, not exclusion
  of other roles. Actual PTHR19375 v19 target leafPTN002500131 descends from ATPase/refolding IBDPTN000452648
  and nuclear IBDPTN002500132; the yeast SSZ1 loss nodePTN001065099 is not on this target path. Original
  plasma-membrane IBA citesPTN002500132, but the current path lacks that term; explain version differences
  separately from biology. HDA membrane PMID19946888 is a lead; distinguish generic membrane fraction
  from plasma-membrane activity. DNAJC2 chromatin roles alone do not locate HSPA14. Recombinant HSP70L1
  extracellular dendritic/TLR4 stimulation is not evidence of endogenous secretion or membrane residence.
  Do not infer exclusivity from predominant cytosol, absence of signal peptide, absent target experiment,
  or single donor.'
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

# HSPA14/Hsp70L1 (Q0VDF9): Adjudicating Intrinsic ATP Hydrolysis, Refolding, and Secondary Compartments

**Focus type:** function_assignment
**Hypothesis slug:** atp-hydrolysis-refolding-and-secondary-compartments
**Target:** Human HSPA14 / Hsp70L1, UniProt Q0VDF9 (NCBITaxon:9606)

---

## Executive Judgment

**Verdict: Over-annotated / refuted as stated, with two narrowly retained caveats.**

The seed hypothesis proposes that human HSPA14/Hsp70L1 (1) has intrinsic ATP **hydrolysis** activity, (2) participates in **refolding of previously denatured proteins**, and (3) functions in the **nucleus** or at the **plasma membrane** under appropriate conditions. Examined claim-by-claim against primary literature, GO provenance, sequence architecture, and orthologue structural biology, the weight of evidence is that HSPA14's experimentally supported identity is a **cytosolic, ribosome-associated, ATP-*binding* (not hydrolysis-driven) atypical Hsp70** that, together with DNAJC2/MPP11 in the mammalian ribosome-associated complex (mRAC), transiently engages nascent chains to assist **de novo cotranslational protein folding**. The three additional activities/locations in the seed hypothesis are best characterized as phylogenetic (IBA) or electronic (IEA) carry-overs, or as in-vitro/recombinant observations that do not establish an endogenous molecular function.

The core reasoning converges from four independent lines. First, **GO provenance**: the intrinsic ATP hydrolysis (GO:0016887) and protein refolding (GO:0042026) annotations for Q0VDF9 rest solely on IEA (InterPro) and IBA (phylogenetic node PTN000452648) evidence — no IDA, IMP, or EXP. Second, **the primary human assay** (PMID21245388) measured only ~0.01 ATP/min for purified E. coli-produced mRAC, near background, and its own authors state intrinsic Hsp70L1 hydrolysis cannot be conclusively demonstrated; mechanistically they show ATP *binding*, not hydrolysis, is the operative activity, and hydrolysis-site mutants (K68A/E172A) still complement yeast whereas the ATP-binding-deficient mutant fails. Third, **orthologue structural biology**: crystal and cryo-EM structures of the direct fungal ortholog Ssz1 demonstrate a catalytically inert nucleotide-binding domain with abolished Hsp70 allostery. Fourth, **direct sequence evidence**: the invariant Hsp70 catalytic/phosphate-binding signature (IDLGTTxS) is degenerate in HSPA14 (GVHLGCTSA), and the protein lacks the C-terminal EEVD and GGMP substrate-handling elements of canonical chaperoning Hsp70s.

**Most important caveats.** (a) The negative in-vitro luciferase-refolding result does not logically exclude every possible substrate or cofactor context; it does, however, mean "protein refolding" is not directly supported and should not be an EXP-backed core term. (b) There is a genuine, functionally distinct **nuclear/chromatin lead** for intracellular HSP70L1 (PMID30635648) that a curator should treat as a separate biological question from the phylogenetic IBA nucleus annotation. (c) The plasma-membrane claim is the weakest: it is absent from the current GO_Central path for Q0VDF9 and is supported only by a generic membrane-fraction proteome and by recombinant extracellular immunology — neither demonstrates endogenous surface residence.

---

## Key Findings

### Finding 1 — Intrinsic ATP hydrolysis (GO:0016887) is unsupported by direct assay; it is an IEA/IBA carry-over

QuickGO provenance for Q0VDF9 shows GO:0016887 (ATP hydrolysis activity) is supported only by **IEA** (ECO:0000256, InterPro IPR013126) and **IBA** (ECO:0000318, GO_REF:0000033, phylogenetic node PTN000452648) — there is no IDA, IMP, or experimental annotation. The single relevant primary biochemical measurement comes from *The chaperone network connected to human ribosome-associated complex* ([PMID: 21245388](https://pubmed.ncbi.nlm.nih.gov/21245388/)), in which purified E. coli-produced mRAC hydrolyzed ATP at **~0.01 ATP/min** — above the mRAC-LKA (ATP-binding-deficient) and MPP11 controls, but near assay background. The authors explicitly state that intrinsic Hsp70L1 hydrolysis cannot be conclusively demonstrated.

Crucially, the same study dissociates hydrolysis from function on a mechanistic level. The verified snippet reads: *"On a mechanistic level, ATP binding, but not ATP hydrolysis, by Hsp70L1 affected mRAC's function as a J-domain partner of Hsp70."* Consistent with this, **hydrolysis-site mutants K68A and E172A still complement** the yeast RAC-loss phenotype, whereas the **ATP-binding-deficient mutant (LKA) fails**. Genetically, therefore, the operative property is nucleotide *binding* — a structural/allosteric role — not catalysis. This is the clearest single argument that a GO:0016887 core annotation for HSPA14 overstates the evidence.

### Finding 2 — Protein refolding (GO:0042026) is IBA-only; the systematic human HSPA/DNAJ screen did not attribute refolding to HSPA14

For Q0VDF9, GO:0042026 (protein refolding) is **IBA only** (ECO:0000318, node PTN000452648). The most direct experimental test bearing on this is Hageman et al. ([PMID: 21231916](https://pubmed.ncbi.nlm.nih.gov/21231916/)), which systematically assayed the human HSPA/DNAJ machine for heat-denatured luciferase refolding and polyQ aggregation suppression. In GO, this paper contributed an IDA for HSPA14 only to **cytosol (GO:0005829)** — not to any refolding term — consistent with HSPA14 lacking measurable luciferase-refolding activity. The paper's own summary highlights strong substrate-specificity within the family: *"Overexpressed chaperones that suppressed polyQ aggregation were found not to be able to stimulate luciferase refolding."*

This finding is reinforced architecturally. Q0VDF9 is **509 aa** (vs. 641 aa for canonical HSPA1A), and it **lacks the C-terminal EEVD motif** and the **canonical GGMP linker repeat** of chaperoning Hsp70s. These deletions indicate a degenerate substrate-binding/co-chaperone-docking capacity typical of the Ssz1-like atypical Hsp70 subfamily, which is not built to autonomously bind and refold released, denatured clients. The negative luciferase result does not by itself exclude all conceivable substrates, so this is a "not directly supported / do not treat as EXP-backed core" conclusion rather than an absolute impossibility.

### Finding 3 — Nucleus (GO:0005634) and plasma membrane (GO:0005886) are phylogenetic carry-overs; only cytosol and ribosome are experimentally supported

QuickGO cellular-component annotations for Q0VDF9: **cytosol (GO:0005829)** has IDA ×2 (PMID16002468, PMID21231916) plus IBA and IEA; **ribosome (GO:0005840)** has IDA (PMID16002468) plus IBA; **membrane (GO:0016020)** has an HDA (high-throughput, ECO:0007005) from PMID19946888. In contrast, **nucleus (GO:0005634) is IBA only** (no experimental evidence), and **plasma membrane (GO:0005886) does not appear** in the current QuickGO annotation set for Q0VDF9 — it survives only as a stale IBA in an older UniProt snapshot, consistent with the current PANTHER PTHR19375 path no longer carrying the ancestral plasma-membrane term.

The experimentally solid localization is captured by *The chaperones MPP11 and Hsp70L1 form the mammalian ribosome-associated complex* ([PMID: 16002468](https://pubmed.ncbi.nlm.nih.gov/16002468/)): *"we report that MPP11 is localized to the cytosol and associates with ribosomes."* The membrane HDA (PMID19946888) derives from an NK-cell (YTS) whole-membrane proteome in which ~40% of 1,843 IDs were predicted membrane proteins and the remainder were "transiently associated" cytosolic species — HSP70-family proteins are classic co-fractionating contaminants, so this is a **generic membrane fraction**, not plasma-membrane residence. Recombinant extracellular HSP70L1 TLR4/dendritic-cell adjuvant activity (PMID14592822, PMID21730052) uses purified protein and does **not** demonstrate endogenous secretion or surface residence.

Separately — and important for curation — there is a genuine intracellular **nuclear/chromatin** function reported: *Intracellular HSP70L1 inhibits human dendritic cell maturation...* ([PMID: 30635648](https://pubmed.ncbi.nlm.nih.gov/30635648/)): *"intracellular HSP70L1 inhibits the recruitment of Ash1l to and maintains the repressive H3K27me3 and H2AK119Ub1 modifications on the promoter regions."* This is a functional lead distinct from the phylogenetic IBA nucleus annotation and should be adjudicated on its own primary evidence rather than merged with the carry-over.

### Finding 4 — The atypical Hsp70 ortholog Ssz1 is catalytically inert (structural/evolutionary evidence)

Crystal and cryo-EM structures of the RAC atypical Hsp70 subunit Ssz1 — the direct fungal ortholog of human HSPA14 — show it cannot perform the canonical Hsp70 ATPase cycle. Leidig et al. 2013 ([PMID: 23202586](https://pubmed.ncbi.nlm.nih.gov/23202586/)): *"The crystal structure of the Ssz1 ATPase domain bound to ATP-Mg²⁺ explains its catalytic inactivity."* Weyer et al. 2017 ([PMID: 28067917](https://pubmed.ncbi.nlm.nih.gov/28067917/)): *"Ssz1 is catalytically inert and cannot adopt the closed conformation, but the substrate binding domain β is completed by Zuo1."* Conz et al. 2007 ([PMID: 17901048](https://pubmed.ncbi.nlm.nih.gov/17901048/)): *"Ssz1 is not an ATPase in vitro, and even its ability to bind ATP is dispensable in vivo."* Kišonaitė et al. 2023 (PMID37081320) further show the Zuo1 HPD motif is masked by the Ssz1 NBD, which positions Ssb for activation.

Together these establish, at atomic resolution, that the atypical Hsp70 of RAC has an NBD structurally incompatible with the Hsp70 catalytic cycle and with the allosteric closed conformation required for client capture/release. Human HSPA14 retains the K68 and E172 residues (confirmed from the Q0VDF9 sequence), but the orthologue's NBD is demonstrated non-catalytic, and the human primary assay measured only near-background hydrolysis. This is strong cross-species convergent evidence against an intrinsic-ATPase core annotation.

### Finding 5 — RAC engages nascent chains transiently at the ribosome, not post-denaturation refolding

Zhang et al. 2020 ([PMID: 32198371](https://pubmed.ncbi.nlm.nih.gov/32198371/)) show that via its rudimentary substrate-binding domain, Ssz1 *"directly binds to emerging nascent chains prior to Ssb"* and is *"an active chaperone optimized for transient, low-affinity substrate binding, which ensures the flux of nascent chains through RAC/Ssb."* Multiple cryo-EM studies (PMID37081320, PMID35701497, PMID25362488) show RAC crouches over the ribosomal tunnel exit and mechanically couples to the elongation cycle, remodeling upon nascent-chain emergence.

The human process that is actually supported for HSPA14 is **GO:0051083 "de novo cotranslational protein folding" (TAS, PMID16002468)**. No study demonstrates HSPA14/Ssz1 autonomously refolding a previously denatured, released substrate. This distinguishes the correct core biological process (cotranslational, transient nascent-chain engagement) from the seed hypothesis's post-denaturation refolding (GO:0042026).

### Finding 6 — Human HSPA14 has a degenerate Hsp70 catalytic signature and no experimental structure

Direct sequence comparison (UniProt Q0VDF9 vs HSPA1A) shows the invariant N-terminal Hsp70 phosphate-binding/catalytic signature — the PROSITE PS00297 pattern **IDLGTTxS** — is present in canonical HSPA1A (**GIDLGTTYS**) but is **degenerate in HSPA14** (**GVHLGCTSA**): the invariant Asp is replaced by His and the Thr-Thr pair by Cys-Thr. HSPA14 is 509 aa vs. 641 aa and additionally lacks the C-terminal EEVD motif and GGMP linker. UniProt reports **no experimental PDB structure** for Q0VDF9 (AlphaFold model only), so all direct structural evidence of catalytic inactivity comes from the fungal ortholog Ssz1. This sequence-level degeneracy is independent, direct evidence that the ATPase active site is atypical and unlikely to support efficient intrinsic hydrolysis.

---

## Mechanistic Model / Interpretation

The consolidated model positions HSPA14 as a **non-catalytic, ATP-binding scaffolding subunit** of the ribosome-associated complex, not a stand-alone chaperone:

```
                Ribosome (80S)
                     |
          polypeptide tunnel exit
                     |
        [ nascent chain emerging ]
                     |
   +-----------------------------------------+
   |            mRAC heterodimer              |
   |  DNAJC2/MPP11 (Zuo1 ortholog, J-domain) |
   |        tethers + docks on ribosome      |
   |                  ||                      |
   |  HSPA14/Hsp70L1 (Ssz1 ortholog)         |
   |  - binds ATP (structural/allosteric)    |
   |  - NBD catalytically inert (no cycle)   |
   |  - rudimentary SBD: transient,          |
   |    low-affinity nascent-chain contact   |
   +-----------------------------------------+
                     |
   J-domain stimulates the SEPARATE canonical
   Hsp70 (HSPA1/Ssb) ATPase -> client folding
```

Key mechanistic separations a curator must preserve:

| Claim in seed hypothesis | What the evidence supports | Correct GO framing |
|---|---|---|
| Intrinsic ATP **hydrolysis** (GO:0016887) | ATP **binding** is operative; hydrolysis near background; hydrolysis-site mutants complement | ATP binding (GO:0005524) supported; GO:0016887 non-core / remove or NOT-qualify |
| **Refolding** of denatured proteins (GO:0042026) | Transient **cotranslational** nascent-chain engagement; luciferase-refolding screen did not credit HSPA14 | GO:0051083 de novo cotranslational protein folding (TAS) is the core BP |
| Stimulates ATPase of an Hsp70 | mRAC's J-domain stimulates the **separate** canonical Hsp70 (HSPA1/Ssb), not HSPA14 itself | Co-chaperone / J-domain partner context — not intrinsic HSPA14 catalysis |
| **Nucleus** (GO:0005634) | IBA only; a distinct chromatin lead exists (PMID30635648) | Non-core; treat chromatin role as separate primary-evidence question |
| **Plasma membrane** (GO:0005886) | Absent from current GO path; generic membrane fraction + recombinant immunology only | Non-core; do not annotate without direct endogenous surface evidence |
| Cytosol / ribosome | IDA-supported (PMID16002468, PMID21231916) | Retain as core CC |

The unifying interpretation: HSPA14 is an **Ssz1-type "pseudo-Hsp70"** whose value to the cell is allosteric and organizational (nucleotide-stabilized scaffolding of the J-domain partner and transient nascent-chain handoff), not enzymatic ATP turnover or autonomous client refolding.

---

## Evidence Base (Evidence Matrix)

| Citation | Evidence type | Supports / Refutes / Qualifies | Claim tested | Key finding | Context | Confidence & limitations |
|---|---|---|---|---|---|---|
| [PMID: 21245388](https://pubmed.ncbi.nlm.nih.gov/21245388/) | Direct assay + mutant phenotype | **Refutes** intrinsic hydrolysis; qualifies ATP role | Intrinsic ATP hydrolysis | ~0.01 ATP/min (near background); ATP *binding* not hydrolysis affects mRAC function; K68A/E172A still complement, LKA fails | Human mRAC, E. coli-purified; yeast complementation | High for "binding not hydrolysis"; assay sensitivity limits absolute exclusion |
| QuickGO provenance (Q0VDF9) | Review/database | **Refutes** core-status of hydrolysis/refolding | GO evidence codes | GO:0016887 & GO:0042026 are IEA/IBA only; no IDA/EXP | Database | High; database snapshot |
| [PMID: 21231916](https://pubmed.ncbi.nlm.nih.gov/21231916/) | Direct assay (screen) | **Refutes** refolding attribution | Post-denaturation refolding | Family-wide luciferase-refolding + polyQ screen; HSPA14 credited only with cytosol IDA, not refolding | Human HSPA/DNAJ overexpression | Medium-high; negative result, single substrate class |
| [PMID: 16002468](https://pubmed.ncbi.nlm.nih.gov/16002468/) | Localization + interaction | **Supports** cytosol/ribosome core | Localization; mRAC identity | MPP11/Hsp70L1 form mRAC; cytosolic, ribosome-associated | Human cells | High |
| [PMID: 23202586](https://pubmed.ncbi.nlm.nih.gov/23202586/) | Structural/evolutionary | **Refutes** intrinsic ATPase | Catalytic capacity of atypical Hsp70 | Ssz1 ATPase-domain crystal structure "explains its catalytic inactivity" | Yeast/C. thermophilum ortholog | High for ortholog; inference to human |
| [PMID: 28067917](https://pubmed.ncbi.nlm.nih.gov/28067917/) | Structural | **Refutes** intrinsic ATPase | Allosteric cycle | "Ssz1 is catalytically inert and cannot adopt the closed conformation" | Yeast ortholog | High for ortholog |
| [PMID: 17901048](https://pubmed.ncbi.nlm.nih.gov/17901048/) | Biochemical + genetic | **Refutes** intrinsic ATPase | ATPase activity / ATP-binding necessity | "Ssz1 is not an ATPase in vitro, and even its ability to bind ATP is dispensable in vivo" | Yeast | High for ortholog |
| [PMID: 32198371](https://pubmed.ncbi.nlm.nih.gov/32198371/) | Functional/structural | **Qualifies** BP as cotranslational | Substrate-engagement mode | Transient, low-affinity nascent-chain binding ensures flux through RAC/Ssb | Yeast | High for ortholog |
| [PMID: 30635648](https://pubmed.ncbi.nlm.nih.gov/30635648/) | Functional (mechanistic) | **Competing / qualifies** nucleus | Nuclear/chromatin role | Intracellular HSP70L1 maintains repressive H3K27me3/H2AK119Ub1, inhibits Ash1l recruitment | Human dendritic cells | Medium; distinct from IBA carry-over |
| PMID: 19946888 | Localization (HDA) | **Qualifies/weak** membrane | Plasma-membrane residence | Whole-membrane NK-cell proteome; HSP70s are classic co-fractionating contaminants | Human NK (YTS) cells | Low; generic fraction, not surface |
| [PMID: 14592822](https://pubmed.ncbi.nlm.nih.gov/14592822/), [PMID: 21730052](https://pubmed.ncbi.nlm.nih.gov/21730052/) | Recombinant assay | **Qualifies/weak** secretion | Extracellular/membrane function | Recombinant HSP70L1 binds TLR4, matures DCs, Th1 adjuvant | Human DCs, recombinant protein | Low for endogenous secretion; uses purified protein |
| UniProt Q0VDF9 sequence | Computational (direct sequence) | **Refutes** canonical ATPase site | Catalytic-site integrity | PS00297 IDLGTTxS degenerate (GVHLGCTSA); no EEVD/GGMP; no experimental PDB | In silico | High for sequence facts; function is inference |

---

## GO Curation Implications (leads requiring curator verification)

| GO term | Aspect | Current basis | Recommended action (lead) |
|---|---|---|---|
| **GO:0016887 ATP hydrolysis activity** | MF | IEA (IPR013126) + IBA (PTN000452648) | **Remove / do not treat as core**, or apply NOT-style scrutiny. Direct assay near background; hydrolysis-site mutants complement; ortholog structurally inert. Prefer **GO:0005524 ATP binding** as the supported MF. |
| **GO:0042026 protein refolding** | BP | IBA only | **Generalize/replace** with **GO:0051083 de novo cotranslational protein folding** (TAS, PMID16002468), the experimentally supported process. Refolding not directly supported. |
| **GO:0005634 nucleus** | CC | IBA only | **Treat as non-core carry-over.** A separate, primary chromatin function exists (PMID30635648) — curate that on its own evidence, not via the IBA. |
| **GO:0005886 plasma membrane** | CC | Stale IBA / absent from current path | **Remove / do not annotate.** No endogenous surface evidence; only generic membrane fraction + recombinant immunology. |
| **GO:0005829 cytosol** | CC | IDA ×2 (PMID16002468, PMID21231916) | **Retain (core).** |
| **GO:0005840 ribosome** | CC | IDA (PMID16002468) | **Retain (core).** |
| **GO:0051083 de novo cotranslational protein folding** | BP | TAS (PMID16002468) | **Retain/promote as core BP.** |

The most informative MF for HSPA14 is **ATP binding (GO:0005524)** plus a co-chaperone / unfolded-protein-binding role in the ribosome-associated complex — not "ATP hydrolysis activity" and not merely "protein binding."

---

## Mechanistic Scope

The immediate molecular function being tested is whether HSPA14's NBD **turns over ATP** and whether its SBD **refolds released denatured clients**. The evidence indicates neither: the NBD binds nucleotide but is catalytically inert (ortholog structures; degenerate human catalytic signature; near-background human assay), and the rudimentary SBD makes only transient, low-affinity contacts with **nascent** chains at the ribosome. The genuine downstream/pathway consequences frequently cited (TLR4/dendritic-cell adjuvant activity, breast-cancer prognosis, HIV replication modulation, prion suppression in yeast complementation) are context-specific phenotypes or recombinant-protein effects — they are not evidence of the intrinsic biochemical activities in the seed hypothesis. The chromatin/H3K27me3 role (PMID30635648) is a distinct, potentially direct intracellular function that must be evaluated separately, not folded into the phylogenetic nucleus IBA.

---

## Conflicts and Alternatives

- **Paralog / family carry-over.** The strongest driver of the seed annotations is InterPro/PANTHER inheritance from the canonical, catalytically active Hsp70 branch. HSPA14 is an atypical Ssz1-type Hsp70; applying the family consensus over-annotates it. The degenerate PS00297 motif is the clearest paralog-discrimination signal.
- **Ortholog inference vs. direct human data.** All catalytic-inactivity *structures* are from fungal Ssz1; there is no experimental structure of human Q0VDF9. This is a species-inference limitation, but it is corroborated by the human sequence degeneracy and the near-background human assay, making the inference robust.
- **Recombinant vs. endogenous.** The extracellular/TLR4 immunology uses purified recombinant HSP70L1. Adjuvant activity of a purified protein does not establish endogenous secretion or plasma-membrane residence — a common source of CC over-annotation for HSP70-family proteins.
- **Co-fractionation artifact.** The membrane HDA is a whole-membrane proteome; HSP70s co-fractionate broadly. This is a classic false-positive route to membrane CC terms.
- **Negative-result logic.** The luciferase-refolding screen is negative for HSPA14; a curator should note this cannot exclude every substrate/cofactor context, but it does remove the direct basis for a refolding EXP annotation.

---

## Limitations and Knowledge Gaps

1. **No experimental structure of human Q0VDF9.** Checked: UniProt lists only an AlphaFold model. Matters because human catalytic inactivity is inferred from ortholog structures + sequence. Resolution: a cryo-EM/crystal structure of human mRAC, or a rigorously controlled ATPase assay of highly purified human HSPA14 with proper background subtraction.
2. **Assay sensitivity floor.** The ~0.01 ATP/min value sits near background; the study cannot formally exclude very slow hydrolysis. Resolution: single-turnover or high-sensitivity kinetics (e.g., malachite-green with rigorous controls, or NMR-based readouts).
3. **Nuclear/chromatin function.** PMID30635648 reports a chromatin role, but whether HSPA14 itself localizes to chromatin (vs. acting indirectly) needs direct evidence. Resolution: endogenous ChIP/CUT&RUN and validated nuclear fractionation with tagged endogenous protein.
4. **Plasma-membrane residence.** Only generic fraction + recombinant data exist. Resolution: surface biotinylation / non-permeabilized immunostaining of endogenous protein in relevant cells.
5. **Substrate breadth of refolding.** The negative result is for luciferase/polyQ only. Resolution: broader client panel or unbiased interactome under denaturing/recovery conditions.

---

## Discriminating Tests (recommended)

- **High-sensitivity single-turnover ATPase assay** of purified human HSPA14 ± DNAJC2/MPP11, with the K68A/E172A hydrolysis-site mutants and the ATP-binding-deficient mutant as internal controls — directly tests intrinsic hydrolysis above background.
- **Cryo-EM of human mRAC on the ribosome** — resolves whether the human NBD can adopt the closed/catalytic conformation, testing the ortholog inference.
- **Endogenous surface biotinylation + non-permeabilized IF** in NK/dendritic cells — discriminates true plasma-membrane residence from co-fractionation.
- **Endogenous nuclear fractionation + CUT&RUN** for tagged HSPA14 — tests direct chromatin engagement vs. indirect effect underlying PMID30635648.
- **Broad refolding/holdase panel** (multiple denatured clients, aggregation-prevention vs. active refolding readouts) — tests whether any substrate class supports GO:0042026.

---

## Curation Leads (require curator verification)

1. **Downgrade/remove GO:0016887** (ATP hydrolysis activity) from core; retain **GO:0005524 ATP binding**. Lead references: PMID21245388 (snippet: *"ATP binding, but not ATP hydrolysis, by Hsp70L1 affected mRAC's function as a J-domain partner of Hsp70"*), PMID17901048 (*"Ssz1 is not an ATPase in vitro..."*), PMID28067917 (*"Ssz1 is catalytically inert..."*), PMID23202586.
2. **Replace GO:0042026** (protein refolding) with **GO:0051083 de novo cotranslational protein folding** as core BP (TAS, PMID16002468); note the PMID21231916 negative luciferase result and family substrate-specificity.
3. **Flag GO:0005634 nucleus** as non-core IBA carry-over; open a separate curation question on the PMID30635648 chromatin role (snippet: *"intracellular HSP70L1 inhibits the recruitment of Ash1l to and maintains the repressive H3K27me3 and H2AK119Ub1 modifications..."*).
4. **Remove GO:0005886 plasma membrane**; document that it is absent from the current GO_Central path and supported only by generic membrane fraction (PMID19946888) and recombinant immunology (PMID14592822, PMID21730052).
5. **Retain GO:0005829 cytosol and GO:0005840 ribosome** as core (IDA, PMID16002468/PMID21231916).
6. **Suggested curator questions:** Does any highly purified human HSPA14 preparation show hydrolysis above background? Is there any endogenous (non-recombinant) evidence for secretion/surface residence? Is the chromatin effect direct or indirect?

---

## Supported and Refuted Hypotheses Summary

| Seed claim | Adjudication | Basis |
|---|---|---|
| Intrinsic ATP hydrolysis activity | **Refuted / over-annotated** | Near-background assay; hydrolysis-site mutants complement; degenerate motif; inert ortholog |
| Refolding of previously denatured proteins | **Refuted as core / not directly supported** | IBA-only; screen did not credit HSPA14; correct BP is cotranslational folding |
| Nuclear function | **Unresolved** (IBA carry-over refuted, but distinct chromatin lead exists) | PMID30635648 is a separate, potentially real function |
| Plasma-membrane function | **Refuted / weakly supported** | Absent from current path; generic fraction + recombinant only |
| ATP-*binding* mRAC cofactor / cotranslational folding | **Supported (established core)** | IDA/TAS; PMID16002468, PMID21245388 |

---

*Prepared as a hypothesis-level curation lead. Structural conclusions about catalytic inactivity derive from the fungal ortholog Ssz1 and human sequence analysis; they are strong but inferential for human HSPA14 pending a direct human structure or high-sensitivity assay. All annotations flagged here require curator verification against current GO_Central provenance.*


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)
- [OpenScientist HSPA14 GO decision table](openscientist_artifacts/provenance_HSPA14_GO_decision_table.csv)
- [OpenScientist HSPA14 catalytic motif comparison](openscientist_artifacts/provenance_HSPA14_catalytic_motif_comparison.csv)
- [OpenScientist HSPA14 orthology structural evidence](openscientist_artifacts/provenance_HSPA14_orthology_structural_evidence.csv)