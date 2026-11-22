---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-21T00:49:07.519336+00:00'
provider_config:
  job_id: dc13b854-c862-4926-82a1-8ae985f1ebe0
  job_status_at_recovery: cancelled
  recovered_from_artifact_member: final_report.md
  report_body_sha256: 4b6b8b4d2792c8631eac6d5a1bfe74789453735530223129700a30fc0a380851
  recovery_provenance: recovery-provenance.json
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
- **Gene directory:** PIK3C3
- **Gene symbol:** PIK3C3
- **UniProt accession:** Q8NEB9

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** pexophagy-and-peroxisome-localization
- **Source file:** genes/human/PIK3C3/PIK3C3-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

Human PIK3C3 participates in pexophagy (GO:0000425) and localizes to the peroxisome (GO:0005777). Adjudicate these two claims independently. Identify the catalytic and complex machinery for mammalian pexophagy and distinguish localization on an engulfing autophagic membrane from residency on the peroxisomal cargo. Assess conservation from experimentally characterized VPS34 orthologs without requiring a new experiment for every conserved role.

## Term and Decision Context

No specific term context supplied.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: Human PIK3C3 participates in pexophagy (GO:0000425) and localizes to the peroxisome (GO:0005777).
  Adjudicate these two claims independently. Identify the catalytic and complex machinery for mammalian
  pexophagy and distinguish localization on an engulfing autophagic membrane from residency on the peroxisomal
  cargo. Assess conservation from experimentally characterized VPS34 orthologs without requiring a new
  experiment for every conserved role.
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

# PIK3C3 (VPS34, Q8NEB9): Pexophagy and Peroxisome Localization — Focused Curation Review

**Focus type:** function_assignment · **Hypothesis slug:** pexophagy-and-peroxisome-localization
**Terms adjudicated:** GO:0000425 *pexophagy* (BP) and GO:0005777 *peroxisome* (CC)
**Final report** (compiled across 3 iterations; provenance verified via UniProt + QuickGO, 2026-09-21)

---

## Executive Judgment

**GO:0000425 pexophagy (BP): PARTIALLY SUPPORTED (retain as a conserved role).**
**GO:0005777 peroxisome (CC): WEAKLY SUPPORTED / likely OVER-ANNOTATED (flag; consider removal or non-core).**

Both terms on human PIK3C3 are annotated **IBA (Inferred from Biological aspect of Ancestor)** from GO_Central — phylogenetic propagation within the VPS34 family, **not** human experimental evidence (UniProt Q8NEB9, fetched 2026-09-21). They must be adjudicated separately:

- **Pexophagy is a real conserved VPS34 role.** Yeast Vps34 (with its PtdIns3P-binding effectors) is experimentally *mandatory* for regulated peroxisome degradation (PMID 21121900). Mammalian pexophagy uses the same core class III PI3K/ATG apparatus to build the engulfing autophagosome. VPS34's contribution is generating **PI3P on the phagophore/omegasome**, an indirect-but-required function. An IBA BP annotation here is defensible; the caveat is that it is a *general-autophagy-derived* role, with no human IDA/IMP.

- **Peroxisome as a cellular component is the weak claim.** Human VPS34's directly demonstrated locations are **late endosome, autophagosome, midbody, plasma membrane, and phagophore assembly site** — not the peroxisome. The CC:peroxisome IBA most plausibly propagated from the yeast observation that "Vps34 is … associated with peroxisomes during biogenesis" (PMID 21121900). This conflates the **engulfing autophagic membrane** with **residency on the peroxisomal cargo**, exactly the distinction the seed hypothesis asks curators to make. The correct location term (GO:0000407 phagophore assembly site) is *already annotated*, making CC:peroxisome redundant and misleading for human.

**Most important caveat:** absence of a human peroxisome-localization assay is not proof of absence, but the well-characterized VPS34 localization repertoire argues against stable peroxisomal residency.

### Annotation lineage (QuickGO, fetched 2026-09-21)

Both human terms are PAINT propagations (GO_REF:0000033, ECO:0000318) through **PANTHER family PTN000005955**, with `withFrom` = **SGD:S000004230 (yeast VPS34, UniProt P22543)**. Tracing to the source, each human IBA rests on **a single yeast experimental annotation from one paper (PMID 21121900)**:

| Human term (Q8NEB9) | Human evidence | Propagated from | Yeast source evidence | Source ref | Conservation reliability |
|---|---|---|---|---|---|
| GO:0000425 pexophagy (BP) | IBA (ECO:0000318) | SGD S000004230 (yeast VPS34) | **IMP** (ECO:0000315, mutant phenotype) | PMID 21121900 | **High** — process roles transfer well across VPS34 orthologs |
| GO:0005777 peroxisome (CC) | IBA (ECO:0000318) | SGD S000004230 (yeast VPS34) | **IDA** (ECO:0000314, direct localization) | PMID 21121900 | **Low** — subcellular location is organism-specific and transfers poorly by orthology; contradicts curated human VPS34 locations |

