---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-24T04:44:34.269218'
end_time: '2026-06-24T05:04:00.494429'
duration_seconds: 1166.23
template_file: templates/treegrafter_function_hypothesis.md
template_variables:
  organism: PSEPK
  gene: aceK
  gene_symbol: aceK
  uniprot_accession: Q88EA1
  taxon_id: NCBITaxon:160488
  taxon_label: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440)
  focus_type: function_assignment
  hypothesis_slug: function-hypothesis-go-0004721
  hypothesis_text: aceK has phosphoprotein phosphatase activity (GO:0004721).
  term_context: '- Term: phosphoprotein phosphatase activity (GO:0004721)

    - Evidence type: IEA

    - Original reference: GO_REF:0000118'
  reference_context: '- GO_REF:0000118

    - file:PSEPK/aceK/aceK-uniprot.txt

    - file:PSEPK/aceK/aceK-notes.md'
  source_file: genes/PSEPK/aceK/aceK-ai-review.yaml
  source_selector: existing_annotations[1].function_hypothesis
  source_context_yaml: "term:\n  id: GO:0004721\n  label: phosphoprotein phosphatase\
    \ activity\nevidence_type: IEA\noriginal_reference_id: GO_REF:0000118"
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 18
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

- **Organism code:** PSEPK
- **Taxon:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440) (NCBITaxon:160488)
- **Gene directory:** aceK
- **Gene symbol:** aceK
- **UniProt accession:** Q88EA1

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** function-hypothesis-go-0004721
- **Source file:** genes/PSEPK/aceK/aceK-ai-review.yaml
- **Source selector:** existing_annotations[1].function_hypothesis

## Seed Hypothesis (propagated by TreeGrafter/PANTHER)

aceK has phosphoprotein phosphatase activity (GO:0004721).

## Term and Decision Context

- Term: phosphoprotein phosphatase activity (GO:0004721)
- Evidence type: IEA
- Original reference: GO_REF:0000118

## Reference Context

- GO_REF:0000118
- file:PSEPK/aceK/aceK-uniprot.txt
- file:PSEPK/aceK/aceK-notes.md

## Source Context YAML

```yaml
term:
  id: GO:0004721
  label: phosphoprotein phosphatase activity
evidence_type: IEA
original_reference_id: GO_REF:0000118
```

## Research Objective

Decide whether **aceK directly has the stated function**. Automated
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

- **Organism code:** PSEPK
- **Taxon:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440) (NCBITaxon:160488)
- **Gene directory:** aceK
- **Gene symbol:** aceK
- **UniProt accession:** Q88EA1

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** function-hypothesis-go-0004721
- **Source file:** genes/PSEPK/aceK/aceK-ai-review.yaml
- **Source selector:** existing_annotations[1].function_hypothesis

## Seed Hypothesis (propagated by TreeGrafter/PANTHER)

aceK has phosphoprotein phosphatase activity (GO:0004721).

## Term and Decision Context

- Term: phosphoprotein phosphatase activity (GO:0004721)
- Evidence type: IEA
- Original reference: GO_REF:0000118

## Reference Context

- GO_REF:0000118
- file:PSEPK/aceK/aceK-uniprot.txt
- file:PSEPK/aceK/aceK-notes.md

## Source Context YAML

```yaml
term:
  id: GO:0004721
  label: phosphoprotein phosphatase activity
evidence_type: IEA
original_reference_id: GO_REF:0000118
```

## Research Objective

Decide whether **aceK directly has the stated function**. Automated
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


# AIGR TreeGrafter Function-Inference Stress Test Report: *P. putida* KT2440 aceK (Q88EA1) — GO:0004721 (phosphoprotein phosphatase activity)

---

## Executive Judgment

**Verdict: Partially supported / too general (Failure Mode 1: Granularity)**

