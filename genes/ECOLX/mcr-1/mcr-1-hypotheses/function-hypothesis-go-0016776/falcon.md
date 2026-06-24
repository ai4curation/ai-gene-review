---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-24T04:28:49.986543'
end_time: '2026-06-24T04:44:29.552187'
duration_seconds: 939.57
template_file: templates/treegrafter_function_hypothesis.md
template_variables:
  organism: ECOLX
  gene: mcr-1
  gene_symbol: mcr-1
  uniprot_accession: A0A0R6L508
  taxon_id: NCBITaxon:562
  taxon_label: Escherichia coli
  focus_type: function_assignment
  hypothesis_slug: function-hypothesis-go-0016776
  hypothesis_text: mcr-1 has phosphotransferase activity, phosphate group as acceptor
    (GO:0016776).
  term_context: '- Term: phosphotransferase activity, phosphate group as acceptor
    (GO:0016776)

    - Evidence type: IEA

    - Original reference: GO_REF:0000118'
  reference_context: '- GO_REF:0000118

    - PMID:29079699'
  source_file: genes/ECOLX/mcr-1/mcr-1-ai-review.yaml
  source_selector: existing_annotations[5].function_hypothesis
  source_context_yaml: "term:\n  id: GO:0016776\n  label: phosphotransferase activity,\
    \ phosphate group as acceptor\nevidence_type: IEA\noriginal_reference_id: GO_REF:0000118"
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 26
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

- **Organism code:** ECOLX
- **Taxon:** Escherichia coli (NCBITaxon:562)
- **Gene directory:** mcr-1
- **Gene symbol:** mcr-1
- **UniProt accession:** A0A0R6L508

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** function-hypothesis-go-0016776
- **Source file:** genes/ECOLX/mcr-1/mcr-1-ai-review.yaml
- **Source selector:** existing_annotations[5].function_hypothesis

## Seed Hypothesis (propagated by TreeGrafter/PANTHER)

mcr-1 has phosphotransferase activity, phosphate group as acceptor (GO:0016776).

## Term and Decision Context

- Term: phosphotransferase activity, phosphate group as acceptor (GO:0016776)
- Evidence type: IEA
- Original reference: GO_REF:0000118

## Reference Context

- GO_REF:0000118
- PMID:29079699

## Source Context YAML

```yaml
term:
  id: GO:0016776
  label: phosphotransferase activity, phosphate group as acceptor
evidence_type: IEA
original_reference_id: GO_REF:0000118
```

## Research Objective

Decide whether **mcr-1 directly has the stated function**. Automated
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

- **Organism code:** ECOLX
- **Taxon:** Escherichia coli (NCBITaxon:562)
- **Gene directory:** mcr-1
- **Gene symbol:** mcr-1
- **UniProt accession:** A0A0R6L508

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** function-hypothesis-go-0016776
- **Source file:** genes/ECOLX/mcr-1/mcr-1-ai-review.yaml
- **Source selector:** existing_annotations[5].function_hypothesis

## Seed Hypothesis (propagated by TreeGrafter/PANTHER)

mcr-1 has phosphotransferase activity, phosphate group as acceptor (GO:0016776).

## Term and Decision Context

- Term: phosphotransferase activity, phosphate group as acceptor (GO:0016776)
- Evidence type: IEA
- Original reference: GO_REF:0000118

## Reference Context

- GO_REF:0000118
- PMID:29079699

## Source Context YAML

```yaml
term:
  id: GO:0016776
  label: phosphotransferase activity, phosphate group as acceptor
evidence_type: IEA
original_reference_id: GO_REF:0000118
```

## Research Objective

Decide whether **mcr-1 directly has the stated function**. Automated
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


# AIGR TreeGrafter Function-Inference Stress Test Report: MCR-1 / GO:0016776

## Executive Judgment

**Verdict: Partially supported / too general (Failure mode 1: Granularity / family-vs-subfamily)**

The seed hypothesis that MCR-1 has "phosphotransferase activity, phosphate group as acceptor" (GO:0016776) is **not wrong** but is **insufficiently specific** and represents a classic granularity error in phylogenetic propagation. MCR-1 is a well-characterized, catalytically active **lipid A phosphoethanolamine (pEtN) transferase** (EC 2.7.4.30) that transfers a phosphoethanolamine moiety — not a bare phosphate group — from phosphatidylethanolamine (PE) to the 4ʹ-phosphate of lipid A (zinkle2025mechanisticbasisof pages 7-8, zinkle2025mechanisticbasisof pages 1-2). Because the acceptor in this reaction is indeed a phosphate group on lipid A, GO:0016776 is technically a valid ancestor term in the GO hierarchy. However, the propagated term captures only the broad enzyme commission class (EC 2.7.4.x) and obscures the protein's actual substrate specificity, its phosphoethanolamine-transfer chemistry, and its biological role in colistin resistance. The most decisive piece of evidence is the deep mutational scanning study by Sun & Palzkill (2021) combined with the full-length cryo-EM structure by Zinkle et al. (2025), which together demonstrate that MCR-1 uses Thr285-mediated nucleophilic attack on phosphatidylethanolamine to form a covalent pEtN-enzyme intermediate, followed by transfer of pEtN to the 4ʹ-phosphate of lipid A — a reaction that is more specific than "phosphotransferase activity, phosphate group as acceptor" (sun2021deepmutationalscanning pages 10-11, sun2021deepmutationalscanning pages 3-5, zinkle2025mechanisticbasisof pages 7-8).

