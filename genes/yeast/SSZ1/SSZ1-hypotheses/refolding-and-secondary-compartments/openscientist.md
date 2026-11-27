---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-20T22:30:34.814011'
end_time: '2026-09-20T22:51:51.632608'
duration_seconds: 1276.82
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: yeast
  gene: SSZ1
  gene_symbol: SSZ1
  uniprot_accession: P38788
  taxon_id: NCBITaxon:559292
  taxon_label: Saccharomyces cerevisiae
  focus_type: function_assignment
  hypothesis_slug: refolding-and-secondary-compartments
  hypothesis_text: 'Saccharomyces cerevisiae Ssz1 supports protein refolding or localizes
    to the nucleus or plasma membrane. Adjudicate these separately. The existing ATP-hydrolysis
    investigation is available and need not be repeated: ask whether ATPase-inactive
    Ssz1 can contribute to refolding through ATP-independent or partner-assisted mechanisms
    beyond its nascent-chain relay. Inspect current PAINT NOT/IRD GO:0042026 at PTN001065099
    under PTN000452648 and determine whether it establishes a relevant loss/generalization
    for this target. Evaluate positive or negative localization assays without assuming
    the ribosome-associated pool is exclusive.'
  term_context: No specific term context supplied.
  reference_context: No specific reference context supplied.
  source_file: genes/yeast/SSZ1/SSZ1-ai-review.yaml
  source_selector: free-text
  source_context_yaml: "hypothesis: 'Saccharomyces cerevisiae Ssz1 supports protein\
    \ refolding or localizes to the nucleus or plasma\n  membrane. Adjudicate these\
    \ separately. The existing ATP-hydrolysis investigation is available and need\n\
    \  not be repeated: ask whether ATPase-inactive Ssz1 can contribute to refolding\
    \ through ATP-independent\n  or partner-assisted mechanisms beyond its nascent-chain\
    \ relay. Inspect current PAINT NOT/IRD GO:0042026\n  at PTN001065099 under PTN000452648\
    \ and determine whether it establishes a relevant loss/generalization\n  for this\
    \ target. Evaluate positive or negative localization assays without assuming the\
    \ ribosome-associated\n  pool is exclusive.'\nfocus_type: function_assignment\n\
    context: []\nreference_id: []"
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
citation_count: 8
artifact_count: 4
artifact_sources:
  openscientist_artifacts_zip: 4
artifacts:
- filename: artifact_GO_decision_table.csv
  path: openscientist_artifacts/artifact_GO_decision_table.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist artifact GO decision table
- filename: artifact_P38788_live_GO_annotations.csv
  path: openscientist_artifacts/artifact_P38788_live_GO_annotations.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist artifact P38788 live GO annotations
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
- **Gene directory:** SSZ1
- **Gene symbol:** SSZ1
- **UniProt accession:** P38788

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** refolding-and-secondary-compartments
- **Source file:** genes/yeast/SSZ1/SSZ1-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

Saccharomyces cerevisiae Ssz1 supports protein refolding or localizes to the nucleus or plasma membrane. Adjudicate these separately. The existing ATP-hydrolysis investigation is available and need not be repeated: ask whether ATPase-inactive Ssz1 can contribute to refolding through ATP-independent or partner-assisted mechanisms beyond its nascent-chain relay. Inspect current PAINT NOT/IRD GO:0042026 at PTN001065099 under PTN000452648 and determine whether it establishes a relevant loss/generalization for this target. Evaluate positive or negative localization assays without assuming the ribosome-associated pool is exclusive.

## Term and Decision Context

No specific term context supplied.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: 'Saccharomyces cerevisiae Ssz1 supports protein refolding or localizes to the nucleus or plasma
  membrane. Adjudicate these separately. The existing ATP-hydrolysis investigation is available and need
  not be repeated: ask whether ATPase-inactive Ssz1 can contribute to refolding through ATP-independent
  or partner-assisted mechanisms beyond its nascent-chain relay. Inspect current PAINT NOT/IRD GO:0042026
  at PTN001065099 under PTN000452648 and determine whether it establishes a relevant loss/generalization
  for this target. Evaluate positive or negative localization assays without assuming the ribosome-associated
  pool is exclusive.'
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

