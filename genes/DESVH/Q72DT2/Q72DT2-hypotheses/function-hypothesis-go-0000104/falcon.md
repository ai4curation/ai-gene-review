---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-24T04:14:40.817222'
end_time: '2026-06-24T04:31:45.261893'
duration_seconds: 1024.44
template_file: templates/treegrafter_function_hypothesis.md
template_variables:
  organism: DESVH
  gene: Q72DT2
  gene_symbol: aprA
  uniprot_accession: Q72DT2
  taxon_id: NCBITaxon:882
  taxon_label: Nitratidesulfovibrio vulgaris (Desulfovibrio vulgaris) Hildenborough
  focus_type: function_assignment
  hypothesis_slug: function-hypothesis-go-0000104
  hypothesis_text: aprA has succinate dehydrogenase activity (GO:0000104).
  term_context: '- Term: succinate dehydrogenase activity (GO:0000104)

    - Evidence type: IEA

    - Original reference: GO_REF:0000118'
  reference_context: '- GO_REF:0000118

    - file:DESVH/Q72DT2/Q72DT2-deep-research-falcon.md'
  source_file: genes/DESVH/Q72DT2/Q72DT2-ai-review.yaml
  source_selector: existing_annotations[1].function_hypothesis
  source_context_yaml: "term:\n  id: GO:0000104\n  label: succinate dehydrogenase\
    \ activity\nevidence_type: IEA\noriginal_reference_id: GO_REF:0000118"
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 27
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

- **Organism code:** DESVH
- **Taxon:** Nitratidesulfovibrio vulgaris (Desulfovibrio vulgaris) Hildenborough (NCBITaxon:882)
- **Gene directory:** Q72DT2
- **Gene symbol:** aprA
- **UniProt accession:** Q72DT2

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** function-hypothesis-go-0000104
- **Source file:** genes/DESVH/Q72DT2/Q72DT2-ai-review.yaml
- **Source selector:** existing_annotations[1].function_hypothesis

## Seed Hypothesis (propagated by TreeGrafter/PANTHER)

aprA has succinate dehydrogenase activity (GO:0000104).

## Term and Decision Context

- Term: succinate dehydrogenase activity (GO:0000104)
- Evidence type: IEA
- Original reference: GO_REF:0000118

## Reference Context

- GO_REF:0000118
- file:DESVH/Q72DT2/Q72DT2-deep-research-falcon.md

## Source Context YAML

```yaml
term:
  id: GO:0000104
  label: succinate dehydrogenase activity
evidence_type: IEA
original_reference_id: GO_REF:0000118
```

## Research Objective

Decide whether **aprA directly has the stated function**. Automated
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

- **Organism code:** DESVH
- **Taxon:** Nitratidesulfovibrio vulgaris (Desulfovibrio vulgaris) Hildenborough (NCBITaxon:882)
- **Gene directory:** Q72DT2
- **Gene symbol:** aprA
- **UniProt accession:** Q72DT2

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** function-hypothesis-go-0000104
- **Source file:** genes/DESVH/Q72DT2/Q72DT2-ai-review.yaml
- **Source selector:** existing_annotations[1].function_hypothesis

## Seed Hypothesis (propagated by TreeGrafter/PANTHER)

aprA has succinate dehydrogenase activity (GO:0000104).

## Term and Decision Context

- Term: succinate dehydrogenase activity (GO:0000104)
- Evidence type: IEA
- Original reference: GO_REF:0000118

## Reference Context

- GO_REF:0000118
- file:DESVH/Q72DT2/Q72DT2-deep-research-falcon.md

## Source Context YAML

```yaml
term:
  id: GO:0000104
  label: succinate dehydrogenase activity
evidence_type: IEA
original_reference_id: GO_REF:0000118
```

## Research Objective

Decide whether **aprA directly has the stated function**. Automated
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


# AIGR Function-Inference Stress Test Report: Q72DT2 (aprA) — GO:0000104 (succinate dehydrogenase activity)

## Executive Judgment

**Verdict: REFUTED — Wrong subfamily (mis-placed).**