No evidence for pseudo-enzyme status (failure mode 2) or within-superfamily mis-placement (failure mode 3) was found. The enzyme is catalytically active with all key residues intact.

---

## Independent Family/Function Assignment

**Protein identity:** MCR-1 (UniProt A0A0R6L508) is a plasmid-encoded **lipid A phosphoethanolamine transferase** belonging to the **alkaline phosphatase superfamily**, classified as a **Class I phosphoethanolamine transferase (PET)** (anandan2020structureandfunction pages 14-17, samantha2020lipidaphosphoethanolamine pages 8-12, anandan2017structureofa pages 1-2).

**Closest characterized homolog:** NmEptA (EptA from *Neisseria meningitidis*), sharing ~36% overall sequence identity with MCR-1, with higher conservation (~50%) in the C-terminal catalytic domain (samantha2020lipidaphosphoethanolamine pages 5-8, sun2021deepmutationalscanning pages 11-13). The full-length crystal structure of NmEptA (Anandan et al. 2017, PNAS) serves as the canonical structural template for this enzyme family (anandan2017structureofa pages 1-2).

**Specific molecular function:** MCR-1 catalyzes the Zn²⁺-dependent transfer of phosphoethanolamine from phosphatidylethanolamine to the 4ʹ-phosphate group of lipid A, proceeding through a ping-pong mechanism with a covalent pEtN-Thr285 intermediate (zinkle2025mechanisticbasisof pages 7-8, sun2021deepmutationalscanning pages 10-11, thai2023phosphoethanolaminetransferasesas pages 16-18, sun2021deepmutationalscanning pages 3-5).

**Recommended GO MF term:** The most appropriate term would be a specific GO term for **"lipid A phosphoethanolamine transferase activity"** or the broader but still more precise **"phosphoethanolamine transferase activity"**. If such a specific GO term does not yet exist, one should be requested. The existing GO:0016776 is a valid ancestor/parent term but should not be the primary annotation.

**Granularity relative to seed term:** The correct annotation is **more specific** than GO:0016776 — it is a child/descendant function, not a sibling or different-branch activity.

---

## Evidence Matrix

The following table summarizes the primary evidence evaluated for this assessment:

| Citation (PMID/DOI) | Evidence Type | Supports/Refutes/Qualifies | Claim Tested | Key Finding | Organism/Assay Context | Confidence and Limitations |
|---|---|---|---|---|---|---|
| Zinkle et al. 2025, Nature Communications, doi:10.1038/s41467-025-65515-3 | Structural/evolutionary; cryo-EM | Qualifies | Does MCR-1 directly have GO:0016776, and what is its specific chemistry? | Full-length MCR-1 structure shows PE donor bound near active site and lipid A bound ~20 Å away in TM region; catalytic cycle transfers phosphoethanolamine (PEtN) to the 4'-phosphate of lipid A via T285 intermediate. This supports a phosphate-group acceptor reaction at a broad level but identifies the specific activity as lipid A phosphoethanolamine transferase, making GO:0016776 too general. (zinkle2025mechanisticbasisof pages 7-8, zinkle2025mechanisticbasisof pages 1-2) | MCR-1 structural and mechanistic analysis; ligand-bound cryo-EM and functional interpretation | High confidence for mechanism and acceptor identity; publication year 2025 is beyond the user's preferred 2023-2024 window but is highly informative. |
| Sun & Palzkill 2021, mBio, doi:10.1128/mBio.02776-21 | Direct assay + mutational scanning | Supports | Is MCR-1 an active enzyme rather than a pseudo-enzyme, and what residues are essential? | Deep mutational scanning of 23 active-site positions found 17 strongly constrained for function; T285 is catalytic nucleophile, and substitutions at T285, E246, D465 and other active-site residues markedly reduce activity/resistance. Confirms intact catalytic machinery and active PEtN transferase function. (sun2021deepmutationalscanning pages 5-7, sun2021deepmutationalscanning pages 10-11, sun2021deepmutationalscanning pages 3-5, sun2021deepmutationalscanning pages 11-13) | E. coli expressing MCR-1; polymyxin selection, deep sequencing, in vitro/in vivo functional analyses | High confidence for essential residue mapping; does not itself define the most specific GO term. |
| Thai et al. 2023, Antibiotics, doi:10.3390/antibiotics12091382 | Review/database synthesis | Qualifies | Is GO:0016776 the best functional annotation, and what is the catalytic mechanism? | Summarizes Class I PEA transferase mechanism: MCR-1 uses Zn2+-dependent ping-pong catalysis to transfer PEtN from PE to lipid A phosphate groups, with key residues Thr285, Glu246, His466 and others. Supports broad phosphotransferase classification but emphasizes a more specific phosphoethanolamine transferase activity. (thai2023phosphoethanolaminetransferasesas pages 16-18, thai2023phosphoethanolaminetransferasesas pages 14-16, thai2023phosphoethanolaminetransferasesas pages 12-14, thai2023phosphoethanolaminetransferasesas pages 7-9) | Cross-species structural/biochemical synthesis of pathogenic Gram-negative PETs | Moderate-high confidence; review rather than primary assay, but integrates multiple structural and biochemical studies. |
| Anandan et al. 2017, PNAS, doi:10.1073/pnas.1612927114 | Structural/evolutionary | Qualifies | What is the closest characterized homolog/subfamily, and could TreeGrafter have propagated a family-level term? | Full-length NmEptA structure establishes canonical Class I lipid A phosphoethanolamine transferase architecture in the alkaline phosphatase superfamily. MCR-1 is placed in this same subfamily rather than a generic phosphotransferase bucket. Supports nearest characterized homolog assignment to EptA-like lipid A PETs. (anandan2017structureofa pages 1-2) | Neisseria meningitidis EptA full-length crystal structure | High confidence for subfamily placement; homolog is not MCR-1 itself, so chemistry is inferred by homology plus later MCR-1 work. |
| Samantha & Vrielink 2020, J Mol Biol, doi:10.1016/j.jmb.2020.04.022 | Review/structural synthesis | Qualifies | Are MCR-1 catalytic residues and fold consistent with active lipid A PET enzymes? | Reviews strong structural/mechanistic congruence between MCR-1 and EptA, including conserved metal-binding residues and catalytic threonine; identifies lipid A phosphate headgroups as acceptor sites and MCR proteins as plasmid-borne EptA-like enzymes. (samantha2020lipidaphosphoethanolamine pages 8-12, samantha2020lipidaphosphoethanolamine pages 5-8) | Comparative structural biology of lipid A PETs | High confidence for conserved mechanism; review-level evidence, not a dedicated MCR-1 assay. |
| Schumann et al. 2024, Microbiol Mol Biol Rev, doi:10.1128/mmbr.00193-23 | Review/evolutionary analysis | Qualifies | Is MCR-1 correctly placed within the lipid A-modifying PET clade rather than another alkaline phosphatase-superfamily neighbor? | Distinguishes three PET clades: lipid A-modifying eptA/mcr, KDO-modifying eptB, and inner-core-modifying cptA/eptC. Supports that MCR-1 belongs specifically to the lipid A-modifying PET clade and likely evolved from chromosomal eptA-like ancestors. (schumann2024themultifacetedroles pages 4-6) | Broad comparative review of PET diversity and function | Moderate-high confidence; useful for mis-placement testing, but mostly comparative and not direct biochemical assay of MCR-1. |
| Schumann et al. 2024, mSphere, doi:10.1128/msphere.00731-24 | Direct assay/comparative functional study | Qualifies | Is MCR-1 merely generic lipid A PET activity, or a more specific site-selective subfamily function? | In isogenic E. coli, MCR-1 selectively modifies the 4'-phosphate of lipid A, unlike EptA and MCR-9 which prefer the 1-phosphate. This refines function below the broad GO:0016776 level and shows subfamily-specific acceptor-site selectivity. (schumann2024themultifacetedroles pages 4-6) | Isogenic E. coli expression system; MALDI/phenotype comparisons among PETs | High confidence for site-selectivity; recent and directly relevant, though citation context available here is summarized via review retrieval. |
| Anderson et al. 2020, J Biol Chem, doi:10.1074/jbc.RA119.011668 | Structural/evolutionary | Competing/qualifies | Could MCR-1 be mis-assigned within the alkaline phosphatase superfamily to a different neighboring subfamily? | BcsG is also a Zn2+-dependent phosphoethanolamine transferase in the alkaline phosphatase superfamily, but acts on cellulose rather than lipid A. This demonstrates that superfamily membership alone is insufficient; substrate-specific subfamily placement is essential. MCR-1 is therefore not just any alkaline-phosphatase-like phosphotransferase. (anderson2020theescherichiacoli pages 16-18) | E. coli BcsG structural and functional characterization | Moderate confidence for warning against within-superfamily overgeneralization; indirect evidence for MCR-1. |
| Liu et al. 2017, Antimicrob Agents Chemother, doi:10.1128/AAC.00580-17 | Direct assay/chemical analysis | Supports | Does MCR-1 directly modify lipid A with PEtN in vivo? | Mass spectrometric analysis showed MCR-1 causes phosphoethanolamine modification of lipid A in Gram-negative pathogens. This directly supports the specific biochemical role of MCR-1 as a lipid A phosphoethanolamine transferase. (sun2021deepmutationalscanning pages 5-7) | Gram-negative ESKAPE pathogens; lipid A structural analysis by mass spectrometry | High confidence for product identification; does not map all catalytic residues. |
| Gaballa et al. 2023, Front Cell Infect Microbiol, doi:10.3389/fcimb.2023.1060519 | Evolutionary/computational | Qualifies | Can sequence similarity alone justify GO:0016776 propagation to MCR-1? | Large-scale phylogeny of mcr-like and intrinsic PET genes found sequence similarity alone is insufficient to discriminate colistin-resistance PETs from other intrinsic lipid-modification PETs. Supports caution with TreeGrafter family-level propagation and argues for subfamily-aware curation. (schumann2024themultifacetedroles pages 4-6) | Comparative genomics/phylogeny across thousands of PET homologs | Moderate confidence; powerful for annotation caution, but not a direct enzymology study. |
| Purcell et al. 2022, J Bacteriol, doi:10.1128/JB.00498-21 | Functional genetics/physiology | Supports | Is MCR-1 an active PE-dependent lipid A PET in cells? | DgkA is required for polymyxin resistance mediated by MCR-1 and other lipid A PEtN transferases because PE donor usage generates DAG that must be recycled. This provides orthogonal physiological support for the PE-to-lipid A phosphoethanolamine transfer mechanism. (thai2023phosphoethanolaminetransferasesas pages 16-18) | E. coli genetics; dgkA deletion and polymyxin-resistance phenotyping | Moderate-high confidence; indirect for active-site chemistry but directly consistent with donor/product logic. |


*Table: This table summarizes the key primary and review evidence used to judge whether MCR-1 should carry the broad GO:0016776 annotation. It highlights that MCR-1 is an active lipid A phosphoethanolamine transferase, so the propagated term is best treated as broadly true but too general.*

