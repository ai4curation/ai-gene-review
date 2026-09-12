---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-09T06:19:13.131308'
end_time: '2026-07-09T06:32:57.318968'
duration_seconds: 824.19
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: GADMO
  gene: A0A8C5FPT8
  gene_symbol: tbc1d14
  uniprot_accession: A0A8C5FPT8
  taxon_id: NCBITaxon:8049
  taxon_label: Gadus morhua
  focus_type: computational_prediction
  hypothesis_slug: prediction-autophagosome
  hypothesis_text: ProtNLM2 predicts autophagosome localization (GO:0005776) for the
    Gadus morhua protein tbc1d14, a TBC-domain Rab GTPase-activating protein. Independently
    assess whether the sequence/domain evidence and orthology support localization
    to the autophagosome itself, versus TBC1D14's characterized association with recycling
    endosomes and the ULK1 complex where it negatively regulates autophagy initiation
    (i.e. a regulator of autophagy that is not itself an autophagosome-resident structural
    protein) -- which would make the autophagosome-localization prediction a misassignment.
    Determine whether the prediction is supported or refuted.
  term_context: '- Term: autophagosome (GO:0005776)'
  reference_context: No specific reference context supplied.
  source_file: ''
  source_selector: ''
  source_context_yaml: "hypothesis: ProtNLM2 predicts autophagosome localization (GO:0005776)\
    \ for the Gadus morhua protein tbc1d14,\n  a TBC-domain Rab GTPase-activating\
    \ protein. Independently assess whether the sequence/domain evidence\n  and orthology\
    \ support localization to the autophagosome itself, versus TBC1D14's characterized\
    \ association\n  with recycling endosomes and the ULK1 complex where it negatively\
    \ regulates autophagy initiation (i.e.\n  a regulator of autophagy that is not\
    \ itself an autophagosome-resident structural protein) -- which would\n  make\
    \ the autophagosome-localization prediction a misassignment. Determine whether\
    \ the prediction is\n  supported or refuted.\nfocus_type: computational_prediction\n\
    term_id: GO:0005776\nterm_label: autophagosome\ncontext: []\nreference_id: []"
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
citation_count: 4
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

- **Organism code:** GADMO
- **Taxon:** Gadus morhua (NCBITaxon:8049)
- **Gene directory:** A0A8C5FPT8
- **Gene symbol:** tbc1d14
- **UniProt accession:** A0A8C5FPT8

## Focus

- **Focus type:** computational_prediction
- **Hypothesis slug:** prediction-autophagosome
- **Source file:** 
- **Source selector:** 

## Seed Hypothesis

ProtNLM2 predicts autophagosome localization (GO:0005776) for the Gadus morhua protein tbc1d14, a TBC-domain Rab GTPase-activating protein. Independently assess whether the sequence/domain evidence and orthology support localization to the autophagosome itself, versus TBC1D14's characterized association with recycling endosomes and the ULK1 complex where it negatively regulates autophagy initiation (i.e. a regulator of autophagy that is not itself an autophagosome-resident structural protein) -- which would make the autophagosome-localization prediction a misassignment. Determine whether the prediction is supported or refuted.

## Term and Decision Context

- Term: autophagosome (GO:0005776)

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: ProtNLM2 predicts autophagosome localization (GO:0005776) for the Gadus morhua protein tbc1d14,
  a TBC-domain Rab GTPase-activating protein. Independently assess whether the sequence/domain evidence
  and orthology support localization to the autophagosome itself, versus TBC1D14's characterized association
  with recycling endosomes and the ULK1 complex where it negatively regulates autophagy initiation (i.e.
  a regulator of autophagy that is not itself an autophagosome-resident structural protein) -- which would
  make the autophagosome-localization prediction a misassignment. Determine whether the prediction is
  supported or refuted.
focus_type: computational_prediction
term_id: GO:0005776
term_label: autophagosome
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
prompt so the report can be compared against them after the run.

Do not rely on literature alone. Where the hypothesis is decidable by computation,
actually run the analysis and keep it as provenance rather than only reasoning
about it. Match the analysis to the question, for example:

- membrane topology / localization: compute a hydropathy profile and predicted
  transmembrane segments from the sequence, and locate signal peptides and
  targeting/sorting motifs (e.g. dileucine, acidic-cluster, NLS); compare against
  UniProt topology features and AlphaFold geometry.