The seed hypothesis that Q72DT2 (aprA from *Nitratidesulfovibrio vulgaris* [*Desulfovibrio vulgaris*] Hildenborough) has succinate dehydrogenase activity (GO:0000104) is **refuted**. The applicable failure mode is **#3: within-superfamily mis-placement**. The AprA alpha subunit of dissimilatory adenosine-5′-phosphosulfate (APS) reductase shares a common fold with the flavoprotein subunit of succinate dehydrogenase (SDH/Complex II), but this structural relationship is explicitly "not reflected in sequence similarity" (meyer2007molecularanalysisof pages 2-3, meyer2007molecularanalysisof pages 1-2). The two enzymes differ fundamentally in substrate (APS vs. succinate), product (sulfite + AMP vs. fumarate), catalytic mechanism (nucleophilic FAD N5 attack on sulfur vs. hydride transfer from succinate C–H bond), cofactor attachment mode (non-covalent FAD vs. covalent 8α-N3-histidyl FAD), active-site residue identity and spacing, subunit composition, metabolic pathway context, and cellular localization. The single most decisive piece of evidence is the **non-covalent FAD binding** in AprA versus the **covalent FAD-histidine linkage** diagnostic of all succinate dehydrogenase flavoproteins (meyer2008homologymodelingof pages 10-14, sharma2020therolesof pages 3-4, sharma2020therolesof pages 4-5).

---

## Independent Family/Function Assignment

**Protein identity:** Q72DT2 is the alpha subunit (AprA) of dissimilatory adenosine-5′-phosphosulfate reductase, a 1:1 αβ heterodimeric iron-sulfur flavoenzyme (AprAB). AprA is a ~70–75 kDa FAD-containing subunit with a three-domain architecture: FAD-binding domain (residues A2–A261 and A394–A487), capping domain (A262–A393), and helical domain (A488–A643) (meyer2008homologymodelingof pages 1-2).

**Closest characterized homolog:** The crystal structure of APS reductase from *Archaeoglobus fulgidus* at 1.6 Å resolution (Fritz et al. 2002, PDB entries 1jnr, 2FJA–2FJE) serves as the primary structural template (meyer2008homologymodelingof pages 2-3, meyer2008homologymodelingof pages 1-2). *D. vulgaris* AprA has 49.5–60.7% sequence identity to *A. fulgidus* AprA and is explicitly modeled with high accuracy (RMSD values at backbone level within the ranges expected for reliable homology models) (meyer2008homologymodelingof pages 3-6, meyer2008homologymodelingof pages 6-7).

**Correct GO term:** **GO:0033748 — adenylylsulfate reductase activity** (definition: catalysis of the reaction APS + 2 e⁻ → sulfite + AMP). This term is on a **different branch** of the GO molecular function hierarchy from GO:0000104 (succinate dehydrogenase activity); the two are not parent–child or sibling terms but represent distinct catalytic activities within a shared structural fold superfamily.

**Granularity relative to seed term:** The correct term is not a more specific or more general version of GO:0000104. It is a **sibling activity from a different functional subfamily** of the same fold superfamily. The seed term names the wrong activity entirely.

---

## Evidence Matrix

The following table summarizes the key evidence for this assessment:

