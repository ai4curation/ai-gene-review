---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-24T04:40:32.647901'
end_time: '2026-10-24T05:33:58.387601'
duration_seconds: 3205.74
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: PSEPK
  gene: kguE
  gene_symbol: kguE
  uniprot_accession: Q88HH8
  taxon_id: NCBITaxon:160488
  taxon_label: Pseudomonas putida KT2440
  focus_type: function_assignment
  hypothesis_slug: function-hypothesis-go-0008114
  hypothesis_text: kguE has phosphogluconate 2-dehydrogenase activity (GO:0008114).
  term_context: '- Term: phosphogluconate 2-dehydrogenase activity (GO:0008114)

    - Evidence type: IEA

    - Original reference: GO_REF:0000003'
  reference_context: '- GO_REF:0000003

    - PMID:39770733'
  source_file: genes/PSEPK/kguE/kguE-ai-review.yaml
  source_selector: existing_annotations[1].function_hypothesis
  source_context_yaml: "term:\n  id: GO:0008114\n  label: phosphogluconate 2-dehydrogenase\
    \ activity\nevidence_type: IEA\noriginal_reference_id: GO_REF:0000003"
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
citation_count: 9
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
- filename: provenance_kguE_GO0008114_evidence.md
  path: openscientist_artifacts/provenance_kguE_GO0008114_evidence.md
  media_type: text/markdown
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist kguE GO0008114 evidence
---

## Question

# AIGR Gene Hypothesis Deep Research

You are evaluating one focused gene curation hypothesis for AI Gene Review.
This is not a general gene overview. Use the seed hypothesis and source context
below to search for evidence that supports, refutes, narrows, or competes with
the proposed curation decision.

## Target Gene

- **Organism code:** PSEPK
- **Taxon:** Pseudomonas putida KT2440 (NCBITaxon:160488)
- **Gene directory:** kguE
- **Gene symbol:** kguE
- **UniProt accession:** Q88HH8

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** function-hypothesis-go-0008114
- **Source file:** genes/PSEPK/kguE/kguE-ai-review.yaml
- **Source selector:** existing_annotations[1].function_hypothesis

## Seed Hypothesis

kguE has phosphogluconate 2-dehydrogenase activity (GO:0008114).

## Term and Decision Context

- Term: phosphogluconate 2-dehydrogenase activity (GO:0008114)
- Evidence type: IEA
- Original reference: GO_REF:0000003

## Reference Context

- GO_REF:0000003
- PMID:39770733

## Source Context YAML

