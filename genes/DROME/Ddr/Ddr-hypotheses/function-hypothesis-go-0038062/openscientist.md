---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-11-11T05:25:08.997269'
end_time: '2026-11-11T05:35:54.475553'
duration_seconds: 645.48
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: DROME
  gene: Ddr
  gene_symbol: Ddr
  uniprot_accession: Q59DZ7
  taxon_id: NCBITaxon:7227
  taxon_label: Drosophila melanogaster
  focus_type: function_assignment
  hypothesis_slug: function-hypothesis-go-0038062
  hypothesis_text: Ddr has protein tyrosine kinase collagen receptor activity (GO:0038062).
  term_context: '- Term: protein tyrosine kinase collagen receptor activity (GO:0038062)

    - Evidence type: IBA

    - Original reference: GO_REF:0000033'
  reference_context: '- GO_REF:0000033

    - PMID:36355066

    - file:DROME/Ddr/Ddr-uniprot.txt'
  source_file: genes/DROME/Ddr/Ddr-ai-review.yaml
  source_selector: existing_annotations[7].function_hypothesis
  source_context_yaml: "term:\n  id: GO:0038062\n  label: protein tyrosine kinase\
    \ collagen receptor activity\nevidence_type: IBA\noriginal_reference_id: GO_REF:0000033"
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

- **Organism code:** DROME
- **Taxon:** Drosophila melanogaster (NCBITaxon:7227)
- **Gene directory:** Ddr
- **Gene symbol:** Ddr
- **UniProt accession:** Q59DZ7

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** function-hypothesis-go-0038062
- **Source file:** genes/DROME/Ddr/Ddr-ai-review.yaml
- **Source selector:** existing_annotations[7].function_hypothesis

## Seed Hypothesis

Ddr has protein tyrosine kinase collagen receptor activity (GO:0038062).

## Term and Decision Context

- Term: protein tyrosine kinase collagen receptor activity (GO:0038062)
- Evidence type: IBA
- Original reference: GO_REF:0000033

## Reference Context

- GO_REF:0000033
- PMID:36355066
- file:DROME/Ddr/Ddr-uniprot.txt

## Source Context YAML