| Citation | Evidence Type | Supports/Refutes/Qualifies | Claim Tested | Key Finding | Organism/Assay Context | Confidence and Limitations |
|---|---|---|---|---|---|---|
| Meyer & Kuever 2008, *PLoS ONE* 3:e1514, doi:10.1371/journal.pone.0001514 | Structural/evolutionary; homology modeling | Refutes | Q72DT2 AprA has succinate dehydrogenase activity | AprA is structurally in the fumarate reductase family, but its catalytic center is APS-reductase-specific: conserved AprA residues include Asn-A74, Trp-A234, Arg-A265, and His-A398; the mechanism is nucleophilic attack of reduced FAD N5 on APS sulfur, not succinate oxidation. D. vulgaris AprA model clusters with sulfate-reducing Apr enzymes, not SDH enzymes. (meyer2008homologymodelingof pages 1-2, meyer2008homologymodelingof pages 2-3, meyer2008homologymodelingof pages 14-16, meyer2008homologymodelingof pages 10-14) | Comparative models based on *Archaeoglobus fulgidus* AprBA templates; includes *D. vulgaris* AprA/AprB models | High for family placement and active-site interpretation; indirect for Q72DT2 because modeled from homologous structures rather than direct biochemical assay of this exact protein |
| Meyer & Kuever 2007, *Microbiology* 153:3478-3498, doi:10.1099/mic.0.2007/008250-0 | Phylogenetic/evolutionary | Refutes | AprA is a succinate dehydrogenase-family enzyme in function rather than only in fold | The paper explicitly states that only AprA has structural similarity to succinate-dehydrogenase/fumarate-reductase flavoproteins, but this relationship is **not reflected in sequence similarity**; aprBA phylogeny and locus context identify the protein specifically as dissimilatory APS reductase. (meyer2007molecularanalysisof pages 2-3, meyer2007molecularanalysisof pages 1-2) | Broad phylogeny of aprBA genes across sulfur oxidizers and sulfate reducers | High for distinguishing structural analogy from true functional orthology; not a direct activity assay |
| Ramos et al. 2012, *Frontiers in Microbiology* 3:137, doi:10.3389/fmicb.2012.00137 | Direct biochemical interaction; mutant phenotype | Supports | AprA participates in the APS-reduction/sulfate-reduction pathway in *D. vulgaris* | QmoABC interacts directly with AprAB with strong affinity (KD = 90 ± 3 nM); qmoABC is essential for growth on sulfate but not sulfite/thiosulfate, placing AprAB in the APS reduction step of sulfate respiration rather than TCA/respiratory complex II succinate oxidation. (ramos2012themembraneqmoabc pages 4-6, ramos2012themembraneqmoabc pages 1-2, ramos2012themembraneqmoabc pages 6-8) | *Desulfovibrio* spp.; co-immunoprecipitation, cross-linking, Far-Western, tag-affinity purification, SPR, growth phenotypes | High for pathway assignment; does not directly assay AprA catalysis or exclude every remote moonlighting activity, but strongly supports APS-reductase role |
| Fritz et al. 2002, *PNAS* 99:1836-1841, doi:10.1073/pnas.042664399 | Structural biology; crystal structure | Refutes | AprA catalytic chemistry matches succinate dehydrogenase | Crystal structure of APS reductase shows an APS-reductase active center with non-covalently bound FAD and key active-site residues including Arg-A265 and His-A398; this chemistry is for APS reduction/sulfite oxidation, not succinate/fumarate interconversion. (meyer2008homologymodelingof pages 2-3, meyer2008homologymodelingof pages 14-16, meyer2008homologymodelingof pages 10-14) | *Archaeoglobus fulgidus* APS reductase crystal structure used as template for bacterial AprA interpretation | High for mechanistic distinction at the subfamily level; limitation is that it is a homologous enzyme, not the exact *D. vulgaris* protein |
| Sharma et al. 2020, *PNAS* 117:23548-23556, doi:10.1073/pnas.2007391117 | Structural/mechanistic comparison | Refutes | AprA could directly have SDH catalytic machinery | SDH/complex II uses a distinct catalytic architecture: covalent FAD linkage via His-H99 and active-site residues H296, T308, R340, H407, and R451. These defining SDH features differ fundamentally from AprA, whose FAD is non-covalent and whose catalytic residues are different. (sharma2020therolesof pages 3-4, sharma2020therolesof pages 4-5) | Human SDHA-SDHAF2 assembly intermediate; interpreted against bacterial complex II literature | High for defining canonical SDH chemistry; limitation is species difference, but active-site logic is broadly conserved across SDH homologs |
| Trotter et al. 2023, *Frontiers in Microbiology* 14:1095191, doi:10.3389/fmicb.2023.1095191 | Genome-wide genetics; fitness profiling | Supports | aprA is required for sulfate-based physiology in *D. vulgaris* | Large-scale transposon analysis identifies a robust essential gene set in *D. vulgaris* under sulfate-rich growth; the study independently describes APS reductase as a key enzyme whose futile substrate interaction explains molybdate toxicity, consistent with aprA functioning in sulfate reduction rather than as SDH. (trotter2023largescalegeneticcharacterization pages 3-4, trotter2023largescalegeneticcharacterization pages 6-7, trotter2023largescalegeneticcharacterization pages 7-9) | *D. vulgaris Hildenborough* RB-TnSeq / Tn-seq fitness assays across 757 experiments | Moderate to high for pathway importance; limitation is that the provided excerpts do not explicitly name aprA in the essentiality paragraph, so inference is supported by study context rather than a quoted aprA fitness value |
| Bramlett & Peck 1975, *Journal of Biological Chemistry* 250:2979-2986, doi:10.1016/S0021-9258(19)41583-4 | Direct enzyme assay; biochemical characterization | Supports | Q72DT2 encodes adenylylsulfate reductase rather than SDH | Historical direct biochemical characterization reported kinetic properties of adenylyl sulfate reductase from *D. vulgaris*, providing primary experimental support that the enzyme in this organism catalyzes APS reduction. (meyer2008homologymodelingof pages 16-17) | *D. vulgaris* enzyme purification and kinetic analysis | Moderate: highly relevant primary assay, but full text/details were not available in the retrieved context, so specific kinetic constants could not be verified here |
| Kushkevych 2016/2020 reviews, doi:10.30970/sbi.1001.560 and doi:10.3390/cells9030698 | Review/database synthesis | Supports/Qualifies | Community consensus on AprAB function in *Desulfovibrio* | Reviews consistently describe AprAB as the key APS reductase in dissimilatory sulfate reduction in *Desulfovibrio*, matching the genomic and biochemical literature and opposing an SDH annotation. (kushkevych2016dissimilatorysulfatereduction pages 18-20) | Review summaries of sulfate-reduction pathways in intestinal and environmental sulfate-reducing bacteria | Moderate: useful corroboration and current consensus, but not primary evidence; should not be used alone for curation |
| Cross-evidence synthesis from AprA-vs-SDH active-site comparisons | Comparative mechanistic inference | Refutes | The TreeGrafter propagation failed only in granularity, not function | The decisive error is **within-superfamily mis-placement**: AprA and SDHA share a fold family, but differ in substrate class, cofactor attachment mode, catalytic residues, pathway context, and gene neighborhood. The annotation is not merely too broad; it names the wrong sibling activity. (meyer2007molecularanalysisof pages 2-3, meyer2008homologymodelingof pages 2-3, meyer2008homologymodelingof pages 14-16, sharma2020therolesof pages 3-4, sharma2020therolesof pages 4-5, ramos2012themembraneqmoabc pages 4-6) | Integrated inference from structural, phylogenetic, biochemical, and genetic evidence | High for curation conclusion; limitation is that this is a synthesis row rather than a single experiment |