```yaml
term:
  id: GO:0008114
  label: phosphogluconate 2-dehydrogenase activity
evidence_type: IEA
original_reference_id: GO_REF:0000003
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

# AIGR Deep Research Report: kguE (Q88HH8) — Phosphogluconate 2-dehydrogenase activity (GO:0008114)

**Organism:** *Pseudomonas putida* KT2440 (NCBITaxon:160488, PSEPK)
**Gene:** kguE | **Locus:** PP_3379 | **UniProt:** Q88HH8
**Hypothesis under review:** *kguE has phosphogluconate 2-dehydrogenase activity (GO:0008114).*
**Focus type:** function_assignment | **Current annotation evidence:** IEA (GO_REF:0000003)

---

## Executive Judgment

**Verdict: REFUTED / over-annotated.**

The seed hypothesis that kguE (Q88HH8) directly possesses **phosphogluconate 2-dehydrogenase activity (GO:0008114, EC 1.1.1.43)** is not supported and should be removed from the gene review. The annotation is a stale, electronically-inferred **ec2go** carry-over (GO_REF:0000003) that originated from a **self-contradictory EMBL/UniProt submission**: the protein is given the submission name "**Epimerase**" yet simultaneously carries EC 1.1.1.43 (6-phospho-D-gluconate:NAD(P)⁺ 2-oxidoreductase). GO_REF:0000003 mechanically converts the submitted EC number into the matching GO molecular-function term, with no evidence that the enzyme actually catalyzes that reaction.

Three independent lines of evidence converge on refutation. **(1) Fold incompatibility:** every signature database maps Q88HH8 to a metal-dependent (β/α)₈ **xylose-isomerase-like TIM barrel** (IPR050312 IolE/XylA/MocC family; IPR036237 superfamily; Gene3D 3.20.20.150; SUPFAM SSF51658; COG1082 "sugar-phosphate isomerases/epimerases"). EC 1.1.1.43 is catalyzed by an **NAD(P)-dependent Rossmann-fold oxidoreductase** — a structurally unrelated fold. Q88HH8 has **no Pfam NAD-binding/Rossmann domain** (no PF03446/PF00393) listed at all. **(2) High-confidence structure:** the AlphaFold model AF-Q88HH8-F1 spans the full 259 aa at mean pLDDT 94.88, a single compact TIM-barrel domain — a genuine metal-dependent isomerase/epimerase, not a fragment or pseudogene, and with no room for a separate cofactor-binding Rossmann lobe. **(3) Family consensus:** a survey of all **75 reviewed (Swiss-Prot)** members of KguE's InterPro family IPR050312 found **zero oxidoreductases** — the family is exclusively EC class 4 (lyases/dehydratases) and class 5 (isomerases/epimerases). EC 1.1.1.43 is biochemically foreign to this family.

Finally, the pathway context identifies where the real EC 1.1.1.43 activity resides. kguE sits in the PtxS-regulated 2-ketogluconate (kgu) operon alongside **kguK** (2-ketogluconokinase) and **kguT** (transporter). The characterized cytoplasmic 2-ketogluconate branch converts 2-ketogluconate → (kinase) → 2-keto-6-phosphogluconate → (**NAD(P)-dependent reductase**) → 6-phosphogluconate. That reductase/dehydrogenase step (the genuine EC 1.1.1.43 chemistry) belongs to a **distinct Rossmann-fold enzyme (KguD-type)**, not to the KguE epimerase. The most likely explanation is that the EC number was mis-attached to the epimerase gene during submission. **Curation lead:** remove GO:0008114; assign a carbohydrate epimerase/isomerase molecular-function term consistent with the "kguE epimerase" identity and the TIM-barrel fold, pending experimental confirmation in [PMID: 39770733](https://pubmed.ncbi.nlm.nih.gov/39770733/).

**Most important caveat:** No direct enzymatic assay of purified KguE exists in the literature reviewed. The refutation rests on strong structural/evolutionary incompatibility and pathway logic rather than a negative activity assay. The precise substrate/product of KguE (its true epimerase/isomerase reaction) remains experimentally undetermined.

---

## Key Findings

### Finding 1 — GO:0008114 is a stale EC2GO carry-over contradicted by the protein's own name and fold family

UniProt **Q88HH8** (kguE, locus PP_3379) carries **no recommended name, no EC number in its name field, and no catalytic-activity or function comment**. Its submission name is literally "**Epimerase**," with EC **1.1.1.43** attached to that submission record. The single molecular-function GO annotation on the entry is **GO:0008114 (phosphogluconate 2-dehydrogenase activity)**, evidence code **IEA**, source tag **UniProtKB-EC** — i.e., the GO_REF:0000003 ec2go mapping that mechanically translates the submitted EC 1.1.1.43 into its corresponding GO term. This is a database pipeline artifact, not an experimental or curator-reviewed assignment.

The domain architecture flatly contradicts a dehydrogenase assignment. Q88HH8's signatures are all consistent with a **metal-dependent (β/α)₈ TIM-barrel isomerase/epimerase**: InterPro **IPR050312** (IolE/XylA/MocC family), **IPR036237** (xylose-isomerase-like superfamily), **Gene3D 3.20.20.150** (divalent-metal-dependent TIM barrel), **SUPFAM SSF51658**, eggNOG **COG1082** ("sugar-phosphate isomerases/epimerases"), and PANTHER **PTHR12110** (hydroxypyruvate isomerase). By contrast, **EC 1.1.1.43** describes a 6-phospho-D-gluconate:NAD(P)⁺ 2-oxidoreductase — an **NAD(P)-dependent Rossmann-fold** enzyme. The TIM barrel and the Rossmann fold are structurally distinct protein architectures with no catalytic overlap; IPR050312 members catalyze inosose dehydration and sugar isomerization/epimerization, reactions that require **no NAD(P) cofactor**. A TIM-barrel metalloenzyme cannot perform NAD(P)-dependent hydride transfer.

### Finding 2 — kguE sits in the PtxS-regulated 2-ketogluconate operon; the EC 1.1.1.43 reductase step belongs to KguD, not KguE

UniProt locus mapping places **kguE (PP_3379)** adjacent to **kguK (PP_3378**, 2-ketogluconokinase, EC 2.7.1.13, Q88HH9), **kguT (PP_3377**, 2-ketogluconate transporter, Q88HI0), and **ptxS (PP_3380**, PtxS regulator, Q88HH7). This is the characterized 2-ketogluconate (kgu) utilization operon.

Daddaoua et al. 2010 ([PMID: 20581202](https://pubmed.ncbi.nlm.nih.gov/20581202/)) describe the cytoplasmic 2-ketogluconate route: the metabolite "is subsequently transported to the cytoplasm, where **two reactions are carried out, giving rise to 6-phosphogluconate**, which enters the Entner-Doudoroff pathway." Those two reactions are a **kinase** (KguK, producing 2-keto-6-phosphogluconate) plus an **NAD(P)-dependent 2-keto-6-phosphogluconate reductase** (the true EC 1.1.1.43 activity, i.e. KguD). del Castillo et al. 2008 ([PMID: 18245293](https://pubmed.ncbi.nlm.nih.gov/18245293/)) assign the 2-ketogluconate utilization genes to the **PtxS regulon**: "PtxS … controls the enzymes for oxidation of gluconate to 2-ketogluconate, its transport and metabolism."

Critically, in UniProt the **only KT2440 protein carrying EC 1.1.1.43 is kguE itself** — and it carries it solely by virtue of its "Epimerase" submission record, not any reductase annotation. This strongly indicates the EC number was **mis-attached to the epimerase gene** rather than to the genuine reductase during genome submission. The true reductase (KguD) is a separate gene product with a Rossmann fold.

### Finding 3 — KguE lacks any NAD(P)-binding/Rossmann domain; AlphaFold confirms a confident single TIM-barrel domain

Q88HH8's signature databases are **exclusively** TIM-barrel/isomerase: Gene3D 3.20.20.150, SUPFAM SSF51658 (xylose-isomerase-like), PANTHER PTHR12110 (hydroxypyruvate isomerase), InterPro IPR050312/IPR036237. **No Pfam domain is even listed**, and — most tellingly — **no NAD-binding/Rossmann signature** (e.g., PF03446 6-phosphogluconate dehydrogenase C-terminal, or PF00393 6-phosphogluconate dehydrogenase NAD-binding) appears anywhere on the entry. Without a cofactor-binding module, EC 1.1.1.43 chemistry is mechanistically impossible.

The **AlphaFold model AF-Q88HH8-F1** covers the full 259 aa at **mean pLDDT 94.88** (very high confidence), depicting a single compact domain consistent with a real metal-dependent (β/α)₈ TIM-barrel enzyme — not a truncated fragment or degraded pseudogene. There is no second domain into which a Rossmann NAD(P)-binding lobe could fit.

In KT2440, the genuine 6-phosphogluconate-dehydrogenase / β-hydroxyacid-dehydrogenase family (Pfam **PF03446**) comprises **distinct genes** — mmsB/PP_4666, glxR/PP_4299, gntZ/PP_4043 (EC 1.1.1.44), PP_2798, PP_1143 — and **kguE is not among them**. del Castillo et al. 2007 ([PMID: 17483213](https://pubmed.ncbi.nlm.nih.gov/17483213/)) confirm the step is a reductase: periplasmic glucose-derived 2-ketogluconate "is transported to the cytoplasm, and subsequently **phosphorylated and reduced to 6-phosphogluconate**," locating the EC 1.1.1.43 chemistry in an NAD(P)-dependent reductase distinct from any epimerase.

### Finding 4 — Zero of 75 characterized family homologs is an oxidoreductase

A systematic survey of **all 75 reviewed (Swiss-Prot) UniProt entries** in KguE's InterPro family **IPR050312** (IolE/XylA/MocC) reveals a strong functional consensus that excludes oxidoreductase activity:

| Recommended-name class | Count |
|---|---|
| Inosose dehydratase (EC 4.2.1.44) | 36 |
| 3-dehydroshikimate dehydratase | 4 |
| Inosose isomerase | 4 |
| Ketose/sugar 3-epimerases (fructoselysine/D-psicose/D-tagatose/L-ribulose) | multiple |

The EC numbers present across the family are **exclusively class 4 (lyases)** — EC 4.2.1.44 (×38), 4.2.1.118 (×4), 4.1.99.-, 4.1.1.120 — and **class 5 (isomerases/epimerases)** — EC 5.3.99.11 (×4), 5.1.3.41, 5.1.3.30, 5.1.3.31, 5.1.3.35, 5.3.1.36, 5.1.3.-. **EC 1.1.1.43 — and indeed any EC class 1 oxidoreductase — is entirely ABSENT from the reviewed family (0/75).** This is exactly what the metal-dependent (β/α)₈ TIM-barrel mechanism predicts: these enzymes perform acid/base-catalyzed isomerization, epimerization, and dehydration using a divalent metal, never NAD(P)-dependent hydride transfer. The gene symbol **kguE** ("E" for epimerase) and the submission name "Epimerase" are consistent with the family consensus — and inconsistent with the dehydrogenase annotation.

---

## Mechanistic Model / Interpretation

The 2-ketogluconate (kgu) branch of peripheral glucose catabolism in *P. putida* KT2440 funnels oxidized glucose derivatives into the Entner-Doudoroff pathway via 6-phosphogluconate. The genomic neighborhood and biochemical logic are:

```
 Periplasm                           Cytoplasm (kgu operon, PtxS-regulated)
 ---------                           --------------------------------------
 glucose --(Gcd)--> gluconate
   gluconate --(Gad)--> 2-ketogluconate
                         |
                    kguT (PP_3377, transporter)
                         v
          2-ketogluconate ---- kguK (PP_3378, kinase, EC 2.7.1.13) ---->
             2-keto-6-phosphogluconate
                         |
                    KguD-type reductase  <==  GENUINE EC 1.1.1.43
                    (Rossmann fold, NAD(P)-dependent)
                         v
             6-phosphogluconate ---> Entner-Doudoroff pathway

          kguE (PP_3379)  =  "Epimerase", TIM-barrel (COG1082/IPR050312)
                            NOT a dehydrogenase; true reaction = sugar
                            epimerization/isomerization (substrate TBD)

          ptxS (PP_3380)  =  LacI-family repressor controlling the operon