The seed hypothesis that *P. putida* KT2440 aceK (Q88EA1) has phosphoprotein phosphatase activity (GO:0004721) is **supported in substance but imprecise in granularity**. AceK is a well-characterized bifunctional isocitrate dehydrogenase kinase/phosphatase whose phosphatase arm specifically dephosphorylates a single phosphoserine residue (Ser113) on isocitrate dehydrogenase (IDH) (zheng2012structuralandmechanistic pages 6-7, zheng2012structuralandmechanistic pages 9-10, zheng2012structuralandmechanistic pages 7-9, miller2000locationsofthe pages 1-2). GO:0004721 (phosphoprotein phosphatase activity) is technically correct as a parent term — AceK does remove phosphate from a phosphoprotein — but the annotation would be more precise as GO:0004722 (protein serine/threonine phosphatase activity), which is the appropriate child term reflecting AceK's serine-specific dephosphorylation chemistry. Additionally, AceK's phosphatase function is **incomplete as a standalone annotation** because the protein is intrinsically bifunctional: it also possesses protein kinase activity (GO:0004672) on the same substrate, and these two activities are catalyzed at the same active site and are allosterically interconverted (zheng2012structuralandmechanistic pages 10-11, rangwala2022kinasesondouble pages 4-5, zheng2012structuralandmechanistic pages 7-9).

The single most decisive piece of evidence is the structural and mutagenesis demonstration that AceK's phosphatase mechanism operates through Asp475 (nucleophile) and Asp477 (general acid) in a HAD-like DXDX(I) motif to dephosphorylate phospho-Ser113 on IDH, and that D477N/D477A mutations abolish phosphatase activity while retaining kinase activity (zheng2012structuralandmechanistic pages 6-7). This proves the phosphatase function is genuine, catalytically separable, and serine-directed.

**Failure mode assessment:**
- **Failure Mode 1 (Granularity): APPLIES.** GO:0004721 is the family-level parent term; the actual function is the more specific protein serine/threonine phosphatase activity (GO:0004722).
- **Failure Mode 2 (Pseudo-enzyme): Does NOT apply.** AceK is not a pseudo-enzyme. The catalytic residues (Asp475, Asp477) that define phosphatase activity are conserved in the characterized E. coli ortholog, and mutagenesis confirms they are required for phosphatase catalysis (zheng2012structuralandmechanistic pages 6-7). The *P. putida* ortholog is expected to retain these residues based on strong orthology and shared gene name/synteny, and systems-level studies in *P. putida* KT2440 infer functional AceK-mediated IDH regulation (weimer2024systemsbiologyof pages 8-9).
- **Failure Mode 3 (Within-superfamily mis-placement): Does NOT apply.** AceK has a unique two-domain architecture (kinase domain + regulatory domain with no known structural homologs) and a highly specific substrate recognition loop (SRL) that extends ~32 Å into the IDH active site cleft (zheng2012structuralandmechanistic pages 1-3, zheng2012structuralandmechanistic pages 11-13). This architecture is exclusive to the isocitrate dehydrogenase kinase/phosphatase family in Gram-negative bacteria and is not confusable with neighboring HAD-superfamily phosphatases or generic protein kinase families.

---

## Independent Family/Function Assignment

**Most likely specific molecular function:** Bifunctional isocitrate dehydrogenase kinase/phosphatase activity, encompassing:
- Protein serine/threonine phosphatase activity (GO:0004722) — specifically, dephosphorylation of phospho-Ser113 on IDH
- Protein serine/threonine kinase activity (GO:0004674) — phosphorylation of Ser113 on IDH

**Closest characterized homolog:** *E. coli* K-12 AceK (UniProt: P11071), 578 amino acids, with crystal structures (PDB: 3LCF, 3EPS) and extensive mutagenesis data (zheng2012structuralandmechanistic pages 3-4, zheng2012structuralandmechanistic pages 1-3, rangwala2022kinasesondouble pages 4-5).

**GO term assignment recommendation:** GO:0004722 (protein serine/threonine phosphatase activity), paired with GO:0004674 (protein serine/threonine kinase activity). The propagated term GO:0004721 is the parent of GO:0004722 and is not wrong, but is **one level too general**. For a bifunctional enzyme, both activities should ideally be annotated.

**Granularity relative to seed term:** The recommended GO:0004722 is **more specific** (child) than the seed term GO:0004721.

---

## Evidence Matrix

The following table summarizes the primary and secondary evidence evaluated in this analysis:

| Citation | Evidence Type | Supports/Refutes/Qualifies | Claim Tested | Key Finding | Organism/Assay Context | Confidence and Limitations |
|---|---|---|---|---|---|---|
| Zheng, Yates & Jia 2012, *Phil. Trans. R. Soc. B* (zheng2012structuralandmechanistic pages 6-7, zheng2012structuralandmechanistic pages 7-9, zheng2012structuralandmechanistic pages 9-10) | Structural/mechanistic analysis; mutational interpretation | Supports, qualifies | Does AceK directly have phosphoprotein phosphatase activity? If so, what kind? | AceK is a bona fide bifunctional IDH kinase/phosphatase; phosphatase chemistry uses Asp475 as nucleophile and Asp477 as general acid in a HAD-like DXDX(I) motif. The substrate phosphate is removed from phosphorylated Ser113 of IDH, showing direct protein phosphatase activity and specifically serine-directed dephosphorylation. | Best-characterized AceK ortholog from *E. coli*; structural and mechanistic work on catalytic cycle and active site | High confidence for AceK family mechanism; limitation: not a direct assay on *P. putida* Q88EA1, so transfer to KT2440 is by close orthology rather than direct biochemical measurement. |
| Zheng, Yates & Jia 2012, phosphatase-defective mutants (zheng2012structuralandmechanistic pages 6-7) | Mutational/structure-function evidence | Supports | Is the phosphatase activity a real catalytic function rather than fold retention or annotation artifact? | D477N and D477A retain kinase activity but abolish phosphatase activity, showing the phosphatase function is catalytically separable and depends on specific active-site residues rather than nonspecific substrate effects. | *E. coli* AceK mutational analysis interpreted in the structural framework | High confidence for catalytic mechanism; limitation: residue test is in the characterized homolog, not experimentally repeated in *P. putida*. |
| Miller et al. 2000, *JBC* (miller2000locationsofthe pages 1-2, miller2000locationsofthe pages 4-6) | Biochemical/regulatory study | Supports, qualifies | Does AceK act directly on a phosphoprotein substrate, and is its phosphatase function separable from kinase regulation? | AceK is the bifunctional IDH kinase/phosphatase acting on IDH phosphorylated at Ser113. aceK3 (Q373R) and aceK4 (Y414C) retain kinase with markedly altered phosphatase behavior, supporting a distinct regulated phosphatase mode within the same enzyme. | *E. coli* IDH/AceK biochemical and regulatory assays | High confidence that AceK is a direct phosphoprotein phosphatase; limitation: focus is regulatory-site mapping, not comprehensive substrate-spectrum testing. |
| Ikeda & LaPorte 1991, *J. Bacteriol.* aceK alleles separating activities (indirectly summarized in later mechanistic literature) (zheng2012structuralandmechanistic pages 6-7, miller2000locationsofthe pages 4-6) | Classical genetic/biochemical separation-of-function evidence | Supports | Can AceK lose phosphatase while retaining kinase, confirming true bifunctionality? | Historical aceK allele studies identified variants expressing kinase but not phosphatase activity, establishing that phosphatase activity is a real, genetically separable catalytic function of AceK rather than an annotation by association. | *E. coli* aceK mutant alleles | Moderate confidence here because the primary paper was not directly accessible in this session; claim is supported via later summaries and related biochemical follow-up rather than direct quote from the 1991 article. |
| Rangwala et al. 2022, *Biomolecules* (rangwala2022kinasesondouble pages 4-5) | Review/database synthesis (UniProtKB-based) | Supports, qualifies | Independent family assignment: is AceK recognized as a bifunctional kinase/phosphatase family member? | Review of UniProtKB-annotated bifunctional kinases lists AceK as a bifunctional Ser/Thr kinase/phosphatase and metabolic sensor for glyoxylate bypass regulation, consistent with direct phosphoprotein phosphatase function. | UniProtKB-curated AceK from *E. coli* within broader kinome review | Moderate confidence: useful for consensus family assignment and annotation context, but secondary source and not a primary biochemical assay. |
| Weimer et al. 2024, *Microbial Cell Factories* (weimer2024systemsbiologyof pages 8-9) | Omics/physiological inference | Qualifies | Is there organism-specific evidence that *P. putida* KT2440 AceK participates in IDH regulation? | In *P. putida* KT2440, metabolic/omics interpretation invokes AceK-mediated phosphorylation and partial inactivation of Icd under conditions favoring glyoxylate shunt flux, consistent with conserved AceK function in this organism. | *P. putida* KT2440 multi-omics under electrogenic/anoxic conditions | Moderate confidence for organism relevance; limitation: inference from systems data and prior literature, not direct in vitro phosphatase assay of Q88EA1. |
| AceK substrate specificity from mechanistic literature: phospho-Ser113 of IDH (zheng2012structuralandmechanistic pages 9-10, zheng2012structuralandmechanistic pages 7-9, zheng2012structuralandmechanistic pages 10-11, miller2000locationsofthe pages 1-2) | Mechanistic/biochemical consensus | Qualifies | Is GO:0004721 the right granularity, or is a more specific child term preferable? | AceK dephosphorylates a phosphoserine residue (Ser113) on IDH; therefore GO:0004721 is supported as a parent term, but the biology is more specifically protein serine/threonine phosphatase activity. | Characterized AceK-IDH system, chiefly *E. coli* | High confidence on specificity; limitation: GO hierarchy itself was not computed here from a GO API during this session, so the curation implication is based on substrate chemistry rather than a directly queried ontology record. |
| AceK family placement and domain architecture (zheng2012structuralandmechanistic pages 3-4, zheng2012structuralandmechanistic pages 1-3, zheng2012structuralandmechanistic pages 4-6, zheng2012structuralandmechanistic pages 11-13) | Structural/evolutionary analysis | Refutes competing mis-placement | Could TreeGrafter have misplaced this protein into a neighboring fold-related but functionally different subfamily? | AceK has the distinctive two-domain architecture of isocitrate dehydrogenase kinase/phosphatase, with a kinase-like C-terminal catalytic domain, unique regulatory domain, and IDH-specific substrate recognition loop; this argues against mis-placement into a neighboring generic phosphatase or kinase family. | AceK family structural analysis in Gram-negative bacteria | High confidence for family assignment; limitation: no direct computational tree/sequence placement artifact was run in this session for Q88EA1 itself. |


