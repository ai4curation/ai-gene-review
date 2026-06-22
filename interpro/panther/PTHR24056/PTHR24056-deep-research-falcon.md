---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-21T20:59:47.256033'
end_time: '2026-06-21T21:16:39.334646'
duration_seconds: 1012.08
template_file: templates/interpro_family_research.md
template_variables:
  interpro_id: PTHR24056
  interpro_name: Cyclin-dependent kinase
  interpro_short_name: CDK
  interpro_type: family
  interpro_integrated: IPR050108
  member_databases: Not specified
  n_proteins: '80839'
  n_taxa: '11482'
  n_subfamilies: '155'
  interpro2go_terms: None mapped (no InterPro2GO terms for this entry)
  interpro_description: The Cyclin-dependent kinase (CDK) family is crucial for cell
    cycle regulation, transcription, and other cellular processes. CDKs are serine/threonine
    protein kinases that, when activated by binding to cyclins, phosphorylate a variety
    of substrates to mediate cell cycle progression. Different CDK-cyclin complexes
    control specific transitions between cell cycle phases. Some family members also
    play roles in transcription regulation by phosphorylating the RNA polymerase II
    C-terminal domain, affecting elongation. Others are involved in developmental
    processes, DNA repair, apoptosis, and neuronal functions. Dysregulation of CDK
    activity is linked to cancer and other diseases.
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 33
artifact_count: 2
artifact_sources:
  edison_answer_artifacts: 2
artifacts:
- filename: artifact-00.md
  path: PTHR24056-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: PTHR24056-deep-research-falcon_artifacts/artifact-01.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-01
---

## Question

# InterPro Family Research for GO Annotation Review

## ⚠️ CRITICAL: Family Identification Context

**BEFORE YOU BEGIN RESEARCH:** You are researching an **InterPro entry** (a protein
family / domain / superfamily signature), not a single gene. The goal is to judge
whether the GO terms that InterPro2GO attaches to this signature are appropriate for
**every** protein the signature matches.

### Target InterPro Entry (from the InterPro API):
- **Accession:** PTHR24056
- **Name:** Cyclin-dependent kinase
- **Short name:** CDK
- **Entry type:** family
- **Integrated into / parent:** IPR050108
- **Member database signatures:** Not specified
- **Scale:** 80839 proteins across 11482 taxa, 155 subfamilies
- **Current InterPro2GO terms (the mappings under review):** None mapped (no InterPro2GO terms for this entry)
- **InterPro description:** The Cyclin-dependent kinase (CDK) family is crucial for cell cycle regulation, transcription, and other cellular processes. CDKs are serine/threonine protein kinases that, when activated by binding to cyclins, phosphorylate a variety of substrates to mediate cell cycle progression. Different CDK-cyclin complexes control specific transitions between cell cycle phases. Some family members also play roles in transcription regulation by phosphorylating the RNA polymerase II C-terminal domain, affecting elongation. Others are involved in developmental processes, DNA repair, apoptosis, and neuronal functions. Dysregulation of CDK activity is linked to cancer and other diseases.

### Why entry type matters:

An entry of type **domain**, **repeat**, or **homologous_superfamily** identifies a
structural/functional *module*, not a whole-protein function. GO terms describing a
whole-protein activity or process attached to such a module systematically over-annotate
every protein that merely *contains* the module. An entry of type **family** is more
likely to support whole-protein function terms, but only if the family is functionally
homogeneous.

## Research Target

Provide a comprehensive, citation-backed research report on the InterPro entry
**PTHR24056 (Cyclin-dependent kinase)**, structured to support GO annotation review.

Prioritize authoritative reviews and primary literature; you may supplement with
database annotations, but treat those as potentially outdated or over-broad.

Address each of the following:

1. **Family definition and biochemistry.** What does this family/domain do
   mechanistically? What fold is it? What are the conserved catalytic or binding
   residues? Cite primary/structural literature for all claims.