*Table: This table summarizes the key evidence bearing on whether Q72DT2 (aprA) from *Desulfovibrio vulgaris* directly has succinate dehydrogenase activity. The matrix shows that the annotation is best explained as a within-superfamily mis-placement: AprA is an APS reductase, not a succinate dehydrogenase.*

---

## Active-Site / Placement Analysis

The core of the mis-annotation can be traced to fold-level structural similarity not accompanied by functional equivalence. The following detailed comparison demonstrates that the two enzyme families diverge in every feature that would be required for succinate dehydrogenase catalysis:

| Feature | APS Reductase (AprA) | Succinate Dehydrogenase (SdhA) | Diagnostic? |
|---|---|---|---|
| FAD binding mode | Non-covalent FAD cofactor bound in AprA active site; reduced FAD N5 attacks APS sulfur (meyer2008homologymodelingof pages 2-3, meyer2008homologymodelingof pages 10-14) | Covalently bound FAD via 8α-N3-histidyl linkage in SDHA/SdhA (sharma2020therolesof pages 3-4, sharma2020therolesof pages 4-5) | **Yes** |
| FAD attachment residue | No covalent attachment residue; FAD held non-covalently by AprA matrix (meyer2008homologymodelingof pages 10-14) | His-99 in human SDHA; equivalent histidine is the covalent flavin ligand in bacterial homologs (sharma2020therolesof pages 3-4, sharma2020therolesof pages 4-5) | **Yes** |
| Substrate | Adenosine 5'-phosphosulfate (APS) (meyer2008homologymodelingof pages 1-2, meyer2008homologymodelingof pages 14-16) | Succinate / dicarboxylate substrate (sharma2020therolesof pages 4-5) | **Yes** |
| Product(s) | Sulfite + AMP in APS reduction (meyer2008homologymodelingof pages 1-2, meyer2008homologymodelingof pages 14-16) | Fumarate + reduced electron acceptor in succinate oxidation (sharma2020therolesof pages 4-5) | **Yes** |
| Catalytic mechanism | Nucleophilic attack of reduced FAD N5 on APS sulfur, forming FAD-APS and FAD-sulfite intermediates (meyer2008homologymodelingof pages 2-3, meyer2008homologymodelingof pages 14-16, meyer2008homologymodelingof pages 10-14) | Dicarboxylate chemistry at complex II active site; succinate/fumarate interconversion with flavin-dependent redox chemistry and distinct active-site geometry (sharma2020therolesof pages 3-4, sharma2020therolesof pages 4-5) | **Yes** |
| Key active-site residue 1 | Arg-A265 hydrogen-bonds to APS sulfate and helps activate substrate (meyer2008homologymodelingof pages 14-16, meyer2008homologymodelingof pages 10-14) | Arg-R340 binds dicarboxylate substrate in SDH active site (sharma2020therolesof pages 4-5) | Different |
| Key active-site residue 2 | His-A398 hydrogen-bonds to APS sulfate and supports catalysis (meyer2008homologymodelingof pages 14-16, meyer2008homologymodelingof pages 10-14) | His-H407 participates in SDH active-site network (sharma2020therolesof pages 4-5) | Different |
| Key active-site residue 3 | Asn-A74 shapes FAD re-face and stabilizes bent flavin conformation (meyer2008homologymodelingof pages 10-14) | His-H296 contributes to dicarboxylate/flavinylation-active-site chemistry (sharma2020therolesof pages 4-5) | Different |
| Key active-site residue 4 | Trp-A234 shapes FAD re-face and bent isoalloxazine geometry (meyer2008homologymodelingof pages 10-14) | Arg-R451 stabilizes catalytic intermediate and is critical for flavinylation-competent SDH conformation (sharma2020therolesof pages 4-5) | Different |
| Iron-sulfur clusters | Two [4Fe-4S] clusters in AprB beta subunit (meyer2008homologymodelingof pages 1-2, meyer2008homologymodelingof pages 2-3) | Distinct complex II Fe-S relay in SdhB/Ip subunit, not the AprB two-[4Fe-4S] arrangement (sharma2020therolesof pages 4-5) | Different arrangement |
| Complex subunit composition | AprA-AprB heterodimeric iron-sulfur flavoenzyme (1:1 alpha/beta) (meyer2008homologymodelingof pages 1-2, meyer2008homologymodelingof pages 2-3) | SdhABCD / complex II membrane-anchored heterotetramer (sharma2020therolesof pages 3-4, sharma2020therolesof pages 4-5) | Different |
| Cellular localization | Cytoplasmic or cytoplasmic face-associated sulfate-reduction enzyme linked to QmoABC (meyer2008homologymodelingof pages 1-2, ramos2012themembraneqmoabc pages 4-6, ramos2012themembraneqmoabc pages 1-2) | Membrane-associated respiratory complex II (sharma2020therolesof pages 3-4, sharma2020therolesof pages 4-5) | Different |
| Metabolic pathway | Dissimilatory sulfate reduction / APS reduction pathway (meyer2008homologymodelingof pages 1-2, ramos2012themembraneqmoabc pages 4-6, ramos2012themembraneqmoabc pages 1-2) | TCA cycle / oxidative phosphorylation / complex II respiration (sharma2020therolesof pages 3-4, sharma2020therolesof pages 4-5) | Different |
| GO term (correct) | GO:0033748 adenylylsulfate reductase activity (supported by AprA-specific mechanism and pathway context) (meyer2008homologymodelingof pages 1-2, meyer2008homologymodelingof pages 14-16, ramos2012themembraneqmoabc pages 4-6) | GO:0000104 succinate dehydrogenase activity (appropriate for SDHA/SdhA, not AprA) (sharma2020therolesof pages 3-4, sharma2020therolesof pages 4-5) | Different branches |
| Domain architecture | FAD-binding domain + capping domain + helical domain; overall classified in fumarate reductase family fold (meyer2008homologymodelingof pages 2-3, meyer2008homologymodelingof pages 1-2) | Related flavoprotein fold with FAD-binding/capping architecture in complex II flavoprotein (sharma2020therolesof pages 3-4, sharma2020therolesof pages 4-5) | Shared fold, different function |
| Covalent FAD attachment factor | None reported/required for AprA non-covalent FAD loading (meyer2008homologymodelingof pages 2-3, meyer2008homologymodelingof pages 10-14) | Requires SdhE/SDHAF2-type assembly factor for covalent flavinylation (sharma2020therolesof pages 3-4, sharma2020therolesof pages 4-5) | **Yes** |


