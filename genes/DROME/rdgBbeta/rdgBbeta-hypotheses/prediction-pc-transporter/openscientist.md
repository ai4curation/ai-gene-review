---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-10T03:54:38.794170'
end_time: '2026-07-10T04:07:23.243439'
duration_seconds: 764.45
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: DROME
  gene: rdgBbeta
  gene_symbol: rdgBbeta
  uniprot_accession: Q9U9P7
  taxon_id: NCBITaxon:7227
  taxon_label: Drosophila melanogaster
  focus_type: computational_prediction
  hypothesis_slug: prediction-pc-transporter
  hypothesis_text: BioReason-Pro SFT predicts phosphatidylcholine transporter activity
    (GO:0008525) for the Drosophila melanogaster protein rdgBbeta (Q9U9P7), a member
    of the RdgB/PITP (phosphatidylinositol transfer protein) family. Independently
    assess whether rdgBbeta -- a Class II PITP (PITPNC1/vibrator-type) -- has phosphatidylcholine
    transfer/transporter activity, or whether its characterized lipid-transfer specificity
    is for phosphatidylinositol (and possibly phosphatidic acid) rather than phosphatidylcholine,
    which would make the phosphatidylcholine-transporter prediction a paralog/substrate
    misassignment. Determine whether the prediction is supported or refuted.
  term_context: '- Term: phosphatidylcholine transporter activity (GO:0008525)'
  reference_context: '- doi:10.64898/2026.03.19.712954'
  source_file: ''
  source_selector: ''
  source_context_yaml: "hypothesis: BioReason-Pro SFT predicts phosphatidylcholine\
    \ transporter activity (GO:0008525) for the Drosophila\n  melanogaster protein\
    \ rdgBbeta (Q9U9P7), a member of the RdgB/PITP (phosphatidylinositol transfer\
    \ protein)\n  family. Independently assess whether rdgBbeta -- a Class II PITP\
    \ (PITPNC1/vibrator-type) -- has phosphatidylcholine\n  transfer/transporter activity,\
    \ or whether its characterized lipid-transfer specificity is for phosphatidylinositol\n\
    \  (and possibly phosphatidic acid) rather than phosphatidylcholine, which would\
    \ make the phosphatidylcholine-transporter\n  prediction a paralog/substrate misassignment.\
    \ Determine whether the prediction is supported or refuted.\nfocus_type: computational_prediction\n\
    term_id: GO:0008525\nterm_label: phosphatidylcholine transporter activity\ncontext:\
    \ []\nreference_id:\n- doi:10.64898/2026.03.19.712954"
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

- **Organism code:** DROME
- **Taxon:** Drosophila melanogaster (NCBITaxon:7227)
- **Gene directory:** rdgBbeta
- **Gene symbol:** rdgBbeta
- **UniProt accession:** Q9U9P7

## Focus

- **Focus type:** computational_prediction
- **Hypothesis slug:** prediction-pc-transporter
- **Source file:** 
- **Source selector:** 

## Seed Hypothesis

BioReason-Pro SFT predicts phosphatidylcholine transporter activity (GO:0008525) for the Drosophila melanogaster protein rdgBbeta (Q9U9P7), a member of the RdgB/PITP (phosphatidylinositol transfer protein) family. Independently assess whether rdgBbeta -- a Class II PITP (PITPNC1/vibrator-type) -- has phosphatidylcholine transfer/transporter activity, or whether its characterized lipid-transfer specificity is for phosphatidylinositol (and possibly phosphatidic acid) rather than phosphatidylcholine, which would make the phosphatidylcholine-transporter prediction a paralog/substrate misassignment. Determine whether the prediction is supported or refuted.

## Term and Decision Context

- Term: phosphatidylcholine transporter activity (GO:0008525)

## Reference Context

- doi:10.64898/2026.03.19.712954

## Source Context YAML

