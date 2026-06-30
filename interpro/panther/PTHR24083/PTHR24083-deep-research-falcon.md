---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-28T21:13:56.888102'
end_time: '2026-06-28T21:42:21.415255'
duration_seconds: 1704.53
template_file: templates/interpro_family_research.md
template_variables:
  interpro_id: PTHR24083
  interpro_name: Nuclear hormone receptor family NR2 subfamily
  interpro_short_name: Nuclear_hormone_rcpt_NR2
  interpro_type: family
  interpro_integrated: IPR050274
  member_databases: Not specified
  n_proteins: '26277'
  n_taxa: '4759'
  n_subfamilies: '52'
  interpro2go_terms: None mapped (no InterPro2GO terms for this entry)
  interpro_description: The nuclear hormone receptor family NR2 subfamily consists
    of transcription factors that play diverse roles in regulating gene expression
    in various biological processes, including development, metabolism, and immune
    response. Members of this family are characterized by their ability to bind DNA
    as monomers or heterodimers to hormone response elements (HREs) and modulate transcription
    in response to ligands such as retinoic acid. They are involved in critical functions
    such as retinal development, circadian rhythm maintenance, lipid metabolism, and
    embryogenesis. Some act as orphan receptors with no known ligands, while others
    are activated by retinoids. They can function as repressors or activators of transcription,
    influencing pathways like spermatogenesis, stem cell proliferation, and photoreceptor
    cell development. The family includes receptors that are essential for vision,
    regulators of hormonal responses, and mediators of developmental processes in
    both vertebrates and invertebrates.
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 36
artifact_count: 2
artifact_sources:
  edison_answer_artifacts: 2
artifacts:
- filename: artifact-00.md
  path: PTHR24083-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: PTHR24083-deep-research-falcon_artifacts/artifact-01.md
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
- **Accession:** PTHR24083
- **Name:** Nuclear hormone receptor family NR2 subfamily
- **Short name:** Nuclear_hormone_rcpt_NR2
- **Entry type:** family
- **Integrated into / parent:** IPR050274
- **Member database signatures:** Not specified
- **Scale:** 26277 proteins across 4759 taxa, 52 subfamilies
- **Current InterPro2GO terms (the mappings under review):** None mapped (no InterPro2GO terms for this entry)
- **InterPro description:** The nuclear hormone receptor family NR2 subfamily consists of transcription factors that play diverse roles in regulating gene expression in various biological processes, including development, metabolism, and immune response. Members of this family are characterized by their ability to bind DNA as monomers or heterodimers to hormone response elements (HREs) and modulate transcription in response to ligands such as retinoic acid. They are involved in critical functions such as retinal development, circadian rhythm maintenance, lipid metabolism, and embryogenesis. Some act as orphan receptors with no known ligands, while others are activated by retinoids. They can function as repressors or activators of transcription, influencing pathways like spermatogenesis, stem cell proliferation, and photoreceptor cell development. The family includes receptors that are essential for vision, regulators of hormonal responses, and mediators of developmental processes in both vertebrates and invertebrates.

### Why entry type matters:

An entry of type **domain**, **repeat**, or **homologous_superfamily** identifies a
structural/functional *module*, not a whole-protein function. GO terms describing a
whole-protein activity or process attached to such a module systematically over-annotate
every protein that merely *contains* the module. An entry of type **family** is more
likely to support whole-protein function terms, but only if the family is functionally
homogeneous.

## Research Target

Provide a comprehensive, citation-backed research report on the InterPro entry
**PTHR24083 (Nuclear hormone receptor family NR2 subfamily)**, structured to support GO annotation review.

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
- **Accession:** PTHR24083
- **Name:** Nuclear hormone receptor family NR2 subfamily
- **Short name:** Nuclear_hormone_rcpt_NR2
- **Entry type:** family
- **Integrated into / parent:** IPR050274
- **Member database signatures:** Not specified
- **Scale:** 26277 proteins across 4759 taxa, 52 subfamilies
- **Current InterPro2GO terms (the mappings under review):** None mapped (no InterPro2GO terms for this entry)
- **InterPro description:** The nuclear hormone receptor family NR2 subfamily consists of transcription factors that play diverse roles in regulating gene expression in various biological processes, including development, metabolism, and immune response. Members of this family are characterized by their ability to bind DNA as monomers or heterodimers to hormone response elements (HREs) and modulate transcription in response to ligands such as retinoic acid. They are involved in critical functions such as retinal development, circadian rhythm maintenance, lipid metabolism, and embryogenesis. Some act as orphan receptors with no known ligands, while others are activated by retinoids. They can function as repressors or activators of transcription, influencing pathways like spermatogenesis, stem cell proliferation, and photoreceptor cell development. The family includes receptors that are essential for vision, regulators of hormonal responses, and mediators of developmental processes in both vertebrates and invertebrates.

### Why entry type matters:

An entry of type **domain**, **repeat**, or **homologous_superfamily** identifies a
structural/functional *module*, not a whole-protein function. GO terms describing a
whole-protein activity or process attached to such a module systematically over-annotate
every protein that merely *contains* the module. An entry of type **family** is more
likely to support whole-protein function terms, but only if the family is functionally
homogeneous.

## Research Target

Provide a comprehensive, citation-backed research report on the InterPro entry
**PTHR24083 (Nuclear hormone receptor family NR2 subfamily)**, structured to support GO annotation review.

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