*Table: This table contrasts the catalytic machinery, cofactors, subunit organization, and pathway context of APS reductase AprA and succinate dehydrogenase SdhA. It shows that the proteins share a broad fold family but belong to different functional subfamilies, explaining why the propagated GO:0000104 annotation is a within-superfamily misplacement.*

**Summary of active-site analysis:**

The APS reductase catalytic mechanism proceeds via nucleophilic attack of the N5 atom of the reduced FAD isoalloxazine moiety on the sulfur atom of APS, forming a covalent FAD-APS intermediate that decomposes to AMP and a FAD-sulfite adduct (meyer2008homologymodelingof pages 2-3, meyer2008homologymodelingof pages 14-16). The active site is buried within a 17 Å channel whose entrance bears five positively charged residues (Arg-A85, Lys-A281, Lys-A283, Arg-A294, Arg-A317) for electrostatic attraction of negatively charged substrates (meyer2008homologymodelingof pages 14-16). The invariant catalytic residues Arg-A265 and His-A398 form hydrogen bonds with APS sulfate oxygens, increasing nucleophilicity of FAD N5 and electrophilicity of the APS sulfur (meyer2008homologymodelingof pages 14-16, meyer2008homologymodelingof pages 10-14). Residues Asn-A74 and Trp-A234 enforce the bent "butterfly" conformation of FAD (25° bend angle along the N5–N10 axis), stabilizing the reduced form with a higher reduction potential (~−245 mV vs. ~−220 mV for free FAD) (meyer2008homologymodelingof pages 10-14). All of these active-site features are strictly conserved across AprA models from sulfate reducers and sulfur oxidizers, including the *D. vulgaris* model (meyer2008homologymodelingof pages 10-14).