# AIGR Gene Hypothesis Deep Research — *Saccharomyces cerevisiae* SSZ1 (P38788)

**Focus:** function_assignment · **Hypothesis slug:** refolding-and-secondary-compartments
**Source:** `genes/yeast/SSZ1/SSZ1-ai-review.yaml` (free-text)
**Gene:** SSZ1 / PDR13 (Ribosome-associated complex subunit Ssz1) · **UniProt:** P38788 · **PANTHER:** PTHR19375, subfamily SF539

---

## Summary

The seed hypothesis proposes three distinct claims that must be adjudicated separately: (1) that Ssz1 supports **protein refolding**, possibly via ATP-independent or partner-assisted mechanisms; (2) that Ssz1 localizes to the **nucleus**; and (3) that Ssz1 localizes to the **plasma membrane**. On the primary biology, all three fail — but for different reasons and with different current annotation states.

**Protein refolding (GO:0042026) is not a genuine molecular function of Ssz1.** Ssz1 is a well-characterized non-canonical Hsp70 that lacks the biochemical machinery required for the canonical refolding cycle: it is not an ATPase in vitro, its ATP-binding capacity is dispensable in vivo, and its peptide-substrate binding is not essential ([PMID: 17901048](https://pubmed.ncbi.nlm.nih.gov/17901048/)). Its only measurable substrate interaction is transient, low-affinity, and dedicated to relaying nascent chains through the Ribosome-Associated Complex (RAC) to the folding Hsp70 Ssb — not to holding or refolding denatured/misfolded proteins ([PMID: 32198371](https://pubmed.ncbi.nlm.nih.gov/32198371/)). The seed's specific question — whether ATPase-inactive Ssz1 could refold clients through ATP-independent or partner-assisted routes — is answered in the negative: Ssz1's partner-assisted role is to *activate Ssb's* ATPase and orient nascent chains, not to fold clients itself. The live GO record shows GO:0042026 present as a **positive IBA** propagated from the canonical-Hsp70 ancestor **PTN000452648**, with **no NOT/IRD deployed anywhere** in the family (0 hits family-wide). The seed's proposed IRD at **PTN001065099** is biologically justified (that node is confirmed ancestral to Ssz1), but it is **not currently in effect**, so the positive IBA reaches Ssz1 unobstructed.

**On localization,** the **plasma membrane (GO:0005886)** annotation has *already been removed* from the live GO_Central set (it lingers only in a lagging UniProt cross-reference snapshot), so no new action is needed there. The **nucleus (GO:0005634)** annotation persists as a live IBA over-annotation propagated from canonical cytosolic Hsp70 paralogs (Ssa1–4, human HSPA) that genuinely shuttle to the nucleus, whereas Ssz1 is a stably ribosome-associated cytosolic chaperone whose only experimentally supported localization is **cytoplasm/cytosol (GO:0005737, IDA)**. The most curation-relevant actions are therefore: (a) apply the IRD/NOT for refolding at PTN001065099 or otherwise block/remove the refolding IBA, and (b) remove the nucleus IBA over-annotation. **Overall verdict: refuted (biology) / over-annotated (annotations), with the plasma-membrane component already resolved.**

---

## Executive Judgment

**Verdict: Refuted (biology) / Over-annotated (annotations); plasma-membrane component already resolved.**

Each of the three seed claims is adjudicated separately below:

- **Protein refolding (GO:0042026): REFUTED as a direct Ssz1 function; the current positive IBA is over-annotation.** Mechanistically impossible via the canonical route (no ATPase; ATP-binding dispensable) and unsupported by any experimental annotation; Ssz1's substrate binding is transient/low-affinity relay, not refolding.
- **Nucleus (GO:0005634): OVER-ANNOTATED.** Live IBA propagated from canonical Hsp70 paralogs; no experimental support; Ssz1's extraribosomal Pdr1-activation role acts posttranslationally and does not require stable nuclear residence.
- **Plasma membrane (GO:0005886): ALREADY RESOLVED.** Absent from live GO_Central; survives only in the lagging UniProt xref snapshot.

**Most important caveats:** This adjudication rests on live public GO/PANTHER/QuickGO state plus primary literature; it does not include the withheld local bioinformatics analyses. The refolding refutation is a mechanistic-plus-annotation judgment (absence of mechanism + absence of experimental evidence), not a dedicated null experiment. The seed's proposed IRD/NOT correction is topologically valid but not currently deployed.

---

## Key Findings

### F001 — Protein refolding (GO:0042026) is not experimentally supported; the positive IBA is over-annotation

The GO term GO:0042026 "protein refolding" on P38788 carries the evidence code **IBA only** (phylogenetic inference; ECO:0000318, GO_REF:0000033, assigned by GO_Central). There is no IDA, IMP, or other experimental (EXP-class) evidence anywhere in the record supporting Ssz1 as a refoldase.

The primary literature explains *why* this is mechanistically expected. Conz et al. (2007) directly demonstrated that "**Ssz1 is not an ATPase in vitro, and even its ability to bind ATP is dispensable in vivo**" ([PMID: 17901048](https://pubmed.ncbi.nlm.nih.gov/17901048/)). Canonical Hsp70-driven refolding is an ATP-hydrolysis-powered clamp-and-release cycle; an Hsp70 that neither hydrolyzes ATP nor requires ATP binding cannot execute that cycle. Furthermore, Zhang et al. (2020) showed that "**the combined data indicate that Ssz1 is an active chaperone optimized for transient, low-affinity substrate binding, which ensures the flux of nascent chains through RAC/Ssb**" ([PMID: 32198371](https://pubmed.ncbi.nlm.nih.gov/32198371/)). Transient, low-affinity binding is the opposite of the stable "holdase" grip needed to sequester and refold a denatured client. Together, the two mechanistic requirements for canonical refolding — an ATPase cycle and stable substrate holding — are both absent in Ssz1. The seed's question about **ATP-independent or partner-assisted refolding** is thereby directly addressed: Ssz1's partner-assisted contribution is to stimulate Ssb (via Zuo1's J-domain) and to relay substrate, not to refold clients itself.

### F002 — PANTHER PTN001065099 is genuinely ancestral to SSZ1, so an IRD there would validly block refolding propagation

A programmatic trace of PANTHER tree **PTHR19375 (release 19)** places SSZ1/P38788 (subfamily SF539) on a lineage passing through **PTN000452648** (LUCA-level Hsp70 ancestor, SF184) → … → **PTN001065099** (Fungi node, SF395) → PTN002321669 (Dikarya divergence, SF539) → … → P38788. Both nodes cited in the seed are confirmed ancestors of Ssz1 (membership check: PTN001065099 ∈ ancestor set = True; PTN000452648 ∈ ancestor set = True). Consequently, a PAINT **NOT/IRD (Inferred from Rapid Divergence)** for GO:0042026 placed at PTN001065099 *would* propagate a loss-of-ancestral-function down to the SSZ1 clade — i.e., the seed's proposed mechanism for correcting the annotation is topologically valid.

### F004 — Live GO state: refolding is an un-blocked positive IBA from PTN000452648; no NOT/IRD is currently deployed

QuickGO (EBI) for P38788 returns 26 annotations. GO:0042026 "protein refolding" appears as a **positive IBA** (qualifier `involved_in`, ECO:0000318, GO_REF:0000033, assigned by GO_Central), whose `withFrom` seeds are canonical Hsp70 refoldases propagated from ancestral node **PTN000452648** (including SGD S000000004 = SSA1, plus human HSPA members P0DMV8/P0DMV9/P11142/P17066/P34931 and SGD S000003806). A family-wide QuickGO query for GO:0042026 with `qualifier=NOT` returns **0 hits across all species** — so no NOT/IRD loss for protein refolding is deployed anywhere, including at PTN001065099. This is the crux for the curator: the biology says the term should be blocked at the Fungi node, PANTHER topology confirms a block there would reach Ssz1, but the block does not currently exist, so the term flows through unobstructed.

### F003 & F005 — Nucleus and plasma-membrane annotations are phylogenetic-only over-annotations; plasma membrane is already removed

For P38788, GO:0005634 "nucleus" and GO:0005886 "plasma membrane" carry **IBA:GO_Central only**. The only experimentally supported localization is cytoplasm/cytosol: **GO:0005737 cytoplasm IDA:SGD**, and the UniProt curated Subcellular Location = Cytoplasm. These CC terms are propagated at the PTHR19375 family GO-slim level as a carry-over from canonical cytosolic Hsp70s (Ssa1–4, human HSPA) that genuinely shuttle to the nucleus and associate with membranes.

Critically, the live state differs from the static UniProt snapshot:

- **Plasma membrane (GO:0005886):** Live QuickGO for P38788 contains **NO** plasma-membrane term — it has already been removed from the current GO_Central set. It survives only in the lagging UniProtKB cross-reference snapshot. **No curation action is needed** beyond noting the xref lag.
- **Nucleus (GO:0005634):** Remains a **live IBA** (qualifier `is_active_in`, GO_REF:0000033), propagated from ancestral node PTN002500132 (which the PANTHER v19 trace places on SSZ1's lineage) with canonical-Hsp70 seeds (SGD S000000004 = SSA1; human HSPA P0DMV8/P0DMV9/P11142; PomBase orthologues). This is a paralog-driven over-annotation and is the localization term that warrants removal.

Ssz1's only well-documented extraribosomal function — posttranslational activation of the transcription factor Pdr1 — does **not** establish stable nuclear residence. Hallstrom & Moye-Rowley showed "**Pdr13p exerts its effect on Pdr1p at a posttranslational step**" ([PMID: 9488429](https://pubmed.ncbi.nlm.nih.gov/9488429/)), and the experimentally supported cytoplasmic localization is documented in Mol Microbiol 2000 ([PMID: 10792726](https://pubmed.ncbi.nlm.nih.gov/10792726/)), where "Hyperactive forms of the Pdr1p transcription factor fail to respond to positive regulation by the hsp70 protein Pdr13p." Acting posttranslationally on a transcription factor is not evidence that Ssz1 itself resides in the nucleus.

### F006 — Ssz1's only experimentally-supported MF interactions are with RAC partner Zuo1, not with refolding clients

Live QuickGO for P38788: all four IPI "protein binding" (GO:0005515) annotations are `withFrom` **P32527 = ZUO1** (PMIDs 11274393, 16429126, 23202586, 37968396); "heat shock protein binding" (GO:0031072, IPI) and "protein-folding chaperone binding" (GO:0051087, IPI) are `withFrom` SGD S000003517 = ZUO1. **No experimental annotation records Ssz1 binding or refolding a denatured/misfolded client.** The direct, experimentally supported chaperone-role annotations are the RAC-context terms **GO:0051083 "de novo cotranslational protein folding"** (IDA/IMP, [PMID: 11274393](https://pubmed.ncbi.nlm.nih.gov/11274393/)) and complex membership GO:0101031. This confirms that the experimentally grounded function of Ssz1 is a *structural/regulatory subunit of RAC that hands nascent chains to Ssb*, not an autonomous refoldase.

---

## Mechanistic Model / Interpretation

Ssz1 is the atypical Hsp70 subunit of the **Ribosome-Associated Complex (RAC)**, an obligate heterodimer with the J-domain protein Zuo1 (Zuotin). RAC docks at the ribosomal polypeptide exit tunnel and functions as a *co-chaperone that activates a third Hsp70, Ssb*, which is the actual nascent-chain-binding folding chaperone. The division of labor is the key to adjudicating this hypothesis:

```
   Nascent chain emerging from ribosome tunnel
                  │
                  ▼
        ┌──────────────────────┐
        │        RAC           │
        │  ┌────────┐  ┌─────┐ │
        │  │ Ssz1   │──│Zuo1 │ │   Ssz1 = atypical Hsp70:
        │  │(non-   │  │(J-  │ │     • NOT an ATPase (PMID 17901048)
        │  │ canon. │  │dom) │ │     • ATP-binding dispensable in vivo
        │  │ Hsp70) │  └──┬──┘ │     • transient/low-affinity binding
        │  └────────┘     │    │       (PMID 32198371)
        └─────────────────┼────┘
                          │ J-domain stimulates
                          ▼
                    ┌──────────┐
                    │   Ssb    │  ← canonical Hsp70; ATP-driven;
                    │ (ATPase) │    actually folds nascent chain
                    └──────────┘
                          │
                          ▼
            Co-translational de novo folding
            (GO:0051083 — the correct BP term)

   Refolding of ALREADY-DENATURED proteins (GO:0042026):
   requires ATP-hydrolysis clamp cycle + stable holding
   → Ssz1 possesses NEITHER → NOT a refoldase
```

The seed's core mechanistic question is whether ATPase-inactive Ssz1 could still refold clients by "ATP-independent or partner-assisted mechanisms beyond its nascent-chain relay." The literature answers directly: Ssz1's partner-assisted role is to help *activate Ssb* and *orient/relay* nascent chains — its transient, low-affinity binding is optimized for **flux**, not for the stable sequestration that refolding demands. Structural studies reinforce this: RAC is held together by a tight Ssz1-SBD–Zuo1 interaction, with Ssz1 positioning Zuo1 to activate Ssb ([PMID: 37081320](https://pubmed.ncbi.nlm.nih.gov/37081320/)); RAC is autoinhibited without a nascent chain and remodels to expose the Zuo1 J-domain to Ssb ([PMID: 35701497](https://pubmed.ncbi.nlm.nih.gov/35701497/)); and Ssb(ATP) heterodimerizes with Ssz1 as the first step of an engagement pathway ([PMID: 34580293](https://pubmed.ncbi.nlm.nih.gov/34580293/)). None of these attribute autonomous client folding to Ssz1.

The **annotation over-reach** arises from PANTHER family PTHR19375 grouping Ssz1 with canonical, ATP-driven, nucleus-shuttling cytosolic Hsp70s. Ancestral GO functions (refolding; nuclear/PM localization) are legitimately inferred for the canonical branch and then propagated by IBA to *all* descendants, including the rapidly diverged, function-specialized Ssz1 subfamily. This is a textbook case where **IRD/NOT annotations at the divergence node** exist precisely to prevent inherited-but-lost functions from leaking onto specialized paralogs.

**Annotation state summary:**

| Term | GO ID | Ontology | Live GO evidence | Experimentally supported? | Recommended action |
|------|-------|----------|------------------|---------------------------|--------------------|
| protein refolding | GO:0042026 | BP | Positive IBA from PTN000452648; no NOT deployed | No (IBA only) | Block via IRD/NOT at PTN001065099, or remove IBA |
| nucleus | GO:0005634 | CC | Live IBA (`is_active_in`) from PTN002500132 | No (IBA only) | Remove (paralog-driven over-annotation) |
| plasma membrane | GO:0005886 | CC | Absent from live QuickGO; only in lagging UniProt xref | No | Already resolved; note xref lag |
| cytoplasm | GO:0005737 | CC | IDA:SGD (PMID:10792726) | **Yes** | Retain |
| de novo cotranslational protein folding | GO:0051083 | BP | IDA/IMP (PMID:11274393) | **Yes** | Retain (this is the correct BP) |
| protein-folding chaperone binding / HSP binding | GO:0051087 / GO:0031072 | MF | IPI withFrom ZUO1 | **Yes** (Zuo1) | Retain |

---

## Evidence Base / Evidence Matrix

| Citation (PMID) | Evidence type | Supports/Refutes/Qualifies | Claim tested | Key finding | Context | Confidence & limitations |
|---|---|---|---|---|---|---|
| [17901048](https://pubmed.ncbi.nlm.nih.gov/17901048/) Conz et al. 2007 | Direct assay + mutant phenotype | **Refutes refolding** | Does Ssz1 have canonical Hsp70 ATPase/ATP-binding required for refolding? | "Ssz1 is not an ATPase in vitro, and even its ability to bind ATP is dispensable in vivo" | *S. cerevisiae*, in vitro + in vivo | High; establishes absence of canonical mechanism |
| [32198371](https://pubmed.ncbi.nlm.nih.gov/32198371/) Zhang et al. 2020 | Direct assay | **Refutes/qualifies refolding** | Nature of Ssz1 substrate binding | "active chaperone optimized for transient, low-affinity substrate binding... ensures the flux of nascent chains through RAC/Ssb" | *S. cerevisiae* RAC | High; shows relay, not holdase/refoldase role |
| [9488429](https://pubmed.ncbi.nlm.nih.gov/9488429/) Hallstrom & Moye-Rowley 1998 | Mutant phenotype / genetics | **Qualifies nucleus** | Is Ssz1's Pdr1 effect nuclear-resident? | "Pdr13p exerts its effect on Pdr1p at a posttranslational step" | *S. cerevisiae* | High; extraribosomal role does not require stable nuclear residence |
| [10792726](https://pubmed.ncbi.nlm.nih.gov/10792726/) Mol Microbiol 2000 | Localization (IDA) | **Supports cytoplasm** | Where does Ssz1 reside? | Cytoplasmic localization; Hsp70 Pdr13p regulates Pdr1p | *S. cerevisiae* | Basis for the only experimental CC term |
| [11274393](https://pubmed.ncbi.nlm.nih.gov/11274393/) | Direct assay/interaction | **Supports RAC role** | Ssz1 function on the ribosome | de novo cotranslational protein folding; Ssz1–Zuo1 interaction | *S. cerevisiae* | Basis for GO:0051083 and Zuo1 IPI |
| [37081320](https://pubmed.ncbi.nlm.nih.gov/37081320/) RAC cryo-EM 2023 | Structural | **Qualifies mechanism** | RAC architecture / Ssz1 role | Ssz1 SBD–Zuo1 interaction holds RAC together; Zuo1 positions Ssb for activation | *C. thermophilum* RAC on 80S | Structural basis: Ssz1 is scaffold/activator, not client-folder |
| [35701497](https://pubmed.ncbi.nlm.nih.gov/35701497/) RAC remodeling 2022 | Structural | **Qualifies mechanism** | RAC dynamics during folding | RAC autoinhibited without nascent chain; remodels to expose Zuo1 J-domain to Ssb | *S. cerevisiae* | Reinforces relay/activation model |
| [34580293](https://pubmed.ncbi.nlm.nih.gov/34580293/) Pathway of Hsp70 at ribosome 2021 | Direct assay (crosslinking) | **Qualifies mechanism** | How Ssb engages ribosome via Ssz1 | Ssb(ATP) heterodimerizes with Ssz1; Ssz1 tethered by Zuo1 | *S. cerevisiae* | Ssz1 role = positioning Ssb, not folding clients |
| [11929994](https://pubmed.ncbi.nlm.nih.gov/11929994/) Functional chaperone triad 2002 | Direct assay/genetics | **Qualifies mechanism** | Ssz1/RAC/Ssb act in concert | Efficient nascent-chain crosslink to Ssb depends on functional RAC | *S. cerevisiae* | Ssz1 acts on nascent chains, in concert with Ssb/Zuo1 |
| [28771464](https://pubmed.ncbi.nlm.nih.gov/28771464/) RAC review 2017 | Review | Orientation | Ssz1/RAC function summary | "unconventional Hsp70 homolog Ssz1"; RAC stimulates Ssb ATPase | Review | Review-level; consistent with primary data |
| PANTHER PTHR19375 v19 | Computational/evolutionary | **Supports curation action** | Is PTN001065099 ancestral to Ssz1? | Both PTN001065099 and PTN000452648 confirmed on Ssz1 lineage | Phylogenetic tree | High for topology; IRD not yet deployed |
| QuickGO/GO_Central (P38788) | Database | **Supports over-annotation call** | Live evidence codes for disputed terms | Refolding = positive IBA, 0 NOT hits family-wide; PM absent; nucleus live IBA | GO snapshot 2026 | Database-level; reflects live state |

---

## GO Curation Implications

The evidence supports the following as **leads requiring curator verification**:

- **GO:0042026 "protein refolding" (BP):** *Not core; remove or block.* The term is supported only by IBA propagated from canonical-Hsp70 ancestor PTN000452648. The correct BP for Ssz1 is **GO:0051083 "de novo cotranslational protein folding"** (retain; IDA/IMP), which captures its true role. Preferred correction per the seed: deploy a PAINT NOT/IRD at PTN001065099 (confirmed ancestral to Ssz1). Verify whether the currently-absent IRD is intentional or un-curated.
- **GO:0005634 "nucleus" (CC):** *Remove.* Live IBA over-annotation from canonical Hsp70 paralogs; no experimental support. Retain only **GO:0005737 "cytoplasm"** (IDA).
- **GO:0005886 "plasma membrane" (CC):** *Already resolved.* Absent from live GO_Central; note the lagging UniProt xref.
- **MF terms:** Retain the Zuo1-based interaction terms (GO:0051087 protein-folding chaperone binding; GO:0031072 heat shock protein binding). These are more informative than generic "protein binding" and reflect the experimentally documented RAC interaction. No refoldase-type MF (e.g., unfolded protein binding tied to refolding) is supported.

---

## Mechanistic Scope

The immediate molecular function under test is whether Ssz1 directly performs **protein refolding** — i.e., ATP-dependent (or ATP-independent) recognition, holding, and productive folding of an *already-denatured or misfolded* client. The evidence indicates Ssz1's direct activity is instead: (i) serving as the structural Hsp70 subunit that, with Zuo1, forms RAC; (ii) tethering to the ribosome via Zuo1; and (iii) contributing to the transient, low-affinity relay of *nascent* chains toward Ssb, whose ATPase Zuo1 activates. Refolding of denatured clients, nuclear residence, and plasma-membrane residence are **not** direct Ssz1 activities. The Pdr1-activation phenotype is a downstream, posttranslational regulatory effect, not evidence of nuclear localization. The disputed CC terms are propagation artifacts, not observed localizations.

---

## Conflicts and Alternatives

The dominant alternative explanation for every disputed annotation is **paralog confusion within PANTHER family PTHR19375**. Ssz1 is grouped with canonical cytosolic Hsp70s (Ssa1–4, human HSPA) that are bona fide ATP-driven refoldases and do shuttle to the nucleus. IBA propagation legitimately assigns those ancestral functions across the family but fails to account for Ssz1's rapid functional divergence into a specialized, ATPase-dead RAC scaffold. No organism-specific or isoform-specific finding rescues the refolding or nucleus claims; the structural literature (PMIDs 37081320, 35701497, 34580293, 11929994) uniformly casts Ssz1 as a scaffold/activator that positions Ssb, reinforcing rather than conflicting with the refutation. The only genuine extraribosomal role (Pdr1 activation) acts posttranslationally and does not require stable nuclear or membrane localization. No conflicting primary evidence supporting autonomous refolding or stable nucleus/PM residence of Ssz1 was found.

---

## Limitations and Knowledge Gaps

1. **The refolding IBA is un-blocked but the IRD is not deployed.** The seed proposes inspecting a NOT/IRD at PTN001065099, but the live check found **0 NOT annotations family-wide** for GO:0042026. *Gap:* is the absence of the IRD an intentional curator decision or an un-curated node? *Resolution:* a curator should confirm whether GO_Central intends to place the IRD at the Fungi node or to correct by direct removal on Ssz1.

2. **Node identity for the nucleus propagation.** The nucleus IBA is propagated from PTN002500132 (per QuickGO withFrom seeds), whereas the refolding IBA comes from PTN000452648; the seed only names PTN001065099/PTN000452648. *Gap:* the exact ancestral node for each disputed term should be verified in the current PANTHER release before an IRD strategy is chosen; the fix for nucleus may differ from the fix for refolding.

3. **UniProt xref lag.** The plasma-membrane term persists in the UniProt cross-reference snapshot though absent from live GO_Central. Curators relying on the UniProt snapshot could mistakenly re-litigate an already-resolved term. *Resolution:* verify against live QuickGO/GO_Central, not the static xref.

4. **No dedicated experimental null for Ssz1 as an autonomous stress refoldase.** The refutation rests on absence of a mechanism (no ATPase, transient binding) and absence of a positive experimental annotation — not on an experiment showing Ssz1 fails to refold a model substrate (e.g., denatured luciferase). This is a reasonable inference but not a direct null result.

5. **Withheld local bioinformatics.** The local `*-bioinformatics` analyses were intentionally withheld from this run; this report should be reconciled against them.

---

## Discriminating Tests

To decisively separate the seed hypothesis from the established relay model:

1. **In vitro refolding assay:** Test purified Ssz1 (± Zuo1, ± Ssb, ± ATP) for the ability to refold a chemically or thermally denatured model substrate (firefly luciferase, MDH). *Prediction under refutation:* Ssz1 alone shows no ATP-dependent refolding; any activity requires the full Ssb-containing triad and is attributable to Ssb.
2. **ATP-independence probe:** Repeat (1) with the ATP-binding-dead Ssz1 mutant. *Prediction:* no change relative to WT Ssz1, consistent with ATP-binding being dispensable (PMID:17901048).
3. **Localization by high-resolution imaging / fractionation:** Quantitative confocal + subcellular fractionation under basal and heat-shock conditions to test for any nuclear or plasma-membrane Ssz1 pool beyond the ribosome-associated cytosolic fraction. *Prediction:* cytosolic/ribosomal only.
4. **PANTHER curation simulation:** Deploy a test IRD for GO:0042026 at PTN001065099 in a sandbox and confirm the positive IBA to P38788 is suppressed — validating F002/F004 as a curation lead.
5. **Client-capture assay:** In vivo crosslinking / proximity labeling from Ssz1 to identify whether any denatured-client interactions exist outside the nascent-chain context. *Prediction:* interactions dominated by Zuo1/Ssb and nascent chains, not mature misfolded clients.

---

## Curation Leads (require curator verification)

**Lead 1 — Protein refolding (GO:0042026) over-annotation.**
- *Action:* Remove or block the positive IBA on P38788. Preferred mechanism per seed: deploy a PAINT **NOT/IRD** for GO:0042026 at **PTN001065099** (confirmed ancestral to Ssz1 in PANTHER v19), suppressing propagation to the SSZ1 clade.
- *Justification snippets to verify:*
  - PMID:17901048 — "Ssz1 is not an ATPase in vitro, and even its ability to bind ATP is dispensable in vivo."
  - PMID:32198371 — "the combined data indicate that Ssz1 is an active chaperone optimized for transient, low-affinity substrate binding, which ensures the flux of nascent chains through RAC/Ssb."
- *Note:* Verify whether the missing IRD (0 NOT hits family-wide) is intentional or un-curated.

**Lead 2 — Nucleus (GO:0005634) over-annotation.**
- *Action:* Remove the live IBA `is_active_in` nucleus annotation as a paralog-driven propagation from canonical cytosolic Hsp70s; retain only cytoplasm (GO:0005737, IDA).
- *Justification snippet:* PMID:9488429 — "Genetic and Western blotting experiments indicated that Pdr13p exerts its effect on Pdr1p at a posttranslational step" (extraribosomal role that does not establish stable nuclear residence).

**Lead 3 — Plasma membrane (GO:0005886).**
- *Action:* No new action; already absent from live GO_Central. Flag the UniProt cross-reference snapshot as lagging.

**Lead 4 — Retain the correct positive annotations.**
- Retain **GO:0051083** "de novo cotranslational protein folding" (BP; IDA/IMP, PMID:11274393), **GO:0005737** cytoplasm (CC; IDA, PMID:10792726), and the Zuo1-based MF interaction terms (GO:0051087 protein-folding chaperone binding; GO:0031072 heat shock protein binding). These, not refolding, represent Ssz1's primary function as a RAC subunit.

**Suggested curator questions:**
1. Is the absence of an IRD for GO:0042026 at PTN001065099 an intentional GO_Central decision, or simply un-curated?
2. Should the nucleus correction be handled by an IRD at the propagating node (PTN002500132) or by direct removal on P38788?
3. Are there any downstream tools relying on the UniProt xref snapshot that would re-introduce the removed plasma-membrane term?

---

*Report generated from 3 completed investigation iterations; 6 confirmed findings; 11 papers reviewed. Live GO/PANTHER/QuickGO checks reflect the 2026 snapshot. Withheld local bioinformatics analyses were not available to this run and should be reconciled against this report.*


## Artifacts

- [OpenScientist artifact GO decision table](openscientist_artifacts/artifact_GO_decision_table.csv)
- [OpenScientist artifact P38788 live GO annotations](openscientist_artifacts/artifact_P38788_live_GO_annotations.csv)
- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)