# Comprehensive Research Report: PTHR24083 — Nuclear Hormone Receptor Family NR2 Subfamily

## 1. Family Definition and Biochemistry

### Overview and Classification

PTHR24083 corresponds to the Nuclear Hormone Receptor Family NR2 Subfamily, a large and functionally diverse group within the nuclear receptor (NR) superfamily of ligand-regulated transcription factors. The NR2 family encompasses 11 human receptors distributed across five subgroups (NR2A, NR2B, NR2C, NR2E, and NR2F), spanning 26,277 proteins across 4,759 taxa with 52 subfamilies in InterPro. The human NR2 members include HNF4α/γ (NR2A), RXRα/β/γ (NR2B), TR2/TR4 (NR2C), TLX/PNR (NR2E), and COUP-TFI/II/EAR2 (NR2F) (lewandowski2025comparativeevaluationand pages 3-4, lewandowski2025comparativeevaluationand pages 1-3).

### Structural Fold

All canonical NR2 members share the modular nuclear receptor architecture: an unstructured N-terminal domain (NTD) containing the AF-1 transactivation function, a highly conserved DNA-binding domain (DBD), a flexible hinge region, and a ligand-binding domain (LBD) containing the AF-2 surface (weikum2018thenuclearreceptor pages 41-46). The LBD adopts a conserved fold comprising 11 α-helices and 4 β-strands arranged as a triple-layered α-helical sandwich, creating a hydrophobic ligand-binding pocket at its base (weikum2018thenuclearreceptor pages 5-9, folkertsma2005thenuclearreceptor pages 53-57, folkertsma2005thenuclearreceptor pages 27-31). The ligand-binding pocket is primarily formed by helices H3, H5, H6, H11, and a small β-sheet region (folkertsma2005thenuclearreceptor pages 27-31).

### DNA-Binding Domain and Zinc Fingers

The DBD is the most conserved domain across the NR superfamily. It consists of approximately 66 residues containing two C4-type zinc finger motifs, each coordinating a zinc ion through four cysteine residues. The first zinc finger's DNA-reading helix makes base-specific contacts in the DNA major groove at genomic response elements, while the second zinc finger's helix participates in dimerization and makes non-specific DNA backbone contacts (weikum2018thenuclearreceptor pages 5-9, folkertsma2005thenuclearreceptor pages 27-31). The P-box region within the first zinc finger confers target DNA specificity; NR2 members such as RXR and HNF4 recognize the AGGTCA half-site motif (owen2000originsandevolutionary pages 2-3).

### Key NR2-Specific Structural Features

HNF4 (NR2A) exhibits a distinctive β-turn in helix 7 characterized by a conserved RxxxE motif with a p-helical geometry, shared only with RXR among nuclear receptors. This feature is critical for stable homodimerization (beinsteiner2023structuralinsightsinto pages 2-4). HNF4 also has the shortest hinge region among nuclear receptors at only 17 amino acids (beinsteiner2023structuralinsightsinto pages 5-8). NR2C and NR2E subfamilies share an autorepressed LBD conformation caused by a kink between helices 10–11, where helix 11 collapses into the ligand-binding site space. These receptors possess a conserved Atro-box motif (ALXXLXXY) beneath helix 12 that recruits atrophin corepressor proteins (lewandowski2025comparativeevaluationand pages 3-4). COUP-TFII (NR2F2) exhibits a related autorepressed conformation in which helix α10 bends into the ligand-binding pocket and the AF-2 helix folds into the cofactor binding site, preventing coactivator recruitment (kruse2008identificationofcouptfii pages 8-11, kruse2008identificationofcouptfii pages 1-2).

---

## 2. InterPro2GO Mapping Appropriateness

**Current status:** No InterPro2GO terms are mapped to PTHR24083.

Given the extreme functional heterogeneity of the NR2 family, the absence of GO mappings is **appropriate**. The following table systematically evaluates candidate GO terms that might be considered:

| Candidate GO Term | GO ID | Aspect (MF/BP/CC) | True for All NR2 Members? | Assessment | Recommendation |
|---|---|---|---|---|---|
| DNA binding | GO:0003677 | MF | No | Not universal for the family because early-diverging ctenophore NR2A-like proteins can lack the canonical zinc-finger DBD; mapping at this family level would over-annotate those members (reitzel2011nuclearreceptorsfrom pages 8-9, lewandowski2025comparativeevaluationand pages 1-3) | REMOVE / do not map at PTHR24083 |
| Zinc ion binding | GO:0008270 | MF | No | Usually expected for canonical nuclear receptor DBDs, but not true for all NR2 matches because some ctenophore NR2 receptors lack the zinc-finger DBD entirely (reitzel2011nuclearreceptorsfrom pages 8-9, weikum2018thenuclearreceptor pages 5-9, lewandowski2025comparativeevaluationand pages 1-3) | REMOVE / do not map at PTHR24083 |
| Nucleus | GO:0005634 | CC | Mostly, but not all contexts securely demonstrated across all taxa | Broadly plausible because NR2 receptors are generally nuclear transcription factors, yet a family-wide CC assertion across highly divergent metazoan members is weaker than it appears, especially given noncanonical localization/activities reported for some nuclear receptors more generally (weikum2018thenuclearreceptor pages 46-56, lewandowski2025comparativeevaluationand pages 1-3) | KEEP_AS_NON_CORE at most; preferably no family-level map |
| Transcription regulator activity | GO:0140110 | MF | Mostly, but not proven for every match | This is the broadest defensible shared function for canonical NR2 proteins, but still not ideal for every family match because of extreme divergence and DBD loss in some early-branching members; acceptable only as a very high-level non-core inference (lewandowski2025comparativeevaluationand pages 1-3, lewandowski2025comparativeevaluationand pages 3-4) | KEEP_AS_NON_CORE or leave unmapped |
| Sequence-specific DNA binding | GO:0043565 | MF | No | Over-broad at family level because sequence-specific DNA binding depends on a canonical DBD that is absent from some ctenophore NR2 proteins; also DNA recognition modes differ across NR2 subfamilies (reitzel2011nuclearreceptorsfrom pages 8-9, weikum2018thenuclearreceptor pages 5-9, beinsteiner2023structuralinsightsinto pages 5-8) | REMOVE / do not map at PTHR24083 |
| Regulation of transcription | GO:0006355 | BP | Mostly, but too broad and not secure for every match | Captures a common high-level role of many NR2 proteins but is biologically diffuse and vulnerable to over-annotation in a family spanning activators, repressors, and DBD-lacking forms; little value at this parent family level (lewandowski2025comparativeevaluationand pages 3-4, lewandowski2025comparativeevaluationand pages 1-3, weikum2018thenuclearreceptor pages 46-56) | KEEP_AS_NON_CORE at most; preferably no family-level map |
| Lipid metabolism | GO:0006629 | BP | No | Restricted mainly to HNF4-centered metabolic regulation and some RXR-linked pathways; not true for neural/retinal/developmental NR2E or NR2F members (lewandowski2025comparativeevaluationand pages 3-4, lewandowski2025comparativeevaluationand pages 4-6) | REMOVE; move to appropriate child entries/subfamilies |
| Retinoid binding | GO:0005501 | MF | No | Characteristic primarily of RXR (NR2B) and not the rest of the NR2 family; would strongly over-annotate orphan and non-retinoid-binding subfamilies (beinsteiner2023structuralinsightsinto pages 1-2, lewandowski2025comparativeevaluationand pages 3-4, kruse2008identificationofcouptfii pages 8-11) | REMOVE; if used, restrict to RXR child family |
| Photoreceptor development | GO:0042461 | BP | No | Specific to NR2E3/PNR lineage and inappropriate for HNF4, RXR, TR2/4, TLX, or COUP-TF family members (lewandowski2025comparativeevaluationand pages 4-6, lewandowski2025comparativeevaluationand pages 20-21, safe2025orphannuclearreceptor pages 17-19) | REMOVE; map only to NR2E3-specific child entry |
| Neurogenesis | GO:0022008 | BP | No | Primarily supported for TLX/NR2E1 and some developmental subgroups, not for the whole NR2 family; would over-annotate metabolic and retinal receptors (lewandowski2025comparativeevaluationand pages 3-4, safe2025orphannuclearreceptor pages 33-34, safe2025orphannuclearreceptor pages 17-19) | REMOVE; map only to TLX/NR2E1-specific child entry |


*Table: This table evaluates candidate GO terms that might be considered for InterPro entry PTHR24083 and shows why family-level mapping is mostly inappropriate. It supports the conclusion that the current absence of InterPro2GO mappings is appropriate for this functionally heterogeneous NR2 family.*

The key issue is that while most canonical NR2 members share certain high-level molecular functions (DNA binding, transcription regulation, nuclear localization), these are not universal across the entire PANTHER family match set. Critically, ctenophore NR2 members (which phylogenetically group with NR2A/HNF4) lack the canonical zinc-finger DBD entirely (reitzel2011nuclearreceptorsfrom pages 8-9), making even "DNA binding" and "zinc ion binding" GO terms inappropriate for family-wide mapping. Process-level terms are radically different across subfamilies (metabolism for HNF4, retinoid signaling for RXR, neurogenesis for TLX, photoreceptor development for PNR, angiogenesis/CNS development for COUP-TF) and would massively over-annotate if applied at the family level (lewandowski2025comparativeevaluationand pages 3-4, lewandowski2025comparativeevaluationand pages 4-6).

---

## 3. Functional Divergence Across the Family

The NR2 family exhibits profound functional divergence across its five subgroups, representing one of the most functionally heterogeneous families in the nuclear receptor superfamily:

| Subfamily | Human Members | Ligand Status | Dimerization Mode | Key Biological Processes | Transcriptional Activity | Taxonomic Distribution |
|---|---|---|---|---|---|---|
| NR2A | HNF4A, HNF4G | Endogenous fatty acids reported; linoleic acid, myristic acid/palmitic acid bound in structures; often described as constitutively active despite ligand occupancy (beinsteiner2023structuralinsightsinto pages 1-2, beinsteiner2023structuralinsightsinto pages 2-4, lewandowski2025comparativeevaluationand pages 4-6) | Obligate homodimer; binds DR1 elements (beinsteiner2023structuralinsightsinto pages 2-4, beinsteiner2023structuralinsightsinto pages 5-8, lewandowski2025comparativeevaluationand pages 3-4) | Liver and pancreatic gene regulation, gluconeogenesis, lipid metabolism, epithelial differentiation; HNF4A mutations linked to MODY1 (lewandowski2025comparativeevaluationand pages 3-4, beinsteiner2023structuralinsightsinto pages 1-2) | Primarily activator/constitutive transactivator (lewandowski2025comparativeevaluationand pages 3-4) | Most ancient NR2 lineage; present in ctenophores, sponges, placozoans, cnidarians, bilaterians (reitzel2011nuclearreceptorsfrom pages 8-9, miglioli2021nuclearreceptorsand pages 7-9) |
| NR2B | RXRA, RXRB, RXRG | Ligand-activated; 9-cis retinoic acid is the canonical high-affinity ligand (beinsteiner2023structuralinsightsinto pages 1-2, lewandowski2025comparativeevaluationand pages 3-4) | RXR homodimers and especially heterodimers as the universal NR partner; permissive/conditional/nonpermissive partner behavior depending on partner receptor (lewandowski2025comparativeevaluationand pages 3-4, baldwin2017annotationofthe pages 6-8) | Retinoid signaling, development, metabolism, inflammation; central heterodimerization hub for other NRs (lewandowski2025comparativeevaluationand pages 3-4, miglioli2021nuclearreceptorsand pages 4-6) | Context-dependent co-activator or co-repressor platform; usually activation-capable in permissive heterodimers (lewandowski2025comparativeevaluationand pages 3-4, weikum2018thenuclearreceptor pages 46-56) | Ancient metazoan distribution, emerging after ancestral HNF4-like receptors; present broadly from cnidarians through vertebrates, with lineage-specific expansions/losses (reitzel2011nuclearreceptorsfrom pages 8-9, baldwin2017annotationofthe pages 6-8) |
| NR2C | NR2C1 (TR2), NR2C2 (TR4) | Mostly orphan; validated physiological ligands remain unclear/limited (lewandowski2025comparativeevaluationand pages 3-4) | Dimerizing orphan receptors; can act in homo/heteromeric contexts; share autorepressed structural features with NR2E (lewandowski2025comparativeevaluationand pages 3-4) | Metabolism, bone physiology, reproduction, neuronal development (lewandowski2025comparativeevaluationand pages 3-4) | Often repressive or context-dependent regulators, though not uniformly repressive in all settings (lewandowski2025comparativeevaluationand pages 3-4) | Broad bilaterian/metazoan NR2 distribution, but less clearly ancestral than NR2A; represented within major animal clades sampled for NR2 evolution (miglioli2021nuclearreceptorsand pages 7-9, reitzel2011nuclearreceptorsfrom pages 5-8) |
| NR2E | NR2E1 (TLX), NR2E3 (PNR/photoreceptor-specific nuclear receptor) | Orphan; no definitive universal endogenous ligand established (lewandowski2025comparativeevaluationand pages 3-4, lewandowski2025comparativeevaluationand pages 4-6, safe2025orphannuclearreceptor pages 17-19) | Autorepressed LBD architecture; recruit corepressors such as atrophin, HDACs, LSD1; function in repressive complexes (lewandowski2025comparativeevaluationand pages 3-4, safe2025orphannuclearreceptor pages 33-34, safe2025orphannuclearreceptor pages 17-19) | Neural stem cell self-renewal and neurogenesis (TLX); retinal photoreceptor development and rod/cone fate specification (NR2E3) (lewandowski2025comparativeevaluationand pages 4-6, lewandowski2025comparativeevaluationand pages 20-21, safe2025orphannuclearreceptor pages 17-19) | Predominantly repressor; TLX represses transcription via corepressors, whereas NR2E3 can repress cone genes and activate rod programs (safe2025orphannuclearreceptor pages 33-34, safe2025orphannuclearreceptor pages 17-19) | Present in early-diverging metazoans and bilaterians; part of the ancient developmental NR2 set seen across cnidarians and other animal lineages (miglioli2021nuclearreceptorsand pages 7-9, reitzel2011nuclearreceptorsfrom pages 5-8) |
| NR2F | NR2F1 (COUP-TFI), NR2F2 (COUP-TFII), NR2F6 (EAR2/COUP-TFIII) | Historically orphan; COUP-TFII can be activated by retinoic acids at relatively high concentrations (kruse2008identificationofcouptfii pages 8-11, kruse2008identificationofcouptfii pages 1-2) | Homo/heterodimerization; autorepressed conformation with helix α10 and AF2 blocking ligand/cofactor sites in COUP-TFII structure (kruse2008identificationofcouptfii pages 8-11, kruse2008identificationofcouptfii pages 1-2) | CNS development, angiogenesis, cell fate specification, metabolism, immune/T-cell differentiation (lewandowski2025comparativeevaluationand pages 4-6, lewandowski2025comparativeevaluationand pages 3-4) | Frequently repressive/transrepressive, though can show constitutive activity and ligand-potentiated activation in some contexts (kruse2008identificationofcouptfii pages 8-11, kruse2008identificationofcouptfii pages 1-2, lewandowski2025comparativeevaluationand pages 3-4) | Broad metazoan distribution; COUP-TF/SVP-like receptors are part of the basic ancient NR2 developmental repertoire across cnidarians and bilaterians (miglioli2021nuclearreceptorsand pages 7-9, reitzel2011nuclearreceptorsfrom pages 5-8) |