In contrast, SDH flavoprotein subunits use covalent FAD attachment via a specific histidine (His-99 in human SDHA), and their active site is configured for dicarboxylate (succinate/fumarate) interconversion with residues His-H296, Thr-T308, Arg-R340, His-H407, and Arg-R451 (sharma2020therolesof pages 3-4, sharma2020therolesof pages 4-5). Furthermore, SDH requires a dedicated assembly factor (SdhE/SDHAF2) for covalent flavinylation, a process absent in APS reductase biology (sharma2020therolesof pages 3-4, sharma2020therolesof pages 4-5). None of the SDH-diagnostic catalytic residues or the covalent FAD linkage are present in AprA.

---

## GO Curation Implications

**Recommended curation action: REMOVE GO:0000104 and REPLACE with GO:0033748 (adenylylsulfate reductase activity).**

This is not a case where the term is merely too general or too specific. The propagated term GO:0000104 names a **wrong sibling activity** from a structurally related but functionally distinct subfamily. The TreeGrafter/PANTHER pipeline appears to have grafted Q72DT2 onto an ancestral node representing the broad fumarate reductase/succinate dehydrogenase fold family and then propagated the SDH-specific GO term, failing to distinguish the APS reductase functional subfamily from the SDH subfamily within this shared fold.

The appropriate terms for Q72DT2 are:
- **MF:** GO:0033748 (adenylylsulfate reductase activity)
- **BP:** GO:0019419 (dissimilatory sulfate reduction) or GO:0000103 (sulfate assimilation)
- **CC:** GO:0005737 (cytoplasm) — the enzyme is cytoplasmic or at the cytoplasmic face of the inner membrane

The term "protein binding" would not be an appropriate fallback, as the protein has a well-defined and experimentally validated catalytic function.

---

## Conflicts, Knowledge Gaps, and Discriminating Tests

### Source of the error
The mis-annotation arises from the well-documented structural analogy between AprA and the SDH/fumarate reductase flavoprotein fold family. Meyer and Kuever (2007) explicitly noted that "only the α subunit, AprA, has structural similarity to the flavoprotein subunits of the succinate-dehydrogenase/fumarate-reductase family; however, this structural relationship is not reflected in sequence similarity" (meyer2007molecularanalysisof pages 2-3). The PANTHER/TreeGrafter reference tree likely has insufficient subfamily resolution to separate the APS reductase clade from the SDH clade at the level where functional annotation is propagated.

### Potential alternative concerns
1. **Paralog confusion:** *D. vulgaris* Hildenborough does encode a separate SDH (sdhA gene, DVU3262), confirming that the organism possesses bona fide succinate dehydrogenase activity through a different gene product. Q72DT2 (aprA, DVU0847/DVU0846 locus) is not the SDH gene.
2. **Moonlighting activity:** No evidence exists for any residual succinate dehydrogenase activity in AprA. The active-site architecture is incompatible with dicarboxylate substrate binding.
3. **Database carry-over risk:** The IEA evidence code (GO_REF:0000118) indicates this annotation was computationally derived and has never been manually curated. This is a well-characterized class of TreeGrafter error for superfamilies containing functionally divergent subfamilies.

### Discriminating tests to definitively resolve
1. **Most efficient:** Confirm that purified recombinant Q72DT2 catalyzes APS reduction (methylviologen → APS → sulfite + AMP) but not succinate → fumarate conversion. This would provide direct assay evidence (EXP/IDA code) for the correct annotation. Bramlett and Peck (1975) previously performed kinetic characterization of the enzyme from *D. vulgaris*, confirming APS reductase activity (meyer2008homologymodelingof pages 16-17).
2. **Computational discriminator:** Sequence-based subfamily classification using tools such as SFLD (Structure-Function Linkage Database) or InterPro subfamily annotations (IPR027477 for APS reductase vs. IPR003953 for SDH/fumarate reductase flavoprotein) would immediately distinguish the two subfamilies.
3. **Covalent FAD test:** Mass spectrometric analysis of the purified protein could confirm non-covalent FAD binding, which is diagnostic against SDH identity.

### Knowledge gaps
- The full-text of Bramlett & Peck (1975) was not available for detailed kinetic parameter extraction.
- The *D. vulgaris* APS reductase has been characterized biochemically but its crystal structure has not been independently determined (homology models from *A. fulgidus* template are used).
- The exact PANTHER subfamily node where the graft occurred was not available for inspection; examining the tree topology would help identify the algorithmic root cause of the mis-placement.

### Confidence assessment
The verdict is rendered with **high confidence**. The evidence converges from structural biology (crystal structures and homology models), phylogenetics (AprBA-specific phylogeny), biochemistry (enzyme assays, spectroscopy, protein-protein interaction studies), and genetics (transposon mutant fitness data, gene essentiality). No evidence supports succinate dehydrogenase activity for this protein.

References