- catalytic / binding activity: check whether the specific active-site,
  metal-binding, or motif residues are present and correctly spaced (in sequence
  and, where useful, structure) and compare to characterized family members.
- DNA-binding / regulatory: examine the binding-domain class, obligate partners,
  and known binding-motif / PWM signatures.
- family / paralog questions: use domain (Pfam/InterPro), orthology, and
  conservation comparisons to distinguish subfamilies.

Use resources you can actually access programmatically (UniProt, AlphaFold DB,
InterPro, sequence computation, public APIs). If a resource is web-only or you
cannot run a check, say so plainly instead of guessing — never fabricate a result,
and an inconclusive or "could not run" analysis is an acceptable and useful
outcome. Report all computational results conservatively and prefer recording the
underlying analysis (code, computed values, table, or plot) as provenance.

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

## Target: *Gadus morhua* tbc1d14 (UniProt A0A8C5FPT8)
### Focus: computational_prediction — autophagosome localization (GO:0005776)
### Hypothesis slug: `prediction-autophagosome`

---

## Summary

The seed hypothesis proposed that ProtNLM2's prediction of **autophagosome localization (GO:0005776)** for the *Gadus morhua* protein tbc1d14 is likely a **misassignment** — the reasoning being that TBC1D14 is a TBC-domain Rab GTPase-activating protein (RabGAP) characterized as a recycling-endosome/ULK1-complex regulator of autophagy *initiation*, not a structural, autophagosome-resident protein. On that logic, placing the protein "inside" the autophagosome would be an over-annotation.