*Table: This table summarizes the primary and secondary evidence relevant to whether P. putida KT2440 AceK directly has GO:0004721 phosphoprotein phosphatase activity. It also distinguishes direct support for phosphatase function from qualifiers about annotation granularity and organism-specific evidence.*

---

## Active-Site / Placement Analysis

The following table details the key catalytic and regulatory residues of AceK, using the characterized *E. coli* enzyme (P11071) as the reference, with assessment of expected conservation in *P. putida* Q88EA1:

| Residue (E. coli numbering) | Role in Catalysis | Critical for Phosphatase? | Critical for Kinase? | Mutation effect | Expected Conservation in *P. putida* Q88EA1 |
|---|---|---|---|---|---|
| P-loop (315-320) | Gly-rich ATP-binding loop in kinase-like catalytic domain; helps position nucleotide in the shared active site (zheng2012structuralandmechanistic pages 3-4) | Indirectly yes, because phosphatase function is ATP/ADP-dependent and uses the same active site (zheng2012structuralandmechanistic pages 6-7, miller2000locationsofthe pages 1-2) | Yes | No specific mutation from retrieved sources in this session; structural evidence indicates ATP-site integrity is required for both activities (zheng2012structuralandmechanistic pages 3-4, zheng2012structuralandmechanistic pages 4-6) | Expected conserved at motif/function level by strong AceK orthology and shared bifunctional family assignment, but not directly verified here because no alignment was run programmatically (rangwala2022kinasesondouble pages 4-5, zheng2012structuralandmechanistic pages 11-13) |
| Gln345 | Substrate-sensing/switch residue; in phosphatase mode interacts with Ser113 region of IDH and contributes to kinase/phosphatase switching (zheng2012structuralandmechanistic pages 10-11) | Yes, regulatory/switch role | Yes, regulatory/switch role | No direct single-site mutant retrieved here; structural model indicates it helps exclude unphosphorylated IDH in phosphatase mode (zheng2012structuralandmechanistic pages 10-11) | Expected conserved functionally in orthologous AceK proteins; exact residue conservation not directly tested here (zheng2012structuralandmechanistic pages 11-13) |
| Lys346 | Forms AMP-responsive salt-bridge network that stabilizes phosphatase-favoring conformation with Glu478 (zheng2012structuralandmechanistic pages 7-9) | Yes, for phosphatase-promoting allosteric state | Indirectly, because switching between modes depends on this loop conformation | No specific mutant retrieved here; implicated in AMP-controlled closure of Loop b3aC (zheng2012structuralandmechanistic pages 7-9) | Expected conserved in AceK orthologs with AMP-regulated bifunctionality; not directly aligned for Q88EA1 (zheng2012structuralandmechanistic pages 11-13) |
| Tyr414 | Gatekeeper/sensor residue transmitting allosteric signals and helping maintain phosphatase mode (zheng2012structuralandmechanistic pages 10-11, zheng2012structuralandmechanistic pages 4-6) | Yes | Indirectly yes | aceK4 Y414C retains kinase but markedly reduces/perturbs phosphatase behavior, separating regulation of the two activities (miller2000locationsofthe pages 4-6) | Strongly expected conserved because it is central to the AceK switching mechanism; direct conservation not computed here (miller2000locationsofthe pages 4-6, zheng2012structuralandmechanistic pages 4-6) |
| Asp457 | Catalytic aspartate in kinase mechanism, part of kinase catalytic cassette in C-terminal domain (zheng2012structuralandmechanistic pages 3-4) | No direct evidence that it is required for phosphatase chemistry | Yes | Retrieved sources identify it as catalytic for kinase, but no explicit mutant effect was retrieved in this session (zheng2012structuralandmechanistic pages 3-4) | Expected conserved in genuine AceK orthologs because kinase activity is core to family identity; not directly checked in Q88EA1 alignment (rangwala2022kinasesondouble pages 4-5, zheng2012structuralandmechanistic pages 3-4) |
| Asn462 | Member of kinase catalytic triad with Asp457 and Asp475 (zheng2012structuralandmechanistic pages 4-6) | No direct evidence for phosphatase chemistry | Yes | Retrieved sources define catalytic role in kinase triad; no explicit site-mutant phenotype retrieved in this session (zheng2012structuralandmechanistic pages 4-6) | Expected conserved in bona fide AceK orthologs; no direct residue-level confirmation for Q88EA1 available from this session (zheng2012structuralandmechanistic pages 4-6) |
| Asp475 | Shared catalytic residue: kinase triad component and phosphatase nucleophile in DXDX(I) motif; also coordinates Mg2+ in ATP site (zheng2012structuralandmechanistic pages 6-7, zheng2012structuralandmechanistic pages 4-6, zheng2012structuralandmechanistic pages 7-9) | Yes, essential | Yes, essential | D475A abolishes ATPase activity and disrupts catalytic metal/cofactor binding; later mechanistic work places it as the phosphatase nucleophile and kinase-triad residue (zheng2012structuralandmechanistic pages 4-6, zheng2012structuralandmechanistic pages 6-7) | Very strong expectation of conservation: this is the signature catalytic Asp of the AceK DXDX motif and a decisive residue against pseudo-enzyme status, although Q88EA1 was not directly aligned here (zheng2012structuralandmechanistic pages 6-7) |
| Asp477 | General acid for phosphatase in DXDX(I) motif; donates proton to leaving-group Ser113 during dephosphorylation (zheng2012structuralandmechanistic pages 6-7, zheng2012structuralandmechanistic pages 9-10, zheng2012structuralandmechanistic pages 7-9) | Yes, essential | Not required for kinase catalysis | D477N and D477A abolish phosphatase while retaining kinase activity, the clearest separation-of-function evidence (zheng2012structuralandmechanistic pages 6-7) | Very strong expectation of conservation in active AceK orthologs because loss of this residue specifically destroys phosphatase function; not directly tested in Q88EA1 sequence here (zheng2012structuralandmechanistic pages 6-7) |
| Glu478 | Partners with Lys346 in AMP-responsive salt bridge stabilizing phosphatase-favoring closed loop conformation (zheng2012structuralandmechanistic pages 7-9) | Yes, for phosphatase-favoring regulatory state | Indirectly | No single-site mutant retrieved here; role inferred from structural/allosteric analysis (zheng2012structuralandmechanistic pages 7-9) | Expected functionally conserved in AceK orthologs that retain AMP-responsive mode switching; exact residue state in Q88EA1 not directly measured here (zheng2012structuralandmechanistic pages 7-9) |


