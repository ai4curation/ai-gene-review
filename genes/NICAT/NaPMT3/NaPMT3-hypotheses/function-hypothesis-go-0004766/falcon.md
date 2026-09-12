---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-24T04:31:49.777216'
end_time: '2026-06-24T04:56:11.194755'
duration_seconds: 1461.42
template_file: templates/treegrafter_function_hypothesis.md
template_variables:
  organism: NICAT
  gene: NaPMT3
  gene_symbol: NaPMT3
  uniprot_accession: A0A314LG79
  taxon_id: NCBITaxon:49451
  taxon_label: Nicotiana attenuata
  focus_type: function_assignment
  hypothesis_slug: function-hypothesis-go-0004766
  hypothesis_text: NaPMT3 has spermidine synthase activity (GO:0004766).
  term_context: '- Term: spermidine synthase activity (GO:0004766)

    - Evidence type: IEA

    - Original reference: GO_REF:0000118'
  reference_context: '- GO_REF:0000118

    - file:NICAT/NaPMT3/NaPMT3-notes.md'
  source_file: genes/NICAT/NaPMT3/NaPMT3-ai-review.yaml
  source_selector: existing_annotations[2].function_hypothesis
  source_context_yaml: "term:\n  id: GO:0004766\n  label: spermidine synthase activity\n\
    evidence_type: IEA\noriginal_reference_id: GO_REF:0000118"
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 23
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

- **Organism code:** NICAT
- **Taxon:** Nicotiana attenuata (NCBITaxon:49451)
- **Gene directory:** NaPMT3
- **Gene symbol:** NaPMT3
- **UniProt accession:** A0A314LG79

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** function-hypothesis-go-0004766
- **Source file:** genes/NICAT/NaPMT3/NaPMT3-ai-review.yaml
- **Source selector:** existing_annotations[2].function_hypothesis

## Seed Hypothesis (propagated by TreeGrafter/PANTHER)

NaPMT3 has spermidine synthase activity (GO:0004766).

## Term and Decision Context

- Term: spermidine synthase activity (GO:0004766)
- Evidence type: IEA
- Original reference: GO_REF:0000118

## Reference Context

- GO_REF:0000118
- file:NICAT/NaPMT3/NaPMT3-notes.md

## Source Context YAML

```yaml
term:
  id: GO:0004766
  label: spermidine synthase activity
evidence_type: IEA
original_reference_id: GO_REF:0000118
```

## Research Objective

Decide whether **NaPMT3 directly has the stated function**. Automated
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

- **Organism code:** NICAT
- **Taxon:** Nicotiana attenuata (NCBITaxon:49451)
- **Gene directory:** NaPMT3
- **Gene symbol:** NaPMT3
- **UniProt accession:** A0A314LG79

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** function-hypothesis-go-0004766
- **Source file:** genes/NICAT/NaPMT3/NaPMT3-ai-review.yaml
- **Source selector:** existing_annotations[2].function_hypothesis

## Seed Hypothesis (propagated by TreeGrafter/PANTHER)

NaPMT3 has spermidine synthase activity (GO:0004766).

## Term and Decision Context

- Term: spermidine synthase activity (GO:0004766)
- Evidence type: IEA
- Original reference: GO_REF:0000118

## Reference Context

- GO_REF:0000118
- file:NICAT/NaPMT3/NaPMT3-notes.md

## Source Context YAML

```yaml
term:
  id: GO:0004766
  label: spermidine synthase activity
evidence_type: IEA
original_reference_id: GO_REF:0000118
```

## Research Objective

Decide whether **NaPMT3 directly has the stated function**. Automated
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


# AIGR TreeGrafter Function-Inference Stress Test Report: NaPMT3 (A0A314LG79) — Spermidine Synthase Activity (GO:0004766)

## Executive Judgment

**Verdict: Wrong subfamily (mis-placed) — REFUTED.**