```yaml
hypothesis: BioReason-Pro SFT predicts phosphatidylcholine transporter activity (GO:0008525) for the Drosophila
  melanogaster protein rdgBbeta (Q9U9P7), a member of the RdgB/PITP (phosphatidylinositol transfer protein)
  family. Independently assess whether rdgBbeta -- a Class II PITP (PITPNC1/vibrator-type) -- has phosphatidylcholine
  transfer/transporter activity, or whether its characterized lipid-transfer specificity is for phosphatidylinositol
  (and possibly phosphatidic acid) rather than phosphatidylcholine, which would make the phosphatidylcholine-transporter
  prediction a paralog/substrate misassignment. Determine whether the prediction is supported or refuted.
focus_type: computational_prediction
term_id: GO:0008525
term_label: phosphatidylcholine transporter activity
context: []
reference_id:
- doi:10.64898/2026.03.19.712954
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

# AIGR Gene Hypothesis Deep Research — Final Report

## Target: Drosophila melanogaster rdgBbeta (UniProt Q9U9P7)
## Hypothesis: Phosphatidylcholine transporter activity (GO:0008525)
## Focus type: computational_prediction (BioReason-Pro SFT)

---

## Summary

The BioReason-Pro SFT model predicts **phosphatidylcholine transporter activity
(GO:0008525)** for the Drosophila melanogaster protein `rdgBbeta` (Q9U9P7). After
three iterations of literature review, sequence/orthology analysis, and a
family-wide GO annotation audit, this prediction is **REFUTED**. `rdgBbeta` is a
**single-domain Class II phosphatidylinositol transfer protein (PITP)** — the
Drosophila ortholog of human **PITPNC1** (the "vibrator"/RdgBβ clade) — and the
direct biochemistry of this clade shows it binds and transfers
**phosphatidylinositol (PI)** and **phosphatidic acid (PA)** but **"hardly binds
phosphatidylcholine"** ([PMID: 22822086](https://pubmed.ncbi.nlm.nih.gov/22822086/)).

Phosphatidylcholine transfer is instead a defining property of a *different*
branch of the family: the **Class I PITPs (PITPα/PITPβ)** with dual PI/PC
specificity, and the **multidomain/Sec14-type** transfer proteins. A systematic
audit of GO:0008525 across human, mouse, rat, fly, and yeast PITPs found direct
experimental (IDA) support only in those PC-competent branches (PITPNA, PITPNB,
Drosophila multidomain `rdgB`, yeast SEC14) — and **no experimental support
anywhere in the Class II clade**. `rdgBbeta` itself carries **no GO:0008525
annotation**; its curated molecular functions are PI binding (GO:0035091, IBA)
and PI transfer activity (GO:0008526, ISS), which are the accurate terms.

The prediction is best explained as **paralog / substrate misassignment**: a
PC-transfer trait that is genuine for Class I and multidomain paralogs has been
incorrectly propagated onto the Class II member. The main caveat is that the
decisive "no PC" assay was performed on the mammalian ortholog PITPNC1, not on
the Drosophila protein directly, so the refutation rests on strong orthology
(61.6% identity to PITPNC1 vs 42.7% to Class I PITPNA) plus concordant clade-level
biochemistry rather than a fly-specific PC-transfer assay. Even so, no evidence
supports PC transport and direct evidence argues against it. **Curator lead:
reject GO:0008525; retain GO:0008526 (PI transfer) as the core molecular
function.**

---

## Key Findings

### Finding 1 — RdgBβ/PITPNC1 binds and transfers PI and phosphatidic acid, but hardly binds phosphatidylcholine

Direct in vitro lipid binding and transfer assays on the Class II PITP
**RdgBβ (PITPNC1)** demonstrate that, besides phosphatidylinositol, the protein
binds and transfers **phosphatidic acid (PA)** and is recovered pre-loaded with
PA / phosphatidylglycerol when expressed in *E. coli* — but it **"hardly binds
phosphatidylcholine"** ([PMID: 22822086](https://pubmed.ncbi.nlm.nih.gov/22822086/),
Garner et al. 2012). This is the single most decisive piece of evidence against
the seed hypothesis, because it assays exactly the activity in question (lipid
transfer specificity) on exactly the clade to which `rdgBbeta` belongs.

The result is corroborated by an **independent Class II ortholog**: recombinant
mouse **mM-rdgBβ1** "shows the specific binding activity to phosphatidylinositol
but not to other phospholipids" ([PMID: 12562526](https://pubmed.ncbi.nlm.nih.gov/12562526/)).
Two independent Class II proteins, characterized in two laboratories, converge on
the same conclusion: PI (and, for PITPNC1, PA) is the physiological cargo, and PC
is not a bound/transferred ligand.

For contrast, PC binding *is* a real property of the **Class I PITPs**: in
Class I PITPα/β "the preferred lipid that can occupy the site can be either
phosphatidylinositol (PI) or phosphatidylcholine (PC)"
([PMID: 10358925](https://pubmed.ncbi.nlm.nih.gov/10358925/)). This dual PI/PC
specificity — quantified elsewhere as an ~16-fold preference for PI over PC with
measurable PC transfer ([PMID: 3651458](https://pubmed.ncbi.nlm.nih.gov/3651458/)) —
is precisely the trait a PC-transporter GO term captures, and it is a Class I /
Sec14-type feature, **not** a Class II feature. The prediction thus maps a real
biochemical activity onto the wrong branch of the family.

### Finding 2 — Drosophila rdgBbeta (Q9U9P7) is a single-domain Class II PITP orthologous to human PITPNC1

UniProt Q9U9P7 is annotated **PITC1_DROME, "Cytoplasmic phosphatidylinositol
transfer protein 1"**, a 273-residue protein consisting of a **single PITP
domain** (Pfam PF02121 IP_trans; InterPro IPR001666 PI_transfer; PANTHER
PTHR10658:SF54). It lacks the additional regulatory/membrane-targeting domains
(FFAT, DDHD, LNS2, transmembrane region) that characterize the large multidomain
RdgBα/Nir-type proteins.

Global pairwise Needleman–Wunsch alignments computed in this investigation place
`rdgBbeta` firmly in the **Class II** clade: **61.6% identity to human PITPNC1
(Class II)** versus only **42.7% identity to human PITPNA (Class I)**. This
~19-point identity gap is a clear orthology signal — `rdgBbeta` is the fly
ortholog of the mammalian "vibrator"/RdgBβ protein PITPNC1, not of the
PC-competent Class I PITPs.

The single-domain Class II identity is confirmed in the review literature:
"Three members of the PITP family (PITPα, PITPβ, and RdgBβ (retinal degeneration
type B) alt. name PITPNC1) are present as single domain proteins"
([PMID: 23086419](https://pubmed.ncbi.nlm.nih.gov/23086419/)). Critically, the
current UniProt GO annotation for Q9U9P7 already reflects the correct
biochemistry: **phosphatidylinositol binding (GO:0035091, IBA)** and
**phosphatidylinositol transfer activity (GO:0008526, ISS)** — and **no
GO:0008525** is present. The predicted PC-transporter term would therefore be an
*addition* that contradicts the existing, more accurate PI-transfer annotation.

### Finding 3 — GO:0008525 has direct evidence only for Class I / multidomain PITP paralogs, never for the Class II PITPNC1/rdgBbeta clade

A systematic QuickGO/GOA enumeration of **GO:0008525 (phosphatidylcholine
transporter activity)** across human, mouse, rat, fly, and yeast PITP-family
proteins reveals a sharp phylogenetic pattern. Direct experimental (**IDA**)
support for the PC-transporter term exists only for the PC-competent branches:

- **Class I PITPs**: human PITPNA (Q00169) and PITPNB (P48739) and their rodent
  orthologs;
- **Drosophila multidomain rdgB** (P43125, IDA);
- **Yeast SEC14** (P24280, IDA) — the founding dual PI/PC transfer protein, whose
  in vitro exchange of PI *or* PC is textbook ([PMID: 15299870](https://pubmed.ncbi.nlm.nih.gov/15299870/)).

By contrast, the **entire Class II clade** carries **a single** GO:0008525
annotation — rat Pitpnc1 (A0A8I6A182), and that annotation is **ISO only**
(inferred electronically from an ortholog), with **no IDA/EXP support anywhere**
in the clade. Drosophila `rdgBbeta` (Q9U9P7) carries **no GO:0008525 annotation
at all**. Within *Drosophila* specifically, PC-transporter activity is annotated
to the paralogs **rdgB (IDA)** and **vib/vibrator (IBA)** — not to `rdgBbeta`.

This is the fingerprint of paralog over-annotation. The one Class II GO:0008525
record in existence is itself a non-experimental electronic inference that most
plausibly originated by carry-over from a Class I / multidomain paralog. A model
trained on such annotation landscapes can readily reproduce the same
misassignment for `rdgBbeta`. *(Provenance: computed enumeration saved to
`/tmp/go0008525_pitp_family.csv`.)*

---

## Mechanistic Model / Interpretation

The PITP family splits into functionally distinct branches, and the seed
hypothesis fails because it ignores that split. The molecular function under test
is monomeric, headgroup-specific lipid transfer by a soluble PITP-domain protein:
extract a lipid, shield its headgroup inside a hydrophobic cavity, and deposit it
at an acceptor membrane. The discriminating variable is **headgroup specificity
(PC vs PI/PA)**.

### PITP family map and PC-transfer competence

| Branch | Representative proteins | Domain architecture | PI transfer | PC transfer | GO:0008525 evidence |
|---|---|---|---|---|---|
| **Class I** | PITPα/PITPNA, PITPβ/PITPNB | Single PITP domain | Yes | **Yes** (dual specificity) | **IDA** (direct) |
| **Multidomain RdgBα / Sec14** | Drosophila rdgB, yeast SEC14, Nir2 | PITP + FFAT/DDHD/LNS2 | Yes | **Yes** | **IDA** (direct) |
| **Class II (target clade)** | **rdgBbeta/PITPNC1**, vibrator | Single PITP domain | Yes | **No / "hardly"** | none direct; 1 ISO record only |

```
                         PITP superfamily
                               |
        -----------------------------------------------
        |                      |                        |
   Class I PITPα/β     Multidomain RdgBα         Class II  <-- rdgBbeta (Q9U9P7)
   PITPNA / PITPNB     rdgB / SEC14 / Nir2       PITPNC1 / vibrator
        |                      |                        |
   PI + PC transfer     PI + PC transfer          PI + PA transfer
   GO:0008525 (IDA)     GO:0008525 (IDA)          "hardly binds PC"
                                                  GO:0008526 (PI transfer)
                                                  << NO GO:0008525 >>

   Prediction path (WRONG):  Class I / multidomain PC-transfer trait
                             ─────propagated across paralogs────►  rdgBbeta