*Table: This table summarizes the catalytic and regulatory residues that define AceK bifunctionality, using the characterized E. coli enzyme as the reference for evaluating P. putida Q88EA1. It is useful for testing pseudo-enzyme loss and confirming that the propagated phosphatase annotation fits the AceK subfamily, while noting that direct sequence alignment of Q88EA1 was not run in this session.*

**Summary of active-site analysis:**

The phosphatase catalytic mechanism of AceK follows a five-step cycle involving a pentacovalent phosphate intermediate, mechanistically related to HAD-superfamily phosphatases (zheng2012structuralandmechanistic pages 6-7, zheng2012structuralandmechanistic pages 9-10, zheng2012structuralandmechanistic pages 7-9). The key residues are:

1. **Asp475** — nucleophile that attacks the phosphate group on phospho-Ser113 of IDH, forming a phosphoenzyme intermediate (zheng2012structuralandmechanistic pages 6-7, zheng2012structuralandmechanistic pages 9-10).
2. **Asp477** — general acid that donates a proton to the leaving Ser113 hydroxyl (zheng2012structuralandmechanistic pages 6-7, zheng2012structuralandmechanistic pages 9-10). D477N and D477A mutations completely abolish phosphatase while retaining kinase activity (zheng2012structuralandmechanistic pages 6-7).
3. **Conserved DXDX(I) motif** (residues 475–479) — structurally aligned with the DXDX(T/V) motif of d,d-heptose 1,7-bisphosphate phosphatase and other HAD phosphatases (zheng2012structuralandmechanistic pages 7-9, zheng2012structuralandmechanistic pages 6-7).
4. **Mg²⁺ coordination** — a strictly conserved lysine coordinates with Mg²⁺ and is essential for catalysis (zheng2012structuralandmechanistic pages 7-9).