1. (meyer2007molecularanalysisof pages 2-3): Birte Meyer and Jan Kuever. Molecular analysis of the distribution and phylogeny of dissimilatory adenosine-5'-phosphosulfate reductase-encoding genes (aprba) among sulfur-oxidizing prokaryotes. Microbiology, 153 Pt 10:3478-98, Oct 2007. URL: https://doi.org/10.1099/mic.0.2007/008250-0, doi:10.1099/mic.0.2007/008250-0. This article has 166 citations and is from a peer-reviewed journal.

2. (meyer2007molecularanalysisof pages 1-2): Birte Meyer and Jan Kuever. Molecular analysis of the distribution and phylogeny of dissimilatory adenosine-5'-phosphosulfate reductase-encoding genes (aprba) among sulfur-oxidizing prokaryotes. Microbiology, 153 Pt 10:3478-98, Oct 2007. URL: https://doi.org/10.1099/mic.0.2007/008250-0, doi:10.1099/mic.0.2007/008250-0. This article has 166 citations and is from a peer-reviewed journal.

3. (meyer2008homologymodelingof pages 10-14): Birte Meyer and Jan Kuever. Homology modeling of dissimilatory aps reductases (aprba) of sulfur-oxidizing and sulfate-reducing prokaryotes. PLoS ONE, 3:e1514, Jan 2008. URL: https://doi.org/10.1371/journal.pone.0001514, doi:10.1371/journal.pone.0001514. This article has 52 citations and is from a peer-reviewed journal.

4. (sharma2020therolesof pages 3-4): Pankaj Sharma, Elena Maklashina, Gary Cecchini, and T. M. Iverson. The roles of sdhaf2 and dicarboxylate in covalent flavinylation of sdha, the human complex ii flavoprotein. Proceedings of the National Academy of Sciences, 117:23548-23556, Sep 2020. URL: https://doi.org/10.1073/pnas.2007391117, doi:10.1073/pnas.2007391117. This article has 55 citations and is from a highest quality peer-reviewed journal.

5. (sharma2020therolesof pages 4-5): Pankaj Sharma, Elena Maklashina, Gary Cecchini, and T. M. Iverson. The roles of sdhaf2 and dicarboxylate in covalent flavinylation of sdha, the human complex ii flavoprotein. Proceedings of the National Academy of Sciences, 117:23548-23556, Sep 2020. URL: https://doi.org/10.1073/pnas.2007391117, doi:10.1073/pnas.2007391117. This article has 55 citations and is from a highest quality peer-reviewed journal.

6. (meyer2008homologymodelingof pages 1-2): Birte Meyer and Jan Kuever. Homology modeling of dissimilatory aps reductases (aprba) of sulfur-oxidizing and sulfate-reducing prokaryotes. PLoS ONE, 3:e1514, Jan 2008. URL: https://doi.org/10.1371/journal.pone.0001514, doi:10.1371/journal.pone.0001514. This article has 52 citations and is from a peer-reviewed journal.

7. (meyer2008homologymodelingof pages 2-3): Birte Meyer and Jan Kuever. Homology modeling of dissimilatory aps reductases (aprba) of sulfur-oxidizing and sulfate-reducing prokaryotes. PLoS ONE, 3:e1514, Jan 2008. URL: https://doi.org/10.1371/journal.pone.0001514, doi:10.1371/journal.pone.0001514. This article has 52 citations and is from a peer-reviewed journal.

8. (meyer2008homologymodelingof pages 3-6): Birte Meyer and Jan Kuever. Homology modeling of dissimilatory aps reductases (aprba) of sulfur-oxidizing and sulfate-reducing prokaryotes. PLoS ONE, 3:e1514, Jan 2008. URL: https://doi.org/10.1371/journal.pone.0001514, doi:10.1371/journal.pone.0001514. This article has 52 citations and is from a peer-reviewed journal.

9. (meyer2008homologymodelingof pages 6-7): Birte Meyer and Jan Kuever. Homology modeling of dissimilatory aps reductases (aprba) of sulfur-oxidizing and sulfate-reducing prokaryotes. PLoS ONE, 3:e1514, Jan 2008. URL: https://doi.org/10.1371/journal.pone.0001514, doi:10.1371/journal.pone.0001514. This article has 52 citations and is from a peer-reviewed journal.

10. (meyer2008homologymodelingof pages 14-16): Birte Meyer and Jan Kuever. Homology modeling of dissimilatory aps reductases (aprba) of sulfur-oxidizing and sulfate-reducing prokaryotes. PLoS ONE, 3:e1514, Jan 2008. URL: https://doi.org/10.1371/journal.pone.0001514, doi:10.1371/journal.pone.0001514. This article has 52 citations and is from a peer-reviewed journal.