---

## Active-Site / Placement Analysis

MCR-1 retains all catalytic and metal-binding residues characteristic of active Class I lipid A phosphoethanolamine transferases. Deep mutational scanning of 23 active-site positions revealed that 17 positions (75%) are essential for function, with wild-type residues strongly predominating after selection for polymyxin resistance (sun2021deepmutationalscanning pages 10-11, sun2021deepmutationalscanning pages 3-5, sun2021deepmutationalscanning pages 11-13). The core catalytic residues — Thr285 (nucleophile), Glu246, Asp465, His466 (Zn²⁺ coordination) — are identical to their equivalents in NmEptA (Thr280, Glu240, Asp452, His453) (samantha2020lipidaphosphoethanolamine pages 8-12, thai2023phosphoethanolaminetransferasesas pages 14-16, anandan2020structureandfunction pages 14-17). Mutation of Thr285 to alanine completely abolishes catalytic activity while stabilizing the protein, confirming its role as the catalytic nucleophile rather than a structural residue (sun2021deepmutationalscanning pages 11-13, sun2021deepmutationalscanning pages 10-11). Conservative substitutions at metal-binding positions (E246D, D465E) significantly reduce both pEtN transferase activity and polymyxin resistance, demonstrating the stringency of the active-site requirements (sun2021deepmutationalscanning pages 10-11).

The detailed residue-by-residue analysis and subfamily placement comparison is presented below:

| Section | Residue Position (MCR-1) / Comparison Item | Equivalent in NmEptA | Role/Function | Conservation Status | Evidence of Essentiality | Notes |
|---|---|---|---|---|---|---|
| Active site | Thr285 | Thr280 | Catalytic nucleophile; forms covalent pEtN-enzyme intermediate and coordinates catalytic Zn2+ | Identical in MCR-1 and NmEptA; absolutely conserved catalytic Thr among Class I lipid A PETs | T285A abolishes catalytic activity; deep mutational scanning found stringent WT preference at this position; phosphorylated Thr observed structurally (samantha2020lipidaphosphoethanolamine pages 8-12, thai2023phosphoethanolaminetransferasesas pages 16-18, sun2021deepmutationalscanning pages 11-13, thai2023phosphoethanolaminetransferasesas pages 14-16, anandan2020structureandfunction pages 14-17) | Decisive evidence against pseudo-enzyme interpretation |
| Active site | Glu246 | Glu240 | Zn2+ coordination; proton shuttle in first catalytic step | Identical between MCR-1 and NmEptA (samantha2020lipidaphosphoethanolamine pages 8-12, thai2023phosphoethanolaminetransferasesas pages 16-18) | Conservative substitution E246D significantly decreases polymyxin resistance/activity; strong WT enrichment in mutational scan (sun2021deepmutationalscanning pages 10-11) | Core catalytic residue supporting intact chemistry |
| Active site | Asp465 | Asp452 | Zn2+ coordination; active-site metal binding | Equivalent catalytic Asp conserved in NmEptA and Class I PETs (samantha2020lipidaphosphoethanolamine pages 8-12, thai2023phosphoethanolaminetransferasesas pages 14-16) | D465E reduces steady-state protein and activity/resistance; WT residue strongly preferred (sun2021deepmutationalscanning pages 11-13, sun2021deepmutationalscanning pages 10-11) | Supports preserved metalloenzyme architecture |
| Active site | His466 | His453 | Zn2+ coordination; catalytic metal environment/productive active-site geometry | Identical catalytic His in MCR-1 and NmEptA (samantha2020lipidaphosphoethanolamine pages 8-12, thai2023phosphoethanolaminetransferasesas pages 14-16) | Point-mutation evidence and Class I PET conservation indicate essentiality; highlighted in mechanistic models (thai2023phosphoethanolaminetransferasesas pages 16-18, zinkle2025mechanisticbasisof pages 3-4, thai2023phosphoethanolaminetransferasesas pages 14-16) | Often discussed with Asp465 as part of catalytic metal-binding set |
| Active site | His395 | His383 | Second Zn2+ coordination / catalytic support in di-zinc model | Conserved among Class I PETs (thai2023phosphoethanolaminetransferasesas pages 16-18, thai2023phosphoethanolaminetransferasesas pages 14-16) | Mechanistic/structural evidence supports importance; included among key charged/polar pocket residues (thai2023phosphoethanolaminetransferasesas pages 16-18, zinkle2025mechanisticbasisof pages 3-4) | Second Zn2+ occupancy may vary by structure/preparation, but residue is conserved |
| Active site | Thr247 | Not explicitly mapped in retrieved context | Hydrogen-bond network adjacent to catalytic center | Strong WT preference in MCR-1 mutational scan (sun2021deepmutationalscanning pages 10-11) | Mutations significantly decrease activity/resistance in active-site randomization study (sun2021deepmutationalscanning pages 10-11) | Supports intact substrate-positioning network |
| Active site | Leu120 | Not explicitly mapped in retrieved context | Hydrophobic interaction in substrate tunnel / PE accommodation | Strong WT preference in mutational scan; part of tunnel-shaped cavity (sun2021deepmutationalscanning pages 5-7, sun2021deepmutationalscanning pages 10-11) | Identified as essential in deep mutational scanning (sun2021deepmutationalscanning pages 10-11) | Important for donor-substrate handling rather than direct metal ligation |
| Active site | Phe93 | Not explicitly mapped in retrieved context | Aromatic residue at substrate tunnel entrance | Present in MCR-1 active-site tunnel architecture (sun2021deepmutationalscanning pages 5-7) | Included among tested active-site/tunnel residues affecting function in mutagenesis framework (sun2021deepmutationalscanning pages 5-7, sun2021deepmutationalscanning pages 3-5) | Contributes to PE headgroup/acyl-chain access path |
| Active site | Tyr97 | Not explicitly mapped in retrieved context | Aromatic residue at tunnel entrance | Present in active-site entrance architecture (sun2021deepmutationalscanning pages 5-7) | Functional importance inferred from active-site residue survey and tunnel design (sun2021deepmutationalscanning pages 5-7, sun2021deepmutationalscanning pages 3-5) | Tunnel-shaping residue |
| Active site | Met105 | Not explicitly mapped in retrieved context | Hydrophobic tunnel/entry residue | Present in donor-substrate tunnel (sun2021deepmutationalscanning pages 5-7) | Functional contribution inferred from active-site mutational framework (sun2021deepmutationalscanning pages 5-7, sun2021deepmutationalscanning pages 3-5) | Supports PE acyl-chain accommodation |
| Active site | Asn108 | Not explicitly mapped in retrieved context | Polar residue in tunnel body/substrate recognition | Present in tunnel body (sun2021deepmutationalscanning pages 5-7) | Functional contribution inferred from active-site mapping (sun2021deepmutationalscanning pages 5-7, sun2021deepmutationalscanning pages 3-5) | Likely participates in donor positioning |
| Active site | Ala109 | Not explicitly mapped in retrieved context | Hydrophobic tunnel residue | Present in tunnel architecture (sun2021deepmutationalscanning pages 5-7) | Functional contribution inferred from active-site mapping (sun2021deepmutationalscanning pages 5-7, sun2021deepmutationalscanning pages 3-5) | Donor-channel shaping residue |
| Active site | Glu116 | Not explicitly mapped in retrieved context | Polar/charged pocket residue near active site | Included in predicted active-site pocket of full-length structure (zinkle2025mechanisticbasisof pages 3-4) | Mechanistic importance supported by structural placement near catalytic center (zinkle2025mechanisticbasisof pages 3-4) | May help orient donor/acceptor phosphates |
| Active site | Thr117 | Not explicitly mapped in retrieved context | Hydrophilic residue at tunnel entrance | Present in tunnel entrance architecture (sun2021deepmutationalscanning pages 5-7) | Functional contribution inferred from active-site mapping (sun2021deepmutationalscanning pages 5-7, sun2021deepmutationalscanning pages 3-5) | Likely contributes to PE headgroup recognition |
| Active site | Lys333 | Not explicitly mapped in retrieved context | Polar/charged pocket residue in active-site environment | Included in predicted active-site pocket (zinkle2025mechanisticbasisof pages 3-4) | Mechanistic importance inferred from full-length structural model (zinkle2025mechanisticbasisof pages 3-4) | Candidate role in phosphate-group stabilization |
| Active site | Leu477 | Not explicitly mapped in retrieved context | Hydrophobic residue in tunnel body | Identified in tunnel-shaped cavity (sun2021deepmutationalscanning pages 5-7) | Functional contribution inferred from active-site mapping (sun2021deepmutationalscanning pages 5-7) | Likely contributes to donor acyl-chain fit |
| Placement | MCR-1 vs NmEptA (nearest characterized homolog) | NmEptA full-length lipid A PET | Same enzyme family/subfamily: Class I lipid A phosphoethanolamine transferases | MCR-1 shares ~36% overall sequence identity with NmEptA; catalytic domain more conserved than TM domain; core catalytic residues identical (samantha2020lipidaphosphoethanolamine pages 5-8, samantha2020lipidaphosphoethanolamine pages 8-12, anandan2020structureandfunction pages 14-17) | Strong structural/evolutionary support for orthologous biochemical function (anandan2020structureandfunction pages 14-17, samantha2020lipidaphosphoethanolamine pages 8-12, anandan2017structureofa pages 1-2) | Closest characterized homolog for function inference is NmEptA, not a generic phosphatase |
| Placement | Superfamily assignment | Alkaline phosphatase superfamily | Fold-level classification | Shared by MCR-1, EptA/NmEptA, and other PETs such as BcsG (anandan2020structureandfunction pages 14-17, samantha2020lipidaphosphoethanolamine pages 8-12, anandan2017structureofa pages 1-2, anderson2020theescherichiacoli pages 16-18) | Structural evidence definitive (anandan2020structureandfunction pages 14-17, samantha2020lipidaphosphoethanolamine pages 8-12, anderson2020theescherichiacoli pages 16-18) | Explains TreeGrafter susceptibility to over-broad family-level transfer |
| Placement | Donor substrate specificity | PE donor also used by EptA/NmEptA | MCR-1 transfers pEtN from phosphatidylethanolamine, not free phosphate | Conserved within Class I lipid A PETs (sun2021deepmutationalscanning pages 5-7, thai2023phosphoethanolaminetransferasesas pages 16-18) | Supported by biochemical and mechanistic studies (sun2021deepmutationalscanning pages 5-7, thai2023phosphoethanolaminetransferasesas pages 16-18) | Seed GO term misses phosphoethanolamine-specific chemistry |
| Placement | Acceptor/site selectivity: MCR-1 | Compared with EptA and other PETs | Lipid A phosphate is acceptor; MCR-1 preferentially modifies 4'-phosphate | 2024 comparative PET study: MCR-1, MCR-3, PET-C are 4'-selective; EptA and MCR-9 prefer 1-phosphate (schumann2024themultifacetedroles pages 4-6) | Experimental comparative phenotype/MS evidence (schumann2024themultifacetedroles pages 4-6) | Key subfamily-level distinction not captured by GO:0016776 |
| Placement | MCR-1 vs EptA | EptA/NmEptA modifies lipid A but often at 1-phosphate | Sibling/near-neighbor activities within same PET family; same broad chemistry, different site selectivity and phenotype | Both are lipid A PETs with common ancestry and conserved catalytic scaffold (samantha2020lipidaphosphoethanolamine pages 5-8, schumann2024themultifacetedroles pages 4-6, thai2023phosphoethanolaminetransferasesas pages 14-16) | Comparative evidence supports same branch but distinct functional granularity (schumann2024themultifacetedroles pages 4-6, thai2023phosphoethanolaminetransferasesas pages 14-16) | Seed term is too general across these subfamilies |
| Placement | MCR-1 vs other PETs (EptB, CptA/EptC, BcsG) | Distinct PET clades/substrates | Different acceptor substrates despite shared fold: Kdo/core sugars/proteins/cellulose vs lipid A | PET family splits into lipid A-modifying, Kdo-modifying, and inner-core-modifying clades; BcsG modifies cellulose (schumann2024themultifacetedroles pages 4-6, anderson2020theescherichiacoli pages 16-18) | Strong evidence for within-superfamily functional diversity (schumann2024themultifacetedroles pages 4-6, anderson2020theescherichiacoli pages 16-18) | Demonstrates why a superfamily-level annotation is insufficiently specific |
| Placement | GO implication | Broad GO:0016776 vs specific lipid A PET activity | MCR-1 directly fits a phosphoethanolamine transferase/lipid A phosphoethanolamine transferase function more specifically than broad phosphotransferase term | Broad chemistry technically compatible because lipid A phosphate is acceptor, but function is better localized to lipid A PET subfamily (zinkle2025mechanisticbasisof pages 1-2, thai2023phosphoethanolaminetransferasesas pages 16-18, samantha2020lipidaphosphoethanolamine pages 5-8, sun2021deepmutationalscanning pages 3-5) | High confidence; limitation is absence in retrieved context of a verified exact GO accession for the specific MF term | Best interpretation: annotation is partially supported but too general |


