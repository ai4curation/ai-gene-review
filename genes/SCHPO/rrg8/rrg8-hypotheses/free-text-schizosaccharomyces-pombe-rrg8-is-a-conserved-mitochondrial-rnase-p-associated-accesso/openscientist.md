---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-01T13:07:51.571873'
end_time: '2026-09-01T13:29:28.474168'
duration_seconds: 1296.9
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: SCHPO
  gene: rrg8
  gene_symbol: rrg8
  uniprot_accession: O14106
  taxon_id: NCBITaxon:284812
  taxon_label: Schizosaccharomyces pombe (strain 972 / ATCC 24843)
  focus_type: free_text
  hypothesis_slug: free-text-schizosaccharomyces-pombe-rrg8-is-a-conserved-mitochondrial-rnase-p-associated-accesso
  hypothesis_text: Schizosaccharomyces pombe Rrg8 is a conserved mitochondrial RNase
    P-associated accessory factor required for mitochondrial tRNA 5'-end processing
  term_context: No specific term context supplied.
  reference_context: No specific reference context supplied.
  source_file: genes/SCHPO/rrg8/rrg8-ai-review.yaml
  source_selector: free-text
  source_context_yaml: "hypothesis: Schizosaccharomyces pombe Rrg8 is a conserved\
    \ mitochondrial RNase P-associated accessory factor\n  required for mitochondrial\
    \ tRNA 5'-end processing\nfocus_type: free_text\ncontext: []\nreference_id: []"
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 3
    use_hypotheses: true
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 7200
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 6
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

- **Organism code:** SCHPO
- **Taxon:** Schizosaccharomyces pombe (strain 972 / ATCC 24843) (NCBITaxon:284812)
- **Gene directory:** rrg8
- **Gene symbol:** rrg8
- **UniProt accession:** O14106

## Focus

- **Focus type:** free_text
- **Hypothesis slug:** free-text-schizosaccharomyces-pombe-rrg8-is-a-conserved-mitochondrial-rnase-p-associated-accesso
- **Source file:** genes/SCHPO/rrg8/rrg8-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

Schizosaccharomyces pombe Rrg8 is a conserved mitochondrial RNase P-associated accessory factor required for mitochondrial tRNA 5'-end processing

## Term and Decision Context

No specific term context supplied.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: Schizosaccharomyces pombe Rrg8 is a conserved mitochondrial RNase P-associated accessory factor
  required for mitochondrial tRNA 5'-end processing
focus_type: free_text
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

# AIGR Deep Research Report — *S. pombe* Rrg8 (O14106 / SPAC31G5.06)

**Seed hypothesis:** *Schizosaccharomyces pombe* Rrg8 is a **conserved mitochondrial RNase P-associated accessory factor required for mitochondrial tRNA 5'-end processing.**

**Source review file:** `genes/SCHPO/rrg8/rrg8-ai-review.yaml` (focus: free_text)

---

## Executive Judgment

**Verdict: Partially supported (orthology-based; unverified in *S. pombe*).**

The hypothesis is an **accurate paraphrase of the experimentally characterized budding-yeast ortholog**, *S. cerevisiae* **RRG8 = MTA1 = YPR116W** (SGD:S000006320). In *S. cerevisiae*, that protein is (i) required for efficient 5′ processing of mitochondrial tRNAs (IMP), (ii) localized to the matrix side of the inner mitochondrial membrane (IDA), and (iii) physically associated with the mitochondrial RNase P protein subunit Rpm2p (Mta1p co-immunopurifies with Rpm2p) — all from a single primary study, **PMID:30759361** (Guedes-Monteiro et al., 2019).

For *S. pombe* rrg8 **specifically**, however, **every functional and localization annotation is orthology-inferred (evidence code ISO, GO_REF:0000024) transferred from that budding-yeast gene**, with **no direct *S. pombe* experimental evidence** for localization, tRNA-processing function, or RNase P association.