This is the crux: the **process** claim is grounded in a yeast mutant-phenotype assay and conserves robustly; the **location** claim is grounded in a yeast *localization* assay whose organism-specific peroxisomal association is not expected to (and empirically does not) transfer to human VPS34, whose demonstrated locations are endosome/autophagosome/midbody/plasma membrane. Note both yeast source annotations derive from the **same single publication**, so neither human IBA has independent corroboration.

---

## Evidence Matrix

| Citation | Evidence type | Stance | Claim tested | Key finding | Context | Confidence / limitations |
|---|---|---|---|---|---|---|
| PMID 21121900 (Grunau 2011) | Direct assay / localization | Supports BP; origin of CC | Vps34/PI3P required for pexophagy; Vps34 peroxisome association | Vps34-complex I + PtdIns3P-binding proteins "mandatory for the regulated degradation of peroxisomes"; peroxisomal PtdIns3P activity; Vps34 associated with peroxisomes during biogenesis | *S. cerevisiae* | High for BP conservation; **yeast-specific** for CC peroxisome association |
| PMID 27597759 (Sargent 2016) | Mutant phenotype / mechanism | Qualifies | Mammalian pexophagy cargo-selection machinery | PEX2 E3 ligase ubiquitinates PEX5/PMP70; NBR1-dependent autophagic clearance | Human/mouse cells, in vivo | High; VPS34 not implicated as cargo-resident |
| PMID 19223761 (Itakura 2009) | Localization / complex biology | Qualifies | Where mammalian VPS34 acts | ATG14 complex → isolation membrane/phagophore (autophagy); UVRAG → late endosome | Mammalian cells | High; supports engulfing-membrane, not peroxisome residency |
| PMID 36076954 (Zhao 2022) | Localization / mechanism | Qualifies | PI3P/Vps34 spatiotemporal control in autophagy | Vps34-PI3K on endosomes/PAS; PI3P recruits WIPI → ATG conjugation | Yeast | Moderate; general autophagy |
| UniProt Q8NEB9 | Database / provenance | Competing | Evidence code of target terms | GO:0005777 peroxisome = **IBA**; GO:0000425 pexophagy = **IBA**; curated locations = endosome/autophagosome/midbody/PM | Human | Definitive on provenance; both target terms are phylogenetic-only |
| QuickGO / SGD S000004230 (P22543) | Structural/evolutionary (annotation lineage) | Competing / qualifies | Source of the human IBA propagation | Both human IBAs trace via PANTHER PTN000005955 to yeast VPS34: peroxisome = **IDA** (ECO:0000314), pexophagy = **IMP** (ECO:0000315), both PMID 21121900 | Human ← *S. cerevisiae* | Definitive on lineage; single-paper origin, no independent human support; location conserves poorly |

Artifacts: `/tmp/PIK3C3_pexophagy_evidence_matrix.csv` (evidence matrix); UniProt GO dump reproduced in-run.

---

## GO Curation Implications (leads — require curator verification)

