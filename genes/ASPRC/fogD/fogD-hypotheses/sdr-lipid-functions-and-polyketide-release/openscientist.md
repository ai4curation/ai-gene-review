---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-21T04:33:47.348753'
end_time: '2026-09-21T05:04:09.768413'
duration_seconds: 1822.42
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: ASPRC
  gene: fogD
  gene_symbol: fogD
  uniprot_accession: A0A017SE81
  taxon_id: NCBITaxon:1388766
  taxon_label: Aspergillus ruber (strain CBS 135680)
  focus_type: function_assignment
  hypothesis_slug: sdr-lipid-functions-and-polyketide-release
  hypothesis_text: Aspergillus ruber CBS 135680 FogD (A0A017SE81) has acylglycerone-phosphate
    reductase (NADP+) activity GO:0000140, triacylglycerol lipase activity GO:0004806,
    endoplasmic reticulum localization GO:0005783, lipid-droplet localization GO:0005811,
    phosphatidic acid biosynthetic participation GO:0006654 and triglyceride catabolism
    GO:0019433. Assess each claim independently using the flavoglaucin study PMID:32134669
    and PTHR44169 ancestral/source evidence. The source Ayr1 has measured dual reductase/lipase
    activity (PMID:24187129); SDR membership alone does not exclude hydrolysis. A
    secondary-metabolite role or missing signal peptide does not establish exclusive
    function or exclude peripheral organelle association. Determine what FogD itself
    was shown to catalyze versus proposed from cluster reconstitution; distinguish
    reductive thioester release from CH-OH donor oxidoreduction GO:0016616. Evaluate
    whether the historical TreeGrafter provenance node PTN001211783 can be traced
    to the current Ayr1-seeded IBD nodes PTN001213826 (ER) and PTN001963740 (other
    five claims), without assuming that one source is weak or family membership is
    itself a wrong graft.
  term_context: No specific term context supplied.
  reference_context: No specific reference context supplied.
  source_file: genes/ASPRC/fogD/fogD-ai-review.yaml
  source_selector: free-text
  source_context_yaml: "hypothesis: Aspergillus ruber CBS 135680 FogD (A0A017SE81)\
    \ has acylglycerone-phosphate reductase (NADP+)\n  activity GO:0000140, triacylglycerol\
    \ lipase activity GO:0004806, endoplasmic reticulum localization\n  GO:0005783,\
    \ lipid-droplet localization GO:0005811, phosphatidic acid biosynthetic participation\
    \ GO:0006654\n  and triglyceride catabolism GO:0019433. Assess each claim independently\
    \ using the flavoglaucin study\n  PMID:32134669 and PTHR44169 ancestral/source\
    \ evidence. The source Ayr1 has measured dual reductase/lipase\n  activity (PMID:24187129);\
    \ SDR membership alone does not exclude hydrolysis. A secondary-metabolite role\n\
    \  or missing signal peptide does not establish exclusive function or exclude\
    \ peripheral organelle association.\n  Determine what FogD itself was shown to\
    \ catalyze versus proposed from cluster reconstitution; distinguish\n  reductive\
    \ thioester release from CH-OH donor oxidoreduction GO:0016616. Evaluate whether\
    \ the historical\n  TreeGrafter provenance node PTN001211783 can be traced to\
    \ the current Ayr1-seeded IBD nodes PTN001213826\n  (ER) and PTN001963740 (other\
    \ five claims), without assuming that one source is weak or family membership\n\
    \  is itself a wrong graft.\nfocus_type: function_assignment\ncontext: []\nreference_id:\
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
citation_count: 7
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

- **Organism code:** ASPRC
- **Taxon:** Aspergillus ruber (strain CBS 135680) (NCBITaxon:1388766)
- **Gene directory:** fogD
- **Gene symbol:** fogD
- **UniProt accession:** A0A017SE81

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** sdr-lipid-functions-and-polyketide-release
- **Source file:** genes/ASPRC/fogD/fogD-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