This investigation confirms the *biological* substance of that concern but **overturns its conclusion that the prediction is a hallucination or clear misassignment.** The decisive finding, obtained by directly interrogating curated GO annotations for the human ortholog TBC1D14 (Q9P2M4), is that **autophagosome (GO:0005776) is an existing, manually curated annotation** supported by two independent evidence lines: an **IDA (Inferred from Direct Assay)** annotation from [PMID: 22613832](https://pubmed.ncbi.nlm.nih.gov/22613832/) assigned by expert BHF-UCL curators, *and* an independent **IBA (phylogenetic)** annotation from GO_Central (PANTHER node PTN000538677). Because the *Gadus morhua* protein is a bona fide 1:1 ortholog (62.1% identity, identical TBC domain architecture with intact catalytic fingers, same PANTHER family PTHR47219), it is legitimately eligible for the same orthology-based inference. The ProtNLM2 prediction therefore *coincides with* existing curated knowledge rather than contradicting it.

The essential caveat is one of **precision, not correctness**. Autophagosome is a **secondary, condition-dependent** localization. TBC1D14's primary and best-characterized compartment is the **Rab11/transferrin-receptor–positive recycling endosome** (relocalizing to the **Golgi** upon starvation), and its role in autophagy is **regulatory** — it is a *negative* regulator of autophagy initiation acting via ULK1 and the TRAPP–ATG9 membrane-delivery axis, not an autophagosome structural protein. The verdict is therefore **PARTIALLY SUPPORTED**: GO:0005776 is defensible for the fish protein by orthology and should be retained, but only *alongside* recycling endosome (GO:0055037) and the regulation-of-autophagy BP terms — never as the sole or primary cellular-component annotation.

---

## Key Findings

### Finding F001 — The *Gadus morhua* protein is a bona fide 1:1 ortholog of human TBC1D14 with an intact TBC RabGAP domain

A global Needleman–Wunsch alignment of A0A8C5FPT8 against human TBC1D14 (Q9P2M4) yielded **414 identical aligned columns out of 667 (62.1% identity)**, comfortably within the range expected for a true 1:1 vertebrate ortholog rather than a distant paralog. Both proteins carry a **single Rab-GAP TBC domain** (UniProt domain 388–596; Pfam **PF00566** RabGAP-TBC; InterPro **IPR000195**), and both are assigned to PANTHER family **PTHR47219**.

Critically, the **dual-finger catalytic residues** that define a functional RabGAP are conserved and positionally aligned between fish and human:

| Catalytic element | Motif | *Gadus* position | Human position |
|---|---|---|---|
| Arg-finger | IKLD**IS**R | ~451 | ~466 |
| Gln-finger | Y**VQ** | ~491 | ~506 |

The N-terminal architecture is likewise conserved (disordered regions plus a coiled-coil at ~315–357). There is **no signal peptide and no annotated transmembrane segment**; the maximum Kyte–Doolittle hydropathy across the whole sequence is only **1.86**, below the threshold that would indicate a sustained membrane-spanning helix. The protein is therefore a **peripheral/cytosolic protein that associates with membranes through protein–protein and Rab interactions**, not an integral membrane protein — exactly what is expected of a RabGAP regulator rather than a resident structural component of an organelle membrane.

The curation consequence is important: the orthology is strong enough that experimental and phylogenetic annotations on human TBC1D14 are propagable to the fish protein by ISO/IBA. This is precisely what converts the autophagosome prediction from "fabricated" to "defensible inference."

### Finding F002 — TBC1D14 localizes to recycling endosomes/Golgi and negatively regulates autophagy; it is not an autophagosome structural protein

The primary mammalian literature paints a consistent, mechanistically detailed picture. In the founding study ([PMID: 22613832](https://pubmed.ncbi.nlm.nih.gov/22613832/)), TBC1D14 was identified as a putative RabGAP that **"colocalizes and interacts with the autophagy kinase ULK1"** and, when overexpressed, **"tubulates ULK1-positive recycling endosomes (REs), impairing their function and inhibiting autophagosome formation."** The same study reported that **"amino acid starvation causes TBC1D14 to relocalize from REs to the Golgi complex, whereas TfnR and Tfn localize to forming autophagosomes"** — meaning that upon autophagy induction the protein itself moves to the Golgi, while transferrin-receptor membrane is delivered onward. This is direct evidence *against* stable autophagosome residence: the protein's steady-state compartment is the recycling endosome and its starvation-response compartment is the Golgi.

The follow-up mechanistic study ([PMID: 26711178](https://pubmed.ncbi.nlm.nih.gov/26711178/)) described **"TBC1D14, as a negative regulator of autophagy that controls delivery of membranes from RAB11-positive recycling endosomes to forming autophagosomes,"** acting via the TRAPP complex and ATG9 traffic. A systematic overexpression screen ([PMID: 22874560](https://pubmed.ncbi.nlm.nih.gov/22874560/)) placed TBC1D14 among TBC-domain proteins that inhibit autophagy when overexpressed, acting **"at an early stage during autophagosome formation"** by regulating recycling-endosomal traffic — with ATG9 and ULK1 localizing to transferrin-receptor-positive recycling endosomes that are tubulated by excess TBC1D14, and RE membrane subsequently incorporated into newly forming autophagosomes.

Together, these establish TBC1D14 as a **traffic regulator operating upstream of and around the forming autophagosome**, not a component embedded in the mature organelle. This validates the *biological* core of the seed hypothesis: the protein is a regulator, and any autophagosome association is transient and delivery-related.

### Finding F003 — CORRECTION: autophagosome (GO:0005776) is a curated experimental + phylogenetic GO annotation, not merely a ProtNLM2 artifact

The pivotal correction to an initial "refuted" reading came from directly querying curated GO annotations (QuickGO) for human TBC1D14 (Q9P2M4). **GO:0005776 (autophagosome) is present with two independent evidence lines:**

1. **ECO:0000314 (IDA, Inferred from Direct Assay)** from [PMID: 22613832](https://pubmed.ncbi.nlm.nih.gov/22613832/), assigned by expert curators at **BHF-UCL**.
2. **ECO:0000318 (IBA, phylogenetic)** from **GO_Central**, PANTHER ancestral node PTN000538677 (GO_REF:0000033).

The same protein is curated to a broader localization set that puts autophagosome in its proper context:

| GO term | Label | Aspect | Evidence | Source |
|---|---|---|---|---|
| GO:0055037 | recycling endosome | CC | IDA ([PMID: 17562788](https://pubmed.ncbi.nlm.nih.gov/17562788/)), IBA, Reactome | primary/PANTHER |
| GO:0005794 | Golgi apparatus | CC | IDA (HPA) + UniProt-SubCell | Human Protein Atlas |
| GO:0005776 | **autophagosome** | CC | **IDA ([PMID: 22613832](https://pubmed.ncbi.nlm.nih.gov/22613832/)), IBA** | BHF-UCL / GO_Central |
| GO:0005773 | vacuole | CC | electronic | ARBA |
| GO:0031410 | cytoplasmic vesicle | CC | electronic | ARBA |
| GO:0010507 | negative regulation of autophagy | BP | IMP | primary |
| GO:2000785 | regulation of autophagosome assembly | BP | IMP + IBA | primary/PANTHER |

The *Gadus morhua* ortholog A0A8C5FPT8 currently carries **only broad electronic CC terms** (vacuole GO:0005773, cytoplasmic vesicle GO:0031410; ARBA) and belongs to PANTHER **PTHR47219**, making it eligible for the same IBA propagation that gave human TBC1D14 its autophagosome annotation. From a curation-provenance standpoint, GO:0005776 for the fish protein is therefore a **legitimate orthology-based inference**, not a hallucinated label — even though it represents a secondary and condition-dependent localization.

A supplementary sequence check strengthens the "regulator, not autophagosome-membrane component" reading: a LIR/AIM motif scan ([WFY]xx[LIV]) returned 13 core matches in the fish sequence and 12 in the human sequence — at chance level (~16 expected across ~700 aa) — and no functional LIR is reported for TBC1D14. This is consistent with a peripheral regulator that is *not* stably anchored to autophagosomal membranes via an ATG8-binding motif (weak evidence, offered only as a supporting caveat).

---

## Mechanistic Model / Interpretation

The synthesis reconciles two facts that at first appear contradictory: (a) TBC1D14 is a *regulator*, not a structural autophagosome protein, yet (b) autophagosome (GO:0005776) is a genuinely curated CC annotation.

```
   NUTRIENT-RICH (steady state)                STARVATION (autophagy induction)
   ---------------------------                 --------------------------------
        Rab11(+) RECYCLING ENDOSOME                 GOLGI COMPLEX
        [PRIMARY localization]                      [TBC1D14 relocalizes here]
                |                                            |
        TBC1D14 --- ULK1 (interaction)              TBC1D14 leaves REs
        RabGAP activity; tubulates REs                       |
        when overexpressed                          TfnR / Tfn membrane -----> FORMING
                |                                    (delivered onward)        AUTOPHAGOSOME
        NEGATIVELY REGULATES                                                   (GO:0005776)
        autophagosome formation                     TBC1D14 transiently/peripherally
        (GO:0010507, GO:2000785)                    associated during membrane delivery
                                                    -> basis of the IDA CC annotation
```

The model runs as follows. In resting (nutrient-rich) cells, TBC1D14 resides at the **recycling endosome**, holding ULK1-positive REs in check and thereby restraining autophagy initiation — its negative-regulator BP role. Its GAP domain, with intact Arg- and Gln-fingers (F001), targets Rab GTPases governing this recycling traffic. Upon amino-acid starvation, TBC1D14 **relocalizes to the Golgi**, releasing recycling-endosomal (transferrin-receptor-positive) membrane that is routed via the TRAPP complex and ATG9 machinery toward the **forming autophagosome**. The autophagosome CC annotation captures a **transient, membrane-delivery-associated presence at/near the forming autophagosome** observed experimentally, rather than stable structural residence.

For curation, the correct representation is a **compound CC picture led by recycling endosome, with autophagosome as a secondary, mechanistically justified term**, tied together by BP terms that describe what the protein actually *does* (negative regulation of autophagy; regulation of autophagosome assembly) and by an MF term for its RabGAP activity. Annotating autophagosome alone would be a category error; omitting it entirely would discard a curated experimental observation.

---

## Evidence Base

| Citation | Evidence type | Supports / refutes / qualifies | Claim tested | Key finding | Context | Confidence & limitations |
|---|---|---|---|---|---|---|
| [PMID: 22613832](https://pubmed.ncbi.nlm.nih.gov/22613832/) (Longatti et al. 2012, JCB) — **GO IDA source** | Direct assay + localization + interaction | **Qualifies** (supports secondary autophagosome; refutes "primary/structural") | Is TBC1D14 an autophagosome-resident protein? | Colocalizes/interacts with ULK1 on Rab11⁺ recycling endosomes; overexpression tubulates REs and inhibits autophagosome formation; relocalizes to Golgi on starvation. Source of the IDA GO:0005776 annotation. | Human cultured cells | High confidence; overexpression may exaggerate RE tubulation; autophagosome call rests on full-text figures |
| [PMID: 26711178](https://pubmed.ncbi.nlm.nih.gov/26711178/) (Lamb et al. 2016, EMBO J) | Mechanism / interaction | **Refutes structural role; supports regulator role** | Is TBC1D14 a regulator vs. resident protein? | Negative regulator of autophagy controlling membrane delivery from RAB11⁺ REs to forming autophagosomes via TRAPP/ATG9. | Mammalian cells | High confidence for regulatory mechanism |
| [PMID: 22874560](https://pubmed.ncbi.nlm.nih.gov/22874560/) (Longatti & Tooze 2012) | Systematic overexpression screen / review | **Qualifies** | Does TBC1D14 act at autophagosome formation? | Among TBC proteins inhibiting autophagy when overexpressed; acts early via recycling-endosomal traffic; RE membrane incorporated into new autophagosomes. | Human cells | Moderate–high; overexpression screen, indirect for endogenous localization |
| [PMID: 17562788](https://pubmed.ncbi.nlm.nih.gov/17562788/) (via QuickGO) | Localization (IDA) | **Supports primary localization** | Where is TBC1D14 at steady state? | Basis for recycling endosome (GO:0055037) IDA annotation. | Human | Database-level orientation; primary paper not re-read here |
| QuickGO curated annotations (Q9P2M4) | Review/database | **Supports** provenance of GO:0005776 | Is autophagosome a real curated CC? | GO:0005776 present with IDA (BHF-UCL) + IBA (GO_Central, PTN000538677). | Human ortholog | High confidence in annotation existence; it is one of several curated CCs |
| Sequence/structural computation (this run) | Structural/evolutionary + computational | **Supports orthology; refutes membrane-integral residence** | Is the fish protein a true TBC1D14 ortholog? Membrane-embedded? | 62.1% identity to human; intact TBC domain (PF00566/IPR000195); conserved Arg/Gln fingers; no signal peptide/TM; max hydropathy 1.86. | *Gadus morhua* vs human | High confidence; computed provenance |

**How the literature bears on the verdict.** The three primary/mechanistic papers ([PMID: 22613832](https://pubmed.ncbi.nlm.nih.gov/22613832/), [PMID: 26711178](https://pubmed.ncbi.nlm.nih.gov/26711178/), [PMID: 22874560](https://pubmed.ncbi.nlm.nih.gov/22874560/)) unanimously frame TBC1D14 as a recycling-endosome-based *regulator* of autophagy. None describes it as an autophagosome structural protein. That is why the hypothesis is not *fully* supported. Yet the same founding paper ([PMID: 22613832](https://pubmed.ncbi.nlm.nih.gov/22613832/)) is the documented source of a curated IDA autophagosome annotation, and that annotation plus its phylogenetic IBA companion are why the prediction is not *refuted* either.

---

## Limitations and Knowledge Gaps

1. **No experimental data in *Gadus morhua*.** Every localization and functional result is mammalian. What was checked: QuickGO for A0A8C5FPT8 (only broad ARBA CC terms) and PubMed. Why it matters: the fish autophagosome call is *transferred*, not measured. Resolver: heterologous or fish-cell co-localization of tagged tbc1d14 with LC3/ATG8 versus Rab11/transferrin receptor.
2. **Strength of the autophagosome IDA.** The precise figure/condition in [PMID: 22613832](https://pubmed.ncbi.nlm.nih.gov/22613832/) underpinning GO:0005776 was not machine-verifiable here (abstract-level access; abstract emphasizes RE/Golgi). Why it matters: it determines whether the annotation reflects stable residence or transient colocalization. Resolver: a curator reading the full text and its imaging figures.
3. **Endogenous vs. overexpression localization.** Several phenotypes derive from overexpression, which can exaggerate RE tubulation and autophagy inhibition. Resolver: endogenous co-localization under fed/starved conditions.
4. **Primary recycling-endosome source not re-read.** GO:0055037 IDA cites [PMID: 17562788](https://pubmed.ncbi.nlm.nih.gov/17562788/); taken here from QuickGO orientation. Resolver: read that paper directly.
5. **Rab substrate of the GAP domain unresolved.** Even in human, TBC1D14 binds active Rab11 but is not established as its GAP; this affects MF specificity. Resolver: in-vitro RabGAP assays across candidate Rabs.
6. **ProtNLM2 raw output not inspected.** The confidence score and whether recycling-endosome or RabGAP terms were also emitted are unknown. Resolver: inspect the full prediction ranking.

---

## Conflicts and Alternatives

- **Seed framing vs. database record.** The seed's "misassignment/hallucination" framing is directly contradicted by the curated IDA + IBA autophagosome annotations on the human ortholog — the central correction of this analysis. The tension is real but resolves toward "less precise," not "wrong."
- **Internal investigation conflict.** Iteration 1 concluded "refuted" from the mechanistic literature; Iteration 2 overturned this on discovering the curated annotation; Iteration 3 settled on "partially supported." The curator inherits this reconciliation.
- **Precision, not fabrication.** The mechanistic literature centers TBC1D14 on the recycling endosome/Golgi as a *regulator*; autophagosome is a co-annotation. The risk is over-emphasis of a secondary CC, not invention of a false one.
- **Provenance concentration.** The autophagosome IDA rests on a single paper and curation group ([PMID: 22613832](https://pubmed.ncbi.nlm.nih.gov/22613832/), BHF-UCL), whose abstract stresses RE/Golgi — so the autophagosome call depends on full-text figures.
- **Paralog confusion (low risk).** The 62.1% identity, shared PANTHER node (PTHR47219), conserved gene name, and conserved N-terminal coiled-coil argue for a specific 1:1 TBC1D14 ortholog, not a mis-mapped paralog.
- **Organism-specific difference (unresolved).** All experimental data are mammalian; the teleost transfer rests entirely on orthology.

---

## Discriminating Tests

1. **Endogenous co-localization panel (most decisive):** immunofluorescence of endogenous TBC1D14 versus Rab11/transferrin receptor (recycling endosome), GM130 (Golgi), and LC3/ATG8 (autophagosome) in fed versus starved cells. Expected: strong RE overlap at steady state; Golgi shift on starvation; only transient/partial LC3 overlap — confirming autophagosome as secondary.
2. **Purified-autophagosome proteomics:** is TBC1D14 enriched relative to core ATG8-family proteins, or transient? Distinguishes residence from delivery-associated passage.
3. **RabGAP activity assay:** in-vitro GAP assay of the *Gadus* TBC domain against candidate Rab substrates (e.g., Rab11) to confirm MF GO:0005096/GO:0005097 and validate the conserved Arg/Gln fingers.
4. **ULK1 interaction test:** co-IP of *Gadus* tbc1d14 with the ULK1 ortholog to confirm the regulatory-complex association behind the BP terms.
5. **Orthology/IBA audit:** confirm A0A8C5FPT8 sits under PANTHER node PTN000538677 to formally license IBA propagation of GO:0005776, GO:0055037, and GO:2000785.

---

## GO Curation Implications and Proposed Actions (leads — require curator verification)

**Overall lead:** treat **GO:0005776 (autophagosome)** as **acceptable-by-orthology but non-exclusive** — retain it as a *secondary* CC, and ensure the fish annotation set is not headed by autophagosome. The ProtNLM2 prediction is *less precise than existing knowledge*, not wrong.

| GO ID | Label | Aspect | Proposed action | Evidence basis |
|---|---|---|---|---|
| GO:0055037 | recycling endosome | CC | **Add as primary CC** (IBA/ISO) | Ortholog IDA [PMID: 17562788](https://pubmed.ncbi.nlm.nih.gov/17562788/) + IBA |
| GO:0005776 | autophagosome | CC | **Retain as secondary CC** (IBA) | Ortholog IDA [PMID: 22613832](https://pubmed.ncbi.nlm.nih.gov/22613832/) + IBA |
| GO:0005794 | Golgi apparatus | CC | Consider adding (IBA) | Ortholog IDA (HPA) |
| GO:0010507 | negative regulation of autophagy | BP | **Add** (IBA) | Ortholog IMP |
| GO:2000785 | regulation of autophagosome assembly | BP | **Add** (IBA) | Ortholog IMP + IBA |
| GO:0005096 / GO:0005097 | GTPase activator activity / Rab GTPase activator activity | MF | **Retain / add** (ISS/IBA) | Intact TBC domain, conserved dual fingers |
| GO:0031267 | small GTPase binding | MF | Retain | TBC domain |
| GO:0005773 | vacuole | CC | Consider generalizing/removing | Broad electronic (ARBA) |
| GO:0031410 | cytoplasmic vesicle | CC | Consider generalizing/removing | Broad electronic (ARBA) |

**Mechanistic scope reminder for the curator.** The immediate molecular activity is RabGAP/Rab-binding; the immediate cellular action is at recycling endosomes with ULK1 and the TRAPP complex; "regulation of autophagosome formation" is a downstream *pathway consequence*; and autophagosome localization is a *secondary, transient* CC. Keep these separated in the annotation set.

**Candidate references with exact snippets to verify:**
- [PMID: 22613832](https://pubmed.ncbi.nlm.nih.gov/22613832/): *"One of these putative RabGAPs, TBC1D14, colocalizes and interacts with the autophagy kinase ULK1. Overexpressed TBC1D14 tubulates ULK1-positive recycling endosomes (REs), impairing their function and inhibiting autophagosome formation."*
- [PMID: 22613832](https://pubmed.ncbi.nlm.nih.gov/22613832/): *"Amino acid starvation causes TBC1D14 to relocalize from REs to the Golgi complex, whereas TfnR and Tfn localize to forming autophagosomes"* — verify the full-text autophagosome-localization figure behind the IDA.
- [PMID: 26711178](https://pubmed.ncbi.nlm.nih.gov/26711178/): *"TBC1D14, as a negative regulator of autophagy that controls delivery of membranes from RAB11-positive recycling endosomes to forming autophagosomes"*.

**Suggested curator question:** should the fish annotation propagate the human IBA set (autophagosome + recycling endosome + regulatory BP + RabGAP MF) rather than remain at the current broad ARBA CC terms?

---

## Provenance (computed this run)

- **UniProt A0A8C5FPT8:** ~709 aa, "Rab-GAP TBC domain-containing protein," gene *tbc1d14*; CC absent; MF = GO:0005096, GO:0031267; TBC domain 388–596 (PF00566/IPR000195).
- **Needleman–Wunsch vs Q9P2M4:** 414/667 identical = **62.1%**; conserved Arg-finger IKLDISR (Gad 451 / Hum 466), Gln-finger YVQ (Gad 491 / Hum 506); max Kyte–Doolittle hydropathy **1.86** (no clear TM); no signal peptide.
- **QuickGO Q9P2M4 CC:** autophagosome (IDA [PMID: 22613832](https://pubmed.ncbi.nlm.nih.gov/22613832/) + IBA), recycling endosome (IDA [PMID: 17562788](https://pubmed.ncbi.nlm.nih.gov/17562788/) + IBA + Reactome), Golgi (IDA HPA + UniProt-SubCell), cytosol, vacuole, cytoplasmic vesicle; BP: negative regulation of autophagy (GO:0010507), regulation of autophagosome assembly (GO:2000785).
- **QuickGO A0A8C5FPT8:** only ARBA CC vacuole (GO:0005773) + cytoplasmic vesicle (GO:0031410); PANTHER PTHR47219.
- **LIR/AIM motif scan ([WFY]xx[LIV]):** 13 (Gadus) / 12 (human) core matches — at chance level (~16 expected in ~700 aa); no functional LIR reported for TBC1D14 (weak supporting caveat only).

---

## Bottom Line

The ProtNLM2 autophagosome prediction for *Gadus morhua* tbc1d14 is **partially supported, not a hallucination**: GO:0005776 is a curated experimental (IDA) plus phylogenetic (IBA) annotation on the human ortholog, and the fish protein is a strong 1:1 ortholog (62.1% identity, PTHR47219) eligible for the same inference. However, autophagosome is a **secondary, condition-dependent** localization. The protein's primary compartment is the Rab11⁺ **recycling endosome** (and Golgi upon starvation), and its primary role is as a **negative regulator of autophagy** acting from those compartments. GO:0005776 should be **retained only alongside** recycling endosome (GO:0055037) and the regulation-of-autophagy BP terms, never as the sole or primary cellular-component annotation.


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)