The seed hypothesis that NaPMT3 has spermidine synthase activity (GO:0004766) is **refuted**. The applicable failure mode is **failure mode 3: within-superfamily mis-placement**. NaPMT3 is a putrescine N-methyltransferase (PMT), not a spermidine synthase (SpdS). Although PMT evolved from SpdS by gene duplication and neofunctionalization and the two enzymes share approximately 70% sequence identity (kozbial2005naturalhistoryof pages 6-7), they catalyze fundamentally different reactions. SpdS transfers an aminopropyl group from decarboxylated S-adenosylmethionine (dcSAM) to putrescine to form spermidine, whereas PMT transfers a methyl group from intact S-adenosylmethionine (SAM) to putrescine to form N-methylputrescine (fuell2010polyaminebiosyntheticdiversity pages 4-6). The single most decisive piece of evidence is that Michael (2017) directly states that in solanaceous plants, SpdS has been duplicated to produce PMT, and SpdS needs only a few amino acid changes to acquire putrescine N-methyltransferase activity (michael2017evolutionofbiosynthetic pages 5-7). This high sequence similarity despite catalytic divergence is precisely the scenario that causes TreeGrafter/PANTHER to propagate the ancestral (SpdS) GO term to a neofunctionalized descendant (PMT).

---

## Independent Family/Function Assignment

**Most likely specific molecular function:** Putrescine N-methyltransferase activity (GO:0030760; EC 2.1.1.53).

**Closest characterized homolog basis:** PMT enzymes from *Nicotiana tabacum* (characterized by Hibi et al. 1994; Riechers & Timko 1999) and related Solanaceae species. These enzymes form a dedicated multigene family in Nicotiana (five PMT genes in *N. tabacum*) and catalyze the first committed step of nicotine biosynthesis (riechers1999structureandexpression pages 2-4, riechers1999structureandexpression pages 4-5, riechers1999structureandexpression pages 5-7).

**Granularity relative to seed term:** The correct term (GO:0030760, putrescine N-methyltransferase activity) is a **sibling** to the propagated term (GO:0004766, spermidine synthase activity) within the aminopropyltransferase fold superfamily. Both proteins share the same ancestral fold but catalyze different reactions with different cofactors and products. This is not a case of correct-but-too-general annotation; it is a mis-assignment to a sibling activity within a shared-fold superfamily.

---

## Evidence Matrix

The following table summarizes all evidence bearing on the seed hypothesis. Each row indicates whether the evidence supports, refutes, or qualifies the claim that NaPMT3 has spermidine synthase activity.