*Table: This table compares the major NR2 subfamilies by members, ligand status, dimerization, biology, regulatory mode, and taxonomic breadth. It is useful for assessing why the InterPro NR2 family is functionally heterogeneous and unsuitable for broad GO mapping.*

### Key Divergences

**Dimerization modes are incompatible across subfamilies.** HNF4 (NR2A) is an obligate homodimer that cannot heterodimerize with RXR due to the absence of key class I markers (Trp40, Arg105) (beinsteiner2023structuralinsightsinto pages 2-4). In contrast, RXR (NR2B) is the universal heterodimer partner for numerous non-NR2 nuclear receptors, functioning as a permissive, conditional, or nonpermissive partner depending on its binding partner (lewandowski2025comparativeevaluationand pages 3-4). COUP-TF members can form both homodimers and heterodimers (kruse2008identificationofcouptfii pages 8-11).

**Transcriptional activity is opposing.** HNF4 functions primarily as a constitutive transcriptional activator in liver and pancreas (lewandowski2025comparativeevaluationand pages 3-4). TLX (NR2E1) functions predominantly as a transcriptional repressor, recruiting HDACs, LSD1, and atrophin corepressors to maintain neural stem cell proliferation (safe2025orphannuclearreceptor pages 33-34, safe2025orphannuclearreceptor pages 17-19). COUP-TFII can function as both a repressor (through its autorepressed conformation blocking coactivator access) and an activator (when released from autoinhibition by retinoic acid) (kruse2008identificationofcouptfii pages 8-11, kruse2008identificationofcouptfii pages 1-2).

**Ligand specificity varies dramatically.** RXR binds 9-cis-retinoic acid as its canonical ligand (beinsteiner2023structuralinsightsinto pages 1-2). HNF4 co-crystallizes with fatty acids such as linoleic acid and myristic acid, though whether these are regulatory ligands or structural cofactors remains debated (beinsteiner2023structuralinsightsinto pages 1-2, beinsteiner2023structuralinsightsinto pages 2-4). Most NR2C, NR2E, and NR2F members remain classified as orphan receptors with no validated endogenous ligands, though COUP-TFII can be activated by retinoic acids at supraphysiological concentrations (kruse2008identificationofcouptfii pages 8-11, lewandowski2025comparativeevaluationand pages 3-4).

**Biological processes are non-overlapping.** NR2A regulates gluconeogenesis and lipid metabolism; NR2B mediates retinoid signaling and serves as a heterodimerization hub; NR2C regulates metabolism, bone physiology, and reproduction; NR2E1 maintains neural stem cell self-renewal; NR2E3 specifies rod vs. cone photoreceptor fate; NR2F members regulate angiogenesis, CNS development, and immune cell differentiation (lewandowski2025comparativeevaluationand pages 3-4, lewandowski2025comparativeevaluationand pages 4-6, lewandowski2025comparativeevaluationand pages 20-21, safe2025orphannuclearreceptor pages 17-19).

**There are no catalytically dead/pseudo-enzyme members** in the conventional sense, as NR2 members are transcription factors rather than enzymes. However, ctenophore NR2 proteins that lack the DBD represent a structural degeneracy analogous to pseudoenzymes—they retain the LBD fold but have lost canonical DNA-binding capacity (reitzel2011nuclearreceptorsfrom pages 8-9).

---

## 4. Taxonomic Scope

The NR2 family has the broadest and most ancient distribution of any nuclear receptor subfamily. NR2A (HNF4) is considered the closest extant relative of the ancestral nuclear receptor (miglioli2021nuclearreceptorsand pages 7-9). The evolutionary distribution includes:

- **Ctenophores (e.g., *Mnemiopsis leidyi*):** Possess NR2A-like receptors that lack the canonical DBD, representing either the ancestral condition or lineage-specific loss. These are the least diverse NR complement of any animal phylum, with representatives clustering only with NR2A (reitzel2011nuclearreceptorsfrom pages 8-9).
- **Sponges (Porifera):** Contain subfamily II NRs that may represent structures closest to the initial ancestral receptors (saez2010nuclearreceptorgenes pages 3-5).
- **Placozoans (*Trichoplax*):** Show partial radiation of NR family 2, suggesting NR2 diversification was underway at this early branch point (reitzel2011nuclearreceptorsfrom pages 8-9).
- **Cnidarians:** Anthozoans contain representatives of four of five NR2 subfamilies (NR2A, NR2C/D, NR2E, NR2F), though RXR (NR2B) orthologs were not identified in anthozoans. Hydrozoans possess HNF4 and NR2E subfamily members (reitzel2011nuclearreceptorsfrom pages 5-8).
- **Protostomes:** Insects, mollusks, and flatworms all possess NR2 members, with lineage-specific expansions (e.g., COUP-TF expansion in fish; NR2 expansion in flatworms) (baldwin2017annotationofthe pages 6-8, miglioli2021nuclearreceptorsand pages 4-6).
- **Deuterostomes/Vertebrates:** Full complement of NR2A-F subfamilies with paralog expansion (e.g., three RXR subtypes, two HNF4 subtypes in mammals) (lewandowski2025comparativeevaluationand pages 3-4).