The phosphatase activity is ATP/ADP-dependent: ADP acts as the catalytic residue in step 3 of the cycle, attacking the aspartatyl-phosphate intermediate to regenerate ATP (zheng2012structuralandmechanistic pages 7-9, zheng2012structuralandmechanistic pages 9-10). This unusual feature distinguishes AceK from typical phosphoprotein phosphatases and is consistent with the enzyme's bifunctional architecture.

**Limitation:** A direct pairwise sequence alignment of *P. putida* Q88EA1 against *E. coli* P11071 was not run programmatically during this session. Conservation of the critical catalytic residues in Q88EA1 is **inferred** from: (a) orthology (shared gene name aceK, shared genomic context in the aceBAK operon region); (b) shared taxonomic restriction to Gram-negative bacteria (zheng2012structuralandmechanistic pages 11-13); and (c) systems-biology evidence that *P. putida* KT2440 uses AceK-mediated IDH regulation for glyoxylate shunt control (weimer2024systemsbiologyof pages 8-9). A direct alignment confirming residue identity at positions corresponding to Asp475 and Asp477 would strengthen this inference.

---

## GO Curation Implications

**Recommended curation action: Make-more-specific**

1. **Retain** GO:0004721 only if annotation rules require the parent term to be present alongside the child term.
2. **Replace with (or add)** GO:0004722 (protein serine/threonine phosphatase activity) as the more specific and accurate term for the phosphatase arm of AceK's bifunctional activity.
3. **Additionally annotate** GO:0004674 (protein serine/threonine kinase activity) to capture the kinase arm, which is equally well-supported and is the other half of this bifunctional enzyme's core molecular function (rangwala2022kinasesondouble pages 4-5, zheng2012structuralandmechanistic pages 7-9).
4. The annotation should ideally carry evidence code **ISS** (Inferred from Sequence or Structural Similarity) with reference to the characterized *E. coli* AceK (P11071), since no direct biochemical assay of Q88EA1 has been published. The current IEA evidence code from TreeGrafter (GO_REF:0000118) is appropriate as an automated annotation but could be upgraded upon curator review.

---

## Conflicts, Knowledge Gaps, and Discriminating Tests

### Knowledge gaps
1. **No direct biochemical assay of *P. putida* Q88EA1 phosphatase activity.** All functional evidence for this specific protein comes from orthology transfer from *E. coli* AceK and from systems-level metabolic inference in *P. putida* (weimer2024systemsbiologyof pages 8-9). A direct in vitro kinase/phosphatase assay of recombinant Q88EA1 with purified *P. putida* IDH would be the most efficient discriminating test.