*Table: This table summarizes residue-level catalytic evidence and subfamily placement for MCR-1. It shows that MCR-1 is an intact, active lipid A phosphoethanolamine transferase in the alkaline phosphatase superfamily and that GO:0016776 is best treated as a broad, too-general annotation.*

**Key conclusions from active-site analysis:**
1. **MCR-1 is not a pseudo-enzyme.** All catalytic residues are intact and functionally validated by mutagenesis.
2. **MCR-1 is correctly placed within the Class I lipid A phosphoethanolamine transferase subfamily,** not a neighboring subfamily of the alkaline phosphatase superfamily (which includes enzymes like BcsG that modify cellulose, or EptB/CptA that modify different LPS components) (schumann2024themultifacetedroles pages 4-6, anderson2020theescherichiacoli pages 16-18).
3. **MCR-1 shows subfamily-specific site selectivity:** it preferentially modifies the 4ʹ-phosphate of lipid A, in contrast to EptA and MCR-9 which prefer the 1-phosphate (schumann2024themultifacetedroles pages 4-6). This further supports a more specific annotation than the broad GO:0016776.

---

## GO Curation Implications

**Recommended curation action: Make-more-specific**

The current GO:0016776 annotation should be **replaced with a more specific term** that accurately reflects lipid A phosphoethanolamine transferase activity. The reasoning is as follows:

1. **GO:0016776 is not incorrect** — it is a valid parent/ancestor term because MCR-1 does transfer a phosphorus-containing group (pEtN) to a phosphate-group acceptor (lipid A phosphate). The enzyme's EC classification (2.7.4.30) falls under the EC 2.7.4.x subclass ("phosphotransferases with a phosphate group as acceptor"), which corresponds to GO:0016776 (anandan2017structureofa pages 1-2).

2. **However, GO:0016776 is too general.** It does not distinguish MCR-1's pEtN transferase chemistry from unrelated phosphotransferases (e.g., nucleotide kinases, polyphosphate kinases) that also have a phosphate-group acceptor. The term fails to capture the biologically and biochemically defining feature of MCR-1: the transfer of a phosphoethanolamine moiety from a glycerophospholipid donor to lipid A (zinkle2025mechanisticbasisof pages 7-8, thai2023phosphoethanolaminetransferasesas pages 16-18).

3. **The ideal annotation** would be a term such as "lipid A phosphoethanolamine transferase activity" (if available in GO) or the more general "phosphoethanolamine transferase activity." If no such term exists at the appropriate granularity, a term request to the GO Consortium would be appropriate.

4. **This is a characteristic TreeGrafter failure mode 1 (granularity).** The PANTHER tree likely captured the broad alkaline-phosphatase-superfamily-level activity at a family node, then propagated it to MCR-1 without resolution to the specific pEtN transferase subfamily.

---

## Conflicts, Knowledge Gaps, and Discriminating Tests