The step-wise diversification of NR2 occurred with initial radiations in NR family 2, followed by NR families 3, 6, and 1/4 originating prior to the bilaterian ancestor (reitzel2011nuclearreceptorsfrom pages 8-9). This means no process-level GO term can safely hold across the full taxonomic breadth of this signature, as functions have been extensively exapted (repurposed) across animal evolution (bodofsky2017conservedandexapted pages 26-27, miglioli2021nuclearreceptorsand pages 7-9).

---

## 5. Over-Annotation Verdict and Recommendations

### Summary Assessment

The current state of PTHR24083 — **no InterPro2GO terms mapped** — is **sound and appropriate**. This entry represents a functionally heterogeneous family-level signature that encompasses five major subgroups with:

1. **Radically different ligand specificities** (fatty acids, retinoids, orphan status)
2. **Incompatible dimerization modes** (obligate homodimer vs. universal heterodimer partner vs. autorepressed)
3. **Opposing transcriptional activities** (constitutive activator vs. dedicated repressor)
4. **Non-overlapping biological processes** (liver metabolism vs. neurogenesis vs. photoreceptor specification vs. angiogenesis)
5. **Structural degeneracy** in early-diverging lineages (ctenophore NR2 members lacking the DBD)

### Recommended GO Action Pattern

| Action | Rationale |
|--------|-----------|
| **ACCEPT** (current no-mapping state) | The absence of InterPro2GO terms for PTHR24083 correctly reflects the functional heterogeneity of the NR2 family. Any family-wide GO term would over-annotate significant fractions of the 26,277 matched proteins. |

### Recommendations for InterPro

- **Do not add family-level GO terms** to PTHR24083. Even the most generic molecular function terms (e.g., DNA binding, zinc ion binding) are not universal due to DBD loss in ctenophore members.
- **GO terms should be mapped at the child/subfamily level** (i.e., to the 52 subfamilies within PTHR24083). Subfamily-specific terms such as "retinoid X receptor activity" for NR2B, "fatty acid binding" for NR2A, "negative regulation of transcription" for NR2E1, and "photoreceptor cell differentiation" for NR2E3 would be appropriate at their respective child entries.
- If any GO term were to be considered at the parent level, only `GO:0140110` (transcription regulator activity) might be defensible as a **NON_CORE** annotation, but this carries minimal informational value and risks false positives for divergent members.
- The family's 52 subfamilies in InterPro provide a natural hierarchy for pushing function-specific GO annotations to appropriate granularity levels, which is the recommended approach.

References

1. (lewandowski2025comparativeevaluationand pages 3-4): Max Lewandowski, Romy Busch, Julian A. Marschner, and Daniel Merk. Comparative evaluation and profiling of chemical tools for the nuclear hormone receptor family 2. ACS pharmacology & translational science, 8:854-870, Feb 2025. URL: https://doi.org/10.1021/acsptsci.4c00719, doi:10.1021/acsptsci.4c00719. This article has 9 citations and is from a peer-reviewed journal.

2. (lewandowski2025comparativeevaluationand pages 1-3): Max Lewandowski, Romy Busch, Julian A. Marschner, and Daniel Merk. Comparative evaluation and profiling of chemical tools for the nuclear hormone receptor family 2. ACS pharmacology & translational science, 8:854-870, Feb 2025. URL: https://doi.org/10.1021/acsptsci.4c00719, doi:10.1021/acsptsci.4c00719. This article has 9 citations and is from a peer-reviewed journal.

3. (weikum2018thenuclearreceptor pages 41-46): Emily R. Weikum, Xu Liu, and Eric A. Ortlund. The nuclear receptor superfamily: a structural perspective. Protein Science, 27:1876-1892, Oct 2018. URL: https://doi.org/10.1002/pro.3496, doi:10.1002/pro.3496. This article has 695 citations and is from a peer-reviewed journal.

4. (weikum2018thenuclearreceptor pages 5-9): Emily R. Weikum, Xu Liu, and Eric A. Ortlund. The nuclear receptor superfamily: a structural perspective. Protein Science, 27:1876-1892, Oct 2018. URL: https://doi.org/10.1002/pro.3496, doi:10.1002/pro.3496. This article has 695 citations and is from a peer-reviewed journal.

5. (folkertsma2005thenuclearreceptor pages 53-57): Simon Folkertsma, Paula Noort, Ralph Brandt, Emmanuel Bettler, Gerrit Vriend, and Jacob Vlieg. The nuclear receptor ligand-binding domain: a family-based structure analysis. Current medicinal chemistry, 12 9:1001-16, May 2005. URL: https://doi.org/10.2174/0929867053764699, doi:10.2174/0929867053764699. This article has 30 citations and is from a peer-reviewed journal.

6. (folkertsma2005thenuclearreceptor pages 27-31): Simon Folkertsma, Paula Noort, Ralph Brandt, Emmanuel Bettler, Gerrit Vriend, and Jacob Vlieg. The nuclear receptor ligand-binding domain: a family-based structure analysis. Current medicinal chemistry, 12 9:1001-16, May 2005. URL: https://doi.org/10.2174/0929867053764699, doi:10.2174/0929867053764699. This article has 30 citations and is from a peer-reviewed journal.

7. (owen2000originsandevolutionary pages 2-3): G. I. Owen and A. Zelent *. Origins and evolutionary diversification of the nuclear receptor superfamily. May 2000. URL: https://doi.org/10.1007/s000180050043, doi:10.1007/s000180050043. This article has 198 citations.