| Citation | Evidence Type | Supports/Refutes/Qualifies | Claim Tested | Key Finding | Organism/Assay Context | Confidence & Limitations |
|---|---|---|---|---|---|---|
| Fuell et al. 2010. *Plant Physiol Biochem* 48:513-520. doi:10.1016/j.plaphy.2010.02.008 (fuell2010polyaminebiosyntheticdiversity pages 4-6) | Evolutionary/comparative review | **Refutes** | Does NaPMT3 directly have spermidine synthase activity? | PMT evolved from spermidine synthase but catalyzes a different reaction: methyl transfer from SAM to putrescine (EC 2.1.1.53), whereas SpdS transfers aminopropyl from dcSAM to putrescine. PMT and SpdS differ in cofactor usage and putrescine-binding site. | Broad plant comparative analysis; PMT discussed for Solanaceae/Convolvulaceae alkaloid biosynthesis. | High confidence for family-level distinction; indirect for NaPMT3 specifically because this is a review/synthesis, not a direct assay of A0A314LG79. |
| Michael 2017. *Biochem J* 474:2277-2299. doi:10.1042/BCJ20160823 (michael2017evolutionofbiosynthetic pages 5-7) | Evolutionary review | **Refutes** | Is the propagated GO term a family-level misassignment rather than the true subfamily function? | In solanaceous plants, SpdS was duplicated to produce PMT; PMT uses SAM as methyl donor, unlike SpdS which uses dcSAM as aminopropyl donor. SpdS needs only a few amino acid changes to acquire PMT activity, explaining phylogenetic confusion. | Polyamine biosynthesis evolution across taxa; discusses solanaceous PMT neofunctionalization. | High confidence for within-superfamily misplacement mechanism; indirect for NaPMT3 catalytic assay. |
| Kozbial & Mushegian 2005. *BMC Struct Biol* 5:19. doi:10.1186/1472-6807-5-19 (kozbial2005naturalhistoryof pages 6-7) | Structural/evolutionary analysis | **Refutes** | Could NaPMT3 still be an SpdS because PMT and SpdS are homologous? | SpdS and PMT share ~70% identity, but SpdS has invariant Asp101 in the glycine-rich loop that restricts the pocket to decarboxylated SAM and excludes SAM; Asp170 is implicated in putrescine deprotonation. This pinpoints the mechanistic basis of divergence despite high similarity. | Comparative structural analysis of SAM-binding protein superfamilies; uses characterized SpdS structures. | High confidence for mechanistic distinction; limitation: does not report a direct NaPMT3 sequence alignment, so inference to NaPMT3 is by homology and gene identity. |
| Kim & Chang 2023. *Molecules* 28:3446. doi:10.3390/molecules28083446 (kim2023structuralanalysisof pages 5-7) | Structural biology/crystal structure | **Qualifies** | What catalytic residues define bona fide spermidine synthase activity? | Crystal structure and comparative analysis identify three conserved catalytic Asp residues in SpdS active site: Asp98, Asp167, Asp170. Roles: aminopropyl capture, putrescine deprotonation, and accurate putrescine binding, respectively. These are hallmarks of aminopropyltransferase activity. | *Kluyveromyces lactis* SpdS crystal structure with comparisons to human, Arabidopsis, Plasmodium, and Trypanosoma SpdS. | High confidence for defining SpdS mechanism; limitation: not a PMT structure and not a direct NaPMT3 assay. Useful as a benchmark for rejecting the GO term. |
| Tong et al. 2025. *Front Plant Sci* published Aug 2025. doi:10.3389/fpls.2025.1647622 (tong2025dnamethylationvalley pages 2-4, tong2025dnamethylationvalley pages 1-2) | Expression/regulatory study | **Refutes** | What function is PMT carrying in *Nicotiana attenuata*? | PMT in *N. attenuata* is described as a pivotal regulatory enzyme in nicotine biosynthesis, catalyzing methylation of putrescine to N-methylputrescine; expression is root-specific and linked to nicotine pathway regulation. | *N. attenuata* roots vs leaves; RNA-seq, qRT-PCR, bisulfite sequencing; nicotine-related gene regulation. | Moderate-high confidence for organism-specific pathway role; limitation: publication year 2025 and not a purified-enzyme assay of NaPMT3 specifically. Still directly relevant to species/context. |
| Riechers & Timko 1999. *Plant Mol Biol* 41:387-401. doi:10.1023/A:1006342018991 (riechers1999structureandexpression pages 2-4, riechers1999structureandexpression pages 4-5, riechers1999structureandexpression pages 5-7) | Gene family/genomic analysis | **Refutes** | Are PMT genes in Nicotiana recognized as a distinct specialized-metabolism gene family? | Tobacco has a five-member PMT gene family; encoded proteins are full-length PMTs and highly similar to one another. This supports existence of a dedicated PMT lineage in Nicotiana rather than misidentified SpdS copies. | *Nicotiana tabacum* genomic library screening, blotting, sequence analysis. | Moderate confidence for paralog/subfamily placement; limitation: species is *N. tabacum*, not *N. attenuata*, and functional inference is family-based. |
| Dalton 2017. Monash University thesis. doi:10.4225/03/58b77d49bebeb (dalton2017theregulationof pages 131-136) | Expression/phenotype-associated regulatory study | **Refutes** | Is PMT behavior in *N. attenuata* consistent with nicotine-defense metabolism rather than core spermidine synthesis? | In *N. attenuata*, PMT expression is modulated by herbivory simulation and circadian regulator TOC1; PMT is treated as the first committed step into nicotine biosynthesis. | *N. attenuata* W+OS herbivory simulation; transcript analysis in control vs TOC1-silenced plants. | Moderate confidence; limitation: thesis source and expression study rather than direct biochemical assay. Nonetheless species-specific and functionally coherent with PMT role. |
| Pegg & Michael 2010. *Cell Mol Life Sci* 67:113-121. doi:10.1007/s00018-009-0165-5 (pegg2010sperminesynthase pages 4-6) | Mechanistic review | **Qualifies** | What residue features are expected for aminopropyltransferase active sites such as SpdS? | Conserved acidic residue Asp104 in human SpdS is part of the nucleoside-binding site and is incompatible with AdoMet binding; aminopropyltransferases instead require decarboxylated AdoMet. This is consistent with the structural basis for distinguishing SpdS from PMT. | Comparative aminopropyltransferase mechanism review, centered on spermine/spermidine synthases. | High confidence for SpdS active-site logic; limitation: not NaPMT3-specific and not a direct comparative PMT mutagenesis study. |