```

The annotation error arises from a single point of failure: during EMBL submission, the EC number **1.1.1.43** (which properly belongs to the pathway's reductase, KguD) was attached to the **"Epimerase" (kguE)** record. GO_REF:0000003 then mechanically propagated this via ec2go into GO:0008114. Every downstream line of evidence — fold family, absence of a Rossmann/NAD-binding domain, the high-confidence TIM-barrel AlphaFold model, and the unanimous isomerase/epimerase/lyase character of 75 reviewed family members — shows the enzyme cannot catalyze NAD(P)-dependent 2-dehydrogenation. KguE's true molecular function is almost certainly a **carbohydrate epimerase or isomerase** (consistent with its name and fold), with the specific substrate still to be determined experimentally.

### Fold / mechanism comparison

| Property | EC 1.1.1.43 (annotated) | KguE (observed signatures) |
|---|---|---|
| Fold | Rossmann (NAD(P)-binding) | (β/α)₈ TIM barrel |
| Superfamily / InterPro | 6-PGDH-like (PF03446/PF00393) | Xylose-isomerase-like (IPR036237) |
| Cofactor | NAD(P)⁺/NAD(P)H | Divalent metal (no NAD(P)) |
| Reaction class | Oxidoreductase (EC 1) | Isomerase/epimerase/lyase (EC 5/4) |
| Present in Q88HH8? | **No domain signature** | **All signatures** |
| AlphaFold | — | Single domain, pLDDT 94.88 |

---

## Evidence Base

| Citation | Evidence type | Supports/Refutes/Qualifies | Claim tested | Key finding | Context | Confidence & limitations |
|---|---|---|---|---|---|---|
| UniProt Q88HH8 record | Database/computational | **Refutes** | Origin of GO:0008114 | Submission name "Epimerase"; EC 1.1.1.43 attached; only MF GO is IEA/ec2go; signatures all TIM-barrel; no Rossmann domain | *P. putida* KT2440, PP_3379 | High for provenance; database-level |
| AlphaFold AF-Q88HH8-F1 | Structural/computational | **Refutes** | Does KguE have a cofactor-binding Rossmann lobe? | Single compact TIM barrel, 259 aa, mean pLDDT 94.88; no second domain | In silico model | High-confidence model; not an experimental structure |
| InterPro IPR050312 family survey (75 Swiss-Prot entries) | Structural/evolutionary | **Refutes** | Is oxidoreductase activity found in this family? | 0/75 are EC class 1; all are EC 4 (lyase) or EC 5 (isomerase/epimerase) | Cross-organism reviewed set | High; family-wide consensus |
| [PMID: 20581202](https://pubmed.ncbi.nlm.nih.gov/20581202/) Daddaoua 2010 | Primary pathway/mutant | **Qualifies (competing)** | Where is the 6-PG-forming activity? | Two cytoplasmic reactions (kinase + reductase) form 6-phosphogluconate | *P. putida* KT2440 | High; locates EC 1.1.1.43 in reductase, not epimerase |
| [PMID: 18245293](https://pubmed.ncbi.nlm.nih.gov/18245293/) del Castillo 2008 | Primary regulatory | **Qualifies** | Operon/regulatory context | PtxS controls gluconate→2-ketogluconate oxidation, transport, metabolism | *P. putida* KT2440 | High; establishes kgu operon context |
| [PMID: 17483213](https://pubmed.ncbi.nlm.nih.gov/17483213/) del Castillo 2007 | Primary genomic/flux | **Qualifies (competing)** | Nature of the 6-PG-forming step | 2-ketogluconate is "phosphorylated and reduced to 6-phosphogluconate" (reductase) | *P. putida* KT2440 | High; confirms reductase, not epimerase |
| [PMID: 39770733](https://pubmed.ncbi.nlm.nih.gov/39770733/) Sun 2024 | Primary (operon characterization) | **Pending** | kgu operon function & regulation | Characterizes 2-ketogluconate utilization operon (no abstract retrieved) | *P. putida* | Primary source to verify KguE's true role |

**Supporting literature orientation (gluconate/2-ketogluconate physiology):** [PMID: 39261865](https://pubmed.ncbi.nlm.nih.gov/39261865/), [PMID: 31931111](https://pubmed.ncbi.nlm.nih.gov/31931111/), [PMID: 28921555](https://pubmed.ncbi.nlm.nih.gov/28921555/), [PMID: 23967821](https://pubmed.ncbi.nlm.nih.gov/23967821/), [PMID: 21513516](https://pubmed.ncbi.nlm.nih.gov/21513516/) — these establish the physiological importance of the 2-ketogluconate loop but do not assign dehydrogenase activity to KguE.

---

## GO Curation Implications

**Likely curation action (lead requiring curator verification):**

1. **Remove / do not retain GO:0008114** (phosphogluconate 2-dehydrogenase activity, MF) on kguE/Q88HH8. The annotation is an IEA ec2go artifact (GO_REF:0000003) propagated from a self-contradictory submission and is contradicted by fold family, absence of a Rossmann/NAD-binding domain, the high-confidence TIM-barrel AlphaFold model, and the complete absence of oxidoreductases among 75 reviewed family homologs.

2. **Reassign a more defensible molecular-function term.** The evidence supports a **carbohydrate epimerase or isomerase** activity (MF), consistent with the "Epimerase" submission name, the kguE symbol, and the IPR050312/COG1082 TIM-barrel family. A conservative lead is a **racemase/epimerase or intramolecular isomerase acting on carbohydrates** term; the exact child term should await identification of the substrate (see Knowledge Gaps). Do **not** default to "protein binding."

3. **Biological process context (BP):** retain/associate kguE with **2-ketogluconate / carbohydrate catabolic process** given its operon membership, but flag that its specific enzymatic step within that process is unconfirmed.

4. The genuine **EC 1.1.1.43 / GO:0008114** activity should be associated with the **KguD-type Rossmann-fold reductase**, not kguE — a cross-reference worth noting for the curator.

---

## Mechanistic Scope

The immediate molecular function being tested is a **direct catalytic activity**: whether the KguE polypeptide catalyzes the NAD(P)-dependent oxidation of 6-phospho-D-gluconate (EC 1.1.1.43). This is a gene-product–intrinsic claim, not a downstream phenotype. The refutation is therefore at the most direct level — the protein's fold and domain composition make the stated chemistry mechanistically impossible — rather than relying on loss-of-function phenotypes or pathway inferences. The pathway/operon evidence (Findings 2–3) is supporting context that correctly relocates the EC 1.1.1.43 reaction to a separate reductase, but the core refutation stands on the structural/evolutionary incompatibility of KguE itself.

No disease, developmental, or pleiotropic manifestations are relevant here; this is a bacterial metabolic enzyme annotation.

---

## Conflicts and Alternatives

- **Database carry-over (primary alternative, confirmed):** The GO:0008114 annotation is best explained as an ec2go artifact from a submission that mislabels the epimerase with the reductase's EC number. This is the most parsimonious explanation and is directly supported by the structure of the UniProt record.
- **Paralog / step confusion:** The real EC 1.1.1.43 chemistry belongs to a co-pathway reductase (KguD-type, Rossmann fold). The annotation likely "jumped" from the reductase gene to the epimerase gene during submission.
- **No competing evidence for dehydrogenase activity:** No primary paper, assay, or structure assigns NAD(P)-dependent dehydrogenase activity to KguE. There is no in vitro–only activity claim to weigh.
- **Residual uncertainty about KguE's true reaction:** While "epimerase/isomerase" is strongly indicated, the specific substrate is not experimentally pinned down. It is conceivable (though not evidenced) that KguE acts on a sugar/sugar-phosphate intermediate elsewhere in peripheral metabolism rather than directly in the 2-keto-6-phosphogluconate step.

---

## Limitations and Knowledge Gaps

1. **No direct enzymatic assay of purified KguE.** The refutation is structural/evolutionary and contextual, not a negative activity measurement. *Checked:* literature search returned no biochemical characterization of purified Q88HH8. *Why it matters:* a positive identification of KguE's true substrate would let a curator assign a precise MF term. *Resolution:* purify KguE and test candidate epimerase/isomerase substrates.

2. **KguE's exact substrate and reaction are unknown.** *Checked:* family survey narrows it to epimerase/isomerase/dehydratase chemistry on a sugar or sugar-phosphate. *Why it matters:* the replacement GO term's specificity depends on this. *Resolution:* metabolomics of a ΔkguE mutant; in vitro substrate screening.

3. **PMID:39770733 (Sun 2024) abstract not retrieved.** *Checked:* no abstract available via the search. *Why it matters:* this is the most recent, directly relevant primary characterization of the kgu operon and may explicitly state KguE's role. *Resolution:* obtain and read the full text; it is the single highest-value document for this curation.

4. **AlphaFold is a model, not an experimental structure.** *Checked:* high pLDDT (94.88) gives strong confidence, but no crystal/cryo-EM structure confirms the active-site metal or substrate. *Resolution:* experimental structure or at least docking of candidate substrates.

---

## Discriminating Tests

1. **In vitro activity assay of purified KguE for EC 1.1.1.43:** measure NAD(P)⁺-dependent oxidation of 6-phospho-D-gluconate. Expected result if hypothesis is refuted: **no activity** (no cofactor site). This is the single most decisive experiment.
2. **ΔkguE vs ΔkguD complementation on 2-ketogluconate:** if KguD alone restores 6-phosphogluconate formation and ΔkguE does not block the reductase step, the EC 1.1.1.43 activity is confirmed in KguD.
3. **Epimerase/isomerase substrate screen** against candidate sugar-phosphates to positively identify KguE's true reaction and enable a precise MF term.
4. **Structure-guided active-site analysis** (metal-coordinating residues in the TIM barrel vs. absent NAD(P)-binding motif) to formally confirm cofactor incompatibility.
5. **Read PMID:39770733 full text** for any direct functional assignment of KguE within the characterized operon.

---

## Proposed Follow-up Actions (Curation Leads)

*All leads below require curator verification.*

- **Action change:** Remove **GO:0008114 (phosphogluconate 2-dehydrogenase activity)** from kguE/Q88HH8 — classify as an incorrect IEA ec2go carry-over (GO_REF:0000003).
- **Candidate replacement GO term(s):** A carbohydrate **epimerase/isomerase** molecular-function term consistent with family IPR050312 and the "Epimerase" submission name (await substrate identification before selecting the most specific child). Retain association with a **2-ketogluconate / carbohydrate catabolic process** BP term, flagged as unresolved at the step level.
- **Candidate references & snippets to verify:**
  - [PMID: 20581202](https://pubmed.ncbi.nlm.nih.gov/20581202/): *"two reactions are carried out, giving rise to 6-phosphogluconate, which enters the Entner-Doudoroff pathway"* — locates the EC 1.1.1.43 reductase step away from the epimerase.
  - [PMID: 17483213](https://pubmed.ncbi.nlm.nih.gov/17483213/): *"transported to the cytoplasm, and subsequently phosphorylated and reduced to 6-phosphogluconate"* — confirms a reductase, not an epimerase, performs the 6-PG-forming step.
  - [PMID: 18245293](https://pubmed.ncbi.nlm.nih.gov/18245293/): *"PtxS … controls the enzymes for oxidation of gluconate to 2-ketogluconate, its transport and metabolism"* — operon/regulon context.
  - [PMID: 39770733](https://pubmed.ncbi.nlm.nih.gov/39770733/): primary kgu-operon characterization — verify for any direct KguE functional statement.
- **Suggested curator questions:** (a) Does the submitting authors' EC 1.1.1.43 belong to KguD rather than KguE? (b) Is there any experimental substrate for KguE? (c) Should the EC 1.1.1.43 annotation be transferred to the KguD-type reductase locus?
- **Suggested experiments:** in vitro EC 1.1.1.43 assay of purified KguE (expected negative); ΔkguE metabolomics and substrate screening to define the true epimerase/isomerase reaction.

---

## Conclusion

The hypothesis that **kguE directly has phosphogluconate 2-dehydrogenase activity (GO:0008114)** is **refuted / over-annotated**. The annotation is an electronic ec2go artifact from a self-contradictory submission. KguE is a high-confidence metal-dependent TIM-barrel enzyme of the xylose-isomerase-like family (IPR050312/COG1082) with no NAD(P)-binding domain; its entire characterized family (0/75 reviewed members are oxidoreductases) performs isomerase/epimerase/lyase chemistry, and the genuine EC 1.1.1.43 reductase step in the 2-ketogluconate pathway belongs to a separate Rossmann-fold KguD enzyme. The recommended curation action is to remove GO:0008114 and assign a carbohydrate epimerase/isomerase molecular-function term, pending experimental substrate identification.


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)
- [OpenScientist kguE GO0008114 evidence](openscientist_artifacts/provenance_kguE_GO0008114_evidence.md)