Key caveats that a curator must weigh:
- **"Conserved" is fungal-restricted, not broad.** PomBase taxonomic distribution = *fungi only*; the primary paper describes the family as *Saccharomycetaceae*; the Pfam family PF17068 ("Required for respiratory growth protein 8, mitochondrial") is detected in the budding-yeast protein but **not** matched on *S. pombe* O14106. This factor exists only in fungi that retain an **RNA-based** mitochondrial RNase P (rnpB-encoded), and has no counterpart in the protein-only PRORP systems of metazoa/plants.
- **Orthology is weak and not independently corroborated.** *S. pombe* vs *S. cerevisiae* RRG8 global identity ≈ **23%** (Needleman–Wunsch, 65/280 aligned positions). PomBase curates them as 1:1 orthologs (manual). But three independent checks fail to reinforce this: (i) O14106 carries **no InterPro/Pfam match** (InterPro HTTP 204), whereas Q06109 clearly has IPR031415/PF17068 ("RRG8, mitochondrial"); (ii) **AlphaFold** models diverge sharply — Q06109 is confidently folded (mean pLDDT **75.5**, 69% of residues >70) while O14106 is largely **low-confidence/disordered** (mean pLDDT **50.2**, 0% >70, 43% <50); (iii) the primary paper calls these genes "of the **Saccharomycetaceae** family," yet PomBase extends the ortholog into *S. pombe* (Taphrinomycotina). None of this **refutes** orthology (low pLDDT and an absent Pfam match can both stem from shallow MSA / a narrow family model built on Saccharomycetaceae), but it means the entire ISO transfer rests on the manual ortholog call alone and should be flagged as a **transfer-risk caveat**, not treated as settled.
- **"Accessory factor" is the correct framing.** The budding-yeast molecular function is explicitly **unknown (GO:0003674, ND)**; the protein is *required for* the process and *associated with* RNase P, but is **not** a catalytic RNase P subunit. Do **not** assign a ribonuclease molecular-function term.
- **A phenotype discrepancy exists.** *S. pombe* rrg8Δ is annotated **inviable** in two genome-wide screens (PMID:20473289; PMID:23697806), whereas the budding-yeast null is viable but respiratory-deficient. This is a species difference (or screen artifact) and does not itself contradict the molecular role.
- **A localization conflict exists.** UniProt's automated subcellular prediction for O14106 is cytoplasm/nucleus, conflicting with the ISO mitochondrial annotation. The automated prediction is low-confidence and should be overridden by the orthology-based mitochondrial call, but note that no *direct* *S. pombe* mitochondrial localization has been shown.

**Bottom line for curation:** The existing GO annotations (GO:0097745 BP; GO:0005739 CC) are **defensible ISO leads that should be retained**, with the source correctly attributed to a strong budding-yeast study. The gene-product name is appropriate. But the review should (a) qualify "conserved" as fungal-restricted, (b) flag that no direct *S. pombe* evidence exists, (c) keep molecular function unassigned, and (d) not upgrade "RNase P-associated" into a physical-complex CC term for *S. pombe* without direct data.

---

## Evidence Matrix