*Table: This table summarizes the principal evidence bearing on whether NaPMT3 from Nicotiana attenuata directly has spermidine synthase activity. The matrix emphasizes that NaPMT3 fits the neofunctionalized PMT subfamily, making the propagated GO:0004766 annotation a within-superfamily misassignment.*

---

## Active-Site / Placement Analysis

The analysis below contrasts the catalytic logic of spermidine synthase and putrescine N-methyltransferase at the active-site level, and explains the structural basis of the TreeGrafter mis-placement.

| Analysis section | Feature / claim | Spermidine synthase (SpdS) | Putrescine N-methyltransferase (PMT) | Relevance to NaPMT3 judgment |
|---|---|---|---|---|
| Feature comparison | Cofactor | Decarboxylated S-adenosylmethionine (dcSAM) (fuell2010polyaminebiosyntheticdiversity pages 4-6, fuell2010polyaminebiosyntheticdiversity pages 3-4, kim2023structuralanalysisof pages 5-7) | Intact S-adenosylmethionine (SAM) (fuell2010polyaminebiosyntheticdiversity pages 4-6) | Different cofactor requirement means PMT is not directly assignable to GO:0004766, which is specific to SpdS aminopropyltransferase chemistry. |
| Feature comparison | Reaction type | Aminopropyl transfer to putrescine (fuell2010polyaminebiosyntheticdiversity pages 4-6, fuell2010polyaminebiosyntheticdiversity pages 3-4, kim2023structuralanalysisof pages 5-7) | Methyl transfer to putrescine (fuell2010polyaminebiosyntheticdiversity pages 4-6) | Seed hypothesis names the wrong chemistry. |
| Feature comparison | EC number | EC 2.5.1.16 (spermidine synthase) (fuell2010polyaminebiosyntheticdiversity pages 4-6, fuell2010polyaminebiosyntheticdiversity pages 3-4) | EC 2.1.1.53 (putrescine N-methyltransferase) (fuell2010polyaminebiosyntheticdiversity pages 4-6) | Distinct EC classes support different GO MF assignments. |
| Feature comparison | GO term | GO:0004766 spermidine synthase activity | GO:0030760 putrescine N-methyltransferase activity | NaPMT3 is best matched to the PMT term, not the propagated SpdS term, based on gene identity and pathway role (tong2025dnamethylationvalley pages 2-4, tong2025dnamethylationvalley pages 1-2). |
| Feature comparison | Shared amine substrate | Putrescine (fuell2010polyaminebiosyntheticdiversity pages 4-6, fuell2010polyaminebiosyntheticdiversity pages 3-4, kim2023structuralanalysisof pages 5-7) | Putrescine (fuell2010polyaminebiosyntheticdiversity pages 4-6) | Shared putrescine usage helps explain why close homologs can be mis-grafted despite different catalytic outcomes. |
| Feature comparison | Product | Spermidine + 5'-methylthioadenosine (MTA) (fuell2010polyaminebiosyntheticdiversity pages 4-6, fuell2010polyaminebiosyntheticdiversity pages 3-4, kim2023structuralanalysisof pages 5-7) | N-methylputrescine + S-adenosylhomocysteine (SAH) (fuell2010polyaminebiosyntheticdiversity pages 4-6) | Product identity directly contradicts the seed GO term. |
| Feature comparison | Key discriminating residue / pocket logic | Invariant Asp101 in glycine-rich loop motif I (PDB 1JQ3) makes cavity too small for full SAM and thereby favors dcSAM; Asp170 implicated in putrescine deprotonation (kozbial2005naturalhistoryof pages 6-7) | PMT active site must accommodate full SAM and therefore diverges from the SpdS dcSAM-selective pocket (fuell2010polyaminebiosyntheticdiversity pages 4-6) | Mechanistic basis for discrimination: PMT is not just a generic SpdS-like protein but a neofunctionalized SAM-dependent methyltransferase within the same fold family. |
| Feature comparison | Catalytic Asp residues defining bona fide SpdS | Kluyveromyces lactis SpdS Asp98, Asp167, Asp170; human equivalent active-site aspartates include Asp104 and corresponding conserved acidic residues required for aminopropyltransferase catalysis (kim2023structuralanalysisof pages 5-7, pegg2010sperminesynthase pages 4-6) | PMT diverged from this SpdS catalytic arrangement to support methyl transfer rather than aminopropyl transfer (fuell2010polyaminebiosyntheticdiversity pages 4-6) | Even without direct NaPMT3 alignment, the defining SpdS catalytic signature is tied to a different reaction class than PMT. |
| Feature comparison | Sequence identity between subfamilies | SpdS and PMT can be ~70% identical despite different functions (kozbial2005naturalhistoryof pages 6-7) | Same | High similarity explains why TreeGrafter/PANTHER can mis-place PMT inside the SpdS neighborhood. |
| Subfamily placement | Gene identity clue | Not expected to be named PMT | NaPMT3 name itself indicates putrescine N-methyltransferase orthology/function | The gene symbol “NaPMT3” is already a strong prior against GO:0004766 and consistent with nicotine-pathway PMT function. |
| Subfamily placement | Evolutionary origin | Ancestral/housekeeping aminopropyltransferase in polyamine biosynthesis (michael2017evolutionofbiosynthetic pages 5-7) | Derived in solanaceous plants by duplication/neofunctionalization from SpdS (fuell2010polyaminebiosyntheticdiversity pages 4-6, michael2017evolutionofbiosynthetic pages 5-7) | NaPMT3 most likely belongs to this derived PMT clade, not to core SpdS. |
| Subfamily placement | Organism/pathway context | Core polyamine biosynthesis | Specialized nicotine/tropane alkaloid biosynthesis; PMT is a pivotal nicotine-pathway enzyme in Nicotiana and root-specific in N. attenuata (tong2025dnamethylationvalley pages 2-4, kim2021structureandfunction pages 24-27, dalton2017theregulationof pages 131-136, tong2025dnamethylationvalley pages 1-2) | Species-context evidence supports PMT assignment for NaPMT3. |
| Subfamily placement | Likely automated annotation failure | If sequence-only propagation ignores neofunctionalization, PMT may inherit ancestral SpdS term | Actual outcome observed here | Best classified as failure mode 3: within-superfamily mis-placement due to high sequence similarity despite catalytic divergence (michael2017evolutionofbiosynthetic pages 5-7, kozbial2005naturalhistoryof pages 6-7). |
| Limitation | Direct NaPMT3 residue-level verification | Could not run direct alignment of A0A314LG79 against characterized SpdS/PMT proteins with programmatic sequence retrieval in this session | Same limitation | Conclusion rests on strong family/subfamily, pathway, and mechanistic evidence; curator verification could add a direct alignment for residue-by-residue provenance. |