8. (beinsteiner2023structuralinsightsinto pages 2-4): Brice Beinsteiner, Isabelle M. L. Billas, and Dino Moras. Structural insights into the hnf4 biology. Frontiers in Endocrinology, Jun 2023. URL: https://doi.org/10.3389/fendo.2023.1197063, doi:10.3389/fendo.2023.1197063. This article has 26 citations.

9. (beinsteiner2023structuralinsightsinto pages 5-8): Brice Beinsteiner, Isabelle M. L. Billas, and Dino Moras. Structural insights into the hnf4 biology. Frontiers in Endocrinology, Jun 2023. URL: https://doi.org/10.3389/fendo.2023.1197063, doi:10.3389/fendo.2023.1197063. This article has 26 citations.

10. (kruse2008identificationofcouptfii pages 8-11): Schoen W Kruse, Kelly Suino-Powell, X. Edward Zhou, Jennifer E Kretschman, Ross Reynolds, Clemens Vonrhein, Yong Xu, Liliang Wang, Sophia Y Tsai, Ming-Jer Tsai, and H. Eric Xu. Identification of coup-tfii orphan nuclear receptor as a retinoic acid–activated receptor. PLoS Biology, 6:e227, Sep 2008. URL: https://doi.org/10.1371/journal.pbio.0060227, doi:10.1371/journal.pbio.0060227. This article has 254 citations and is from a highest quality peer-reviewed journal.

11. (kruse2008identificationofcouptfii pages 1-2): Schoen W Kruse, Kelly Suino-Powell, X. Edward Zhou, Jennifer E Kretschman, Ross Reynolds, Clemens Vonrhein, Yong Xu, Liliang Wang, Sophia Y Tsai, Ming-Jer Tsai, and H. Eric Xu. Identification of coup-tfii orphan nuclear receptor as a retinoic acid–activated receptor. PLoS Biology, 6:e227, Sep 2008. URL: https://doi.org/10.1371/journal.pbio.0060227, doi:10.1371/journal.pbio.0060227. This article has 254 citations and is from a highest quality peer-reviewed journal.

12. (reitzel2011nuclearreceptorsfrom pages 8-9): Adam M Reitzel, Kevin Pang, Joseph F Ryan, James C Mullikin, Mark Q Martindale, Andreas D Baxevanis, and Ann M Tarrant. Nuclear receptors from the ctenophore mnemiopsis leidyi lack a zinc-finger dna-binding domain: lineage-specific loss or ancestral condition in the emergence of the nuclear receptor superfamily? EvoDevo, 2:3-3, Feb 2011. URL: https://doi.org/10.1186/2041-9139-2-3, doi:10.1186/2041-9139-2-3. This article has 44 citations and is from a peer-reviewed journal.

13. (weikum2018thenuclearreceptor pages 46-56): Emily R. Weikum, Xu Liu, and Eric A. Ortlund. The nuclear receptor superfamily: a structural perspective. Protein Science, 27:1876-1892, Oct 2018. URL: https://doi.org/10.1002/pro.3496, doi:10.1002/pro.3496. This article has 695 citations and is from a peer-reviewed journal.

14. (lewandowski2025comparativeevaluationand pages 4-6): Max Lewandowski, Romy Busch, Julian A. Marschner, and Daniel Merk. Comparative evaluation and profiling of chemical tools for the nuclear hormone receptor family 2. ACS pharmacology & translational science, 8:854-870, Feb 2025. URL: https://doi.org/10.1021/acsptsci.4c00719, doi:10.1021/acsptsci.4c00719. This article has 9 citations and is from a peer-reviewed journal.

15. (beinsteiner2023structuralinsightsinto pages 1-2): Brice Beinsteiner, Isabelle M. L. Billas, and Dino Moras. Structural insights into the hnf4 biology. Frontiers in Endocrinology, Jun 2023. URL: https://doi.org/10.3389/fendo.2023.1197063, doi:10.3389/fendo.2023.1197063. This article has 26 citations.

16. (lewandowski2025comparativeevaluationand pages 20-21): Max Lewandowski, Romy Busch, Julian A. Marschner, and Daniel Merk. Comparative evaluation and profiling of chemical tools for the nuclear hormone receptor family 2. ACS pharmacology & translational science, 8:854-870, Feb 2025. URL: https://doi.org/10.1021/acsptsci.4c00719, doi:10.1021/acsptsci.4c00719. This article has 9 citations and is from a peer-reviewed journal.

17. (safe2025orphannuclearreceptor pages 17-19): Stephen Safe, Arafat R. Oany, Wai Ning Tsui, Miok Lee, Vinod Srivastava, Srijana Upadhyay, Amanuel Hailemariam, Evan Farkas, Sarah Kakwan, Caitrina Kearns, and Gargi Sivaram. Orphan nuclear receptor transcription factors as drug targets. Transcription, 16:224-260, May 2025. URL: https://doi.org/10.1080/21541264.2025.2521766, doi:10.1080/21541264.2025.2521766. This article has 7 citations and is from a peer-reviewed journal.