| Citation (PMID/DB) | Evidence type | Supports/Refutes/Qualifies | Claim tested | Key finding | Context | Confidence & limitations |
|---|---|---|---|---|---|---|
| **PMID:30759361** (Guedes-Monteiro 2019) | Mutant phenotype (IMP) + localization (IDA) + interaction (co-IP) | **Supports** (for ortholog) | Rrg8/Mta1 required for mito tRNA 5′ processing; RNase P-associated | MTA1/MTA2/GEP5/PET130 needed for efficient 5′ processing of *S. cerevisiae* mito tRNAs; inner-membrane; HMW complexes; **Mta1p co-IPs with Rpm2p** | *S. cerevisiae* mitochondria | High for budding yeast; **not** *S. pombe*; "may be present in a common complex with Rpm2p" is cautiously worded |
| SGD:S000006320 (RRG8/YPR116W/**MTA1**) | Database (curated) | Supports/Qualifies | Identity & function of ISO source | "Protein of unknown function; required for efficient 5′ processing of mitochondrial tRNAs, for respiratory growth and mitochondrial genome maintenance; localizes to the matrix side of the inner mitochondrial membrane"; **MF = ND** | *S. cerevisiae* | Establishes the ISO donor is the very co-IP protein (Mta1); MF explicitly unknown |
| PomBase SPAC31G5.06 `annotation_details` | Database (provenance) | **Qualifies** | Basis of *S. pombe* annotations | GO:0097745 & GO:0005739 both **ISO / GO_REF:0000024 / with:SGD:S000006320**; taxonomic distribution "fungi only"; ortholog = YPR116W | *S. pombe* | Definitive that *S. pombe* support is orthology-only |
| **PMID:12923256** (Seif 2003) | Structural/evolutionary | Supports (pathway context) | *S. pombe* mito RNase P is RNA-based | Identified/confirmed mtDNA-encoded **rnpB** (RNase P RNA) in *S. pombe* and *S. octosporus* | Fission yeast mtDNA | Confirms correct enzymatic context (RNA-based, not PRORP) |
| **PMID:22991464** (Howard 2012) | Structural/evolutionary/review | Qualifies | RNA- vs protein-only RNase P | Yeast mito genomes encode an RNase P RNA; PRORP is a distinct, metazoan/plant innovation | Cross-species | Clarifies Rrg8 is an accessory factor in an RNA-based system |
| **PMID:24184848** (Herbert 2013, review) | Review | Qualifies | Yeast mito RNA factors context | *S. pombe* encodes ~10 PPR proteins; mito general factors include RNA polymerase and RNase P | Yeast mitochondria | Orientation only; Rrg8 is not a PPR protein |
| PMID:20473289; PMID:23697806 | HT mutant phenotype (microscopy) | **Conflicts/Qualifies** | Essentiality | *S. pombe* rrg8Δ scored **inviable** | Genome-wide *S. pombe* deletion screens | Genome-wide calls; possible artifact; stronger than budding-yeast null |
| UniProt O14106 | Database (automated) | **Conflicts** | Localization | Automated SL prediction: cytoplasm/nucleus; protein existence "Predicted"; no InterPro/Pfam xref | *S. pombe* | Low-confidence automated call; overridden by orthology but signals absence of direct data |
| Computed (this run) | Computational | Qualifies | Orthology strength (sequence) | Global identity ≈23% (65/280); Q06109 has IPR031415/PF17068, O14106 has **no** InterPro/Pfam match (HTTP 204) | Pairwise Spombe/S.cer | Twilight-zone identity; transfer-risk flag |
| Computed (this run; AlphaFold DB v6) | Computational (structure) | **Qualifies / competing** | Structural conservation | Q06109 confidently folded (mean pLDDT 75.5; 69% >70); **O14106 low-confidence/disordered (mean pLDDT 50.2; 0% >70; 43% <50)** | AlphaFold monomer models | Structure does not corroborate a shared fold; low pLDDT may also reflect shallow MSA for a fungi-only protein (does not refute) |

---

## GO Curation Implications (leads requiring curator verification)

| GO term | Aspect | Current evidence | Recommended action (lead) |
|---|---|---|---|
| **GO:0097745** mitochondrial tRNA 5′-end processing | BP | ISO from SGD:S000006320 (donor IMP, PMID:30759361) | **Retain** as an ISO lead. It is an appropriately specific BP term backed by a strong ortholog IMP. Keep ISO evidence and the GO_REF; do not upgrade to experimental. |
| **GO:0005739** mitochondrion | CC | ISO from SGD:S000006320 (donor IDA GO:0099617) | **Retain**; optionally consider the more specific CC by orthology (donor is IDA for GO:0099617 "matrix side of mitochondrial inner membrane" / GO:0005743 inner membrane). Given ~23% identity, a conservative curator may keep the general GO:0005739. |
| **GO:0003674** molecular function | MF | Donor = ND (unknown) | **Leave unassigned.** Do **not** add ribonuclease/nuclease activity or "protein binding." No MF is supported. |
| (candidate) part_of RNase P / RNase P complex association | CC/complex | Only budding-yeast co-IP (Mta1–Rpm2) | **Do not add for *S. pombe***. Physical association is shown only in *S. cerevisiae* and only for Mta1; treat as non-core, hypothesis-level. |

Gene-product name "mitochondrial tRNA 5'-end processing protein Rrg8" is consistent with the evidence and can stand.

### Module / holoenzyme context (Iteration 3 checks)

- The budding-yeast tRNA 5′-processing module comprises four accessory factors, each mapping to a **distinct recognized orthogroup**: MTA1/RRG8 (Q06109; OrthoDB 4035333at2759, eggNOG ENOG502S46Y), MTA2 (Q12167; 4065996at2759, ENOG502RYGE), GEP5 (Q12393; 4066262at2759, ENOG502S2Q8), PET130 (P47065; 4062049at2759, ENOG502S17D). **Limitation:** the OrthoDB v12 public API returned `null` for these v11-style group IDs in this environment, so I could **not** programmatically enumerate member species (i.e., whether *S. pombe* also retains orthologs of MTA2/GEP5/PET130). This is reported rather than inferred. Whether the *whole* module is conserved in *S. pombe* — which would strengthen the pathway-context plausibility of rrg8's role — remains an open, checkable question (see Discriminating Tests).
- A targeted PubMed search for a recent **solved structure of the yeast mitochondrial RNase P holoenzyme** naming Mta1/Rrg8 returned nothing indexed. Thus the "RNase P subunit/associated" status of Mta1/Rrg8 currently rests on the **co-IP + co-sedimentation** evidence in PMID:30759361 ("may be present in a common complex with Rpm2p"), not on a structural assignment. This keeps "accessory factor" (rather than defined structural subunit) the appropriately conservative wording.

---

## Mechanistic Scope

- **Immediate molecular activity being claimed:** an accessory (non-catalytic) protein that promotes 5′ endonucleolytic maturation of mitochondrial pre-tRNAs by the RNA-based mitochondrial RNase P holoenzyme (RNA subunit = mtDNA rnpB; protein subunit = Rpm2 in budding yeast).
- **Direct gene-product activity (ortholog-supported):** membrane-associated component that is *required for* efficient 5′ processing and *physically associates* with Rpm2p. Its own catalytic activity is unknown (ND).
- **Downstream / indirect effects (must not be conflated with core function):** respiratory-growth deficiency, mitochondrial genome maintenance defects, decreased plasma-membrane electron transport (budding-yeast null), and the *S. pombe* inviable phenotype. These are loss-of-function consequences, not the molecular function.

---

## Conflicts and Alternatives

1. **Localization conflict:** UniProt automated prediction (cytoplasm/nucleus) vs orthology-based mitochondrion. Resolve in favor of mitochondrion, but acknowledge no direct *S. pombe* localization.
2. **Orthology / conservation risk:** ~23% identity, no PF17068 match on O14106, and an AlphaFold model that is low-confidence/disordered (mean pLDDT 50.2, 0% >70) versus a well-folded budding-yeast ortholog (75.5). The budding-yeast function may not transfer cleanly; the *S. pombe* protein could have diverged or acquired additional roles (consistent with its inviable phenotype). Caveat: low pLDDT/absent Pfam can also arise from shallow MSA for a fungi-restricted protein, so this weakens — but does not refute — the transfer.
3. **Phenotypic divergence:** rrg8Δ inviable in *S. pombe* vs viable/respiratory-deficient in *S. cerevisiae*. Alternative explanations: (a) *S. pombe* dependence on mitochondrial translation/mtDNA maintenance makes the defect lethal; (b) an additional essential (non-mitochondrial) function; (c) genome-wide-screen false positive.
4. **"RNase P-associated" strength:** In the primary paper, direct co-IP with Rpm2 was demonstrated for **Mta1p** (=RRG8) specifically — good for this gene — but the authors phrase the complex membership cautiously ("**may** be present in a common complex"). An alternative model is that these factors influence mito tRNA stability or membrane-tethered RNA metabolism rather than acting as bona fide RNase P subunits.
5. **No paralog confusion detected:** single-copy in *S. pombe*; the ISO donor is unambiguously YPR116W/RRG8/MTA1.

---

## Knowledge Gaps

| Gap | What was checked | Why it matters | What would resolve it |
|---|---|---|---|
| No direct *S. pombe* mito tRNA-processing assay | PomBase annotation_details (ISO only) | The core BP claim is untested in *S. pombe* | Northern blot / RNA-seq of mito pre-tRNA 5′ ends in rrg8-depletion (conditional allele, given inviability) |
| No direct *S. pombe* localization | UniProt (predicted cyto/nucleus); PomBase (ISO mito) | CC term unverified in the organism | GFP-tagging + submitochondrial fractionation |
| Does *S. pombe* have an Rpm2 ortholog / how is its mito RNase P organized? | Confirmed mtDNA rnpB exists (PMID:12923256); Rpm2 protein partner not established | "RNase P-associated" presupposes a protein partner to associate with | Identify *S. pombe* mito RNase P protein subunits; co-IP Rrg8 with rnpB RNA / Rpm2 ortholog |
| Orthology confidence (~23% id, no Pfam match, disordered AF model) | Computed NW identity; InterPro API (204/no match); AlphaFold pLDDT (O14106 50.2 vs Q06109 75.5) | Determines whether ISO transfer is safe | Foldseek/TM-align structural superposition with MSA-depth control; phylogenetic ortholog analysis across Taphrinomycotina; cross-species complementation |
| Basis of inviable phenotype | Two genome-wide screens | Affects interpretation of essentiality vs respiratory role | Tetrad dissection / conditional allele; test viability on non-fermentable vs fermentable media |

---

## Discriminating Tests (most efficient first)

1. **Cross-species complementation:** does *S. pombe* rrg8 rescue the respiratory defect of *S. cerevisiae* mta1Δ (and vice versa)? Directly tests functional orthology behind the ISO transfer.
2. **Mito pre-tRNA 5′-end assay in *S. pombe*** (conditional rrg8 allele): accumulation of 5′-extended mito pre-tRNAs would confirm the transferred BP.
3. **Submitochondrial localization** of tagged Rrg8 in *S. pombe* (fractionation/protease protection) to confirm inner-membrane, matrix-side placement.
4. **Interaction test:** co-purify Rrg8 with *S. pombe* mitochondrial RNase P (rnpB RNA and any protein partner) to test the "RNase P-associated" claim in the organism.
5. **AlphaFold structural comparison** of O14106 vs Q06109 to buttress orthology despite low sequence identity. *(Attempted this run: O14106's model is low-confidence/disordered — mean pLDDT 50.2 — so it did not corroborate a shared fold; a Foldseek/TM-align comparison with MSA-depth controls would be more decisive.)*
6. **Module-conservation check:** determine whether *S. pombe* retains orthologs of MTA2/GEP5/PET130 (OrthoDB/eggNOG member-species enumeration, or PomBase reverse ortholog lookup). Presence of the whole module would strengthen the pathway context; absence would argue the rrg8 role may not transfer.

---

## Curation Leads (require curator verification)

- **Candidate reference to attach / verify:** **PMID:30759361** (Guedes-Monteiro et al., 2019, *RNA Biol/…* — "5′ processing of *Saccharomyces cerevisiae* mitochondrial tRNAs requires expression of multiple genes"). Exact snippets to verify: *"Here, we identify four novel genes MTA1, MTA2, GEP5 and PET130 of the Saccharomycetaceae family that are necessary for an efficient processing of mitochondrial tRNAs."* and *"This is supported by pull-down assays showing co-immunopurification of Rpm2 with Mta1p."* (Note SGD alias: RRG8/YPR116W = MTA1.)
- **Pathway-context references:** PMID:12923256 (*S. pombe* mtDNA-encoded rnpB / RNA-based mito RNase P); PMID:22991464 (RNA-based yeast vs protein-only PRORP).
- **GO actions:** Retain GO:0097745 (BP, ISO) and GO:0005739 (CC, ISO); optionally consider the more specific CC (GO:0005743 / GO:0099617) by orthology. Keep MF unassigned. Do not add a physical RNase P-complex CC term for *S. pombe* without direct data. Avoid "protein binding" as a recommendation.
- **Qualifier for the review text:** change "conserved" → "conserved within fungi (Ascomycota; fungi-only distribution)"; add explicit note that the *S. pombe* annotation is orthology-inferred (ISO) from budding-yeast Mta1/Rrg8 and is **not** experimentally verified in fission yeast; flag ~23% ortholog identity and absent PF17068 match as a transfer caveat.
- **Suggested curator questions:** (1) Is the PomBase 1:1 ortholog call to YPR116W robust beyond sequence similarity (synteny/structure)? (2) Should the inviable phenotype be reconciled with a respiratory-only role? (3) Is there any *S. pombe* Rpm2 ortholog for Rrg8 to associate with?
- **Suggested experiments:** the five Discriminating Tests above (complementation and mito pre-tRNA assay are highest value).

---

*Provenance:* All database values were fetched programmatically this run (UniProt REST for O14106/Q06109; PomBase API `annotation_details` for SPAC31G5.06; SGD backend for S000006320; EBI InterPro API). Sequence identity was computed by an in-run Needleman–Wunsch alignment (65/280 = 23.2%). Where a resource returned no content (InterPro for O14106, HTTP 204), this is reported rather than inferred.


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)