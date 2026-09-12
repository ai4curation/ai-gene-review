---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-11T06:13:03.105227'
end_time: '2026-07-11T06:33:53.234014'
duration_seconds: 1250.13
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: BACSU
  gene: spoIIGA
  gene_symbol: spoIIGA
  uniprot_accession: P13801
  taxon_id: NCBITaxon:224308
  taxon_label: Bacillus subtilis (strain 168)
  focus_type: computational_prediction
  hypothesis_slug: prediction-aspartic-endopeptidase
  hypothesis_text: GO-GPT (via BioReason-Pro) predicts aspartic-type endopeptidase
    activity (GO:0004190) for the Bacillus subtilis sporulation protein SpoIIGA (P13801),
    the membrane-bound protease that processes pro-sigma-E to active sigma-E in the
    mother cell during sporulation. Independently assess whether SpoIIGA is an aspartic-type
    endopeptidase -- i.e. whether it has the catalytic machinery of an aspartic protease
    (a paired catalytic aspartate dyad in an aspartic-protease/pepsin-like fold) --
    or whether it belongs to a different protease class or mechanism, which bears
    on whether the aspartic-type-endopeptidase molecular-function prediction is supported.
    Determine whether the prediction is supported or refuted.
  term_context: '- Term: aspartic-type endopeptidase activity (GO:0004190)'
  reference_context: '- doi:10.64898/2026.03.19.712954'
  source_file: ''
  source_selector: ''
  source_context_yaml: "hypothesis: GO-GPT (via BioReason-Pro) predicts aspartic-type\
    \ endopeptidase activity (GO:0004190) for\n  the Bacillus subtilis sporulation\
    \ protein SpoIIGA (P13801), the membrane-bound protease that processes\n  pro-sigma-E\
    \ to active sigma-E in the mother cell during sporulation. Independently assess\
    \ whether SpoIIGA\n  is an aspartic-type endopeptidase -- i.e. whether it has\
    \ the catalytic machinery of an aspartic protease\n  (a paired catalytic aspartate\
    \ dyad in an aspartic-protease/pepsin-like fold) -- or whether it belongs\n  to\
    \ a different protease class or mechanism, which bears on whether the aspartic-type-endopeptidase\
    \ molecular-function\n  prediction is supported. Determine whether the prediction\
    \ is supported or refuted.\nfocus_type: computational_prediction\nterm_id: GO:0004190\n\
    term_label: aspartic-type endopeptidase activity\ncontext: []\nreference_id:\n\
    - doi:10.64898/2026.03.19.712954"
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

- **Organism code:** BACSU
- **Taxon:** Bacillus subtilis (strain 168) (NCBITaxon:224308)
- **Gene directory:** spoIIGA
- **Gene symbol:** spoIIGA
- **UniProt accession:** P13801

## Focus

- **Focus type:** computational_prediction
- **Hypothesis slug:** prediction-aspartic-endopeptidase
- **Source file:** 
- **Source selector:** 

## Seed Hypothesis

GO-GPT (via BioReason-Pro) predicts aspartic-type endopeptidase activity (GO:0004190) for the Bacillus subtilis sporulation protein SpoIIGA (P13801), the membrane-bound protease that processes pro-sigma-E to active sigma-E in the mother cell during sporulation. Independently assess whether SpoIIGA is an aspartic-type endopeptidase -- i.e. whether it has the catalytic machinery of an aspartic protease (a paired catalytic aspartate dyad in an aspartic-protease/pepsin-like fold) -- or whether it belongs to a different protease class or mechanism, which bears on whether the aspartic-type-endopeptidase molecular-function prediction is supported. Determine whether the prediction is supported or refuted.

## Term and Decision Context

- Term: aspartic-type endopeptidase activity (GO:0004190)

## Reference Context

- doi:10.64898/2026.03.19.712954

## Source Context YAML