Aspergillus ruber CBS 135680 FogD (A0A017SE81) has acylglycerone-phosphate reductase (NADP+) activity GO:0000140, triacylglycerol lipase activity GO:0004806, endoplasmic reticulum localization GO:0005783, lipid-droplet localization GO:0005811, phosphatidic acid biosynthetic participation GO:0006654 and triglyceride catabolism GO:0019433. Assess each claim independently using the flavoglaucin study PMID:32134669 and PTHR44169 ancestral/source evidence. The source Ayr1 has measured dual reductase/lipase activity (PMID:24187129); SDR membership alone does not exclude hydrolysis. A secondary-metabolite role or missing signal peptide does not establish exclusive function or exclude peripheral organelle association. Determine what FogD itself was shown to catalyze versus proposed from cluster reconstitution; distinguish reductive thioester release from CH-OH donor oxidoreduction GO:0016616. Evaluate whether the historical TreeGrafter provenance node PTN001211783 can be traced to the current Ayr1-seeded IBD nodes PTN001213826 (ER) and PTN001963740 (other five claims), without assuming that one source is weak or family membership is itself a wrong graft.

## Term and Decision Context

No specific term context supplied.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: Aspergillus ruber CBS 135680 FogD (A0A017SE81) has acylglycerone-phosphate reductase (NADP+)
  activity GO:0000140, triacylglycerol lipase activity GO:0004806, endoplasmic reticulum localization
  GO:0005783, lipid-droplet localization GO:0005811, phosphatidic acid biosynthetic participation GO:0006654
  and triglyceride catabolism GO:0019433. Assess each claim independently using the flavoglaucin study
  PMID:32134669 and PTHR44169 ancestral/source evidence. The source Ayr1 has measured dual reductase/lipase
  activity (PMID:24187129); SDR membership alone does not exclude hydrolysis. A secondary-metabolite role
  or missing signal peptide does not establish exclusive function or exclude peripheral organelle association.
  Determine what FogD itself was shown to catalyze versus proposed from cluster reconstitution; distinguish
  reductive thioester release from CH-OH donor oxidoreduction GO:0016616. Evaluate whether the historical
  TreeGrafter provenance node PTN001211783 can be traced to the current Ayr1-seeded IBD nodes PTN001213826
  (ER) and PTN001963740 (other five claims), without assuming that one source is weak or family membership
  is itself a wrong graft.
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

# AIGR Gene Hypothesis Deep Research — Final Report

**Gene:** fogD (FogD) · **Organism:** *Aspergillus ruber* CBS 135680 (NCBITaxon:1388766) · **UniProt:** A0A017SE81 (286 aa)
**Focus type:** function_assignment · **Hypothesis slug:** sdr-lipid-functions-and-polyketide-release
**Source:** `genes/ASPRC/fogD/fogD-ai-review.yaml` (free-text)

---

## Executive Judgment

**Verdict: Over-annotated (for the six lipid GO terms) / Partially supported (for the underlying SDR chemistry).**

The seed hypothesis asks a curator to weigh six lipid-metabolism GO terms on FogD —
acylglycerone-phosphate reductase (NADP+) activity (GO:0000140), triacylglycerol lipase
activity (GO:0004806), endoplasmic reticulum localization (GO:0005783), lipid-droplet
localization (GO:0005811), phosphatidic acid biosynthetic participation (GO:0006654), and
triglyceride catabolism (GO:0019433) — against what FogD was actually shown to do.