*Table: This table contrasts the catalytic logic of spermidine synthase and putrescine N-methyltransferase and summarizes why NaPMT3 belongs to the PMT subfamily. It also localizes the TreeGrafter error as a within-superfamily mis-placement caused by high sequence similarity despite a different reaction chemistry.*

**Key active-site findings:**

Spermidine synthase possesses three highly conserved catalytic aspartate residues (Asp98, Asp167, Asp170 in *Kluyveromyces lactis* SpdS; equivalent residues in human SpdS include Asp104) (kim2023structuralanalysisof pages 5-7). Asp98 captures the aminopropyl moiety of dcSAM, Asp167 deprotonates putrescine, and Asp170 ensures accurate putrescine binding (kim2023structuralanalysisof pages 5-7). Critically, the invariant Asp101 (PDB:1JQ3 numbering) in the glycine-rich loop (motif I) creates a binding cavity too small to accommodate the carboxyl group of intact SAM, thereby enforcing selectivity for decarboxylated SAM (kozbial2005naturalhistoryof pages 6-7). In PMT, this pocket has been remodeled to accommodate full SAM for methyl transfer (fuell2010polyaminebiosyntheticdiversity pages 4-6).

**Limitation:** A direct sequence alignment of NaPMT3 (A0A314LG79) against characterized SpdS and PMT proteins could not be performed programmatically in this session due to lack of real-time access to sequence databases. This residue-level verification is recommended as a curator follow-up. However, the evolutionary, structural, and pathway-context evidence is overwhelming and internally consistent.

---

## GO Curation Implications

**Recommended curation action: Replace with sibling term.**

The current annotation of GO:0004766 (spermidine synthase activity) should be **replaced** with GO:0030760 (putrescine N-methyltransferase activity). This is not a case where the term should be merely generalized or made more specific; the propagated term names the wrong reaction chemistry entirely. The correct EC number is EC 2.1.1.53, not EC 2.5.1.16.