### Conflicts and alternatives
- **No conflict with enzymatic activity.** MCR-1 is unambiguously an active enzyme, ruling out pseudo-enzyme concerns.
- **No within-superfamily mis-placement.** MCR-1 clearly belongs to the lipid A-modifying PET clade, not to the cellulose-modifying (BcsG), Kdo-modifying (EptB), or core-sugar-modifying (CptA/EptC) PET clades (schumann2024themultifacetedroles pages 4-6, anderson2020theescherichiacoli pages 16-18).
- **Paralog confusion risk:** The alkaline phosphatase superfamily contains diverse enzymes with the same fold but different activities (phosphatases, sulfatases, phosphodiesterases). TreeGrafter propagation at the superfamily level could erroneously assign any of these activities. In this case, the propagated term (GO:0016776) happens to be a valid ancestor but is too shallow in the hierarchy.

### Knowledge gaps
- **GO term availability:** It is not confirmed from the retrieved evidence whether a specific GO term for "lipid A phosphoethanolamine transferase activity" currently exists in the Gene Ontology. This should be verified against the live GO database.
- **Acceptor-site selectivity annotation:** MCR-1's preference for the 4ʹ-phosphate over the 1-phosphate of lipid A (schumann2024themultifacetedroles pages 4-6) represents a further level of functional specificity not captured by any standard GO MF term.
- **Quantitative kinetic parameters:** While the enzyme is clearly active, precise kinetic constants (kcat, KM) for MCR-1 under standardized conditions are not well-established in the retrieved literature, which limits quantitative comparison with other PETs.

### Discriminating tests
1. **GO term hierarchy check:** Query the GO database for child terms of GO:0016776 that specifically describe phosphoethanolamine transferase activity. If such a term exists, it should replace GO:0016776 for MCR-1.
2. **InterPro/Pfam annotation review:** Verify that MCR-1's InterPro entry maps to the specific PEtN transferase family (e.g., IPR017849/Pfam sulfatase-like domain) rather than a generic alkaline phosphatase superfamily entry, and use this to guide appropriate GO mapping.
3. **In vitro kinetic assay with defined substrates:** A direct enzymatic assay using purified full-length MCR-1, PE as donor, and Kdo₂-lipid A as acceptor, with product detection by mass spectrometry, would provide the definitive biochemical evidence for curator-verified GO annotation at the most specific level.


References

1. (zinkle2025mechanisticbasisof pages 7-8): Allen P. Zinkle, Mariana Bunoro Batista, Carmen M. Herrera, Satchal K. Erramilli, Brian Kloss, Khuram U. Ashraf, Kamil Nosol, Guozhi Zhang, Rosemary J. Cater, Michael T. Marty, Anthony A. Kossiakoff, M. Stephen Trent, Rie Nygaard, Phillip J. Stansfeld, and Filippo Mancia. Mechanistic basis of antimicrobial resistance mediated by the phosphoethanolamine transferase mcr-1. Nature Communications, Nov 2025. URL: https://doi.org/10.1038/s41467-025-65515-3, doi:10.1038/s41467-025-65515-3. This article has 4 citations and is from a highest quality peer-reviewed journal.

2. (zinkle2025mechanisticbasisof pages 1-2): Allen P. Zinkle, Mariana Bunoro Batista, Carmen M. Herrera, Satchal K. Erramilli, Brian Kloss, Khuram U. Ashraf, Kamil Nosol, Guozhi Zhang, Rosemary J. Cater, Michael T. Marty, Anthony A. Kossiakoff, M. Stephen Trent, Rie Nygaard, Phillip J. Stansfeld, and Filippo Mancia. Mechanistic basis of antimicrobial resistance mediated by the phosphoethanolamine transferase mcr-1. Nature Communications, Nov 2025. URL: https://doi.org/10.1038/s41467-025-65515-3, doi:10.1038/s41467-025-65515-3. This article has 4 citations and is from a highest quality peer-reviewed journal.

3. (sun2021deepmutationalscanning pages 10-11): Zhizeng Sun and Timothy Palzkill. Deep mutational scanning reveals the active-site sequence requirements for the colistin antibiotic resistance enzyme mcr-1. Dec 2021. URL: https://doi.org/10.1128/mbio.02776-21, doi:10.1128/mbio.02776-21. This article has 22 citations and is from a domain leading peer-reviewed journal.

4. (sun2021deepmutationalscanning pages 3-5): Zhizeng Sun and Timothy Palzkill. Deep mutational scanning reveals the active-site sequence requirements for the colistin antibiotic resistance enzyme mcr-1. Dec 2021. URL: https://doi.org/10.1128/mbio.02776-21, doi:10.1128/mbio.02776-21. This article has 22 citations and is from a domain leading peer-reviewed journal.

5. (anandan2020structureandfunction pages 14-17): Anandhi Anandan and Alice Vrielink. Structure and function of lipid a–modifying enzymes. Annals of the New York Academy of Sciences, 1459:19-37, Jan 2020. URL: https://doi.org/10.1111/nyas.14244, doi:10.1111/nyas.14244. This article has 54 citations and is from a peer-reviewed journal.

6. (samantha2020lipidaphosphoethanolamine pages 8-12): Ariela Samantha and Alice Vrielink. Lipid a phosphoethanolamine transferase: regulation, structure and immune response. Journal of Molecular Biology, 432:5184-5196, Aug 2020. URL: https://doi.org/10.1016/j.jmb.2020.04.022, doi:10.1016/j.jmb.2020.04.022. This article has 87 citations and is from a domain leading peer-reviewed journal.