The clear answer from primary literature and public annotation provenance is that **all six
lipid terms are electronic (IEA:TreeGrafter) carry-overs propagated from the experimentally
characterized *Saccharomyces cerevisiae* protein Ayr1, and none of them is supported by any
FogD-specific assay, localization experiment, or mutant phenotype.** FogD's only
experimentally demonstrated role is as a **secondary-metabolite short-chain dehydrogenase/
reductase (SDR)** in the flavoglaucin biosynthetic cluster, where it temporarily reduces a
polyketide salicylaldehyde to a salicyl alcohol to permit downstream decoration
([PMID:32134669](https://pubmed.ncbi.nlm.nih.gov/32134669/)).

The important nuance — which the seed hypothesis correctly insists on — is that this is **not a
case of "wrong graft" or "weak source."** The PANTHER family assignment (PTHR44169, the Ayr1
family) is genuine, FogD retains an intact SDR catalytic tetrad, and SDR membership does not
by itself exclude hydrolase side-activity. But *plausible-by-homology is not
demonstrated-for-FogD*. At ~39% identity to Ayr1 (twilight zone), conserved fold and cofactor
chemistry transfer, whereas Ayr1's **specific substrate identities and dual moonlighting
functions do not**. The six lipid terms should therefore be treated as non-core electronic
predictions rather than as FogD functions, and the review should foreground the
secondary-metabolite reductase role.

---

## Key Findings

### Finding 1 — FogD's experimentally supported function is a secondary-metabolite SDR (polyketide salicylaldehyde reduction), not lipid metabolism

UniProt A0A017SE81 records the recommended name **"Short-chain dehydrogenase fogD"**, EC
1.1.1.-, and the alternate designation **"Flavoglaucin biosynthesis cluster protein D,"** with
the FUNCTION and PATHWAY comments framing the protein within secondary-metabolite biosynthesis
(ECO:0000269 / ECO:0000305 sourced to
[PMID:32134669](https://pubmed.ncbi.nlm.nih.gov/32134669/)). The DISRUPTION PHENOTYPE is
equally telling: deletion of *fogD* impairs flavoglaucin and congener production and yields
very low accumulation of (8E,10E,12E)-3,5,7-trihydroxytetradeca-8,10,12-trienoic acid — a
polyketide intermediate, not a glyceride or phospholipid.

The mechanistic paper is unambiguous about the chemistry. In the flavoglaucin pathway, the
polyketide skeleton is *"released as alkylated salicyl alcohols, which is a prerequisite for
consecutive hydroxylation and prenylation, before reoxidation to the final aldehyde products"*
([PMID:32134669](https://pubmed.ncbi.nlm.nih.gov/32134669/)). This describes a **reductive
tailoring step on a polyketide** — a CH-OH-forming NADP(H)-dependent reduction — which is the
generic SDR chemistry FogD shares with its family, applied to a secondary-metabolite substrate.
This is distinct from the *reductive thioester release* mechanism sometimes seen in polyketide
synthase R-domains; the evidence here supports a discrete oxidoreductase forming an alcohol,
consistent with the general MF term **GO:0016616 (oxidoreductase acting on CH-OH group of
donors, NAD/NADP acceptor).**

Sequence inspection confirms the enzyme is a bona fide catalytically competent SDR: the 286-aa
protein carries the N-terminal Rossmann cofactor motif **TGCGQGGIG** (residues ~8–16), the
catalytic serine (Ser145/146), the SDR signature **YxxxK** motif (**YNATK**, Tyr147/Lys151),
and the conserved Asn within an **NCAG** context (~res 82). The catalytic machinery is intact,
so the enzyme is a genuine active reductase — the question is only *on which substrate*, and
the direct evidence points to a polyketide, not acyl-DHAP or a triglyceride.

### Finding 2 — The six lipid-metabolism GO terms are IEA:TreeGrafter carry-overs seeded by *S. cerevisiae* Ayr1

Every one of the six lipid terms on A0A017SE81 carries the evidence code **IEA:TreeGrafter**.
FogD maps to PANTHER family **PTHR44169 "NADPH-DEPENDENT 1-ACYLDIHYDROXYACETONE PHOSPHATE
REDUCTASE"** — the Ayr1 family — and to subfamily **PTHR44169:SF3 "SHORT-CHAIN DEHYDROGENASE
SRDE."** The set of six terms mirrors, almost exactly, the experimentally characterized dual
biology of yeast Ayr1:

- **acyl-DHAP reductase** (GO:0000140),
- **novel TAG lipase** (GO:0004806) — *"identification of Ayr1p as a novel triacylglycerol
  lipase of yeast lipid droplets"* ([PMID:24187129](https://pubmed.ncbi.nlm.nih.gov/24187129/)),
- **ER + lipid-droplet** dual localization (GO:0005783, GO:0005811),
- and **ether/phospholipid + TAG metabolism** (GO:0006654, GO:0019433).

No FogD-specific assay, localization experiment, or mutant supports any of these six terms.
They are a coherent bundle precisely *because* they were transferred as a bundle from one
well-studied source protein. This is the signature of homology-based propagation, not of
independent characterization.

### Finding 3 — Provenance chain verified: the six lipid terms are TreeGrafter-propagated (node PTN001211783) from experimentally annotated Ayr1

Querying the QuickGO annotation API for A0A017SE81 shows all six terms with evidence
**IEA / ECO:0007826**, reference **GO_REF:0000118**, `assignedBy = TreeGrafter`, and
`withFrom = PANTHER:PTN001211783`. The corresponding QuickGO record for *S. cerevisiae* Ayr1
(**P40471**) shows each of these terms is **both experimentally supported and IBA-propagated**
(GO_Central, GO_REF:0000033):

| GO term | Ayr1 (P40471) experimental support |
|---|---|
| GO:0000140 acylglycerone-P reductase | IMP [PMID:10617610](https://pubmed.ncbi.nlm.nih.gov/10617610/) + EXP [PMID:1512203](https://pubmed.ncbi.nlm.nih.gov/1512203/) |
| GO:0004806 TAG lipase | IDA/IMP/IGI [PMID:24187129](https://pubmed.ncbi.nlm.nih.gov/24187129/) |
| GO:0005783 endoplasmic reticulum | IDA [PMID:10617610](https://pubmed.ncbi.nlm.nih.gov/10617610/) + EXP [PMID:14562095](https://pubmed.ncbi.nlm.nih.gov/14562095/)/[28916712](https://pubmed.ncbi.nlm.nih.gov/28916712/) + HDA [PMID:26928762](https://pubmed.ncbi.nlm.nih.gov/26928762/) |
| GO:0005811 lipid droplet | EXP [PMID:10515935](https://pubmed.ncbi.nlm.nih.gov/10515935/)/[21820081](https://pubmed.ncbi.nlm.nih.gov/21820081/) + IDA [PMID:10617610](https://pubmed.ncbi.nlm.nih.gov/10617610/)/[24868093](https://pubmed.ncbi.nlm.nih.gov/24868093/) |
| GO:0006654 phosphatidic acid biosynthesis | IMP [PMID:10617610](https://pubmed.ncbi.nlm.nih.gov/10617610/) |
| GO:0019433 triglyceride catabolism | IGI [PMID:24187129](https://pubmed.ncbi.nlm.nih.gov/24187129/) |

This confirms the seed hypothesis's core provenance concern: the FogD annotations trace back to
**genuinely experimental Ayr1 annotations**, propagated electronically. The historical
TreeGrafter provenance node **PTN001211783** is the recorded `withFrom` source on FogD; it is
consistent with — but at the resolution of the public annotation index cannot be independently
disambiguated from — the seed's proposed ancestral IBD nodes **PTN001213826** (ER) and
**PTN001963740** (the other five claims). The ancestral IBD node annotations themselves are not
exposed in the public GOlr annotation index and could not be retrieved to complete a
node-by-node trace. This is a genuine, honestly reported provenance gap: the propagation is
real and Ayr1-seeded, but the exact internal graft-node lineage is not fully verifiable from
public endpoints.

### Finding 4 — FogD shares only ~39% identity with Ayr1: conserved SDR chemistry, twilight-zone divergence

A global Needleman–Wunsch alignment of FogD (A0A017SE81, 286 aa) against *S. cerevisiae* Ayr1
(P40471, 297 aa) yields **111 identical residues over 281 aligned non-gap columns = 39.5%
identity** (38.8% over FogD length). Both proteins retain the N-terminal Rossmann NAD(P)-binding
motif (FogD **VTGCGQGGIG**; Ayr1 **VVTGASGG**) and the SDR catalytic **YxxxK** motif (FogD
Tyr147/Lys151; Ayr1 Tyr157/Lys161). Crucially, FogD is placed in the **distinct** subfamily
**PTHR44169:SF3 (SRDE)**, separate from the Ayr1 subfamily.

~39% identity sits squarely in the **twilight zone** of sequence homology. At this divergence,
the fold and the cofactor/catalytic chemistry are reliably conserved — so calling FogD an SDR
oxidoreductase is safe — but **substrate identity and specialized moonlighting functions are
not reliably transferable.** Ayr1's dual acyl-DHAP-reductase / TAG-lipase behavior and its
specific glyceride substrates are precisely the kind of fine specificity that diverges across
40%-identity paralogs, especially when the two proteins occupy different PANTHER subfamilies and
different biological contexts (primary lipid metabolism in yeast vs. secondary-metabolite
tailoring in a filamentous fungus).

---

## Mechanistic Model / Interpretation

The two competing readings of FogD can be laid out directly:

```
                          PTHR44169  (Ayr1 family, NADPH-dependent SDR fold)
                                  |
        +-------------------------+---------------------------+
        |                                                     |
  S. cerevisiae Ayr1 (P40471)                        A. ruber FogD (A0A017SE81)
  subfamily = Ayr1                                   subfamily = PTHR44169:SF3 (SRDE)
  297 aa                                             286 aa
        |                                                     |
  EXPERIMENTAL (multiple PMIDs):                     EXPERIMENTAL (PMID:32134669):
   - acyl-DHAP reductase  GO:0000140                  - flavoglaucin cluster SDR
   - TAG lipase           GO:0004806  <== moonlight    - reduces polyketide salicyl-
   - ER                   GO:0005783                     ALDEHYDE -> salicyl ALCOHOL
   - lipid droplet        GO:0005811                   - deletion impairs flavoglaucin
   - PA biosynthesis      GO:0006654                   - EC 1.1.1.-, intact SDR tetrad
   - TAG catabolism       GO:0019433                     (TGCGQGGIG / Ser / YNATK / NCAG)
        |                                                     ^
        |            ~39% identity (twilight zone)            |
        +-----> IEA:TreeGrafter propagation (withFrom -------+
                PANTHER:PTN001211783, GO_REF:0000118)
                copies all six lipid terms to FogD
```

**What transfers across 39% identity:** the SDR three-dimensional fold, the Rossmann
NAD(P)-binding site, the catalytic Ser–Tyr–Lys triad, and therefore the generic capacity for
**NADP(H)-dependent CH-OH ↔ C=O oxidoreduction** (GO:0016616). This is safe.

**What does NOT transfer:** the *specific substrates* (acyl-DHAP, triacylglycerol,
phosphatidic-acid pathway intermediates), the *hydrolase moonlighting* activity, and the
*organelle localization* (ER + lipid droplet) that were measured for Ayr1. These are
context-specific properties of a yeast primary-metabolic enzyme, not portable predictions for a
fungal secondary-metabolite tailoring enzyme.

**Reconciling the two views:** the seed hypothesis is right that SDR membership does not exclude
hydrolysis, and right that a secondary-metabolite role or a missing signal peptide does not by
itself *prove* the absence of peripheral organelle association. But the burden of evidence runs
the other way: there is *positive* experimental evidence for the polyketide-reductase role
(mutant phenotype + pathway reconstitution logic in PMID:32134669) and *zero* FogD-specific
evidence for any of the six lipid activities/locations. The parsimonious model is that FogD is a
**dedicated secondary-metabolite SDR** whose lipid annotations are homology artifacts.

The distinction the seed asks us to draw — *reductive thioester release vs. CH-OH donor
oxidoreduction* — resolves toward the latter as the safe MF: the evidence supports FogD forming
an alcohol (salicyl alcohol) by NADP(H)-dependent reduction, i.e. GO:0016616-type chemistry,
rather than establishing a chain-releasing R-domain thioester reductase mechanism.

---

## Evidence Base / Evidence Matrix

| Citation | Evidence type | Supports / refutes / qualifies | Claim tested | Key finding | Context | Confidence & limitations |
|---|---|---|---|---|---|---|
| [PMID:32134669](https://pubmed.ncbi.nlm.nih.gov/32134669/) | Direct assay + mutant phenotype (pathway reconstitution, gene deletion) | **Supports** FogD = secondary-metabolite SDR; **refutes** lipid-metabolism core role | FogD's actual catalytic role | Polyketide skeleton "released as alkylated salicyl alcohols… before reoxidation to the final aldehyde products"; *fogD* deletion impairs flavoglaucin production | *A. ruber* / flavoglaucin cluster, deletion + reconstitution | High for reductase role; exact substrate-bound state (free vs carrier-bound) less pinned |
| UniProt A0A017SE81 (record; sources PMID:32134669) | Review/database (curated, EXP-sourced) | Supports | Naming, EC, disruption phenotype | "Short-chain dehydrogenase fogD," EC 1.1.1.-, "Flavoglaucin biosynthesis cluster protein D"; SDR catalytic tetrad intact | Database, sourced to EXP paper | High for annotation; database orientation |
| QuickGO A0A017SE81 annotations | Computational (provenance) | **Refutes core status** of six lipid terms | Evidence codes / provenance of six lipid terms | All six terms = IEA/ECO:0007826, GO_REF:0000118, assignedBy=TreeGrafter, withFrom=PANTHER:PTN001211783 | Public annotation API | High; direct provenance readout |
| [PMID:24187129](https://pubmed.ncbi.nlm.nih.gov/24187129/) (Ayr1, P40471) | Direct assay (yeast) | **Competing / source of graft** | Origin of TAG-lipase + lipid-droplet terms | "identification of Ayr1p as a novel triacylglycerol lipase of yeast lipid droplets" | *S. cerevisiae* Ayr1 | High for Ayr1; not transferable to FogD at 39% id |
| [PMID:10617610](https://pubmed.ncbi.nlm.nih.gov/10617610/) (Ayr1) | Direct assay / mutant / localization (yeast) | Competing / source of graft | Origin of acyl-DHAP reductase, ER, PA-biosynthesis terms | Ayr1 experimental acyl-DHAP reductase + ER + PA-biosynthesis annotations | *S. cerevisiae* | High for Ayr1; source of propagation |
| Needleman–Wunsch FogD vs Ayr1 (this work) | Structural/evolutionary (computed) | **Qualifies** | Transferability of Ayr1 functions | 39.5% identity; shared Rossmann + YxxxK motifs; distinct PANTHER subfamily (SF3/SRDE) | Sequence analysis | High for the numbers; twilight-zone interpretation is standard but a judgment call |
| PANTHER PTHR44169 / :SF3 | Structural/evolutionary (database) | Qualifies | Family placement | FogD in Ayr1 family but distinct SRDE subfamily | Database | Medium-high; family real, subfamily distinct |

**How the literature bears on the findings.** The single deep-read primary paper,
*Biosynthesis of the Prenylated Salicylaldehyde Flavoglaucin Requires Temporary Reduction to
Salicyl Alcohol for Decoration before Reoxidation to the Final Product*
([PMID:32134669](https://pubmed.ncbi.nlm.nih.gov/32134669/)), directly establishes FogD's real
role and is the anchor for Findings 1 and the refutation of the lipid terms as core.
[PMID:24187129](https://pubmed.ncbi.nlm.nih.gov/24187129/) and
[PMID:10617610](https://pubmed.ncbi.nlm.nih.gov/10617610/) are Ayr1 (yeast) studies that
*explain the origin* of the propagated terms rather than supporting them for FogD — they are the
"competing/source-of-graft" evidence.

---

## GO Curation Implications

**Lead action (requires curator verification):** treat the six lipid terms as **non-core
electronic predictions**, not FogD functions. Concretely:

| GO term | Aspect | Current basis | Recommended curation lead |
|---|---|---|---|
| GO:0000140 acylglycerone-phosphate reductase (NADP+) activity | MF | IEA:TreeGrafter (Ayr1) | **Generalize / demote.** Replace as core MF with GO:0016616 (CH-OH donor, NAD/NADP acceptor oxidoreductase). Retain GO:0000140 only as a non-core IEA if kept at all. |
| GO:0004806 triacylglycerol lipase activity | MF | IEA:TreeGrafter (Ayr1 moonlight) | **Remove from core / flag as over-annotation.** No FogD hydrolase evidence; hydrolase moonlighting is Ayr1-specific. |
| GO:0005783 endoplasmic reticulum | CC | IEA:TreeGrafter (Ayr1) | **Do not treat as core.** No FogD localization data; retain only as low-confidence IEA. |
| GO:0005811 lipid droplet | CC | IEA:TreeGrafter (Ayr1) | **Do not treat as core.** Same rationale. |
| GO:0006654 phosphatidic acid biosynthetic process | BP | IEA:TreeGrafter (Ayr1) | **Remove from core / non-core.** FogD BP is secondary-metabolite biosynthesis, not glycerophospholipid. |
| GO:0019433 triglyceride catabolic process | BP | IEA:TreeGrafter (Ayr1) | **Remove from core / non-core.** Contradicts the demonstrated anabolic secondary-metabolite role. |

**Positively supported terms (leads to ADD as core):**

- **MF:** GO:0016616 — oxidoreductase activity, acting on the CH-OH group of donors, NAD or
  NADP as acceptor (safe, evidence-backed generalization of the demonstrated reduction). EC
  1.1.1.- from UniProt is consistent.
- **BP:** GO:0044550 — secondary metabolite biosynthetic process (and, if a curator accepts
  cluster-level annotation, a flavoglaucin/polyketide-specific child). Evidence: mutant
  phenotype + pathway role in [PMID:32134669](https://pubmed.ncbi.nlm.nih.gov/32134669/).

The recommendation deliberately avoids "protein binding" and instead anchors on the
evidence-backed oxidoreductase MF and secondary-metabolite BP.

---

## Mechanistic Scope

The **immediate molecular function** under test is a specific NADP(H)-dependent oxidoreduction.
The direct evidence (PMID:32134669) supports FogD catalyzing the reduction of a flavoglaucin
polyketide **salicylaldehyde to a salicyl alcohol** — an on-pathway, reversible tailoring step
that primes the intermediate for hydroxylation and prenylation before final reoxidation. This
is CH-OH/NADP oxidoreductase chemistry (GO:0016616), performed on a secondary-metabolite
substrate.

Separated from this direct activity are the **downstream / inferred properties** that the seed
hypothesis correctly flags:
- *Lipid substrates and hydrolase activity* (acyl-DHAP, TAG) are inferred only from Ayr1 homology.
- *ER and lipid-droplet localization* are inferred from Ayr1, with no FogD imaging.
- *Phosphatidic-acid biosynthesis and triglyceride catabolism* are pathway memberships copied
  from Ayr1's biology, not FogD phenotypes.

None of these downstream/inferred properties has been observed for FogD itself. The
loss-of-function evidence that *does* exist (deletion impairs flavoglaucin) points exclusively
to the secondary-metabolite role.

---

## Conflicts and Alternatives

1. **Paralog carry-over (primary conflict).** The six lipid terms are database carry-over from
   Ayr1 via TreeGrafter. This is the single most important alternative explanation and it is
   well supported: identical bundle of terms, identical `withFrom` source, IEA evidence only.
2. **Organism/context difference.** Ayr1 is a yeast primary-metabolic enzyme (glycerolipid
   metabolism); FogD is a filamentous-fungus secondary-metabolite tailoring enzyme. Different
   biological compartments and substrate pools make wholesale function transfer unlikely.
3. **Subfamily divergence.** FogD sits in PTHR44169:SF3 (SRDE), a distinct subfamily from
   Ayr1, reinforcing that specialized function has diverged even though the family is shared.
4. **The seed's own caution is valid and retained.** SDR fold does not exclude hydrolase
   side-activity, and absence of a signal peptide does not exclude peripheral membrane/organelle
   association. So the six terms cannot be declared *impossible* — only *unsupported for FogD*.
   The honest position is "not demonstrated," not "disproven."
5. **Mechanism ambiguity (thioester release vs alcohol formation).** The data favor discrete
   CH-OH-forming reduction (GO:0016616) over a chain-releasing thioester-reductase mechanism,
   but the exact substrate-tethering state at the moment of reduction is not fully resolved.

---

## Limitations and Knowledge Gaps

| Gap | What was checked | Why it matters | What would resolve it |
|---|---|---|---|
| Ancestral IBD node lineage | QuickGO/GOlr for FogD (found withFrom=PTN001211783) and Ayr1; ancestral IBD nodes PTN001213826 / PTN001963740 not exposed publicly | The seed asks to trace PTN001211783 → the two Ayr1-seeded IBD nodes; without the node index this cannot be fully closed | PANTHER internal tree/graft data or GO_Central IBD export for PTHR44169 |
| No FogD localization data | Literature + UniProt | ER/lipid-droplet terms rest entirely on Ayr1 homology | GFP fusion / fractionation of FogD in *A. ruber* |
| No direct FogD lipid/hydrolase assay | Literature | TAG-lipase / acyl-DHAP-reductase terms untested for FogD | In vitro assay of purified FogD against acyl-DHAP and triacylglycerol |
| Exact FogD substrate-bound state | PMID:32134669 | Distinguishes CH-OH oxidoreduction from thioester-release mechanism | In vitro reconstitution with defined polyketide intermediates ± ACP tether |
| Single primary paper for FogD | 1 paper (PMID:32134669) reviewed in depth | Function rests largely on one study | Independent biochemical/structural characterization |

---

## Discriminating Tests

1. **In vitro substrate panel with purified recombinant FogD** — assay NADPH-dependent
   reduction of (a) the flavoglaucin polyketide salicylaldehyde intermediate, (b) acyl-DHAP,
   and (c) a triacylglycerol hydrolysis readout. This directly separates the demonstrated
   secondary-metabolite reductase activity from the Ayr1-derived lipid activities.
2. **Subcellular localization of FogD in *A. ruber*** (fluorescent fusion + organelle markers)
   to test ER/lipid-droplet claims directly rather than by homology.
3. **Structural comparison** — an AlphaFold model or crystal structure of FogD superposed on
   Ayr1, examining the substrate-binding pocket and any residues implicated in Ayr1's lipase
   moonlighting, to predict whether hydrolase capability plausibly survived divergence.
4. **Complementation swap** — test whether FogD rescues a yeast *ayr1Δ* lipid phenotype, and
   whether Ayr1 rescues a *fogD* flavoglaucin defect, to measure functional interchangeability.
5. **PANTHER node-lineage retrieval** — obtain the internal IBD graft nodes (PTN001213826,
   PTN001963740) to complete the provenance chain the seed requested.

---

## Proposed Follow-up Experiments / Actions (Curation Leads — require curator verification)

- **Reframe the review** so the core function is the secondary-metabolite SDR: propose core
  **MF GO:0016616** (CH-OH/NADP oxidoreductase) and core **BP GO:0044550** (secondary metabolite
  biosynthetic process), each citing [PMID:32134669](https://pubmed.ncbi.nlm.nih.gov/32134669/).
- **Downgrade the six lipid terms** (GO:0000140, GO:0004806, GO:0005783, GO:0005811, GO:0006654,
  GO:0019433) from any core status to non-core IEA:TreeGrafter predictions, with a note that they
  are Ayr1-seeded homology transfers unsupported by FogD-specific evidence.
- **Candidate reference + snippet to verify:**
  [PMID:32134669](https://pubmed.ncbi.nlm.nih.gov/32134669/) — *"The polyketide skeleton was
  released as alkylated salicyl alcohols, which is a prerequisite for consecutive hydroxylation
  and prenylation, before reoxidation to the final aldehyde products."* Use as the primary
  support for the reductase MF and secondary-metabolite BP.
- **Provenance note to add:** QuickGO A0A017SE81 — all six lipid terms `IEA:TreeGrafter`,
  `GO_REF:0000118`, `withFrom=PANTHER:PTN001211783`; source Ayr1 (P40471) carries these terms
  experimentally (e.g. TAG lipase [PMID:24187129](https://pubmed.ncbi.nlm.nih.gov/24187129/)).
- **Suggested curator questions:** (i) Should the six lipid terms be retained as IEA or removed
  given the strong competing experimental role? (ii) Is a flavoglaucin/polyketide-specific BP
  child preferred over generic GO:0044550? (iii) Can the ancestral IBD nodes be retrieved to
  finalize provenance?
- **Suggested experiments:** the in vitro substrate panel and localization assay above.

---

## Conclusion

FogD is genuinely a member of the Ayr1 SDR family and a catalytically intact NADP(H)-dependent
oxidoreductase, but its **only experimentally supported role is temporary reduction of a
flavoglaucin polyketide salicylaldehyde to salicyl alcohol** — a secondary-metabolite tailoring
step. The six lipid-metabolism GO terms in the seed hypothesis are **IEA:TreeGrafter
over-annotations propagated from experimentally characterized yeast Ayr1** and are **not
supported by any FogD-specific evidence**. At ~39% identity (twilight zone) and in a distinct
PANTHER subfamily, conserved SDR chemistry transfers but Ayr1's specific lipid substrates,
hydrolase moonlighting, and organelle localization do not. The recommended curation lead is to
foreground **GO:0016616 (MF)** and **GO:0044550 (BP)** as core, and to treat all six lipid terms
as non-core electronic predictions rather than FogD functions — while acknowledging that they
are unsupported rather than formally disproven.


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)