18. (safe2025orphannuclearreceptor pages 33-34): Stephen Safe, Arafat R. Oany, Wai Ning Tsui, Miok Lee, Vinod Srivastava, Srijana Upadhyay, Amanuel Hailemariam, Evan Farkas, Sarah Kakwan, Caitrina Kearns, and Gargi Sivaram. Orphan nuclear receptor transcription factors as drug targets. Transcription, 16:224-260, May 2025. URL: https://doi.org/10.1080/21541264.2025.2521766, doi:10.1080/21541264.2025.2521766. This article has 7 citations and is from a peer-reviewed journal.

19. (miglioli2021nuclearreceptorsand pages 7-9): Angelica Miglioli, Laura Canesi, Isa D. L. Gomes, Michael Schubert, and Rémi Dumollard. Nuclear receptors and development of marine invertebrates. Genes, 12:83, Jan 2021. URL: https://doi.org/10.3390/genes12010083, doi:10.3390/genes12010083. This article has 40 citations.

20. (baldwin2017annotationofthe pages 6-8): William S. Baldwin, W. Tyler Boswell, Gautam Ginjupalli, and Elizabeth J. Litoff. Annotation of the nuclear receptors in an estuarine fish species, fundulus heteroclitus. Nuclear receptor research, Jan 2017. URL: https://doi.org/10.11131/2017/101285, doi:10.11131/2017/101285. This article has 5 citations and is from a peer-reviewed journal.

21. (miglioli2021nuclearreceptorsand pages 4-6): Angelica Miglioli, Laura Canesi, Isa D. L. Gomes, Michael Schubert, and Rémi Dumollard. Nuclear receptors and development of marine invertebrates. Genes, 12:83, Jan 2021. URL: https://doi.org/10.3390/genes12010083, doi:10.3390/genes12010083. This article has 40 citations.

22. (reitzel2011nuclearreceptorsfrom pages 5-8): Adam M Reitzel, Kevin Pang, Joseph F Ryan, James C Mullikin, Mark Q Martindale, Andreas D Baxevanis, and Ann M Tarrant. Nuclear receptors from the ctenophore mnemiopsis leidyi lack a zinc-finger dna-binding domain: lineage-specific loss or ancestral condition in the emergence of the nuclear receptor superfamily? EvoDevo, 2:3-3, Feb 2011. URL: https://doi.org/10.1186/2041-9139-2-3, doi:10.1186/2041-9139-2-3. This article has 44 citations and is from a peer-reviewed journal.

23. (saez2010nuclearreceptorgenes pages 3-5): Pablo J Sáez, Soledad Lange, Tomas Pérez‐Acle, and Gareth I Owen. Nuclear receptor genes: evolution. ArXiv, Jan 2010. URL: https://doi.org/10.1002/9780470015902.a0006145.pub3, doi:10.1002/9780470015902.a0006145.pub3. This article has 15 citations.

24. (bodofsky2017conservedandexapted pages 26-27): Shari Bodofsky, Francine Koitz, and Bruce Wightman. Conserved and exapted functions of nuclear receptors in animal development. Nuclear receptor research, Jun 2017. URL: https://doi.org/10.11131/2017/101305, doi:10.11131/2017/101305. This article has 33 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](PTHR24083-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](PTHR24083-deep-research-falcon_artifacts/artifact-01.md)

## Citations

1. weikum2018thenuclearreceptor pages 41-46
2. folkertsma2005thenuclearreceptor pages 27-31
3. owen2000originsandevolutionary pages 2-3
4. beinsteiner2023structuralinsightsinto pages 2-4
5. beinsteiner2023structuralinsightsinto pages 5-8
6. lewandowski2025comparativeevaluationand pages 3-4
7. reitzel2011nuclearreceptorsfrom pages 8-9
8. kruse2008identificationofcouptfii pages 8-11
9. beinsteiner2023structuralinsightsinto pages 1-2
10. miglioli2021nuclearreceptorsand pages 7-9
11. saez2010nuclearreceptorgenes pages 3-5
12. reitzel2011nuclearreceptorsfrom pages 5-8
13. lewandowski2025comparativeevaluationand pages 1-3
14. weikum2018thenuclearreceptor pages 5-9
15. folkertsma2005thenuclearreceptor pages 53-57
16. kruse2008identificationofcouptfii pages 1-2
17. weikum2018thenuclearreceptor pages 46-56
18. lewandowski2025comparativeevaluationand pages 4-6
19. lewandowski2025comparativeevaluationand pages 20-21
20. safe2025orphannuclearreceptor pages 17-19
21. safe2025orphannuclearreceptor pages 33-34
22. baldwin2017annotationofthe pages 6-8
23. miglioli2021nuclearreceptorsand pages 4-6
24. bodofsky2017conservedandexapted pages 26-27
25. https://doi.org/10.1021/acsptsci.4c00719,
26. https://doi.org/10.1002/pro.3496,
27. https://doi.org/10.2174/0929867053764699,
28. https://doi.org/10.1007/s000180050043,
29. https://doi.org/10.3389/fendo.2023.1197063,
30. https://doi.org/10.1371/journal.pbio.0060227,
31. https://doi.org/10.1186/2041-9139-2-3,
32. https://doi.org/10.1080/21541264.2025.2521766,
33. https://doi.org/10.3390/genes12010083,
34. https://doi.org/10.11131/2017/101285,
35. https://doi.org/10.1002/9780470015902.a0006145.pub3,
36. https://doi.org/10.11131/2017/101305,