This annotation error represents a well-known pitfall of phylogenetic annotation pipelines when applied to neofunctionalized gene duplicates. PMT evolved from SpdS through gene duplication in solanaceous plants (fuell2010polyaminebiosyntheticdiversity pages 4-6, michael2017evolutionofbiosynthetic pages 5-7), and the ~70% sequence identity between the two enzymes (kozbial2005naturalhistoryof pages 6-7) is sufficient to cause tree-grafting algorithms to place PMT sequences on the SpdS branch. The PANTHER reference tree likely lacks a dedicated PMT subfamily node, causing the family-level SpdS term to be propagated to a functionally divergent descendant.

---

## Conflicts, Knowledge Gaps, and Discriminating Tests

### Conflicts and Alternatives

1. **Paralog confusion within Nicotiana:** *N. attenuata* likely possesses both bona fide spermidine synthase genes and PMT genes. Care must be taken not to confuse the two; however, the gene symbol "NaPMT3" and the organism's well-characterized nicotine biosynthesis pathway strongly place this protein in the PMT subfamily (tong2025dnamethylationvalley pages 2-4, tong2025dnamethylationvalley pages 1-2).

2. **Database carry-over risk:** Because PMT and SpdS share very high sequence identity, automated annotation from any sequence-similarity-based pipeline (not just TreeGrafter) may propagate SpdS terms to PMT orthologs. This is a systemic issue for all Solanaceae PMT genes.

3. **No direct enzymatic assay of NaPMT3 (A0A314LG79) found:** While PMT function in *Nicotiana attenuata* is well-established at the pathway level (dalton2017theregulationof pages 131-136, tong2025dnamethylationvalley pages 2-4), a purified-enzyme kinetic characterization of this specific protein (NaPMT3, UniProt A0A314LG79) was not located. Most direct enzymatic characterizations of PMT have been performed on *N. tabacum* or *Datura stramonium* PMTs.

### Knowledge Gaps

- The exact residue-level alignment of NaPMT3 against characterized SpdS catalytic sites (Asp98/167/170 equivalents) was not computationally verified in this session. This is the most important gap for residue-level provenance.
- Whether NaPMT3 retains any residual aminopropyltransferase activity (i.e., whether it is a "bifunctional" enzyme with trace SpdS activity) has not been experimentally tested, though the evolutionary literature suggests PMT function fully replaces SpdS function in the duplicated copy (michael2017evolutionofbiosynthetic pages 5-7).

### Most Efficient Discriminating Tests

1. **Direct sequence alignment:** Align NaPMT3 (A0A314LG79) against characterized SpdS (e.g., *Arabidopsis thaliana* AtSPDS, PDB:1XJ5) and characterized PMT (e.g., *N. tabacum* NtPMT1a, GenBank:D28506). Check the motif-I glycine-rich loop for the Asp101-equivalent residue. If this residue is altered in NaPMT3 (allowing full SAM binding), this confirms PMT identity.
2. **Recombinant enzyme assay:** Express NaPMT3 in *E. coli* and test for both methyltransferase activity (SAM + putrescine → N-methylputrescine + SAH) and aminopropyltransferase activity (dcSAM + putrescine → spermidine + MTA) to definitively establish catalytic specificity.
3. **PANTHER tree inspection:** Examine the PANTHER family tree to determine whether a PMT subfamily node exists. If absent, this confirms the root cause of the mis-annotation and suggests a PANTHER database improvement.


References

1. (kozbial2005naturalhistoryof pages 6-7): Piotr Z Kozbial and Arcady R Mushegian. Natural history of s-adenosylmethionine-binding proteins. BMC Structural Biology, 5:19-19, Oct 2005. URL: https://doi.org/10.1186/1472-6807-5-19, doi:10.1186/1472-6807-5-19. This article has 407 citations and is from a peer-reviewed journal.

2. (fuell2010polyaminebiosyntheticdiversity pages 4-6): Christine Fuell, Katherine A. Elliott, Colin C. Hanfrey, Marina Franceschetti, and Anthony J. Michael. Polyamine biosynthetic diversity in plants and algae. Plant physiology and biochemistry : PPB, 48 7:513-20, Jul 2010. URL: https://doi.org/10.1016/j.plaphy.2010.02.008, doi:10.1016/j.plaphy.2010.02.008. This article has 237 citations.

3. (michael2017evolutionofbiosynthetic pages 5-7): Anthony J. Michael. Evolution of biosynthetic diversity. The Biochemical journal, 474 14:2277-2299, Jul 2017. URL: https://doi.org/10.1042/bcj20160823, doi:10.1042/bcj20160823. This article has 51 citations.