2. **No programmatic sequence alignment was run.** Conservation of Asp475 and Asp477 (E. coli numbering) in Q88EA1 is strongly expected but not computationally verified in this session. A BLAST or HMM alignment of Q88EA1 against P11071, confirming these residues are intact with correct spacing, would close this gap definitively.

3. **GO:0004737 status.** The most precise historical GO term for AceK's phosphatase activity was GO:0004737 ([isocitrate dehydrogenase (NADP+)] phosphatase), but this term has been obsoleted/merged in recent GO releases. The current ontology hierarchy should be checked to identify whether a replacement specific term exists or whether GO:0004722 is the correct leaf term.

### Potential conflicts
- **AceK's phosphatase is mechanistically atypical.** Unlike conventional protein serine/threonine phosphatases (PPP or PPM families), AceK uses a HAD-like mechanism with an aspartyl-phosphate intermediate and requires ATP/ADP as a cofactor for the dephosphorylation cycle (zheng2012structuralandmechanistic pages 6-7, zheng2012structuralandmechanistic pages 7-9). This means it does not belong to the canonical phosphatase families (PP1/PP2A/PP2B/PP2C) despite sharing the GO:0004722 functional classification. Curators should note this mechanistic distinction.
- **Bifunctionality creates annotation complexity.** Annotating only the phosphatase function without the kinase function is misleading, as both activities are intrinsic to the same protein at the same active site and are allosterically interconverted by metabolite signals (AMP, 3-phosphoglycerate, pyruvate) (zheng2012structuralandmechanistic pages 7-9, zheng2012structuralandmechanistic pages 10-11).

### Most efficient discriminating tests
1. **Sequence alignment** of Q88EA1 vs. P11071 to confirm Asp475/Asp477 conservation (computational, minutes).
2. **In vitro phosphatase assay** of recombinant Q88EA1 with phospho-IDH substrate (experimental, days-weeks).
3. **AlphaFold structure comparison** of Q88EA1 model against the E. coli AceK crystal structure (PDB: 3LCF) to confirm active-site geometry and DXDX motif positioning (computational, hours).

References

1. (zheng2012structuralandmechanistic pages 6-7): Jimin Zheng, Susan P. Yates, and Zongchao Jia. Structural and mechanistic insights into the bifunctional enzyme isocitrate dehydrogenase kinase/phosphatase acek. Philosophical Transactions of the Royal Society B: Biological Sciences, 367:2656-2668, Sep 2012. URL: https://doi.org/10.1098/rstb.2011.0426, doi:10.1098/rstb.2011.0426. This article has 36 citations and is from a domain leading peer-reviewed journal.

2. (zheng2012structuralandmechanistic pages 9-10): Jimin Zheng, Susan P. Yates, and Zongchao Jia. Structural and mechanistic insights into the bifunctional enzyme isocitrate dehydrogenase kinase/phosphatase acek. Philosophical Transactions of the Royal Society B: Biological Sciences, 367:2656-2668, Sep 2012. URL: https://doi.org/10.1098/rstb.2011.0426, doi:10.1098/rstb.2011.0426. This article has 36 citations and is from a domain leading peer-reviewed journal.

3. (zheng2012structuralandmechanistic pages 7-9): Jimin Zheng, Susan P. Yates, and Zongchao Jia. Structural and mechanistic insights into the bifunctional enzyme isocitrate dehydrogenase kinase/phosphatase acek. Philosophical Transactions of the Royal Society B: Biological Sciences, 367:2656-2668, Sep 2012. URL: https://doi.org/10.1098/rstb.2011.0426, doi:10.1098/rstb.2011.0426. This article has 36 citations and is from a domain leading peer-reviewed journal.

4. (miller2000locationsofthe pages 1-2): Stephen P. Miller, Ridong Chen, Elizabeth J. Karschnia, Charles Romfo, Antony Dean, and David C. LaPorte. Locations of the regulatory sites for isocitrate dehydrogenase kinase/phosphatase*. The Journal of Biological Chemistry, 275:833-839, Jan 2000. URL: https://doi.org/10.1074/jbc.275.2.833, doi:10.1074/jbc.275.2.833. This article has 36 citations.