```yaml
hypothesis: GO-GPT (via BioReason-Pro) predicts aspartic-type endopeptidase activity (GO:0004190) for
  the Bacillus subtilis sporulation protein SpoIIGA (P13801), the membrane-bound protease that processes
  pro-sigma-E to active sigma-E in the mother cell during sporulation. Independently assess whether SpoIIGA
  is an aspartic-type endopeptidase -- i.e. whether it has the catalytic machinery of an aspartic protease
  (a paired catalytic aspartate dyad in an aspartic-protease/pepsin-like fold) -- or whether it belongs
  to a different protease class or mechanism, which bears on whether the aspartic-type-endopeptidase molecular-function
  prediction is supported. Determine whether the prediction is supported or refuted.
focus_type: computational_prediction
term_id: GO:0004190
term_label: aspartic-type endopeptidase activity
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

# SpoIIGA (P13801, BACSU) — Aspartic-type Endopeptidase Prediction Review

**Hypothesis under review:** GO-GPT (via BioReason-Pro) predicts **aspartic-type endopeptidase activity (GO:0004190)** for *Bacillus subtilis* SpoIIGA, the membrane protease that processes pro-σE to σE in the mother cell.

**Focus type:** computational_prediction · **Term:** GO:0004190 aspartic-type endopeptidase activity

---

## Executive Judgment

**Verdict: SUPPORTED (with a fold caveat).**

Independent primary literature and curated database evidence converge on SpoIIGA being an **aspartic-type endopeptidase**:

- Direct mutational + homology-modeling study concludes SpoIIGA is *"a novel type of aspartic protease"* whose catalytic (C-terminal) domain **dimerizes like HIV-1 protease** (Imamura et al. 2008, **PMID 18378688**), reaffirmed in Imamura et al. 2011 (**PMID 21362630**).
- UniProt (SP2G_BACSU / P13801) annotates it as *"Sporulation sigma-E factor-processing peptidase"*, **EC 3.4.23.-** (the aspartic-endopeptidase EC class), keyword **"Aspartyl protease"**, and **MEROPS family A36.001** — SpoIIGA is the *holotype* of aspartic-peptidase family A36.
- The single UniProt-annotated **active site is Asp183**, embedded in a canonical aspartic-protease catalytic motif **D183-S184-G185 (D-S-G)** — directly homologous to the HIV-1 protease **D25-T26-G27 (DTG)** motif. Mutagenesis of residues 181/182/**183**/184 abolishes pro-σE cleavage (D183 abolishes cleavage of wild-type SigE).

The one caveat: the aspartic mechanism is established by **catalytic-aspartate mutagenesis + homology modeling**, not by an experimental crystal structure. SpoIIGA is a **divergent, dimeric (retropepsin/HIV-like), membrane-associated** aspartic protease, not a classical monomeric pepsin-fold enzyme. GO:0004190 does not require the pepsin fold — it requires the aspartic catalytic mechanism — so the term is appropriate. The prediction is therefore **correct**, and if anything is *more* specific and better supported than the historical "putative protease of unknown mechanism" status (Pfam still uses the legacy name **Peptidase_U4**, "U" = unknown catalytic type).

---

## Evidence Matrix

| # | Citation | Evidence type | Supports/Refutes/Qualifies | Claim tested | Key finding | Context | Confidence & limitations |
|---|----------|---------------|----------------------------|--------------|-------------|---------|--------------------------|
| 1 | Imamura, Zhou, Feig, Kroos 2008 — **PMID 18378688** | Structural modeling + mutagenesis + reconstitution | **Supports** | Is SpoIIGA an aspartic protease? | *"SpoIIGA is a novel type of aspartic protease whose C-terminal half forms a dimer similar to the HIV-1 protease"*; SpoIIR+SpoIIGA sufficient to process pro-σE in *E. coli*; catalytic-Asp mutations abolish cleavage | *B. subtilis* / *E. coli* reconstitution; sporulation | High for aspartic mechanism; fold from modeling, not crystallography |
| 2 | Imamura, Kuwana, Kroos, Feig, Takamatsu, Watabe 2011 — **PMID 21362630** | Mutagenesis / substrate specificity | **Supports / qualifies** | Aspartic protease classification + substrate recognition | *"SpoIIGA is a novel type of membrane-associated aspartic protease… cleaving Pro-σ(E)"*; basic residues 245/284 (substrate binding, not catalytic) contribute to specificity | Cross-species *Bacillus* orthologs, *E. coli* co-expression | High; distinguishes catalytic (D183) from substrate-recognition residues (R245, K284) |
| 3 | UniProt **P13801** (SP2G_BACSU) | Database record | **Supports** | Curated MF classification | EC **3.4.23.-**; keyword "Aspartyl protease"; **active site Asp183**; MEROPS **A36.001** (family holotype); 5 N-terminal TM helices + C-terminal protease domain | Curated, reference proteome | High as curated synthesis; itself informed by refs 1–2 |
| 4 | This analysis (sequence motif scan) | Computational (sequence) | **Supports** | Presence of aspartic catalytic motif | Asp183 sits in a **D-S-G** motif (positions 183–185), homologous to HIV-1 protease DTG dyad; C-terminal cytoplasmic domain | Computed on P13801 sequence | High; motif presence consistent with dimeric aspartic mechanism |
| 5 | Fawcett, Melnikov, Youngman 1998 — **PMID 9663680**; Hofmeister 1998 — PMID 9573195 | Localization / interaction | **Qualifies (context)** | Where/how SpoIIGA acts | SpoIIGA targets to the sporulation septum membrane; forms a complex with pro-σE | *B. subtilis* sporulation | Supports CC (membrane/septum) + substrate interaction, not MF class |
| 6 | Pfam **PF03419** "Peptidase_U4" | Database (legacy) | **Qualifies** | Historical mechanism uncertainty | Domain retains "U4" (unknown catalytic type) name predating 2008 reclassification to aspartic (MEROPS A36) | Domain family | Reflects that aspartic call is a post-2008 refinement, now well supported |
| 7 | This analysis — ortholog alignment (UniProt P13801, D5DQW6, Q45832) | Computational (evolutionary/orthology) | **Supports** | Is the catalytic Asp motif conserved across the family? | Catalytic **D-[S/T]-G** motif conserved: *B. subtilis* D183-S-G, *P. megaterium* D183-S-G, *C. acetobutylicum* D174-T-G (DTG); flanking L-D-[S/T]-G-N pattern conserved | Bacillus → Priestia → Clostridium orthologs | High; conservation across phyla argues against lineage-specific artifact |
| 8 | This analysis — AlphaFold model AF-P13801-F1 (v6) | Computational (structural, predicted) | **Qualifies** | Is D183 in a confidently modeled protease fold? | Mean pLDDT 85; catalytic Asp183/DSG region pLDDT 80–93; res183=ASP. Monomer model cannot show the inter-subunit dyad | Predicted structure only; no experimental PDB | Moderate; supports residue identity/fold confidence but not the dimeric dyad geometry |

---

## Evolutionary Conservation of the Catalytic Motif (computed this run)

Alignment of reviewed SpoIIGA orthologs (UniProt) confirms the catalytic aspartate sits in a conserved aspartic-protease **D-[S/T]-G** motif, independent of the *B. subtilis*-specific mutagenesis:

| Ortholog | Organism | Length | EC | MEROPS | Catalytic motif (position) | Local context |
|----------|----------|--------|-----|--------|----------------------------|---------------|
| **P13801** | *Bacillus subtilis* 168 | 309 | 3.4.23.- | A36.001 | **D183-S-G** | `GLIDSGNQLYD` |
| **D5DQW6** | *Priestia (Bacillus) megaterium* | 307 | 3.4.23.- | A36.001 | **D183-S-G** | `GLIDSGNQLVD` |
| **Q45832** | *Clostridium acetobutylicum* | 266 | 3.4.23.- | — | **D174-T-G** | `FLDTGNELRE` |

The catalytic Asp and its flanking **L-D-[S/T]-G-N** pattern are conserved from *Bacillus* to the distant *Clostridium* ortholog (which carries the classical **DTG** variant, identical in type to HIV-1 protease). This is orthogonal evolutionary support that the aspartic catalytic residue is a genuine, maintained feature of the SpoIIGA family, not a lineage-specific artifact. (Provenance: UniProt REST retrieval + regex motif scan executed in Iteration 2.)

---

## GO Curation Implications (leads — require curator verification)

- **Retain / assign GO:0004190 (aspartic-type endopeptidase activity)** as the SpoIIGA molecular-function term. It is biologically supported by direct mutational evidence (catalytic D183 in a DSG motif) plus curated MEROPS A36 / EC 3.4.23.- classification. The GO-GPT prediction is **correct and appropriately specific** (more informative than "peptidase activity" or "protein binding").
- **Recommended evidence basis:** because the aspartic mechanism rests on homology modeling + mutagenesis (not a solved structure), the most defensible support is a **sequence/mutation-based** or **author-statement** basis citing PMID 18378688 and 21362630, rather than a direct enzymological demonstration of aspartic-class inhibitor sensitivity. Curator may prefer ISS/IMP-flavored evidence with these PMIDs over IDA.
- **Companion terms that are also well supported** (for completeness, not part of this focus): BP **GO:0042174 negative regulation of sporulation / sigma-factor processing / GO:0030436 asexual sporulation** context via pro-σE processing; CC **GO:0005886 plasma membrane** / sporulation septum (5 TM helices, septal localization, PMID 9663680). MF could optionally note substrate = sigma-factor precursor.
- **Do not** downgrade to generic "protein binding" — a specific catalytic MF term is supported.

## Mechanistic Scope

- **Direct molecular function (what GO:0004190 tests):** SpoIIGA is the endopeptidase that hydrolyzes a peptide bond in **pro-σE**, removing the 27-residue pro-sequence to release active σE. Catalysis uses an **aspartic mechanism**: the C-terminal cytoplasmic domain dimerizes so that two copies of the **D183(S184)(G185)** motif form the paired catalytic aspartate dyad (retropepsin/HIV-1-protease-like).
- **Distinct from downstream phenotypes:** the sporulation defect of *spoIIGA* mutants, mother-cell/forespore compartmentalization of σE activity, and the intercellular SpoIIR→SpoIIGA signaling are **downstream/contextual** consequences, not the molecular activity itself. The N-terminal 5-TM domain is a **membrane signal-receiving/regulatory module** (senses SpoIIR), not the catalytic center.

## Conflicts and Alternatives

- **No primary evidence assigns SpoIIGA to a different protease class** (serine/cysteine/metallo). The only "conflict" is historical/nomenclatural: SpoIIGA was long a *"putative protease"* of unknown mechanism (Pfam **Peptidase_U4**, "U" = unknown), and some early models entertained that SpoIIGA might be a regulator of an unidentified protease. The 2008 *E. coli* reconstitution (SpoIIR + SpoIIGA **sufficient**) plus catalytic-Asp mutagenesis resolved this in favor of SpoIIGA being the aspartic protease itself.
- **Paralog/ortholog confusion:** low risk. SpoIIGA orthologs across *Bacillus* share the mechanism; the closest mechanistic analog is HIV-1 protease (fold analogy, not homology). Substrate-recognition residues (R245, K284) are sometimes mis-read as "catalytic" because their mutation abolishes cleavage, but 2011 data show these are **substrate-binding**, not the catalytic dyad.
- **In-vitro-only concern:** not applicable — activity is demonstrated in the physiological *B. subtilis* pathway and reconstituted heterologously.

## Knowledge Gaps

1. **No experimental 3D structure.** Checked: UniProt lists only an AlphaFoldDB model (no PDB). I retrieved the AlphaFold model (AF-P13801-F1, v6): mean pLDDT = **85.0** (high confidence), C-terminal protease domain (151–309) mean pLDDT = 85.0, and the catalytic **Asp183/DSG** region is confidently modeled (pLDDT 80–93, res183 = ASP as annotated). However, the *functional* active site is an **inter-subunit dimer dyad**, which a monomer model cannot display — so the pepsin/HIV-like fold and the two-Asp active site remain **inferred from modeling + mutagenesis + conservation**, not observed. A crystal/cryo-EM structure of the dimer (ideally with a transition-state analog or pepstatin-class inhibitor bound) would confirm the aspartic dyad geometry. Matters because GO:0004190's mechanistic basis currently rests on indirect evidence.
2. **Second catalytic aspartate identity.** Checked: UniProt annotates only one active site (D183) because catalysis is provided by a **homodimer** contributing two D183 copies; whether an intramolecular second Asp also contributes is not experimentally pinned. Resolving this needs the structure or a mixed-dimer complementation assay.
3. **Inhibitor sensitivity.** No report (found) of classic aspartic-protease inhibitor (pepstatin A) inhibiting SpoIIGA. A positive result would provide orthogonal, direct enzymological confirmation of the aspartic class.

## Discriminating Tests

- **Structure determination** of the C-terminal domain dimer (± substrate/inhibitor) to visualize the paired Asp dyad — the single most decisive test.
- **Pepstatin A / aspartic-protease inhibitor** sensitivity assay on reconstituted pro-σE cleavage (positive = confirms class; important because SpoIIGA is divergent and might be inhibitor-insensitive).
- **Catalytic-dyad complementation:** co-express two SpoIIGA D183 point mutants that could complement in trans within a dimer; restoration of activity confirms the shared dimeric aspartic active site.
- **AlphaFold2/3 model inspection** of the C-terminal domain for spatial apposition of two D183-S-G motifs at a dimer interface (fast, in-silico corroboration).

## Curation Leads (verify before applying)

- **Action:** support/keep MF **GO:0004190** for SpoIIGA (P13801). Prediction is **correct**.
- **Candidate references (with snippets to verify):**
  - **PMID 18378688** — *"SpoIIGA is a novel type of aspartic protease whose C-terminal half forms a dimer similar to the human immunodeficiency virus type 1 protease."*
  - **PMID 21362630** — *"SpoIIGA is a novel type of membrane-associated aspartic protease that responds to a signal from the forespore by cleaving Pro-σ(E)…"*
  - **Database:** UniProt P13801 (EC 3.4.23.-, "Aspartyl protease", active site D183); MEROPS **A36.001**.
- **Suggested qualifier/note for curator:** flag that the mechanism is **modeling + mutagenesis-based** (no crystal structure) and that the enzyme is a **divergent membrane-associated dimeric aspartic protease** (family A36), so evidence code should reflect sequence/experiment-inference rather than direct structural proof.
- **Suggested questions:** Is there any pepstatin-sensitivity or structural datum post-2011 that would upgrade the evidence to IDA-level? Should the substrate (sigma-factor precursor) be captured via a "with/from" or extension?
- **Suggested experiment:** pepstatin inhibition + cryo-EM of the SpoIIGA/pro-σE complex.

---

### Bottom line
The aspartic-type endopeptidase prediction for SpoIIGA is **supported** by convergent mutational, database, and sequence-motif evidence. SpoIIGA is the founding member of MEROPS aspartic-peptidase family A36, carries a catalytic Asp183 in a D-S-G motif, and functions as a dimeric HIV-protease-like aspartic endopeptidase — with the only reservation that the fold/dyad is established by modeling and mutagenesis rather than an experimental structure.


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)