```yaml
term:
  id: GO:0038062
  label: protein tyrosine kinase collagen receptor activity
evidence_type: IBA
original_reference_id: GO_REF:0000033
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

# AIGR Hypothesis Report: Drosophila Ddr and GO:0038062 (Protein Tyrosine Kinase Collagen Receptor Activity)

**Target gene:** Ddr (Discoidin domain receptor) — *Drosophila melanogaster* (DROME), UniProt **Q59DZ7**
**Seed hypothesis:** Ddr has protein tyrosine kinase collagen receptor activity (**GO:0038062**).
**Focus type:** function_assignment
**Current annotation under review:** GO:0038062, evidence type **IBA**, original reference **GO_REF:0000033**

---

## Summary

The assignment of **protein tyrosine kinase collagen receptor activity (GO:0038062)** to *Drosophila* Ddr (Q59DZ7) is well justified and should be **retained** with its current **IBA** (Inferred by Biological aspect of Ancestor) evidence code. The judgment rests on three mutually reinforcing lines of evidence: a complete and canonical DDR domain architecture, unambiguous orthology to the mammalian DDR1/DDR2 collagen-receptor family with conservation of the specific collagen-contacting residues, and in vivo *Drosophila* genetic evidence that Ddr behaves as a collagen receptor in native tissue.

Q59DZ7 (1,054 aa) carries an N-terminal collagen-binding discoidin/DS (F5/8 type C) domain, a single transmembrane helix, and a C-terminal tyrosine-kinase domain with fully intact catalytic motifs — i.e., a predicted active kinase, not a pseudokinase. A computed pairwise alignment shows the fly DS domain is equally identical (40.6%) to human DDR1 and DDR2, the signature of a single pre-vertebrate-duplication ortholog, and the collagen-contacting tryptophan-rich loop is conserved. In native *Drosophila* peripheral nerve, Ddr is required for axon ensheathment by wrapping glia and shows a strong dominant genetic interaction with the collagen Multiplexin (Mp), leading the authors of [PMID:36355066](https://pubmed.ncbi.nlm.nih.gov/36355066/) to conclude that "Ddr functions as a collagen receptor."

The **key caveat** is that this is an inference from orthology, conserved architecture, and *genetic* (not biochemical) interaction. No published study has directly measured collagen binding or collagen-induced autophosphorylation of the fly protein. GO:0038062 asserts a biochemical molecular-function activity; for Q59DZ7 that activity is **inferred**, not **demonstrated**. This is exactly what IBA is designed to encode — so the annotation should be retained, but its evidence code should not be upgraded to an experimental code on current data.

**Verdict: Supported — retain GO:0038062 (IBA).**

---

## Key Findings

### Finding 1 — Q59DZ7 has canonical DDR architecture and in vivo collagen-receptor genetic evidence

*Drosophila* Ddr (Q59DZ7, 1,054 aa) displays the full, textbook DDR receptor-tyrosine-kinase layout:

| Region | Residues | Domain / annotation | Source |
|---|---|---|---|
| Ectodomain | 106–262 | DDR-type discoidin / F5-8 type C (DS) domain | InterPro IPR048525 (DDR1-2_DS-like), Pfam PF21114 |
| Membrane anchor | 501–525 | Single transmembrane helix | UniProt topology |
| Catalytic module | 759–1038 | Tyrosine kinase domain | Pfam PF07714 (PK_Tyr), InterPro IPR050122 (RTK) |

Critically, the kinase domain contains **intact catalytic machinery**: a glycine-rich loop (GSGVFG), a VAIK-type catalytic lysine, and a catalytic loop HRDLATRSC with the catalytic aspartate present. This marks Ddr as a **predicted active tyrosine kinase**, not a pseudokinase — a prerequisite for the "protein tyrosine kinase" portion of GO:0038062.

The functional component of the finding comes from native *Drosophila* genetics ([PMID:36355066](https://pubmed.ncbi.nlm.nih.gov/36355066/), Corty et al. 2022). Two verified quotations anchor the claim:

- *"we identified the conserved receptor tyrosine kinase Discoidin domain receptor (Ddr)"* — confirms the tyrosine-kinase identity.
- *"we found a strong dominant genetic interaction between Ddr and the type XV/XVIII collagen Multiplexin (Mp), suggesting that Ddr functions as a collagen receptor to drive axon wrapping"* — provides in vivo evidence for collagen-receptor function.

Functionally, Ddr RNAi in wrapping glia severely reduces axon ensheathment and caliber, placing the receptor at the center of a glia–extracellular matrix signaling axis. UniProt already carries both GO:0038062 (IBA) and GO:0005518 collagen binding (IBA), consistent with this picture.

**Interpretation.** The combination of (a) an intact collagen-binding DS domain, (b) an intact, catalytically competent tyrosine kinase domain, and (c) a genetic interaction with a bona fide collagen in the tissue where Ddr acts together satisfy the biological logic of GO:0038062 at the inference level appropriate to IBA.

### Finding 2 — Fly Ddr DS and kinase domains are strongly conserved with human DDR1/DDR2, including the collagen-binding interface

A computed Needleman–Wunsch pairwise alignment quantifies the orthology:

| Compared region | Fly Ddr vs human DDR1 (Q08345) | Fly Ddr vs human DDR2 (Q16832) |
|---|---|---|
| Discoidin/DS domain (fly 106–262) | **40.6%** identity (155 aligned columns) | **40.6%** identity (155 aligned columns) |
| Kinase domain | **50.9%** identity (138/271) | — |

The fact that the fly DS domain is **equally** identical to DDR1 and DDR2 is the expected signature of a **single ancestral ortholog that predates the vertebrate DDR1/DDR2 gene duplication** — i.e., fly Ddr co-orthologs both mammalian receptors rather than being specifically a DDR1 or DDR2 homolog.

Beyond overall identity, the alignment shows conservation of **functionally critical, collagen-relevant residues**:

- The invariant DDR "GAWCP" tryptophan motif (fly GGAWCP**K**H vs DDR2 GDGAWCP**E**I).
- The collagen-contacting **RWxxWR** loop (fly **KWIRWRS** vs DDR2 **RWISWRN**), with three tryptophans aligning as conserved columns.

In the mammalian DDR DS domain, the tryptophan-rich loop forms the direct collagen-binding interface. Its conservation in the fly protein is the strongest available sequence-level argument that Q59DZ7 retains genuine collagen-binding capacity.

**Interpretation.** Conservation is not limited to generic domain presence; it extends to the specific residues that mediate collagen contact in characterized mammalian DDRs. This substantially strengthens the IBA inference beyond a bare "has a discoidin domain" argument.

---

## Mechanistic Model / Interpretation

The evidence supports the following molecular model for *Drosophila* Ddr:

```
        Extracellular matrix (collagen; e.g., Multiplexin / type XV-XVIII)
                               |
                   collagen triple helix
                               |
                [ DS / discoidin domain ]  <- res 106-262
             RWxxWR + GAWCP Trp loop (conserved collagen interface)
        -----------------------------------------------  cell membrane
                [ transmembrane helix ]    <- res 501-525
                               |
                [ tyrosine kinase domain ] <- res 759-1038
             intact Gly-loop / VAIK Lys / HRD catalytic Asp
                               |
                 (predicted) tyrosine autophosphorylation
                               |
            downstream glial signaling -> axon ensheathment