```

**Immediate molecular function.** The evidence indicates the direct molecular
activity of Q9U9P7 is **PI transfer** (GO:0008526) and, by clade analogy with
PITPNC1, **PA binding/transfer** — with PC essentially excluded from the binding
pocket. PC transfer is therefore not this gene product's activity; it is the
activity of sister paralogs. Downstream roles of PITPs (phosphoinositide
signaling, photoreceptor/neural signal transduction) are pathway consequences,
not the primary molecular activity, and do not implicate PC transport.

**Why the model likely erred.** Three compounding factors: (1) *frequency /
paralog bias* — most experimentally characterized PITPs (Class I, SEC14) are
PC-competent, so "PC transporter" is the family-common label; (2) *shared PITP
domain* — the single conserved fold (PF02121) is common to PC-competent and
PC-incompetent members, so domain-level features do not discriminate; (3)
*annotation carry-over* — the one existing Class II GO:0008525 record is an ISO
electronic inference, providing a spurious training signal. None of these reflect
the measured biochemistry of the Class II clade.

---

## Evidence Base / Evidence Matrix

| Citation | Evidence type | Direction | Claim tested | Key finding | Context | Confidence & limitations |
|---|---|---|---|---|---|---|
| [PMID: 22822086](https://pubmed.ncbi.nlm.nih.gov/22822086/) | Direct assay (in vitro binding/transfer) | **Refutes** | Does RdgBβ/PITPNC1 transfer PC? | Binds/transfers PI and PA; "hardly binds phosphatidylcholine"; preloaded with PA/PG | Recombinant mammalian PITPNC1 | High; mammalian ortholog, not fly protein directly |
| [PMID: 12562526](https://pubmed.ncbi.nlm.nih.gov/12562526/) | Direct assay (recombinant binding) | **Refutes** | PC binding by a Class II RdgBβ ortholog | mM-rdgBβ1 binds PI "but not to other phospholipids" | Recombinant mouse Class II PITP | Moderate–high; splice variant; qualitative |
| [PMID: 10358925](https://pubmed.ncbi.nlm.nih.gov/10358925/) | Review of direct assays | **Qualifies / competing** | Which PITPs bind PC? | PI *or* PC can occupy the Class I PITP site | Mammalian Class I PITPα/β | High; establishes PC transfer as Class I trait |
| [PMID: 3651458](https://pubmed.ncbi.nlm.nih.gov/3651458/) | Direct assay (affinity/kinetics) | **Qualifies / competing** | Magnitude of PC vs PI transfer | ~16-fold PI-over-PC preference; measurable PC transfer | Bovine brain PI-TP (Class I-like) | High; PC transfer is a Class I quantitative property |
| [PMID: 15299870](https://pubmed.ncbi.nlm.nih.gov/15299870/) | Structural/biochemical | **Competing** | Dual PI/PC specificity origin | SEC14 exchanges PI *or* PC in vitro | Yeast Sec14p | High; multidomain/Sec14 branch, not Class II |
| [PMID: 23086419](https://pubmed.ncbi.nlm.nih.gov/23086419/) | Structural/evolutionary review | **Supports (classification)** | Is RdgBβ/PITPNC1 a single-domain Class II PITP? | Confirms RdgBβ = PITPNC1, single-domain, distinct branch | Family-wide | High |
| UniProt Q9U9P7 + Pfam/InterPro/PANTHER; NW identity (61.6% vs PITPNC1; 42.7% vs PITPNA) | Computational (sequence/domain/orthology) | **Supports (classification)** | Is fly rdgBbeta a Class II PITPNC1 ortholog? | Single PITP domain; closest to PITPNC1 by identity | Bioinformatic | High; standard alignment/domain evidence |
| QuickGO/GOA enumeration of GO:0008525 | Database landscape (computed) | **Refutes (over-annotation pattern)** | Who has direct PC-transporter evidence? | IDA only in Class I / multidomain / SEC14; Class II has 1 ISO record; rdgBbeta has none | Human/mouse/rat/fly/yeast | High for the annotation pattern |
| [PMID: 17543578](https://pubmed.ncbi.nlm.nih.gov/17543578/) | Review | Orientation | RdgB family function | RdgB proteins are PITP-domain lipid-transfer proteins | Family review | Moderate; review-level |
| [PMID: 9216063](https://pubmed.ncbi.nlm.nih.gov/9216063/) | Molecular characterization | Orientation | rdgB family homology | Human rdgB N-terminus homologous to PITPα/β | Rat/human retina | Moderate; supports family placement |

---

## GO Curation Implications

**Leads (require curator verification):**

1. **Do NOT add GO:0008525 (phosphatidylcholine transporter activity)** to
   `rdgBbeta` (Q9U9P7). The computational prediction is contradicted by direct
   assays on the clade ("hardly binds phosphatidylcholine",
   [PMID: 22822086](https://pubmed.ncbi.nlm.nih.gov/22822086/)) and by the absence
   of any experimental PC-transporter evidence in the entire Class II clade.
   Recommend **reject** the prediction.

2. **Retain the existing, more accurate MF annotations**:
   - **GO:0008526 — phosphatidylinositol transfer activity** (currently ISS): the
     correct, clade-consistent molecular function and core MF.
   - **GO:0035091 — phosphatidylinositol binding** (currently IBA): consistent
     with clade biochemistry.

3. **Consider (lead) a phosphatidic-acid–related MF** as a more informative
   activity than PC transfer, given that PITPNC1 binds/transfers PA
   ([PMID: 22822086](https://pubmed.ncbi.nlm.nih.gov/22822086/)). Any such term
   should be applied only with an ISS/ISO evidence code from PITPNC1 and flagged,
   since the direct PA assay was on the mammalian ortholog; Drosophila-specific
   evidence is lacking, so treat as non-core for DROME for now.

4. **Treat GO:0008525 as non-core** for this gene and flag the single existing
   Class II ISO GO:0008525 record (rat Pitpnc1) as a candidate paralog-carry-over
   error.

The evidence supports an **MF** decision (lipid-transfer specificity), not a BP or
CC change. "Protein binding" is explicitly **not** recommended — the informative
term (PI transfer, GO:0008526) is already supported.

---

## Mechanistic Scope

The immediate function tested is **headgroup-specific monomeric lipid transfer**.
The seed prediction (PC transporter) conflates the Class II RdgBβ pocket
specificity (PI/PA) with the Class I PITPα/β dual PI/PC specificity. Everything
downstream — phosphoinositide signaling, secretory/Golgi function attributed to
some RdgB proteins, photoreceptor/neural signal transduction — is a pathway or
developmental consequence, not the primary molecular activity, and none of it
implicates PC transport by `rdgBbeta`. Importantly, `rdgBbeta` (small, cytosolic,
PITPNC1-type) must not be confused with `rdgB`-alpha (large multidomain
PITPNM/Nir-type); they are distinct paralogs with distinct biology, and it is the
alpha/multidomain and Class I paralogs — not `rdgBbeta` — that carry the direct
PC-transfer evidence.

---

## Conflicts and Alternatives

- **Paralog confusion (primary alternative and likely source of the prediction).**
  PC-transporter activity is genuine for Class I PITPα/β
  ([PMID: 10358925](https://pubmed.ncbi.nlm.nih.gov/10358925/)), for multidomain
  Drosophila `rdgB` (IDA), and for yeast SEC14
  ([PMID: 15299870](https://pubmed.ncbi.nlm.nih.gov/15299870/)). These are
  *paralogs* of `rdgBbeta`, not `rdgBbeta` itself. The model most plausibly
  generalized a family-common PC-transfer trait onto a Class II member that lacks
  it.
- **Isoform / organism-specific gaps.** The strongest "no PC" assay
  ([PMID: 22822086](https://pubmed.ncbi.nlm.nih.gov/22822086/)) used mammalian
  PITPNC1; the mouse Class II assay ([PMID: 12562526](https://pubmed.ncbi.nlm.nih.gov/12562526/))
  used mM-rdgBβ1. No published in vitro PC-transfer assay on the Drosophila Q9U9P7
  protein itself was located. The refutation rests on strong orthology plus
  concordant clade biochemistry rather than a fly-specific assay.
- **Quantitative "hardly" vs absolute exclusion.** "Hardly binds PC" is a low but
  non-zero statement; under artificial vesicle conditions trace PC association is
  conceivable. This does not justify a core PC-**transporter** MF annotation,
  which implies a physiological transport function.
- **Database carry-over.** The single Class II GO:0008525 record (rat Pitpnc1,
  ISO) is electronic and unverified; it should not be treated as independent
  support and may share the same error origin as the prediction.

---

## Limitations and Knowledge Gaps

1. **No Drosophila-protein-specific PC-transfer assay or functional phenotype
   paper.** *Checked:* PubMed for CG17818/rdgBbeta biochemistry and
   photoreceptor/PLC function; GOA. *Why it matters:* specificity is inferred from
   the mammalian ortholog. *Resolver:* in vitro PI/PC/PA transfer assay with
   purified recombinant Drosophila `rdgBbeta`. (No experimental PDB exists for
   Q9U9P7, but a high-confidence AlphaFold model is available, global pLDDT ≈ 91.5,
   so structural pocket analysis is immediately feasible.)
2. **PA-transfer relevance for the fly protein is inferred, not measured.**
   *Checked:* PMID 22822086 (PITPNC1). *Why it matters:* a PA-related MF would be
   the most informative substitute for the rejected PC term. *Resolver:* PA
   binding/transfer assay on Q9U9P7 or structural pocket analysis.
3. **Provenance of the single Class II ISO GO:0008525 record.** *Checked:*
   QuickGO/GOA enumeration. *Why it matters:* if it seeded the prediction, it is a
   correctable pipeline artifact. *Resolver:* trace the ISO "with/from" source
   protein.
4. **Provenance of the BioReason-Pro prediction** (whether it used Class I
   features) is unverified; matters for judging systematic paralog bias.

---

## Discriminating Tests / Proposed Follow-up Experiments

1. **In vitro fluorescent-lipid transfer assay** (pyrene-PI vs pyrene-PC vs
   NBD-PA) with purified recombinant DROME `rdgBbeta` — the single most decisive
   experiment. Expectation if refuted: robust PI (and PA) transfer, negligible PC
   transfer, mirroring [PMID: 22822086](https://pubmed.ncbi.nlm.nih.gov/22822086/).
2. **Mass-spectrometric lipidomics of the co-purified ligand** (as done for
   PITPNC1, which co-purified PA/PG). Absence of PC in the bound pool directly
   counters the prediction.
3. **Structural pocket comparison** (AlphaFold model of Q9U9P7 vs Class I PITPα
   holo-structures vs PITPNC1): identify headgroup-coordinating residues and test
   whether the pocket can accommodate the PC choline headgroup.
4. **Rescue/complementation:** does `rdgBbeta` substitute for Class I PITP
   PC-dependent functions? A negative result supports non-PC specificity.
5. **Annotation-provenance audit:** trace the rat Pitpnc1 ISO GO:0008525 record's
   source and any BioReason-Pro training exposure to Class I / multidomain PITP
   PC-transporter annotations, to confirm the paralog-carry-over mechanism.

---

## Curation Leads (require curator verification)

- **Action change:** Reject/omit **GO:0008525** for `rdgBbeta`; do not import the
  BioReason-Pro SFT prediction.
- **Retain:** **GO:0008526** (phosphatidylinositol transfer activity, ISS) and
  **GO:0035091** (phosphatidylinositol binding, IBA) as the accurate MF core.
- **Candidate new/replacement term (lead):** a **phosphatidic-acid
  binding/transfer** MF term supported by ISS/ISO from PITPNC1
  ([PMID: 22822086](https://pubmed.ncbi.nlm.nih.gov/22822086/)), clearly flagged
  as ortholog-inferred and non-core for DROME.
- **Candidate reference + snippet to verify:** [PMID: 22822086](https://pubmed.ncbi.nlm.nih.gov/22822086/)
  — *"besides PI, RdgBβ binds and transfers phosphatidic acid (PA) but hardly binds
  phosphatidylcholine."*
- **Candidate reference + snippet to verify:** [PMID: 12562526](https://pubmed.ncbi.nlm.nih.gov/12562526/)
  — *"The recombinant mM-rdgBbeta1 protein shows the specific binding activity to
  phosphatidylinositol but not to other phospholipids."*
- **Paralog-source reference:** [PMID: 10358925](https://pubmed.ncbi.nlm.nih.gov/10358925/)
  — *"The preferred lipid that can occupy the site can be either phosphatidylinositol
  (PI) or phosphatidylcholine (PC)"* (establishes PC transfer as a Class I trait).
- **Suggested curator question:** Was GO:0008525 propagated from Class I /
  multidomain PITP paralogs (rdgB, vib, PITPNA/B), and should the single Class II
  ISO record (rat Pitpnc1) also be flagged?
- **Suggested experiment:** direct DROME `rdgBbeta` PI/PC/PA transfer assay.

---

## Conclusion

The prediction of **phosphatidylcholine transporter activity (GO:0008525)** for
Drosophila `rdgBbeta` (Q9U9P7) is **REFUTED**. `rdgBbeta` is a single-domain
**Class II PITP** orthologous to human PITPNC1 (61.6% identity vs 42.7% to Class I
PITPNA). Direct biochemical characterization of this clade shows it binds and
transfers **phosphatidylinositol and phosphatidic acid** but **"hardly binds
phosphatidylcholine"** ([PMID: 22822086](https://pubmed.ncbi.nlm.nih.gov/22822086/));
PC transfer is a Class I / multidomain (Sec14-type) property. The prediction is a
**paralog / substrate misassignment**, reinforced by the fact that GO:0008525 has
direct (IDA) support only in Class I and multidomain paralogs and none in the
Class II clade. Curators should reject GO:0008525 and retain the more accurate
**phosphatidylinositol transfer activity (GO:0008526)**.

---

*Provenance:* UniProt Q9U9P7 JSON parse and Needleman–Wunsch identity computation
were executed in this investigation (rdgBbeta vs human PITPNC1 = 61.6%; vs PITPNA
= 42.7%). GO:0008525 family enumeration saved to `/tmp/go0008525_pitp_family.csv`.
Literature retrieved via PubMed.


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)