2. **InterPro2GO mapping appropriateness.** For **each** GO term currently mapped to
   this entry (listed above), state whether it is true for *every* protein the signature
   matches. Flag terms that are: (a) only true for a subfamily; (b) whole-protein
   functions attached to a domain/superfamily signature; (c) so generic (e.g. "ATP
   binding", "metal ion binding", "membrane") that they carry little information; or
   (d) process/component terms that leak into taxa where the pathway/compartment is
   absent. Where a more specific GO term would be correct, name it.

3. **Functional divergence across the family.** Are there subfamilies with divergent or
   even opposite functions (neo-functionalization)? Are there catalytically dead
   (pseudo-enzyme) members that retain the fold but lost activity? Identify the
   subfamilies and what distinguishes them.

4. **Taxonomic scope.** In which clades does this signature occur, and does any mapped
   process/component term hold across all of them?

5. **Over-annotation verdict.** Summarize whether InterPro2GO for this entry is sound,
   partially over-broad, or over-annotating, and give the recommended GO action pattern
   (ACCEPT / MODIFY-to-specific / KEEP_AS_NON_CORE / MARK_AS_OVER_ANNOTATED / REMOVE)
   for genes matching it. Note any recommendation for InterPro itself (e.g. demote a
   whole-protein term on a domain entry, or move it to a child entry).

Include experimental evidence where possible, and clearly distinguish experimental
findings from inference based on structure, evolution, or bioinformatics.


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

# InterPro Family Research for GO Annotation Review

## ⚠️ CRITICAL: Family Identification Context

**BEFORE YOU BEGIN RESEARCH:** You are researching an **InterPro entry** (a protein
family / domain / superfamily signature), not a single gene. The goal is to judge
whether the GO terms that InterPro2GO attaches to this signature are appropriate for
**every** protein the signature matches.

### Target InterPro Entry (from the InterPro API):
- **Accession:** PTHR24056
- **Name:** Cyclin-dependent kinase
- **Short name:** CDK
- **Entry type:** family
- **Integrated into / parent:** IPR050108
- **Member database signatures:** Not specified
- **Scale:** 80839 proteins across 11482 taxa, 155 subfamilies
- **Current InterPro2GO terms (the mappings under review):** None mapped (no InterPro2GO terms for this entry)
- **InterPro description:** The Cyclin-dependent kinase (CDK) family is crucial for cell cycle regulation, transcription, and other cellular processes. CDKs are serine/threonine protein kinases that, when activated by binding to cyclins, phosphorylate a variety of substrates to mediate cell cycle progression. Different CDK-cyclin complexes control specific transitions between cell cycle phases. Some family members also play roles in transcription regulation by phosphorylating the RNA polymerase II C-terminal domain, affecting elongation. Others are involved in developmental processes, DNA repair, apoptosis, and neuronal functions. Dysregulation of CDK activity is linked to cancer and other diseases.

### Why entry type matters:

An entry of type **domain**, **repeat**, or **homologous_superfamily** identifies a
structural/functional *module*, not a whole-protein function. GO terms describing a
whole-protein activity or process attached to such a module systematically over-annotate
every protein that merely *contains* the module. An entry of type **family** is more
likely to support whole-protein function terms, but only if the family is functionally
homogeneous.

## Research Target

Provide a comprehensive, citation-backed research report on the InterPro entry
**PTHR24056 (Cyclin-dependent kinase)**, structured to support GO annotation review.

Prioritize authoritative reviews and primary literature; you may supplement with
database annotations, but treat those as potentially outdated or over-broad.

Address each of the following:

1. **Family definition and biochemistry.** What does this family/domain do
   mechanistically? What fold is it? What are the conserved catalytic or binding
   residues? Cite primary/structural literature for all claims.

2. **InterPro2GO mapping appropriateness.** For **each** GO term currently mapped to
   this entry (listed above), state whether it is true for *every* protein the signature
   matches. Flag terms that are: (a) only true for a subfamily; (b) whole-protein
   functions attached to a domain/superfamily signature; (c) so generic (e.g. "ATP
   binding", "metal ion binding", "membrane") that they carry little information; or
   (d) process/component terms that leak into taxa where the pathway/compartment is
   absent. Where a more specific GO term would be correct, name it.

3. **Functional divergence across the family.** Are there subfamilies with divergent or
   even opposite functions (neo-functionalization)? Are there catalytically dead
   (pseudo-enzyme) members that retain the fold but lost activity? Identify the
   subfamilies and what distinguishes them.

4. **Taxonomic scope.** In which clades does this signature occur, and does any mapped
   process/component term hold across all of them?

5. **Over-annotation verdict.** Summarize whether InterPro2GO for this entry is sound,
   partially over-broad, or over-annotating, and give the recommended GO action pattern
   (ACCEPT / MODIFY-to-specific / KEEP_AS_NON_CORE / MARK_AS_OVER_ANNOTATED / REMOVE)
   for genes matching it. Note any recommendation for InterPro itself (e.g. demote a
   whole-protein term on a domain entry, or move it to a child entry).

Include experimental evidence where possible, and clearly distinguish experimental
findings from inference based on structure, evolution, or bioinformatics.


# InterPro Family Research Report for PTHR24056 (Cyclin-Dependent Kinase)

## Executive Summary

InterPro entry **PTHR24056** represents the cyclin-dependent kinase (CDK) family, spanning 80,839 proteins across 11,482 taxa with 155 subfamilies. This entry currently has **no InterPro2GO mappings**. Based on comprehensive literature analysis, this absence of GO annotations is **appropriate and should be maintained**, because the CDK family is functionally heterogeneous at the whole-family level, exhibiting extreme divergence across three phylogenetically and functionally distinct subfamilies that would be systematically over-annotated by any biological process or specific molecular function terms applied at the family level (pellarin2025cyclindependentproteinkinases pages 2-4, pluta2024cyclin‐dependentkinasesmasters pages 3-5).

---

## 1. Family Definition and Biochemistry

### Protein Fold and Structural Architecture

Cyclin-dependent kinases are serine/threonine protein kinases belonging to the CMGC kinase superfamily (karimbayli2024insightsintothe pages 1-2). The CDK family shares a highly conserved bi-lobal kinase domain of approximately 250-300 amino acids, consisting of an N-terminal lobe (N-lobe) and a C-terminal lobe (C-lobe) with the catalytic cleft positioned between them (hope2023emergingapproachesto pages 1-2, gharbi2022crystalstructureof pages 1-2, hope2023emergingapproachesto pages 2-3).

### Conserved Catalytic Residues

**Pan-kinase conserved motifs:** The HRD and DFG motifs are universally conserved across all CDK family members and are essential for catalytic activity (karimbayli2024insightsintothe pages 1-2, karimbayli2024insightsintothe pages 2-4). These motifs coordinate ATP binding and metal ion positioning for phosphotransfer.

**ATP binding site:** The kinase ATP-binding pocket is formed between the N-lobe and C-lobe and contains a conserved glycine-rich loop (G-loop), an αC-helix, and hinge region residues that contact the adenine moiety of ATP (hope2023emergingapproachesto pages 1-2, hope2023emergingapproachesto pages 2-3). Most CDKs possess a bulky phenylalanine as the gatekeeper residue (hope2023emergingapproachesto pages 1-2).

**T-loop (activation segment):** For canonical CDKs (CDK1, CDK2, CDK4, CDK6), full activation requires phosphorylation on a conserved threonine residue within the T-loop (T160 in CDK2, T161 in CDK1, T172 in CDK4, T177 in CDK6) by the CDK-activating kinase (CAK) complex (gharbi2022crystalstructureof pages 1-2, łukasik2021cyclindependentkinases(cdk) pages 1-2, li2023unveilingthenoncanonical pages 1-2, gharbi2022crystalstructureof pages 2-4). This phosphorylation reorients the activation segment into an "out" conformation compatible with substrate binding (gharbi2022crystalstructureof pages 1-2, hope2023emergingapproachesto pages 2-3, gharbi2022crystalstructureof pages 2-4).

Importantly, some atypical CDKs (e.g., PCTAIRE and PFTAIRE subfamilies) have a **serine** instead of threonine at the corresponding T-loop position, suggesting alternative or serine-based activation mechanisms (karimbayli2024insightsintothe pages 1-2, karimbayli2024insightsintothe pages 2-4).

**Cyclin-binding domain:** CDKs are defined by a conserved cyclin-binding region, classically the **PSTAIRE motif** in CDK1-3 (pellarin2025cyclindependentproteinkinases pages 2-4, pluta2024cyclin‐dependentkinasesmasters pages 3-5, łukasik2021cyclindependentkinases(cdk) pages 1-2). This region undergoes conformational changes upon cyclin binding, enabling the αC-helix to move inward and form a critical Glu-Lys salt bridge that stabilizes the active conformation (hope2023emergingapproachesto pages 1-2, hope2023emergingapproachesto pages 2-3). 

However, the motif is not universally PSTAIRE across all CDKs. Variant motifs include **PI(L)STV(I)RE** (CDK4/6), **PSSALRE** (CDK5), **PFTAIRE** (CDK14/15), **PCTAIRE** (CDK16/17/18), and **PNQALRE** (CDK20) (pluta2024cyclin‐dependentkinasesmasters pages 3-5, karimbayli2024insightsintothe pages 1-2, karimbayli2024insightsintothe pages 2-4). These motif variations correlate with subfamily-specific cyclin partners and activation mechanisms (karimbayli2024insightsintothe pages 1-2, karimbayli2024insightsintothe pages 2-4).

### Activation Mechanisms

**Canonical two-step activation:** Cell cycle CDKs (CDK1/2/4/6) require (1) cyclin binding, which induces partial activity and conformational changes, and (2) T-loop phosphorylation by CAK (composed of CDK7, cyclin H, and MAT1), which stabilizes the active conformation and greatly enhances kinase activity (hope2023emergingapproachesto pages 1-2, łukasik2021cyclindependentkinases(cdk) pages 1-2, hope2023emergingapproachesto pages 2-3, li2023unveilingthenoncanonical pages 1-2).

**Noncanonical activation mechanisms:** CDK7 and CDK8 require a third subunit for full activation—CDK7 requires MAT1 in the CAK complex, and CDK8 requires interaction with Mediator complex components (li2023unveilingthenoncanonical pages 1-2). CDK5 does not bind classical cyclins; instead, it is activated by p35 or p39, membrane-anchored proteins with a single cyclin-box-like fold (pellarin2025cyclindependentproteinkinases pages 15-16).

**Inhibitory regulation:** Many CDKs are negatively regulated by phosphorylation on T14 and Y15 (e.g., in CDK1 and CDK2) mediated by WEE1 and MYT1 kinases, which prevent ATP binding and must be removed by CDC25 phosphatases for activation (łukasik2021cyclindependentkinases(cdk) pages 1-2, pellarin2025cyclindependentproteinkinases pages 8-9, pellarin2025cyclindependentproteinkinases pages 7-8). Additionally, CDK inhibitor (CKI) proteins—INK4 family members (p16INK4a, p15INK4b, p18INK4c, p19INK4d) and CIP/KIP family members (p21Cip1, p27Kip1, p57Kip2)—directly bind to and inhibit CDK activity (pellarin2025cyclindependentproteinkinases pages 2-4, łukasik2021cyclindependentkinases(cdk) pages 1-2, hope2023emergingapproachesto pages 2-3).

---

## 2. InterPro2GO Mapping Appropriateness

### Current Status

PTHR24056 currently has **no InterPro2GO mappings**. This is the correct annotation state for this family-level entry.

### Evaluation of Potential GO Terms

| GO Term Category | Specific GO Terms to Consider | Appropriateness (ACCEPT/REJECT/SUBFAMILY-SPECIFIC) | Rationale | Recommendation |
|---|---|---|---|---|
| Molecular function | protein serine/threonine kinase activity | ACCEPT (core, but use cautiously) | CDKs are serine/threonine protein kinases with a conserved kinase domain, catalytic HRD/DFG motifs, ATP-binding cleft, and activation segment; this is the strongest family-wide biochemical function supported across canonical CDKs, transcriptional CDKs, and atypical CDKs, although experimental depth varies by branch (hope2023emergingapproachesto pages 1-2, karimbayli2024insightsintothe pages 1-2, li2023unveilingthenoncanonical pages 1-2) | If any MF term is mapped at family level, this is the best-supported core term. |
| Molecular function | protein kinase activity | ACCEPT but less specific | True for the family, but less informative than protein serine/threonine kinase activity because available evidence supports serine/threonine-directed catalysis specifically (łukasik2021cyclindependentkinases(cdk) pages 1-2, li2023unveilingthenoncanonical pages 1-2) | Prefer the more specific serine/threonine kinase MF term over this broader parent. |
| Molecular function | cyclin binding | SUBFAMILY-SPECIFIC | Many CDKs are activated by cyclins, but binding partners and mechanisms differ substantially across the family: canonical cell-cycle CDKs bind classical cyclins, transcriptional CDKs are embedded in larger complexes, and CDK5 is activated by p35/p39 rather than classical cyclins; some atypical CDKs use noncanonical partners (pepino2021overviewofpctk3cdk18 pages 1-2, li2023unveilingthenoncanonical pages 1-2, pellarin2025cyclindependentproteinkinases pages 15-16) | Do not map at PTHR24056 family level; move to child entries/subfamilies where cyclin dependence is demonstrated. |
| Molecular function | ATP binding | REJECT | ATP binding is expected for active kinases but is too generic to be informative for InterPro2GO review; it adds little value and risks broad, low-information annotation (hope2023emergingapproachesto pages 1-2, łukasik2021cyclindependentkinases(cdk) pages 1-2) | Keep unmapped at this family level. |
| Molecular function | transferase activity, transferring phosphorus-containing groups | ACCEPT but non-preferred | Mechanistically correct for kinases, but substantially less informative than kinase-specific terms (łukasik2021cyclindependentkinases(cdk) pages 1-2, li2023unveilingthenoncanonical pages 1-2) | If used at all, replace with the more specific serine/threonine kinase activity term. |
| Biological process | cell cycle | SUBFAMILY-SPECIFIC | Cell-cycle control is a major role for CDK1/2/3/4/6 and ancestral eukaryotic CDKs, but many family members instead regulate transcription, neuronal development, ciliogenesis, membrane trafficking, or metabolism; applying cell-cycle terms to all matches would over-annotate transcriptional and atypical CDKs (pellarin2025cyclindependentproteinkinases pages 2-4, pluta2024cyclin‐dependentkinasesmasters pages 3-5, pluta2024cyclin‐dependentkinasesmasters pages 5-6, pellarin2025cyclindependentproteinkinases pages 15-16) | Do not map to the parent family; place on cell-cycle CDK child entries only. |
| Biological process | regulation of cell cycle | SUBFAMILY-SPECIFIC | Same issue as above: valid for canonical cell-cycle CDKs, not universal across transcriptional or atypical branches (pellarin2025cyclindependentproteinkinases pages 2-4, pluta2024cyclin‐dependentkinasesmasters pages 5-6, pellarin2025cyclindependentproteinkinases pages 9-10) | Restrict to child entries representing CDK1/2/3/4/6-type branches. |
| Biological process | G1/S transition of mitotic cell cycle | SUBFAMILY-SPECIFIC | Appropriate for CDK2, CDK4, CDK6, and some lineage-specific orthologs, but not for mitotic CDK1, transcriptional CDKs, or atypical CDKs (zhang2024cdk2andcdk4 pages 1-2, pellarin2025cyclindependentproteinkinases pages 7-8, pellarin2025cyclindependentproteinkinases pages 5-6) | Map only to specific G1/S CDK subfamilies if supported. |
| Biological process | G2/M transition of mitotic cell cycle / mitotic cell cycle | SUBFAMILY-SPECIFIC | Strongly supported for CDK1 and related mitotic kinases, not for most other CDKs (pellarin2025cyclindependentproteinkinases pages 8-9, pellarin2025cyclindependentproteinkinases pages 9-10) | Restrict to mitotic CDK child entries. |
| Biological process | regulation of transcription by RNA polymerase II | SUBFAMILY-SPECIFIC | Strongly supported for transcriptional CDKs such as CDK7, CDK8/19, CDK9, CDK12, and CDK13, but not for core cell-cycle CDKs as a family-wide property (hope2023emergingapproachesto pages 2-3, li2023unveilingthenoncanonical pages 1-2, pellarin2025cyclindependentproteinkinases pages 9-10) | Map only to transcriptional CDK child entries. |
| Biological process | transcription initiation / transcription elongation | SUBFAMILY-SPECIFIC | CDK7 acts in TFIIH/CAK and promoter escape; CDK9 and CDK12/13 act in pause release and elongation. These are not shared by all CDKs (hope2023emergingapproachesto pages 2-3, li2023unveilingthenoncanonical pages 1-2, pellarin2025cyclindependentproteinkinases pages 9-10) | Keep off parent family; use child/subfamily mappings. |
| Biological process | signal transduction | REJECT | Overly broad and not sufficiently discriminative; while CDKs are signaling enzymes, this process term is too generic and not useful for family-level annotation review (karimbayli2024insightsintothe pages 1-2, pellarin2025cyclindependentproteinkinases pages 28-29) | Do not map. |
| Biological process | neuron differentiation / neuronal development | SUBFAMILY-SPECIFIC | Supported mainly for CDK5 and some atypical CDKs, not universal across the family (pellarin2025cyclindependentproteinkinases pages 15-16) | Restrict to CDK5/related child entries. |
| Biological process | DNA damage response / DNA repair | SUBFAMILY-SPECIFIC | Reported for several CDKs including CDK1, CDK2, and some others, but not a universal property of all family members (pellarin2025cyclindependentproteinkinases pages 2-4, pellarin2025cyclindependentproteinkinases pages 7-8, pluta2024cyclin‐dependentkinasesmasters pages 5-6) | Annotate only at specific subfamily/gene levels. |
| Cellular component | nucleus | SUBFAMILY-SPECIFIC / REJECT at family level | Many CDKs localize to the nucleus, especially transcriptional and cell-cycle CDKs, but others are cytoplasmic, membrane-associated, centrosomal, mitochondrial, or mixed in localization; localization is not universal (pellarin2025cyclindependentproteinkinases pages 8-9, pellarin2025cyclindependentproteinkinases pages 15-16) | Do not map at the parent family level. |
| Cellular component | TFIIH complex | SUBFAMILY-SPECIFIC | Valid for CDK7 only, as part of CAK within TFIIH (hope2023emergingapproachesto pages 2-3, pellarin2025cyclindependentproteinkinases pages 9-10) | Move to CDK7-specific child entries only. |
| Cellular component | Mediator complex / CDK8 kinase module | SUBFAMILY-SPECIFIC | Valid for CDK8/CDK19 branch, not for other CDKs (li2023unveilingthenoncanonical pages 1-2, pellarin2025cyclindependentproteinkinases pages 9-10) | Restrict to CDK8/CDK19 child entries. |
| Cellular component | cyclin-dependent protein kinase holoenzyme complex | SUBFAMILY-SPECIFIC | Many CDKs form holoenzyme complexes, but partners differ markedly and some atypical CDKs use noncanonical activators; too heterogeneous for the whole family (pepino2021overviewofpctk3cdk18 pages 1-2, li2023unveilingthenoncanonical pages 1-2, pellarin2025cyclindependentproteinkinases pages 15-16) | Avoid family-level mapping; consider child entries where complex composition is stable. |
| Overall verdict | No current InterPro2GO mappings | ACCEPT CURRENT STATE | The family is biochemically coherent as a kinase family but biologically heterogeneous across cell-cycle, transcriptional, and atypical branches spanning many eukaryotic clades; therefore absence of process/component mappings is appropriate and avoids systematic over-annotation (pellarin2025cyclindependentproteinkinases pages 2-4, pluta2024cyclin‐dependentkinasesmasters pages 3-5, karimbayli2024insightsintothe pages 1-2, perezposada2019gradualevolutionof pages 11-13) | Recommended action pattern: KEEP unmapped at family level, or at most add only a core kinase MF term if InterPro requires one. |


*Table: This table summarizes which GO terms are appropriate for the PTHR24056 cyclin-dependent kinase family as a whole versus only for specific CDK subfamilies. It is useful for preventing over-annotation from a functionally diverse InterPro family entry.*

**Molecular Function Terms:**
- **Protein serine/threonine kinase activity**: This is the strongest pan-family biochemical property supported by structural and biochemical data (hope2023emergingapproachesto pages 1-2, łukasik2021cyclindependentkinases(cdk) pages 1-2, karimbayli2024insightsintothe pages 1-2, li2023unveilingthenoncanonical pages 1-2). If any MF term were to be mapped at the family level, this is the only well-supported candidate. However, even this term should be applied cautiously because experimental validation depth varies across subfamilies.
  
- **Cyclin binding**: This term would over-annotate because not all CDKs bind classical cyclins. CDK5 binds p35/p39 instead, and many atypical CDKs have noncanonical activation partners or mechanisms (pepino2021overviewofpctk3cdk18 pages 1-2, karimbayli2024insightsintothe pages 2-4, pellarin2025cyclindependentproteinkinases pages 15-16). This term should **not** be mapped at the PTHR24056 family level but could be applied to specific child subfamilies.

- **ATP binding**: Too generic and uninformative; should remain unmapped (hope2023emergingapproachesto pages 1-2, łukasik2021cyclindependentkinases(cdk) pages 1-2).

**Biological Process Terms:**
- **Cell cycle / regulation of cell cycle**: These terms are valid for cell cycle CDKs (CDK1/2/3/4/6) but **not** for transcriptional CDKs (CDK7-13, 19, 20) or atypical CDKs (CDK5, 14-18) (pellarin2025cyclindependentproteinkinases pages 2-4, pluta2024cyclin‐dependentkinasesmasters pages 3-5, pluta2024cyclin‐dependentkinasesmasters pages 5-6, pellarin2025cyclindependentproteinkinases pages 15-16, pellarin2025cyclindependentproteinkinases pages 9-10). Mapping these terms at the family level would systematically over-annotate non-cell-cycle CDKs. These should be restricted to cell-cycle CDK child entries only.

- **G1/S transition / G2/M transition**: These are even more specific and apply to subsets of cell cycle CDKs (e.g., CDK4/6 and CDK2 for G1/S; CDK1 for G2/M) (zhang2024cdk2andcdk4 pages 1-2, pellarin2025cyclindependentproteinkinases pages 8-9, pellarin2025cyclindependentproteinkinases pages 7-8, pellarin2025cyclindependentproteinkinases pages 5-6, pellarin2025cyclindependentproteinkinases pages 9-10). These should absolutely **not** be mapped at the family level.

- **Regulation of transcription by RNA polymerase II / transcription initiation / transcription elongation**: These terms are valid for transcriptional CDKs (CDK7, CDK8/19, CDK9, CDK12/13) but not for cell cycle or atypical CDKs (hope2023emergingapproachesto pages 2-3, li2023unveilingthenoncanonical pages 1-2, pellarin2025cyclindependentproteinkinases pages 9-10). Mapping at the family level would over-annotate cell-cycle and atypical branches.

- **Neuron differentiation / neuronal development**: Valid primarily for CDK5 and possibly some atypical CDKs, but not a universal family property (pellarin2025cyclindependentproteinkinases pages 15-16). Should be restricted to relevant child entries.

**Cellular Component Terms:**
- **Nucleus**: Many CDKs localize to the nucleus, but others are cytoplasmic, membrane-associated, mitochondrial, or have mixed localization (pellarin2025cyclindependentproteinkinases pages 8-9, pellarin2025cyclindependentproteinkinases pages 15-16). Not universal; should not be mapped at family level.

- **TFIIH complex / Mediator complex / CDK8 kinase module**: These are specific to CDK7 and CDK8/19, respectively, and should only be mapped to those specific child entries (hope2023emergingapproachesto pages 2-3, li2023unveilingthenoncanonical pages 1-2, pellarin2025cyclindependentproteinkinases pages 9-10).

### Recommendation for InterPro2GO

**Verdict: ACCEPT current state (no mappings) / or optionally add only "protein serine/threonine kinase activity"**

The CDK family at the PTHR24056 level is functionally too heterogeneous to support meaningful biological process or specific molecular function annotations beyond the core kinase catalytic activity. The family encompasses:
1. Cell cycle regulators (CDK1-6)
2. Transcriptional regulators (CDK7-13, 19, 20)
3. Atypical/tissue-specific kinases (CDK5, 14-18)

These subfamilies have **non-overlapping biological functions**, distinct substrate specificities, different cyclin partners, and divergent activation mechanisms (pellarin2025cyclindependentproteinkinases pages 2-4, pluta2024cyclin‐dependentkinasesmasters pages 3-5, karimbayli2024insightsintothe pages 1-2, pluta2024cyclin‐dependentkinasesmasters pages 5-6, pellarin2025cyclindependentproteinkinases pages 15-16). Applying process terms like "cell cycle" or "transcription" at the family level would systematically over-annotate proteins belonging to other functional branches.

**Recommended Action Pattern:**
- **ACCEPT** the current absence of InterPro2GO mappings.
- If InterPro requires a molecular function term, consider mapping only **"protein serine/threonine kinase activity" (GO:0004674)** with caution.
- **Do NOT map** biological process terms (cell cycle, transcription, etc.) or specific cellular component terms at this family level.
- Encourage annotation of these terms at **child subfamily entries** corresponding to cell-cycle CDKs, transcriptional CDKs, and atypical CDKs separately.

---

## 3. Functional Divergence Across the Family

The CDK family exhibits profound functional divergence organized into three main phylogenetic subfamilies (pellarin2025cyclindependentproteinkinases pages 2-4, pluta2024cyclin‐dependentkinasesmasters pages 3-5, karimbayli2024insightsintothe pages 1-2):

| Subfamily | CDK Members | Cyclin-binding Motif | Primary Functions | Cyclin Partners | Key Features |
|---|---|---|---|---|---|
| Cell cycle CDKs | CDK1, CDK2, CDK3, CDK4, CDK6 | CDK1-3: **PSTAIRE**; CDK4/6: **PI(L)STV(I)RE** | Drive core cell-cycle transitions: CDK4/6 control G1 restriction point and RB phosphorylation; CDK2 promotes G1/S transition, DNA replication, and S-phase progression; CDK1 is the master mitotic kinase for G2/M and mitosis; CDK3 contributes to G1 progression and cell-cycle gene regulation (pellarin2025cyclindependentproteinkinases pages 2-4, pellarin2025cyclindependentproteinkinases pages 5-6, pluta2024cyclin‐dependentkinasesmasters pages 5-6, pellarin2025cyclindependentproteinkinases pages 9-10) | CDK1: cyclins A/B; CDK2: cyclins E/A; CDK3: cyclins E/A/C; CDK4/6: cyclin D (pellarin2025cyclindependentproteinkinases pages 2-4, pellarin2025cyclindependentproteinkinases pages 8-9, pellarin2025cyclindependentproteinkinases pages 7-8, pluta2024cyclin‐dependentkinasesmasters pages 5-6, pellarin2025cyclindependentproteinkinases pages 9-10) | Canonical two-step activation by cyclin binding plus T-loop phosphorylation by CAK; inhibitory T14/Y15 phosphorylation in many members; strongest conservation of core cell-cycle role across eukaryotes (łukasik2021cyclindependentkinases(cdk) pages 1-2, hope2023emergingapproachesto pages 2-3, li2023unveilingthenoncanonical pages 1-2, perezposada2019gradualevolutionof pages 5-8) |
| Transcriptional CDKs | CDK7, CDK8, CDK9, CDK10, CDK11, CDK12, CDK13, CDK19, CDK20 | Diverse/non-PSTAIRE motifs; includes CDK20/CCRK (**PNQALRE**); family grouped functionally rather than by a single shared motif (karimbayli2024insightsintothe pages 1-2, pellarin2025cyclindependentproteinkinases pages 15-16) | Regulate RNA polymerase II transcription: CDK7 acts in TFIIH/CAK and Pol II CTD Ser5/Ser7 phosphorylation; CDK8/19 act in Mediator kinase module; CDK9 promotes pause release/elongation; CDK12/13 sustain elongation, RNA processing, and genome stability; CDK10/11/20 have more specialized transcription/splicing or regulatory roles (hope2023emergingapproachesto pages 2-3, li2023unveilingthenoncanonical pages 1-2, pellarin2025cyclindependentproteinkinases pages 8-9, pellarin2025cyclindependentproteinkinases pages 9-10) | CDK7-cyclin H-MAT1; CDK8/19-cyclin C; CDK9-cyclin T; CDK10-cyclin M; CDK11-cyclin L; CDK12/13-cyclin K; CDK20 can complex with cyclin H in some reports (li2023unveilingthenoncanonical pages 1-2, pellarin2025cyclindependentproteinkinases pages 8-9, pellarin2025cyclindependentproteinkinases pages 15-16, pellarin2025cyclindependentproteinkinases pages 9-10) | Often function as subunits of larger macromolecular complexes rather than simple binary cyclin-CDK dimers; some show noncanonical activation requiring third subunits (CDK7 with MAT1; CDK8 with Mediator components) (hope2023emergingapproachesto pages 2-3, li2023unveilingthenoncanonical pages 1-2, pellarin2025cyclindependentproteinkinases pages 9-10) |
| Atypical CDKs | CDK5, CDK14, CDK15, CDK16, CDK17, CDK18 | CDK5: **PSSALRE**; CDK14-15: **PFTAIRE**; CDK16-18: **PCTAIRE** (karimbayli2024insightsintothe pages 1-2, karimbayli2024insightsintothe pages 2-4, pellarin2025cyclindependentproteinkinases pages 15-16) | More specialized roles outside the canonical cell-cycle engine: CDK5 functions mainly in post-mitotic neurons, synaptic biology, migration, and neurodevelopment; PFTAIRE/PCTAIRE kinases contribute to membrane trafficking, neurite biology, genome integrity, ciliogenesis, and other tissue-specific functions (pepino2021overviewofpctk3cdk18 pages 1-2, karimbayli2024insightsintothe pages 1-2, pellarin2025cyclindependentproteinkinases pages 15-16) | CDK5 is activated by p35/p39 rather than classical cyclins; CDK14-18 can associate with noncanonical cyclins such as cyclin Y or cyclin A2 in specific contexts; CDK18 has reported activation by cyclin A2 and by phosphorylation (pepino2021overviewofpctk3cdk18 pages 1-2, karimbayli2024insightsintothe pages 2-4, pellarin2025cyclindependentproteinkinases pages 15-16) | Most divergent functional branch of the family; activation mechanisms can be noncanonical and sometimes cyclin-independent in the classical sense; several are understudied “dark kinases” with conserved kinase cores but extended regulatory regions (karimbayli2024insightsintothe pages 1-2, karimbayli2024insightsintothe pages 2-4, pellarin2025cyclindependentproteinkinases pages 15-16) |
| Evolutionary scope across subfamilies | Yeast CDKs (e.g., Cdc28/CDK1, Pho85, Kin28/CDK7-like, Srb10/CDK8-like, Bur1/CDK9-like, Ctk1), unicellular holozoan CDK1-3 ancestor, metazoan-expanded repertoires | Motif diversification from ancestral CDK-like kinases into PSTAIRE, PSSALRE, PFTAIRE, PCTAIRE, and related motifs (pluta2024cyclin‐dependentkinasesmasters pages 3-5, karimbayli2024insightsintothe pages 1-2, perezposada2019gradualevolutionof pages 11-13) | Broadly conserved in eukaryotes, with expansion from a smaller ancestral toolkit to specialized animal repertoires; core cell-cycle and transcriptional functions predate animals, whereas some subfamily specializations expanded later (pluta2024cyclin‐dependentkinasesmasters pages 3-5, perezposada2019gradualevolutionof pages 5-8, bradley2019evolutionofprotein pages 1-2, perezposada2019gradualevolutionof pages 11-13) | Yeast and unicellular eukaryotes often use fewer CDKs with broader cyclin partnerships; metazoans show more specialized pairings (pluta2024cyclin‐dependentkinasesmasters pages 3-5, perezposada2019gradualevolutionof pages 5-8, perezposada2019gradualevolutionof pages 11-13) | Important for GO review because family-level signatures span cell-cycle, transcriptional, and neuronal branches; therefore many biological-process terms are not valid for all matched proteins (pellarin2025cyclindependentproteinkinases pages 2-4, pluta2024cyclin‐dependentkinasesmasters pages 3-5, karimbayli2024insightsintothe pages 1-2, pluta2024cyclin‐dependentkinasesmasters pages 5-6) |


*Table: This table summarizes the major cyclin-dependent kinase subfamilies, their members, motifs, cyclin partners, and biological roles. It is useful for evaluating whether family-level GO annotations would be broadly valid or would over-annotate functionally divergent CDK branches.*

### Cell Cycle CDKs (CDK1-6)

**Members:** CDK1, CDK2, CDK3, CDK4, CDK6 (pellarin2025cyclindependentproteinkinases pages 2-4, pellarin2025cyclindependentproteinkinases pages 5-6, pluta2024cyclin‐dependentkinasesmasters pages 5-6)

**Function:** These are the canonical cell-cycle regulators. CDK4/6-cyclin D complexes phosphorylate retinoblastoma (Rb) protein in G1 phase, enabling progression through the restriction point. CDK2-cyclin E/A drives the G1/S transition and S-phase progression, including DNA replication initiation. CDK1-cyclin A/B is the master mitotic kinase controlling G2/M transition and mitosis (pellarin2025cyclindependentproteinkinases pages 2-4, pellarin2025cyclindependentproteinkinases pages 8-9, pellarin2025cyclindependentproteinkinases pages 7-8, pellarin2025cyclindependentproteinkinases pages 5-6, pellarin2025cyclindependentproteinkinases pages 9-10).

**Distinguishing features:** These CDKs use the canonical two-step activation (cyclin binding + T-loop phosphorylation). They are subject to tight regulation by CDC25 phosphatases, WEE1/MYT1 kinases, and CKI inhibitors (łukasik2021cyclindependentkinases(cdk) pages 1-2, hope2023emergingapproachesto pages 2-3, pellarin2025cyclindependentproteinkinases pages 8-9, pellarin2025cyclindependentproteinkinases pages 7-8).

**Experimental evidence:** Extensive biochemical, genetic, and structural data support cell-cycle functions. Knockout studies in mice demonstrate essential roles in development, with CDK1 being absolutely required for cell division, whereas CDK2/4/6 show more context-dependent essentiality (pellarin2025cyclindependentproteinkinases pages 8-9, pellarin2025cyclindependentproteinkinases pages 7-8, pellarin2025cyclindependentproteinkinases pages 5-6, pellarin2025cyclindependentproteinkinases pages 9-10).

### Transcriptional CDKs (CDK7-13, 19, 20)

**Members:** CDK7, CDK8, CDK9, CDK10, CDK11, CDK12, CDK13, CDK19, CDK20 (hope2023emergingapproachesto pages 2-3, li2023unveilingthenoncanonical pages 1-2, pellarin2025cyclindependentproteinkinases pages 15-16, pellarin2025cyclindependentproteinkinases pages 9-10)

**Function:** These CDKs regulate RNA polymerase II (Pol II) transcription by phosphorylating the C-terminal domain (CTD) of Pol II and associated transcription factors. CDK7 (in the CAK/TFIIH complex) phosphorylates Pol II CTD Ser5/Ser7 for transcription initiation. CDK8/19 (in the Mediator kinase module) regulate transcription initiation and can act as coactivators or corepressors. CDK9 (in P-TEFb) promotes pause release and elongation by phosphorylating Pol II CTD Ser2 and NELF/DSIF. CDK12/13 sustain elongation and couple transcription to RNA processing and genome stability (hope2023emergingapproachesto pages 2-3, li2023unveilingthenoncanonical pages 1-2, pellarin2025cyclindependentproteinkinases pages 9-10).

**Distinguishing features:** Transcriptional CDKs often function as subunits of large multiprotein complexes rather than simple binary cyclin-CDK dimers. Some (CDK7, CDK8) use noncanonical activation requiring a third subunit beyond cyclin binding (li2023unveilingthenoncanonical pages 1-2). Their substrate specificity is directed toward the Pol II CTD heptapeptide repeats and transcription/splicing factors rather than cell-cycle regulators (hope2023emergingapproachesto pages 2-3, pellarin2025cyclindependentproteinkinases pages 9-10).

**Experimental evidence:** Structural studies of CDK7, CDK8, and CDK9 complexes with cyclins and partner proteins reveal distinct activation mechanisms (hope2023emergingapproachesto pages 2-3, li2023unveilingthenoncanonical pages 1-2). Functional studies demonstrate roles in transcriptional regulation, mRNA processing, and chromatin modification (pellarin2025cyclindependentproteinkinases pages 9-10).

### Atypical CDKs (CDK5, 14-18)

**Members:** CDK5 (PSSALRE motif), CDK14-15 (PFTAIRE motif), CDK16-18 (PCTAIRE motif) (pepino2021overviewofpctk3cdk18 pages 1-2, karimbayli2024insightsintothe pages 1-2, karimbayli2024insightsintothe pages 2-4, pellarin2025cyclindependentproteinkinases pages 15-16)

**Function:** CDK5 is primarily expressed in post-mitotic neurons and regulates neuronal migration, synaptic plasticity, axon outgrowth, and neurodevelopment (pellarin2025cyclindependentproteinkinases pages 15-16). PCTAIRE kinases (CDK16/17/18) have diverse roles including membrane trafficking, genome integrity, ciliogenesis, and tissue-specific functions (pepino2021overviewofpctk3cdk18 pages 1-2, karimbayli2024insightsintothe pages 1-2, karimbayli2024insightsintothe pages 2-4). PFTAIRE kinases (CDK14/15) have less well-characterized roles.

**Distinguishing features:** CDK5 does **not** bind classical cyclins; it is activated by p35 or p39, which are membrane-anchored proteins with a single cyclin-box-like fold rather than the tandem cyclin-box fold of classical cyclins (pellarin2025cyclindependentproteinkinases pages 15-16). PCTAIRE/PFTAIRE kinases may interact with noncanonical cyclins (e.g., cyclin Y) or use alternative activation mechanisms (karimbayli2024insightsintothe pages 1-2, karimbayli2024insightsintothe pages 2-4). Many atypical CDKs have extended N-terminal and C-terminal regions beyond the conserved kinase domain (karimbayli2024insightsintothe pages 1-2, karimbayli2024insightsintothe pages 2-4).

**Experimental evidence:** Structural and biochemical studies of CDK5-p35/p25 complexes reveal the unique activation mechanism (pellarin2025cyclindependentproteinkinases pages 15-16). Studies of PCTAIRE kinases are more limited, with many being classified as "dark kinases" with incomplete functional characterization (karimbayli2024insightsintothe pages 1-2, karimbayli2024insightsintothe pages 2-4).

### Catalytically Inactive CDKs or Pseudokinases

**No evidence for kinase-dead CDKs:** Our comprehensive literature search found **no examples** of catalytically inactive or kinase-dead CDK pseudokinases in the family. All CDK family members appear to retain catalytic activity, although the extent of experimental validation varies across subfamilies. Unlike some other kinase families (e.g., receptor tyrosine kinases), the CDK family does not appear to include pseudokinases that have lost phosphotransferase activity but retained regulatory scaffolding functions (karimbayli2024insightsintothe pages 1-2, karimbayli2024insightsintothe pages 2-4, pellarin2025cyclindependentproteinkinases pages 15-16).

**Alternative activation mechanisms:** While not catalytically dead, some CDKs (CDK5, CDK7, CDK8, atypical CDKs) use noncanonical activation mechanisms that differ from the classical cyclin-dependent two-step activation, suggesting neofunctionalization rather than pseudoenzyme evolution (li2023unveilingthenoncanonical pages 1-2, pellarin2025cyclindependentproteinkinases pages 15-16).

---

## 4. Taxonomic Scope

### Eukaryotic Distribution

CDKs are **broadly conserved across eukaryotes** but **absent from prokaryotes** (bacteria and archaea, including Asgard archaea) (bradley2019evolutionofprotein pages 1-2, yuki2024evolutionofthe pages 2-5, perezposada2019gradualevolutionof pages 11-13, mclatchie2024phylogeneticchallengesto pages 1-2).

**Presence in major eukaryotic clades:**
- **Animals (Metazoa):** Humans have 20 CDK genes (plus CDK11A/B isoforms), with all three subfamilies (cell cycle, transcriptional, atypical) represented (pellarin2025cyclindependentproteinkinases pages 2-4, pluta2024cyclin‐dependentkinasesmasters pages 3-5). CDKs are present across invertebrate phyla including Cephalochordata, Hemichordata, Echinodermata, Onychophora, Annelida, Mollusca, and Arthropoda (yuki2024evolutionofthe pages 2-5).

- **Fungi:** Budding yeast (*Saccharomyces cerevisiae*) has 6 CDKs: Cdc28 (CDK1 ortholog), Pho85, Kin28 (CDK7-like), Srb10 (CDK8-like), Bur1 (CDK9-like), and Ctk1 (pluta2024cyclin‐dependentkinasesmasters pages 3-5, pluta2024cyclin‐dependentkinasesmasters pages 17-19, pluta2024cyclin‐dependentkinasesmasters pages 5-6). Fission yeast (*Schizosaccharomyces pombe*) has a similar repertoire including Cdc2 (CDK1), Pef1, and transcriptional CDKs (pluta2024cyclin‐dependentkinasesmasters pages 17-19, pluta2024cyclin‐dependentkinasesmasters pages 5-6).

- **Unicellular holozoans:** *Capsaspora owczarzaki* (a unicellular relative of animals) possesses cyclins A, B, and E and a single ancestral CDK1-3 gene, representing an intermediate evolutionary state before the expansion of CDKs in metazoans (perezposada2019gradualevolutionof pages 5-8, perezposada2019gradualevolutionof pages 11-13). Choanoflagellates also possess CDKs (perezposada2019gradualevolutionof pages 11-13).

- **Plants:** CDKs are present in plants, with functions in cell cycle and development (bradley2019evolutionofprotein pages 1-2).

- **Unicellular eukaryotes:** CDKs are distributed across diverse unicellular eukaryotic lineages, indicating ancient eukaryotic origin (perezposada2019gradualevolutionof pages 5-8, bradley2019evolutionofprotein pages 1-2, perezposada2019gradualevolutionof pages 11-13).

**Absence from prokaryotes:** Phylogenomic analyses confirm that CDKs are not found in bacterial or archaeal proteomes, including the Asgard superphylum archaea that are considered the closest prokaryotic relatives of eukaryotes (mclatchie2024phylogeneticchallengesto pages 1-2). This indicates that CDKs arose during or after eukaryogenesis, likely in the last eukaryotic common ancestor (LECA) (bradley2019evolutionofprotein pages 1-2, mclatchie2024phylogeneticchallengesto pages 1-2).

### Evolutionary Expansion

The CDK family has expanded from an ancestral toolkit of ~6 CDKs in unicellular eukaryotes/fungi to 20+ in mammals (pellarin2025cyclindependentproteinkinases pages 2-4, pluta2024cyclin‐dependentkinasesmasters pages 3-5, perezposada2019gradualevolutionof pages 5-8, perezposada2019gradualevolutionof pages 11-13). Key evolutionary transitions include:

1. **Core cell-cycle CDKs** (CDK1-like ancestors) are ancient and conserved across eukaryotes (perezposada2019gradualevolutionof pages 5-8, perezposada2019gradualevolutionof pages 11-13).

2. **Transcriptional CDKs** (CDK7, CDK8, CDK9 orthologs) are also ancient and conserved from fungi to animals (pluta2024cyclin‐dependentkinasesmasters pages 3-5, pluta2024cyclin‐dependentkinasesmasters pages 17-19, pluta2024cyclin‐dependentkinasesmasters pages 5-6).

3. **CDK1-3 duplication** occurred in the metazoan lineage, leading to specialized CDK1 (mitotic) and CDK2/3 (interphase) functions in animals (perezposada2019gradualevolutionof pages 5-8, perezposada2019gradualevolutionof pages 11-13).

4. **CDK4/6 evolution** is associated with the evolution of the Rb pathway in metazoans (yuki2024evolutionofthe pages 1-2, yuki2024evolutionofthe pages 2-5).

5. **Atypical CDKs** (CDK5, PCTAIRE, PFTAIRE) show lineage-specific distributions and expansions (karimbayli2024insightsintothe pages 1-2, karimbayli2024insightsintothe pages 2-4).

### Taxonomic Implications for GO Annotations

Because CDKs are restricted to eukaryotes and absent from prokaryotes, **any GO biological process or cellular component terms mapped to PTHR24056 would be eukaryote-specific**. However, within eukaryotes, not all GO process terms apply uniformly:

- **"Cell cycle" terms:** While cell-cycle CDKs are broadly conserved from yeast to mammals, applying "cell cycle" terms at the family level would over-annotate transcriptional and atypical CDKs (pellarin2025cyclindependentproteinkinases pages 2-4, pluta2024cyclin‐dependentkinasesmasters pages 3-5, pluta2024cyclin‐dependentkinasesmasters pages 5-6, perezposada2019gradualevolutionof pages 11-13).

- **"Transcription" terms:** Transcriptional CDKs are conserved across eukaryotes, but applying transcription terms at the family level would over-annotate cell-cycle and atypical CDKs (hope2023emergingapproachesto pages 2-3, li2023unveilingthenoncanonical pages 1-2, pellarin2025cyclindependentproteinkinases pages 9-10).

- **Tissue-specific terms** (e.g., "neuron differentiation"): These are valid only for specific CDKs (e.g., CDK5) in specific lineages and would massively over-annotate if applied broadly (pellarin2025cyclindependentproteinkinases pages 15-16).

**Conclusion:** The taxonomic distribution of CDKs (eukaryote-specific but functionally divergent within eukaryotes) reinforces that family-level GO annotations should be minimal or absent, with specific terms applied only at subfamily levels.

---

## 5. Over-Annotation Verdict and Recommendations

### Summary Assessment

The CDK family (PTHR24056) is **functionally heterogeneous** at the whole-family level, encompassing three phylogenetically and functionally distinct subfamilies:
1. Cell cycle regulators (CDK1-6)
2. Transcriptional regulators (CDK7-13, 19, 20)
3. Atypical/specialized kinases (CDK5, 14-18)

These subfamilies have **non-overlapping biological functions**, distinct substrate specificities, divergent activation mechanisms, and variable tissue/developmental expression patterns (pellarin2025cyclindependentproteinkinases pages 2-4, pluta2024cyclin‐dependentkinasesmasters pages 3-5, karimbayli2024insightsintothe pages 1-2, pluta2024cyclin‐dependentkinasesmasters pages 5-6, pellarin2025cyclindependentproteinkinases pages 15-16, pellarin2025cyclindependentproteinkinases pages 9-10).

### InterPro2GO Status: Sound

The **current absence of InterPro2GO mappings for PTHR24056 is appropriate and should be maintained**. Applying biological process terms like "cell cycle," "regulation of transcription by RNA polymerase II," or cellular component terms at the family level would systematically over-annotate proteins belonging to functionally divergent subfamilies.

### Recommended GO Action Pattern

**Primary recommendation: ACCEPT current state (no InterPro2GO mappings)**

- **Molecular Function:** If InterPro requires a molecular function term, consider mapping only **"protein serine/threonine kinase activity" (GO:0004674)**. This is the only biochemical property supported across all CDK subfamilies by structural and experimental data (hope2023emergingapproachesto pages 1-2, łukasik2021cyclindependentkinases(cdk) pages 1-2, karimbayli2024insightsintothe pages 1-2, li2023unveilingthenoncanonical pages 1-2). Apply with caution and note that experimental validation depth varies across subfamilies.

- **Do NOT map at family level:**
  - **Biological Process terms:** "cell cycle," "regulation of cell cycle," "G1/S transition," "G2/M transition," "regulation of transcription by RNA polymerase II," "transcription initiation," "transcription elongation," "neuron differentiation," etc.
  - **Cellular Component terms:** "nucleus," "TFIIH complex," "Mediator complex," "CDK8 kinase module," etc.
  - **Other Molecular Function terms:** "cyclin binding" (not universal; CDK5 uses p35/p39), "ATP binding" (too generic).

- **Recommended action for subfamily-specific terms:**
  - Encourage InterPro to create or use **child subfamily entries** corresponding to:
    1. Cell-cycle CDKs (e.g., CDK1/2/4/6 subfamilies)
    2. Transcriptional CDKs (e.g., CDK7, CDK8/19, CDK9, CDK12/13 subfamilies)
    3. Atypical CDKs (e.g., CDK5, PCTAIRE, PFTAIRE subfamilies)
  - Apply subfamily-specific GO process and component terms at these child levels where they are experimentally supported and apply to all members of that child entry.

### Action Pattern Code

**For genes matching PTHR24056:**
- **ACCEPT** current absence of InterPro2GO annotations
- If molecular function term is required: Consider **MODIFY-to-specific** by adding only "protein serine/threonine kinase activity" (GO:0004674)
- For subfamily-specific annotations: **Recommend annotation at child subfamily level**
- **Do NOT** apply subfamily-specific process/component terms at the family level to avoid systematic over-annotation

### Recommendation for InterPro

InterPro should consider whether PTHR24056 is appropriately scoped as a single family entry or whether it should be restructured to better reflect the functional and phylogenetic diversity of CDKs. Given that the entry encompasses 155 subfamilies spanning vastly different biological roles (cell cycle vs. transcription vs. neuronal functions), it may be more appropriate to:

1. Maintain PTHR24056 as a high-level family entry with minimal or no GO annotations (current state is correct), OR
2. Promote child subfamily entries for cell-cycle CDKs, transcriptional CDKs, and atypical CDKs, and apply GO annotations at those more functionally homogeneous levels.

Either approach would prevent the over-annotation problem inherent in applying specific biological process terms to a functionally heterogeneous family.

---

## References

All claims in this report are supported by citations to the retrieved literature (pellarin2025cyclindependentproteinkinases pages 2-4, mclatchie2024phylogeneticchallengesto pages 1-2), representing recent peer-reviewed publications from 2019-2025, including structural studies, comprehensive reviews, and experimental investigations of CDK structure, function, phylogeny, and regulation. Key references include recent reviews by Pellarin et al. (2025), Pluta et al. (2024), Hope et al. (2023), and structural determinations by Gharbi et al. (2022), Zhang et al. (2024), and Li et al. (2023), among others.

---

**Report prepared:** 2026  
**Entry reviewed:** PTHR24056 (Cyclin-dependent kinase)  
**Recommendation:** ACCEPT current absence of InterPro2GO mappings; do not add subfamily-specific process/component terms at family level.

References

1. (pellarin2025cyclindependentproteinkinases pages 2-4): Ilenia Pellarin, Alessandra Dall'Acqua, Andrea Favero, I. Segatto, Valentina Rossi, Nicole Crestan, Javad Karimbayli, B. Belletti, and Gustavo Baldassarre. Cyclin-dependent protein kinases and cell cycle regulation in biology and disease. Signal Transduction and Targeted Therapy, Jan 2025. URL: https://doi.org/10.1038/s41392-024-02080-z, doi:10.1038/s41392-024-02080-z. This article has 324 citations and is from a peer-reviewed journal.

2. (pluta2024cyclin‐dependentkinasesmasters pages 3-5): Aleksandra J. Pluta, Cécilia Studniarek, Shona Murphy, and Chris J. Norbury. Cyclin‐dependent kinases: masters of the eukaryotic universe. Wiley Interdisciplinary Reviews. RNA, Sep 2024. URL: https://doi.org/10.1002/wrna.1816, doi:10.1002/wrna.1816. This article has 58 citations and is from a peer-reviewed journal.

3. (karimbayli2024insightsintothe pages 1-2): Javad Karimbayli, Ilenia Pellarin, Barbara Belletti, and Gustavo Baldassarre. Insights into the structural and functional activities of forgotten kinases: pctaires cdks. Molecular Cancer, Jun 2024. URL: https://doi.org/10.1186/s12943-024-02043-6, doi:10.1186/s12943-024-02043-6. This article has 13 citations and is from a highest quality peer-reviewed journal.

4. (hope2023emergingapproachesto pages 1-2): Ian Hope, Jane A. Endicott, and Jessica E. Watt. Emerging approaches to cdk inhibitor development, a structural perspective. RSC Chemical Biology, 4:146-164, Jan 2023. URL: https://doi.org/10.1039/d2cb00201a, doi:10.1039/d2cb00201a. This article has 19 citations and is from a peer-reviewed journal.

5. (gharbi2022crystalstructureof pages 1-2): Severine Isabelle Gharbi, Laura A. Pelletier, Alfonso Espada, Jesus Gutiérrez, Sonia Maria Gutiérrez Sanfeliciano, Charles T. Rauch, Maria Patricia Ganado, Carmen Baquero, Elisabet Zapatero, Aiping Zhang, Jordi Benach, Anna-Maria Russell, Leticia Cano, Sandra Gomez, Howard Broughton, Nicholas Pulliam, Carmen Maria Perez, Raquel Torres, Marjoke F. Debets, Alfonso de Dios, Oscar Puig, Mark T. Hilgers, and Maria Jose Lallena. Crystal structure of active cdk4-cyclin d and mechanistic basis for abemaciclib efficacy. NPJ Breast Cancer, Nov 2022. URL: https://doi.org/10.1038/s41523-022-00494-y, doi:10.1038/s41523-022-00494-y. This article has 31 citations and is from a peer-reviewed journal.

6. (hope2023emergingapproachesto pages 2-3): Ian Hope, Jane A. Endicott, and Jessica E. Watt. Emerging approaches to cdk inhibitor development, a structural perspective. RSC Chemical Biology, 4:146-164, Jan 2023. URL: https://doi.org/10.1039/d2cb00201a, doi:10.1039/d2cb00201a. This article has 19 citations and is from a peer-reviewed journal.

7. (karimbayli2024insightsintothe pages 2-4): Javad Karimbayli, Ilenia Pellarin, Barbara Belletti, and Gustavo Baldassarre. Insights into the structural and functional activities of forgotten kinases: pctaires cdks. Molecular Cancer, Jun 2024. URL: https://doi.org/10.1186/s12943-024-02043-6, doi:10.1186/s12943-024-02043-6. This article has 13 citations and is from a highest quality peer-reviewed journal.

8. (łukasik2021cyclindependentkinases(cdk) pages 1-2): Paweł Łukasik, Michał Załuski, and Izabela Gutowska. Cyclin-dependent kinases (cdk) and their role in diseases development–review. International Journal of Molecular Sciences, 22:2935, Mar 2021. URL: https://doi.org/10.3390/ijms22062935, doi:10.3390/ijms22062935. This article has 308 citations.

9. (li2023unveilingthenoncanonical pages 1-2): Tao Li, Hui-Chi Tang, and Kuang-Lei Tsai. Unveiling the noncanonical activation mechanism of cdks: insights from recent structural studies. Frontiers in Molecular Biosciences, Nov 2023. URL: https://doi.org/10.3389/fmolb.2023.1290631, doi:10.3389/fmolb.2023.1290631. This article has 11 citations.

10. (gharbi2022crystalstructureof pages 2-4): Severine Isabelle Gharbi, Laura A. Pelletier, Alfonso Espada, Jesus Gutiérrez, Sonia Maria Gutiérrez Sanfeliciano, Charles T. Rauch, Maria Patricia Ganado, Carmen Baquero, Elisabet Zapatero, Aiping Zhang, Jordi Benach, Anna-Maria Russell, Leticia Cano, Sandra Gomez, Howard Broughton, Nicholas Pulliam, Carmen Maria Perez, Raquel Torres, Marjoke F. Debets, Alfonso de Dios, Oscar Puig, Mark T. Hilgers, and Maria Jose Lallena. Crystal structure of active cdk4-cyclin d and mechanistic basis for abemaciclib efficacy. NPJ Breast Cancer, Nov 2022. URL: https://doi.org/10.1038/s41523-022-00494-y, doi:10.1038/s41523-022-00494-y. This article has 31 citations and is from a peer-reviewed journal.

11. (pellarin2025cyclindependentproteinkinases pages 15-16): Ilenia Pellarin, Alessandra Dall'Acqua, Andrea Favero, I. Segatto, Valentina Rossi, Nicole Crestan, Javad Karimbayli, B. Belletti, and Gustavo Baldassarre. Cyclin-dependent protein kinases and cell cycle regulation in biology and disease. Signal Transduction and Targeted Therapy, Jan 2025. URL: https://doi.org/10.1038/s41392-024-02080-z, doi:10.1038/s41392-024-02080-z. This article has 324 citations and is from a peer-reviewed journal.

12. (pellarin2025cyclindependentproteinkinases pages 8-9): Ilenia Pellarin, Alessandra Dall'Acqua, Andrea Favero, I. Segatto, Valentina Rossi, Nicole Crestan, Javad Karimbayli, B. Belletti, and Gustavo Baldassarre. Cyclin-dependent protein kinases and cell cycle regulation in biology and disease. Signal Transduction and Targeted Therapy, Jan 2025. URL: https://doi.org/10.1038/s41392-024-02080-z, doi:10.1038/s41392-024-02080-z. This article has 324 citations and is from a peer-reviewed journal.

13. (pellarin2025cyclindependentproteinkinases pages 7-8): Ilenia Pellarin, Alessandra Dall'Acqua, Andrea Favero, I. Segatto, Valentina Rossi, Nicole Crestan, Javad Karimbayli, B. Belletti, and Gustavo Baldassarre. Cyclin-dependent protein kinases and cell cycle regulation in biology and disease. Signal Transduction and Targeted Therapy, Jan 2025. URL: https://doi.org/10.1038/s41392-024-02080-z, doi:10.1038/s41392-024-02080-z. This article has 324 citations and is from a peer-reviewed journal.

14. (pepino2021overviewofpctk3cdk18 pages 1-2): Rebeka de Oliveira Pepino, Fernanda Coelho, Tatiane Aparecida Buzanello Janku, Diandra Pinheiro Alencar, Walter Figueira de Azevedo, and Fernanda Canduri. Overview of pctk3/cdk18: a cyclin-dependent kinase involved in specific functions in post-mitotic cells. Oct 2021. URL: https://doi.org/10.2174/0929867328666210329122147, doi:10.2174/0929867328666210329122147. This article has 24 citations and is from a peer-reviewed journal.

15. (pluta2024cyclin‐dependentkinasesmasters pages 5-6): Aleksandra J. Pluta, Cécilia Studniarek, Shona Murphy, and Chris J. Norbury. Cyclin‐dependent kinases: masters of the eukaryotic universe. Wiley Interdisciplinary Reviews. RNA, Sep 2024. URL: https://doi.org/10.1002/wrna.1816, doi:10.1002/wrna.1816. This article has 58 citations and is from a peer-reviewed journal.

16. (pellarin2025cyclindependentproteinkinases pages 9-10): Ilenia Pellarin, Alessandra Dall'Acqua, Andrea Favero, I. Segatto, Valentina Rossi, Nicole Crestan, Javad Karimbayli, B. Belletti, and Gustavo Baldassarre. Cyclin-dependent protein kinases and cell cycle regulation in biology and disease. Signal Transduction and Targeted Therapy, Jan 2025. URL: https://doi.org/10.1038/s41392-024-02080-z, doi:10.1038/s41392-024-02080-z. This article has 324 citations and is from a peer-reviewed journal.

17. (zhang2024cdk2andcdk4 pages 1-2): Wengang Zhang, Yonglan Liu, Hyunbum Jang, and Ruth Nussinov. Cdk2 and cdk4: cell cycle functions evolve distinct, catalysis-competent conformations, offering drug targets. JACS Au, 4:1911-1927, May 2024. URL: https://doi.org/10.1021/jacsau.4c00138, doi:10.1021/jacsau.4c00138. This article has 38 citations and is from a peer-reviewed journal.

18. (pellarin2025cyclindependentproteinkinases pages 5-6): Ilenia Pellarin, Alessandra Dall'Acqua, Andrea Favero, I. Segatto, Valentina Rossi, Nicole Crestan, Javad Karimbayli, B. Belletti, and Gustavo Baldassarre. Cyclin-dependent protein kinases and cell cycle regulation in biology and disease. Signal Transduction and Targeted Therapy, Jan 2025. URL: https://doi.org/10.1038/s41392-024-02080-z, doi:10.1038/s41392-024-02080-z. This article has 324 citations and is from a peer-reviewed journal.

19. (pellarin2025cyclindependentproteinkinases pages 28-29): Ilenia Pellarin, Alessandra Dall'Acqua, Andrea Favero, I. Segatto, Valentina Rossi, Nicole Crestan, Javad Karimbayli, B. Belletti, and Gustavo Baldassarre. Cyclin-dependent protein kinases and cell cycle regulation in biology and disease. Signal Transduction and Targeted Therapy, Jan 2025. URL: https://doi.org/10.1038/s41392-024-02080-z, doi:10.1038/s41392-024-02080-z. This article has 324 citations and is from a peer-reviewed journal.

20. (perezposada2019gradualevolutionof pages 11-13): Alberto Perez-Posada, Omaya Dudin, Eduard Ocaña-Pallarès, Iñaki Ruiz-Trillo, and Andrej Ondracka. Gradual evolution of cell cycle regulation by cyclin-dependent kinases during the transition to animal multicellularity. bioRxiv, Jul 2019. URL: https://doi.org/10.1101/719534, doi:10.1101/719534. This article has 0 citations.

21. (perezposada2019gradualevolutionof pages 5-8): Alberto Perez-Posada, Omaya Dudin, Eduard Ocaña-Pallarès, Iñaki Ruiz-Trillo, and Andrej Ondracka. Gradual evolution of cell cycle regulation by cyclin-dependent kinases during the transition to animal multicellularity. bioRxiv, Jul 2019. URL: https://doi.org/10.1101/719534, doi:10.1101/719534. This article has 0 citations.

22. (bradley2019evolutionofprotein pages 1-2): David Bradley and Pedro Beltrao. Evolution of protein kinase substrate recognition at the active site. PLOS Biology, 17:e3000341, Jun 2019. URL: https://doi.org/10.1371/journal.pbio.3000341, doi:10.1371/journal.pbio.3000341. This article has 95 citations and is from a highest quality peer-reviewed journal.

23. (yuki2024evolutionofthe pages 2-5): Shiori Yuki, Shunsuke Sasaki, Yuta Yamamoto, Fumika Murakami, Kazumi Sakata, and Isato Araki. Evolution of the <i>cdk4/6</i>–<i>cdkn2</i> system in invertebrates. Genes to Cells, 29:1037-1051, Oct 2024. URL: https://doi.org/10.1111/gtc.13165, doi:10.1111/gtc.13165. This article has 1 citations and is from a peer-reviewed journal.

24. (mclatchie2024phylogeneticchallengesto pages 1-2): Jonathan McLatchie. Phylogenetic challenges to the evolutionary origin of the eukaryotic cell cycle. BIO-Complexity, Mar 2024. URL: https://doi.org/10.5048/bio-c.2024.4, doi:10.5048/bio-c.2024.4. This article has 3 citations and is from a peer-reviewed journal.

25. (pluta2024cyclin‐dependentkinasesmasters pages 17-19): Aleksandra J. Pluta, Cécilia Studniarek, Shona Murphy, and Chris J. Norbury. Cyclin‐dependent kinases: masters of the eukaryotic universe. Wiley Interdisciplinary Reviews. RNA, Sep 2024. URL: https://doi.org/10.1002/wrna.1816, doi:10.1002/wrna.1816. This article has 58 citations and is from a peer-reviewed journal.

26. (yuki2024evolutionofthe pages 1-2): Shiori Yuki, Shunsuke Sasaki, Yuta Yamamoto, Fumika Murakami, Kazumi Sakata, and Isato Araki. Evolution of the <i>cdk4/6</i>–<i>cdkn2</i> system in invertebrates. Genes to Cells, 29:1037-1051, Oct 2024. URL: https://doi.org/10.1111/gtc.13165, doi:10.1111/gtc.13165. This article has 1 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](PTHR24056-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](PTHR24056-deep-research-falcon_artifacts/artifact-01.md)

## Citations

1. karimbayli2024insightsintothe pages 1-2
2. hope2023emergingapproachesto pages 1-2
3. li2023unveilingthenoncanonical pages 1-2
4. pellarin2025cyclindependentproteinkinases pages 15-16
5. pellarin2025cyclindependentproteinkinases pages 9-10
6. yuki2024evolutionofthe pages 2-5
7. perezposada2019gradualevolutionof pages 11-13
8. bradley2019evolutionofprotein pages 1-2
9. mclatchie2024phylogeneticchallengesto pages 1-2
10. pellarin2025cyclindependentproteinkinases pages 2-4
11. gharbi2022crystalstructureof pages 1-2
12. hope2023emergingapproachesto pages 2-3
13. karimbayli2024insightsintothe pages 2-4
14. gharbi2022crystalstructureof pages 2-4
15. pellarin2025cyclindependentproteinkinases pages 8-9
16. pellarin2025cyclindependentproteinkinases pages 7-8
17. pellarin2025cyclindependentproteinkinases pages 5-6
18. pellarin2025cyclindependentproteinkinases pages 28-29
19. perezposada2019gradualevolutionof pages 5-8
20. yuki2024evolutionofthe pages 1-2
21. https://doi.org/10.1038/s41392-024-02080-z,
22. https://doi.org/10.1002/wrna.1816,
23. https://doi.org/10.1186/s12943-024-02043-6,
24. https://doi.org/10.1039/d2cb00201a,
25. https://doi.org/10.1038/s41523-022-00494-y,
26. https://doi.org/10.3390/ijms22062935,
27. https://doi.org/10.3389/fmolb.2023.1290631,
28. https://doi.org/10.2174/0929867328666210329122147,
29. https://doi.org/10.1021/jacsau.4c00138,
30. https://doi.org/10.1101/719534,
31. https://doi.org/10.1371/journal.pbio.3000341,
32. https://doi.org/10.1111/gtc.13165,
33. https://doi.org/10.5048/bio-c.2024.4,