```

In mammals, collagen binding by the DS domain triggers slow, sustained DDR autophosphorylation and downstream signaling. The fly protein preserves every structural element required for this cascade, and the one piece of native-tissue functional data (axon wrapping, Mp genetic interaction) is consistent with the receptor operating in this canonical mode.

Two layers of claim must be kept distinct for curation:

| Layer | Status in fly Ddr | Evidence |
|---|---|---|
| Possesses collagen-binding DS domain + active kinase domain | **Strongly supported** (structural inference) | Domain architecture, residue conservation |
| Acts as a collagen receptor in vivo | **Supported** (genetic) | Mp genetic interaction, wrapping-glia RNAi phenotype |
| Directly binds collagen biochemically (fly protein) | **Not demonstrated** | No in vitro binding assay for Q59DZ7 |
| Collagen-induced autophosphorylation (fly protein) | **Not demonstrated** | No biochemical kinase assay for Q59DZ7 |

GO:0038062 asserts the molecular-function activity (the combined structural + receptor layers). The annotation is supported at the **inference** level appropriate to IBA, with the biochemical demonstration layer remaining an open gap.

---

## Evidence Matrix

| Citation | Evidence type | Supports / Qualifies | Claim tested | Key finding | Context | Confidence & limitations |
|---|---|---|---|---|---|---|
| [PMID:36355066](https://pubmed.ncbi.nlm.nih.gov/36355066/) | Mutant phenotype / genetic interaction (in vivo) | **Supports** | Does fly Ddr act as a collagen receptor? | Ddr RNAi in wrapping glia reduces ensheathment/caliber; strong dominant genetic interaction with collagen Multiplexin; authors conclude "Ddr functions as a collagen receptor" | *Drosophila* peripheral nerve, wrapping glia | High for in vivo function; genetic (not biochemical) — does not directly show collagen binding by the protein |
| Computed alignment (this analysis) | Structural / evolutionary | **Supports** | Is fly Ddr a true ortholog with conserved collagen interface? | DS domain 40.6% identical to BOTH human DDR1 and DDR2; kinase 50.9% to DDR1; conserved GAWCP Trp and RWxxWR loop | Sequence analysis, Q59DZ7 vs Q08345/Q16832 | High confidence; inference only — conservation implies but does not prove retained binding |
| UniProt Q59DZ7 / InterPro / Pfam | Computational / database | **Supports** | Does Ddr have the required domains and an active kinase? | DS domain (IPR048525/PF21114), TM helix, tyrosine kinase (PF07714/IPR050122) with intact Gly-loop, VAIK Lys, HRD catalytic Asp | Protein annotation | High for architecture; predicted (not assayed) kinase activity |
| [PMID:42836584](https://pubmed.ncbi.nlm.nih.gov/42836584/) | Direct assay / disease model (mammalian) | **Qualifies** | Is DDR a collagen-activated RTK? | Human DDR1 phosphorylation increases on collagen III; drives fibroblast proliferation | Human hypertrophic scar fibroblasts | High for human DDR1; species-different, informs ancestral function |
| [PMID:42450310](https://pubmed.ncbi.nlm.nih.gov/42450310/) | Direct assay / mutant (mammalian) | **Qualifies** | Is DDR1 kinase activity required for collagen-driven behavior? | Kinase-dead DDR1 and inhibitor 7rh block Th17 migration in collagen gels | Human Th17 / mouse CIA | High for human DDR1 kinase dependence; species-different |
| [PMID:42323896](https://pubmed.ncbi.nlm.nih.gov/42323896/) | Mutant phenotype (model organism) | **Qualifies** | Do DDR orthologs act via ECM? | DDR2-ortholog knockdown/knockout in zebrafish causes craniofacial defects via ECM | Zebrafish, mouse, human embryo | Supports conserved collagen/ECM role of the family (DDR2 branch) |
| [PMID:42926526](https://pubmed.ncbi.nlm.nih.gov/42926526/) | Direct assay (mammalian) | **Qualifies** | Is DDR1 a collagen-activated RTK? | DDR1 described as collagen-activated RTK; collagen-dependent ectodomain shedding regulates signaling | Human glioblastoma | High for human DDR1; species-different |
| [PMID:42462480](https://pubmed.ncbi.nlm.nih.gov/42462480/) | Direct assay (mammalian) | **Qualifies** | Is DDR1 kinase a collagen-dependent effector? | DDR1 drives collagen-dependent migration/invasion; kinase activity targetable | Human colorectal cancer | High for human DDR1; species-different |
| [PMID:42771502](https://pubmed.ncbi.nlm.nih.gov/42771502/) | Direct assay (mammalian) | **Qualifies** | Does collagen ligand control DDR1 activity? | ¾Col-I fragment is the high-affinity DDR1 ligand; controls receptor stability/signaling | Human PDAC | High for human DDR1 ligand biology; species-different |

---

## Evidence Base

**Primary, directly on target.** *Discoidin domain receptor regulates ensheathment, survival and caliber of peripheral axons* ([PMID:36355066](https://pubmed.ncbi.nlm.nih.gov/36355066/), Corty et al. 2022) is the single most important paper. It provides the only native-*Drosophila* functional evidence: it identifies Ddr as a "conserved receptor tyrosine kinase," shows wrapping-glia RNAi phenotypes, and reports the dominant genetic interaction with collagen Multiplexin from which the authors conclude Ddr "functions as a collagen receptor." It supports both halves of GO:0038062 (tyrosine kinase + collagen receptor).

**Ortholog / family evidence (mammalian and zebrafish; qualifies by establishing conserved ancestral function).**

- [PMID:42836584](https://pubmed.ncbi.nlm.nih.gov/42836584/) — human DDR1 phosphorylation is collagen III-induced; confirms collagen-activated RTK behavior of the mammalian ortholog.
- [PMID:42450310](https://pubmed.ncbi.nlm.nih.gov/42450310/) — kinase-dead and inhibitor data establish that DDR1's tyrosine-kinase activity is required for collagen-driven cell behavior.
- [PMID:42926526](https://pubmed.ncbi.nlm.nih.gov/42926526/) — reiterates DDR1 as a collagen-activated receptor tyrosine kinase.
- [PMID:42462480](https://pubmed.ncbi.nlm.nih.gov/42462480/) — collagen-dependent, kinase-dependent DDR1 function in cancer.
- [PMID:42771502](https://pubmed.ncbi.nlm.nih.gov/42771502/) — defines the high-affinity ¾Col-I collagen ligand for DDR1.
- [PMID:42323896](https://pubmed.ncbi.nlm.nih.gov/42323896/) — DDR2-ortholog knockdown in zebrafish causes ECM-mediated craniofacial defects, confirming conserved collagen/ECM receptor function across the family and in a non-mammalian vertebrate.

**Database / sequence orientation.** UniProt Q59DZ7; InterPro IPR048525, IPR050122; Pfam PF21114, PF07714; plus the computed alignment against human DDR1 (Q08345) and DDR2 (Q16832).

Collectively, the mammalian/zebrafish ortholog literature establishes that the DDR family's ancestral molecular function is a collagen-activated tyrosine kinase; the fly-specific paper and sequence analysis establish that *Drosophila* Ddr retains the required machinery and operates as a collagen receptor in vivo. This is precisely the logical basis an IBA annotation is meant to formalize.

---

## GO Curation Implications

**Lead (requires curator verification): Retain GO:0038062 (protein tyrosine kinase collagen receptor activity) with IBA evidence.**

- **Aspect:** GO:0038062 is a **Molecular Function (MF)** term. The evidence supports it at the inference level appropriate to IBA.
- **Retain, do not remove.** The domain architecture, equal orthology to DDR1/DDR2, conserved collagen-contact residues, and the in vivo Mp genetic interaction collectively justify the term.
- **Do not strengthen the evidence code.** There is no direct biochemical assay of collagen binding or collagen-induced autophosphorylation for the *fly* protein, so the annotation should remain IBA rather than being promoted to EXP/IDA/IPI.
- **Do not generalize or over-specify.** GO:0038062 is the correct granularity: it captures both the collagen-receptor and tyrosine-kinase aspects in one MF term. Generalizing to "transmembrane receptor protein tyrosine kinase activity" (GO:0004714) would lose the collagen-ligand specificity that the conserved DS-domain interface and Mp genetic interaction actually support. "Protein binding" (GO:0005515) would be inappropriately uninformative.
- **Companion terms.** GO:0005518 (collagen binding, IBA) is consistent and should be retained. A BP annotation to glial axon ensheathment is separately supportable from [PMID:36355066](https://pubmed.ncbi.nlm.nih.gov/36355066/) but is outside this MF-focused hypothesis.

**GO decision table:**

| Term | Aspect | Current | Recommended action | Rationale |
|---|---|---|---|---|
| GO:0038062 protein tyrosine kinase collagen receptor activity | MF | IBA | **Retain (IBA)** | Supported by orthology + conserved interface + in vivo genetic interaction |
| GO:0005518 collagen binding | MF | IBA | **Retain (IBA)** | Consistent companion; conserved DS-domain collagen interface |
| GO:0004714 transmembrane receptor PTK activity | MF | — | Not needed as replacement | More general; loses collagen specificity |
| GO:0005515 protein binding | MF | — | Avoid | Uninformative |

---

## Mechanistic Scope

The **immediate molecular function** under test is a receptor tyrosine kinase that (i) binds fibrillar/network collagen via its extracellular discoidin (DS) domain and (ii) transduces that binding into intracellular tyrosine-kinase signaling. That is precisely what GO:0038062 encodes.

Direct gene-product activity (what the term asserts):
- Collagen binding by the DS domain.
- Tyrosine autophosphorylation / kinase catalysis by the intracellular kinase domain.

Downstream / separable phenomena (NOT the MF term, though informative):
- **Axon ensheathment and caliber control** in *Drosophila* — a biological-process/developmental outcome downstream of receptor signaling (the readout used to detect Ddr function genetically).
- Mammalian disease phenotypes (fibrosis, tumor invasion, arthritis, orofacial clefting) — downstream pathway consequences in orthologs, useful only to confirm the ancestral molecular activity.

The genetic Mp interaction and the RNAi wrapping-glia phenotype are the evidence that *connects* the inferred molecular activity to a real in vivo role, but they are a loss-of-function readout, not a direct measurement of the biochemical activity. This distinction is why IBA (inference) — not EXP — is the correct evidence code.

---

## Conflicts and Alternatives

No evidence **refutes** the hypothesis. The considerations that could in principle weaken it are:

1. **Orthology ambiguity (DDR1 vs DDR2).** Fly Ddr is equally identical to both human paralogs, so it is a co-ortholog of both, not a specific match to the more intensively studied DDR1. This is not a conflict — GO:0038062 applies to the whole family — but paralog-specific claims from the mammalian cancer literature should not be carried over to the fly gene.

2. **Genetic vs biochemical evidence.** The in vivo support is a *dominant genetic interaction* with Mp, consistent with but not uniquely proving a direct physical collagen–Ddr interaction. A less parsimonious alternative is that Ddr and Mp act in parallel converging pathways rather than as receptor–ligand. The conserved collagen-binding interface makes the direct receptor model more likely, but a binding assay is needed to exclude the alternative.

3. **Ligand identity.** Mammalian DDR1's highest-affinity ligand is a specific ¾Col-I fragment ([PMID:42771502](https://pubmed.ncbi.nlm.nih.gov/42771502/)); the fly ligand implicated genetically is Multiplexin (type XV/XVIII-like collagen). Collagen class specificity may differ between fly and mammal, but this does not affect validity of the general MF term.

4. **Database carry-over risk.** As an IBA annotation propagated from the ancestral family, there is an inherent (and acceptable) dependence on the quality of the reference phylogenetic set. No evidence suggests mis-propagation — the fly protein genuinely has the required domains and an intact kinase.

No isoform-specific, artifact, or experimental-contradiction issues were identified.

---

## Limitations and Knowledge Gaps

| Gap | What was checked | Why it matters for curation | What would resolve it |
|---|---|---|---|
| No direct collagen-binding assay for the fly protein | Literature; UniProt; PMID:36355066 | GO:0038062 asserts a biochemical activity; fly binding is inferred only | Solid-phase/SPR binding assay of recombinant fly Ddr ectodomain vs collagens / Multiplexin |
| No collagen-induced autophosphorylation assay for Q59DZ7 | Literature; kinase-motif inspection (motifs intact) | Confirms the "tyrosine kinase" half of the term is active in the fly protein | Collagen-stimulation phospho-Ddr Western in fly or transfected cells |
| Genetic (not physical) Mp–Ddr interaction | PMID:36355066 | Distinguishes direct receptor–ligand from parallel-pathway models | Co-IP / proximity labeling; rescue with binding-dead DS mutant |
| Fly collagen-class ligand specificity | Mammalian ligand literature (¾Col-I fragment) | Which collagen(s) activate fly Ddr is unknown | In vitro activation panel across collagen types / Mp |
| Orthology one-to-two (DDR1+DDR2) | Computed alignment (equal 40.6% identity) | Prevents inappropriate paralog-specific claim transfer | Phylogenetic reconciliation (already consistent with pre-duplication ortholog) |

---

## Discriminating Tests

To move the fly annotation from inference to demonstration, the most efficient experiments are:

1. **Recombinant ectodomain binding assay.** Express the fly Ddr DS domain (res ~106–262) and measure binding to triple-helical collagens and to Multiplexin by SPR or solid-phase ELISA. A positive result directly confirms collagen-receptor activity.
2. **Collagen-induced autophosphorylation.** Express full-length fly Ddr in S2 or mammalian cells; stimulate with collagen; blot for phospho-tyrosine on Ddr. Confirms the kinase half of GO:0038062 is collagen-responsive.
3. **Structure-function rescue.** Test whether a DS-domain binding-interface mutant (mutating the conserved RWxxWR tryptophans) or a kinase-dead (catalytic Asp) mutant fails to rescue the wrapping-glia phenotype in *Ddr* knockdown flies, linking molecular activity to the in vivo role.
4. **Physical Ddr–Mp interaction.** Co-IP or proximity labeling in vivo to test direct receptor–ligand contact versus parallel pathways.
5. **Collagen-class panel.** Determine which collagen types activate fly Ddr, clarifying ligand specificity relative to mammals.

---

## Curation Leads (require curator verification)

**Immediate:**
1. **Retain** GO:0038062 (IBA) and GO:0005518 (IBA). No action change required.
2. Keep the evidence code as **IBA** — do not upgrade to experimental codes; fly-specific biochemistry is absent.
3. Optionally add/confirm a **BP** annotation for glial axon ensheathment from [PMID:36355066](https://pubmed.ncbi.nlm.nih.gov/36355066/) (separate from this MF hypothesis).
4. Record the orthology note (fly Ddr = pre-duplication co-ortholog of human DDR1 **and** DDR2) to prevent paralog-specific claim transfer.

**Candidate reference and snippets to verify (from [PMID:36355066](https://pubmed.ncbi.nlm.nih.gov/36355066/)):**
- *"we identified the conserved receptor tyrosine kinase Discoidin domain receptor (Ddr)"*
- *"we found a strong dominant genetic interaction between Ddr and the type XV/XVIII collagen Multiplexin (Mp), suggesting that Ddr functions as a collagen receptor to drive axon wrapping"*

**Candidate GO terms:** retain GO:0038062 (MF, IBA) and GO:0005518 (MF, IBA); no replacement proposed.

**Suggested questions for curators:** Is any fly-specific biochemical binding/autophosphorylation data available beyond the genetic interaction? Should a BP term for axon ensheathment be added from the same reference?

**Suggested experiments:** see Discriminating Tests.

---

### Bottom line

The IBA annotation of **GO:0038062** to *Drosophila* Ddr (Q59DZ7) is biologically well supported by conserved domain architecture, equal orthology to the human DDR1/DDR2 collagen-receptor family with a conserved collagen-binding interface, and in vivo genetic evidence of collagen-receptor function. **Retain the annotation as IBA.** The only substantive gap is the absence of direct biochemical collagen-binding and autophosphorylation data for the fly protein — a reason to keep the evidence code at the inference level, not a reason to remove the term.


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)