4. (riechers1999structureandexpression pages 2-4): Dean E. Riechers and Michael P. Timko. Structure and expression of the gene family encoding putrescine n-methyltransferase in nicotiana tabacum: new clues to the evolutionary origin of cultivated tobacco. Plant Molecular Biology, 41:387-401, Oct 1999. URL: https://doi.org/10.1023/a:1006342018991, doi:10.1023/a:1006342018991. This article has 149 citations and is from a peer-reviewed journal.

5. (riechers1999structureandexpression pages 4-5): Dean E. Riechers and Michael P. Timko. Structure and expression of the gene family encoding putrescine n-methyltransferase in nicotiana tabacum: new clues to the evolutionary origin of cultivated tobacco. Plant Molecular Biology, 41:387-401, Oct 1999. URL: https://doi.org/10.1023/a:1006342018991, doi:10.1023/a:1006342018991. This article has 149 citations and is from a peer-reviewed journal.

6. (riechers1999structureandexpression pages 5-7): Dean E. Riechers and Michael P. Timko. Structure and expression of the gene family encoding putrescine n-methyltransferase in nicotiana tabacum: new clues to the evolutionary origin of cultivated tobacco. Plant Molecular Biology, 41:387-401, Oct 1999. URL: https://doi.org/10.1023/a:1006342018991, doi:10.1023/a:1006342018991. This article has 149 citations and is from a peer-reviewed journal.

7. (kim2023structuralanalysisof pages 5-7): Seongjin Kim and Jeong Ho Chang. Structural analysis of spermidine synthase from kluyveromyces lactis. Molecules, 28:3446, Apr 2023. URL: https://doi.org/10.3390/molecules28083446, doi:10.3390/molecules28083446. This article has 6 citations.

8. (tong2025dnamethylationvalley pages 2-4): Ahui Tong, Bingwu Wang, and Jinsong Wu. Dna methylation valley as a distinguishing feature occurs in root-specific expressed nicotine-related genes in nicotiana attenuata. Frontiers in Plant Science, Aug 2025. URL: https://doi.org/10.3389/fpls.2025.1647622, doi:10.3389/fpls.2025.1647622. This article has 2 citations.

9. (tong2025dnamethylationvalley pages 1-2): Ahui Tong, Bingwu Wang, and Jinsong Wu. Dna methylation valley as a distinguishing feature occurs in root-specific expressed nicotine-related genes in nicotiana attenuata. Frontiers in Plant Science, Aug 2025. URL: https://doi.org/10.3389/fpls.2025.1647622, doi:10.3389/fpls.2025.1647622. This article has 2 citations.

10. (dalton2017theregulationof pages 131-136): Heidi L Dalton. The regulation of defence chemistry in nicotiana. ArXiv, Jan 2017. URL: https://doi.org/10.4225/03/58b77d49bebeb, doi:10.4225/03/58b77d49bebeb. This article has 1 citations.

11. (pegg2010sperminesynthase pages 4-6): Anthony E. Pegg and Anthony J. Michael. Spermine synthase. Cellular and Molecular Life Sciences, 67:113-121, Oct 2010. URL: https://doi.org/10.1007/s00018-009-0165-5, doi:10.1007/s00018-009-0165-5. This article has 220 citations and is from a domain leading peer-reviewed journal.

12. (fuell2010polyaminebiosyntheticdiversity pages 3-4): Christine Fuell, Katherine A. Elliott, Colin C. Hanfrey, Marina Franceschetti, and Anthony J. Michael. Polyamine biosynthetic diversity in plants and algae. Plant physiology and biochemistry : PPB, 48 7:513-20, Jul 2010. URL: https://doi.org/10.1016/j.plaphy.2010.02.008, doi:10.1016/j.plaphy.2010.02.008. This article has 237 citations.

13. (kim2021structureandfunction pages 24-27): Neill Kim, Benjamin Chavez, Charles Stewart, and John C. D’Auria. Structure and function of enzymes involved in the biosynthesis of tropane alkaloids. ArXiv, pages 21-50, Jan 2021. URL: https://doi.org/10.1007/978-981-33-4535-5\_2, doi:10.1007/978-981-33-4535-5\_2. This article has 5 citations.

## Artifacts

- [Edison artifact artifact-00](falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](falcon_artifacts/artifact-01.md)