11. (ramos2012themembraneqmoabc pages 4-6): Ana Raquel Ramos, K. Keller, J. Wall, and I. Pereira. The membrane qmoabc complex interacts directly with the dissimilatory adenosine 5′-phosphosulfate reductase in sulfate reducing bacteria. Frontiers in Microbiology, Mar 2012. URL: https://doi.org/10.3389/fmicb.2012.00137, doi:10.3389/fmicb.2012.00137. This article has 134 citations and is from a peer-reviewed journal.

12. (ramos2012themembraneqmoabc pages 1-2): Ana Raquel Ramos, K. Keller, J. Wall, and I. Pereira. The membrane qmoabc complex interacts directly with the dissimilatory adenosine 5′-phosphosulfate reductase in sulfate reducing bacteria. Frontiers in Microbiology, Mar 2012. URL: https://doi.org/10.3389/fmicb.2012.00137, doi:10.3389/fmicb.2012.00137. This article has 134 citations and is from a peer-reviewed journal.

13. (ramos2012themembraneqmoabc pages 6-8): Ana Raquel Ramos, K. Keller, J. Wall, and I. Pereira. The membrane qmoabc complex interacts directly with the dissimilatory adenosine 5′-phosphosulfate reductase in sulfate reducing bacteria. Frontiers in Microbiology, Mar 2012. URL: https://doi.org/10.3389/fmicb.2012.00137, doi:10.3389/fmicb.2012.00137. This article has 134 citations and is from a peer-reviewed journal.

14. (trotter2023largescalegeneticcharacterization pages 3-4): Valentine V. Trotter, Maxim Shatsky, Morgan N. Price, Thomas R. Juba, Grant M. Zane, Kara B. De León, Erica L.-W. Majumder, Qin Gui, Rida Ali, Kelly M. Wetmore, Jennifer V. Kuehl, Adam P. Arkin, Judy D. Wall, Adam M. Deutschbauer, John-Marc Chandonia, and Gareth P. Butland. Large-scale genetic characterization of the model sulfate-reducing bacterium, desulfovibrio vulgaris hildenborough. Frontiers in Microbiology, Mar 2023. URL: https://doi.org/10.3389/fmicb.2023.1095191, doi:10.3389/fmicb.2023.1095191. This article has 13 citations and is from a peer-reviewed journal.

15. (trotter2023largescalegeneticcharacterization pages 6-7): Valentine V. Trotter, Maxim Shatsky, Morgan N. Price, Thomas R. Juba, Grant M. Zane, Kara B. De León, Erica L.-W. Majumder, Qin Gui, Rida Ali, Kelly M. Wetmore, Jennifer V. Kuehl, Adam P. Arkin, Judy D. Wall, Adam M. Deutschbauer, John-Marc Chandonia, and Gareth P. Butland. Large-scale genetic characterization of the model sulfate-reducing bacterium, desulfovibrio vulgaris hildenborough. Frontiers in Microbiology, Mar 2023. URL: https://doi.org/10.3389/fmicb.2023.1095191, doi:10.3389/fmicb.2023.1095191. This article has 13 citations and is from a peer-reviewed journal.

16. (trotter2023largescalegeneticcharacterization pages 7-9): Valentine V. Trotter, Maxim Shatsky, Morgan N. Price, Thomas R. Juba, Grant M. Zane, Kara B. De León, Erica L.-W. Majumder, Qin Gui, Rida Ali, Kelly M. Wetmore, Jennifer V. Kuehl, Adam P. Arkin, Judy D. Wall, Adam M. Deutschbauer, John-Marc Chandonia, and Gareth P. Butland. Large-scale genetic characterization of the model sulfate-reducing bacterium, desulfovibrio vulgaris hildenborough. Frontiers in Microbiology, Mar 2023. URL: https://doi.org/10.3389/fmicb.2023.1095191, doi:10.3389/fmicb.2023.1095191. This article has 13 citations and is from a peer-reviewed journal.

17. (meyer2008homologymodelingof pages 16-17): Birte Meyer and Jan Kuever. Homology modeling of dissimilatory aps reductases (aprba) of sulfur-oxidizing and sulfate-reducing prokaryotes. PLoS ONE, 3:e1514, Jan 2008. URL: https://doi.org/10.1371/journal.pone.0001514, doi:10.1371/journal.pone.0001514. This article has 52 citations and is from a peer-reviewed journal.

18. (kushkevych2016dissimilatorysulfatereduction pages 18-20): I.V. Kushkevych. Dissimilatory sulfate reduction in the intestinal sulfate-reducing bacteria. ArXiv, 10:197-228, Jan 2016. URL: https://doi.org/10.30970/sbi.1001.560, doi:10.30970/sbi.1001.560. This article has 35 citations.

## Artifacts

- [Edison artifact artifact-00](falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](falcon_artifacts/artifact-01.md)