| GO ID | Term | Aspect | Current evidence | Lead action | Rationale |
|---|---|---|---|---|---|
| GO:0000425 | pexophagy | BP | IBA:GO_Central | **Retain** (conserved, non-core) | Experimentally required in yeast (PMID 21121900); mammalian pexophagy uses core PI3K/ATG machinery. IBA is appropriate; label as conserved general-autophagy role, not a human-demonstrated dedicated function. |
| GO:0005777 | peroxisome | CC | IBA:GO_Central | **Flag → consider REMOVE or mark non-core** | Human VPS34 localizes to endosome/autophagosome/**phagophore assembly site (GO:0000407, already annotated)**, not the peroxisome. IBA likely conflates the engulfing membrane with peroxisomal cargo residency. |

- The **MF** basis of the gene product (GO:0016303 PI 3-kinase activity, IDA) is solid and is the mechanistic root of any pexophagy role.
- Do **not** default to "protein binding"; the informative location term for VPS34's autophagy action already exists (GO:0000407).

---

## Mechanistic Scope

- **Direct molecular activity:** VPS34 is the catalytic subunit of class III PI3K; it phosphorylates PtdIns to **PI3P**. In autophagy it operates within **Complex I** (VPS34–VPS15/PIK3R4–Beclin1–ATG14) on the phagophore/omegasome, and **Complex II** (with UVRAG) on endosomes.
- **Pexophagy (indirect, required):** PI3P produced on the engulfing membrane recruits WIPI/ATG effectors that build the autophagosome around a peroxisome that has been **selected** by cargo machinery (PEX2 ubiquitination → NBR1/p62). VPS34's role is *enabling autophagosome formation*, not selecting or residing on peroxisomes.
- **Downstream/context effects to keep separate:** peroxisome number regulation, lipid metabolism, IFN-III/MAVS antiviral signaling (PMID 41186416) are consequences of pexophagy flux, not VPS34 molecular functions.

---

## Conflicts and Alternatives

- **Paralog/ortholog carry-over:** The CC:peroxisome and BP:pexophagy IBAs derive from the yeast *Vps34* ancestor. Yeast Vps34 associating with peroxisomes (PMID 21121900) is an **organism-specific** localization not shown for human VPS34 — a classic IBA over-reach for CC.
- **Machinery vs cargo confusion:** Mammalian pexophagy specificity is conferred by PEX2/NBR1 (PMID 27597759); VPS34 is a shared upstream factor for *all* macroautophagy. Assigning a peroxisome CC to a pan-autophagy kinase risks propagating cargo terms to every selective-autophagy factor.
- **No isoform-specific peroxisomal targeting** is reported for PIK3C3.

---

## Knowledge Gaps

1. **Human VPS34 at peroxisomes?** Checked: UniProt curated locations — none peroxisomal. Matters because it is the crux of the CC decision. *Resolve:* high-resolution colocalization (VPS34/PI3P biosensor vs PMP70) during induced pexophagy; APEX2 peroxisomal proximity labeling.
2. **Is human pexophagy VPS34-dependent experimentally?** Checked: no human IDA/IMP found; inference is by conservation. *Resolve:* PIK3C3 KO/inhibitor (SAR405/VPS34-IN1) block of PEX2-driven peroxisome clearance.
3. **Which VPS34 complex drives pexophagy** (ATG14 vs UVRAG)? *Resolve:* ATG14/UVRAG depletion during starvation-induced pexophagy.

---

## Discriminating Tests

- **VPS34 inhibitor (SAR405/VPS34-IN1) + PEX2 overexpression** → does peroxisome clearance require VPS34 activity in human cells? (tests BP causally in human).
- **PI3P biosensor (2×FYVE) live imaging during pexophagy** → is PI3P generated on the nascent phagophore around the peroxisome, and is VPS34 recruited to the *phagophore* rather than the peroxisome membrane? (discriminates engulfing-membrane vs cargo residency → the CC question).
- **Peroxisomal APEX2 proximity proteomics** → is endogenous VPS34 a peroxisomal neighbor? Negative result would support removing CC:peroxisome.

---

## Curation Leads (require curator verification)

- **Reference to attach for BP pexophagy (conservation):** PMID 21121900 — snippet: *"The function of Vps34p-containing complex I as well as a subset of PtdIns3P-binding proteins proved to be mandatory for the regulated degradation of peroxisomes. This demonstrates that PtdIns3P-mediated signalling is required for pexophagy."*
- **Reference clarifying mammalian machinery (VPS34 not cargo-resident):** PMID 27597759 — *"the peroxisomal E3 ubiquitin ligase peroxin 2 (PEX2) is the causative agent for mammalian pexophagy … degradation of peroxisomes in an NBR1-dependent autophagic process."*
- **Reference for correct location of VPS34 activity:** PMID 19223761 — *"Atg14 localizes to isolation membrane/phagophore during starvation and is essential for autophagosome formation."*
- **Action change candidates:**
  - GO:0000425 (BP): **retain**; annotate as conserved/non-core; keep IBA (no human experimental upgrade available).
  - GO:0005777 (CC): **flag for removal or reclassification as non-core**; GO:0000407 (phagophore assembly site) already captures the correct autophagy location.
- **Suggested curator questions:** (1) Is there any human dataset placing VPS34 at the peroxisome membrane/lumen? (2) Should pan-autophagy factors inherit selective-autophagy cargo CC terms by IBA at all?
- **Suggested experiments:** VPS34-inhibitor pexophagy block; 2×FYVE/PI3P imaging; peroxisomal APEX2 proximity labeling (above).

---

### Bottom line
Adjudicated independently: **pexophagy (BP) is a genuine conserved VPS34 role — retain (non-core, conservation-based); peroxisome (CC) is over-annotated for human VPS34 — flag for removal/non-core**, because VPS34 acts on the *engulfing autophagic membrane* (phagophore, already annotated as GO:0000407), not as a resident of the peroxisomal cargo. Both current annotations are IBA-only, so neither reflects human experimental evidence.
