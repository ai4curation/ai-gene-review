---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-24T04:33:58.930608'
end_time: '2026-06-24T04:47:46.340948'
duration_seconds: 827.41
template_file: templates/treegrafter_function_hypothesis.md
template_variables:
  organism: DOROP
  gene: ADAR2
  gene_symbol: ADAR2
  uniprot_accession: C1JAR3
  taxon_id: NCBITaxon:1051066
  taxon_label: Doryteuthis opalescens
  focus_type: function_assignment
  hypothesis_slug: function-hypothesis-go-0008251
  hypothesis_text: ADAR2 has tRNA-specific adenosine deaminase activity (GO:0008251).
  term_context: '- Term: tRNA-specific adenosine deaminase activity (GO:0008251)

    - Evidence type: IEA

    - Original reference: GO_REF:0000118'
  reference_context: '- GO_REF:0000118

    - PMID:37342458

    - PMID:19390115'
  source_file: genes/DOROP/ADAR2/ADAR2-ai-review.yaml
  source_selector: existing_annotations[10].function_hypothesis
  source_context_yaml: "term:\n  id: GO:0008251\n  label: tRNA-specific adenosine\
    \ deaminase activity\nevidence_type: IEA\noriginal_reference_id: GO_REF:0000118"
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 25
artifact_count: 2
artifact_sources:
  edison_answer_artifacts: 2
artifacts:
- filename: artifact-00.md
  path: falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: falcon_artifacts/artifact-01.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-01
---

## Question

# AIGR TreeGrafter Function-Inference Stress Test

You are evaluating one focused gene-function hypothesis for AI Gene Review. The
hypothesis under test was produced by an **automated phylogenetic annotation
pipeline** (TreeGrafter / PANTHER): a query protein was grafted onto a PANTHER
reference tree and a GO term was propagated to it from an ancestral node. Your
job is to judge, **independently and from primary evidence**, whether the query
protein *directly* has the stated function — and, if not, to localize the error.

This is not a general gene overview. Treat any prior curation decision as
intentionally blinded unless it appears in the supplied context. Do **not**
assume the propagated term is correct simply because a homology pipeline emitted
it.

## Target Gene

- **Organism code:** DOROP
- **Taxon:** Doryteuthis opalescens (NCBITaxon:1051066)
- **Gene directory:** ADAR2
- **Gene symbol:** ADAR2
- **UniProt accession:** C1JAR3

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** function-hypothesis-go-0008251
- **Source file:** genes/DOROP/ADAR2/ADAR2-ai-review.yaml
- **Source selector:** existing_annotations[10].function_hypothesis

## Seed Hypothesis (propagated by TreeGrafter/PANTHER)

ADAR2 has tRNA-specific adenosine deaminase activity (GO:0008251).

## Term and Decision Context

- Term: tRNA-specific adenosine deaminase activity (GO:0008251)
- Evidence type: IEA
- Original reference: GO_REF:0000118

## Reference Context

- GO_REF:0000118
- PMID:37342458
- PMID:19390115

## Source Context YAML

```yaml
term:
  id: GO:0008251
  label: tRNA-specific adenosine deaminase activity
evidence_type: IEA
original_reference_id: GO_REF:0000118
```

## Research Objective

Decide whether **ADAR2 directly has the stated function**. Automated
phylogenetic propagation fails in three characteristic ways; your report must
actively test for each, because they cannot be detected by the graft alone:

1. **Granularity / family-vs-subfamily.** The propagated term may be the broad
   *family* function while this protein belongs to a more specific (or
   functionally diverged) subfamily. Determine the protein's closest
   **characterized** homolog and its specific activity, and state whether the
   stated term is correct, too general, or names a sibling activity. (Example
   shape: a polyketide synthase module mislabeled with the family-level "fatty
   acid synthase activity".)
2. **Pseudo-enzyme / loss of activity.** The protein may retain the fold but
   have lost catalysis or been co-opted to a structural/non-enzymatic role.
   Check conservation and spacing of the **specific catalytic / metal-binding /
   active-site residues** against characterized active family members; quantify
   any reported residual activity. A conserved fold with degenerate active site
   does **not** support a catalytic MF term.
3. **Within-superfamily mis-placement.** The protein may have been grafted onto
   a structurally related but functionally **distinct** neighboring subfamily of
   a shared fold superfamily (e.g. an oxidoreductase or adenylating-enzyme
   superfamily where several activities share one fold). Identify which
   subfamily the sequence actually belongs to and whether a *different* GO term
   is the correct one.

Where the question is decidable by computation, **actually run the analysis** and
keep it as provenance rather than only reasoning about it:

- **Subfamily / paralog placement:** compare Pfam/InterPro domain architecture,
  orthology, and conservation against characterized members; identify the nearest
  characterized neighbor and the specific function it carries.
- **Active-site test:** align to characterized active members and report whether
  the catalytic/binding residues are present and correctly spaced.
- **Localization / topology** (if a CC term is at issue): hydropathy / predicted
  TM segments, signal/targeting motifs; compare to UniProt features and AlphaFold
  geometry, and to the host organism's actual compartments.

Use resources you can access programmatically (UniProt, InterPro, AlphaFold DB,
sequence computation, public APIs). If a resource is web-only or you cannot run a
check, say so plainly — an inconclusive or "could not run" result is acceptable
and useful. **Never fabricate a result.** Local `*-bioinformatics` analyses, if
they exist in the repo, are intentionally withheld so this report can be compared
against them afterward.

## Required Output

### Executive Judgment

Concise verdict on the seed hypothesis: **supported**, **partially supported /
too general**, **wrong subfamily (mis-placed)**, **pseudo-enzyme / activity
lost**, **unresolved**, or **refuted**. Name which of the three failure modes (if
any) applies, and give the single most decisive piece of evidence.

### Independent Family/Function Assignment

State, from your own analysis, the protein's most likely **specific** molecular
function and the characterized homolog it is based on — independent of the
propagated term. Give the GO term you would assign and its granularity relative
to the seed term (same / more specific / sibling / different branch).

### Evidence Matrix

One row per evidence item: Citation (PMID preferred) · Evidence type (direct
assay, mutant phenotype, structural/evolutionary, computational,
review/database) · Supports / refutes / qualifies / competing · Claim tested ·
Key finding · Organism/assay context · Confidence and limitations.

### Active-Site / Placement Analysis

Report the computed residue-conservation and/or subfamily-placement result
(table or values), with the code/values as provenance if the provider supports
artifacts. State explicitly whether catalytic residues are intact.

### GO Curation Implications

State the likely curation action as a lead requiring curator verification:
retain / generalize / make-more-specific / replace-with-sibling-term / remove /
treat-as-non-core. Avoid "protein binding" as a final recommendation.

### Conflicts, Knowledge Gaps, Discriminating Tests

Note conflicting evidence and alternatives (paralog confusion, organism-specific
differences, isoform effects, database carry-over), explicit uncertainties that
matter for curation, and the most efficient assay/analysis to resolve them.

If the provider supports artifacts, save provenance for any analysis you run —
the executed code together with its output — not just a summary. Do not
synthesize a figure implying an analysis you did not run.


## Output

Question: You are an expert researcher providing comprehensive, well-cited information.

Provide detailed information focusing on:
1. Key concepts and definitions with current understanding
2. Recent developments and latest research (prioritize 2023-2024 sources)
3. Current applications and real-world implementations
4. Expert opinions and analysis from authoritative sources
5. Relevant statistics and data from recent studies

Format as a comprehensive research report with proper citations. Include URLs and publication dates where available.
Always prioritize recent, authoritative sources and provide specific citations for all major claims.

# AIGR TreeGrafter Function-Inference Stress Test

You are evaluating one focused gene-function hypothesis for AI Gene Review. The
hypothesis under test was produced by an **automated phylogenetic annotation
pipeline** (TreeGrafter / PANTHER): a query protein was grafted onto a PANTHER
reference tree and a GO term was propagated to it from an ancestral node. Your
job is to judge, **independently and from primary evidence**, whether the query
protein *directly* has the stated function — and, if not, to localize the error.

This is not a general gene overview. Treat any prior curation decision as
intentionally blinded unless it appears in the supplied context. Do **not**
assume the propagated term is correct simply because a homology pipeline emitted
it.

## Target Gene

- **Organism code:** DOROP
- **Taxon:** Doryteuthis opalescens (NCBITaxon:1051066)
- **Gene directory:** ADAR2
- **Gene symbol:** ADAR2
- **UniProt accession:** C1JAR3

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** function-hypothesis-go-0008251
- **Source file:** genes/DOROP/ADAR2/ADAR2-ai-review.yaml
- **Source selector:** existing_annotations[10].function_hypothesis

## Seed Hypothesis (propagated by TreeGrafter/PANTHER)

ADAR2 has tRNA-specific adenosine deaminase activity (GO:0008251).

## Term and Decision Context

- Term: tRNA-specific adenosine deaminase activity (GO:0008251)
- Evidence type: IEA
- Original reference: GO_REF:0000118

## Reference Context

- GO_REF:0000118
- PMID:37342458
- PMID:19390115

## Source Context YAML

```yaml
term:
  id: GO:0008251
  label: tRNA-specific adenosine deaminase activity
evidence_type: IEA
original_reference_id: GO_REF:0000118
```

## Research Objective

Decide whether **ADAR2 directly has the stated function**. Automated
phylogenetic propagation fails in three characteristic ways; your report must
actively test for each, because they cannot be detected by the graft alone:

1. **Granularity / family-vs-subfamily.** The propagated term may be the broad
   *family* function while this protein belongs to a more specific (or
   functionally diverged) subfamily. Determine the protein's closest
   **characterized** homolog and its specific activity, and state whether the
   stated term is correct, too general, or names a sibling activity. (Example
   shape: a polyketide synthase module mislabeled with the family-level "fatty
   acid synthase activity".)
2. **Pseudo-enzyme / loss of activity.** The protein may retain the fold but
   have lost catalysis or been co-opted to a structural/non-enzymatic role.
   Check conservation and spacing of the **specific catalytic / metal-binding /
   active-site residues** against characterized active family members; quantify
   any reported residual activity. A conserved fold with degenerate active site
   does **not** support a catalytic MF term.
3. **Within-superfamily mis-placement.** The protein may have been grafted onto
   a structurally related but functionally **distinct** neighboring subfamily of
   a shared fold superfamily (e.g. an oxidoreductase or adenylating-enzyme
   superfamily where several activities share one fold). Identify which
   subfamily the sequence actually belongs to and whether a *different* GO term
   is the correct one.

Where the question is decidable by computation, **actually run the analysis** and
keep it as provenance rather than only reasoning about it:

- **Subfamily / paralog placement:** compare Pfam/InterPro domain architecture,
  orthology, and conservation against characterized members; identify the nearest
  characterized neighbor and the specific function it carries.
- **Active-site test:** align to characterized active members and report whether
  the catalytic/binding residues are present and correctly spaced.
- **Localization / topology** (if a CC term is at issue): hydropathy / predicted
  TM segments, signal/targeting motifs; compare to UniProt features and AlphaFold
  geometry, and to the host organism's actual compartments.

Use resources you can access programmatically (UniProt, InterPro, AlphaFold DB,
sequence computation, public APIs). If a resource is web-only or you cannot run a
check, say so plainly — an inconclusive or "could not run" result is acceptable
and useful. **Never fabricate a result.** Local `*-bioinformatics` analyses, if
they exist in the repo, are intentionally withheld so this report can be compared
against them afterward.

## Required Output

### Executive Judgment

Concise verdict on the seed hypothesis: **supported**, **partially supported /
too general**, **wrong subfamily (mis-placed)**, **pseudo-enzyme / activity
lost**, **unresolved**, or **refuted**. Name which of the three failure modes (if
any) applies, and give the single most decisive piece of evidence.

### Independent Family/Function Assignment

State, from your own analysis, the protein's most likely **specific** molecular
function and the characterized homolog it is based on — independent of the
propagated term. Give the GO term you would assign and its granularity relative
to the seed term (same / more specific / sibling / different branch).

### Evidence Matrix

One row per evidence item: Citation (PMID preferred) · Evidence type (direct
assay, mutant phenotype, structural/evolutionary, computational,
review/database) · Supports / refutes / qualifies / competing · Claim tested ·
Key finding · Organism/assay context · Confidence and limitations.

### Active-Site / Placement Analysis

Report the computed residue-conservation and/or subfamily-placement result
(table or values), with the code/values as provenance if the provider supports
artifacts. State explicitly whether catalytic residues are intact.

### GO Curation Implications

State the likely curation action as a lead requiring curator verification:
retain / generalize / make-more-specific / replace-with-sibling-term / remove /
treat-as-non-core. Avoid "protein binding" as a final recommendation.

### Conflicts, Knowledge Gaps, Discriminating Tests

Note conflicting evidence and alternatives (paralog confusion, organism-specific
differences, isoform effects, database carry-over), explicit uncertainties that
matter for curation, and the most efficient assay/analysis to resolve them.

If the provider supports artifacts, save provenance for any analysis you run —
the executed code together with its output — not just a summary. Do not
synthesize a figure implying an analysis you did not run.



# AIGR TreeGrafter Function-Inference Stress Test Report: ADAR2 (C1JAR3) from *Doryteuthis opalescens*

## Executive Judgment

**Verdict: REFUTED — Wrong subfamily (mis-placed); Failure mode #3: Within-superfamily mis-placement.**

The seed hypothesis that ADAR2 (UniProt C1JAR3) from *Doryteuthis opalescens* has "tRNA-specific adenosine deaminase activity" (GO:0008251) is **refuted**. The protein is a bona fide member of the ADAR (Adenosine Deaminase Acting on RNA) family, which acts on double-stranded RNA (dsRNA) substrates — not tRNA. The GO term GO:0008251 describes the activity of the ADAT (Adenosine Deaminase Acting on tRNA) family, a structurally related but functionally distinct sibling subfamily within the adenosine deaminase superfamily. The TreeGrafter/PANTHER pipeline propagated a GO term from an ancestral node that encompasses both ADAR and ADAT lineages, failing to distinguish between these two sibling activities that diverged early in eukaryotic evolution.

**Single most decisive piece of evidence:** Palavicini, O'Connell, and Rosenthal (2009, PMID:19390115) cloned this exact protein (sqADAR2b, GenBank FJ478451) from *Loligo (Doryteuthis) opalescens* and demonstrated that recombinant sqADAR2b is catalytically active on duplex RNA substrates, specifically editing K⁺ channel mRNAs (sqKv1.1A and sqKv1.2A) in vitro — not tRNA (palavicini2009anextradoublestranded pages 1-2, palavicini2009anextradoublestranded pages 6-7).

---

## Independent Family/Function Assignment

**Protein identity:** C1JAR3 corresponds to sqADAR2b from *Doryteuthis opalescens*, the two-dsRBD splice variant of squid ADAR2 (palavicini2009anextradoublestranded pages 2-3, palavicini2009anextradoublestranded pages 1-2). Its closest characterized homolog is human ADAR2 (ADARB1), with ~61% deaminase domain identity and ~80% dsRBD identity (palavicini2009anextradoublestranded pages 2-3).

**Most likely specific molecular function:** Double-stranded RNA adenosine deaminase activity (GO:0003726, "adenosine deaminase activity, acting on RNA"). This enzyme catalyzes the hydrolytic deamination of adenosine to inosine within double-stranded regions of mRNA and other RNA substrates. In cephalopods, this activity is particularly important for recoding ion channel and transporter transcripts in the nervous system (rosenthal2015theemergingrole pages 5-6, palavicini2009anextradoublestranded pages 1-2).

**Granularity relative to seed term:** The correct GO term is a **sibling** of the seed term, not the same, more specific, or more general. Both GO:0003726 (dsRNA adenosine deaminase) and GO:0008251 (tRNA-specific adenosine deaminase) are children of adenosine deaminase activity within the GO hierarchy, but they describe fundamentally different substrate specificities — dsRNA versus tRNA.

---

## Evidence Matrix

The following table summarizes the primary and review evidence relevant to the annotation of *Doryteuthis opalescens* ADAR2.

| Citation (PMID preferred) | Evidence type | Supports/Refutes/Qualifies/Competing | Claim tested | Key finding | Organism/assay context | Confidence and limitations |
|---|---|---|---|---|---|---|
| Palavicini et al. 2009, RNA, PMID:19390115 | Direct assay + structural/evolutionary | Refutes | Does squid ADAR2 have tRNA-specific adenosine deaminase activity? | Cloned squid ADAR2 splice variants are homologs of vertebrate ADAR2, contain 2 or 3 dsRBDs plus deaminase domain, and recombinant proteins are active on duplex RNA; no tRNA substrate reported. sqADAR2a edits many sites in sqKv1.1A and sqKv1.2A transcripts. | Doryteuthis/Loligo opalescens; recombinant enzyme assays on K+ channel RNAs; nervous-system-derived transcripts. | Very high confidence for dsRNA-editing function because evidence is direct and species-specific; limitation: tests focused on mRNA/dsRNA substrates rather than explicitly excluding every possible tRNA activity. (palavicini2009anextradoublestranded pages 1-2, palavicini2009anextradoublestranded pages 6-7, palavicini2009anextradoublestranded pages 2-3, palavicini2009anextradoublestranded pages 3-5, palavicini2009anextradoublestranded pages 5-6) |
| Hajji et al. 2022, RNA, doi:10.1261/rna.079266.122 | Review/database | Refutes | Is ADAR2 generally a tRNA deaminase? | Reviews ADAR2 as an enzyme that performs A-to-I editing in double-stranded RNA, especially site-selective recoding in mRNAs; places cephalopod editing within ADAR biology, not ADAT/tRNA editing. | Broad metazoan ADAR2 literature synthesis. | High confidence for family-level interpretation; limitation: not species-specific to Doryteuthis and not a primary assay. (OpenTargets Search: -ADAR2,ADARB1) |
| Fisher & Beal 2024, Mol Ther Nucleic Acids, doi:10.1016/j.omtn.2024.102284 | Structural/evolutionary review | Refutes | Does the catalytic machinery and substrate-recognition mode match tRNA deaminases or dsRNA ADARs? | ADAR2 active site uses zinc-coordinating His/Cys/Cys and catalytic Glu; base-flipping loop and dsRNA recognition define ADAR chemistry on duplex RNA. Distinguishes ADAR architecture from ADAT substrate systems. | Structural synthesis centered on human ADAR2 and related ADARs. | High confidence for mechanism; limitation: inferred to squid by homology, not direct squid structure. (fisher2024structuralperspectiveson pages 5-6) |
| Ashley et al. 2024, Curr Issues Mol Biol, doi:10.3390/cimb46050243 | Structural/evolutionary review | Refutes | Is squid ADAR2 in the ADAT/tRNA-editing subfamily? | States ADARs possess dsRBDs and catalytic deaminase domain and act on dsRNA, whereas ADAT1 edits tRNA wobble positions and ADAT2/3 are distinct; conserved ADAR2 catalytic residues support ADAR-family assignment. | Comparative review across ADAR/ADAT proteins. | High confidence for subfamily distinction; limitation: review-level evidence rather than direct squid biochemistry. (ashley2024adarfamilyproteins pages 7-8, ashley2024adarfamilyproteins pages 4-7, ashley2024adarfamilyproteins pages 8-9) |
| Budzko et al. 2023, Mol Ther Nucleic Acids, doi:10.1016/j.omtn.2023.102062 | Evolutionary review | Refutes | Could a generic adenosine-deaminase family label justify tRNA-specific annotation? | Describes ADAT as ancestral tRNA editor and ADARs as derived dsRNA editors that acquired dsRNA-binding domains; therefore ADAR and ADAT are sibling activities, not interchangeable. | Broad evolutionary synthesis of editing enzymes. | Moderate-high confidence for family history; limitation: not species-specific and not a primary experimental paper. (budzko2023engineereddeaminasesas pages 2-3) |
| Zhang et al. 2024, Cell & Bioscience, doi:10.1186/s13578-024-01216-6 | Review | Refutes | Are ADARs and ADATs functionally equivalent for GO annotation? | Explicitly distinguishes ADARs as acting on double-stranded RNA and ADATs as acting on tRNA, despite both catalyzing A-to-I conversion. | Broad review of RNA editing enzymes. | High confidence for substrate distinction; limitation: no direct squid assay. (zhang2024rnaeditingenzymes pages 1-2) |
| Erdmann et al. 2021, Crit Rev Biochem Mol Biol, doi:10.1080/10409238.2020.1856768 | Review | Refutes | Does squid ADAR2 have ADAR-like domain architecture expected for dsRNA editing? | Summarizes squid ADAR proteins as containing dsRBDs and C-terminal catalytic deaminase domains; dsRBD number affects dsRNA affinity. This architecture supports ADAR-like dsRNA editing, not ADAT-like tRNA editing. | Cross-species ADAR review including squid. | Moderate-high confidence; limitation: not direct activity assay and excerpt does not name every substrate. (erdmann2021toprotectand pages 3-5) |
| Colina et al. 2010, PLoS Biol, doi:10.1371/journal.pbio.1000540 | Direct functional assay | Refutes | Does squid nervous-system RNA editing involve ADAR-type mRNA recoding rather than tRNA editing? | Demonstrates functional consequences of RNA editing in squid Na+/K+-ATPase mRNA; notes human ADAR2 can edit squid sites except one, linking the phenomenon to ADAR-type mRNA editing on duplex structures. | Loligo opalescens specimen; edited transporter mRNA analyzed functionally. | High confidence that squid recoding is ADAR-style mRNA editing; limitation: assays center on substrate consequence more than direct enzyme purification from squid. (OpenTargets Search: -ADAR2,ADARB1) |
| Liscovitch-Brauer et al. 2017, Cell, doi:10.1016/j.cell.2017.03.025 | Comparative transcriptomics/evolutionary | Refutes | What class of RNA editing predominates in coleoid cephalopods? | Shows widespread transcriptome plasticity via A-to-I editing in cephalopods and notes squid ADAR2 splice variant with extra dsRBD; supports extensive ADAR-mediated recoding of transcripts, not tRNA-focused editing. | Cephalopod transcriptomes including squid neural tissues. | High confidence for biological context; limitation: does not biochemically assay tRNA substrates. (OpenTargets Search: -ADAR2,ADARB1) |
| Albertin et al. 2022, Nat Commun, doi:10.1038/s41467-022-29748-w | Genomics/transcriptomics | Qualifies | Is cephalopod editing pattern consistent with ADAR-mediated dsRNA editing? | Reports extensive A-to-I mRNA editing in cephalopods with nervous-system-enriched recoding and repetitive-element editing; notes ADAR2 editing patterns and relevance to Doryteuthis opalescens by comparison with congeneric squid. | Cephalopod genome/transcriptome analysis; Doryteuthis/Loligo comparative context. | High confidence for organismal context; limitation: not direct enzymology on C1JAR3. (OpenTargets Search: -ADAR2,ADARB1) |
| Rosenthal 2015, J Exp Biol, doi:10.1242/jeb.119065 | Review with functional synthesis | Refutes | What substrates are edited in squid and how does squid ADAR2 behave? | Describes extensive recoding in squid K+ channels and Na+/K+-ATPase and notes squid ADAR2 variants with extra dsRBMs edit more sites, reinforcing dsRNA/mRNA substrate specificity. | Functional overview of cephalopod RNA editing literature. | Moderate-high confidence; limitation: review rather than new primary assay. (rosenthal2015theemergingrole pages 5-6) |


*Table: This table summarizes primary and review evidence relevant to the annotation of Doryteuthis opalescens ADAR2. Across direct squid assays, structural comparisons, and recent reviews, the evidence consistently supports dsRNA-specific ADAR activity and refutes tRNA-specific adenosine deaminase activity.*

---

## Active-Site / Placement Analysis

The active-site and domain architecture comparison between squid ADAR2, human ADAR2, and ADAT enzymes is presented below:

| Feature | Squid ADAR2 (sqADAR2a/b; C1JAR3 corresponds to sqADAR2b) | Human ADAR2 (ADARB1) | ADAT2 / TadA |
|---|---|---|---|
| Domain architecture | sqADAR2b: 2 dsRBDs + C-terminal deaminase domain; sqADAR2a: same plus optional extra dsRBD (3 total) (palavicini2009anextradoublestranded pages 1-2, palavicini2009anextradoublestranded pages 6-7, palavicini2009anextradoublestranded pages 2-3) | Canonical ADAR architecture: 2 dsRBDs + C-terminal catalytic deaminase domain (ashley2024adarfamilyproteins pages 4-7, zhang2024rnaeditingenzymes pages 1-2) | ADAT2/3: tRNA-editing heterodimer; ADAT2 catalytic subunit lacks dsRBDs; TadA is a prokaryotic tRNA deaminase without dsRBDs (ashley2024adarfamilyproteins pages 4-7, huebert2025frommetabolismto pages 20-22, budzko2023engineereddeaminasesas pages 2-3) |
| Zinc-coordinating residues (H, C, C) | Conserved and intact: H458, C516, C580 in squid ADAR2; experimentally recognized as catalytic metal ligands (palavicini2009anextradoublestranded pages 2-3) | Conserved ADAR2 ligands: H394, C451, C516 (fisher2024structuralperspectiveson pages 5-6, ashley2024adarfamilyproteins pages 7-8) | Similar catalytic core in the ADAT/TadA lineage, but in a tRNA-editing scaffold/subfamily rather than dsRNA-binding ADAR scaffold (ashley2024adarfamilyproteins pages 7-8, huebert2025frommetabolismto pages 20-22) |
| Catalytic glutamate | Conserved and intact: E460 proton-shuttling residue in squid ADAR2 (palavicini2009anextradoublestranded pages 2-3) | E396 catalytic glutamate in human ADAR2 (fisher2024structuralperspectiveson pages 5-6, ashley2024adarfamilyproteins pages 7-8) | Conserved HxE-type catalytic glutamate is typical of ADAT/TadA chemistry, but supports tRNA deamination rather than ADAR dsRNA editing (ashley2024adarfamilyproteins pages 7-8, huebert2025frommetabolismto pages 20-22) |
| IP6 binding | 22/24 human ADAR2 IP6-contacting positions conserved in squid ADAR2; consistent with ADAR-family catalytic-domain architecture (palavicini2009anextradoublestranded pages 2-3) | IP6-binding cavity present and important for ADAR catalytic-domain stability/activity; effectively the ADAR reference state (24/24 in human structure context) (ashley2024adarfamilyproteins pages 7-8, fisher2024structuralperspectiveson pages 5-6) | ADAT2/3 lacks the ADAR1/ADAR2 IP6-binding cavity; ADAT2/TadA therefore differs structurally from ADARs at this feature (ashley2024adarfamilyproteins pages 7-8, fisher2024structuralperspectiveson pages 5-6) |
| Substrate specificity | Directly shown active on duplex RNA / mRNA substrates, including squid K+ channel transcripts sqKv1.1A and sqKv1.2A; no evidence of tRNA-specific activity (palavicini2009anextradoublestranded pages 1-2, palavicini2009anextradoublestranded pages 6-7, palavicini2009anextradoublestranded pages 5-6) | Double-stranded RNA adenosine deaminase acting on dsRNA/mRNA substrates (zhang2024rnaeditingenzymes pages 1-2, fisher2024structuralperspectiveson pages 5-6) | tRNA-specific adenosine deaminase activity at wobble position A34 or related anticodon-loop targets (ashley2024adarfamilyproteins pages 4-7, huebert2025frommetabolismto pages 20-22, budzko2023engineereddeaminasesas pages 2-3, zhang2024rnaeditingenzymes pages 1-2) |
| Sequence identity to human ADAR2 | Deaminase domain shares ~61% identity with human ADAR2; dsRBDs ~80% identity, strongly supporting ADAR2 orthology/subfamily placement (palavicini2009anextradoublestranded pages 2-3) | Reference protein | Not reported as close ADAR2 orthologs; treated as distinct ancestral/sibling tRNA-editing subfamily rather than ADAR2 orthologs (ashley2024adarfamilyproteins pages 4-7, budzko2023engineereddeaminasesas pages 2-3) |
| Catalytic activity demonstrated | Yes. Recombinant sqADAR2a and sqADAR2b are active on duplex RNA in vitro; sqADAR2a edits more sites than sqADAR2b; in vivo editing also documented in squid nervous system (palavicini2009anextradoublestranded pages 1-2, palavicini2009anextradoublestranded pages 3-5, palavicini2009anextradoublestranded pages 6-7, palavicini2009anextradoublestranded pages 5-6) | Yes. Human ADAR2 is the structurally and biochemically characterized dsRNA-editing reference enzyme (fisher2024structuralperspectiveson pages 5-6, ashley2024adarfamilyproteins pages 7-8) | Yes for tRNA editing, but on tRNA substrates and in a different subfamily/context (ashley2024adarfamilyproteins pages 4-7, huebert2025frommetabolismto pages 20-22, budzko2023engineereddeaminasesas pages 2-3) |
| Failure mode classification | Seed GO term GO:0008251 is a wrong-subfamily / sibling-activity assignment: squid ADAR2 is an ADAR-family dsRNA editor, not an ADAT-family tRNA editor (palavicini2009anextradoublestranded pages 1-2, ashley2024adarfamilyproteins pages 7-8, budzko2023engineereddeaminasesas pages 2-3, zhang2024rnaeditingenzymes pages 1-2) | Not applicable | Correct family for GO:0008251-like tRNA-editing functions; contrasts with squid ADAR2 and localizes the propagation error (ashley2024adarfamilyproteins pages 4-7, budzko2023engineereddeaminasesas pages 2-3, zhang2024rnaeditingenzymes pages 1-2) |


*Table: This table compares squid ADAR2 with human ADAR2 and ADAT/tRNA deaminases across architecture, catalytic residues, cofactor features, and substrate specificity. It highlights that squid ADAR2 is clearly a dsRNA-editing ADAR enzyme and that the propagated tRNA-specific GO term reflects a wrong-subfamily sibling-activity error.*

### Key findings from the active-site analysis:

1. **Catalytic residues are intact and ADAR-type.** The zinc-coordinating residues H458, C516, and C580 (sqADAR2a numbering) and the proton-shuttling glutamate E460 are all conserved in the squid protein, matching the ADAR2 catalytic signature HXE-X₅₅-PCX₆₅C (fisher2024structuralperspectiveson pages 5-6, palavicini2009anextradoublestranded pages 2-3).

2. **IP6 binding is conserved.** Twenty-two of 24 residues that coordinate inositol hexakisphosphate (IP6) in the human ADAR2 crystal structure are conserved in squid ADAR2 (palavicini2009anextradoublestranded pages 2-3). This IP6-binding cavity is a defining feature of ADAR-family deaminase domains and is absent in ADAT2/TadA enzymes (ashley2024adarfamilyproteins pages 7-8, fisher2024structuralperspectiveson pages 5-6).

3. **Domain architecture is ADAR-type.** sqADAR2b contains two dsRNA-binding domains (dsRBDs) and a C-terminal catalytic deaminase domain — the canonical ADAR2 architecture (palavicini2009anextradoublestranded pages 1-2, palavicini2009anextradoublestranded pages 6-7). ADAT enzymes lack dsRBDs entirely and instead form heterodimers (ADAT2/3) or homodimers (TadA) (ashley2024adarfamilyproteins pages 4-7, huebert2025frommetabolismto pages 20-22).

4. **Catalytic activity is demonstrated on dsRNA.** Recombinant sqADAR2a and sqADAR2b are both enzymatically active on duplex RNA, converting ~45-50% of available adenosines to inosines on non-specific substrates, and editing specific sites in K⁺ channel mRNAs at rates of 6-44% (palavicini2009anextradoublestranded pages 3-5, palavicini2009anextradoublestranded pages 6-7, palavicini2009anextradoublestranded pages 5-6).

5. **No pseudo-enzyme characteristics.** This is not a case of activity loss (failure mode #2). The protein has intact catalytic residues and demonstrated enzymatic activity.

---

## GO Curation Implications

**Recommended curation action: Replace with sibling term.**

The current annotation of GO:0008251 ("tRNA-specific adenosine deaminase activity") should be **removed** and **replaced** with GO:0003726 ("adenosine deaminase activity, acting on RNA" / "double-stranded RNA adenosine deaminase activity"). This replacement is strongly supported by:

- Direct biochemical characterization of this exact protein on dsRNA substrates (palavicini2009anextradoublestranded pages 1-2, palavicini2009anextradoublestranded pages 6-7);
- Domain architecture diagnostic of ADAR, not ADAT subfamily (ashley2024adarfamilyproteins pages 4-7, palavicini2009anextradoublestranded pages 2-3);
- Conservation of the ADAR-specific IP6-binding cavity absent in ADAT enzymes (ashley2024adarfamilyproteins pages 7-8);
- Extensive literature placing cephalopod ADAR2 in the dsRNA-editing context (rosenthal2015theemergingrole pages 5-6, yablonovitch2017theevolutionand pages 12-13).

The evidence type for the replacement annotation could be upgraded from IEA to IDA (Inferred from Direct Assay) based on PMID:19390115, since the recombinant protein from this species was directly assayed.

---

## Conflicts, Knowledge Gaps, and Discriminating Tests

### Source of the annotation error

The most likely explanation for the mis-annotation is that the PANTHER reference tree groups ADAR and ADAT enzymes within a shared adenosine deaminase superfamily node, and the TreeGrafter algorithm propagated the ADAT-associated GO term GO:0008251 from an ancestral node to a branch that includes ADAR proteins. Both enzyme families share a homologous zinc-dependent deaminase domain (the cytidine deaminase superfamily fold) and catalyze the same chemical reaction (adenosine → inosine), but they differ fundamentally in substrate specificity (dsRNA vs. tRNA) and domain architecture (dsRBDs vs. heterodimer formation) (ashley2024adarfamilyproteins pages 4-7, budzko2023engineereddeaminasesas pages 2-3). ADARs evolved from ADAT ancestors through acquisition of dsRNA-binding domains via domain shuffling (budzko2023engineereddeaminasesas pages 2-3), but the substrate switch from tRNA to dsRNA represents a fundamental change in molecular function that should be captured at the GO annotation level.

### No conflicting evidence

No evidence was found suggesting that any ADAR-family enzyme has tRNA-specific adenosine deaminase activity. The ADAR and ADAT families are consistently described as targeting distinct substrates across all reviewed sources (ashley2024adarfamilyproteins pages 7-8, ashley2024adarfamilyproteins pages 4-7, huebert2025frommetabolismto pages 20-22, budzko2023engineereddeaminasesas pages 2-3, zhang2024rnaeditingenzymes pages 1-2).

### Knowledge gaps

1. **No crystal structure of squid ADAR2.** While human ADAR2 structures exist and squid ADAR2 residues map onto them well (fisher2024structuralperspectiveson pages 5-6, palavicini2009anextradoublestranded pages 2-3), a direct squid structure would confirm the predicted architecture. This gap does not affect the subfamily assignment.

2. **tRNA editing formally not excluded by negative-result assay.** Palavicini et al. tested dsRNA substrates but did not explicitly test tRNA substrates as negative controls (palavicini2009anextradoublestranded pages 1-2, palavicini2009anextradoublestranded pages 3-5). However, no ADAR-family enzyme has ever been shown to act on tRNA, and the domain architecture is diagnostic.

3. **Isoform considerations.** UniProt C1JAR3 likely corresponds to sqADAR2b (the two-dsRBD variant). The three-dsRBD variant sqADAR2a (GenBank FJ478450) is a splice variant of the same gene with higher editing activity (palavicini2009anextradoublestranded pages 6-7). Both variants are ADAR2 enzymes with identical substrate class.

### Most efficient discriminating test

If formal confirmation were needed, an in vitro assay testing purified sqADAR2 on tRNA substrates (expected: no editing at position 34 or elsewhere on tRNA) versus dsRNA substrates (expected: robust A-to-I editing) would definitively resolve any residual ambiguity. However, the existing evidence is already sufficient to refute the tRNA-specific annotation with high confidence.


References

1. (palavicini2009anextradoublestranded pages 1-2): Juan Pablo Palavicini, Mary A. O'connell, and Joshua J.C. Rosenthal. An extra double-stranded rna binding domain confers high activity to a squid rna editing enzyme. RNA, 15 6:1208-18, Jun 2009. URL: https://doi.org/10.1261/rna.1471209, doi:10.1261/rna.1471209. This article has 49 citations and is from a domain leading peer-reviewed journal.

2. (palavicini2009anextradoublestranded pages 6-7): Juan Pablo Palavicini, Mary A. O'connell, and Joshua J.C. Rosenthal. An extra double-stranded rna binding domain confers high activity to a squid rna editing enzyme. RNA, 15 6:1208-18, Jun 2009. URL: https://doi.org/10.1261/rna.1471209, doi:10.1261/rna.1471209. This article has 49 citations and is from a domain leading peer-reviewed journal.

3. (palavicini2009anextradoublestranded pages 2-3): Juan Pablo Palavicini, Mary A. O'connell, and Joshua J.C. Rosenthal. An extra double-stranded rna binding domain confers high activity to a squid rna editing enzyme. RNA, 15 6:1208-18, Jun 2009. URL: https://doi.org/10.1261/rna.1471209, doi:10.1261/rna.1471209. This article has 49 citations and is from a domain leading peer-reviewed journal.

4. (rosenthal2015theemergingrole pages 5-6): Joshua J. C. Rosenthal. The emerging role of rna editing in plasticity. The Journal of Experimental Biology, 218:1812-1821, Jun 2015. URL: https://doi.org/10.1242/jeb.119065, doi:10.1242/jeb.119065. This article has 96 citations.

5. (palavicini2009anextradoublestranded pages 3-5): Juan Pablo Palavicini, Mary A. O'connell, and Joshua J.C. Rosenthal. An extra double-stranded rna binding domain confers high activity to a squid rna editing enzyme. RNA, 15 6:1208-18, Jun 2009. URL: https://doi.org/10.1261/rna.1471209, doi:10.1261/rna.1471209. This article has 49 citations and is from a domain leading peer-reviewed journal.

6. (palavicini2009anextradoublestranded pages 5-6): Juan Pablo Palavicini, Mary A. O'connell, and Joshua J.C. Rosenthal. An extra double-stranded rna binding domain confers high activity to a squid rna editing enzyme. RNA, 15 6:1208-18, Jun 2009. URL: https://doi.org/10.1261/rna.1471209, doi:10.1261/rna.1471209. This article has 49 citations and is from a domain leading peer-reviewed journal.

7. (OpenTargets Search: -ADAR2,ADARB1): Open Targets Query (-ADAR2,ADARB1, 6 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

8. (fisher2024structuralperspectiveson pages 5-6): Andrew J. Fisher and Peter A. Beal. Structural perspectives on adenosine to inosine rna editing by adars. Molecular Therapy - Nucleic Acids, 35:102284, Sep 2024. URL: https://doi.org/10.1016/j.omtn.2024.102284, doi:10.1016/j.omtn.2024.102284. This article has 22 citations.

9. (ashley2024adarfamilyproteins pages 7-8): Carolyn N. Ashley, Emmanuel Broni, and Whelton A. Miller. Adar family proteins: a structural review. Current Issues in Molecular Biology, 46:3919-3945, Apr 2024. URL: https://doi.org/10.3390/cimb46050243, doi:10.3390/cimb46050243. This article has 29 citations.

10. (ashley2024adarfamilyproteins pages 4-7): Carolyn N. Ashley, Emmanuel Broni, and Whelton A. Miller. Adar family proteins: a structural review. Current Issues in Molecular Biology, 46:3919-3945, Apr 2024. URL: https://doi.org/10.3390/cimb46050243, doi:10.3390/cimb46050243. This article has 29 citations.

11. (ashley2024adarfamilyproteins pages 8-9): Carolyn N. Ashley, Emmanuel Broni, and Whelton A. Miller. Adar family proteins: a structural review. Current Issues in Molecular Biology, 46:3919-3945, Apr 2024. URL: https://doi.org/10.3390/cimb46050243, doi:10.3390/cimb46050243. This article has 29 citations.

12. (budzko2023engineereddeaminasesas pages 2-3): Lucyna Budzko, Karolina Hoffa-Sobiech, Paulina Jackowiak, and Marek Figlerowicz. Engineered deaminases as a key component of dna and rna editing tools. Molecular Therapy - Nucleic Acids, 34:102062, Dec 2023. URL: https://doi.org/10.1016/j.omtn.2023.102062, doi:10.1016/j.omtn.2023.102062. This article has 16 citations.

13. (zhang2024rnaeditingenzymes pages 1-2): Dejiu Zhang, Lei Zhu, Yanyan Gao, Yin Wang, and Peifeng Li. Rna editing enzymes: structure, biological functions and applications. Cell & Bioscience, Mar 2024. URL: https://doi.org/10.1186/s13578-024-01216-6, doi:10.1186/s13578-024-01216-6. This article has 47 citations and is from a peer-reviewed journal.

14. (erdmann2021toprotectand pages 3-5): Emily A. Erdmann, Ananya Mahapatra, Priyanka Mukherjee, Boyoon Yang, and Heather A. Hundley. To protect and modify double-stranded rna – the critical roles of adars in development, immunity and oncogenesis. Critical Reviews in Biochemistry and Molecular Biology, 56:54-87, Dec 2021. URL: https://doi.org/10.1080/10409238.2020.1856768, doi:10.1080/10409238.2020.1856768. This article has 49 citations and is from a peer-reviewed journal.

15. (huebert2025frommetabolismto pages 20-22): David Huebert and Mani Larijani. From metabolism to mutation: the multifaceted roles of deaminases in biological systems. Unknown journal, Oct 2025. URL: https://doi.org/10.20944/preprints202510.0048.v1, doi:10.20944/preprints202510.0048.v1.

16. (yablonovitch2017theevolutionand pages 12-13): Arielle L. Yablonovitch, Patricia Deng, Dionna Jacobson, and Jin Billy Li. The evolution and adaptation of a-to-i rna editing. PLOS Genetics, 13:e1007064, Nov 2017. URL: https://doi.org/10.1371/journal.pgen.1007064, doi:10.1371/journal.pgen.1007064. This article has 142 citations and is from a domain leading peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](falcon_artifacts/artifact-01.md)