7. (anandan2017structureofa pages 1-2): Anandhi Anandan, Genevieve L. Evans, Karmen Condic-Jurkic, Megan L. O’Mara, Constance M. John, Nancy J. Phillips, Gary A. Jarvis, Siobhan S. Wills, Keith A. Stubbs, Isabel Moraes, Charlene M. Kahler, and Alice Vrielink. Structure of a lipid a phosphoethanolamine transferase suggests how conformational changes govern substrate binding. Proceedings of the National Academy of Sciences, 114:2218-2223, Feb 2017. URL: https://doi.org/10.1073/pnas.1612927114, doi:10.1073/pnas.1612927114. This article has 153 citations and is from a highest quality peer-reviewed journal.

8. (samantha2020lipidaphosphoethanolamine pages 5-8): Ariela Samantha and Alice Vrielink. Lipid a phosphoethanolamine transferase: regulation, structure and immune response. Journal of Molecular Biology, 432:5184-5196, Aug 2020. URL: https://doi.org/10.1016/j.jmb.2020.04.022, doi:10.1016/j.jmb.2020.04.022. This article has 87 citations and is from a domain leading peer-reviewed journal.

9. (sun2021deepmutationalscanning pages 11-13): Zhizeng Sun and Timothy Palzkill. Deep mutational scanning reveals the active-site sequence requirements for the colistin antibiotic resistance enzyme mcr-1. Dec 2021. URL: https://doi.org/10.1128/mbio.02776-21, doi:10.1128/mbio.02776-21. This article has 22 citations and is from a domain leading peer-reviewed journal.

10. (thai2023phosphoethanolaminetransferasesas pages 16-18): Van C. Thai, Keith A. Stubbs, Mitali Sarkar-Tyson, and Charlene M. Kahler. Phosphoethanolamine transferases as drug discovery targets for therapeutic treatment of multi-drug resistant pathogenic gram-negative bacteria. Antibiotics, 12:1382, Aug 2023. URL: https://doi.org/10.3390/antibiotics12091382, doi:10.3390/antibiotics12091382. This article has 13 citations.

11. (sun2021deepmutationalscanning pages 5-7): Zhizeng Sun and Timothy Palzkill. Deep mutational scanning reveals the active-site sequence requirements for the colistin antibiotic resistance enzyme mcr-1. Dec 2021. URL: https://doi.org/10.1128/mbio.02776-21, doi:10.1128/mbio.02776-21. This article has 22 citations and is from a domain leading peer-reviewed journal.

12. (thai2023phosphoethanolaminetransferasesas pages 14-16): Van C. Thai, Keith A. Stubbs, Mitali Sarkar-Tyson, and Charlene M. Kahler. Phosphoethanolamine transferases as drug discovery targets for therapeutic treatment of multi-drug resistant pathogenic gram-negative bacteria. Antibiotics, 12:1382, Aug 2023. URL: https://doi.org/10.3390/antibiotics12091382, doi:10.3390/antibiotics12091382. This article has 13 citations.

13. (thai2023phosphoethanolaminetransferasesas pages 12-14): Van C. Thai, Keith A. Stubbs, Mitali Sarkar-Tyson, and Charlene M. Kahler. Phosphoethanolamine transferases as drug discovery targets for therapeutic treatment of multi-drug resistant pathogenic gram-negative bacteria. Antibiotics, 12:1382, Aug 2023. URL: https://doi.org/10.3390/antibiotics12091382, doi:10.3390/antibiotics12091382. This article has 13 citations.

14. (thai2023phosphoethanolaminetransferasesas pages 7-9): Van C. Thai, Keith A. Stubbs, Mitali Sarkar-Tyson, and Charlene M. Kahler. Phosphoethanolamine transferases as drug discovery targets for therapeutic treatment of multi-drug resistant pathogenic gram-negative bacteria. Antibiotics, 12:1382, Aug 2023. URL: https://doi.org/10.3390/antibiotics12091382, doi:10.3390/antibiotics12091382. This article has 13 citations.

15. (schumann2024themultifacetedroles pages 4-6): Anna Schumann, Ahmed Gaballa, and Martin Wiedmann. The multifaceted roles of phosphoethanolamine-modified lipopolysaccharides: from stress response and virulence to cationic antimicrobial resistance. Microbiology and Molecular Biology Reviews, Dec 2024. URL: https://doi.org/10.1128/mmbr.00193-23, doi:10.1128/mmbr.00193-23. This article has 13 citations and is from a domain leading peer-reviewed journal.

16. (anderson2020theescherichiacoli pages 16-18): Alexander C. Anderson, Alysha J.N. Burnett, Lana Hiscock, Kenneth E. Maly, and Joel T. Weadge. The escherichia coli cellulose synthase subunit g (bcsg) is a zn2+-dependent phosphoethanolamine transferase. Journal of Biological Chemistry, 295:6225-6235, May 2020. URL: https://doi.org/10.1074/jbc.ra119.011668, doi:10.1074/jbc.ra119.011668. This article has 36 citations and is from a domain leading peer-reviewed journal.

17. (zinkle2025mechanisticbasisof pages 3-4): Allen P. Zinkle, Mariana Bunoro Batista, Carmen M. Herrera, Satchal K. Erramilli, Brian Kloss, Khuram U. Ashraf, Kamil Nosol, Guozhi Zhang, Rosemary J. Cater, Michael T. Marty, Anthony A. Kossiakoff, M. Stephen Trent, Rie Nygaard, Phillip J. Stansfeld, and Filippo Mancia. Mechanistic basis of antimicrobial resistance mediated by the phosphoethanolamine transferase mcr-1. Nature Communications, Nov 2025. URL: https://doi.org/10.1038/s41467-025-65515-3, doi:10.1038/s41467-025-65515-3. This article has 4 citations and is from a highest quality peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](falcon_artifacts/artifact-01.md)