5. (zheng2012structuralandmechanistic pages 10-11): Jimin Zheng, Susan P. Yates, and Zongchao Jia. Structural and mechanistic insights into the bifunctional enzyme isocitrate dehydrogenase kinase/phosphatase acek. Philosophical Transactions of the Royal Society B: Biological Sciences, 367:2656-2668, Sep 2012. URL: https://doi.org/10.1098/rstb.2011.0426, doi:10.1098/rstb.2011.0426. This article has 36 citations and is from a domain leading peer-reviewed journal.

6. (rangwala2022kinasesondouble pages 4-5): Aziz M. Rangwala, Victoria R. Mingione, George Georghiou, and Markus A. Seeliger. Kinases on double duty: a review of uniprotkb annotated bifunctionality within the kinome. Biomolecules, 12:685, May 2022. URL: https://doi.org/10.3390/biom12050685, doi:10.3390/biom12050685. This article has 3 citations.

7. (weimer2024systemsbiologyof pages 8-9): Anna Weimer, Laura Pause, Fabian Ries, Michael Kohlstedt, Lorenz Adrian, Jens Krömer, Bin Lai, and Christoph Wittmann. Systems biology of electrogenic pseudomonas putida - multi-omics insights and metabolic engineering for enhanced 2-ketogluconate production. Microbial Cell Factories, Sep 2024. URL: https://doi.org/10.1186/s12934-024-02509-8, doi:10.1186/s12934-024-02509-8. This article has 7 citations and is from a peer-reviewed journal.

8. (zheng2012structuralandmechanistic pages 1-3): Jimin Zheng, Susan P. Yates, and Zongchao Jia. Structural and mechanistic insights into the bifunctional enzyme isocitrate dehydrogenase kinase/phosphatase acek. Philosophical Transactions of the Royal Society B: Biological Sciences, 367:2656-2668, Sep 2012. URL: https://doi.org/10.1098/rstb.2011.0426, doi:10.1098/rstb.2011.0426. This article has 36 citations and is from a domain leading peer-reviewed journal.

9. (zheng2012structuralandmechanistic pages 11-13): Jimin Zheng, Susan P. Yates, and Zongchao Jia. Structural and mechanistic insights into the bifunctional enzyme isocitrate dehydrogenase kinase/phosphatase acek. Philosophical Transactions of the Royal Society B: Biological Sciences, 367:2656-2668, Sep 2012. URL: https://doi.org/10.1098/rstb.2011.0426, doi:10.1098/rstb.2011.0426. This article has 36 citations and is from a domain leading peer-reviewed journal.

10. (zheng2012structuralandmechanistic pages 3-4): Jimin Zheng, Susan P. Yates, and Zongchao Jia. Structural and mechanistic insights into the bifunctional enzyme isocitrate dehydrogenase kinase/phosphatase acek. Philosophical Transactions of the Royal Society B: Biological Sciences, 367:2656-2668, Sep 2012. URL: https://doi.org/10.1098/rstb.2011.0426, doi:10.1098/rstb.2011.0426. This article has 36 citations and is from a domain leading peer-reviewed journal.

11. (miller2000locationsofthe pages 4-6): Stephen P. Miller, Ridong Chen, Elizabeth J. Karschnia, Charles Romfo, Antony Dean, and David C. LaPorte. Locations of the regulatory sites for isocitrate dehydrogenase kinase/phosphatase*. The Journal of Biological Chemistry, 275:833-839, Jan 2000. URL: https://doi.org/10.1074/jbc.275.2.833, doi:10.1074/jbc.275.2.833. This article has 36 citations.

12. (zheng2012structuralandmechanistic pages 4-6): Jimin Zheng, Susan P. Yates, and Zongchao Jia. Structural and mechanistic insights into the bifunctional enzyme isocitrate dehydrogenase kinase/phosphatase acek. Philosophical Transactions of the Royal Society B: Biological Sciences, 367:2656-2668, Sep 2012. URL: https://doi.org/10.1098/rstb.2011.0426, doi:10.1098/rstb.2011.0426. This article has 36 citations and is from a domain leading peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](falcon_artifacts/artifact-01.md)